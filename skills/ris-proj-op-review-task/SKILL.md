---
name: ris-proj-op-review-task
description: >-
  Review one confirmed RIS task change and return a checked findings report,
  saving a versioned report when authorized. Use for project code or document
  review and focused re-review; not fixing findings, feature design approval,
  publication or tracker completion. Self-review does not supply independent approval.
---

# Review one project task

Own the checked project report. Load/apply `ris-proj-lib-common` with applicable resources,
`ris-proj-op-resolve-context` for the operation's rules/specs/selected adapter and, only when
needed, shared report paths, and `ris-port-op-review-change` for the assessment. Check
dependency availability and actual results. A direct confirmed-ID invocation
needs no execution role or scenario skill.

Establish exact project/task ID, requested review scope/version, available
requirements/technical constraints and checks. Through the selected available
adapter freshly read identity, task content, membership and relevant dependencies;
adapter-specific commands and storage belong to it. A stale handoff is not a
current input. Missing essential identity blocks a task-bound report; missing
spec/design/baseline limits the affected conclusion without stopping useful
current-content analysis. Do not invent a feature design for a small repair.
No claim mutation is needed. Analysis does not require report-write permission.
Explicit primary root is needed for dependent shared-path actions from a worktree;
without it return available analysis unsaved, rather than guessing shared paths.

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

With permission, save `workspace.tasks/<confirmed-ID>/review.md` by default;
explicit report address overrides it. Read existing content, preserve history
and unrelated notes, append/identify the new round and read it back. On a write
conflict return the assessment unsaved with the blocker; do not overwrite history.
Without permission return the unsaved report. Include actual independence,
inputs/versions, checks, both finding groups (explicitly empty when applicable),
verdict, prior dispositions and limitations.

Return status, ID, reviewed version, report content/location and saved/unsaved
state, independence and gate limitations. High/medium need correction or decision
resolution and reassessment of affected bytes; optional low does not block pass.
Stop at the report: no repairs, publication, tracker evidence writes/closure or
next-operation launch.
