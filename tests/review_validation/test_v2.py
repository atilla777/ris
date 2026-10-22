"""Compact review program contract; synthetic locators are not approval evidence."""

from copy import deepcopy
import unittest

from test_contract import dump
from test_validate_review import SKILL, validator


def example():
    return {
        "schema": "ris.review/2",
        "work": {"project": "example-repository", "id": "example-1", "scope": "Change"},
        "rounds": [
            {
                "id": "r1",
                "created_at": "2026-10-22T10:00:00Z",
                "purpose": "publication",
                "snapshot": {
                    "object_format": "sha1",
                    "base": "2" * 40,
                    "tree": "1" * 40,
                    "exclusions": [],
                },
                "inputs": [
                    {
                        "role": "requirements",
                        "address": "example:request",
                        "version": "S1",
                        "status": "accepted",
                    }
                ],
                "provenance": {
                    "reviewer_context": "reviewer-session",
                    "authors": ["author-session"],
                    "invocation_evidence": "example:invocation",
                    "independence": "confirmed",
                },
                "assessment": "Requirements/rules and final correctness checked; architecture "
                "unchanged; program tests and affected docs inspected.",
                "checks": [
                    {
                        "description": "Applicable regression tests",
                        "required": True,
                        "outcome": "pass",
                        "evidence": ["example:tests"],
                    }
                ],
                "findings": [],
                "dispositions": [],
                "verdict": "approved",
                "limitations": [],
            }
        ],
    }


def finding(ident="F1", severity="medium"):
    return {
        "id": ident,
        "severity": severity,
        "location": "parser.py:12",
        "description": "The parser drops inputs; preserve them and test the failure.",
    }


def append_round(data, **changes):
    r = deepcopy(example()["rounds"][0])
    r.update(id=f"r{len(data['rounds']) + 1}", created_at="2026-10-22T11:00:00Z")
    r.update(changes)
    data["rounds"].append(r)
    return r


