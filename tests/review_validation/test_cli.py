"""Actual CLI checks in disposable directories without Git/Beads/network tools."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from contextlib import redirect_stderr
from io import StringIO
from test_validate_review import EXAMPLE, SKILL, validator


class CLITests(unittest.TestCase):
    def test_incompatible_setup_is_separate_error(self):
        for patches in (
            {"version": lambda name: "0.0.0"},
            {"sys.version_info": (3, 9)},
        ):
            error = StringIO()
            target, value = next(iter(patches.items()))
            if target == "version":
                context = patch.object(validator, target, value)
            else:
                context = patch.object(validator.sys, "version_info", value)
            with context, redirect_stderr(error):
                self.assertEqual(3, validator.main(["unread.yaml"]))
            self.assertIn("error", error.getvalue())

    def test_installed_relative_read_only_and_exits(self):
        with tempfile.TemporaryDirectory(
            prefix="ris-7qq-", dir="/tmp/opencode"
        ) as temp:
            root = Path(temp)
            installed = root / "installed-skill"
            shutil.copytree(SKILL, installed)
            script = installed / "scripts/validate_review.py"
            report = root / "report.yaml"
            env = dict(os.environ, PATH="", PYTHONDONTWRITEBYTECODE="1")
            for text, code, message in (
                (EXAMPLE, 0, "valid"),
                (EXAMPLE + "passed: true\n", 1, "invalid"),
                (EXAMPLE.replace("ris.review/1", "ris.review/99"), 2, "unsupported"),
                (EXAMPLE.replace("required: true", 'required: "true"'), 1, "required"),
                (EXAMPLE + "\n---\nfoo: bar\n", 1, "YAML"),
            ):
                report.write_text(text, encoding="utf-8")
                before = {
                    p.relative_to(root): p.read_bytes()
                    for p in root.rglob("*")
                    if p.is_file()
                }
                result = subprocess.run(
                    [sys.executable, "-B", str(script), str(report)],
                    cwd=root,
                    env=env,
                    text=True,
                    capture_output=True,
                )
                with self.subTest(code=code, message=message):
                    self.assertEqual(code, result.returncode, result.stderr)
                    self.assertIn(message, result.stdout + result.stderr)
                    after = {
                        p.relative_to(root): p.read_bytes()
                        for p in root.rglob("*")
                        if p.is_file()
                    }
                    self.assertEqual(before, after)
            for args in (
                [],
                [str(root / "missing.yaml")],
                [str(root)],
                [str(report), "extra"],
            ):
                result = subprocess.run(
                    [sys.executable, "-B", str(script), *args],
                    cwd=root,
                    env=env,
                    text=True,
                    capture_output=True,
                )
                self.assertEqual(3, result.returncode, result.stderr)
                self.assertIn("error", result.stderr)
            result = subprocess.run(
                [sys.executable, "-B", "-S", str(script), str(report)],
                cwd=root,
                env=env,
                text=True,
                capture_output=True,
            )
            self.assertEqual(3, result.returncode, result.stderr)
            self.assertIn("dependency", result.stderr)
            self.assertNotIn("Traceback", result.stderr)

    def test_invalid_utf8(self):
        with tempfile.TemporaryDirectory(
            prefix="ris-7qq-", dir="/tmp/opencode"
        ) as temp:
            report = Path(temp) / "bad.yaml"
            report.write_bytes(b"\xff")
            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(SKILL / "scripts/validate_review.py"),
                    str(report),
                ],
                text=True,
                capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("UTF-8", result.stderr)
