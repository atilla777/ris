# RIS configuration v2 — preparation procedure

Use this resource from the installed `ris-proj-op-resolve-context` skill. It is the operational
contract; do not require access to RIS's documentation repository at runtime.

## Inputs and selection

1. Establish the calling operation and its **specific** required settings,
   which directories are existing inputs and which are prospective outputs,
   any execution role required by the caller (or that none is required),
   task parameters, and allowed actions. Investigate available facts before
   asking a user; if a necessary decision is missing, report what it blocks.
   No operation makes all settings universally mandatory. A concrete document
   is chosen by the caller from its task inputs and document links, not here.
2. Determine the target `project_root` from the task, working environment and
   applicable instructions. Do not infer it from this skill's installation,
   RIS source, a config file, or a sibling project. The supported Git layout is
   one repository — one project; monorepo subprojects are not supported.
   Ambiguous project roots block affected preparation.
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
version: 2
sources:
  rules: docs/rules/
  product: docs/product/
  specs: docs/specs/
workspace:
  tasks: .sdlc/tasks/
  worktrees: .sdlc/worktrees/
workflows:
  prepare_feature:
    auto_accept: true
```

With a selected project config, use its values except for these leaf defaults:
an omitted `workspace.tasks` is `.sdlc/tasks/`, and an omitted
`workspace.worktrees` is `.sdlc/worktrees/`, also when `workspace` itself is absent.
An explicit valid leaf overrides only that leaf; directory presence never chooses
settings. An omitted `workflows.prepare_feature.auto_accept` defaults to boolean
`true`, including when `workflows` or `prepare_feature` is absent. This applies
to existing v2 configs without migration. This is not general config merging: do not supplement `sources.*`,
adapters or execution roles. Validate all present fields before applying defaults;
null, empty or wrong-type workspace values are errors, not omissions.
Require `version: 2`
(an integer, not a boolean). Optional sections `sources`, `workspace`,
`adapters`, `adapters.tasks`, `workflows`, `workflows.prepare_feature`, `execution`, `execution.roles` and each
`execution.roles.<role>` must be mappings when present. Allowed leaf
settings: `sources.rules`, `sources.product`, `sources.specs`,
`workspace.tasks`, `workspace.worktrees` (each a nonempty path string), and
`adapters.tasks.skill` (a nonempty skill-name string) plus optional
`adapters.tasks.options` (a mapping of adapter-owned data). The only other
top-level keys are optional `workflows` and `execution`. Within `workflows` allow
only `prepare_feature`, and within it only `auto_accept`: strictly a YAML boolean
`true` or `false` (not YAML-1.1-style `yes`/`no`/`on`/`off`), never strings
(including `"true"`), null, numbers, lists or
mappings. Empty mappings at either parent mean omission; null/wrong-type parents
are errors. Unknown workflow keys are errors even for callers not using them.
Within `execution` only `roles` is allowed.
Within `roles`, each nonempty, non-whitespace role identifier maps to a
record with exactly one allowed key, `agent`, whose value is a nonempty,
non-whitespace string naming a project-provided OpenCode subagent. The caller
determines which semantic role identifiers its operation requires; do not
invent or enforce a global role list. An empty roles mapping or absent roles
is not a substitute for a role required by the caller. Reject unknown
keys except within `options`, wrong types, null/empty values in place of
required settings, duplicate or merge keys, YAML aliases, custom tags,
executable expressions, and malformed YAML. No `extends` or imports. Do not
silently ignore an invalid present field even if this operation does not use
it. Missing fields only block operations that require them; do not require
adapter selection for unrelated document preparation. Adapter `options`
belong to its own contract, not an invented RIS schema. A configured adapter
is not proof it is installed or supports an operation. There is no package
default for `execution`; do not supplement an absent role in a selected
project config (or a missing section) from any other config or example.
Reject v1, including `sources.concepts`, with a migration diagnostic rather
than aliasing the old key or falling back to defaults. To migrate, review
the intended author-owned product source, set `version: 2`, replace
`sources.concepts` with its actual `sources.product` directory, and check
all existing fields, links and consumers. Do not assume the old concepts
directory contains product knowledge or rename it automatically. An absent
root config selects the full v2 package defaults; a selected valid file gets only
the workspace leaves and auto_accept default described above.

Return the requested workflow value with explicit-config path/key/version or
package-default provenance (distinguish absent optional root from omitted leaf
in a selected valid config). Validate the whole selected config first: any invalid
present field prevents automatic continuation, never a fallback to `true`.
Context prepares this setting only; only `ris-proj-flow-prepare-feature` may use
it to determine separate requirements/design acceptance modes. It grants no
auto acceptance to direct specify/design calls or other workflows and no action
authority, substantive answers, review approval, implementation or closure.

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
and write scope; provenance for each returned setting (including a requested
`execution.roles.<role>.agent`); specific diagnostics,
limitations and independent usable partial data; `changes: []`. State when a
required non-defaulted field is absent instead of filling it. Record each workspace
leaf's explicit-config or package-default provenance. A missing optional `ris.yaml`
is not an error. A missing goal or selected document is a caller input gap,
not a reason to invent one. Never label a configured adapter installed or
call a merely prepared path a completed artifact. The caller checks the
result before use and rechecks mutable state before any subsequent writing.
