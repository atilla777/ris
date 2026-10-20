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

Before producing/saving a project report or consuming prior rounds, read
`references/report-format.md` from this installed skill. It is the sole owner of
`ris.review/1` serialization, types, history and approval applicability. Ordinary
project review requires that complete YAML; explicit fast execution alone permits
a sufficient session result without a file. An optional fast save uses the same
format. No duplicate Markdown report or Beads verdict/findings copy.

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

With a supplied ID, load/apply the selected available adapter and freshly read
exact typed identity, content, membership and relevant dependencies. Discover the
ID's accepted versions/decisions from its links and current candidate evidence
from the actual supplied tree, tests, documents and applicable checks. Do not
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

For a supplied exact native bug use ordinary typed bug reads and retrieve the full current
report (including the exact published file when linked), aligned criteria and
accepted constraints/decisions with their authority. A sufficient report replaces
formal spec/design, not authority or separate acceptance of material design.
Select the review basis by the **actual subject**, not the existence of a bug ID:

- **Pre-execution design/document review:** bind the exact document candidate and
  separate acceptance decision where applicable to the full current report/criteria/
  accepted constraints and source versions. No future historical execution-input
  snapshot, fix implementation, implementation checks or execution plan/omission
  decision is required for this subject. Compare current inputs with that bound
  basis; material drift returns affected design/document evidence for reassessment.
  This exception does not accept the design or approve a future fix. Keep independent
  review, applicable document checks and complete candidate-tree binding.
- **Fix implementation review, including its publication gate:** additionally read
  the full historical notes execution-input snapshot at project/tracker + bug ID +
  marker and name it in the report; a number/hash alone is insufficient. Compare
  current report/criteria/decisions with that basis and bind exact candidate/check
  versions to original divergence and affected regressions. Material drift requires
  targeted plan/change/review/evidence applicability assessment before approval,
  preserving compatible evidence with reasons. Never approve a changed expectation
  just because the implementation passes it. Assess sufficient accepted technical
  inputs and current code/tests, not the author's plan or TDD-history persistence.
  A mixed implementation/document subject
  retains these implementation guards; it cannot select the pre-execution exception.

For dependent shared-path actions use context's checked primary selection and
provenance (explicit or verified available saved indication). If unresolved,
return available analysis unsaved with the exact dependent save gap; do not guess.

Supply verified project inputs, prior rounds/dispositions where applicable and
the actual review/gate purpose to `ris-port-op-review-change`; apply its method instead of
repeating it here. Record reviewer/context identity and actual launch evidence
when separate. The caller owns launching independent context: self-review is
not independent approval. Missing required independence leaves that gate
unverified, even if useful assessment is possible. Reassessment of affected fixes
is required; independence of that reassessment follows project/caller rules.

Check report sufficiency under the format resource: scope/version and baseline limits, applicable
criterion/design/architecture/document coverage, evidence applicability, exactly
one severity per finding, two groups (required high/medium; optional low), verdict
and unresolved limitations. Project display may translate severities to
высокий/средний/низкий. Preserve IDs and fix/dispute links across rounds; a
collective low disposition suffices and low alone triggers no repair/task/round.
For a publication gate verify complete subject and predeclared exclusions are
bound separately from context. A missing/ambiguous mapping or changed subject
during review leaves approval unverified; saving a local report must not alter
its subject. Ordinary review need not invent a publication manifest.

Save the ordinary project result as one `ris.review/1` file, using checked primary
`workspace.tasks/<confirmed-ID>/review.yaml` by default or an explicit authorized
local override. No-ID save requires an explicit authorized address, not an invented
ID/directory. Translate the portable semantic assessment into complete coverage,
checks, findings, provenance and verdict per the format resource; do not impose
RIS serialization on the portable base. Preserve previous rounds, append the new
round with semantic mapping `pass` → `approved`, `changes-required` →
`changes_required`, `unverified` → `blocked` only when the format's verdict and
external applicability predicates actually hold. No mechanical conversion creates
approval from insufficient evidence. Append that
round after fresh comparison and independently read back. On conflict, missing
permission/path or unresolved snapshot return useful assessment unsaved/blocked;
do not call an unmet ordinary mandatory save success. Fast alone permits the
response-only exception. A response may summarize/link the YAML, not replace it.
Return its local address and explicit round selector for any separately authorized
tracker operation; this review owner never writes Beads. The address is not a
promise of availability from another machine. Historical reports remain unchanged,
without automatic migration or new-format approval from an old Markdown verdict.

Keep format validity (`valid|invalid|unsupported`) separate from approval for the
expected subject. Before returning a gate, apply the resource's external tree/base/
exclusions, inputs, required checks and actual invocation/authorship observations.
Read later rounds too: refuting or invalid/unknown later rounds forbid fallback.
Missing required provenance/evidence or an inaccessible local report leaves no
approval; the report's own `approved`/`confirmed` fields cannot certify themselves.

Return status, project/change identity (confirmed ID only when supplied), reviewed
version, report content/location and saved/unsaved
state, checked primary provenance for shared saves, input/decision/evidence
locators and actual channel facts/remainder under common's recoverable-result
rules. A receiver rechecks current applicability and required rights/protection;
the report/old write window is not a live gate. High/medium need correction or decision
resolution and reassessment of affected bytes; optional low does not block pass.
Stop at the report: no repairs, publication, tracker evidence writes/closure or
next-operation launch.
