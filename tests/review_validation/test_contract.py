from copy import deepcopy
from io import StringIO
import unittest
from ruamel.yaml import YAML
from test_validate_review import EXAMPLE, validator


def example():
    return YAML(typ="safe", pure=True).load(EXAMPLE)


def dump(data):
    stream = StringIO()
    YAML(typ="safe", pure=True).dump(data, stream)
    return stream.getvalue()


class ShapeTests(unittest.TestCase):
    def test_exact_keys_every_mapping(self):
        data = example()
        r = data["rounds"][0]
        r["snapshot"]["exclusions"] = [{"path": "file.md", "reason": "foreign"}]
        r["dispositions"] = [
            {"finding_id": "F1", "decision": "deferred", "basis": "optional"}
        ]
        r["limitations"] = [{"description": "local", "blocks_approval": False}]

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
                old = mapping.pop(key)
                with self.subTest(missing=key), self.assertRaises(validator.Invalid):
                    validator.validate_text(dump(data))
                mapping[key] = old

    def test_types_enums_and_empty_values(self):
        mutations = [
            ("work", "project", True),
            ("work", "id", 123),
            ("work", "scope", "  "),
            ("round", "purpose", "other"),
            ("round", "verdict", "pass"),
            ("round", "created_at", 123),
            ("round", "coverage", []),
            ("round", "inputs", {}),
            ("round", "checks", None),
            ("check", "required", "true"),
            ("check", "outcome", "failed"),
            ("coverage", "area", "quality"),
            ("coverage", "evidence", [1]),
            ("finding", "severity", "critical"),
            ("finding", "status", "fixed"),
            ("provenance", "authors", [None]),
            ("snapshot", "object_format", "SHA1"),
            ("input", "status", "ready"),
        ]
        for owner, key, value in mutations:
            data = example()
            r = data["rounds"][0]
            targets = {
                "work": data["work"],
                "round": r,
                "check": r["checks"][0],
                "coverage": r["coverage"][0],
                "finding": r["findings"][0],
                "provenance": r["provenance"],
                "snapshot": r["snapshot"],
                "input": r["inputs"][0],
            }
            targets[owner][key] = value
            with (
                self.subTest(owner=owner, key=key),
                self.assertRaises(validator.Invalid),
            ):
                validator.validate_text(dump(data))

    def test_empty_rounds(self):
        data = example()
        data["rounds"] = []
        with self.assertRaises(validator.Invalid):
            validator.validate_text(dump(data))


