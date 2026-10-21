---
name: ris-proj-op-complete-container
description: >-
  Close from completed direct children, verify fulfillment, or verify and close one exact RIS
  feature, standalone task-container or epic, according to the requested intent.
  Verification is read-only by default. Use for explicit container requests; not leaf-task completion,
  code publication, automatic parent closure or planning repair work.
---

# Close or verify one selected container

Own the requested container result. Keep child-based closure, administrative status, substantive
verification, evidence persistence and tracker publication distinct. This single
project owner combines project identity/authority and adapter effects; its
conditional feature assessment reuses the portable verifier, without a new base.
Load/apply `ris-proj-lib-common` and its applicable resources, and `ris-proj-op-resolve-context` with its
configuration resource for selected rules and adapter; resolve specs/product only
when assessment needs them, not as ordinary or administrative close prerequisites. A
direct call needs no execution role. From a worktree require context's checked
primary selection/provenance through context's explicit → verified saved →
verified ordinary Git source-copy procedure
only if shared workspace paths are needed; no local report is mandatory.

## Select the requested result before assessment loads

- **Close (default for a closure request):** for a parent with direct children,
  use the short child-based path below. “Close the feature/epic” or “check whether
  it can be closed” does not request a new substantive acceptance assessment.
  A feasibility-only question uses the same bounded reads without any write.
- **Administrative close:** an explicit decision to close this exact container.
  Use the bounded administrative path below, with no new acceptance assessment.
- **Verify fulfillment:** read-only by default, including on a closed ID. Return
  criterion → observation/usable evidence → fulfilled / unfulfilled /
  insufficient-data. No claim, notes/metadata/verification write, close, publication
  or mandatory report file. Separate permission to save evidence does not imply
  permission to close; any expressly requested save is a separate bounded effect.
- **Verify-and-close:** assess the whole, then close
  only on successful current verification and native closure checks.

Use natural-language intent, not a new CLI mode. Do not require the user to say
“administratively” to get ordinary child-based closure. Explicit “verify fulfillment”
or “verify-and-close” selects substantive assessment; a mere closure-feasibility
check does not. If intent or ID is genuinely
ambiguous, clarify only that gap; never infer close from a verification request
or child completion. Without closing authority only the requested read-only check is allowed.
Do not obtain a new design/acceptance decision merely to execute administrative close.

## Identify scope and authority

Require exact project/container ID and actual kind. Read the exact record through
the selected available adapter and confirm its supported reads/closure guarantees.
An epic has native type `epic`; a feature is a task confirmed by explicit selected
scope, actual content/source association and relevant native relationships, with
optional epic; an ordinary task-container needs explicit subject/content
evidence. Neither a title, zero children nor absent/invalid feature JSON proves
ordinary kind. Preserve historical/malformed feature data; parser failure never
silently reclassifies it. An implementation leaf is outside this operation.

### Ordinary child-based exact-ID path

Freshly read the exact parent ID/type/status, its complete all-status **direct**
children and the parent's directed active blockers through the selected adapter.
For an already closed ID report unchanged status without another close or acceptance
reconstruction. Otherwise require a nonempty direct-child list, every child in
`closed` status and no active parent blocker. Unknown/incomplete reads block the
conclusion; cancelled/deferred/open children are not `closed` substitutes.

Trust the children's completion statuses. Do not recurse into descendants, inspect
child blockers, repeat child checks/reviews, read accepted specs/design, reconstruct
Git deliveries, audit decomposition completeness or require a new criterion report,
verification record, claim, worktree or independent reviewer. Missing historical
evidence is not a blocker for this path. This proves completion of the recorded
direct children, not a new independent acceptance of the whole or proof that all
conceivable work was recorded. Leave description, historical payloads and evidence
unchanged. Do not reinterpret this result as successful substantive verification.

For feasibility-only requests report eligible/not eligible and any open child or
active blocker, then stop read-only. For an authorized close, request the adapter's
ordinary child-based exact-container close, not verified-work completion. Use its
fresh native child/blocker guards, close only this ID without force, independently
reread status/reason and direct children/blockers, then apply the separate tracker
publication section. On refusal or ambiguous output reconcile actual effects before
retrying only a proved-missing effect. Never close children/ancestors or remove edges.

**No vacuous success:** an open feature with zero children may represent a one-task
implementation. Its ordinary closure must assess its own result using the feature
verification/verified-close sections below (closure authority already comes from
the request); execution's checks, independent review and Git gates stay intact.
A zero-child epic/ordinary container is not eligible for child-based close: report
the absence and use substantive assessment or an explicitly requested administrative
decision, never invent children or silently take the administrative shortcut.
Feasibility-only requests stay read-only and report that own-result assessment is
needed; do not launch it unless requested. Skip all assessment resources for the
nonempty child-based path.

