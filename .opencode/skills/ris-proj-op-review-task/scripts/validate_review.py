"""Read-only mechanical validation of ris.review/1 and /2; see report-format.md."""

from datetime import datetime, timezone
from decimal import Decimal
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import re
import sys


class Invalid(ValueError):
    """The supplied report violates the supported contract."""


class Unsupported(ValueError):
    """The report declares an unknown schema."""


# Executable representation, not a second normative format owner.
OUTCOMES = frozenset(("pass", "fail", "unverified", "not_applicable"))
AREAS = frozenset(
    ("requirements", "architecture", "rules", "correctness", "tests", "docs")
)
COVERAGE = dict(
    area=AREAS, basis="text", outcome=OUTCOMES, evidence=["text"], reason="text"
)
CHECK = dict(
    id="text",
    description="text",
    required="bool",
    outcome=OUTCOMES,
    snapshot_tree="text",
    evidence=["text"],
    reason="text",
)
FINDING = dict(
    id="text",
    severity=frozenset(("high", "medium", "low")),
    status=frozenset(("open", "resolved")),
    location="text",
    summary="text",
    basis="text",
    required_change="text",
)
ROUND = dict(
    id="text",
    previous="nullable",
    created_at="text",
    purpose=frozenset(("analysis", "publication")),
    snapshot=dict(
        repository="text",
        object_format=frozenset(("sha1", "sha256")),
        tree="text",
        base="nullable",
        exclusions=[dict(path="text", reason="text")],
    ),
    inputs=[
        dict(
            role="text",
            address="text",
            version="text",
            status=frozenset(("accepted", "observed", "proposed")),
        )
    ],
    provenance=dict(
        reviewer_context="text",
        authors=["text"],
        invocation_evidence="nullable",
        independence=frozenset(("confirmed", "unverified", "self")),
        basis="text",
    ),
    coverage=[COVERAGE],
    checks=[CHECK],
    findings=[FINDING],
    dispositions=[
        dict(
            finding_id="text",
            decision=frozenset(
                ("fixed", "not_a_defect", "deferred", "accepted_recommendation")
            ),
            basis="text",
        )
    ],
    summary="text",
    verdict=frozenset(("approved", "changes_required", "blocked")),
    limitations=[dict(description="text", blocks_approval="bool")],
)
REPORT = dict(
    schema="text",
    work=dict(project="text", id="nullable", scope="text"),
    rounds=[ROUND],
)

# /1 is intentionally unchanged: an existing file continues its original contract.
ROUND_V2 = dict(
    id="text",
    created_at="text",
    purpose=ROUND["purpose"],
    snapshot={k: v for k, v in ROUND["snapshot"].items() if k != "repository"},
    inputs=ROUND["inputs"],
    provenance={k: v for k, v in ROUND["provenance"].items() if k != "basis"},
    assessment="text",
    checks=[{k: CHECK[k] for k in ("description", "required", "outcome", "evidence")}],
    findings=[
        dict(
            id="text", severity=FINDING["severity"], location="text", description="text"
        )
    ],
    dispositions=ROUND["dispositions"],
    verdict=ROUND["verdict"],
    limitations=ROUND["limitations"],
)
REPORT_V2 = dict(schema="text", work=REPORT["work"], rounds=[ROUND_V2])


def require(condition, path, reason):
    if not condition:
        raise Invalid(f"{path}: {reason}")


def shape(value, schema, path):
    if isinstance(schema, dict):
        require(type(value) is dict, path, "expected mapping")
        require(
            set(value) == set(schema),
            path,
            f"missing keys {sorted(set(schema) - set(value))}; "
            f"unknown keys {sorted(set(value) - set(schema))}",
        )
        for key, child in schema.items():
            shape(value[key], child, f"{path}.{key}")
    elif isinstance(schema, list):
        require(type(value) is list, path, "expected array")
        for i, child in enumerate(value):
            shape(child, schema[0], f"{path}[{i}]")
    elif isinstance(schema, frozenset):
        require(
            type(value) is str and value in schema,
            path,
            f"expected one of {sorted(schema)}",
        )
    elif schema == "bool":
        require(type(value) is bool, path, "expected boolean, without coercion")
    elif schema != "nullable" or value is not None:
        require(
            type(value) is str and bool(value.strip()), path, "expected nonempty string"
        )


def unique(values, path):
    require(len(values) == len(set(values)), path, "duplicate identifiers")


