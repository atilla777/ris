---
name: ris-port-adapter-worktrunk-worktrees
description: >-
  Execute and verify bounded worktrees/1 list, read or create operations through
  explicitly selected Worktrunk (wt), with exact repository/path/branch/commit
  inputs and inspected tool side effects. Use for direct Worktrunk operations
  or as the selected adapter; not task claim, belonging decisions, environment
  acceptance, planning, repair, deletion or publication.
---

# Worktrunk worktree adapter

Own only the requested tool operation and its verified effects. Direct calls
need no RIS config, tracker, common/context, portable base or Git-adapter skill.
The caller owns association, permissions, setup and the combined result. Read
`references/worktrunk.md` from this installed folder **before operations** and
apply its CLI mapping, JSON checks and independent Git oracle. Before creation,
also read/apply `references/effects.md`: effective hooks and configuration are
preflight inputs even when setup was not requested. Read its copy section only
when authorized copy-ignored is involved. Do not merely name these resources.

Advertise `worktrees/1` list/read/create, actual wt/Git versions, checked
capabilities and guarantees. Require explicit repository/invocation root,
operation, absolute target for read/create, literal branch and full pinned base
commit for create, expected absence or explicitly authorized existing-branch
state, read/write/hook scope and actual project constraints. Check availability
of the selected tool before dependent writes. Missing/incompatible wt, incomplete
JSON or uncontrolled mandatory effects block; do not switch to Git creation.
Git inspection/fetch is the mapped supporting oracle, not an adapter fallback.

Return `status: ok|blocked|conflict|error`, operation/tool/versions, requested and
observed repository common directory, path/branch/HEAD/base, index/files/operation
diagnostics, list completeness, actual ref/copy/config/hook/process effects,
checks, limits and safe recovery. Reconcile every nonzero/ambiguous response
through Git before retry. Distinguish a verified copy from pending/failed setup;
do not accept environment readiness for the caller. Ordinary new creation without
hooks/setup checks registrations, target/ref, pinned base and the actual new copy,
not all primary/sibling file contents. Reuse binds selected-copy HEAD/refs/index
and changed/protected bytes; hooks/setup bind their exact protected resources and
authorized outputs. Limit preservation claims to those observations.
Preserve existing work:
no force/clobber, reset, rebase, stash, commit, repair/prune, deletion, automatic
rollback or blind retry. Individual Git locks and read/write/read do not promise
cross-operation uniqueness. Ordinary creation needs no manual window/global lock;
an explicitly required stronger unsupported guarantee returns its exact limitation
before writing, without asking to pause writers.
Stop at this bounded result; no claim, technical plan or next lifecycle operation.