class CompactTests(unittest.TestCase):
    def test_owner_example(self):
        text = (
            (SKILL / "references/report-format.md")
            .read_text()
            .split("```yaml\n", 1)[1]
            .split("```", 1)[0]
        )
        validator.validate_text(text)

    def test_unsafe_yaml_and_mixed_schema(self):
        text = dump(example())
        for extra in (
            "extra: 1.5",
            "extra: 2026-10-22",
            "extra: &x []",
            "extra: *x",
            "extra: !custom hello",
            "extra: {<<: {a: b}}",
            "extra: {a: 1, a: 2}",
            "extra: {true: value}",
            "extra: !!binary aGk=",
            "extra: !!set {a: null}",
            "---\nother: document",
            "schema: ris.review/2",
        ):
            with self.subTest(extra=extra), self.assertRaises(validator.Invalid):
                validator.validate_text(text + extra + "\n")
        for text in (
            text.replace("ris.review/2", "ris.review/1"),
            "%YAML 1.1\n---\n" + text,
        ):
            with self.assertRaises(validator.Invalid):
                validator.validate_text(text)

    def test_exact_mapping_keys(self):
        data = example()
        r = data["rounds"][0]
        r["findings"] = [finding(severity="low")]
        r["snapshot"]["exclusions"] = [{"path": "foreign.md", "reason": "Foreign work"}]
        r["limitations"] = [
            {"description": "Local evidence only", "blocks_approval": False}
        ]
        append_round(
            data,
            dispositions=[
                {
                    "finding_id": "F1",
                    "decision": "accepted_recommendation",
                    "basis": "Optional",
                }
            ],
        )
        validator.validate_text(dump(data))

        def mappings(value):
            if isinstance(value, dict):
                yield value
                for child in value.values():
                    yield from mappings(child)
            elif isinstance(value, list):
                for child in value:
                    yield from mappings(child)

        for mapping in mappings(data):
            mapping["unexpected"] = True
            with self.subTest(keys=list(mapping)), self.assertRaises(validator.Invalid):
                validator.validate_text(dump(data))
            del mapping["unexpected"]
            for key in list(mapping):
                value = mapping.pop(key)
                with self.subTest(missing=key), self.assertRaises(validator.Invalid):
                    validator.validate_text(dump(data))
                mapping[key] = value

    def test_types_oids_paths_and_declarations(self):
        for owner, key, value in (
            ("root", "rounds", []),
            ("work", "id", False),
            ("work", "project", " "),
            ("round", "assessment", " "),
            ("round", "inputs", None),
            ("round", "verdict", "pass"),
            ("round", "created_at", "2026-10-22"),
            ("round", "created_at", "2026-02-30T10:00:00Z"),
            ("snapshot", "tree", "main"),
            ("snapshot", "base", None),
            ("snapshot", "tree", "A" * 40),
            ("snapshot", "tree", "1" * 39),
            ("snapshot", "object_format", "SHA1"),
            ("snapshot", "exclusions", [{"path": "a/../b", "reason": "x"}]),
            ("snapshot", "exclusions", [{"path": "/absolute", "reason": "x"}]),
            ("provenance", "authors", ["same", "same"]),
            ("provenance", "reviewer_context", "author-session"),
            ("provenance", "invocation_evidence", None),
            ("provenance", "independence", "yes"),
            ("check", "required", "true"),
            ("check", "required", 1),
            ("check", "outcome", "failed"),
            ("check", "evidence", []),
            ("finding", "severity", "critical"),
            ("finding", "description", ""),
            ("input", "status", "ready"),
            ("input", "version", None),
        ):
            data = example()
            r = data["rounds"][0]
            r["findings"] = [finding(severity="low")]
            targets = {
                "root": data,
                "work": data["work"],
                "round": r,
                "snapshot": r["snapshot"],
                "provenance": r["provenance"],
                "check": r["checks"][0],
                "finding": r["findings"][0],
                "input": r["inputs"][0],
            }
            targets[owner][key] = value
            with (
                self.subTest(owner=owner, key=key, value=value),
                self.assertRaises(validator.Invalid),
            ):
                validator.validate_text(dump(data))

    def test_minimal_publication_and_analysis(self):
        data = example()
        validator.validate_text(dump(data))
        r = data["rounds"][0]
        r.update(purpose="analysis", checks=[], inputs=[])
        r["snapshot"].update(object_format="sha256", tree="a" * 64, base=None)
        data["work"]["id"] = None
        validator.validate_text(dump(data))

    def test_verdict_gates(self):
        for mutate in (
            lambda r: r.update(findings=[finding()]),
            lambda r: r["checks"][0].update(outcome="fail"),
            lambda r: r["checks"][0].update(outcome="unverified"),
            lambda r: r["limitations"].append(
                {"description": "missing", "blocks_approval": True}
            ),
            lambda r: r["provenance"].update(independence="unverified"),
            lambda r: r["provenance"].update(
                independence="self", reviewer_context="author-session"
            ),
            lambda r: r.update(verdict="changes_required"),
        ):
            data = example()
            mutate(data["rounds"][0])
            with self.subTest(mutation=mutate), self.assertRaises(validator.Invalid):
                validator.validate_text(dump(data))
        for outcome in ("fail", "unverified"):
            data = example()
            data["rounds"][0]["checks"][0].update(outcome=outcome, required=False)
            validator.validate_text(dump(data))

    def test_fold_prior_findings_until_explicit_resolution(self):
        data = example()
        first = data["rounds"][0]
        first.update(findings=[finding()], verdict="changes_required")
        second = append_round(data, verdict="changes_required")
        validator.validate_text(dump(data))  # No repetition of F1.
        second["verdict"] = "approved"
        with self.assertRaises(validator.Invalid):
            validator.validate_text(dump(data))
        second["dispositions"] = [
            {"finding_id": "F1", "decision": "fixed", "basis": "Fix inspected"}
        ]
        validator.validate_text(dump(data))
        append_round(data)  # Resolved findings need no repeated disposition either.
        validator.validate_text(dump(data))

    def test_history_references_and_ids(self):
        data = example()
        data["rounds"][0].update(findings=[finding()], verdict="changes_required")
        second = append_round(
            data,
            dispositions=[
                {
                    "finding_id": "F1",
                    "decision": "not_a_defect",
                    "basis": "Requirement checked",
                }
            ],
        )
        validator.validate_text(dump(data))
        for changes in (
            {"id": "r1"},
            {"created_at": "2026-10-22T09:00:00Z"},
            {"findings": [finding()]},
            {
                "dispositions": [
                    {"finding_id": "missing", "decision": "fixed", "basis": "x"}
                ]
            },
            {"dispositions": second["dispositions"] * 2},
            {
                "dispositions": [
                    {"finding_id": "F1", "decision": "deferred", "basis": "later"}
                ]
            },
            {
                "dispositions": [
                    {
                        "finding_id": "F1",
                        "decision": "accepted_recommendation",
                        "basis": "x",
                    }
                ]
            },
        ):
            bad = deepcopy(data)
            bad["rounds"][1].update(changes)
            with self.subTest(changes=changes), self.assertRaises(validator.Invalid):
                validator.validate_text(dump(bad))
        third = append_round(data, dispositions=deepcopy(second["dispositions"]))
        with self.assertRaises(validator.Invalid):
            validator.validate_text(
                dump(data)
            )  # Cannot dispose of an already closed ID.
        third.update(
            dispositions=[], findings=[finding("F2")], verdict="changes_required"
        )
        validator.validate_text(dump(data))  # Rediscovery needs a new ID.

    def test_deferred_does_not_close_high_or_medium(self):
        for severity in ("high", "medium", "low"):
            data = example()
            data["rounds"][0].update(
                findings=[finding(severity=severity)],
                verdict="approved" if severity == "low" else "changes_required",
            )
            second = append_round(
                data,
                verdict="approved" if severity == "low" else "changes_required",
                dispositions=[
                    {"finding_id": "F1", "decision": "deferred", "basis": "Later"}
                ],
            )
            validator.validate_text(dump(data))
            if severity != "low":
                second["verdict"] = "blocked"
                with self.assertRaises(validator.Invalid):
                    validator.validate_text(dump(data))

    def test_later_adverse_unknown_or_invalid_cannot_be_skipped(self):
        data = example()
        append_round(
            data,
            verdict="blocked",
            limitations=[
                {
                    "description": "Current inputs unavailable",
                    "blocks_approval": True,
                }
            ],
        )
        validator.validate_text(
            dump(data)
        )  # Valid format, not approval of latest subject.
        data["rounds"][-1]["verdict"] = "unknown"
        with self.assertRaises(validator.Invalid):
            validator.validate_text(dump(data))
        data["rounds"][-1]["verdict"] = "approved"
        with self.assertRaises(validator.Invalid):
            validator.validate_text(dump(data))


if __name__ == "__main__":
    unittest.main()
