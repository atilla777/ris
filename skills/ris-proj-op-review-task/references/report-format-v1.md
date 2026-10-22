# Project review report — `ris.review/1`

Conditional compatibility resource of `report-format.md`. Read **only** when an
existing file declares `schema: ris.review/1`; continue that file unchanged under
this original contract. New files use /2. Do not load this resource for ordinary /2.

Read before producing, saving or consuming a project review file, including an
optional fast-route save. This resource alone owns serialization, types and gate
semantics; portable review owns assessment. The bundled Python validator implements
only mechanical checks under this resource; it is not another norm owner, an
approval engine, schema registry or Gas City metadata.

## Mechanical validator: setup and CLI

Use Python **>=3.10** and **ruamel.yaml==0.18.16** (YAML 1.2, pure-Python safe
loader). `requirements.txt` and `scripts/validate_review.py` live inside this
skill, so the same command works from a source or installed skill folder.
Dependency installation is a separate, explicitly authorized action, never a
validator side effect. For example, choose an authorized venv location and set
`skill` to the actual installed folder (not the caller's project root):

```sh
skill='/absolute/path/to/.opencode/skills/ris-proj-op-review-task'
python3 -m venv /authorized/path/review-venv
/authorized/path/review-venv/bin/python -m pip install -r "$skill/requirements.txt"
/authorized/path/review-venv/bin/python -B "$skill/scripts/validate_review.py" /absolute/path/review.yaml
```

CLI: `python -B <skill>/scripts/validate_review.py <review.yaml>`. Exit **0** means
`valid` format only; **1** means `invalid` (including non-UTF-8); **2** means
`unsupported` schema; **3** is a separate operational/setup error (usage, I/O,
unsupported Python or missing/incompatible dependency), not an invalid report.
Diagnostics identify a YAML line/column or field path and reason. Nothing is
repaired, written or published. Git, Beads, network and agents are not needed.
The validator never installs dependencies or fetches evidence. Missing dependency
returns the setup error with explicit-install guidance; do not treat it as a pass
or auto-install. If unavailable, substantive manual inspection remains possible,
but must not be described as machine validation.

The program checks the document profile, exact schema, intrinsic round/finding
history and formally represented verdict contradictions below. It cannot compare
past file bytes for append-only saving, determine whether prose is truthful or a
reason is substantively adequate, resolve objects/addresses, establish actual
independence, detect external mandatory violations or approve publication.
Consumers still own all external predicates and concurrent save/read-back checks.

Implementation basis for **ris-7qq / T3**: requirements and V1 decision at
`ff79c496b733756a86003b44e70eb72c60efa532`,
`docs/specs/sdlc-audit-remediation/spec.md`, T3. The user separately accepted the
bounded implementation design (execution-request version) in the dialogue: Python >=3.10, pinned
ruamel.yaml, these skill-local files/CLI, distinct validity/unsupported/setup
results, explicit venv installation, mechanical read-only scope and no external
approval claims. This records that design scope, not a renewal of the historical
V1 decision or an independent review/acceptance of implementation.

## Storage and authority

The ordinary project route saves one complete `review.yaml`, by default at
context-checked primary `workspace.tasks/<ID>/review.yaml`. Without an ID, saving
requires an explicit authorized local address; never invent a task. The YAML is
the sole authority for review content and verdict, not a Markdown twin or Beads
metadata. Beads stores only its address and selected round ID, through a separately
authorized tracker owner. The short work result, published Git SHA and completion
facts remain in Beads; they are not a second review. Another local session can
read this file; remote archival, publication with code and access from another
machine are not promised. Missing local reports never imply approval.

Fast execution retains independent review without a mandatory file; its sufficient
session result is not a second serialization format. If saving is separately
requested, use this same contract. Preserve historical Markdown reports unchanged;
do not automatically migrate them or treat them as a current-format gate.

One file holds work identity and append-only rounds. Before saving, read and compare
the existing file/history with the inspected version. Append the new complete
round without rewriting prior rounds or unrelated data; independently read back
the complete result. A conflict or partial/unparseable write blocks the save/gate;
reconcile before retry, never overwrite another writer. Fresh comparison/read-back
is not filesystem CAS or a transaction. No separate latest verdict/passed flag.

## YAML and exact mappings

One UTF-8 YAML 1.2 document. Mapping keys are strings. Reject duplicate and merge
keys, anchors/aliases, custom tags and scalar types other than string, boolean,
integer and null. Do not coerce values (including timestamps/OIDs) into expected
types or silently discard unknown fields. Fixed mappings have **exactly** the
keys below. Every field is required; null is allowed only where stated. Strings
must be nonempty/non-whitespace unless explicitly allowed otherwise (none here).
Arrays may be empty except where a nonempty/complete set is required. Use block
strings for substantial explanations. Unknown schema is `unsupported`, not pass.

| Mapping | Required fields and types |
|---|---|
| root | `schema`: literal string `ris.review/1`; `work`: Work; `rounds`: nonempty array of Round |
| Work | `project`: repository/project locator string; `id`: string or null for no-ID; `scope`: string |
| Round | `id`: unique string; `previous`: immediately preceding round ID string or null; `created_at`: RFC3339 string with timezone; `purpose`: `analysis` or `publication`; `snapshot`: Snapshot; `inputs`: array of Input; `provenance`: Provenance; `coverage`: nonempty array of Coverage; `checks`: array of Check; `findings`: array of Finding; `dispositions`: array of Disposition; `summary`: string; `verdict`: `approved`, `changes_required` or `blocked`; `limitations`: array of Limitation |
| Snapshot | `repository`: repository locator string; `object_format`: `sha1` or `sha256`; `tree`: full Git tree OID string; `base`: full commit OID string or null; `exclusions`: array of Exclusion |
| Exclusion | `path`: exact repository-relative path string; `reason`: string |
| Input | `role`: string; `address`: string; `version`: string; `status`: `accepted`, `observed` or `proposed` |
| Provenance | `reviewer_context`: string; `authors`: array of unique context/actor ID strings; `invocation_evidence`: address string or null; `independence`: `confirmed`, `unverified` or `self`; `basis`: string |
| Coverage | `area`: `requirements`, `architecture`, `rules`, `correctness`, `tests` or `docs`; `basis`: string; `outcome`: `pass`, `fail`, `unverified` or `not_applicable`; `evidence`: array of address strings; `reason`: string |
| Check | `id`: unique string within round; `description`: string; `required`: boolean; `outcome`: same four enums as Coverage; `snapshot_tree`: full OID string; `evidence`: array of address strings; `reason`: string |
| Finding | `id`: stable string, unique within round; `severity`: `high`, `medium` or `low`; `status`: `open` or `resolved`; `location`: file/symbol/artifact scope string; `summary`, `basis`, `required_change`: strings |
| Disposition | `finding_id`: existing finding ID string; `decision`: `fixed`, `not_a_defect`, `deferred` or `accepted_recommendation`; `basis`: string |
| Limitation | `description`: string; `blocks_approval`: boolean |

## Subject, history and verdict invariants

- Git OIDs are lowercase hex strings of exactly 40/64 characters according to
  `object_format`, never branch/tag/short SHA. `tree` identifies the **complete**
  checked tree: unchanged base plus additions/deletions/content/modes. The locator
  must resolve the repository/object store; an absolute path is not a remote
  availability guarantee. A null base permits current-content analysis, not
  invented delta evidence or an ambiguous publication basis.
- WIP is not HEAD. Obtain its exact prospective tree from the existing snapshot
  owner without changing the user's index/worktree or creating a snapshot commit
  solely for review. A loose Git object is not a backup: after object loss recover
  the exact subject or review anew. Declare exclusions before assessment. For dirty
  tracked exclusions the tree retains base bytes/modes, not missing tracked files.
  Compare the actual complete publication tree/base/exclusions with this subject.
  Saving ignored local review evidence does not change that tree.
- First round has `previous: null`; a resolved finding needs a reasoned reviewer
  disposition, never `deferred` for high/medium. Read `review-history.md` beside
  this resource before appending/consuming multiple rounds, prior-finding
  dispositions or conflicting historical evidence. It owns the detailed history
  branch of this same format, not another report contract. No new round for low
  alone; collective reasoned prose disposition remains sufficient.
- Coverage has exactly one result for each of the six areas. Keep requirements
  and rules/quality distinguishable. `fail`/`unverified` coverage forbids approved;
  `not_applicable` needs a specific checked reason. Publication inputs identify
  applicable requirements/rules and design where required; missing mandatory
  inputs cannot be hidden with `not_applicable`.
- Required checks with `fail`/`unverified` forbid approval. `not_applicable` needs
  a checked reason, not a missing tool. Claimed pass requires evidence (also for
  coverage); every Check's `snapshot_tree` equals its Round's tree. Consumers
  independently assess whether evidence actually applies to that tree. Checks
  describe reviewer checks or applicable results assessed by the reviewer, not
  the history of the author's test development or copied implementation log.
- `changes_required`: established unresolved high/medium or mandatory violation.
  If evidence is also insufficient, retain those limitations. `blocked`: no
  established actionable blocker, but missing required access/evidence/independence
  or applicability. `approved`: sufficient coverage/checks, no open high/medium,
  mandatory violations, failed/unverified gates or blocking limitations, and
  confirmed independence. Open low is allowed. Contradictory verdict is invalid;
  a repaired finding alone is not approval.
- `reviewer_context` may be in `authors` when `independence: self`; otherwise it
  must not be. Self-review may be a valid `blocked` or `changes_required` analysis
  (according to findings), never `approved`, and never replaces required separate
  independent review. Confirmed independence requires a non-null invocation
  evidence address and real inspectable invocation/context evidence, compared by
  the caller with the actual
  launch and **all** authors/repairers. A name, configured role or self-declared
  `confirmed` does not prove this. Null/missing-access evidence cannot establish
  an independent gate. No cryptographic attestation or trusted registry is implied.

## Two separate consumer results

1. Establish format validity: syntax, supported schema, exact keys/types/enums,
   OIDs/round/finding references and verdict consistency → `valid`, `invalid` or
   `unsupported`. Ordinary YAML parsing establishes syntax only, not full schema
   validity. Use the bundled CLI above for mechanical validation when available;
   retain its operational error separately from the three format results. Manual
   inspection must not claim machine validation that did not occur.
2. For an approval gate receive expected project/work identity and scope, purpose,
   complete current tree/base/exclusions, applicable input versions, necessary
   coverage/checks and trusted caller provenance observations. Read the **whole**
   report, selecting an explicit round ID. Verify structural validity and every
   external predicate; `passed` is a consumer outcome, never a saved report flag.
   It requires a supported valid approved round, exact subject/inputs, actual
   independence, sufficient applicable checks and no later refuting round. Multiple
   rounds/conflicting history activate `review-history.md` before deciding the gate;
   never fall back past later adverse/invalid/unknown evidence. Missing/invalid/unsupported/stale/contradictory
   reports or inaccessible required evidence give **no gate**, not an invented
   defect or pass. Report the exact unmet predicate separately from format validity.

The publisher still owns whole-tree integration/reassessment and remote/primary
sync; this format grants neither publication authority nor feature acceptance.

## Synthetic serialization example

Locators and OIDs below are illustrative, not real evidence. Syntax/shape alone
cannot establish approval. Positive applicability assumes the caller independently
resolves these exact objects, inputs, evidence and distinct invocation/authors.
The validator's existing program-test fixture reads this example here.

```yaml
schema: ris.review/1
work:
  project: example-repository
  id: example-1
  scope: Review documentation wording
rounds:
  - id: r1
    previous: null
    created_at: "2026-10-20T15:00:00Z"
    purpose: publication
    snapshot:
      repository: example-repository
      object_format: sha1
      tree: "1111111111111111111111111111111111111111"
      base: "2222222222222222222222222222222222222222"
      exclusions: []
    inputs:
      - {role: requirements, address: "example:request", version: S1, status: accepted}
      - {role: rules, address: "example:rules", version: R1, status: observed}
    provenance:
      reviewer_context: reviewer-session
      authors: [author-session]
      invocation_evidence: "example:invocation"
      independence: confirmed
      basis: Caller compared actual invocation and all authors
    coverage:
      - {area: requirements, basis: S1, outcome: pass, evidence: ["example:reading"], reason: Required wording is present}
      - {area: architecture, basis: Documentation-only scope, outcome: not_applicable, evidence: [], reason: No architecture contract changes}
      - {area: rules, basis: R1, outcome: pass, evidence: ["example:reading"], reason: Applicable rules checked}
      - {area: correctness, basis: Exact tree inspection, outcome: pass, evidence: ["example:reading"], reason: Links and meaning checked}
      - {area: tests, basis: Documentation-only scope, outcome: not_applicable, evidence: [], reason: No executable behavior changed}
      - {area: docs, basis: S1, outcome: pass, evidence: ["example:reading"], reason: Documentation matches subject}
    checks:
      - id: reading
        description: Inspect exact candidate and links
        required: true
        outcome: pass
        snapshot_tree: "1111111111111111111111111111111111111111"
        evidence: ["example:reading"]
        reason: Applicable final-tree reading
    findings:
      - id: F1
        severity: low
        status: open
        location: README.md wording
        summary: Optional shorter sentence
        basis: Readability recommendation only
        required_change: Consider shortening in a later edit
    dispositions: []
    summary: Requirements and rules checked; optional recommendation does not block
    verdict: approved
    limitations: []
```

## Optional negative reading examples

Read `report-examples.md` beside this resource only when a synthetic serialization
or negative-history illustration is needed. Routine production/consumption uses
the rules above and conditional history resource, not illustrative evidence.
