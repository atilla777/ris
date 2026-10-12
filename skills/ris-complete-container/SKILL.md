---
name: ris-complete-container
description: >-
  Verify and explicitly close one RIS feature or epic container, persisting
  criterion and revision evidence through the selected task adapter. Use for
  requested container completion after integration; not leaf-task completion,
  code publication, automatic parent closure or planning repair work.
---

# Verify and complete one selected container

Own the combined project result: verified mandatory scope, acceptance evidence,
safe persistence and separately verified closure of the exact authorized ID.
Load/apply `ris-common` and its applicable resources, and `ris-context` with its
configuration resource for selected rules/specs/product and adapter paths. A
direct call needs no execution role. From a worktree require explicit primary
root only if shared workspace paths are needed; no local report is mandatory.
For a feature load and actually apply `ris-verify-feature-base`. For an epic
instead read `references/epic.md` relative to this installed folder; do not load
the feature method merely because the epic contains features.

## Identify scope and authority

Require exact project/container ID and kind, completion permission, the accepted
mandatory outcomes/member set (including any one-task feature), applicable
criteria/decisions, integrated revision evidence and allowed tracker fields.
Do not infer the kind from a title or zero children: a feature is the confirmed
feature task linked to its epic/spec, an epic is its actual tracker type.
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
guarantees. Read its adapter-owned resource before use. Validate ID ↔ immutable
slug ↔ spec/design and separate accepted scoped versions/decisions. A legacy or
malformed record blocks dependent writes; do not fabricate a slug or migrate it
as a completion shortcut. Another adapter may supply equivalent operations only
under an explicit compatible contract, never by assuming all v1 adapters can close.

## Verify the feature on the common revision

Read accepted requirements/design from the published integrated Git tree, compare
their scoped versions to the record and retrieve their approved decision evidence.
Confirm the actual integration target and remote-backed revision; local push output
alone is insufficient. Reassess target drift and evidence applicability. Supply
these inputs, the complete AC set, architecture/contracts, linked source baselines,
current sources and actual check evidence to `ris-verify-feature-base`; use its
assessment rather than merely mentioning it. Check that the returned coverage
and integration/architecture/docs outcomes all belong to that exact revision.

On failure or unverified material evidence, leave the feature open. Return bounded
correction/decision needs for authorization by its owner; do not create a repair
task, change design or edit product inside completion. If separately authorized
and safe, persist actual failed verification as failed, preserving previous
evidence. A later repair requires completed mandatory work and verification on
the new published integrated revision; do not retry closure using old success.

## Persist, read back, then close

Before each dependent write establish the adapter-required conditional guarantee
covering this record, mandatory membership, blockers and evidence through read-back.
Identify its provider, scope and duration. A claim/lease, worktree, sandbox, local
lock or read/write/read does not exclude remote writers. Missing/expired guarantee
means `conflict` without that write; useful read-only verification can continue.
Re-read the exact record/children/blockers and compare with the verified expected
state immediately before each operation; changed facts invalidate dependent approval.

Map the method's result to the adapter-owned verification representation, including
all slug-qualified AC, actual outcomes/check addresses, full Git SHA, both accepted
digests, integration/architecture/docs and limitations. Evidence and decisions must
be accessible to another session, not depend solely on an ignored local report.
Preserve prior verification/history and unrelated content through the adapter.
Call `record-verification` only with authorized fields and verify exact complete
read-back before considering closure. Recording evidence does not close the task.

Close only if full mandatory scope is completed, no active blockers remain, all
criteria and required checks pass, evidence is usable/current and the exact ID is
authorized for closure. Reconfirm the final published integrated revision and still
accepted scopes; call `complete` separately, then reread status, close reason,
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
