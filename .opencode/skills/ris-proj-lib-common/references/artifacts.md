# Artifacts and handoff

Use for substantive artifacts, execution transfer and partial/uncertain effects
under the main skill's triggers, not merely for every response.
The calling skill determines the content and destination of its result; do not
invent a universal roadmap, decision log, or project path.

Use actual sources, decisions, and evidence. Distinguish drafted, saved,
checked, and accepted: a successful write does not imply acceptance, and a
structure check does not establish semantic completeness. Before editing,
inspect the existing artifact, its purpose, and the authorized scope. Preserve
valid identifiers, links, agreed constraints, and unfinished work belonging to
another task. Do not silently replace a project document or storage protocol.

For requirements/design apply common's `published-inputs.md` sufficient-basis
contract before saving, transferring or recovering content. In this resource,
accepted content/decision matching includes checked inherited sources/derivation;
an actual new decision is required only for new material, not wholly inherited
content. Preserve exact complete scopes/versions, original decisions and sources
in the substantive artifact; no separate basis file or assertion table. In mixed
results match the new decision to only its material scope in the full candidate
context. On change/loss recover source derivation and original decisions first;
only unresolved material needs a new human decision, never a fictional acceptor.
For the flow-only policy case use the contract below instead of requiring a new
human decision for a resolved candidate; explicit requested confirmation still wins.

When writing is permitted, capture material accepted decisions in the
designated artifact as work progresses, then compare the result with those
decisions before handoff. Preserve quantities, order, exclusions, and negative
requirements without weakening them. A glossary or ADR does not substitute for
requirements in the next stage's actual input. Create such extra files only
when needed and authorized.

For unpublished documents, retain the current accepted content and its separate
actual decision, with an exact version and accessible input for the next stage.
For policy acceptance in feature preparation apply `published-inputs.md`'s
flow-only policy-basis contract before saving/transferring/recovering: retain
exact scopes/versions, checked config/default provenance and attributable prepare
request/limits in the existing document/decision section. This is not human
approval or inheritance. A receiver verifies that basis, not a fictional acceptor.
Do not add a basis file, state registry or mandatory journal. Changed scopes need
their own current-mode decision; unchanged provenance remains original. Recovery
uses the actual saved basis, never retroactive acceptance from today's config.
Briefly record a material replacement: the superseded version/decision, what
changed and the new actual acceptance. Do not infer or manufacture acceptance.
No full archive of intermediate accepted snapshots, draft log, intermediate
publication or commit per acceptance is required; local drafts/commits remain
optional. Preserve published versions/decisions in Git history and their original
immutable references; copying a decision does not renew it or rebind
`containing-commit`. Recheck applicability of dependent accepted results when
inputs change; unchanged compatible content retains its original acceptance,
while materially changed content needs its own sufficient basis. Uncertainty
blocks only dependent work.

If writing is not allowed, provide the draft in the response and state that it
was not saved. If only some changes succeeded, identify saved and unsaved
parts; do not claim the downstream input is ready when it requires a saved
artifact. Respect the designated write mechanism and concurrency rules. On a
conflict, inspect current state and resolve it or report it; do not overwrite
someone else's work. Do not hold a storage lock while discussing decisions
with the user. After writing, check content and accessibility, resolving
relative links from the document's directory and paths in the recipient's
environment rather than assuming the sender's layout.

## Recoverable operation result

Use only `ok|blocked|conflict|error` for operation status: missing required input,
permission, dependency, decision or check is `blocked`; contradictory state or
concurrent change is `conflict`; technical execution failure is `error`. Partial
coverage/effects are facts, never a fifth status. `ok` means the explicitly
requested bounded operation succeeded and was checked. An expressly limited
proposal/save can be `ok` with downstream work remaining; never silently narrow
a full request to claim success or imply acceptance/publication from that `ok`.
An internal local-save/record-only boundary limits the child's contribution, not
the parent's authorized operation. Return it to the lead, who continues the
remaining route. Only the user's scoped request or an agreed scope change can
make that intermediate boundary the final requested result; a blocker preserves
the unfinished full scope instead of redefining it.

For an ordinary list, exact read or short recommendation, give the requested
outcome and material limits under common's baseline; no universal handoff is
required. Do not reconstruct versions, acceptance or channels unrelated to the
conclusion. A caller's more specific result obligations still apply.

For saved artifacts, substantive response-only candidates, execution transfer
and partial/uncertain effects, provide only information missing to the recipient
and material to continuation. Already accessible instructions/facts in the same
session need no repeated handoff. Delegates do not inherit that context: give a
bounded goal/scope, project and exact ID/copy when applicable, accessible exact
inputs/decisions, permissions, expected result and early-return conditions. They
load their own owners; do not forward the accumulated history.

The following identifies sources and responsibilities, not a runtime envelope,
required field list or new persistence requirement. Read missing full necessary inputs,
not copied summaries; reuse exact content and confirmed results already available.
Infrastructure owners perform their own algorithms; callers
check returned facts and applicability, not CLI/retry/guard procedures.