def timestamp(value, path):
    match = re.fullmatch(
        r"(\d{4}-\d{2}-\d{2})[Tt](\d{2}:\d{2}:)(\d{2})(\.\d+)?([Zz]|[+-]\d{2}:\d{2})",
        value,
        flags=re.ASCII,
    )
    require(match is not None, path, "expected RFC3339 string with timezone")
    date, time, second, fraction, zone = match.groups()
    # Actual leap-second occurrence is external evidence, not checked here.
    leap = second == "60"
    normalized = date + "T" + time + ("59" if leap else second)
    if zone.upper() == "Z":
        normalized += "+00:00"
    else:
        require(
            int(zone[1:3]) <= 23 and int(zone[4:]) <= 59,
            path,
            "invalid timezone offset",
        )
        normalized += zone
    try:
        whole = datetime.fromisoformat(normalized).astimezone(timezone.utc)
        return whole, int(leap), Decimal(fraction or "0")
    except (ValueError, OverflowError) as exc:
        raise Invalid(f"{path}: invalid RFC3339 date/time") from exc


def invariants(data):
    rounds = data["rounds"]
    require(bool(rounds), "$.rounds", "expected nonempty array")
    unique([r["id"] for r in rounds], "$.rounds")
    previous_id, previous_time, prior_findings = None, None, set()
    for index, item in enumerate(rounds):
        path = f"$.rounds[{index}]"
        require(
            item["previous"] == previous_id,
            path + ".previous",
            "must link immediately preceding round",
        )
        created = timestamp(item["created_at"], path + ".created_at")
        require(
            previous_time is None or created >= previous_time,
            path + ".created_at",
            "rounds must be chronological",
        )
        previous_id, previous_time = item["id"], created
        snapshot = item["snapshot"]
        length = 40 if snapshot["object_format"] == "sha1" else 64

        def oid(value, at):
            require(
                re.fullmatch(r"[0-9a-f]{" + str(length) + "}", value) is not None,
                at,
                f"expected full lowercase {snapshot['object_format']} OID",
            )

        oid(snapshot["tree"], path + ".snapshot.tree")
        if snapshot["base"] is not None:
            oid(snapshot["base"], path + ".snapshot.base")
        for n, exclusion in enumerate(snapshot["exclusions"]):
            require(
                all(
                    part not in ("", ".", "..") for part in exclusion["path"].split("/")
                ),
                f"{path}.snapshot.exclusions[{n}].path",
                "expected exact repository-relative path",
            )
        for field in ("checks", "findings"):
            unique([entry["id"] for entry in item[field]], path + "." + field)
        coverage = item["coverage"]
        require(
            len(coverage) == 6 and {c["area"] for c in coverage} == AREAS,
            path + ".coverage",
            "expected exactly one result for each of the six areas",
        )
        for field in ("coverage", "checks"):
            for n, entry in enumerate(item[field]):
                at = f"{path}.{field}[{n}]"
                if entry["outcome"] == "pass":
                    require(
                        bool(entry["evidence"]),
                        at + ".evidence",
                        "pass requires evidence",
                    )
                if field == "checks":
                    oid(entry["snapshot_tree"], at + ".snapshot_tree")
                    require(
                        entry["snapshot_tree"] == snapshot["tree"],
                        at + ".snapshot_tree",
                        "must equal round tree",
                    )
        provenance = item["provenance"]
        unique(provenance["authors"], path + ".provenance.authors")
        if provenance["independence"] != "self":
            require(
                provenance["reviewer_context"] not in provenance["authors"],
                path + ".provenance.reviewer_context",
                "author/reviewer overlap requires independence: self",
            )
        if provenance["independence"] == "confirmed":
            require(
                provenance["invocation_evidence"] is not None,
                path + ".provenance.invocation_evidence",
                "confirmed independence requires an evidence address",
            )
        findings = {f["id"]: f for f in item["findings"]}
        require(
            prior_findings <= findings.keys(),
            path + ".findings",
            "all prior findings must remain represented",
        )
        prior_findings = set(findings)
        dispositions = item["dispositions"]
        for n, disposition in enumerate(dispositions):
            at = f"{path}.dispositions[{n}]"
            ident = disposition["finding_id"]
            require(
                ident in findings,
                at + ".finding_id",
                "must reference an existing finding",
            )
            finding = findings[ident]
            require(
                not (
                    finding["severity"] in ("high", "medium")
                    and finding["status"] == "resolved"
                    and disposition["decision"] == "deferred"
                ),
                at + ".decision",
                "high/medium cannot be resolved by deferred",
            )
        for ident, finding in findings.items():
            if finding["status"] == "resolved":
                require(
                    any(d["finding_id"] == ident for d in dispositions),
                    path + ".findings",
                    f"resolved finding {ident!r} requires a disposition",
                )
        actionable = (
            any(
                f["severity"] in ("high", "medium") and f["status"] == "open"
                for f in findings.values()
            )
            or any(c["outcome"] == "fail" for c in coverage)
            or any(c["required"] and c["outcome"] == "fail" for c in item["checks"])
        )
        if item["verdict"] == "changes_required":
            require(
                actionable,
                path + ".verdict",
                "changes_required needs an established high/medium or mandatory violation",
            )
        elif item["verdict"] == "blocked":
            require(
                not actionable,
                path + ".verdict",
                "established actionable violations require changes_required",
            )
        else:
            sufficient = (
                not actionable
                and all(c["outcome"] not in ("fail", "unverified") for c in coverage)
                and all(
                    not c["required"] or c["outcome"] not in ("fail", "unverified")
                    for c in item["checks"]
                )
                and not any(lim["blocks_approval"] for lim in item["limitations"])
                and provenance["independence"] == "confirmed"
            )
            require(
                sufficient,
                path + ".verdict",
                "approved contradicts coverage/checks/findings/limitations/independence",
            )


