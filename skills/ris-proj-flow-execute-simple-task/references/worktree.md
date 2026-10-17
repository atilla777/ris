# Conditional isolation through existing preparation owners

Read before preparation when project rules demand isolation, parallel changes
overlap, the current copy is busy/foreign, or its ownership/safety is ambiguous.
Do not move dirty foreign work to a new branch to avoid this condition.

- With a real confirmed task ID, load/apply
  `ris-proj-op-prepare-task-worktree`. Pass exact project/ID/actor, current copy,
  checked primary selection/provenance for shared paths, agreed task → repository/
  path/branch association, exact base or authorized established remote selection,
  selected adapter and permitted claim/copy/setup/evidence effects. Keep fresh
  ownership/blocker gates. Do not fabricate an ID to use this owner.
- Without an ID, load/apply `ris-port-op-prepare-worktree` directly with explicit
  work identity, repository/current root, agreed absolute path/own branch/base,
  association evidence, actual project constraints and permissions. No
  `workspace.tasks/<invented-ID>` or fake task record. Obtain only the needed
  project settings/authorized path through context when applicable. Adapter choice
  follows the preparation owner's contract; the owner loads/applies the selected
  available `worktrees/1` adapter. Do not bypass an unavailable selected adapter.

These owners retain copy/environment preflight, preservation, creation/reuse and
verification algorithms. Do not duplicate Git worktree commands here. Supply
shared tracker/notes/nested-worktree exclusions to authorized environment setup;
copy creation does not imply installation or service startup.

Inspect the returned canonical repository/path/branch/HEAD, pinned base or reuse
basis, index/files/untracked/unfinished-operation state, association and actual
effects; verify copy readiness separately from requested environment readiness.
Re-resolve context in the resulting project copy with context-checked primary
when needed; verify current rules/config and selected tracker workspace again.
Wrong project/config/association blocks dependent work; no fallback tracker init.
Keep existing branch/copy on reuse and preserve foreign work on failure. Partial
or ambiguous creation/setup activates recovery; never prune, reset, delete,
recreate or repeat setup blindly. Return the checked copy to the main route.
