# Beads-specific ordinary native bug execution

Read before ordinary bug execution claim, versioned execution-basis read/append, fix-result
persistence or fix-completion, accepted-design source-link append, and their
prerequisite children/blocker reads.
Apply main typed read/reconcile; read/apply `claim.md`, `update.md` or
`completion.md` for the requested action, and `concurrency.md`
before dependent writes. Use the single `dolt-publication.md` method only for
separately authorized publication. This resource adds bounded capabilities, not
tasks v1 feature operations, feature-record/2, diagnosis or composition.

## Advertise the requested capability and inputs

Support exact typed **bug read**, complete **children/blocker reads**, native
**claim**, **accepted-design source-link append**, **historical basis read/locator append/reconcile**, **fix-result persistence** and
separate **exact fix-completion**. Require selected workspace, exact ID/expected
`bug`, actor for claim, authorized bounded effects and expected current state.
Basis append/result/completion additionally require the caller's sufficient report/
criteria/accepted decisions; reads do not require readiness. The caller owns
readiness and completion assessment; this adapter verifies supplied predicates
and stored effects. Never convert the bug, add an artificial parent/feature record,
or enter feature-only task APIs. Registration and investigation retain their own
conditional resources; investigation disposition is not execution completion.

- Exact `bd show <bug-id> --brief-deps --json` requires one matching native bug.
  Main compact identity reads can precede it but cannot replace the full inputs. Retrieve full
  notes, current report/criteria, decisions, assignee/status and linked sources.
- `bd list --parent <bug-id> --all --limit 0 --brief --json` covers all direct children;
  inspect relevant descendants for mandatory-scope completion. Validate actual
  parent/type/identity; unexpected children require caller reconciliation, not
  implicit execution of a container or creation of stage children.
- `bd dep list <bug-id> --type blocks --direction=down --json` supplies blockers;
  normalize blocked → blocker under main rules. Failed/truncated/unknown-shaped
  results cannot establish an empty set. Membership is not a blocking edge.
- Apply `claim.md` to this bug, including its guarded reassignment for explicit
  human continuation; otherwise use its native claim. Freshly check unblocked open/same-own state and reread
  status/assignee/children/blockers afterward and before new batches. Ownership
  CAS does not make readiness or report content atomic. Without explicit continuation
  authority preserve foreign claims; no new bug claim engine is introduced.

For an authorized design-only source update, append pinned published design and
separate decision locators with their substantive scope to notes using
`update.md` native append/standalone supplementation, without changing current report/acceptance.
Require exact bug type, actual design acceptance/publication evidence, approved
content and a stable scoped marker; reconcile marker AND full content/occurrences
before and after append and after ambiguous responses. Reuse exact prior effects;
conflicting/repeated markers stop. No concurrent append-once guarantee. This link
append needs no not-yet-selected execution basis and does not assert fix readiness
or completion. Any necessary report/acceptance replacement uses investigation's
bounded single-investigator persistence conditions, not this append capability.

## Reproducible historical execution basis

The admission owner selects the full used report/criteria/decisions, their authority,
inspected code revision and material environment. This adapter owns technical
historical retrieval, completeness comparison and locator persistence, not admission
or acceptance. A basis is selected project/tracker + exact native bug ID + exact
saved record version and necessary immutable Git commit/path/section locators.
No full duplicate notes snapshot, file, JSON/schema record or text handoff is required.
Read the full selected inputs; a hash, readiness label or inaccessible link is not enough.

### Exact historical read and comparison

For fresh admission without an existing version locator, find a saved history entry
whose full used fields match the admitted content, select its exact `CommitHash`
and independently reread/compare it below before saving the locator. If none matches,
return the unsaved/unavailable-input gap, never pin a newer nonmatching HEAD.

1. Use native `bd history <bug-id> --limit 0 --json` in the selected workspace.
   Beads 1.3.1 returns entries with `CommitHash` and a full `Issue`. Require successful,
   complete JSON; recover host-truncated output before inspecting it. Select the
   **exact** requested full `CommitHash`, never newest/nearest/current HEAD. Require
   one unambiguous matching version and `Issue.id`/`Issue.issue_type` matching the
   exact ID and `bug`. Zero matches is unavailable history; conflicting duplicates,
   unknown shapes, partial output or a wrong ID/type/version cannot establish a basis.
2. Independently retrieve that entry's entire used `description`,
   `acceptance_criteria`, `notes` and any other used decision/constraint fields.
   Compare the actual full selected content with the admission owner's used inputs,
   including report identity/investigator, original divergence, fix/regression criteria
   and accepted constraints. Missing is not empty. An omitted used field is a gap,
   even if current `show` has it; do not splice current text into a historical version.
   A demonstrably unused field need not be invented. `show --as-of <version> --json`
   is an alternative only after proving it returns **all** used fields at that exact
   version; observed 1.3.1 output omitted criteria, so flag support alone is insufficient.