class InvariantTests(unittest.TestCase):
    def test_leap_second_orders_before_next_second(self):
        data = example()
        first = data["rounds"][0]
        first["created_at"] = "2016-12-31T23:59:60.5Z"
        second = deepcopy(first)
        second.update(id="r2", previous="r1", created_at="2017-01-01T00:00:00Z")
        data["rounds"].append(second)
        validator.validate_text(dump(data))

    def test_fractional_chronology_without_precision_loss(self):
        data = example()
        first = data["rounds"][0]
        first["created_at"] = "2026-10-20T15:00:00.0000002Z"
        second = deepcopy(first)
        second.update(id="r2", previous="r1", created_at="2026-10-20T15:00:00.0000001Z")
        data["rounds"].append(second)
        with self.assertRaises(validator.Invalid):
            validator.validate_text(dump(data))

    def check_mutation(self, mutate):
        data = example()
        mutate(data["rounds"][0])
        with self.assertRaises(validator.Invalid):
            validator.validate_text(dump(data))

    def test_oids_dates_paths_and_uniqueness(self):
        for value in ("main", "A" * 40, "1" * 39, 123):
            with self.subTest(oid=value):
                self.check_mutation(lambda r: r["snapshot"].update(tree=value))
        for value in (
            "2026-10-21",
            "2026-02-30T00:00:00Z",
            "2026-10-21T00:00:00",
            "2026-10-21 00:00:00Z",
        ):
            with self.subTest(date=value):
                self.check_mutation(lambda r: r.update(created_at=value))
        for path in ("/absolute", "../escape", "a/../b", "./file", "a//b"):
            with self.subTest(path=path):
                self.check_mutation(
                    lambda r: r["snapshot"].update(
                        exclusions=[dict(path=path, reason="x")]
                    )
                )
        self.check_mutation(lambda r: r["checks"][0].update(snapshot_tree="3" * 40))
        self.check_mutation(lambda r: r["coverage"].pop())
        self.check_mutation(lambda r: r["coverage"].append(deepcopy(r["coverage"][0])))
        self.check_mutation(lambda r: r["checks"].append(deepcopy(r["checks"][0])))
        self.check_mutation(lambda r: r["findings"].append(deepcopy(r["findings"][0])))
        self.check_mutation(lambda r: r["provenance"].update(authors=["same", "same"]))

    def test_verdict_contradictions(self):
        for mutate in (
            lambda r: r["findings"][0].update(severity="high"),
            lambda r: r["checks"][0].update(outcome="fail"),
            lambda r: r["checks"][0].update(outcome="unverified"),
            lambda r: r["checks"][0].update(evidence=[]),
            lambda r: r["coverage"][0].update(outcome="fail"),
            lambda r: r["coverage"][0].update(outcome="unverified"),
            lambda r: r["coverage"][0].update(evidence=[]),
            lambda r: r["limitations"].append(
                dict(description="missing access", blocks_approval=True)
            ),
            lambda r: r["provenance"].update(independence="unverified"),
            lambda r: r["provenance"].update(
                independence="self", reviewer_context="author-session"
            ),
            lambda r: r["provenance"].update(invocation_evidence=None),
            lambda r: r["provenance"].update(reviewer_context="author-session"),
            lambda r: r.update(verdict="changes_required"),
            lambda r: r["findings"][0].update(status="resolved"),
            lambda r: r["dispositions"].append(
                dict(finding_id="missing", decision="fixed", basis="x")
            ),
        ):
            with self.subTest(mutation=mutate):
                self.check_mutation(mutate)

    def test_valid_adverse_self_and_sha256(self):
        data = example()
        r = data["rounds"][0]
        r["provenance"].update(
            independence="self",
            reviewer_context="author-session",
            invocation_evidence=None,
        )
        r["verdict"] = "blocked"
        validator.validate_text(dump(data))
        r["findings"][0]["severity"] = "high"
        r["verdict"] = "changes_required"
        validator.validate_text(dump(data))
        r["verdict"] = "blocked"
        with self.assertRaises(validator.Invalid):
            validator.validate_text(dump(data))
        data = example()
        r = data["rounds"][0]
        r["snapshot"].update(object_format="sha256", tree="a" * 64, base=None)
        r["checks"][0]["snapshot_tree"] = "a" * 64
        data["work"]["id"] = None
        validator.validate_text(dump(data))

    def test_history(self):
        data = example()
        r2 = deepcopy(data["rounds"][0])
        r2.update(id="r2", previous="r1", created_at="2026-10-20T16:00:00+00:00")
        r2["findings"][0]["status"] = "resolved"
        r2["dispositions"] = [
            dict(finding_id="F1", decision="fixed", basis="reviewed fix")
        ]
        data["rounds"].append(r2)
        validator.validate_text(dump(data))
        for key, value in (
            ("id", "r1"),
            ("previous", None),
            ("previous", "other"),
            ("findings", []),
            ("dispositions", []),
            ("created_at", "2026-10-20T14:00:00Z"),
        ):
            bad = deepcopy(data)
            bad["rounds"][1][key] = value
            with (
                self.subTest(key=key, value=value),
                self.assertRaises(validator.Invalid),
            ):
                validator.validate_text(dump(bad))
        r2["findings"][0]["severity"] = "high"
        r2["dispositions"][0]["decision"] = "deferred"
        with self.assertRaises(validator.Invalid):
            validator.validate_text(dump(data))
