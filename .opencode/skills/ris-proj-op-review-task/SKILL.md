---
name: ris-proj-op-review-task
description: >-
  Review one bounded RIS project change, with or without a task ID, and return
  checked findings and one local YAML report in the ordinary project route. Use for
  project code or document review and focused re-review; not fixing findings, feature design approval,
  publication or tracker completion. Self-review does not supply independent approval.
---

# Review one project change

Own the checked project report. Load/apply `ris-proj-lib-common` with applicable resources,
`ris-proj-op-resolve-context` for applicable project rules and, only when needed,
specs, selected adapter or shared report paths, and `ris-port-op-review-change`
for the assessment. Check dependency availability and actual results. A direct invocation
needs no execution role or scenario skill.

Fast calls this owner only for its active review branch (explicit human request,
mandatory applicable target-project policy or explained concrete material risk).
This includes suitable natural selection of `ris-proj-flow-execute-simple-task`,
not only a slash command. The flow owns applicability; this review owner neither
starts unsolicited review nor cancels a requested direct assessment. Conditional
Fast review does not weaken this owner's substantive/independence gates or the
full/feature/bug/direct review contracts. Self-check is never independent approval.

Before producing/saving a project review **file** or consuming saved rounds, read
`references/report-format.md` from this installed skill. It is the sole owner of
supported serialization, types, history and approval applicability. New files use
`ris.review/2`; existing /1 files continue under its conditional compatibility resource. Ordinary
project review requires that complete YAML; selected Fast execution alone permits
a sufficient session result without a file. An optional fast save uses the same
format. No duplicate Markdown report or Beads verdict/findings copy.
Use that resource's skill-local validator/setup instructions for mechanical file
checks when available; keep operational/dependency errors separate from report
invalidity. It neither establishes external evidence/independence nor replaces
this assessment. Never install its dependency silently.
For selected Fast session-only review, apply the portable assessment and this
skill's subject/independence gates without loading YAML serialization resources.
Read `references/bug-subject.md` only for a supplied native bug, before selecting
its document versus fix-implementation basis. Read resources relative to this
installed skill folder; reuse already available current instructions.

Establish the exact project, attributable agreed request, boundaries/criteria,
accepted technical constraints/material decisions, requested review scope/version
and review/gate purpose. Identify the current copy, branch, baseline and complete
concrete candidate, including additions, deletions and modes, plus checks/results
and their applicability limits. A sufficient request may supply this substance
directly: spec/design/plan files are not inherently required. Missing material
inputs or baseline limit the affected conclusion, never become approval; continue
useful current-content analysis. Do not invent a feature design for a small repair.
Verify actual candidate bytes rather than approving HEAD alone or assuming an
absent change from missing local evidence. A stale handoff is not a current input.
Analysis requires neither claim mutation nor report-write permission.

For requirements/design independently assess each full scope/version and its
sufficient basis under common's `published-inputs.md`, including derivation and
original authority/applicability, not mere compatibility. Use supplied exact
locators; do not repeat discovery. Policy basis needs its actual flow/config/
overrides; it is not human approval or inheritance. Wholly inherited content needs
no new acceptor; unresolved material choices return to the human. Review never
supplies acceptance or changes the independent whole-tree/report gate.

For an active Fast local-only review, inspect exact actual authorized targets and
useful effects, before/after state or accessible equivalent and current checks,
not an inert worktree replica or fictitious Git baseline/SHA. Mixed subjects bind
both the whole Git candidate and actual local targets. Inaccessible targets or
unproved useful effects limit/block the dependent conclusion; never infer them
from Git publication. This does not turn the reviewer into a target writer or
authorize disclosure of secrets. Bind session assessment to the checkable actual
subject; changed targets require applicable independent reassessment just as changed
Git bytes do. No new review schema or mandatory file is introduced.