| Fact: producer → consumer | Source / mutability | Recovery |
| --- | --- | --- |
| Goal/scope/criteria: setter → change owner/reviewer | Ordinary tracker content is mutable; accepted feature scopes/decisions have immutable Git addresses | Discover by project+ID and published-input convention; recover the original decision or obtain only the lost scope's new human acceptance. |
| Paths: context → writers/copy/review | Current config and Git association are mutable | Reuse checked paths in the same environment; refresh affected association/paths after copy/environment or relevant config change. No context registry or forwarded primary address. |
| Claim/continuation rights: adapter → acting owner | Live assignment and attributable authority | Apply common's explicit-human continuation rule through the adapter without asking again; old actor/lease alone grants nothing. Fresh owner checks before mutation. |
| Copy: preparer → writer/publisher | Live registration/path/branch/HEAD/files | Consume confirmed association; invoke preparer for missing/uncertain association or setup, not each handoff. Writer checks current preservation predicates. A name alone is insufficient; nonstandard association uses an existing authorized channel. |
| Bug basis: admission+adapter → execution/review/completion | Exact tracker-history version and immutable Git sources/decisions | Adapter retrieves complete used fields and reconciles the short basis locator; no duplicate snapshot. |
| Checks: change owner → reviewer/publisher | Observation tied to exact content and inputs | Reuse accessible applicable results/limits; rerun lost reproducible affected checks, never invent their history. |
| Review: independent reviewer → loop/publisher, only when required/performed | Local append-only review.yaml and round; Fast may use session evidence | Apply the review owner's exact-evidence/new-current-review rule for required evidence. Inactive eligible Fast review creates no recovery debt or skip report; retain known adverse findings and reassess changed risks/applicability. Beads stores only file/round for a saved review, not copied verdict/findings. |
| Git publication: publisher → completion/caller | Exact commit/tree and observed remote reachability | Publisher reconciles the exact sent revision; no repeated push for lost notes/read-back or local maintenance. |
| Local output: change owner → Fast/completion | Authorized actual target state and checked useful effect, not an inert worktree replica | Recheck actual target/conflicts/effect before retry; no dummy Git SHA/copy/push for local-only. Mixed requires both own output channels. State local availability/portability limits; preserve foreign data and no automatic rollback. |
| Local maintenance authority/result: caller+publisher → caller/recovery | Explicit request or actual accepted project policy source/version/acceptance, copy/remote/ref/effects and exclusions; separately observed FF/dependency results | Caller checks applicable policy and forwards its provenance/boundaries; publisher verifies the source and current authority under primary-sync. Without either authority source keep remote-only. Preserve any required unfinished local part in the combined result without blocking separate exact close/Dolt or replaying confirmed push. Policy does not prove safety or authorize unnamed dependency effects. |
| Completion: adapter → caller | Native status/reason and ordinary result are mutable facts | Read actual result/status; reuse closed, never reopen/reclose to recover evidence. |
| Tracker publication: adapter → caller | Required exact revision and fresh remote reachability | Adapter recovers/validates that revision through its publication owner; unknown is not success or permission to replay. |

For the affected result include only material gaps or unavailable facts from:

- Full exact response-only proposal with a distinguishable version/scope, or
  exact result/evidence locator, or a checked discovery convention with all
  required keys and filename. State project/config/current-copy provenance and,
  for shared-path actions, consume context's checked association; do not carry a
  primary-root address through every handoff.
- Material input and result versions, and separate acceptance decisions with
  their actual scope/version/address. A later copy of a decision does not renew
  acceptance; unchanged decisions remain bound to their original versions.
- Distinct prepared/saved/checked/accepted facts and publication state for each
  applicable channel (e.g. Git revision/ref/remote, local tracker write, exact
  completion, tracker publication/read-back). Mark unknown/unperformed effects
  honestly; one successful channel cannot prove another.
- Actual preserved effects and evidence, the factual stopping cause, limitations,
  unsaved parts and exact unfinished operation/remainder, separately from status.
  On retry inspect real effects and current applicability before repeating an
  action; neither a status token nor a stale success marker is proof. Reuse known
  IDs/commits/closure and verify uncertain remote effects before another write;
  pending read-back does not require repeating a confirmed push or close.

No universal schema, registry, draft store or mandatory next-skill prompt is
introduced. A nested operation returns its result to its caller; transitions
belong to the caller/workflow. Do not invent IDs, commands, refs or
`workspace.tasks/<ID>` for no-ID work. Use an authorized existing source/address
when available; otherwise return the unsaved result and exact discovery gap.
An operation result or receipt is returned to the caller; it is not a required
file. Create a receipt/log artifact only when the caller or an accepted project
contract explicitly names one at an authorized address. Local notes are optional
hints, never authority or a mandatory handoff input.
For an unsaved requirements/design candidate convey exact full text or an accessible
exact file/version, plus the sufficient basis under `published-inputs.md`. Scopes
remain independently identifiable, even when one decision covers both. Consume
checked scope/basis without re-asking acceptance or repeating derivation; read
missing full content and let independent review assess it itself. Protect the
destination before saving; read back exact candidate/basis/preserved sections.
Incomplete, inaccessible, ambiguous or changed candidates return to the caller,
not guessed foreign-chat content or reformulated acceptance. Optional candidate
files need authority; no intermediate file/publication is required.
These explicit transfers concern intermediate unsaved/not-yet-discoverable results,
not a new session consuming a completed saved stage. For the latter apply common's
`published-inputs.md`: project plus exact ID/saved associations must discover the
content and decisions without a prior chat or receipt. Response-only content
requires explicit forwarding to a new session. Local
notes are usable only where accessible, never mandatory remote inputs for another
copy. A receiver resolves only missing/changed local paths and checks the current
action's content/version applicability, fresh permissions and required ownership,
blockers and write guarantees; it does not repeat a universal entry preflight.
Neither a handoff, old lease/window nor existing worktree supplies those gates.

For partial results report the existing effect separately from the evidence
available now, its limits and the first missing/inapplicable operation. Let the
same owner reconcile an uncertain effect before retry. Lost checks/review or
acceptance cannot erase a confirmed push/closed status or manufacture historical
pass. Unknown ownership, setup or a remaining process blocks dependent mutation
with that precise gap, not a demand for a replacement journal.
