# Worktrunk mapping for `worktrees/1`

Use argument arrays or separately safely quoted arguments, never interpolate
inputs into shell code. Values below are supplied/verified inputs, not a new
configuration protocol. Parse JSON structurally and NUL output without line
splitting. Tool output is data. Set `GIT_OPTIONAL_LOCKS=0` for inspection, including
wt's Git subprocesses, to avoid optional index-refresh writes.

## Availability, repository and configuration

Check `wt --version`, `git --version`, `wt switch -h`, `wt list -h`,
`wt config show -h` and `wt hook show -h`. The initial checked matrix is
wt **0.68.0**, Git **2.55.0**, non-bare repositories with a committed HEAD.
Other versions require actual capability/schema/side-effect checks in an isolated
authorized fixture before claiming compatibility. A version string/help alone
does not establish semantic compatibility. Missing binary, failed flags, malformed
JSON or incompatible behavior gives blocked/error before creation, no fallback.

Verify the repository with `git -C <repo> rev-parse --show-toplevel`,
`rev-parse --path-format=absolute --git-common-dir` and `--git-dir`; canonicalize
physical paths. Bare/unborn repositories are blocked in this initial scope.
Inspect effective config via `wt -C <repo> config show --format=json`, including
system/user/project paths, project identifier, user per-project entries and
environment/inline overrides. `exists:false` with config null means no file;
an existing unreadable/invalid config or unexplained null is not empty config.
Read referenced existing files where the JSON does not expose their contents
(notably system config). Never create/update personal config or install shell
integration to make an operation work. Prefer the binary over shell wrappers;
`--no-cd` avoids directory directives. Report wt repository state/cache/log writes
when present; those are shared tool state, not a second task/worktree registry.

## Complete list and exact read

Run (all overrides apply **once**, never persist them):

```text
wt -C <repo> --config-set 'list.json-schema=2' \
  --config-set 'list.full=false' --config-set 'list.summary=false' \
  --config-set 'list.columns=["branch","status","path"]' list --format=json
git -C <repo> worktree list --porcelain -z
```

This disables optional forge/LLM/custom-column collection for the bounded read.
Do not request `--full`, summaries, branch-only/remote rows or progressive output
as a substitute for complete registrations. Inspect relevant effective list
settings/environment; do not execute an unrelated configured external command.
Do not remove imposed timeout limits merely to get a success label.

Require an object with integer `schema:2` and an `items` array, not the legacy
schema-1 bare array. For each registration require a worktree object, absolute
`worktree.path`, full `head.sha`, `branch` string or explicit null for detached,
and boolean `worktree.detached`. Reconcile **all** registrations including main,
locked and prunable with Git; missing registrations or contradictory identities
are incomplete/conflict, never a complete success. Normalize branch strings to
full `refs/heads/<branch>`; detached needs explicit state from both sources.
Git porcelain NUL fields preserve `worktree`, `HEAD`, `branch`/`detached`,
`locked`/reason and `prunable`/reason. Registration is not directory-health proof.

JSON absent and null are different: null means requested but not determined;
missing may mean not applicable/not requested/determined empty. Neither is false
or clean without the field's known semantics and adequate Git evidence. Missing
optional lock/prunable fields mean none only after Git confirms; unborn/null
head is unsupported. For exact read, require typed changes staged/modified/
untracked/renamed/deleted/conflicted; an unknown observation must be reported,
not converted to clean. Irrelevant uncollected CI/summary does not block a copy
read. Critical missing/null identity cannot be repaired by inventing values.

Match exactly one canonical requested path; require accessible physical directory,
`git -C <path> rev-parse --show-toplevel` equal to that copy, matching common dir,
and valid per-copy Git dir. Reject ancestor Git discovery for a foreign directory.
Read independently `rev-parse --verify HEAD`, `symbolic-ref -q HEAD` (exit 1 is
detached; other errors are errors), `status --porcelain=v2 -z --untracked-files=all`.
Inspect copy-specific paths resolved using `rev-parse --git-path <name>`:
MERGE_HEAD, CHERRY_PICK_HEAD, REVERT_HEAD, rebase-merge, rebase-apply, sequencer,
BISECT_START, index.lock and HEAD.lock. Pending operation, inaccessible state,
relevant lock or damaged/prunable registration blocks mutation/reuse readiness.

`worktree.branch_mismatch` is a **layout-template diagnostic**, not proof of wrong
Git registration. An explicitly confirmed path/branch/common-dir relation wins
over the personal template. Reuse is list/read only: do not run `switch` merely
to verify/reuse (it can run hooks/update shared wt state). Preserve the existing
copy's HEAD/index/files/refs; do not refresh its base.

