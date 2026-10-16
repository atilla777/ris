---
name: ris-port-op-prepare-worktree
description: >-
  Prepare or safely reuse a worktree for explicitly identified work, with a
  selected adapter, verified Git state and optional authorized environment setup.
  Use for autonomous working-copy preparation or a caller composing that result;
  not task selection/claim, technical planning, implementation, repair or publication.
---

# Prepare a working copy

Own the portable **copy and environment result**, including partial effects and
handoff. Work directly from supplied repository/root paths, work identity and
evidence of its copy association, adapter selection, branch/path, base revision
or remote/main-branch selection rule, permissions and actual project constraints.
No RIS config, tracker, common/context skill, task ID or directory layout is
required. A project caller owns those inputs and any combined project result.

Read `references/worktrees-contract.md` from this installed folder before adapter
operations. Load/apply only the selected adapter; check its actual availability,
version, operations and guarantees against `worktrees/1`. Explicit selection wins,
otherwise use an unambiguous supplied project rule, otherwise select
`ris-port-adapter-git-worktrees`. An unavailable/incompatible selected adapter blocks
its dependent work: do not fall back to another adapter or its CLI. Neither
the adapter nor this base claims tasks or decides another owner's acceptance.

## Establish the copy

1. Confirm inputs, permissions and repository identity, current and explicitly
   supplied primary roots (if the caller needs shared resources). A branch name
   alone is not ownership evidence: require an agreed identity → repository,
   branch and path association, accessible previous evidence, or explicit
   confirmation of an existing copy. Missing association blocks reuse; ask only
   for the affected decision. Do not invent a registry or infer a tracker ID.
2. Inspect complete registrations and exact candidate state through the adapter
   **before mutation**. Validate branch without sanitizing identity, absolute path,
   authorized parent/real target and collisions (including symlinks, nested
   worktrees, registrations and refs). Keep an established path/branch on repeat.
   Missing/damaged/prunable registration, foreign data, ambiguous association,
   inaccessible copy or unfinished Git operation is a concrete conflict/blocker;
   do not delete, move, repair, prune, reset, rebase, stash or commit it.
3. For a confirmed existing copy, use `read` and preserve HEAD, index, files,
   untracked data and refs. Report changes/divergence without updating the copy.
   Do not fetch merely to reuse or apply a newly selected base to existing work.
   An existing branch with no copy requires confirmed association **and** explicit
   permission to use its freshly read current commit; otherwise stop conflict.
4. For a new branch, an explicit revision wins: resolve it to one accessible
   commit without an implicit fetch. Otherwise require the selected remote and
   its established primary branch, refresh that exact remote branch, and pin the
   returned full commit. Failure/offline blocks creation; stale tracking refs or
   local main are not substitutes. Never switch/reset the main copy. The selected
   adapter owns the concrete Git mapping for these observations.
5. Preflight selected-tool side effects and any required environment actions.
   Pass exact absolute path, validated branch, pinned commit, permissions and
   expected absence/state to `create`. Recheck effects after every response,
   including nonzero/ambiguous results, before considering a retry. Git protects
   individual operations, not the whole sequence. Ordinary creation needs no
   manual window or global lock. If strict cross-operation uniqueness is
   explicitly required but unsupported, report that exact limitation before
   dependent creation, without asking to pause writers.

## Environment and verification

No automatic install/copy/start is implied. If setup or tool hooks are requested
or required, read `references/environment.md` **before any dependent mutation**
and apply it to the exact authorized actions, outputs and verification signals.
If required actions cannot be safely executed/observed, stop dependent creation
where preflight can detect that; otherwise retain and report partial effects.
Hooks and background starts are not successful setup just because creation exits 0.

Verify the actual copy using the adapter's independent Git oracle: repository
relationship, canonical path, branch/detached, HEAD, index/files/untracked and
operation state. For new creation compare branch/path/HEAD with pinned inputs;
for reuse compare pre/post state and report unexpected changes as conflict rather
than attributing them to this operation. Setup may change only authorized outputs;
identify those separately from preserved pre-existing work. Reconcile completed
actions before retry, never blindly recreate or rerun a non-idempotent setup.

## Self-contained handoff and stop

Return structured Markdown or equivalent with:

- `status: ok|blocked|conflict|error`, work identity/association evidence,
  permissions and requested vs observed operation (new/reuse/existing branch);
- repository identity, current/primary roots (explicit or unknown), copy path,
  branch/detached, HEAD, new-copy base commit and how it was selected (or n/a);
- selected adapter/tool/version, index/staged/unstaged/untracked/operation state,
  any known divergence and actual checks with their limits;
- separate `copy: ready|blocked|conflict|error` and
  `environment: ready|not-requested|blocked|error`, completed actions and evidence;
- observed effects (including fetched refs, created branch/copy, completed setup),
  shared-state limitations and the exact safe continuation after any failure.

`ok` requires verified copy and all requested/required setup; not-requested is
not proof of environment readiness. A ready copy with failed requested setup has
the stopping cause's non-`ok` status (`error` for technical failure, `blocked` for
missing prerequisites, `conflict` for contradictory state), with copy readiness,
completed setup effects and exact remaining setup reported separately. Preserve
effects; reconcile them before rerunning setup; no silent rollback or claim release. Save
evidence only to an explicitly authorized supplied address, preserving existing
history; otherwise return it. Do not create a task/worktree registry, declare
requirements ready, prepare a technical plan, implement, publish, close tasks,
remove copies or start a next lifecycle operation. Stop at this checked handoff.
