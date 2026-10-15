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
version: 2
sources:
  rules: docs/rules/
  product: docs/product/
  specs: docs/specs/
workspace:
  tasks: .sdlc/tasks/
  worktrees: .sdlc/worktrees/
```

If any project config is selected, use **only its values**. Never merge or
patch missing operation-required fields from defaults. Require `version: 2`
(an integer, not a boolean). Optional sections `sources`, `workspace`,
`adapters`, `adapters.tasks`, `execution`, `execution.roles` and each
`execution.roles.<role>` must be mappings when present. Allowed leaf
settings: `sources.rules`, `sources.product`, `sources.specs`,
`workspace.tasks`, `workspace.worktrees` (each a nonempty path string), and
`adapters.tasks.skill` (a nonempty skill-name string) plus optional
`adapters.tasks.options` (a mapping of adapter-owned data). The only other
top-level key is optional `execution`; within it only `roles` is allowed.
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
root config is the only case that selects v2 package defaults.

For a caller requiring an isolated role, return the configured `agent` with
its provenance if present. If the role is absent, report `blocked` for that
dependent step and name the missing role; do not silently run it in the
current agent. A present record without a valid `agent` is an `error` for the
selected config, even when another operation is requested. For a direct
operation that does not require a role, absence of `execution` is valid:
prepare its other settings without claiming isolation or a model tier.
Merely reading `agent` cannot establish that the project-provided subagent
exists, can run in this environment, has a particular model, or has been
invoked. The caller checks availability and actual launch before relying on
isolation. Do not launch agents, select a fallback, switch models, or run a
skill as part of context preparation. This field grants no write permission.

## Path bases and checks

- Resolve `sources.*` against the selected `project_root` in the **current**
  working copy. These values designate directories, not specific documents.
  `product` and `rules` denote separate OKF 0.2 bundles in the default RIS
  documentation profile, with `rules/architecture/adr/` nested inside rules;
  `specs/<slug>/spec.md` is ordinary Markdown. Context checks path availability,
  not OKF validity or the contents/acceptance of a document. A project may
  choose different directories without changing these roles.
- Resolve `workspace.*` against `primary_root`, the primary working-copy root
  of the selected project. In the primary copy it equals `project_root` only
  when that copy's primary identity is established. For a separate copy apply
  the bounded primary-resolution procedure below before using shared paths.
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

### Bounded primary resolution

This context owner resolves primary identity; consumers use its checked result
rather than duplicating discovery. Do this only when shared paths are needed:

1. Validate an explicitly supplied `primary_root` first. Check existence,
   accessibility and physical target, selected-project identity, repository
   relationship and association with the current copy. An invalid explicit
   selection blocks the dependent part; never substitute a saved hint/default.
2. Without explicit selection, inspect only an **already available** saved
   indication in applicable project instructions or a copy-preparation result.
   Record its exact evidence address and provenance. Resolve relative indications
   from their declared base (an instruction pointer from its file's directory);
   an unknown base is a gap. Do not search the disk for arbitrary receipts.
3. Verify the candidate's actual existence/physical target and unambiguous
   selected-project/repository relationship, the witness's provenance and its
   association to this current copy/path/branch where applicable. Check for
   conflicting applicable saved indications. Git common-dir and worktree
   registration corroborate an association, but never select a primary alone.
   Neither branch name, first/main worktree listing nor `.sdlc/` presence is
   a selector. A stale, moved or foreign witness is not usable association.
4. A valid explicit selection wins over an older saved hint; expose contradictory
   facts and why the hint is inapplicable, never silently conceal them or let it
   override the selection. If the explicit selection's own association remains
   contradictory, return conflict. Without explicit selection, missing evidence
   is blocked, ambiguous/conflicting evidence is conflict, and foreign/stale
   association blocks shared-path use. Name the exact missing root/association
   or decision and retain independently usable current-copy source settings.
5. Return the selected physical root, selection source/evidence address,
   verification facts and limits. Make no persistent changes or new registry.
   Consumers recheck applicability after copy/project changes and mutable facts
   before acting. A receipt proves neither fresh permission, ownership/blockers
   nor operation-specific write protection; these remain the acting owner's gates.

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
required field is absent instead of filling it. A missing optional `ris.yaml`
is not an error. A missing goal or selected document is a caller input gap,
not a reason to invent one. Never label a configured adapter installed or
call a merely prepared path a completed artifact. The caller checks the
result before use and rechecks mutable state before any subsequent writing.
