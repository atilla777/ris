---
name: ris-proj-op-complete-container
description: >-
  Verify and explicitly close one RIS feature, standalone task-container or epic, persisting
  criterion and revision evidence through the selected task adapter. Use for
  requested container completion after integration; not leaf-task completion,
  code publication, automatic parent closure or planning repair work.
---

# Verify and complete one selected container

Own the combined project result: verified mandatory scope, acceptance evidence,
safe persistence and separately verified closure of the exact authorized ID.
Load/apply `ris-proj-lib-common` and its applicable resources, and `ris-proj-op-resolve-context` with its
configuration resource for selected rules/specs/product and adapter paths. A
direct call needs no execution role. From a worktree require context's checked
primary selection/provenance (explicit or verified available saved indication)
only if shared workspace paths are needed; no local report is mandatory.
For a feature load and actually apply `ris-port-op-verify-feature`. For an epic
instead read `references/epic.md` relative to this installed folder; do not load
the feature method merely because the epic contains features. For an explicitly
identified ordinary standalone task-container instead read `references/standalone.md`
before assessment or persistence; it owns that branch and applies the portable
feature verifier only when the subject has feature-like integrated AC.

## Identify scope and authority

Require exact project/container ID and kind, separate permission to close this
container (not inferred from child completion or permission to record evidence), the accepted
mandatory outcomes/member set (including any one-task feature), applicable
criteria/decisions, integrated revision evidence and allowed tracker fields.
Do not infer the kind from a title or zero children: a feature is the confirmed
feature task linked to its epic/spec, an epic is its actual tracker type, and
a standalone task-container is explicitly established by ordinary accepted
content/sources and mandatory composition. Discover these from exact ID reads
and linked accepted versions before asking for missing facts. A malformed or
historical feature payload is not reclassified as standalone.
A leaf implementation task is outside this operation. Read-only assessment is
possible without closing permission; return unsaved results and do not mutate.

Load the selected adapter from its actual available location. Verify operation
versions, completeness and guarantees before using it, not merely its configured
name. Use complete all-status selections, exact reads, recursive child membership
and directed blockers to verify actual identity and full mandatory scope. Compare
expected outcomes/members to actual records; absence of open children cannot
establish that missing mandatory work was done. A cancelled member needs explicit
scope disposition/acceptance, not treatment as completed. Unexpected membership
or content is a conflict; do not silently reparent, shrink scope or create tasks.
Check active blockers on the container and mandatory members. Four closed children
are useful completion facts, not feature acceptance or permission to close parents.

For features require `tasks` v1 reads of items/children/dependencies and the
explicitly advertised `tasks.feature-record/1` operations `tasks.features.read`,
`tasks.features.record-verification`, `tasks.features.complete` with their actual
guarantees before each needed write; assessment alone needs only reads. Read its
adapter-owned resource before use. Validate ID ↔ immutable slug ↔ spec/design
and exact accepted requirements/design reference objects: project-relative path,
full published Git revision, whole-file or unambiguous semantic section and each
result's own immutable Git acceptance address. Read both pinned content and
separate decisions; match the named content/section/revision and authorized
acceptor, resolving decision-only `containing-commit` per the adapter contract.
Confirm remote publication, not merely local object existence. A null design
blocks completion. Former scope/sha256/digest-verification/history payloads are
`historical/unsupported` despite the same `/1` schema/markers: return their ID,
unchanged payload and diagnostic, block dependent writes and preserve the data.
Do not reinterpret, drop history or migrate on read/retry/completion. Malformed
records also block dependent writes. Another adapter may supply equivalent operations only
under an explicit compatible contract, never by assuming all v1 adapters can close.

## Verify the feature on the common revision

This section and feature-record verification mapping below apply only to the
feature branch. Standalone assessment/persistence follows its owned resource;
shared authority/composition/protection, separate closure and channel gates apply
to every kind. Epic uses its own resource without artificial feature payloads.

