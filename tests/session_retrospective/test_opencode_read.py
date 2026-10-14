import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import subprocess
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from contextlib import contextmanager

SCRIPT = Path(__file__).resolve().parents[2] / 'skills/ris-retrospect-session/scripts/opencode_read.py'
spec = importlib.util.spec_from_file_location('reader', SCRIPT)
assert spec is not None and spec.loader is not None
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def fixture(sid='ses_root', parent=None):
    info = {'id': sid, 'projectID': 'proj_one', 'directory': '/safe/project',
            'version': '1.18.33', 'time': {'created': 1000, 'updated': 9000}}
    if parent:
        info['parentID'] = parent
    return {'info': info, 'messages': [{'info': {'id': 'msg_one', 'sessionID': sid,
            'role': 'assistant', 'time': {'created': 1000, 'completed': 9000}},
            'parts': [{'id': 'prt_one', 'sessionID': sid, 'messageID': 'msg_one',
                       'type': 'text', 'text': 'first middle last'}]}]}


def deep_export(sid='ses_root', levels=1100):
    f = fixture(sid)
    f['messages'][0]['parts'][0]['metadata'] = {'payload': 'depth-marker'}
    return json.dumps(f).replace('"depth-marker"', '[' * levels + '"CANARYPRIVATE"' + ']' * levels)


def deep_value(levels=1100):
    value = 'CANARYPRIVATE'
    for _ in range(levels):
        value = [value]
    return value


