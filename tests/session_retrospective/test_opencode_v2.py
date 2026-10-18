"""Deterministic reader tests against the pinned V2 public contract, not agents."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch


SCRIPT = (
    Path(__file__).resolve().parents[2]
    / "skills/ris-proj-op-retrospect-session/scripts/opencode_read.py"
)
spec = importlib.util.spec_from_file_location("reader_v2", SCRIPT)
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def fixture(sid="ses_root", parent=None):
    info = {
        "id": sid,
        "projectID": "proj_one",
        "location": {"directory": "/safe/project"},
        "time": {"created": 1000, "updated": 9000},
        "cost": 0,
        "tokens": {
            "input": 9999999,
            "output": 2,
            "reasoning": 0,
            "cache": {"read": 0, "write": 0},
        },
    }
    if parent:
        info["parentID"] = parent
    return {
        "info": info,
        "messages": [
            {
                "id": "msg_user",
                "type": "user",
                "time": {"created": 1000},
                "text": "request",
            },
            {
                "id": "msg_system",
                "type": "system",
                "time": {"created": 1001},
                "text": "historically received instructions",
            },
            {
                "id": "msg_skill",
                "type": "skill",
                "time": {"created": 1002},
                "skill": "test",
                "name": "test",
                "text": "skill body",
            },
            {
                "id": "msg_assistant",
                "type": "assistant",
                "time": {"created": 2000, "streamed": 3000, "completed": 9000},
                "agent": "general",
                "model": {"providerID": "test", "id": "test"},
                "tokens": {
                    "input": 120000,
                    "output": 8,
                    "reasoning": 2,
                    "cache": {"read": 30001, "write": 0},
                },
                "content": [{"type": "text", "text": "first middle last"}],
                "finish": "stop",
            },
            {
                "id": "msg_idle",
                "type": "idle",
                "time": {"created": 9000},
                "outcome": "succeeded",
            },
        ],
    }


def tool(child="ses_child", background=True):
    return {
        "type": "tool",
        "name": "subagent",
        "id": "call:opaque/id-1",
        "executed": False,
        "time": {"created": 3000, "ran": 4000, "completed": 5000},
        "state": {
            "status": "completed",
            "input": {"background": background},
            "metadata": {
                "sessionID": child,
                "status": "running" if background else "completed",
            },
            "content": [{"type": "text", "text": "dispatched"}],
        },
    }


def parse(data, **kwargs):
    return r.read_export(json.dumps(data), "/safe/project", **kwargs)


class V2Reader(unittest.TestCase):
    def test_missing_content_and_malformed_tool_fail_instead_of_disappearing(self):
        f = fixture()
        del f["messages"][3]["content"]
        with self.assertRaisesRegex(r.ReadError, "assistant content"):
            parse(f)
        f = fixture()
        t = tool()
        del t["state"]["content"]
        f["messages"][3]["content"].append(t)
        with self.assertRaisesRegex(r.ReadError, "tool content"):
            parse(f)

    def test_child_project_identity_and_unknown_content_are_not_discarded(self):
        f = fixture()
        f["messages"][3]["content"] += [
            tool(),
            {"type": "future-kind", "payload": "retained"},
        ]
        root = parse(f)
        child_data = fixture("ses_child", "ses_root")
        child_data["info"]["projectID"] = "foreign"
        tree = r.participants(root, {"ses_root": root, "ses_child": parse(child_data)})
        self.assertIn("foreign-project", [g["kind"] for g in tree["gaps"]])
        self.assertEqual(
            json.loads(root["events"][-2]["content"])["payload"], "retained"
        )

    def test_export_envelope_preserves_all_message_kinds_and_opaque_call_ids(self):
        f = fixture()
        f["messages"][3]["content"].append(tool())
        source = parse({"data": f}, version="2.0.32")
        self.assertEqual(source["format"], "v2")
        self.assertEqual(
            [e["type"] for e in source["events"]],
            ["user", "system", "skill", "assistant", "text", "tool", "idle"],
        )
        event = source["events"][5]
        self.assertEqual(event["ref"], "ses_root/msg_assistant/content/1")
        self.assertEqual(json.loads(event["content"])["id"], "call:opaque/id-1")
        self.assertIn(
            "historically received",
            r.pages(source, budget=65536)["items"][1]["content"],
        )

    def test_no_claim_of_source_version_from_v2_schema(self):
        source = parse(fixture())
        self.assertIsNone(source["version"])
        self.assertIsNone(r.metrics(source)["peak"])
        self.assertEqual(r.metrics(source)["semantics"], "unknown version")

    def test_request_peak_is_assistant_usage_not_session_sum(self):
        m = r.metrics(parse(fixture(), version="2.0.32"))
        self.assertEqual(m["peak"], 150001)
        self.assertEqual(m["peak_quality"], "lower-bound")
        self.assertTrue(m["threshold_signal"])
        self.assertEqual(m["enumerated_requests"], 1)
        self.assertEqual(m["context_sum"], 150001)
        self.assertEqual(m["requests"][0]["ref"], "ses_root/msg_assistant")

    def test_zero_unknown_and_future_semantics_not_guessed(self):
        f = fixture()
        f["messages"][3]["tokens"] = {
            "input": 0,
            "output": 0,
            "reasoning": 0,
            "cache": {"read": 0, "write": 0},
        }
        self.assertIsNone(r.metrics(parse(f, version="2.0.32"))["peak"])
        self.assertIsNone(r.metrics(parse(fixture(), version="2.1.0"))["peak"])

    def test_retry_usage_is_not_counted_as_all_attempts(self):
        f = fixture()
        f["messages"][3]["retry"] = {
            "attempt": 2,
            "at": 2001,
            "error": {"type": "test"},
        }
        m = r.metrics(parse(f, version="2.0.32"))
        self.assertEqual(m["context_sum"], 150001)
        self.assertIn("unmeasured-retry-attempts", [g["kind"] for g in m["gaps"]])

    def test_crossing_cutoff_does_not_promote_usage(self):
        source = parse(fixture(), version="2.0.32", cutoff=5000)
        self.assertIsNone(r.metrics(source, cutoff=5000)["peak"])
        self.assertFalse(r.metrics(source, cutoff=5000)["threshold_signal"])
        with self.assertRaisesRegex(r.ReadError, "boundary snapshot conflict"):
            parse(fixture(), version="2.0.32", cutoff=5000, boundary=True)

    def test_identity_sanitization_duplicate_and_foreign_sources(self):
        f = fixture()
        with self.assertRaises(r.SourceConflict):
            parse(f, session="ses_foreign")
        with self.assertRaises(r.SourceConflict):
            parse(f, version="1.18.33")
        f["info"]["location"]["directory"] = "/[redacted:session-directory:ses_root]"
        with self.assertRaises(r.SourceConflict):
            parse(f)
        self.assertEqual(parse(f, project_id="proj_one")["session"], "ses_root")
        with self.assertRaises(r.SourceConflict):
            parse(f, project_id="foreign")
        f = fixture()
        f["messages"].append(copy.deepcopy(f["messages"][0]))
        with self.assertRaisesRegex(r.ReadError, "duplicate message"):
            parse(f)

    def test_subagents_foreground_background_reuse_and_fork(self):
        f = fixture()
        f["messages"][3]["content"] += [
            tool(),
            dict(tool(background=False), id="call-second"),
        ]
        root, child = parse(f), parse(fixture("ses_child", "ses_root"))
        tree = r.participants(
            root,
            {"ses_root": root, "ses_child": child},
            children={"ses_root": ["ses_child"], "ses_child": []},
        )
        self.assertEqual(tree["participants"], ["ses_root", "ses_child"])
        self.assertEqual(tree["gaps"], [])
        self.assertEqual(len(tree["links"]), 1)
        m = r.metrics(root)
        self.assertEqual(m["time"]["parent_task_wait_union"], 1000)
        self.assertEqual(m["time"]["tool_union"], 0)
        child["data"]["info"]["parentID"] = "ses_foreign"
        self.assertIn(
            "foreign-parent",
            [
                g["kind"]
                for g in r.participants(root, {"ses_root": root, "ses_child": child})[
                    "gaps"
                ]
            ],
        )
        child["data"]["info"]["parentID"] = "ses_root"
        child["data"]["info"]["fork"] = {"sessionID": "ses_root"}
        self.assertEqual(
            r.participants(root, {"ses_root": root, "ses_child": child})[
                "participants"
            ],
            ["ses_root"],
        )

    def test_pages_cover_large_content_and_reject_changed_snapshot(self):
        f = fixture()
        f["messages"][3]["content"][0]["text"] = "x" * 100000
        source = parse(f)
        cursor, total = None, 0
        while True:
            page = r.pages(source, cursor, 1000)
            total += sum(len(e["content"]) for e in page["items"])
            cursor = page["next"]
            if cursor is None:
                break
        self.assertEqual(total, sum(len(e["content"]) for e in source["events"]))
        cursor = r.pages(source, budget=1000)["next"]
        f["messages"][0]["text"] += "changed"
        with self.assertRaisesRegex(r.ReadError, "snapshot conflict"):
            r.pages(parse(f), cursor)


class V2Transport(unittest.TestCase):
    def test_no_id_list_keeps_explicit_server(self):
        args = r.parser().parse_args(
            [
                "list",
                "--project",
                "/safe/project",
                "--allow-cli",
                "--endpoint",
                "http://localhost:4096",
            ]
        )
        with patch.object(r, "cli_capture", return_value="[]") as capture:
            result = r.operate(args)
        capture.assert_called_once_with(
            "/safe/project", "list", endpoint="http://localhost:4096"
        )
        self.assertIsNone(result["selected"])

    def test_compaction_request_is_not_session_or_checkpoint_usage(self):
        f = fixture()
        f["messages"].append(
            {
                "type": "compaction",
                "id": "msg_compact",
                "time": {"created": 9500},
                "status": "completed",
                "reason": "manual",
                "summary": "summary",
                "recent": "recent",
                "tokens": {
                    "input": 200000,
                    "output": 10,
                    "reasoning": 0,
                    "cache": {"read": 0, "write": 0},
                },
                "providerContext": {"tokens": 9999999},
            }
        )
        source = parse(f, version="2.0.32")
        metric = r.metrics(source)
        self.assertEqual(metric["enumerated_requests"], 2)
        self.assertEqual(metric["peak"], 200000)
        self.assertEqual(metric["context_sum"], 350001)
        self.assertEqual(
            r.metrics(parse(f, version="2.0.32", cutoff=10000), cutoff=10000)["peak"],
            150001,
        )

    def test_api_failure_does_not_retry_cli_for_linked_children(self):
        f = fixture()
        f["messages"][3]["content"].append(tool())
        calls = []

        def capture(project, operation, session=None, **kwargs):
            calls.append((operation, session))
            if operation == "export":
                raw = r.Captured(json.dumps({"data": f}).encode())
                raw.source_version = "2.0.32"
                return raw
            if session == "/api/info":
                return '{"version":"2.0.32"}'
            raise r.ReadError("CLI read failed")

        args = r.parser().parse_args(
            [
                "overview",
                "--project",
                "/safe/project",
                "--session",
                "ses_root",
                "--allow-cli",
            ]
        )
        with patch.object(r, "cli_capture", side_effect=capture):
            result = r.operate(args)
        self.assertEqual(
            calls,
            [
                ("export", "ses_root"),
                ("api", "/api/info"),
                ("api", "/api/session/active"),
            ],
        )
        self.assertEqual(result["status"], "error")
        self.assertIn("child-acquisition-failed", [g["kind"] for g in result["cause"]])

    def test_recursive_tree_includes_nested_child_only_once(self):
        data = [
            fixture(),
            fixture("ses_child", "ses_root"),
            fixture("ses_nested", "ses_child"),
        ]
        for f, child in zip(data, ["ses_child", "ses_nested"]):
            f["messages"][3]["content"].append(tool(child))
        sources = {f["info"]["id"]: parse(f) for f in data}
        tree = r.participants(
            sources["ses_root"],
            sources,
            children={
                "ses_root": ["ses_child"],
                "ses_child": ["ses_nested"],
                "ses_nested": [],
            },
        )
        self.assertEqual(tree["participants"], ["ses_root", "ses_child", "ses_nested"])
        self.assertEqual(tree["gaps"], [])

    def test_pagination_accumulated_byte_limit(self):
        with (
            patch.object(r, "MAX_BYTES", 20),
            self.assertRaisesRegex(r.ReadError, "byte limit"),
        ):
            r.v2_page_data(
                lambda *args: {
                    "data": [{"id": "ses_a", "text": "long payload"}],
                    "cursor": {},
                },
                "/api/session",
                {},
            )

    def test_body_pagination_keeps_order_and_filters(self):
        calls = []

        def get(path, query):
            calls.append((path, dict(query)))
            if len(calls) == 1:
                return {"data": [{"id": "ses_a"}], "cursor": {"next": "opaque+/="}}
            return {"data": [{"id": "ses_b"}], "cursor": {"next": None}}

        self.assertEqual(
            [
                x["id"]
                for x in r.v2_page_data(get, "/api/session", {"parentID": "ses_root"})
            ],
            ["ses_a", "ses_b"],
        )
        self.assertEqual(
            calls[1][1], {"parentID": "ses_root", "limit": "100", "cursor": "opaque+/="}
        )

    def test_pagination_loops_duplicates_and_missing_envelope_fail(self):
        for value in [
            {"data": [], "cursor": {"next": "loop"}},
            {"data": [{"id": "ses_a"}], "cursor": {"next": "loop"}},
            [],
        ]:
            with self.subTest(value=value), self.assertRaises(r.ReadError):
                r.v2_page_data(lambda *args: value, "/api/session", {})

    def test_fixed_v2_cli_with_explicit_server_and_memory_capture(self):
        calls = []

        def run(argv, **kwargs):
            calls.append(argv)
            if argv[-1] == "--version":
                return subprocess.CompletedProcess(argv, 0, b"opencode v2.0.32\n", b"")
            payload = json.dumps({"data": fixture()}).encode()
            if hasattr(kwargs["stdout"], "write"):
                kwargs["stdout"].write(payload)
                payload = None
            return subprocess.CompletedProcess(argv, 0, payload, b"secret stderr")

        with patch.object(r.subprocess, "run", side_effect=run):
            raw = r.cli_capture(
                "/safe/project", "export", "ses_root", endpoint="http://localhost:4096"
            )
            self.assertEqual(raw.source_version, "2.0.32")
            r.cli_capture(
                "/safe/project",
                "api",
                "/api/session",
                query={"parentID": "ses_root", "cursor": "opaque"},
            )
        self.assertEqual(
            calls[1],
            [
                "opencode",
                "session",
                "export",
                "ses_root",
                "--server",
                "http://localhost:4096",
            ],
        )
        self.assertEqual(
            calls[3],
            [
                "opencode",
                "api",
                "get",
                "/api/session?parentID=ses_root&cursor=opaque",
            ],
        )

    def test_mutations_embedded_auth_and_arbitrary_queries_never_run(self):
        with patch.object(r.subprocess, "run") as run:
            for path, query in [
                ("/api/session/ses_root/shell", {}),
                ("/api/fs/read", {}),
                ("/api/session", {"delete": "true"}),
            ]:
                with self.assertRaises(r.ReadError):
                    r.cli_capture("/safe/project", "api", path, query=query)
            run.assert_not_called()
        for endpoint in [
            "http://user:secret@localhost",
            "http://localhost/path",
            "file:///tmp/anything",
        ]:
            with self.assertRaises(r.ReadError):
                r.validate_endpoint(endpoint)

    def test_endpoint_messages_and_children_are_recursively_paginated(self):
        root, child = fixture(), fixture("ses_child", "ses_root")
        calls = []

        def get(endpoint, project, path, **kwargs):
            query = kwargs.get("query") or {}
            calls.append((path, dict(query)))
            if path == "/api/session/active":
                return {"data": {}}
            if path == "/api/session":
                return {
                    "data": [child["info"]] if query["parentID"] == "ses_root" else [],
                    "cursor": {},
                }
            data = child if "ses_child" in path else root
            if path.endswith("/message"):
                if "cursor" not in query:
                    return {"data": data["messages"][:2], "cursor": {"next": "next"}}
                return {"data": data["messages"][2:], "cursor": {}}
            return {"data": data["info"]}

        args = r.parser().parse_args(
            [
                "metrics",
                "--project",
                "/safe/project",
                "--session",
                "ses_root",
                "--version",
                "2.0.32",
                "--endpoint",
                "http://localhost:4096",
            ]
        )
        with patch.object(r, "get_json", side_effect=get):
            result = r.operate(args)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(len(result["result"]["participants"]), 2)
        self.assertEqual(sum(p.endswith("/message") for p, _ in calls), 4)

    def test_v2_cli_source_version_comes_from_server(self):
        f = fixture()
        calls = []

        def capture(project, operation, session=None, **kwargs):
            calls.append((operation, session))
            if operation == "export":
                raw = r.Captured(json.dumps({"data": f}).encode())
                raw.source_version = "2.0.32"
                return raw
            return json.dumps(
                {"version": "2.1.0"}
                if session == "/api/info"
                else {"data": [], "cursor": {}}
                if session == "/api/session"
                else {"data": {}}
            )

        args = r.parser().parse_args(
            [
                "metrics",
                "--project",
                "/safe/project",
                "--session",
                "ses_root",
                "--allow-cli",
            ]
        )
        with patch.object(r, "cli_capture", side_effect=capture):
            result = r.operate(args)
        self.assertEqual(result["identity"]["version"], "2.1.0")
        self.assertIsNone(result["result"]["participants"][0]["peak"])
        self.assertIn(("api", "/api/info"), calls)


if __name__ == "__main__":
    unittest.main()
