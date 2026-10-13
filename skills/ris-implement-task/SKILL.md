---
name: ris-implement-task
description: >-
  Implement or fix review findings for one claimed RIS task using accepted
  design/contracts, tests and authorized documentation updates. Use for project
  task execution; not task selection, feature redesign, independent approval,
  worktree preparation, Git publication or tracker completion.
---

# Implement one claimed project task

Own the project's checked change and handoff. Load/apply `ris-common` and its
applicable resources, `ris-context` for rules/specs/adapter and shared task paths,
and `ris-implement-base` for code/test work. Before documentation synchronization,
load/apply `ris-update-documentation`. Check actual dependency availability and
results, not just their names. Direct execution needs no configured agent role.

Require exact task ID/project, actor, authorized code/test/docs scope, current
working copy, applicable plan or enough accepted technical inputs, and optional
review findings to repair. Through the selected available adapter freshly read
task identity/content, membership, blockers and claim. Check its explicitly
supported claim operation: `tasks` v1 alone does not promise it. Confirm own
claim or atomically claim an authorized open/unblocked task before file changes;
verify ownership/state/blockers after. Do not overwrite another actor's live claim.
Recheck ownership on resumption and before new mutation batches; stop on loss or
new blockers, preserving partial work. Verify the supplied current copy's
repository/project relationship, actual HEAD/state and task/branch/path association
when it is a task-specific copy; do not infer ownership from a branch name alone.
Reprepare context after copy changes and require an explicit primary root for
shared notes/tracker access. Missing/conflicting copy inputs block dependent
mutations. Do not create, switch, repair or reset a worktree, or load working-copy
preparation skills/adapters. Direct implementation in an already suitable current
copy remains possible, with the same claim guard and preservation of existing work.

Verify current accepted requirements/design scopes, decisions and contract
versions against relevant inspected code and shared-contract integration; use
the feature record's supported read capability when applicable. No feature record
is required for standalone work. Pass these verified inputs and constraints to
`ris-implement-base` and apply its implementation/repair method. The wrapper owns
claim and project integration; do not repeat the portable algorithm here.

Apply `ris-update-documentation` to the affected **authorized** documents (or
record a justified no-change result). Supply actual implementation evidence and
whether the tree is pre-integration; future architecture must not be presented as
current before integration. Product writes need separate explicit permission.
Check the combined code/tests/docs diff against task criteria and accepted
contracts. Save checks and repair mapping in the confirmed task's shared local
workspace with a stated filename and exact final tree fingerprint; read them back.
Do not write tracker content/evidence unless separately authorized through the
adapter's supported concurrency guarantees.

Return status, ID/claim/copy, scope and input versions, final tree identity,
criteria/checks/docs results, report paths and remaining revision needs. Local
choices do not reopen global design; material departures return bounded impact
and decision needs, with dependent changes stopped. Stop at the checked change;
no independent approval, commit/push, task/container closure or next-skill launch.
