# Resolve the ordinary source folder

Context owns this read-only resolution; consumers use its checked result rather
than implementing discovery. Read only for shared workspace paths or explicitly
requested source-copy maintenance. Support **one repository — one project**, an
ordinary non-bare source folder with its `.git` directory and linked worktrees.

1. From the selected current project copy obtain the physical Git top-level and
   common directory (`git rev-parse --show-toplevel --git-common-dir`), resolving
   relative Git output against the invocation directory. Require the project root
   to be that copy's repository root, not a monorepo subproject.
2. Resolve the physical common directory. It must be the ordinary source folder's
   `.git` directory. Verify its parent exists and is accessible, is non-bare, maps
   back to that same common directory, and is the registered ordinary source
   working copy. Verify the current copy's registration and shared repository
   association (native `git worktree list --porcelain` corroborates those facts).
   The branch name and worktree listing order do not select a folder.
3. Return that physical source folder as `primary_root` for consumer compatibility,
   with the checked Git association and limits. It is only the base of shared
   paths, not an integration workspace or authority to mutate its files/branch.
   Do not read saved-primary indications, cascade through candidate folders, scan
   the disk, persist a context result or introduce a registry. A supplied old
   `primary_root` may only corroborate this Git-derived root, never override it;
   a contradictory explicit assertion is a conflict, not a fallback opportunity.

Bare, missing/inaccessible source folders, separate/nonordinary common-directory
layouts, multiple-project mapping or contradictory registration are unsupported:
diagnose the exact dependent shared-path/maintenance operation and retain useful
independent current-copy settings. Do not pick another linked worktree. No Git is
needed for independent installation or agreed pre-Git bootstrap settings; this
does not fabricate a source-folder identity for shared Git operations.

After a copy/project change recheck the same association, not saved selection
evidence. Before mutation consumers still check fresh permission, own assignment,
blockers and operation-specific preservation. Resolving shared notes/worktree
addresses never permits branch switching or development in the source folder.