3. Return the fully read inputs or their checked accessible exact locators and the
   fields/comparison covered. The consumer reads content needed for its own assessment,
   without repeating this CLI algorithm. Git sources/decisions are retrieved under
   common's published-inputs method at full commit/path/section, with actual separate
   acceptance and original decision provenance; publication is not acceptance.
   Unavailable objects/decisions or mismatching content block dependent work, not
   permission to substitute a fresh revision. No raw SQL, database clone, storage
   parser or API wrapper is needed.

### Short ordinary locator append and ambiguous retry

After a successful historical comparison, inspect current full notes for an existing
unambiguous locator addressing the **same full used basis**. Reuse it if complete;
otherwise append only missing addresses as a short ordinary note. Use a stable
project/bug-scoped marker and clearly bounded note retained on retry, not a new
runtime schema. Include exact bug/history version, used Git sources and decisions,
inspected code revision and material environment only where not already addressed
in the saved report. Unsaved material decisions go to their existing content owner
for authorized saving first; this adapter cannot invent acceptance or save it as a
locator. No description/acceptance replacement belongs to this operation.

1. Fresh-read current report/criteria/decisions, ownership and relevant blockers.
   Compare with the admitted basis; drift needs the affected owner's assessment
   before dependent effects. Compare marker **and full content/occurrences** in notes.
   One exact existing note returns unchanged. Conflicting/repeated markers, partial
   content or uncertain boundaries stop without minting a new marker to evade them.
2. Only if proven absent and authorized, use `bd --sandbox update <bug-id>
   --append-notes <short-basis-locator> --json` under `update.md`/`concurrency.md`.
   Never replace a read whole notes field. Preserve foreign notes and old snapshots.
3. Independently exact-read after success, failure or ambiguous response. Verify one
   complete exact locator, preserved prior content and current-input applicability;
   reread the pinned historical inputs if not already verified. Reconcile before any
   retry: exact present means no append, conflicting/unknown means stop, proven absent
   permits only the missing append after renewed gates. Never blindly replay.

Native append merges notes transactionally, not concurrent append-once, report+locator
atomicity or general content CAS. Claim/sandbox/read-back supply no stronger promise.
An explicitly required unsupported guarantee stops that write; do not install locks,
pause writers or invent flags. Current report/criteria replacement remains owned by
`investigation.md` with its bounded single-investigator persistence conditions.

Retain the pinned history and include it in separately authorized ordinary Dolt
publication; a local read is not remote availability. Do not flatten/rewrite history.
New sessions discover the basis from project+ID ordinary notes/source links, then
request this exact historical read without prior chat/local files. Old full snapshot
blocks stay untouched and may be used as actual recoverable historical input, not
migrated or demanded anew. Material report/criteria/decision drift needs targeted
change/review/evidence assessment and a new short locator for the newly admitted
basis, never rewriting the old version. Reuse compatible evidence with reasons;
preserve confirmed Git/closed effects without reopening, pushing or closing again.

## Separate result persistence and exact fix-completion

Persist only the authorized fix result via `update.md` native append or suitable
independent metadata keys. Include exact bug/versioned-basis locator, original criteria
coverage, actual integrated Git revision/publication receipt, checks and independent
review applicability, mandatory scope/children/blockers, limits and accessible
evidence. Preserve existing notes/decisions and reconcile marker/content on retry.
Local persistence is neither closure nor tracker publication.
For project change-review references store only local YAML address and selected
round, not a copied verdict/findings. The caller checks its applicability before
completion; keep the short fix/check/publication/completion facts distinct. Local
review availability on another machine is not promised, unlike remote bug inputs.

Then apply `completion.md` verified-work branch separately to this exact native bug: require caller's
verified real fix criteria and full mandatory-scope disposition, applicable checks/
independent review and confirmed required Git publication. Freshly inspect status,
complete mandatory children/descendants, directed blockers and external evidence;
refuse unfinished children/active blockers or insufficient completion evidence.
Use native `bd --sandbox close <bug-id> --reason <fix-result-and-evidence> --json`
with no force, status-update shortcut, auto-next or ancestor closure. Verify status,
reason, preserved result/basis locators and historical inputs, children/blockers and evidence afterward. Native
transactional direct-child/blocker checks cover only those predicates, not exact
membership, descendants or external-evidence freshness; no graph-wide freeze.

Insufficient research, proved-correct and duplicate messages cannot masquerade as
fixed bugs. Their separate investigation disposition requires its own resource.
Already closed work is not closed again or reopened: reconcile actual reason/
evidence and remaining publication only. Unknown effects require reads before
retry. Return main status envelope, exact locators, provider/covered predicates/
limits and distinct basis, result, Git, close and tracker-publication facts.
Stop at the requested bounded operation; publication is separately authorized.
