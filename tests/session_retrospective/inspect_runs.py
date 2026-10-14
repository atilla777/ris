"""Evidence extraction from actual host runs, not an LLM substitute."""
import json
from pathlib import Path
import shlex

root = Path('/tmp/opencode/ris-01r-22-verification/logs')
for case in sorted(root.iterdir()):
    if not (case / 'calls.json').exists(): continue
    calls = json.loads((case / 'calls.json').read_text())
    summary = json.loads((case / 'summary.json').read_text())
    selected = []; resources = []; actions = []; forbidden = []
    for call in calls:
        tool = call['tool']; state = call['state']; args = state.get('input', {})
        if tool == 'skill': selected.append(args.get('name'))
        elif tool == 'read': resources.append(args.get('filePath'))
        elif tool == 'bash':
            command = args.get('command', '')
            words = shlex.split(command)
            if len(words) < 4 or words[:2] != ['python3', '-B'] or not words[2].endswith('/scripts/opencode_read.py') or any(x in command for x in (';', '&&', '|', '>', '$(', '`')):
                forbidden.append({'tool': tool, 'command': command})
            actions.append({'operation': words[3] if len(words) > 3 else '?', 'state': state['status'],
                            'participant': words[words.index('--participant') + 1] if '--participant' in words else 'root'})
        elif tool not in ('glob', 'grep', 'list'):
            forbidden.append({'tool': tool})
    report = (case / 'response.md').read_text()
    print(json.dumps({'case': case.name, 'session': summary['session'], 'unchanged': summary['fixture_unchanged'],
                      'write_events': len(summary['writes']), 'secret_absent': summary['secret_absent'],
                      'selected': selected, 'resources': resources, 'reader_actions': actions, 'forbidden_attempts': forbidden,
                      'seven_sections': all(f'## {i}.' in report for i in range(1, 8))}, ensure_ascii=True))
