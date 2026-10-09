# RIS configuration v1 — preparation procedure

Use this resource from the installed `ris-context` skill. It is the operational
contract; do not require access to RIS's documentation repository at runtime.

## Inputs and selection

1. Establish the calling operation and its **specific** required settings,
   which directories are existing inputs and which are prospective outputs,
   task parameters, and allowed actions. Investigate available facts before
   asking a user; if a necessary decision is missing, report what it blocks.
   No operation makes all settings universally mandatory. A concrete document
   is chosen by the caller from its task inputs and document links, not here.
2. Determine the target `project_root` from the task, working environment and
   applicable instructions. Do not infer it from this skill's installation,
   RIS source, a config file, or a sibling project. In a monorepo identify the
   actual selected project. Ambiguous project roots block affected preparation.
3. Only after fixing the root, select the config: explicit task path first;
   otherwise the single unambiguous applicable project-instruction pointer
   (e.g. `AGENTS.md`); otherwise `ris.yaml` directly at `project_root`. Do not
   search parents or children or inherit a sibling project's file. A relative
   task path is based at the known invocation directory; a relative pointer
   in project instructions is based at that instruction file's directory.
   Conflicting same-priority pointers block dependent preparation. Explicitly
   selected missing, unreadable or invalid config is an error, never grounds
   for fallback. Only absence of the optional root file selects defaults.

## Schema and defaults

When the optional root `ris.yaml` is absent, use these package values:

```yaml
version: 1
sources:
  rules: docs/rules/
  concepts: docs/concepts/
  specs: docs/specs/
workspace:
  tasks: .sdlc/tasks/
  worktrees: .sdlc/worktrees/
```

If any project config is selected, use **only its values**. Never merge or
patch missing operation-required fields from defaults. Require `version: 1`
(an integer, not a boolean). Optional sections `sources`, `workspace`,
`adapters`, `adapters.tasks` must be mappings when present. Allowed leaf
settings: `sources.rules`, `sources.concepts`, `sources.specs`,
`workspace.tasks`, `workspace.worktrees` (each a nonempty path string), and
`adapters.tasks.skill` (a nonempty skill-name string) plus optional
`adapters.tasks.options` (a mapping of adapter-owned data). Reject unknown
keys except within `options`, wrong types, null/empty values in place of
required settings, duplicate or merge keys, YAML aliases, custom tags,
executable expressions, and malformed YAML. No `extends` or imports. Do not
silently ignore an invalid present field even if this operation does not use
it. Missing fields only block operations that require them; do not require
adapter selection for unrelated document preparation. Adapter `options`
belong to its own contract, not an invented RIS schema. A configured adapter
is not proof it is installed or supports an operation.

## Path bases and checks

- Resolve `sources.*` against the selected `project_root` in the **current**
  working copy. These values designate directories, not specific documents.
- Resolve `workspace.*` against `primary_root`, the primary working-copy root
  of the selected project. In the primary copy it equals `project_root`. From
  a separate worktree require `primary_root` supplied **explicitly** for any
  operation needing shared paths. Do not discover/substitute it silently or
  treat `.sdlc/` inside the worktree as shared. If unknown, block only the
  shared-path-dependent part and return independently usable source paths.
- Config location does not move either root. Absolute path values remain
  absolute, subject to scope and access checks. Do not interpolate `~`,
  `${ENV_VAR}` or `{{variable}}`. For `..`, symlinks or paths outside the
  selected root, inspect the actual target and authorized scope; explicitly
  approved external storage may be used, silent escape may not. Resolve
  Markdown links from the document's directory, not the path's config base.
- If a required **input** directory is missing or inaccessible, block its
  dependent operation. A prospective **output** directory need not yet exist
  if creation is permitted; check authorization and conflicts when the
  result owner actually writes. If writing is not authorized, return a
  proposal without claiming creation. Directory presence does not validate
  a document's content, acceptance, or OKF format.
- `workspace.tasks` and `workspace.worktrees` are base directories only.
  Without a confirmed tracker task ID, do not invent an `<id>` folder,
  project slug or branch name. Never create directories or worktrees here.
  Re-resolve paths in each recipient's environment after project/worktree or
  container changes; do not cache local absolute paths in `ris.yaml`.

## Permissions, result, and stopping conditions

Determine whether the request permits changes, and exactly which changes.
Default to `write: false`; a natural-language instruction can authorize
specific work without a YAML envelope. A path or config entry cannot grant
permission, and `write: true` cannot override project/environment restrictions.
RIS context itself **always makes zero persistent changes**, regardless of
caller permission. Do not run a task adapter merely because it is configured;
if a caller needs it, return its selection/options and leave availability,
operation semantics and tracker access to its actual contract. Do not
validate OKF bundles or read all the files in a document directory.

Return an equivalent structured block or clear prose with: `status` (`ok`
only when the requested preparation succeeded; otherwise `blocked` for
missing inputs or permission, `conflict` for ambiguity, `error` for invalid
or inaccessible selected config); `project_root` and `primary_root` when
needed and established; selected `config_file` or `config_source: package
defaults`; relevant resolved `settings`; `run` operation, task parameters
and write scope; provenance for each returned setting; specific diagnostics,
limitations and independent usable partial data; `changes: []`. State when a
required field is absent instead of filling it. A missing optional `ris.yaml`
is not an error. A missing goal or selected document is a caller input gap,
not a reason to invent one. Never label a configured adapter installed or
call a merely prepared path a completed artifact. The caller checks the
result before use and rechecks mutable state before any subsequent writing.