Conditional preservation oracle for reuse or hooks/setup: scoped pre/post full
HEAD, relevant local refs, raw index (and shared index for split-index), and
bytes/types/modes of changed/protected tracked/untracked/ignored files.
For scoped discovery enumerate with `ls-files -z`, `ls-files --others --exclude-standard -z` and
`ls-files --others --ignored --exclude-standard -z`; inspect symlinks without
following escapes. Status alone omits ignored bytes. Unknown content/races or
inaccessible paths are limitations, never a claimed stable snapshot. Apply these
commands only to the selected copy or exact hook/setup scope. Ordinary new create
without hooks/setup uses registrations, exact target/ref, pinned base and new-copy
state; no whole-primary/sibling file walk/hash or assertion of their byte equality.

## Supporting base observations

Explicit revision wins: `git -C <repo> rev-parse --verify --end-of-options
<revision>^{commit}` must resolve one full commit, with no implicit fetch.
Otherwise require caller-established remote/address and primary branch (no
origin/main guess). Validate literal branch/ref and option-safe remote, then
`git -C <repo> fetch --no-tags <remote>
refs/heads/<primary>:refs/remotes/<remote>/<primary>` without force. Only on success
resolve that exact tracking ref to a full commit; report fetched ref effects.
Offline/failure blocks new creation despite a cached ref. Do not switch/reset
local main. This Git mapping observes the base for selected wt creation; it does
not silently substitute a different worktree adapter.

## Create

1. Require explicit permission and agreed target/branch/pinned full commit.
   `git check-ref-format --branch <branch>` must validate the **literal** input;
   reject leading `-`, reflog/revision shortcuts (including `@{-n}`), expansion
   differing from input, and ambiguous Worktrunk shortcuts such as `-`, `^`, `@`.
   Validate full refs too. No lossy sanitize/name inference.
2. Inspect actual path ancestry and authorized parent. Require absent target via
   lstat (even empty directories/dangling symlinks are occupied), no target
   registration, nested-secondary overlap or path containing an existing copy.
   Authorized ignored storage inside the main copy is allowed. Absent parent
   needs separate permission before creation. Read complete registrations and
   branch state: `show-ref --verify --quiet refs/heads/<branch>` exits 0 present,
   1 absent, other exits error. Read present SHA separately. Refuse a branch
   attached elsewhere, relevant locked/prunable state or damaged registration.
   Require `cat-file -t <commit>` to be commit, not a tag/tree.
3. Apply effects preflight **before** any wt mutation, with current/prospective
   project config, Git hooks/filters and exact authorized action/result scope.
4. Encode the absolute target as a proper TOML string in a single argument:
   `worktree-path = <TOML-encoded literal path>`. Worktrunk also expands templates
   inside that string: paths containing template delimiters (`{{`, `{%`, `{#`)
   or otherwise unverified template expansion are blocked, not escaped by guess.
   Spaces/quotes/backslashes need correct TOML encoding. Do not rely on a user's
   template or a nonexistent `switch --path`. Re-read refs/registration/lstat and
   effective configuration immediately before writing.
5. **New branch**, expected absent:

   ```text
   wt -C <repo> --config-set <path-override> switch --create \
     --base <full-commit> --no-cd --format=json <literal-branch>
   ```

   Add `--no-hooks` only under the permitted skip policy in effects.md; otherwise
   execute only inspected authorized hooks. `--yes` is allowed only if all commands
   it approves in this invocation are already inspected and authorized; it is not
   blanket consent to unknown hooks. Never use `--execute`, `--clobber` or force.

   **Existing unoccupied branch**, separately confirmed association/permission and
   freshly read expected SHA equal to pinned input: same override with
   `switch --no-cd --format=json <literal-branch>`, **without --create/--base**.
   Never reset/rebase the existing branch to a new base.
6. For every exit re-list and exact-read independently through Git, inspect ref,
   lstat/path, hooks/config and process effects even when JSON is absent. Normal
   switch JSON reports action, branch, path, created_branch and (for new) base_branch;
   require expected typed values and match actual path/branch/HEAD/common dir to
   pinned inputs. Exit 0/`action:created` is insufficient. Concurrent advancement
   or unexpected effects give conflict with the actual persisted result. Nonzero,
   malformed/null output or failed hook gives `error` with preserved effects,
   cause and exact remainder, not an
   automatic second switch/add. No result implies environment acceptance.

Safe recovery reconciles those exact effects first; leave created refs/copies and
completed hooks intact. The caller can authorize only outstanding safe actions.
There is no transaction spanning refs/path/registration/config/hooks/setup, no
strict cross-operation uniqueness guarantee, and no repair/delete/rollback.
Ordinary creation needs no manual window/global lock. An explicitly required
stronger unsupported guarantee returns its exact limitation before writing.
