---
name: ris-proj-op-complete-container
description: >-
  Administratively close, verify fulfillment, or verify and close one exact RIS
  feature, standalone task-container or epic, according to the requested intent.
  Verification is read-only by default. Use for explicit container requests; not leaf-task completion,
  code publication, automatic parent closure or planning repair work.
---

# Close or verify one selected container

Own the requested container result. Keep administrative status, substantive
verification, evidence persistence and tracker publication distinct. This single
project owner combines project identity/authority and adapter effects; its
conditional feature assessment reuses the portable verifier, without a new base.
Load/apply `ris-proj-lib-common` and its applicable resources, and `ris-proj-op-resolve-context` with its
configuration resource for selected rules and adapter; resolve specs/product only
when assessment needs them, not as administrative prerequisites. A
direct call needs no execution role. From a worktree require context's checked
primary selection/provenance (explicit or verified available saved indication)
only if shared workspace paths are needed; no local report is mandatory.

## Select the requested result before assessment loads

- **Administrative close:** an explicit decision to close this exact container.
  Use the bounded administrative path below, with no new acceptance assessment.
- **Verify fulfillment:** read-only by default, including on a closed ID. Return
  criterion → observation/usable evidence → fulfilled / unfulfilled /
  insufficient-data. No claim, notes/metadata/verification write, close, publication
  or mandatory report file. Separate permission to save evidence does not imply
  permission to close; any expressly requested save is a separate bounded effect.
- **Verify-and-close:** assess the whole, then persist authorized evidence and close
  only on successful current verification and native closure checks.

Use natural-language intent, not a new CLI mode. If intent or ID is genuinely
ambiguous, clarify only that gap; never infer close from a verification request
or child completion. Without closing authority only read-only assessment is allowed.
Do not obtain a new design/acceptance decision merely to execute administrative close.

## Identify scope and authority

Require exact project/container ID and actual kind. Read the exact record through
the selected available adapter and confirm its supported reads/closure guarantees.
An epic has native type `epic`; a feature is a confirmed feature task associated
with its epic/spec; an ordinary task-container needs explicit subject/content
evidence. Neither a title, zero children nor absent/invalid feature JSON proves
ordinary kind. Preserve historical/malformed feature data; parser failure never
silently reclassifies it. An implementation leaf is outside this operation.

### Administrative exact-ID path

Require explicit authority/reason to close only this container. Request the
adapter's advertised tool-specific administrative exact-status close (including
feature containers), **not** `tasks.features.complete`. Freshly read exact
ID/type/status, relevant complete direct children and directed active blockers.
Use native close without force/continue/claim-next; preserve native refusal for
open direct children/live blockers. Never close children/parents, remove edges,
shrink scope or reopen a record as a workaround. Already closed returns unchanged
actual status without another close or reconstruction of acceptance.

No recursive delivery reconstruction, new substantive acceptance, Git evidence,
result persistence or verification write is a prerequisite. Feature status may
become closed while verification is null, failed, historical or malformed; leave
the entire description/block/refs/verification untouched. Exact native identity
and explicit feature-subject evidence suffice without validating published
spec/design decisions or feature-record write readiness. Unknown kind blocks
only its dependent action, not permission to guess ordinary kind.

Apply the adapter's native concurrency protocol to relevant predicates, close
one exact ID and independently read status/reason, preserved content and direct
children/blockers. Native policy is not full composition/evidence CAS. On refusal
return its bounded cause. On ambiguous/nonzero output read actual effects before
retry; retry only a proved-missing authorized effect. Confirmed close leaves only
any separately authorized publication/read-back remainder. Report explicitly:
**administrative closed is not independent acceptance of results**. Then use the
publication/result section; skip all assessment/persistence sections below.

## Verification inputs and conditional method