### Administrative exact-ID path

Require explicit authority/reason to close only this container. Request the
adapter's advertised tool-specific administrative exact-status close (including
feature containers), not verified-work completion. Freshly read exact
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

Only for explicit verify/verify-and-close or own-result closure of a zero-child feature require the accepted
mandatory outcomes/member set (including any one-task feature), applicable
criteria/decisions, integrated revision evidence and allowed tracker fields.
Discover them from exact reads and linked versions before asking for missing
facts. Closing authority is needed for verify-and-close or own-result close. Missing material
inputs leave dependent criteria insufficient-data; retain independent observations.
For a feature load/apply `ris-port-op-verify-feature`. For an epic read only
`references/epic.md`; do not apply the feature method indiscriminately to children.
For an ordinary task-container read only `references/standalone.md`, applying the
portable verifier when its integrated AC require it. Resources resolve relative
to this installed folder and are not loaded on the administrative path.

Load the selected adapter from its actual available location. Verify operation
versions, completeness and guarantees before using it, not merely its configured
name. Use complete all-status selections, exact reads, recursive child membership
and directed blockers to verify actual identity and full mandatory scope. These are
assessment-only requirements, never prerequisites to ordinary child-based close. Compare
expected outcomes/members to actual records; absence of open children cannot
establish that missing mandatory work was done. A cancelled member needs explicit
scope disposition/acceptance, not treatment as completed. Unexpected membership
or content is a conflict; do not silently reparent, shrink scope or create tasks.
Check active blockers on the container and mandatory members. Four closed children
are useful completion facts, not feature acceptance or permission to close parents.

For features require native exact item/children/dependency reads and verified-work
exact closure with advertised actual guarantees; assessment alone needs only reads.
Apply common's published-inputs document convention: new feature requirements at
`sources.specs/<full feature ID>/spec.md`, sufficient independently accepted inline
or adjacent design. Read both actual content scopes and separate attributable
decisions at exact published revisions; match path/section/version/acceptor and
resolve `containing-commit` at its original decision. Confirm remote publication,
not local file/object existence. Legacy explicit links and readable payload paths
are only hints to actual documents/decisions. Missing/old/malformed JSON alone is
no blocker; missing substantive inputs or ambiguous identity is. Preserve all old
data; no schema validation, migration or substitute registry is required.

## Verify the feature on the common revision

This section applies only to the
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

## Verify-and-close: assess, then exact close

This section applies to authorized verify-and-close and own-result closure of a
zero-child feature, not ordinary child-based close. No saved verification or
readiness record, report file or evidence-write permission is prerequisite. A
short ordinary outcome may be included in the close reason; any separately
requested save stays a distinct bounded effect. An already closed ID is never closed again: assess requested scope,
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

Consume the actual unsaved criterion assessment: all feature-qualified AC,
observations/checks, integrated Git SHA, applicable independently accepted content,
integration/architecture/docs and limitations. Do not encode duplicate refs or
verification in Beads or require a persisted assessment before closing. Preserve
historical payloads, explicit links and unrelated content unchanged.

Close only if full mandatory scope is completed, no active blockers remain, all
criteria and required checks pass, evidence is usable/current and the exact ID is
authorized for closure. Reconfirm the final published integrated revision and still
accepted content/decisions and actual applicability; call native verified-work close
using the adapter's native closure guards and fresh checks, then reread status, close reason,
unchanged evidence/identity, membership and blockers. On ambiguous/nonzero results
inspect actual persisted effects before deciding recovery; no blind retry or force.
If already closed, verify existing evidence/scope and report unchanged status,
not a new closure; do not rewrite history solely for a repeated call.

## Publication and result

Git integration/publication is an assessment input where required, never an
ordinary child-based or administrative-close input/output and never performed here. Default verify does
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

For ordinary child-based close/eligibility keep the result brief: exact ID,
closed/total direct children, parent blockers, eligible/not eligible/unknown,
actual status and (only for writes) separate tracker publication confirmation or
remainder. State that whole-result acceptance was not reassessed; no formal report
or unrelated revision/acceptance reconstruction is needed.

For substantive assessment/administrative branches return
`status: ok|blocked|conflict|error`, project, exact ID/kind, requested intent,
scope, criterion verdict/revision where assessed (child-based/administrative: not assessed), operations/guarantees, saved vs unsaved
evidence, actual local status and separate remote publication/read-back evidence.
For assessment-only state `closed: false` or existing status, never imply completion.
Full remote-gated `ok` requires both channels independently confirmed. Stop at this
container: no parent auto-close, next task/skill launch, Git push or new workflow.
