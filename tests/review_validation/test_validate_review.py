"""Program tests, not agent sessions. The format owner's example is synthetic."""

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills/ris-proj-op-review-task"
SCRIPT = SKILL / "scripts/validate_review.py"
spec = importlib.util.spec_from_file_location("validate_review", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
EXAMPLE = (
    (SKILL / "references/report-format.md")
    .read_text()
    .split("```yaml\n", 1)[1]
    .split("```", 1)[0]
)


class ParsingTests(unittest.TestCase):
    def test_owner_example(self):
        self.assertIsNone(validator.validate_text(EXAMPLE))

    def test_forbidden_yaml(self):
        for extra in (
            "extra: 1.5",
            "extra: 2026-10-21",
            "extra: &x []",
            "extra: *x",
            "extra: !custom hello",
            "extra: {<<: {a: b}}",
            "extra: {a: 1, a: 2}",
            "extra: {true: value}",
            "extra: !!binary aGk=",
            "extra: !!set {a: null}",
        ):
            with self.subTest(extra=extra), self.assertRaises(validator.Invalid):
                validator.validate_text(EXAMPLE + extra + "\n")

    def test_document_profile(self):
        for text in (
            "",
            EXAMPLE + "---\nx: y\n",
            "%YAML 1.1\n---\n" + EXAMPLE,
            "[unterminated",
            "true",
            "null",
        ):
            with self.subTest(text=text[:30]), self.assertRaises(validator.Invalid):
                validator.validate_text(text)

    def test_unsupported_schema(self):
        with self.assertRaises(validator.Unsupported):
            validator.validate_text(EXAMPLE.replace("ris.review/1", "ris.review/99"))

    def test_malformed_explicit_scalar_is_invalid(self):
        for value in ("!!int nope", "!!bool nope", "!!null nope"):
            with self.subTest(value=value), self.assertRaises(validator.Invalid):
                validator.validate_text(
                    EXAMPLE.replace("id: example-1", "id: " + value)
                )


if __name__ == "__main__":
    unittest.main()