def invariants_v2(data):
    rounds = data["rounds"]
    require(bool(rounds), "$.rounds", "expected nonempty array")
    unique([r["id"] for r in rounds], "$.rounds")
    previous_time = None
    findings, open_ids = {}, set()
    for index, item in enumerate(rounds):
        path = f"$.rounds[{index}]"
        created = timestamp(item["created_at"], path + ".created_at")
        require(
            previous_time is None or created >= previous_time,
            path + ".created_at",
            "rounds must be chronological",
        )
        previous_time = created
        snapshot = item["snapshot"]
        length = 40 if snapshot["object_format"] == "sha1" else 64
        for key in ("tree", "base"):
            value = snapshot[key]
            if key == "base" and value is None:
                require(
                    item["purpose"] == "analysis",
                    path + ".snapshot.base",
                    "publication requires a full base commit",
                )
                continue
            require(
                re.fullmatch(r"[0-9a-f]{" + str(length) + "}", value) is not None,
                path + ".snapshot." + key,
                "expected full lowercase Git OID",
            )
        for n, exclusion in enumerate(snapshot["exclusions"]):
            require(
                all(
                    part not in ("", ".", "..") for part in exclusion["path"].split("/")
                ),
                f"{path}.snapshot.exclusions[{n}].path",
                "expected exact repository-relative path",
            )
        provenance = item["provenance"]
        unique(provenance["authors"], path + ".provenance.authors")
        if provenance["independence"] != "self":
            require(
                provenance["reviewer_context"] not in provenance["authors"],
                path + ".provenance.reviewer_context",
                "author/reviewer overlap requires independence: self",
            )
        if provenance["independence"] == "confirmed":
            require(
                provenance["invocation_evidence"] is not None,
                path + ".provenance.invocation_evidence",
                "confirmed independence requires an evidence address",
            )
        for n, check in enumerate(item["checks"]):
            if check["outcome"] == "pass":
                require(
                    bool(check["evidence"]),
                    f"{path}.checks[{n}].evidence",
                    "pass requires evidence",
                )
        unique([d["finding_id"] for d in item["dispositions"]], path + ".dispositions")
        # Resolve only previously open findings. New findings cannot be silently
        # closed in their introducing round, and closed IDs cannot be reused.
        for n, disposition in enumerate(item["dispositions"]):
            at = f"{path}.dispositions[{n}]"
            ident, decision = disposition["finding_id"], disposition["decision"]
            require(
                ident in open_ids,
                at + ".finding_id",
                "must reference an open finding from a prior round",
            )
            severity = findings[ident]["severity"]
            require(
                decision != "accepted_recommendation" or severity == "low",
                at + ".decision",
                "accepted_recommendation is only for low findings",
            )
            if decision != "deferred" or severity == "low":
                open_ids.remove(ident)
        for n, finding in enumerate(item["findings"]):
            ident = finding["id"]
            require(
                ident not in findings,
                f"{path}.findings[{n}].id",
                "finding IDs are globally unique; do not repeat or reopen findings",
            )
            findings[ident] = finding
            open_ids.add(ident)
        actionable = any(
            findings[ident]["severity"] in ("high", "medium") for ident in open_ids
        ) or any(c["required"] and c["outcome"] == "fail" for c in item["checks"])
        if item["verdict"] == "changes_required":
            require(
                actionable,
                path + ".verdict",
                "changes_required needs an established high/medium or mandatory violation",
            )
        elif item["verdict"] == "blocked":
            require(
                not actionable,
                path + ".verdict",
                "established actionable violations require changes_required",
            )
        else:
            sufficient = (
                not actionable
                and all(
                    not c["required"] or c["outcome"] not in ("fail", "unverified")
                    for c in item["checks"]
                )
                and not any(lim["blocks_approval"] for lim in item["limitations"])
                and provenance["independence"] == "confirmed"
            )
            require(
                sufficient,
                path + ".verdict",
                "approved contradicts checks/findings/limitations/independence",
            )


