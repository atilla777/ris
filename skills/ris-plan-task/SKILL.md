---
name: ris-plan-task
description: >-
  Save and verify a technical plan for one confirmed RIS tracker task using
  current code and accepted design/contracts. Use for project task planning
  in the supplied current working copy; not worktree preparation, task
  selection, decomposition, feature redesign or implementation.
---

# Prepare one project's task plan

Own the verified project plan. Load and apply `ris-common` and its applicable conditional resources,
`ris-context` for this operation's rules/specs, tasks adapter and workspace paths,
and `ris-plan-task-base` before planning. Resolve resources from their installed
owners; unavailable dependencies block their dependent result. No execution role
is required for a direct call.

## Establish the task and permissions

Require the selected project, exact task ID, current working copy and plan
proposal vs persistence scope. Use the selected available
adapter's supported read operations to confirm type, identity, content,
membership and blockers; never guess an ID from a title. Read the task's actual
requirements, governing accepted design scope/version/decision and relevant
contracts/test seams. Preserve `slug#AC-nnn` references where supplied. A
standalone task needs its accepted technical constraints, not an artificial
feature record. Check inspected current code and related contract integration;
stale or unavailable material inputs produce a partial/blocked plan, not readiness.

Planning does not require or obtain a claim or separate worktree. Verify the
supplied current copy's repository/project relationship and, when a task-specific
copy is supplied, its confirmed task/branch/path association and actual HEAD/state.
Require `primary_root` explicitly for shared paths in a worktree; reprepare context
after a copy change. Preserve dirty/untracked work. Missing or conflicting copy
inputs block the dependent plan; do not create, switch, repair or reset a copy,
or load working-copy preparation skills/adapters. A copy does not isolate the
tracker or shared notes. Plan persistence still needs its own write permission
and safe shared-note access, not a claim inferred from planning.

## Compose and verify

Supply the confirmed task, requirements/design/contract evidence, current code,
constraints and available check environment to `ris-plan-task-base`; actually
apply its method. This wrapper does not substitute its own plan algorithm.
Check the returned scope, version currency, criterion coverage and readiness
against project evidence. Material departures return a bounded design/requirements
revision need and affected work; do not silently change accepted contracts.

With persistence permission save the supported plan by default as
`workspace.tasks/<confirmed-ID>/plan.md` under the primary copy, or the explicit
project-prescribed address. Inspect an existing plan before updating it; preserve
unrelated notes and identify changes. Read back the saved content and verify it
can be found by ID without this chat. A partial plan may be saved only when that
partial artifact is authorized and clearly labeled. It is local working evidence,
not a replacement tracker or remotely available requirement.

Return status `ok|partial|blocked|conflict|error`, confirmed ID/project/primary root,
plan readiness and exact saved path (or unsaved proposal), input versions and
decisions, criterion-to-check coverage, observed copy state, diagnostics
and remaining decisions. Stop at the plan; do not prepare a worktree, implement, publish,
close a task, or select the next operation.
