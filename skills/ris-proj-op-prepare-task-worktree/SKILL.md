---
name: ris-proj-op-prepare-task-worktree
description: >-
  Prepare or safely reuse one confirmed RIS task's worktree with checked claim,
  shared roots, selected Git or Worktrunk adapter and a self-contained handoff.
  Use for project task working-copy preparation; not task selection, technical
  planning, implementation, repair, publication or task completion.
---

# Prepare one RIS task's working copy

Own the combined **project copy and environment handoff**. Load/apply installed
`ris-proj-lib-common` with its applicable resources, `ris-proj-op-resolve-context` for this operation's
rules, selected tasks adapter and needed shared paths, and
`ris-port-op-prepare-worktree` for the portable method. Check availability and actual
results, not names. Direct invocation requires no execution role. Only the base
loads the selected worktree adapter; the tasks adapter owns tracker effects.

## Project inputs and preflight

Require selected project, exact task ID, actor, current working copy and explicit
permissions for claim, copy creation/reuse, environment actions and optional
evidence writes. Never choose a task or infer its ID from a title. Prepare context
for these inputs; read the applicable project rules. For shared paths consume
context's checked `primary_root`, selected explicitly or from an already available
verified saved indication under its owned procedure. Inspect its provenance and
current-copy association; do not derive a root independently from Git. Resolve `sources.*` in
the current project and `workspace.*` in the primary copy; config location is
not a root. Missing settings block only the part needing them. Do not require
product/specification acceptance just to prepare a copy, or change `ris.yaml`.

Through the selected available tasks adapter freshly verify exactly this task's
identity/type/content, membership, status, blockers and assignee. Check supported
read and claim operations and their actual guarantees; `tasks` v1 alone does not
promise claim. Closed/invalid/blocked tasks stop dependent filesystem mutation;
a foreign live claim is a conflict, never overwritten. Read-only inspection may
return observations without claiming or creating anything.

An explicit ordinary standalone task/child is supported without an epic or
feature payload; its structural parent alone does not establish feature identity.
Use exact ID/links and inspected copy receipts for available facts before asking
for missing association/actor/authority; do not infer them from a title or path.

For a new association propose branch `task/<ID>` and absolute
`workspace.worktrees/<ID>` unless explicit input, project rules or a previously
confirmed association takes priority. Validate the unmodified ID/path/branch:
unsafe or ambiguous values require clarification, not lossy sanitization. A
conventional name alone is not proof of ownership. Require an agreed association
of task, repository, branch and path, accessible prior evidence or explicit
confirmation before reuse; inspect an optional existing witness when supplied.
No new registry or tracker fields are introduced.

Pass repository/current/primary roots, task identity and association evidence,
branch/path, explicit revision or established remote/main rule, permissions,
project constraints and exact optional setup to the base. Explicit adapter choice
wins, then an unambiguous project rule, otherwise Git; installed `wt` does not
select Worktrunk. Apply the base's available read-only tool/path/ref/side-effect
preflight **before claiming or creating**. A missing selected capability blocks
without fallback; do not copy the base's creation or preservation algorithm here.

## Claim-aware composition

Before any creation or environment mutation, confirm an existing own claim or
obtain an explicitly authorized claim of the open unblocked task through the
adapter's supported guarded operation. If permission/capability is missing, stop
that mutation. Independently reread ownership, in-progress status and blockers
after claim and before each new mutation batch, including retry, setup and
optional evidence writes. Stop on ownership loss/new blockers and report effects.
Claim/worktree do not isolate shared state or supply CAS/concurrent uniqueness.

Apply the base's preparation/reuse, selected adapter and conditional environment
method to the verified inputs. Keep shared tracker storage, primary task notes,
nested worktrees and other shared mutable resources out of copied setup files;
pass their actual paths and exclusions, including custom/external locations.
Verify the combined result against the task association and permissions, using
the base's actual independent Git observations. Reprepare context with
`project_root` equal to the resulting copy's project directory and the checked
primary root with its selection evidence; verify paths, applicable rules and selected tracker workspace again.
A changed/missing config or a tracker resolved to a different project blocks the
project handoff even when the Git copy exists. Do not initialize another tracker
or silently substitute defaults/shared paths. Shared tracker access must use the
confirmed project workspace, not an ambient new database in the copy.

## Handoff, optional evidence and stop

Return the base's complete copy/environment result plus task ID, actor, fresh
claim/status/blocker observations, current and primary project roots, confirmed
tracker workspace, config provenance and re-resolved rules/shared paths. Include
association evidence and its inspectable address (or honest unsaved discovery gap),
primary selection source/verification, actual path/branch/HEAD, new-copy pinned base or n/a on
reuse, index/staged/unstaged/untracked/operation state, tool/version, permissions,
checks/limits and effects. Report copy and environment verdicts separately;
unrequested setup is not proof of environment readiness. This handoff must be
usable without chat history and does not establish implementation readiness.
Apply common recoverable-result facts, including saved/accepted/publication
channels and unfinished remainder. A receiver must freshly check rights, claim,
blockers and operation-specific protection; the witness/lease is not a live gate.

Only when separately authorized, save this witness as
`workspace.tasks/<confirmed-ID>/worktree.md` in the primary copy (or the explicit
project address). Read existing content, preserve all history/unrelated text,
append an identified observation and verify read-back. Check safe write scope and
concurrency before writing; on a conflict return the handoff unsaved. The witness
is local evidence, not an authoritative mutable registry or mandatory remote input.

For incomplete execution return the cause's `blocked|conflict|error` and enumerate
actual claim, branch/copy, fetched refs and completed
setup actions, failed/missing context or evidence, and exact safe continuation.
Retain effects: no implicit claim release, rollback, removal or blind recreation.
Retry rereads task, copy and setup before further effects. Stop at the checked
handoff; do not prepare a technical plan, implement, review, publish, close tasks
or containers, or name/select/start a next lifecycle skill.
