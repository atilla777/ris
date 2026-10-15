# Consume a supplied task-specific or separate copy

Read for a task-specific/separate copy or after a copy change, before dependent
mutations or shared-path access. This wrapper owns task association and project
applicability, not working-copy preparation or tool-specific worktree operations.

- Verify the supplied repository/project relationship, actual revision/state and
  established task → copy/branch/path association using available current facts
  and handoff evidence. A conventional branch name alone proves no ownership.
- Reprepare context after a copy change. Sources belong to the current project
  root; shared notes/tracker access use context's checked primary selection and
  provenance (explicit or verified available saved indication) for a separate
  worktree. Recheck association and fresh permissions/claim/blockers before
  mutation; a saved witness or lease is not general write protection. Do not silently substitute a local task directory or a
  different tracker. Require only paths needed by the dependent action.
- Preserve pre-existing staged/unstaged/untracked work and unfinished operations.
  Unsuitable, ambiguous or conflicting state blocks dependent mutation; report
  observed facts and the needed suitable-copy handoff without an implicit repair.
- Copy preparation owns creation/reuse and environment readiness; the selected
  `worktrees/1` adapter owns concrete commands, tool side effects and observation
  mapping for those operations. Do not reproduce their algorithms, invoke them
  from implementation or infer that a copy/claim isolates shared state or gives CAS.
