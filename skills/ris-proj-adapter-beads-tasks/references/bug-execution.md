# Beads-specific ordinary native bug execution

Read before ordinary bug execution claim, execution-input snapshot, fix-result
persistence or fix-completion, accepted-design source-link append, and their
prerequisite children/blocker reads.
Apply main typed read/reconcile, Claim and Complete methods and `concurrency.md`
before dependent writes. Use the single `dolt-publication.md` method only for
separately authorized publication. This resource adds bounded capabilities, not
tasks v1 feature operations, feature-record/1, diagnosis or composition.

## Advertise the requested capability and inputs

Support exact typed **bug read**, complete **children/blocker reads**, native
**claim**, **accepted-design source-link append**, **snapshot append/read/reconcile**, **fix-result persistence** and
separate **exact fix-completion**. Require selected workspace, exact ID/expected
`bug`, actor for claim, authorized bounded effects and expected current state.
Snapshot/result/completion additionally require the caller's sufficient report/
criteria/accepted decisions; reads do not require readiness. The caller owns
readiness and completion assessment; this adapter verifies supplied predicates
and stored effects. Never convert the bug, add an artificial parent/feature record,
or enter feature-only task APIs. Registration and investigation retain their own
conditional resources; investigation disposition is not execution completion.

- Exact `bd show <bug-id> --json` requires one matching native bug. Retrieve full
  notes, current report/criteria, decisions, assignee/status and linked sources.
- `bd list --parent <bug-id> --all --limit 0 --json` covers all direct children;
  inspect relevant descendants for mandatory-scope completion. Validate actual
  parent/type/identity; unexpected children require caller reconciliation, not
  implicit execution of a container or creation of stage children.
- `bd dep list <bug-id> --type blocks --direction=down --json` supplies blockers;
  normalize blocked → blocker under main rules. Failed/truncated/unknown-shaped
  results cannot establish an empty set. Membership is not a blocking edge.
- Apply main **Claim** to this bug with `bd --sandbox --actor <actor> update
  <bug-id> --claim --json`. Freshly check unblocked open/same-own state and reread
  status/assignee/children/blockers afterward and before new batches. Ownership
  CAS does not make readiness or report content atomic. Preserve foreign claims.

For an authorized design-only source update, append pinned published design and
separate decision locators with their substantive scope to notes using main native
Update/standalone supplementation, without changing current report/acceptance.
Require exact bug type, actual design acceptance/publication evidence, approved
content and a stable scoped marker; reconcile marker AND full content/occurrences
before and after append and after ambiguous responses. Reuse exact prior effects;
conflicting/repeated markers stop. No concurrent append-once guarantee. This link
append needs no not-yet-created execution snapshot and does not assert fix readiness
or completion. Any necessary report/acceptance replacement uses investigation's
unchanged real-content-protection gate, not this append capability.

## Full recoverable historical execution-input snapshot

Require an approved stable execution-input identifier scoped to project/bug and
an unambiguous begin/end marker, retained on retry. The payload must contain:

- Project/tracker identity, exact bug ID and snapshot identifier/author.
- Full used report text, report identity/version/investigator, inspected code
  revision/environment and exact current-report source (description section or
  published repository/full commit/path).
- Exact agreed fix criteria, original divergence/success and affected regression
  checks, with accepted scope/constraints and their authority/source versions.
- Full substantive accepted decisions/constraints and, when required, separate
  design content and its pinned source/actual acceptance evidence. Preserve the
  distinction between accepted choices, observed facts and proposals.

The caller supplies content; do not reconstruct it from a readiness label or
hash. A locator is selected project/tracker + exact bug ID + unique snapshot
marker, retrievable by exact `show`, without ignored primary notes or chat.
References identify provenance but do not substitute for recoverable report,
criteria and decision text. This is immutable historical evidence, not another
editable current report. Do not replace description/acceptance to save it.

1. Fresh-read full notes and current report/acceptance/decision sources. Check
   supplied snapshot text still matches the caller's admitted inputs; material
   drift returns for applicability assessment before dependent execution.
2. Inspect marker **and complete content/occurrences**. One exact existing block
   returns verified unchanged. Same identifier with different/incomplete text,
   repeated markers or uncertain boundaries are conflict; do not silently pick
   a block, mint a replacement ID or append again to evade uncertainty.
3. If absent and authorized, use native `bd --sandbox update <bug-id>
   --append-notes <full-marked-snapshot> --json`, preserving all foreign notes.
   Never replay a read whole notes field. Follow main safe argument handling.
4. Independently exact-read notes and current report/criteria/decisions after
   success, failure or ambiguous output. Verify one complete exact block, preserved
   foreign content and report applicability. Reconcile an ambiguous response before
   retry; absent proven effect alone permits a bounded retry under fresh gates.
   Report repeated/conflicting blocks and partial effects without further writes.

Native append merges current notes transactionally, but is **not concurrent
append-once**, a report+snapshot transaction or general content CAS. No strict
guarantee is inferred from claim/status/sandbox/read-back. If expressly required
stronger protection is unavailable, return that exact limitation before its write;
do not install coordination, pause writers or invent flags. Investigation report/
acceptance replacements keep their stronger `investigation.md` gate unchanged.

On later material report/criteria/decision changes preserve the snapshot and pass
old/current content to the affected consumer for targeted plan/change/review/evidence
reassessment. New accepted basis needs a newly identified full snapshot. Compatible
unchanged evidence may be reused with reasons; old hashes/status do not prove it.

## Separate result persistence and exact fix-completion

Persist only the authorized fix result via main Update's native append or suitable
independent metadata keys. Include exact bug/snapshot locator, original criteria
coverage, actual integrated Git revision/publication receipt, checks and independent
review applicability, mandatory scope/children/blockers, limits and accessible
evidence. Preserve existing notes/decisions and reconcile marker/content on retry.
Local persistence is neither closure nor tracker publication.

Then apply main **Complete** separately to this exact native bug: require caller's
verified real fix criteria and full mandatory-scope disposition, applicable checks/
independent review and confirmed required Git publication. Freshly inspect status,
complete mandatory children/descendants, directed blockers and external evidence;
refuse unfinished children/active blockers or insufficient completion evidence.
Use native `bd --sandbox close <bug-id> --reason <fix-result-and-evidence> --json`
with no force, status-update shortcut, auto-next or ancestor closure. Verify status,
reason, preserved result/snapshot, children/blockers and evidence afterward. Native
transactional direct-child/blocker checks cover only those predicates, not exact
membership, descendants or external-evidence freshness; no graph-wide freeze.

Insufficient research, proved-correct and duplicate messages cannot masquerade as
fixed bugs. Their separate investigation disposition requires its own resource.
Already closed work is not closed again or reopened: reconcile actual reason/
evidence and remaining publication only. Unknown effects require reads before
retry. Return main status envelope, exact locators, provider/covered predicates/
limits and distinct snapshot, result, Git, close and tracker-publication facts.
Stop at the requested bounded operation; publication is separately authorized.
