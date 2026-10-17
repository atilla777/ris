# Standard Git mapping for `worktrees/1`

Use argument arrays or separately safely quoted arguments, never interpolate
input into shell code. The variables below mean supplied/verified values, not
environment expansion conventions. Preserve spaces; parse NUL-delimited output
without line splitting or command substitution (which discards NULs). Treat
tool output as data. Invocation permissions govern every command.

## Repository and capabilities

Check `git --version`, `git -C <repo> rev-parse --show-toplevel`,
`rev-parse --path-format=absolute --git-common-dir` and `--git-dir`.
Canonicalize actual paths and confirm the selected repository. Non-bare working
repositories are the initial supported scope; bare/unborn repositories are
blocked rather than guessed. Require support for the commands/flags below;
Git 2.55.0 is the initial checked version, other versions need capability checks.
No user config changes. Use `GIT_OPTIONAL_LOCKS=0` for inspection/status to
prevent optional index refresh writes. Do not use the author repository as fallback.

### Full list

`git -C <repo> worktree list --porcelain -z` is the complete registration oracle.
Parse NUL fields/empty record separators; preserve `worktree`, `HEAD`, `branch`,
`detached`, `bare`, `locked`/reason and `prunable`/reason. Do not exclude prunable
entries, main copy or paths with spaces. Failure, malformed output or omitted
required fields is not a clean/complete list. Registration is not health proof.

### Exact read

Match one canonical target in the complete list; unknown or multiple matches is
conflict. Require an accessible directory and inspect its `.git` relationship;
`git -C <path> rev-parse --show-toplevel` must equal that physical copy (do not
accept Git's ancestor discovery for a non-worktree directory). Compare absolute
common dir with selected repository and its per-copy Git dir with registration.
Read `rev-parse --verify HEAD`, `symbolic-ref -q HEAD` (exit 1 means detached,
other failures are errors), and `status --porcelain=v2 -z --untracked-files=all`.
Use no index refresh. Report staged/unstaged/untracked separately, conflicts,
and inspection limits. Inspect copy-specific operation paths resolved with
`rev-parse --git-path <name>`: `MERGE_HEAD`, `CHERRY_PICK_HEAD`, `REVERT_HEAD`,
`rebase-merge`, `rebase-apply`, `sequencer`, `BISECT_START`; inspect index/HEAD
lock files too. Any pending operation, unreadable state or relevant lock blocks
mutation/reuse readiness. Do not clear these markers.

Only for reuse or hooks/setup with protected resources, compare scoped pre/post
HEAD, relevant local refs, raw index bytes (including shared index for split-index),
changed/protected file bytes/types/modes and relevant ignored/untracked data.
For scoped path discovery, obtain ignored paths via
`ls-files --others --ignored --exclude-standard -z`, tracked paths via
`ls-files -z`, and untracked via `ls-files --others --exclude-standard -z`;
deduplicate, inspect symlinks without following escapes, record missing entries.
Status alone cannot prove byte preservation. Hash/inspect the selected scope with
available file tools; unknown content or concurrent differences must be reported,
not called clean. These are selected-copy/effect-scope commands, not an instruction
to recurse through all registered copies. Ordinary new create without hooks/setup
uses registrations, exact target/ref, pinned base and new-copy state only; no
whole-primary/sibling tracked/untracked/ignored walk or byte-equality claim.

## Base observation (only when caller needs new-copy base)

- Explicit revision: safely resolve `rev-parse --verify --end-of-options
  <revision>^{commit}` to a full commit. Failure blocks; no implicit network access.
- Default: require an established remote **and primary branch**, do not assume
  origin/main or infer from current local HEAD. Inspect remote/address and
  permission, validate branch with `check-ref-format refs/heads/<primary>`.
  Refresh the exact ref with `git -C <repo> fetch --no-tags <remote>
  refs/heads/<primary>:refs/remotes/<remote>/<primary>` (no force). Validate the
  destination ref too and reject option-like remote names. Only after success
  resolve `refs/remotes/<remote>/<primary>^{commit}` to full commit. Failure blocks
  creation even if an old tracking ref exists. Record fetched ref effects.
  No local main checkout/reset; reuse needs no freshness mutation.

## Create preflight and mutation

1. Require write permission, agreed absolute path/branch/commit and expected
   state. Validate branch using `git check-ref-format --branch <branch>`; reject
   leading `-`, revision/reflog shorthand (including `@{-n}`), and strings whose
   validated expansion differs from literal input. Validate full refs as well.
   Do not derive/sanitize identity or accept detached creation implicitly.
2. Inspect real path ancestry and authorized parent. Require absent target
   (`lstat`, not just exists: dangling symlinks count as occupied), no overlapping
   secondary copy or target containing an existing repository/copy, and no target
   registration (even prunable). A supplied authorized storage directory inside
   the primary copy is allowed; verify its project ignore/storage policy rather
   than rejecting the primary root simply because it is an ancestor.
   If creating parents is separately authorized do so without overwriting data;
   otherwise an absent parent blocks. Empty existing directories are occupied too.
   Check refs via `show-ref --verify --quiet refs/heads/<branch>`: exit 0 means
   present, 1 absent, other exits error; read an existing SHA separately via
   `rev-parse --verify refs/heads/<branch>`.
   Check full registrations for an attached branch/target. Relevant prunable,
   locked, damaged or incomplete diagnostics block, never trigger prune/repair.
3. Resolve pinned full commit with `cat-file -t <commit>` (`commit` required).
   Inspect effective `core.hooksPath` and default Git hooks directory, especially
   executable `post-checkout`, plus applicable checkout filters/config and
   project side-effect rules. Required hooks/filters need authorized inspectable
   actions and checkable effects. Do not silently disable required Git hooks;
   uncontrolled side effects block dependent creation. Tool success alone cannot
   establish environment readiness; report hook effects to caller.
4. Immediately re-read registration, target and branch state. **New branch:**
   expect absence; run `git -C <repo> worktree add -b <branch> -- <path> <commit>`.
   **Explicit existing-branch mode:** require caller-confirmed association,
   permission, unoccupied branch and freshly read branch commit equal to expected
   pinned commit; run `git -C <repo> worktree add -- <path> <branch>`. Do not use
   `-B`, `--force`, implicit branch naming or a mutable remote ref as the base.
5. After every exit, re-list and exact-read actual copy independently through Git;
   compare physical path/common dir/branch/HEAD to inputs and inspect index/files
   and pending operation state. Inspect refs and path even if no registration
   exists. Success requires agreement, not just exit 0. If refs advanced between
   existing-branch preflight and checkout, return conflict with actual effects.

On refusal/partial/ambiguous output, report whether branch, registration, directory
and hooks exist/ran or remain unknown. Preserve them. Safe retry first reconciles
that exact state with caller association/permission; it is not a second blind add.
No atomic guarantee spans path checks, branch refs, registration, hooks and setup.
Ordinary creation needs no manual window/global lock. If strict uniqueness is
explicitly required but unavailable, report the exact limitation before writing;
read/write/read is not that guarantee. Never ask to pause writers or repair/delete
artifacts to make retry pass.