@contextmanager
def endpoint(responses):
    calls = []
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = self.path.split('?', 1)[0]; calls.append(path)
            body = responses.get(path)
            self.send_response(200 if body is not None else 404)
            self.end_headers()
            self.wfile.write(body.encode() if body is not None else b'{}')
        def log_message(self, format, *args):
            pass
    server = HTTPServer(('127.0.0.1', 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
    try:
        yield f'http://127.0.0.1:{server.server_port}', calls
    finally:
        server.shutdown(); server.server_close(); thread.join()


class Identity(unittest.TestCase):
    def test_wrong_session_is_not_success(self):
        with self.assertRaisesRegex(r.ReadError, 'session mismatch'):
            r.read_export(json.dumps(fixture()), '/safe/project', 'ses_other')

    def test_foreign_project_is_not_success(self):
        with self.assertRaisesRegex(r.ReadError, 'project mismatch'):
            r.read_export(json.dumps(fixture()), '/foreign')

    def test_malformed_has_safe_diagnostic(self):
        with self.assertRaisesRegex(r.ReadError, '^invalid export JSON$'):
            r.read_export('{"secret":"CANARY', '/safe/project')

    def test_duplicate_event_is_rejected(self):
        f = fixture(); f['messages'][0]['parts'] *= 2
        with self.assertRaisesRegex(r.ReadError, 'duplicate'):
            r.read_export(json.dumps(f), '/safe/project')

    def test_identity_and_fingerprint(self):
        a = r.read_export(json.dumps(fixture()), '/safe/project')
        b = r.read_export(json.dumps(fixture(), indent=2), '/safe/project')
        self.assertEqual(a['fingerprint'], b['fingerprint'])
        self.assertEqual(a['session'], 'ses_root')
        self.assertEqual(a['version'], '1.18.33')

    def test_sanitized_needs_exact_independent_project_binding(self):
        f = fixture(); f['info']['directory'] = '[redacted:session-directory:ses_root]'
        args = r.parser().parse_args(['overview', '--project', '/safe/project', '--export', '-'])
        args.project_id = 'proj_one'
        import io
        with patch.object(r.sys, 'stdin', io.StringIO(json.dumps(f))):
            result = r.operate(args)
        self.assertEqual(result['identity']['session'], 'ses_root')
        self.assertTrue(any(g['kind'] == 'redacted-project-directory' for g in result['gaps']))

    def test_boundary_assertion_cannot_override_contradictory_source_time(self):
        with self.assertRaisesRegex(r.ReadError, 'boundary snapshot conflict'):
            r.read_export(json.dumps(fixture()), '/safe/project', cutoff=5000, boundary=True)


class Coverage(unittest.TestCase):
    def test_large_event_and_all_content(self):
        f = fixture(); f['messages'][0]['parts'][0]['text'] = 'FIRST' + 'x' * 19000 + 'LAST'
        s = r.read_export(json.dumps(f), '/safe/project')
        cursor = None; chunks = []
        while True:
            p = r.pages(s, cursor, budget=1000)
            chunks.extend(i['content'] for i in p['items'])
            cursor = p['next']
            if cursor is None:
                break
        combined = ''.join(chunks)
        self.assertIn('FIRST', combined)
        self.assertIn('LAST', combined)
        self.assertGreater(len(chunks), 19)
        self.assertTrue(all(len(c) <= 1000 for c in chunks))

    def test_changed_snapshot_cursor_rejected(self):
        a = fixture(); a['messages'][0]['parts'][0]['text'] *= 1000
        s = r.read_export(json.dumps(a), '/safe/project')
        cursor = r.pages(s, budget=100)['next']
        a['messages'][0]['parts'][0]['text'] += 'changed'
        changed = r.read_export(json.dumps(a), '/safe/project')
        with self.assertRaisesRegex(r.ReadError, 'snapshot conflict'):
            r.pages(changed, cursor, budget=100)

    def test_cursor_cannot_mix_detail_and_pages(self):
        f = fixture(); f['messages'][0]['parts'][0]['text'] *= 1000
        source = r.read_export(json.dumps(f), '/safe/project')
        cursor = r.pages(source, budget=100)['next']
        with self.assertRaisesRegex(r.ReadError, 'snapshot conflict'):
            r.pages(dict(source, view='detail/part'), cursor, budget=100)


class Safety(unittest.TestCase):
    def test_R3_actual_stdin_main_returns_bounded_JSON_not_traceback(self):
        result = subprocess.run([sys.executable, '-B', str(SCRIPT), 'overview', '--project', '/safe/project', '--export', '-'],
                                input=deep_export().encode(), capture_output=True, timeout=10)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stderr, b'')
        error = json.loads(result.stdout)
        self.assertEqual(error, {'status': 'error', 'diagnostic': 'JSON nesting limit exceeded'})
        self.assertNotIn(b'CANARY', result.stdout)

    def test_R3_optional_deep_child_preserves_root_pages(self):
        args = r.parser().parse_args(['pages', '--project', '/safe/project', '--export', 'root', '--child-export', 'child'])
        with patch.object(r, 'read_supplied', side_effect=lambda path: json.dumps(fixture()) if path == 'root' else deep_export('ses_child')):
            result = r.operate(args)
        self.assertEqual(result['identity']['session'], 'ses_root')
        self.assertTrue(any(g['kind'] == 'child-export-invalid' for g in result['gaps']))
        self.assertIn('first middle last', ''.join(i['content'] for i in result['result']['items']))

    def test_R3_GET_deep_messages_have_safe_error(self):
        f = fixture(); messages = deep_export().split('"messages": ', 1)[1][:-1]
        with endpoint({'/session/ses_root': json.dumps(f['info']), '/session/ses_root/message': messages}) as (url, calls):
            args = r.parser().parse_args(['overview', '--project', '/safe/project', '--session', 'ses_root', '--endpoint', url])
            with self.assertRaisesRegex(r.ReadError, '^JSON nesting limit exceeded$'):
                r.operate(args)

    def test_R3_list_depth_is_bounded(self):
        rows = '[{"id":"ses_root","directory":"/safe/project","updated":1,"title":' + '[' * 1100 + '0' + ']' * 1100 + '}]'
        with self.assertRaisesRegex(r.ReadError, '^JSON nesting limit exceeded$'):
            r.list_rows(rows, '/safe/project')

    def test_R3_cursor_depth_is_bounded(self):
        args = r.parser().parse_args(['pages', '--project', '/safe/project', '--export', 'root', '--cursor', '[' * 1100 + '0' + ']' * 1100])
        with patch.object(r, 'read_supplied', return_value=json.dumps(fixture())):
            with self.assertRaisesRegex(r.ReadError, '^JSON nesting limit exceeded$'):
                r.operate(args)

    def test_R3_redaction_depth_is_bounded(self):
        with self.assertRaisesRegex(r.ReadError, '^JSON nesting limit exceeded$'):
            r.safe(deep_value())

    def test_R3_GET_normalization_depth_is_bounded(self):
        f = fixture(); f['messages'][0]['parts'][0]['metadata'] = {'payload': deep_value()}
        args = r.parser().parse_args(['overview', '--project', '/safe/project', '--session', 'ses_root', '--endpoint', 'http://localhost:1'])
        with patch.object(r, 'get_json', side_effect=[f['info'], f['messages']]):
            with self.assertRaisesRegex(r.ReadError, '^JSON nesting limit exceeded$'):
                r.operate(args)

    def test_R3_quotes_do_not_turn_long_string_into_nesting(self):
        f = fixture(); f['messages'][0]['parts'][0]['text'] = '\\"[[[{quoted}]]]' * 1200
        source = r.read_export(json.dumps(f), '/safe/project')
        self.assertEqual(len(source['events']), 2)

    def test_R3_deep_GET_child_preserves_independent_root(self):
        f = fixture(); child = fixture('ses_child', 'ses_root')
        f['messages'][0]['parts'].append({'id': 'prt_task', 'sessionID': 'ses_root', 'messageID': 'msg_one',
                'type': 'tool', 'tool': 'task', 'state': {'metadata': {'sessionId': 'ses_child', 'parentSessionId': 'ses_root'}}})
        messages = deep_export('ses_child').split('"messages": ', 1)[1][:-1]
        responses = {'/session/status': '{}', '/session/ses_root/children': '[]',
                     '/session/ses_child': json.dumps(child['info']), '/session/ses_child/message': messages}
        with endpoint(responses) as (url, calls):
            args = r.parser().parse_args(['pages', '--project', '/safe/project', '--export', 'root', '--endpoint', url])
            with patch.object(r, 'read_supplied', return_value=json.dumps(f)):
                result = r.operate(args)
        self.assertEqual(result['identity']['session'], 'ses_root')
        self.assertTrue(any(g['kind'] == 'child-acquisition-failed' for g in result['gaps']))
        self.assertIn('first middle last', ''.join(i['content'] for i in result['result']['items']))

    def test_R3_normalization_cycles_are_safe_and_moderate_nesting_works(self):
        cycle = []; cycle.append(cycle)
        with self.assertRaisesRegex(r.ReadError, '^JSON nesting limit exceeded$'):
            r.encode_json(cycle)
        source = r.read_export(deep_export(levels=64), '/safe/project')
        page = r.pages(source)
        self.assertNotIn('CANARY', r.encode_json(page))

    def test_secret_safe_content_and_unknown_part_gap(self):
        import io
        f = fixture()
        f['messages'][0]['parts'].append({'id': 'prt_unknown', 'messageID': 'msg_one', 'sessionID': 'ses_root',
             'type': 'future-kind', 'error': 'password=CANARYSECRET', 'secret': 'CANARYKEY'})
        args = r.parser().parse_args(['pages', '--project', '/safe/project', '--export', '-'])
        with patch.object(r.sys, 'stdin', io.StringIO(json.dumps(f))):
            result = r.operate(args)
        self.assertNotIn('CANARY', json.dumps(result))
        self.assertTrue(any(g['kind'] == 'unknown-part-type' for g in result['gaps']))

    def test_invalid_state_is_typed_error(self):
        f = fixture(); f['messages'][0]['parts'][0]['state'] = []
        with self.assertRaisesRegex(r.ReadError, 'unsupported part state'):
            r.read_export(json.dumps(f), '/safe/project')

    def test_invalid_metadata_is_typed_error(self):
        f = fixture(); f['messages'][0]['parts'][0]['state'] = {'metadata': 'not a mapping'}
        with self.assertRaisesRegex(r.ReadError, 'unsupported part metadata'):
            r.read_export(json.dumps(f), '/safe/project')

    def test_duplicate_json_keys_are_typed_error(self):
        with self.assertRaisesRegex(r.ReadError, 'duplicate JSON key'):
            r.read_export('{"info": {}, "info": {}, "messages": []}', '/safe/project')


class SnapshotTree(unittest.TestCase):
    def test_crossing_and_undated_are_late(self):
        self.assertEqual(r.temporal({'time': {'start': 1, 'end': 9}}, 5), 'pending-at-cutoff; late evidence')
        self.assertEqual(r.temporal({'type': 'step-finish'}, 5), 'unknown-at-cutoff; late evidence')
        self.assertEqual(r.temporal({'time': {'start': 1, 'end': 4}}, 5), 'before-cutoff')
        self.assertEqual(r.temporal({'time': {'start': 6, 'end': 9}}, 5), 'after-cutoff')
        self.assertEqual(r.temporal({}, 5, True), 'captured-boundary')

    def test_nested_reused_missing_foreign(self):
        f = fixture()
        part = {'id': 'prt_task', 'messageID': 'msg_one', 'sessionID': 'ses_root',
                'type': 'tool', 'tool': 'task', 'state': {'metadata': {'sessionId': 'ses_child', 'parentSessionId': 'ses_root'}}}
        f['messages'][0]['parts'].append(part)
        f['messages'][0]['parts'].append(dict(part, id='prt_repeat'))
        c = fixture('ses_child', 'ses_root')
        c['messages'][0]['parts'].append(dict(part, id='prt_nested', sessionID='ses_child', state={'metadata': {'sessionId': 'ses_missing', 'parentSessionId': 'ses_child'}}))
        root = r.read_export(json.dumps(f), '/safe/project')
        child = r.read_export(json.dumps(c), '/safe/project')
        tree = r.participants(root, {'ses_child': child})
        self.assertEqual(tree['participants'], ['ses_root', 'ses_child'])
        self.assertTrue(any(g['kind'] == 'missing-child' for g in tree['gaps']))
        c['info']['parentID'] = 'ses_foreign'
        tree = r.participants(root, {'ses_child': r.read_export(json.dumps(c), '/safe/project')})
        self.assertEqual(tree['participants'], ['ses_root'])
        self.assertTrue(any(g['kind'] == 'foreign-parent' for g in tree['gaps']))


class Metrics(unittest.TestCase):
    def conflict_source(self, message_tokens, step_tokens):
        f = fixture(); f['messages'][0]['info']['tokens'] = message_tokens
        for i, tokens in enumerate(step_tokens):
            f['messages'][0]['parts'].append({'id': f'prt_s{i}', 'sessionID': 'ses_root', 'messageID': 'msg_one',
                                            'type': 'step-finish', 'tokens': tokens})
        return r.read_export(json.dumps(f), '/safe/project')

    def test_R4_single_request_conflict_retains_both_and_investigation_signal(self):
        small = {'input': 1, 'cache': {'read': 0, 'write': 0}}
        large = {'input': 160001, 'cache': {'read': 0, 'write': 0}}
        for message, step in [(large, small), (small, large)]:
            with self.subTest(message=message['input']):
                result = r.metrics(self.conflict_source(message, [step]))
                self.assertNotEqual(result['peak_quality'], 'known')
                self.assertIsNone(result['peak'])
                self.assertIsNone(result['context_sum'])
                self.assertEqual(result['conflicting_requests'], 1)
                self.assertEqual(result['known_requests'], 0)
                self.assertTrue(result['threshold_signal'])
                readings = result['requests'][0]['readings']
                self.assertEqual({p['context'] for p in readings}, {1, 160001})
                self.assertEqual({p['provenance'] for p in readings}, {'ses_root/msg_one/prt_s0', 'ses_root/msg_one'})
                self.assertEqual(result['threshold_evidence'][0]['basis'], 'conflicting-reading')

    def test_R4_equal_total_different_cache_components_is_conflict(self):
        message = {'input': 120, 'cache': {'read': 30, 'write': 0}}
        step = {'input': 100, 'cache': {'read': 50, 'write': 0}}
        result = r.metrics(self.conflict_source(message, [step]))
        self.assertNotEqual(result['peak_quality'], 'known')
        self.assertEqual(result['requests'][0]['conflicting_fields'], ['input', 'cache_read'])
        self.assertFalse(result['threshold_signal'])

    def test_R4_partial_conflicting_message_keeps_qualified_lower_bound(self):
        result = r.metrics(self.conflict_source({'input': 160001}, [{'input': 1, 'cache': {'read': 0, 'write': 0}}]))
        self.assertNotEqual(result['peak_quality'], 'known')
        self.assertTrue(result['threshold_signal'])
        evidence = result['threshold_evidence'][0]
        self.assertEqual(evidence['quality'], 'lower-bound')
        self.assertEqual(evidence['context'], 160001)
        self.assertEqual(evidence['basis'], 'conflicting-reading')

    def test_R4_multistep_message_is_not_compared_as_single_request(self):
        result = r.metrics(self.conflict_source({'input': 160001, 'cache': {'read': 0, 'write': 0}},
                       [{'input': 1, 'cache': {'read': 0, 'write': 0}}, {'input': 2, 'cache': {'read': 0, 'write': 0}}]))
        self.assertEqual(result['peak'], 2)
        self.assertEqual(result['context_sum'], 3)
        self.assertFalse(result['threshold_signal'])
        self.assertEqual(result.get('conflicting_requests', 0), 0)

    def test_R4_late_conflict_does_not_trigger_historical_threshold(self):
        source = self.conflict_source({'input': 160001, 'cache': {'read': 0, 'write': 0}},
                                      [{'input': 1, 'cache': {'read': 0, 'write': 0}}])
        result = r.metrics(source, cutoff=5000)
        self.assertFalse(result['threshold_signal'])
        self.assertIsNone(result['context_sum'])
        self.assertEqual(result.get('conflicting_requests'), 1)

    def test_R4_unknown_version_does_not_invent_comparable_context(self):
        source = self.conflict_source({'input': 160001, 'cache': {'read': 0, 'write': 0}},
                                      [{'input': 1, 'cache': {'read': 0, 'write': 0}}])
        source['version'] = 'unknown'
        result = r.metrics(source)
        self.assertIsNone(result['peak'])
        self.assertFalse(result['threshold_signal'])
        self.assertTrue(all(p['context'] is None for p in result['requests'][0]['readings']))

    def test_R4_other_unconflicted_request_remains_known_subset_lower_bound(self):
        first = fixture()
        first['messages'][0]['info']['tokens'] = {'input': 160001, 'cache': {'read': 0, 'write': 0}}
        first['messages'][0]['parts'].append({'id': 'prt_conflict', 'sessionID': 'ses_root', 'messageID': 'msg_one',
                'type': 'step-finish', 'tokens': {'input': 1, 'cache': {'read': 0, 'write': 0}}})
        second = {'info': {'id': 'msg_two', 'sessionID': 'ses_root', 'role': 'assistant'}, 'parts': [
            {'id': 'prt_known', 'sessionID': 'ses_root', 'messageID': 'msg_two', 'type': 'step-finish',
             'tokens': {'input': 10, 'cache': {'read': 0, 'write': 0}}}]}
        first['messages'].append(second)
        result = r.metrics(r.read_export(json.dumps(first), '/safe/project'))
        self.assertEqual(result['peak_quality'], 'conflict')
        self.assertEqual(result['peak_lower_bound'], 10)
        self.assertEqual(result['context_sum'], 10)
        self.assertEqual(result['sums']['input']['value'], 10)
        self.assertEqual(result['known_requests'], 1)
        self.assertTrue(result['threshold_signal'])

    def test_R4_unknown_step_can_use_partial_message_lower_bound(self):
        source = self.conflict_source({'input': 160001}, [{'input': 0, 'cache': {'read': 0, 'write': 0}}])
        result = r.metrics(source)
        self.assertEqual(result['peak_lower_bound'], 160001)
        self.assertEqual(result['peak_quality'], 'lower-bound')
        self.assertTrue(result['threshold_signal'])
        self.assertEqual(result['known_requests'], 1)

    def test_R4_compatible_missing_step_cache_uses_one_message_fallback(self):
        source = self.conflict_source({'input': 1, 'cache': {'read': 160000, 'write': 0}}, [{'input': 1}])
        result = r.metrics(source)
        self.assertEqual(result['peak'], 160001)
        self.assertEqual(result['context_sum'], 160001)
        self.assertEqual(result['conflicting_requests'], 0)
        self.assertTrue(result['threshold_signal'])
        self.assertIn('fallback', result['requests'][0]['provenance'])

    def test_R4_output_conflict_is_not_hidden_by_context_fallback(self):
        source = self.conflict_source({'input': 160001, 'cache': {'read': 0, 'write': 0}, 'output': 1}, [{'output': 50}])
        result = r.metrics(source)
        self.assertNotEqual(result['peak_quality'], 'known')
        self.assertEqual(result['requests'][0]['conflicting_fields'], ['output'])
        self.assertIsNone(result['sums']['output']['value'])
        self.assertTrue(result['threshold_signal'])
        self.assertEqual(result['threshold_evidence'][0]['basis'], 'conflicting-reading')

    def source(self, usages, version='1.18.33'):
        f = fixture(); f['info']['version'] = version
        for i, tokens in enumerate(usages):
            f['messages'][0]['parts'].append({'id': f'prt_step{i}', 'messageID': 'msg_one',
                'sessionID': 'ses_root', 'type': 'step-finish', 'tokens': tokens})
        f['info']['tokens'] = {'input': 9000000}
        # A session aggregate is not a request. Only multi-step messages may
        # carry an uninterpretable summary in this ordinary arithmetic fixture.
        if len(usages) > 1:
            f['messages'][0]['info']['tokens'] = {'input': 9000000}
        return r.read_export(json.dumps(f), '/safe/project')

    def test_threshold_and_no_aggregate_double_count(self):
        a = {'input': 100000, 'cache': {'read': 40000, 'write': 10000}, 'output': 900000, 'reasoning': 50}
        b = dict(a, input=100001)
        s = self.source([a, b])
        m = r.metrics(s)
        self.assertEqual(m['peak'], 150001)
        self.assertEqual(m['context_sum'], 300001)
        self.assertTrue(m['threshold_signal'])
        self.assertFalse(r.metrics(self.source([a]))['threshold_signal'])

    def test_missing_cache_lower_bound_unknown_version_and_default_zero(self):
        m = r.metrics(self.source([{'input': 150001}]))
        self.assertEqual(m['peak_quality'], 'lower-bound')
        self.assertTrue(m['threshold_signal'])
        self.assertIsNone(r.metrics(self.source([{'input': 1}], 'unknown'))['peak'])
        self.assertIsNone(r.metrics(self.source([{'input': 0, 'cache': {'read': 0, 'write': 0}}]))['peak'])

    def test_late_usage_excluded(self):
        s = self.source([{'input': 160000, 'cache': {'read': 0, 'write': 0}}])
        self.assertIsNone(r.metrics(s, cutoff=5000)['peak'])
        self.assertEqual(r.metrics(s, cutoff=5000, boundary=True)['peak'], 160000)

    def test_union_oracles(self):
        self.assertEqual(r.union([(2, 5), (4, 7)]), 5)
        self.assertEqual(r.union([(1, 6), (4, 9)]), 8)
        self.assertEqual(r.union([(1, 9), (2, 4), (10, 12)]), 10)

    def test_historical_late_intervals_excluded(self):
        s = self.source([{'input': 160000, 'cache': {'read': 0, 'write': 0}}])
        self.assertEqual(r.metrics(s, cutoff=5000)['time']['assistant_elapsed_union'], 0)

    def test_conflicting_version_not_silently_overridden(self):
        with self.assertRaisesRegex(r.ReadError, 'version conflict'):
            r.read_export(json.dumps(fixture()), '/safe/project', version='1.19.0')

    def test_single_fallback_no_multistep_guess(self):
        f = fixture(); f['messages'][0]['info']['tokens'] = {'input': 10, 'cache': {'read': 20, 'write': 30}}
        f['messages'][0]['parts'].append({'id': 'prt_step', 'messageID': 'msg_one', 'sessionID': 'ses_root', 'type': 'step-finish'})
        self.assertEqual(r.metrics(r.read_export(json.dumps(f), '/safe/project'))['context_sum'], 60)
        f['messages'][0]['parts'].append(dict(f['messages'][0]['parts'][-1], id='prt_step2'))
        self.assertIsNone(r.metrics(r.read_export(json.dumps(f), '/safe/project'))['context_sum'])

    def test_single_default_step_uses_known_message_fallback_once(self):
        f = fixture()
        f['messages'][0]['info']['tokens'] = {'input': 10, 'cache': {'read': 20, 'write': 30}}
        f['messages'][0]['parts'].append({'id': 'prt_step', 'messageID': 'msg_one', 'sessionID': 'ses_root', 'type': 'step-finish',
                                       'tokens': {'input': 0, 'cache': {'read': 0, 'write': 0}, 'output': 0, 'reasoning': 0}})
        result = r.metrics(r.read_export(json.dumps(f), '/safe/project'))
        self.assertEqual(result['context_sum'], 60)
        self.assertEqual(result['known_requests'], 1)
        self.assertIn('fallback', result['requests'][0]['provenance'])


class Transport(unittest.TestCase):
    def test_R2_GET_identity_duplicates_are_rejected_before_normalization(self):
        f = fixture()
        info = json.dumps(f['info']).replace('"id": "ses_root"', '"id": "ses_foreign", "id": "ses_root"')
        responses = {'/session/ses_root': info, '/session/ses_root/message': json.dumps(f['messages']),
                     '/session/status': '{}', '/session/ses_root/children': '[]'}
        with endpoint(responses) as (url, calls):
            args = r.parser().parse_args(['overview', '--project', '/safe/project', '--session', 'ses_root', '--endpoint', url])
            with self.assertRaisesRegex(r.ReadError, '^duplicate JSON key$'):
                r.operate(args)
        self.assertEqual(calls, ['/session/ses_root'])

    def test_R2_GET_usage_duplicates_are_rejected_through_metrics_operation(self):
        f = fixture()
        f['messages'][0]['parts'].append({'id': 'prt_step', 'sessionID': 'ses_root', 'messageID': 'msg_one',
                'type': 'step-finish', 'tokens': {'input': 1, 'cache': {'read': 0, 'write': 0}}})
        messages = json.dumps(f['messages']).replace('"input": 1', '"input": 160001, "input": 1')
        responses = {'/session/ses_root': json.dumps(f['info']), '/session/ses_root/message': messages,
                     '/session/status': '{}', '/session/ses_root/children': '[]'}
        with endpoint(responses) as (url, calls):
            args = r.parser().parse_args(['metrics', '--project', '/safe/project', '--session', 'ses_root', '--endpoint', url])
            with self.assertRaisesRegex(r.ReadError, '^duplicate JSON key$'):
                r.operate(args)

    def test_R2_list_duplicate_keys_have_secret_safe_errors(self):
        raw = '[{"id":"CANARYPRIVATE","id":"ses_root","directory":"/safe/project","updated":1}]'
        with self.assertRaisesRegex(r.ReadError, '^duplicate JSON key$'):
            r.list_rows(raw, '/safe/project')

    def test_fixed_cli_argv_and_large_memfd(self):
        calls = []
        payload = b'x' * 200000
        def run(argv, **kwargs):
            calls.append((argv, kwargs))
            if argv[-1] == '--version':
                return subprocess.CompletedProcess(argv, 0, b'1.18.33\n', b'')
            target = kwargs['stdout']
            if hasattr(target, 'write'):
                target.write(payload)
                return subprocess.CompletedProcess(argv, 0, None, b'private stderr')
            return subprocess.CompletedProcess(argv, 0, payload, b'private stderr')
        with patch.object(r.subprocess, 'run', side_effect=run):
            self.assertEqual(r.cli_capture('/safe/project', 'export', 'ses_root'), payload)
        self.assertEqual(calls[-1][0], ['opencode', '--pure', 'export', 'ses_root'])
        self.assertFalse(calls[-1][1]['shell'])
        self.assertEqual(calls[-1][1]['cwd'], '/safe/project')

    def test_invalid_cli_never_runs(self):
        with patch.object(r.subprocess, 'run') as run:
            for op, sid in [('serve', None), ('export', 'ses_x;touch /tmp/x'), ('export', None)]:
                with self.assertRaises(r.ReadError):
                    r.cli_capture('/safe/project', op, sid)
            run.assert_not_called()

    def test_list_shape_no_latest_selection(self):
        rows = [{'id': f'ses_r{i}', 'directory': '/safe/project', 'projectId': 'proj_one',
                 'updated': i, 'created': 0, 'title': 'root'} for i in range(9)]
        listed = r.list_rows(json.dumps(rows), '/safe/project')
        self.assertEqual(len(listed), 5)
        self.assertEqual(listed[0]['id'], 'ses_r8')
        self.assertEqual(r.list_rows('', '/safe/project'), [])

    def test_get_scope_and_redirect(self):
        paths = []
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                paths.append(self.path)
                if '/children' in self.path:
                    self.send_response(302); self.send_header('Location', '/mutation'); self.end_headers()
                else:
                    self.send_response(200); self.end_headers(); self.wfile.write(b'{"ok":true}')
            def log_message(self, format, *args):
                pass
        server = HTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
        endpoint = f'http://127.0.0.1:{server.server_port}'
        try:
            self.assertEqual(r.get_json(endpoint, '/safe/project', '/session/ses_root'), {'ok': True})
            with self.assertRaisesRegex(r.ReadError, 'GET failed'):
                r.get_json(endpoint, '/safe/project', '/session/ses_root/children')
            with self.assertRaises(r.ReadError):
                r.get_json(endpoint, '/safe/project', '/session/ses_root/shell')
            self.assertEqual(len(paths), 2)
            self.assertNotIn('/mutation', paths)
            self.assertIn('directory=%2Fsafe%2Fproject', paths[0])
        finally:
            server.shutdown(); server.server_close(); thread.join()


class Application(unittest.TestCase):
    def test_malformed_optional_child_preserves_root_evidence(self):
        args = r.parser().parse_args(['overview', '--project', '/safe/project', '--export', 'root', '--child-export', 'child'])
        with patch.object(r, 'read_supplied', side_effect=lambda path: json.dumps(fixture()) if path == 'root' else '{CANARY'):
            result = r.operate(args)
        self.assertEqual(result['identity']['session'], 'ses_root')
        self.assertTrue(any(g['kind'] == 'child-export-invalid' for g in result['gaps']))

    def test_stdin_pages_metrics_and_overview(self):
        import io
        for op in ('overview', 'pages', 'metrics'):
            args = r.parser().parse_args([op, '--project', '/safe/project', '--export', '-'])
            with patch.object(r.sys, 'stdin', io.StringIO(json.dumps(fixture()))):
                result = r.operate(args)
            self.assertEqual(result['status'], 'partial')
            self.assertEqual(result['identity']['session'], 'ses_root')
            self.assertIn('fingerprint', result['identity'])
            if op == 'pages':
                self.assertIn('first middle last', ''.join(i['content'] for i in result['result']['items']))

    def test_no_source_never_bootstraps(self):
        args = r.parser().parse_args(['overview', '--project', '/safe/project', '--session', 'ses_root'])
        with patch.object(r.subprocess, 'run') as run:
            with self.assertRaisesRegex(r.ReadError, 'source required'):
                r.operate(args)
            run.assert_not_called()

    def test_late_child_remains_readable_separate_from_historical_totals(self):
        root = fixture(); child = fixture('ses_child', 'ses_root')
        root['messages'][0]['parts'].append({'id': 'prt_task', 'messageID': 'msg_one', 'sessionID': 'ses_root',
            'type': 'tool', 'tool': 'task', 'state': {'metadata': {'sessionId': 'ses_child', 'parentSessionId': 'ses_root'}}})
        args = r.parser().parse_args(['pages', '--project', '/safe/project', '--export', 'root',
                '--child-export', 'child', '--cutoff', '5000', '--participant', 'ses_child'])
        with patch.object(r, 'read_supplied', side_effect=lambda path: json.dumps(root if path == 'root' else child)):
            result = r.operate(args)
        self.assertEqual(result['result']['participant_scope'], 'late snapshot evidence only')
        self.assertIn('first middle last', ''.join(i['content'] for i in result['result']['items']))

    def test_boundary_root_does_not_backdate_new_GET_child_usage(self):
        root = fixture(); child = fixture('ses_child', 'ses_root')
        root['info']['time']['updated'] = 5000
        root['messages'][0]['info']['time']['completed'] = 5000
        root['messages'][0]['parts'].append({'id': 'prt_task', 'messageID': 'msg_one', 'sessionID': 'ses_root',
            'type': 'tool', 'tool': 'task', 'state': {'metadata': {'sessionId': 'ses_child', 'parentSessionId': 'ses_root'}}})
        child['messages'][0]['parts'].append({'id': 'prt_step', 'messageID': 'msg_one', 'sessionID': 'ses_child',
            'type': 'step-finish', 'tokens': {'input': 160000, 'cache': {'read': 0, 'write': 0}}})
        args = r.parser().parse_args(['metrics', '--project', '/safe/project', '--export', 'root', '--cutoff', '5000',
                                     '--captured-boundary', '--endpoint', 'http://localhost:1234'])
        def get(endpoint, project, path):
            return {'/session/status': {}, '/session/ses_root/children': [child['info']],
                    '/session/ses_child': child['info'], '/session/ses_child/message': child['messages'],
                    '/session/ses_child/children': []}[path]
        with patch.object(r, 'read_supplied', return_value=json.dumps(root)), patch.object(r, 'get_json', side_effect=get):
            result = r.operate(args)
        self.assertIsNone(result['result']['participants'][1]['peak'])


if __name__ == '__main__':
    unittest.main()