Read the actual requirements/design at their accepted pinned revisions and at the
published integrated Git tree. Compare applicable content with diff plus semantic
section review and retrieve separate decision evidence. Same labels/references
alone do not establish applicability; editorial or unrelated shared-file changes
need not invalidate an unchanged accepted result. Material or uncertain changes
block acceptance and return to the relevant owner without repinning old refs.
Confirm the actual integration target and remote-backed revision; local push output
alone is insufficient. Reassess target drift and evidence applicability. Supply
these inputs, the complete AC set, architecture/contracts, linked source baselines,
current sources and actual check evidence to `ris-port-op-verify-feature`; use its
assessment rather than merely mentioning it. Check that the returned coverage
and integration/architecture/docs outcomes all belong to that exact revision.

On failure or unverified material evidence, leave the feature open. Return bounded
correction/decision needs for authorization by its owner; do not create a repair
task, change design or edit product inside completion. If separately authorized
and safe, persist actual failed verification as failed, replacing only authorized
current verification; Git-addressed reports retain prior evidence, not a tracker
history field. A later repair requires completed mandatory work and verification on
the new published integrated revision; do not retry closure using old success.

## Persist, read back, then close

Before each dependent write apply the adapter's bounded native-operation protocol
and identify actual guarded predicates and limits. Use targeted persistence and
native exact close with fresh substantive composition/evidence checks; require
no manual window, global lock or graph/external-evidence transaction. A claim/lease,
worktree, sandbox or read/write/read does not exclude remote writers. An explicitly
required stronger unsupported guarantee blocks only its dependent write.
Re-read the exact record/children/blockers and compare with the verified expected
state immediately before each operation; changed facts invalidate dependent approval.

Map the method's result to the adapter-owned verification representation, including
all slug-qualified AC, actual outcomes/check addresses, full Git SHA, both accepted
reference objects (including their separate acceptance addresses),
integration/architecture/docs and limitations. Evidence and decisions must
be accessible to another session, not depend solely on an ignored local report.
Store the exact references as `verification.requirements` and
`verification.design`, matching the feature record. Preserve the accepted refs,
immutable identity and unrelated content; do not add digest fields or decision
history. Replace only authorized current verification through the adapter.
Call `record-verification` only with authorized fields and verify exact complete
read-back before considering closure. Recording evidence does not close the task.

Close only if full mandatory scope is completed, no active blockers remain, all
criteria and required checks pass, evidence is usable/current and the exact ID is
authorized for closure. Reconfirm the final published integrated revision and still
accepted references and actual content applicability; call `complete` separately
using the adapter's native closure guards and fresh checks, then reread status, close reason,
unchanged evidence/identity, membership and blockers. On ambiguous/nonzero results
inspect actual persisted effects before deciding recovery; no blind retry or force.
If already closed, verify existing evidence/scope and report unchanged status,
not a new closure; do not rewrite history solely for a repeated call.

## Publication and result

Git integration/publication is an input, not performed here. Tracker publication
is separate: only when authorized/required use the selected adapter's publication
operation, inspect the entire outgoing scope and remote, suppress auto-push during
gated writes and independently read the selected remote from another copy. If
remote publication is required, preflight its availability/authority and outgoing
scope before dependent writes. Do not configure a remote or publish unrelated work.
Git success never proves tracker publication. A failed tracker publication leaves
the actual local evidence/status as partial; report them and concrete recovery.

Return `status: ok|blocked|conflict|partial|error`, project, exact ID/kind, mandatory
scope, criterion verdict and revision, operations/guarantees, saved vs unsaved
evidence, actual local status and separate remote publication/read-back evidence.
For assessment-only state `closed: false` or existing status, never imply completion.
Full remote-gated `ok` requires both channels independently confirmed. Stop at this
container: no parent auto-close, next task/skill launch, Git push or new workflow.
