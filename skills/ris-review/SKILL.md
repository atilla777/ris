---
name: ris-review
description: >-
  Review one RIS task change against accepted design and project rules and save
  a versioned findings report. Use for project code or document review; not fixing
  findings, feature design approval, publication or tracker completion. Self-review
  does not supply independent approval.
---

# Review and record one task change

Own the checked project report. Load/apply `ris-common` and applicable resources,
`ris-context` for rules/specs/adapter and shared report paths, and `ris-review-base`
before assessment. A direct call works without an execution role. Require exact
project/task ID, change base/final tree, requirements/design/contract evidence,
check results and report-write permission. Use selected adapter reads to confirm
identity, scope, membership and relevant dependencies; check current evidence
instead of trusting a stale handoff. Explicit primary root is required for shared
paths from a worktree. No claim mutation is needed for read-only review.

Supply those verified inputs to `ris-review-base` and apply its assessment.
Record actual reviewer identity/context and launch evidence if invoked separately.
Do not disguise implementer self-review as independent approval; when an
independent gate is required and cannot be established, report it unverified.
The invoking workflow owns launching an independent reviewer and checking its
result; this wrapper does not invent an agent or select a following operation.

Check the report's criterion/design/architecture/doc coverage and precise
base/final tree identity. A changed tree during review invalidates its approval
claim. Preserve exactly one severity per finding (project display may translate
high/medium/low to высокий/средний/низкий). With permission save and read back
`workspace.tasks/<confirmed-ID>/review.md` by default, or the specified report
name; inspect existing content and preserve earlier rounds when updating. Without
permission return an unsaved report. Include independence, inputs/versions, checks,
findings or explicit no-findings, verdict and limitations.
Verify that the report explicitly binds the complete proposed publication
snapshot and its predeclared exclusions separately from contextual task/tooling/
local evidence. Saving this report must not recursively change its approval
subject. A missing or ambiguous snapshot mapping makes the gate unverified.

Return status, ID, reviewed tree, report location/content and actual independence.
High/medium findings require correction and another independent assessment of the
new tree; track low dispositions. Stop at the report; no repairs, publication,
tracker evidence writes, closure or next-skill launch.
