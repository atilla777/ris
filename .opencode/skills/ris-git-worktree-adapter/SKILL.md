---
name: ris-git-worktree-adapter
description: >-
  Execute and verify bounded worktrees/1 list, read or create operations with
  standard Git and explicit repository/path/branch/commit inputs. Use for direct
  Git worktree operations or as the selected worktree adapter; not ownership,
  task claim, environment setup, repair, planning or publication.
---

# Git worktree adapter

Own only the requested Git effect and its independently checked result. Direct
calls need no RIS, tracker, base or common/context installation. The caller owns
association, permissions, setup and the combined result. Read `references/git.md`
from this installed folder **before operations** and apply its exact CLI mapping,
preflight and reconciliation; do not merely name the resource.

Advertise `worktrees/1` with `worktrees.list|read|create`, actual Git version and
checked capabilities. Require explicit repository/invocation root, operation,
absolute target path for read/create, branch/full base commit for create,
expected absence or explicitly authorized existing-branch state, write/hook
scope and applicable project constraints. Check selected repository and CLI
availability before dependent writes. Failed capability or incomplete observation
is blocked/error, not permission to use Worktrunk or another repository.

Return status (`ok|blocked|conflict|error`), operation/tool/version, requested and
observed common directory/path/branch/HEAD/base, index/files/operation diagnostics,
list completeness, actual effects including partial hook/create/ref effects,
checks/limits and safe recovery. Git oracle reads must independently confirm
creation, even after nonzero/ambiguous output. Preserve existing work; no force,
reset, rebase, stash, commit, repair/prune, deletion, automatic rollback or retry.
Individual Git locks are not cross-operation uniqueness: external coordination
is required if the caller demands that guarantee. Stop at the bounded tool result;
do not decide belonging, claim work, accept environment readiness or invoke a
subsequent lifecycle operation.
