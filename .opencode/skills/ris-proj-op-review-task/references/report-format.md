# Project review report — `ris.review/2`

Read before producing, saving or consuming a project review **file**, including
an optional fast save. This resource alone owns serialization, history and gate
semantics; portable review owns assessment. New files use /2. Only when an
existing file declares `ris.review/1`, read `report-format-v1.md` beside this file
and continue its original contract without rewriting/migrating it. One file has
one schema; unknown versions are unsupported, never approval. Ordinary /2 does
not load the conditional /1 resources.

## Read-only mechanical validator

Use Python **>=3.10** and **ruamel.yaml==0.18.16**, the pure-Python safe YAML 1.2
loader pinned in this skill's `requirements.txt`. Dependency installation needs
separate explicit authority, never a validator side effect. Choose an authorized
venv location and the actual source or installed skill folder:

```sh
skill='/absolute/path/to/.opencode/skills/ris-proj-op-review-task'
python3 -m venv /authorized/path/review-venv
/authorized/path/review-venv/bin/python -m pip install -r "$skill/requirements.txt"
/authorized/path/review-venv/bin/python -B "$skill/scripts/validate_review.py" /absolute/path/review.yaml
```

CLI: `python -B <skill>/scripts/validate_review.py <review.yaml>`.
Exit **0**: valid format only; **1**: invalid (including non-UTF-8);
**2**: unsupported schema; **3**: operational/setup error (usage, I/O, unsupported
Python or unavailable/incompatible dependency). Diagnostics identify a YAML
line/column or field path and reason. Both /1 and /2 use this same CLI. Nothing is
written, repaired, installed, fetched or published; Git, Beads, network and agents
are not needed. Missing setup is not invalidity or pass. Manual substantive
inspection remains possible but is not machine validation.

The program checks exact types, intrinsic history and declared contradictions.
It cannot compare old file bytes for append-only saving, establish truthful prose,
adequate checks, real independence, Git/source accessibility or external approval.

## Storage and authority

Ordinary review saves one local `review.yaml`, by default at context-checked
`workspace.tasks/<confirmed-ID>/review.yaml` in the source folder. Without an ID,
require an explicit authorized local address; never invent a task. Beads holds
only address/round, not verdict/findings. No Markdown twin, second review registry,
implementation log or automatically published evidence. Availability on another
machine is not promised. Fast retains independent session-only review; optional
save follows this same schema-selection rule.

Before appending, freshly read/compare the existing complete file and preserve
work identity and all prior round bytes. Append one complete round; independently
read back the whole result. Conflict, partial/unparseable save or changed prior
bytes blocks the gate: reconcile, never overwrite another writer. Fresh comparison
and read-back are not filesystem CAS. Never rewrite old approval after a repair.

If the local report is lost, recover the exact accessible evidence unchanged or
conduct new independent review of the exact available subject with current time
and actual provenance. Do not invent historical approval before an earlier push.
If the old tree is unavailable, identify the current reviewed tree honestly.
Lost reproducible checks are rerun as needed; already published/closed effects
remain facts, not reasons to replay push/close. Broader recovery stays with its owner.

## Exact YAML mappings

One UTF-8 YAML 1.2 document. Reject duplicate/merge keys, anchors/aliases, custom
tags and scalar types other than string, boolean, integer and null. Mapping keys
are strings. No coercion or discarded unknown fields. Each mapping has **exactly**
the keys below; every field is required. Strings are nonempty/non-whitespace;
null is allowed only where stated. Arrays can be empty except `rounds`.

| Mapping | Required fields and types |
| --- | --- |
| root | `schema`: literal `ris.review/2`; `work`: Work; `rounds`: nonempty chronological array of Round |
| Work | `project`: repository/project locator string; `id`: string or null for no-ID; `scope`: string |
| Round | `id`: unique string; `created_at`: RFC3339 string with timezone; `purpose`: `analysis` or `publication`; `snapshot`: Snapshot; `inputs`: array of Input; `provenance`: Provenance; `assessment`: string; `checks`: array of Check; `findings`: array of new Finding; `dispositions`: array of Disposition; `verdict`: `approved`, `changes_required` or `blocked`; `limitations`: array of Limitation |
| Snapshot | `object_format`: `sha1` or `sha256`; `base`: full commit OID string or null only for analysis; `tree`: full tree OID string; `exclusions`: array of Exclusion |
| Exclusion | `path`: exact repository-relative path string; `reason`: string |
| Input | `role`, `address`, `version`: strings; `status`: `accepted`, `observed` or `proposed` |
| Provenance | `reviewer_context`: string; `authors`: array of unique context/actor strings; `invocation_evidence`: address string or null; `independence`: `confirmed`, `unverified` or `self` |
| Check | `description`: string; `required`: boolean; `outcome`: `pass`, `fail`, `unverified` or `not_applicable`; `evidence`: array of address strings |
| Finding | `id`: globally unique stable string; `severity`: `high`, `medium` or `low`; `location`: file/symbol/artifact scope string; `description`: string including cause and necessary correction |
| Disposition | `finding_id`: prior open finding ID string; `decision`: `fixed`, `not_a_defect`, `deferred` or `accepted_recommendation`; `basis`: substantive string |
| Limitation | `description`: string; `blocks_approval`: boolean |

`assessment` covers applicable requirements, architecture, rules, correctness,
tests and documents in one coherent evaluation, explaining gaps/inapplicability.
There are no six fixed coverage mappings, per-check `snapshot_tree`, `previous`,
duplicated finding prose fields or repeated prior findings. Requirements and
rules/quality remain substantively distinguishable. Inputs identify used versions
and actual acceptance decisions where required; a missing mandatory input cannot
be concealed as inapplicable. Empty inputs/checks require sufficient substantive
grounds in the assessment, not invented results. A pass check requires nonempty
evidence; description/assessment explains failure, unverified or inapplicability.
An unavailable mandatory tool is not `not_applicable`. Checks inherit the round
tree and describe assessed reviewer/current results, not author RED/GREEN history.

