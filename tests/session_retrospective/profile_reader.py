"""Deterministic long-history profile; no collection or persistent fixtures."""
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time

path = Path(__file__).resolve().parents[2] / 'skills/ris-retrospect-session/scripts/opencode_read.py'
spec = importlib.util.spec_from_file_location('reader', path)
assert spec and spec.loader
reader = importlib.util.module_from_spec(spec); spec.loader.exec_module(reader)
count = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
sid = 'ses_profile'
data = {'info': {'id': sid, 'directory': '/safe/project', 'version': '1.18.33'}, 'messages': []}
for i in range(count):
    mid = f'msg_p{i}'
    data['messages'].append({'info': {'id': mid, 'sessionID': sid, 'role': 'user'},
                            'parts': [{'id': f'prt_p{i}', 'messageID': mid, 'sessionID': sid,
                                       'type': 'text', 'text': f'FIRST {i} ' + 'content ' * 1000 + ' LAST'}]})
raw = json.dumps(data).encode()
start = time.monotonic()
source = reader.read_export(raw, '/safe/project')
cursor = None; pages = returned = 0
while True:
    page = reader.pages(source, cursor, 8192)
    pages += 1; returned += sum(len(i['content']) for i in page['items'])
    cursor = page['next']
    if cursor is None: break
assert returned == sum(len(e['content']) for e in source['events'])
print(json.dumps({'messages': count, 'events': len(source['events']), 'source_bytes': len(raw),
                  'content_bytes': returned, 'pages': pages, 'acquisitions': 1,
                  'seconds': time.monotonic() - start, 'maxrss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}))
