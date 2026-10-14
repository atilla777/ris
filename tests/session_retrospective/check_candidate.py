"""Scoped parity/link manifest, not a full tree or semantic acceptance check.

OKF rules remain the pinned specification. Run without Python bytecode writes.
"""
import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

root = Path(__file__).resolve().parents[2]
source = root / 'skills/ris-retrospect-session'
installed = root / '.opencode/skills/ris-retrospect-session'
files = [root / p for p in ('README.md', 'docs/concepts/overview.md', 'docs/concepts/ris-sdlc-mvp-skills.md', 'docs/rules/architecture/repository.md',
                           'docs/specs/session-retrospective/spec.md', 'docs/specs/session-retrospective/design.md',
                           'docs/specs/session-retrospective/acceptance.md')]
for owner in (source, installed):
    assert owner.is_dir()
    resources = sorted(p for p in owner.rglob('*') if p.is_file())
    assert {str(p.relative_to(owner)) for p in resources} == {
        'SKILL.md', 'references/opencode.md', 'references/langfuse.md',
        'references/delegation.md', 'references/save-report.md', 'scripts/opencode_read.py'}
    files.extend(resources)
    text = (owner / 'SKILL.md').read_text()
    assert text.startswith('---\nname: ris-retrospect-session\ndescription: >-\n')
    assert len(text.split('---', 2)[1].split('description:', 1)[1]) <= 1024
    assert '/home/aleksei/' not in text
    ast.parse((owner / 'scripts/opencode_read.py').read_text())
    for p in resources:
        assert not p.is_symlink()
        assert p.resolve().is_relative_to(root.resolve())
        assert p.read_bytes() == (source / p.relative_to(owner)).read_bytes()
base_source = root / 'skills/ris-retrospect-session-base'
for owner in (base_source, root / '.opencode/skills/ris-retrospect-session-base'):
    assert owner.is_dir()
    resources = sorted(p for p in owner.rglob('*') if p.is_file())
    assert {str(p.relative_to(owner)) for p in resources} == {
        'SKILL.md', 'references/analysis.md', 'references/metrics.md', 'references/report.md'}
    for p in resources:
        assert not p.is_symlink()
        assert p.resolve().is_relative_to(root.resolve())
        assert p.read_bytes() == (base_source / p.relative_to(owner)).read_bytes()
    files.extend(resources)
files.extend(sorted((root / 'tests/session_retrospective').glob('*.py')))
for p in files:
    if p.suffix != '.md':
        ast.parse(p.read_text()); continue
    if str(p.relative_to(root)).startswith(('docs/concepts/', 'docs/rules/')):
        assert re.match(r'^---\ntype: [^\n]+\n---\n', p.read_text())
    for address in re.findall(r'\[[^\]]*\]\(([^)]+)\)', p.read_text()):
        address = unquote(address.split('#', 1)[0])
        if not address or re.match(r'[a-z]+:', address): continue
        target = p.parent / address
        assert target.exists(), (p.relative_to(root), address)
base = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
entries = [{'path': str(p.relative_to(root)), 'mode': oct(p.stat().st_mode & 0o777),
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(set(files))]
payload = {'base': base, 'files': entries}
identity = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
print(json.dumps({'snapshot_sha256': identity, **payload,
                  'source_skills': len(list((root / 'skills').glob('ris-*/SKILL.md'))),
                  'installed_RIS_skills': len(list((root / '.opencode/skills').glob('ris-*/SKILL.md')))}, indent=2))
