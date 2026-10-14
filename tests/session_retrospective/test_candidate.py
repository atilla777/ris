"""Exercise the packaging checker against isolated complete and damaged installs.

This checks actual file membership/bytes, not retrospective agent judgment.
"""
import contextlib
import io
import json
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / 'tests/session_retrospective/check_candidate.py'


class CandidatePackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='packaging-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for parent in ('skills', '.opencode/skills'):
            for name in ('ris-retrospect-session', 'ris-retrospect-session-base'):
                shutil.copytree(ROOT / parent / name, self.root / parent / name)
        for relative in ('README.md', 'docs/concepts/overview.md',
                         'docs/concepts/ris-sdlc-mvp-skills.md',
                         'docs/rules/architecture/repository.md',
                         'docs/specs/session-retrospective/spec.md',
                         'docs/specs/session-retrospective/design.md',
                         'docs/specs/session-retrospective/acceptance.md'):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            # Minimal link-free document; real project links have their own check.
            path.write_text('---\ntype: Specification\n---\n\n# Fixture\n')
        self.checker = self.root / 'tests/session_retrospective/check_candidate.py'
        self.checker.parent.mkdir(parents=True)
        shutil.copyfile(CHECKER, self.checker)

    def check(self):
        output = io.StringIO()
        # Git metadata is not the seam under test; keep this fixture uncommitted.
        with patch('subprocess.check_output', return_value='0' * 40 + '\n'):
            with contextlib.redirect_stdout(output):
                runpy.run_path(str(self.checker), run_name='__main__')
        return json.loads(output.getvalue())

    def test_complete_conditional_package_is_accepted(self):
        result = self.check()
        paths = {entry['path'] for entry in result['files']}
        self.assertIn('skills/ris-retrospect-session/references/langfuse.md', paths)
        self.assertIn('.opencode/skills/ris-retrospect-session/references/save-report.md', paths)

    def test_base_drift_and_incomplete_installs_are_rejected(self):
        # A valid package must pass before faults are introduced, so a stale
        # wrapper membership assertion cannot masquerade as base validation.
        self.check()
        base = self.root / '.opencode/skills/ris-retrospect-session-base'
        path = base / 'references/metrics.md'
        original = path.read_bytes()
        with self.subTest('changed metric semantics'):
            path.write_bytes(original + b'\nchanged measurement contract\n')
            with self.assertRaises(AssertionError):
                self.check()
        path.write_bytes(original)
        with self.subTest('missing installed resource'):
            path.unlink()
            with self.assertRaises(AssertionError):
                self.check()
        path.write_bytes(original)
        with self.subTest('unexpected installed resource'):
            (base / 'references/unowned.md').write_text('unowned instructions\n')
            with self.assertRaises(AssertionError):
                self.check()


if __name__ == '__main__':
    unittest.main()