With a supplied ID, consume exact checked identity/source locators or obtain
missing identity, scope and relevant dependency facts through the selected adapter.
Independently read and assess necessary full candidate content, accepted basis,
tests/documents and applicable checks; supplied discovery is reusable, the author's
conclusion is not independent review. Refresh mutable tracker facts only when
the review conclusion or report-write predicate depends on their currency, or
relevant drift/conflict is observed. No execution claim is required merely for
read-only assessment. Do not
discover or require implementation reports, saved plans or historical RED/GREEN
logs as review admission evidence. Assess final correctness/test sufficiency,
not the author's development chronology; executor TDD obligations remain theirs.
Adapter commands/storage belong to it. Missing essential
identity blocks a task-bound report. Structural parent is not feature identity;
ordinary standalone children retain their own sufficient scope/criteria/refs and
constraints. Missing/malformed feature data cannot select an ordinary contract.
Without an ID, do not load a task adapter or require task-note discovery, a task
directory or a fabricated record. Apply project-required tracking/report policy;
no-ID admission does not waive a mandatory project gate.

For dependent shared-path actions use context's checked Git-derived ordinary
source-folder association. If unresolved,
return available analysis unsaved with the exact dependent save gap; do not guess.

Supply verified project inputs, prior rounds/dispositions where applicable and
the actual review/gate purpose to `ris-port-op-review-change`; apply its method instead of
repeating it here. Record reviewer/context identity and actual launch evidence
when separate. The caller owns launching independent context: self-review is
not independent approval. Missing required independence leaves that gate
unverified, even if useful assessment is possible. Reassessment of affected fixes
is required; independence of that reassessment follows project/caller rules.

For feature preparation a pre-decision draft assessment is optional, not a
mandatory duplicate of publication review. One applicable publication-purpose
assessment of the complete final snapshot suffices. After change independently
reassess the new full subject with affected checks; the same still-independent
reviewer may reuse unaffected evidence. Never promote an inapplicable draft
assessment or human acceptance alone to publication approval.

Check assessment sufficiency: scope/version and baseline limits, applicable
criterion/design/architecture/document coverage, evidence applicability, exactly
one severity per finding, two groups (required high/medium; optional low), verdict
and unresolved limitations. Project display may translate severities to
высокий/средний/низкий. Preserve IDs and fix/dispute links across rounds; a
collective low disposition suffices and low alone triggers no repair/task/round.
For a publication gate verify complete subject and predeclared exclusions are
bound separately from context. A missing/ambiguous mapping or changed subject
during review leaves approval unverified; saving a local report must not alter
its subject. Ordinary review need not invent a publication manifest.

Save the ordinary project result as one compact `ris.review/2` file (or continue
an existing /1 unchanged under the format owner's conditional contract), using checked primary
`workspace.tasks/<confirmed-ID>/review.yaml` by default or an explicit authorized
local override. No-ID save requires an explicit authorized address, not an invented
ID/directory. Translate the portable semantic assessment into a substantive assessment,
checks, findings, provenance and verdict per the format resource; do not impose
RIS serialization on the portable base. Preserve previous rounds, append the new
round with semantic mapping `pass` → `approved`, `changes-required` →
`changes_required`, `unverified` → `blocked` only when the format's verdict and
external applicability predicates actually hold. No mechanical conversion creates
approval from insufficient evidence. Append that
round after fresh comparison and independently read back; check the complete
saved file under the format owner's validation instructions. On conflict, missing
permission/path or unresolved snapshot return useful assessment unsaved/blocked;
do not call an unmet ordinary mandatory save success. Fast alone permits the
response-only exception. A response may summarize/link the YAML, not replace it.
Return its local address and explicit round selector for any separately authorized
tracker operation; this review owner never writes Beads. The address is not a
promise of availability from another machine. Historical reports remain unchanged,
without automatic migration or new-format approval from an old Markdown verdict.

Before returning a saved-file gate, apply the format owner's two consumer results
to the expected subject, inputs/checks and actual invocation/all-author evidence;
require its external approval gate, not merely format validity or a verdict.
For fast session-only review verify the same substantive subject, independence,
evidence and repair predicates without YAML; changed bytes never inherit approval.

Return status, project/change identity (confirmed ID only when supplied), reviewed
version, report content/location and saved/unsaved
state, checked primary provenance for shared saves, input/decision/evidence
locators and actual channel facts/remainder under common's recoverable-result
rules. A receiver rechecks current applicability and required rights/protection;
the report/old write window is not a live gate. High/medium need correction or decision
resolution and reassessment of affected bytes; optional low does not block pass.
Stop at the report: no repairs, publication, tracker evidence writes/closure or
next-operation launch.
