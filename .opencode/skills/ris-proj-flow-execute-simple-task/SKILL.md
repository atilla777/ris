---
name: ris-proj-flow-execute-simple-task
description: >-
  Execute or resume one already assigned, clear bounded project request through
  proportionate checks, independent subagent review, verified direct Git push and
  separate tracker completion when used. Use for simple work with optional ID,
  including text, configuration or code; not queue selection, feature preparation,
  registered-bug preparation, whole-container execution or a replacement for the
  full task flow and mandatory TDD contracts.
---

# Execute one simple assigned task

Own sufficiency, transitions, one human dialogue and the combined result. One
project flow suffices: existing owners supply portable stage methods. The main
agent loads and **applies** those owners directly for implementation, repairs,
copy preparation, publication and tracker operations; only independent review
requires a separate subagent. Do not copy their algorithms or load the full task
flow's resources. No new implementation wrapper, role, registry or state format.

## Establish scope and permissions

Accept an attributable assigned outcome, selected project, optional exact ID,
available clarifications and accepted constraints. Natural requests such as “do
this quickly”, or agent choice for work already assigned by the user, may select
this route. Empty input asks what work to do; never choose from a queue or start
unassigned work. Judge clarity, bounded consequences and checkability, not diff
size or a closed list of change types. A clear request can suffice without an
interview, spec/design document, decomposition or saved technical plan.

Read the selected project's instructions and relevant implementation. Load/apply
`ris-proj-lib-common` and its resources under their triggers. Apply
`ris-proj-op-resolve-context` and its owned configuration resource for applicable
rules and the required `task-review` role; request adapter settings, document or
shared paths only when needed. Check status, provenance, diagnostics and rights.
Missing unused paths or execution roles do not block work; direct work requires
neither `task-execution` nor `task-implementation`. If delegating bounded work,
resolve its corresponding configured role and verify host availability/permissions
and actual launch; an unavailable role blocks that delegated route, without silent
substitution. Context's configured agent name alone
does not prove reviewer availability. Before fresh mutations verify the actual
host can launch the configured reviewer independently of every author/repairer.
No fallback agent, self-approval or model switch substitutes for that gate.

A full invocation authorizes the agreed implementation/check/review/repair,
commit and direct push cycle to the established project primary branch without
another formal confirmation; when tracking applies it also authorizes separate
selected-task completion and tracker publication under their actual gates.
Explicitly narrower requests, environment permissions and mandatory project rules
win. Do not infer content acceptance or rights from a command, status or claim.
No PR, release or deploy fallback. No mandatory plan, execution/implementation log
or review **file** by default: retain sufficient evidence in the session, with
short tracker accounting when used. Required project checks still apply;
this flow does not silently waive TDD or other substantive gates.

Read resources from **this installed skill folder**, only before their triggers:

- `references/tracker.md` when an ID is supplied or project rules require task
  accounting, before admission/claim and later tracker effects. A configured
  adapter alone does not activate tracking. Otherwise load no task adapter,
  create no record, invent no ID or task-note directory.
- `references/worktree.md` before all versioned Git-project edits, to prepare or
  reuse this work's dedicated worktree through the existing owner.
- `references/recovery.md` on resume, prior/partial effects, interruption or an
  ambiguous operation response, before selecting a transition or retry.

Unavailable required dependencies/resources block only their dependent work.
Loading an owner is not applying it; inspect its actual output before advancing.
Reuse already available facts within this session. For bounded delegation use
common's artifacts contract with only missing exact inputs, permissions and
expected result; recipients load their owners without assumed chat inheritance.
On recovery discover saved sources by project+ID (or the explicit no-ID subject),
not a required prior final answer or handoff file.

## Execute the fresh route or reconciled remainder

1. **Admit this work.** Establish outcome, boundaries, criteria, technical
   constraints/material decisions and a sufficient check strategy from the
   request and current facts. Apply the tracker branch if triggered; keep real
   type, ownership, accepted inputs, mandatory composition and blockers. Minor
   ambiguity gets a targeted clarification and continues fast. A material choice
   about behavior, public contract, responsibility or architecture stops only
   dependent actions: state affected criteria, available compatible results and
   the exact decision needed from the person. Agree the necessary preparation or
   full route, rather than automatically restarting the SDLC or redesigning here.
2. **Prepare or reuse this work's dedicated worktree before edits.** Apply the
   worktree resource, using the same claim-aware project preparer as full task,
   feature and bug work when tracked. For genuinely no-ID work use its portable
   preparation branch without inventing an ID. Consume the checked association,
   copy/branch/base and preservation result; this flow owns no native create/switch
   algorithm. Reuse one confirmed worktree across stages and sessions, not a new
   copy per executor. The ordinary source folder is never a development copy,
   even if clean or on an own branch. Preserve foreign and dirty work; do not
   transfer it to a new copy automatically. Re-resolve context in the result copy
   and verify current rules/config and shared tracker association before writes.