def parse(text):
    from ruamel.yaml import YAML
    from ruamel.yaml.error import YAMLError
    from ruamel.yaml.events import AliasEvent, DocumentStartEvent
    from ruamel.yaml.nodes import MappingNode, SequenceNode, ScalarNode

    yaml = YAML(typ="safe", pure=True)
    yaml.version = (1, 2)
    yaml.allow_duplicate_keys = False

    def reject(node, message):
        mark = node.start_mark
        raise Invalid(f"line {mark.line + 1}, column {mark.column + 1}: {message}")

    def inspect(node):
        if isinstance(node, ScalarNode) and node.tag in {
            "tag:yaml.org,2002:" + t for t in ("bool", "int", "null")
        }:
            if yaml.resolver.resolve(ScalarNode, node.value, (True, False)) != node.tag:
                reject(node, "scalar spelling does not match its YAML 1.2 type")
        if node.tag not in {
            "tag:yaml.org,2002:" + t
            for t in ("map", "seq", "str", "bool", "int", "null")
        }:
            reject(node, f"forbidden YAML type/tag {node.tag}")
        if isinstance(node, MappingNode):
            keys = set()
            for key, value in node.value:
                if key.tag != "tag:yaml.org,2002:str" or key.value == "<<":
                    reject(key, "mapping keys must be strings, not merge keys")
                if key.value in keys:
                    reject(key, f"duplicate key {key.value!r}")
                keys.add(key.value)
                inspect(value)
        elif isinstance(node, SequenceNode):
            for value in node.value:
                inspect(value)

    try:
        for event in yaml.parse(text):
            if isinstance(event, DocumentStartEvent) and event.version not in (
                None,
                (1, 2),
            ):
                reject(event, "only YAML 1.2 is supported")
            if (
                isinstance(event, AliasEvent)
                or getattr(event, "anchor", None) is not None
            ):
                reject(event, "anchors and aliases are forbidden")
        node = yaml.compose(text)
        if node is None:
            raise Invalid("$: expected one YAML document")
        inspect(node)
        return yaml.load(text)
    except (YAMLError, ValueError, KeyError, RecursionError) as exc:
        raise Invalid(f"YAML: {exc}") from exc


def validate_text(text):
    data = parse(text)
    if type(data) is not dict:
        raise Invalid("$: expected mapping")
    if type(data.get("schema")) is not str or not data["schema"].strip():
        raise Invalid("$.schema: expected nonempty schema string")
    if data["schema"] not in ("ris.review/1", "ris.review/2"):
        raise Unsupported(f"$.schema: unsupported schema {data['schema']!r}")
    if data["schema"] == "ris.review/1":
        shape(data, REPORT, "$")
        invariants(data)
    else:
        shape(data, REPORT_V2, "$")
        invariants_v2(data)


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print(
            "error: usage: python -B <skill>/scripts/validate_review.py <review.yaml>",
            file=sys.stderr,
        )
        return 3
    if sys.version_info < (3, 10):
        print("error: Python >=3.10 is required", file=sys.stderr)
        return 3
    try:
        if version("ruamel.yaml") != "0.18.16":
            raise ImportError("expected ruamel.yaml==0.18.16")
        from ruamel.yaml import YAML  # noqa: F401 — check availability before reading
    except (ImportError, PackageNotFoundError) as exc:
        print(
            f"error: YAML dependency unavailable/incompatible ({exc}); "
            "install the skill's requirements.txt in an explicitly authorized venv; "
            "see references/report-format.md",
            file=sys.stderr,
        )
        return 3
    try:
        text = Path(args[0]).read_text(encoding="utf-8")
        validate_text(text)
    except UnicodeError as exc:
        print(f"invalid: {args[0]}: expected UTF-8 ({exc})", file=sys.stderr)
        return 1
    except Invalid as exc:
        print(f"invalid: {args[0]}: {exc}", file=sys.stderr)
        return 1
    except Unsupported as exc:
        print(f"unsupported: {args[0]}: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"error: {args[0]}: {exc}", file=sys.stderr)
        return 3
    print("valid: format only; no external evidence or approval verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