For verify and verify-and-close require the accepted
mandatory outcomes/member set (including any one-task feature), applicable
criteria/decisions, integrated revision evidence and allowed tracker fields.
Discover them from exact reads and linked versions before asking for missing
facts. Closing authority is needed only for verify-and-close. Missing material
inputs leave dependent criteria insufficient-data; retain independent observations.
For a feature load/apply `ris-port-op-verify-feature`. For an epic read only
`references/epic.md`; do not apply the feature method indiscriminately to children.
For an ordinary task-container read only `references/standalone.md`, applying the
portable verifier when its integrated AC require it. Resources resolve relative
to this installed folder and are not loaded on the administrative path.

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
explicitly advertised `tasks.feature-record/2` operations `tasks.features.read`,
`tasks.features.record-verification`, `tasks.features.complete` with their actual
guarantees before each needed write; assessment alone needs only reads. Read its
adapter-owned resource before use. Validate ID ↔ immutable slug ↔ spec/design
and exact accepted requirements/design reference objects: project-relative path,
full published Git revision, whole-file or unambiguous semantic section and each
result's own immutable Git acceptance address. Read both pinned content and
separate decisions; match the named content/section/revision and authorized
acceptor, resolving decision-only `containing-commit` per the adapter contract.
Confirm remote publication, not merely local object existence. Null identity,
requirements or design blocks verified completion; an early /2 record is not
malformed or ordinary. Sufficient inline design still needs a non-null accepted
design ref. Every /1 and former scope/sha256/digest-verification/history payload is
`historical/unsupported`: return its ID,
unchanged payload and diagnostic, block dependent writes and preserve the data.
Do not reinterpret, drop history or migrate on read/retry/completion. Malformed
records also block dependent writes. Another adapter may supply equivalent operations only
under an explicit compatible contract, never by assuming all v1 adapters can close.

## Verify the feature on the common revision

This section and feature-record verification mapping below apply only to the
feature branch. Standalone assessment/persistence follows its owned resource;
shared verification authority/composition/protection and channel gates apply
to assessment branches only. Epic uses its own resource without artificial feature payloads.

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

On failure or unverified material evidence, do not close. Preserve any already
closed status; never reopen/reclose to repair an acceptance gap. Return bounded
correction/decision needs for authorization by its owner; do not create a repair
task, change design or edit product inside completion. If separately authorized
and safe, persist actual failed verification as failed, replacing only authorized
current verification; Git-addressed reports retain prior evidence, not a tracker
history field. A later repair requires completed mandatory work and verification on
the new published integrated revision; do not retry closure using old success.

Map portable `pass|fail|unverified` to fulfilled / unfulfilled / insufficient-data;
use the same three verdicts for epic/standalone outcomes. An assessment verdict
reports observed fulfillment, not a new human approval. Operation status remains
`ok|blocked|conflict|error`: a completed read-only assessment can be `ok` with an
unfulfilled verdict; unavailable required assessment inputs are `blocked` with
the insufficient-data coverage and useful observations. For default **verify**,
return the unsaved assessment now: no persistence, closure or publication follows.

## Verify-and-close: persist, read back, then close

This section applies only to verify-and-close with separately authorized
persistence. An already closed ID is never closed again: assess requested scope,
report any verification gap and perform only an expressly authorized missing
evidence/publication effect. Do not rewrite history solely for a repeated call.

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

Git integration/publication is an assessment input where required, never an
administrative-close input/output and never performed here. Default verify does
not publish. For authorized write branches tracker publication
is separate: only when authorized/required use the selected adapter's publication
operation, check authorized shared-main scope and remote, suppress auto-push during
gated writes and inspect fresh selected-remote revision/reachability evidence.
Local exact-content checks remain separate from remote revision assurance. If
remote publication is required, preflight its availability/authority and outgoing
scope before dependent writes. Do not configure a remote or publish unrelated work.
Git success never proves tracker publication. A failed tracker publication leaves
the actual local evidence and closure intact; report the cause's non-`ok` status,
confirmed effects and concrete remaining publication/read-back operation. Never
repeat a confirmed closure merely because publication or its evidence is missing.

Return `status: ok|blocked|conflict|error`, project, exact ID/kind, requested intent,
scope, criterion verdict/revision where assessed (administrative: not assessed), operations/guarantees, saved vs unsaved
evidence, actual local status and separate remote publication/read-back evidence.
For assessment-only state `closed: false` or existing status, never imply completion.
Full remote-gated `ok` requires both channels independently confirmed. Stop at this
container: no parent auto-close, next task/skill launch, Git push or new workflow.
