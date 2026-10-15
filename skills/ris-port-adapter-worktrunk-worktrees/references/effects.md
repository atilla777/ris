# Worktrunk effects preflight

Read before creation; the caller owns permissions, environment actions and final
environment acceptance. This resource owns wt-specific discovery/execution
observations, not a second general setup algorithm. No hooks/copy/start is
authorized merely because a config or ignored file exists.

## Effective hooks and automatic side effects

Use `wt -C <repo> config show --format=json` and
`wt -C <repo> hook show --format=json`; inspect actual referenced system/user/
project files, per-project user entries, applicable WORKTRUNK_* overrides and
inline config. Sources can combine; a project hook does not replace a same-type
user hook. Hook JSON gives type/source/template/name/needs_approval; approval
state is not permission for this invocation. Do not run an uninspected alias.

Inspect both invoking-copy project config and config that will exist in the new
copy at the pinned commit (or existing branch SHA), including an explicit
WORKTRUNK_PROJECT_CONFIG_PATH if applicable. Read exact blob without checkout;
relative config paths resolve from each copy. Git checkout/hooks may affect the
config; unexpected differences stop subsequent actions. `hook show --expanded`
uses the **current** copy's variables: it is not proof of new-copy destinations.
Resolve templates for the exact new branch/path/source/primary copy, inspect
scripts and bound reads/writes/network/process lifecycles to the authorized scope.
Unknown dynamically selected commands or required uncheckable effects block.

On 0.68.0 switching/creation can run pre-switch, pre-start, post-start and
post-switch hooks; inspect all applicable types, ordering, concurrent tables and
sequential pipelines, not only pre-start. Foreground pre-* exits may stop the
operation **after** refs/registration exist. Post-* are detached/background:
successful switch does not mean they finished. Logs/launch messages/PIDs alone
do not prove success. Require an observable return code/completion artifact or
approved service-readiness signal bound to this exact instance, and verify its
outputs. Where configured hooks cannot provide that observation, block mandatory
setup before creation; optional effects need a caller-approved bounded policy.
Do not silently kill jobs, remove artifacts or repeat completed hooks on retry.

`--no-hooks` may suppress additional wt hooks only when project/caller rules
explicitly permit skipping them; it is not the default workaround for unknown
mandatory actions. It does **not** authorize skipping mandatory Git hooks. Inspect
effective `git config --show-origin --get core.hooksPath` (absence means default
hooks directory), executable post-checkout and checkout filters/attributes/config.
Resolve relative hooksPath in the checkout context. Inspect expected hook/filter
effects and verify them independently; no `core.hooksPath=/dev/null` override.
Preflight the invoking and target checkout contexts. A required unknown Git
hook/filter blocks creation even if wt --no-hooks is permitted. Preserve shared
repository config and primary-copy state; wt itself can update previous-branch
state/cache/logs. Report these authorized tool-state effects explicitly.

## Conditional: authorized `copy-ignored`

Read/apply only if an authorized setup/hook actually invokes this wt command.
The caller supplies exact source/destination and allowlist, protected shared
paths, expected bytes/types and retry policy. wt's default **all ignored** is
not permission; built-in excludes do not cover all tracker/notes layouts.

Check `wt step copy-ignored -h` capabilities. Inspect .worktreeinclude and
effective `step.copy-ignored.exclude` in system/user/per-project/project config
and overrides; inspect real ignored source paths, nested worktrees and symlinks.
Where an approved .worktreeinclude exists use `--require-include`. Do not edit a
project's include/config implicitly to obtain an allowlist; when it cannot
express the authorized set, block this copy route and let the caller decide.
Includes use gitignore patterns, not literal arrays; prove their actual selected
set rather than assuming a narrow-looking glob is exact.

Run from the verified source with **explicit** branch endpoints:

```text
wt -C <source> step copy-ignored --from <source-branch> --to <target-branch> \
  --require-include --dry-run --format=json
```

On 0.68.0 JSON dry-run exposes `outcome:"planned"`, `dry_run:true`, exact
`from`/`to` paths and an `entries` array of `kind`/`path` candidates. Require
those typed fields, inspect both streams and independently enumerate sources;
expand directory entries to their actual contents. Aggregate counts alone
cannot establish a safe selection. Every selected path must be
within the explicit allowlist, inspectable, with safe real ancestry and absent
destination; reject escaped symlinks, shared tracker databases, primary-copy
notes, Git metadata, nested copies and other shared mutable resources. Use
one-shot extra excludes only if their semantics/actual selection are checked;
no broad copy, overwrite or `--force`. Recheck include/config/source/destination
immediately before repeating the **same** command without --dry-run.

Observe foreground completion, actual copied bytes/types/modes and excluded-path
preservation. Existing destinations are skipped by wt; skipped is not successful
setup unless exact current bytes/type match previously authorized evidence.
Nonzero/ambiguous results retain copied effects and are reconciled before retry.
A copy launched by a post-* hook still requires its own bound completion signal.
If dry-run/selection is incomplete or hooks hide a broad copy command, block the
dependent effect rather than trusting a count or wt's default exclusions.
