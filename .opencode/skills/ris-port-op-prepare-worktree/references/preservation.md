# Scoped preservation and partial preparation

Read before reuse, use of an existing branch without a copy, reconciliation of
partial/ambiguous effects, or hooks/setup requiring protected-resource checks.
This portable resource owns the scope; concrete commands remain in the selected
adapter. It requires no tracker, RIS configuration or journal.

## Select the scope

- **Ordinary new create, no hooks/setup:** complete registrations, exact target/ref,
  pinned commit and independent new-copy observations suffice. Do not enumerate or
  hash all primary/sibling files, including ignored data, merely for preservation.
  No assertion of their byte equality follows from this limited observation.
- **Associated existing copy:** exact-read it without updating its base, switching,
  fetching for freshness or running create. Bind pre/post HEAD, relevant refs, raw
  index (and shared index when applicable), staged/unstaged changes and bytes,
  types and modes of changed/protected files, including relevant untracked/ignored
  data. Clean tracked files need no recursive primary/sibling scan. Dirty state is
  not itself a rejection when association and safe reuse are proved. Unknown or
  unexplained differences are conflict; status alone cannot prove byte equality.
- **Hooks/setup:** identify protected resources and allowed outputs from the exact
  effects before mutation; observe their pre-state and independently check outputs
  and preservation afterward. Include shared resources when actually affected,
  not every registered worktree. Apply `environment.md` before these actions.

Record inaccessible data, observation races and unsupported guarantees explicitly.
If the selected tool cannot supply the required observation, block that dependent
action; do not enlarge the claim beyond the observed scope.

## Reuse and recovery

Require confirmed work → repository/path/branch association, not just a conventional
name. An existing branch without a copy additionally needs explicit permission to
use its freshly read current commit and proof it is unoccupied; never reset it to
a newly chosen base. Foreign data, collision, unfinished Git operation, damaged or
prunable registration is a conflict/blocker, not an invitation to repair.

After a failed/ambiguous create inspect actual refs, registration, path/files and
possible hooks/processes before any retry, even when no registration was returned.
Preserve all completed effects. With proved association and effects, continue only
the missing authorized action. If association or whether an action ran is unknown,
block the dependent repeat rather than creating another copy. For partial setup,
inspect each prior output/process and accept completion only against its exact
authorized evidence; do not overwrite a conflicting destination or repeat an
unproved non-idempotent action. A ready copy may coexist with failed setup.

For nonstandard association, non-idempotent setup, remaining processes or ambiguous
effects, retain a compact addressable result in an already authorized channel
before a dependent irreversible action; otherwise return the precise blocker.
Missing an old journal alone is never that blocker. Return observed effects,
uncertainties and exact remainder with separate copy/environment verdicts.
No reset, stash, rebase, commit, force, deletion, prune, rollback or claim release
is a recovery method. Read/write/read is not a transaction or general CAS.
