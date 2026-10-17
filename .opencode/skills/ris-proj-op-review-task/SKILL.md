---
name: ris-proj-op-review-task
description: >-
  Review one bounded RIS project change, with or without a task ID, and return
  checked findings, saving a versioned report when required and authorized. Use for
  project code or document review and focused re-review; not fixing findings, feature design approval,
  publication or tracker completion. Self-review does not supply independent approval.
---

# Review one project change

Own the checked project report. Load/apply `ris-proj-lib-common` with applicable resources,
`ris-proj-op-resolve-context` for applicable project rules and, only when needed,
specs, selected adapter or shared report paths, and `ris-port-op-review-change`
for the assessment. Check dependency availability and actual results. A direct invocation
needs no execution role or scenario skill.

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
from the supplied copy and accessible primary task reports (default
`implementation.md`, `execution.md`, `plan.md`, or inspected overrides), retaining
project-required inputs. Adapter commands/storage belong to it. Missing essential
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
  just because the implementation passes it. Check saved plan or justified applicable
  omission with sufficient technical inputs; omission cannot waive mandatory project
  persistence, including RIS local plans. A mixed implementation/document subject
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

Check report sufficiency: scope/version and baseline limits, applicable
criterion/design/architecture/document coverage, evidence applicability, exactly
one severity per finding, two groups (required high/medium; optional low), verdict
and unresolved limitations. Project display may translate severities to
высокий/средний/низкий. Preserve IDs and fix/dispute links across rounds; a
collective low disposition suffices and low alone triggers no repair/task/round.
For a publication gate verify complete subject and predeclared exclusions are
bound separately from context. A missing/ambiguous mapping or changed subject
during review leaves approval unverified; saving a local report must not alter
its subject. Ordinary review need not invent a publication manifest.

Return a versioned response-only report when project rules permit; saving is not
inherently required. Save when explicitly authorized or required by project/caller
rules, with actual write permission. With a real ID use checked
`workspace.tasks/<confirmed-ID>/review.md` by default; an explicit report address
overrides it. Without an ID require an explicitly authorized address for a save;
never invent an ID/directory. Read existing content, preserve history and unrelated
notes, append/identify the new round and read it back. On a write conflict or
missing required address/permission, return the assessment unsaved with the exact
dependent gap; an unmet mandatory save is not optional no-save success. Do not
overwrite history. Include actual independence,
inputs/versions, checks, both finding groups (explicitly empty when applicable),
verdict, prior dispositions and limitations.

Return status, project/change identity (confirmed ID only when supplied), reviewed
version, report content/location and saved/unsaved
state, checked primary provenance for shared saves, input/decision/evidence
locators and actual channel facts/remainder under common's recoverable-result
rules. A receiver rechecks current applicability and required rights/protection;
the report/old write window is not a live gate. High/medium need correction or decision
resolution and reassessment of affected bytes; optional low does not block pass.
Stop at the report: no repairs, publication, tracker evidence writes/closure or
next-operation launch.