3. **Implement and check in the main agent.** Load/apply
   `ris-port-op-implement-change` with the accepted request/constraints, current
   copy/base, allowed files/effects and `implementation_mode: standard|tdd`.
   Use `tdd` when project rules require it or it is selected as useful; mandatory
   TDD wins. This route never relaxes `ris-proj-op-implement-task-tdd`'s contract.
   Refresh required ownership/blockers before each new change batch. For affected
   authorized documentation apply `ris-proj-op-update-documentation`; do not
   invent scope or accept new product/design decisions through documentation.
   Text/word replacement: inspect actual result and diff; configuration: run its
   applicable validation; logic: meaningful affected/regression tests and new tests
   where substantively needed. Keep mandatory checks, no ceremonial text tests.
   Apply target-project prohibitions on agent tests. Static instruction inspection
   establishes prescriptions, never observed runtime reliability or speed.
4. **Actually launch independent review.** Load/apply `ris-proj-op-review-task`
   in a fresh invocation of the configured, available `task-review` subagent,
   independent of all implementation/repair authors. Supply project/config/rules,
   attributable request/clarifications/criteria, publication-gate purpose, accepted decisions and versions,
   real ID only if used, copy/branch/base, full exact candidate and checks/limits.
   Bind the complete publication tree/base and predeclared exclusions, including
   additions/deletions/modes and unchanged base bytes, not HEAD alone or a dirty-tree
   hash. Give the reviewer accessible bytes and bounded read-only
   scope (report writes only when separately needed/authorized). Explicitly pass
   this fast no-file exception: a sufficient independent result may remain in
   session; absence of review.yaml alone does not block. If saving is requested,
   use the installed review owner's references/report-format.md and the same
   supported format (/2 new file; /1 only for an existing /1 file), never a Markdown twin. Ask for a checkable report,
   early return on missing essential evidence or material conflict, not a live
   agent test. Verify actual launch/context identity and returned subject/version,
   coverage, stable findings with exactly one high/medium/low severity, verdict
   and limits. Missing/unavailable/inapplicable independence blocks publication.
   For a saved file apply the format owner's consumer gate with the expected
   subject, inputs/checks and actual launch/all-author evidence; require its
   applicable approval, not just a verdict. For session-only evidence check
   substantive independence/snapshot/repair gates without loading YAML resources.
   Review final results, not author logs or historical RED/GREEN runs.
5. **Repair and recheck.** High/medium returns to the main agent applying the
   implementation owner with finding IDs; repair, run affected checks and obtain
   fresh independent review. Preserve links across rounds. Repeat until none
   remains unresolved; a round limit cannot approve a blocker. Consider low
   recommendations and record a reasoned disposition, collectively if suitable;
   low alone requires no fix, task or extra round. Reassess evidence whenever
   bytes/inputs change. If progress needs a material decision, return it to the
   human dialogue with preserved results.
   Apply the machine outcome explicitly: valid applicable independent `approved`
   proceeds without another loop; `changes_required` repairs and re-reviews;
   `blocked` or missing/invalid/unsupported/inapplicable evidence stops dependent
   progression for the missing input/evidence, not an automatic repair loop.
6. **Publish through the existing owner.** Main agent loads/applies
   `ris-proj-op-publish-task`, Task/change branch, with exact independently
   approved **whole** snapshot, check/review provenance, prepared own branch/copy,
   accepted inputs and actual direct-push authority/target. Inspect its receipt,
   not a success assertion. It owns Git integration, outgoing-history, commit/push
   and remote confirmation. A changed integrated/hook/upstream/document snapshot
   returns to affected checks and independent `task-review` whole-tree reassessment
   **before push**, reusing compatible evidence with reasons. Never self-approve
   or add after-the-fact exclusions. Require sent commit/tree/ref/remote and fresh
   remote evidence; missing rights/checks/review or PR-only policy blocks this
   route, and ambiguous effects activate recovery before retry.
   The default result is remote-only: do not request source-copy maintenance or
   branch return. Only an explicitly requested local update activates the
   publisher's rare safe-FF resource, without branch switching. Retain its
   unfinished local remainder separately; it never blocks exact close/Dolt or
   requires replay of confirmed remote publication.
7. **Finish distinct effects.** Without tracking, verified Git plus the session
   result ends the cycle. With tracking, use the already-triggered tracker
   resource for short result/Git SHA persistence, separately verified exact close
   and separately authorized tracker publication. No parent closure or feature
   acceptance inferred from a push or review.

## Assess the combined result and stop

Return `ok|blocked|conflict|error`, subject and user-visible change, project/config/
actor when applicable, actual copy/branch/base and final snapshot; attributable
inputs/decisions, checks/results/limits, independent reviewer/version/verdict,
repair/low dispositions, evidence content or exact accessible locators, and Git
commit/tree/ref/remote confirmation. Give separate local tracker result, exact
closure and tracker publication/read-back facts when used. No artificial status
store is needed. `ok` requires all effects promised by the actual scope verified;
one channel cannot establish another. On partial/failed work preserve accessible
changes/evidence, state the causal blocker, unknown effects and exact remaining
operation/decision. Stop at this request; never select, claim or start next work.