## Subject, history and fold

- OIDs are lowercase hex of exactly 40/64 characters for sha1/sha256. Repository
  comes from `work.project`. `tree` identifies the complete subject (unchanged
  base plus additions/deletions/content/modes), not HEAD-only or a dirty fingerprint.
  Publication needs a non-null base. Null permits analysis, not invented delta.
  The CLI checks shape only; the caller resolves the actual objects/repository.
- WIP is not HEAD. Use the existing snapshot owner for an exact prospective tree
  without altering foreign index/worktree or making a commit solely for review.
  Declare exact exclusions before assessment: no absolute/empty/`.`/`..` path
  components. Excluded dirty tracked files retain base bytes/modes in the tree.
  Compare the actual complete publishing tree/base/exclusions. Saving ignored
  evidence does not alter it; loose objects are not a durable backup.
- Read **all rounds**, in array order, with unique round IDs and nondecreasing
  RFC3339 instants (timezone/fraction aware). No forks, renumbering or fallback.
  The array replaces `previous`. Save-time preservation of earlier bytes is an
  external obligation; a standalone validator cannot prove it.
- Fold findings/dispositions in order. A new finding opens a never-before-used ID;
  it cannot repeat/redefine a prior finding or be disposed in its introducing
  round. A disposition references an open finding from a prior round, at most
  once per round. `fixed` and `not_a_defect` close it after reasoned reviewer
  assessment; `deferred` closes low only and leaves high/medium open.
  `accepted_recommendation` is low-only and closes that recommendation. Closed IDs
  cannot be disposed again/reopened; rediscovery gets a new ID with the prior
  reference in its description. Neither findings nor dispositions are recopied
  into later rounds. An unresolved high/medium persists even when omitted.
- Low can receive a collective reasoned session decision without creating a new
  round for low alone; reflect it in the next assessment when another round is
  otherwise needed. Open low does not prevent approval.
- Reviewer/context in `authors` requires `independence: self`; otherwise overlap
  is invalid. `confirmed` requires non-null invocation evidence. The caller checks
  actual launch and **all** authors/repairers: names/roles/declarations are not
  proof. Self-review can be blocked/adverse analysis, never independent approval.

## Machine verdict and external gate

| `verdict` | Mechanical consistency and consumer action |
| --- | --- |
| `approved` | No folded open high/medium, required failed/unverified checks or blocking limitations; confirmed independence. Do not repeat implementation/review when this is valid, applicable and actually independent for the exact subject. |
| `changes_required` | Established actionable violation: folded open high/medium or required failed check. Send corrections to the implementation owner, then new independent review. Retain additional evidence gaps as limitations. |
| `blocked` | No established actionable violation, but insufficient required input/access/evidence/independence/applicability. Stop dependent progression to obtain the missing fact, not an endless implementation loop. |

Mandatory violations not expressed by a failed check need an actionable high/medium
finding. A sufficient-looking blocked report does not grant approval: adequacy of
its explanation is assessed externally. Do not infer a branch from prose, or add
duplicate `repeat`/`passed`/`latest` flags. GAS City is a future consumer, not a
loop script or business-metadata owner in this package change.

Two separate results are required:

1. **Format:** the whole file's syntax/schema/types/OIDs/history/declared verdict
   consistency, via the CLI when available. Exit 0 includes valid adverse/blocked
   files and is never approval. Invalid/unsupported/setup errors stop dependent
   progression; never ignore a malformed tail or silently select another schema.
2. **Approval applicability:** caller supplies expected project/work/scope,
   publication purpose, complete current tree/base/exclusions, applicable input
   versions, sufficient assessment/checks and trusted invocation/all-author
   observations. Select an explicit round, resolve actual evidence and compare
   every predicate. A later refuting, adverse/blocked, invalid or unknown round
   forbids falling back to old approved; reconcile or obtain fresh independent
   assessment of the exact subject. Missing/stale/inaccessible/unverified evidence
   means **no gate**, not an invented defect/pass or automatic repair loop.

The publisher retains whole-tree integration/reassessment and publication authority.
This report is neither feature acceptance nor proof of historical operations.

## Synthetic serialization example

Illustrative locators/OIDs, not real evidence or approval. External applicability
would require independently resolving the exact subject, inputs and invocation.

```yaml
schema: ris.review/2
work: {project: example-repository, id: example-1, scope: Review documentation wording}
rounds:
  - id: r1
    created_at: "2026-10-22T10:00:00Z"
    purpose: publication
    snapshot:
      object_format: sha1
      base: "2222222222222222222222222222222222222222"
      tree: "1111111111111111111111111111111111111111"
      exclusions: []
    inputs:
      - {role: requirements, address: "example:request", version: S1, status: accepted}
      - {role: rules, address: "example:rules", version: R1, status: observed}
    provenance:
      reviewer_context: reviewer-session
      authors: [author-session]
      invocation_evidence: "example:invocation"
      independence: confirmed
    assessment: >-
      Requirements and rules checked; final wording and links are correct.
      No architecture or executable changes; program tests are inapplicable.
      Documentation matches the requested scope.
    checks:
      - {description: Inspect exact candidate and links, required: true, outcome: pass, evidence: ["example:reading"]}
    findings: []
    dispositions: []
    verdict: approved
    limitations: []
```
