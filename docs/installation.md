# Installing, updating and removing RIS

Use the [README quick start](../README.md#install-in-opencode) for first installation.
All package operations use one
[Bash engine](../skills/ris-port-op-manage-installation/scripts/ris-install.sh).
The [management skill](../skills/ris-port-op-manage-installation/SKILL.md) invokes
that same engine; it does not implement a separate copying algorithm.

## Requirements

Choose an **existing absolute project path**; spaces are supported. Runtime tools:

- **Bash 3.2+, Git 2.20+, flock**.
- Standard Unix `cp`, `mv`, `rm`, `mkdir`, `rmdir`, `mktemp`, `chmod`, `cmp`,
  `diff`, `id`, `ls`, `readlink`.
- On Linux use util-linux flock. On macOS install **discoteq/flock 0.4.0**,
  for example with `brew install flock`; `/bin/bash` is sufficient.
- `curl` is needed only for the README download step. Python 3 is development/test-only.

The installer reports missing tools and never installs dependencies. It does not
require `ris.yaml`, Beads, OpenCode or a Git repository in the target project.
Project-integrated skills have their own prerequisites after installation.

The combined current source menu is **22 commands (17 project + 4 portable + one
help exception)** and **53 skills / five flows**, including `/ris-help` →
`ris-proj-op-show-help` and `/risp-run-simple-task` →
`ris-proj-flow-execute-simple-task` under the
[accepted D2 amendment](specs/compact-commands/spec.md#8-поправка-fast-task-execution-d2--один-новый-вход).
It also includes `/risp-status` → `ris-proj-op-show-plan` under
[plan-status D1](specs/plan-status/design.md#8-поставка-и-совместимость).
It adds `/risp-init` → `ris-proj-flow-initialize-project` under
[initialization D1](specs/project-initialization/design.md). Choose a complete
published package revision containing the needed additions; a source candidate
and this guide alone do not establish installation, parity or delivery
success. Counts in a historical pinned revision remain those of that revision.

After package installation and discovery refresh, invoke `/risp-init <project and
scope>` separately to agree and check local project settings, instructions,
documents and RIS infrastructure. It preserves existing work and obtains separate
content decisions through the document authors. Tool installation, Git/Beads side
effects and project agent definitions need their own agreed scope; installation
permission does not grant them. Init offers publication separately and stops
before roadmap/product development or build/test/format/CI setup. The installer
still performs no project initialization or configuration writes.

### Standard/Advanced project agents

`/risp-init` checks **both project definitions and effective OpenCode settings**
for `standard` and `advanced`, including mode, pinned model/variant and caller/
child permissions. Global-only agents or model inheritance do not satisfy this
project-owned tier setup. New agents use `mode: subagent`; an existing suitable
`all` mode may be preserved. Hidden agents need exact-ID availability checks;
visibility alone is not launch permission.

Init recommends exact model IDs from the **target project's current available
catalog**, with source/date, reasons and known capability/cost limits, then asks
which models you want where the choice is missing or materially changing.
Standard favors adequate capability and cost/latency for ordinary organizational
work; Advanced favors capability for complex work and review. No model version or
provider is a permanent package default; a missing catalog is an explicit gap,
not permission to guess a "latest" model. Existing suitable saved choices are
reused without another questionnaire or automatic upgrade. Catalog availability
is not proof of a successful authenticated model request.

The proposed `ris.yaml` bindings are:

| Agent | RIS roles |
| --- | --- |
| `standard` | `feature-selection`, `task-decomposition`, `task-execution` |
| `advanced` | `feature-preparation`, `task-implementation`, `task-review` |

`project-initialization` is agreed separately, normally proposed as `advanced`
for document work. Existing alternative bindings are preserved until a specific
migration is agreed. These are init proposals, not new resolver defaults or
mandatory roles for every direct RIS operation. An independent reviewer is a
fresh invocation separate from all authors/fixers, not necessarily another model.

After agreement, init creates/updates only the bounded project definitions in
`.opencode/agents/<name>.md` or the project's existing native V2 `agents` config
entries, preserving unrelated settings, comments, visibility and permission
policy. The model is explicit in each OpenCode agent definition, not in RIS's
role records. Init does not edit global settings, write credentials, silently
escalate rights or duplicate competing definitions. It records choices in the
agreed settings-decision document, default `docs/ris-initialization.md`.

Saved definitions, effective agent/model discovery and agreed role mappings are
rechecked without test sessions or model requests. A disruptive refresh requires
appropriate permission. Refusal, override conflicts or unavailable discovery/
models/permissions leave explicit readiness limits and remaining actions; they
do not erase independent useful results or count as a fully ready working cycle.
The [operational contract](../skills/ris-proj-flow-initialize-project/references/agents.md)
and [bounded amendment](specs/project-initialization/agent-tiers-amendment.md)
describe the current tier requirements; historical v1/D1 decisions stay pinned.

## Selecting a version

Leave `ref` empty in the quick start to follow upstream remote HEAD, regardless of
branch name. Set it to an **exact tag** or **full 40-hex commit SHA** to pin a version.
The downloaded raw script and `--ref` use the same pin.

Branch names and Git revision expressions are not `--ref` inputs. Lightweight and
annotated tags are supported; a 40-hex tag spelling is interpreted as a commit SHA.
For tags containing URL-special characters, URL-encode `raw_ref` in the bootstrap
while retaining the literal tag in `ref`. Incomplete package revisions are rejected.
Download errors stop before script execution; the bootstrap does not use `curl | sh`.

## Manage from an agent

After RIS is available to the agent, use an explicit operation and target:

```text
/risb-installation install RIS in /absolute/path/to/project
/risb-installation update RIS in /absolute/path/to/project to tag v-example
/risb-installation uninstall RIS from /absolute/path/to/project
```

The skill clarifies missing intent or target, runs its owner-relative script and
checks exit status, paths, counts and the version record. Update/removal is never
silently changed to install. `v-example` is a placeholder for your chosen tag.

## Manage from the shell

**First migration from long commands:** an old installed engine cannot acquire
the compact package. Use the README checked-download bootstrap from the chosen
new package revision, with that same tag/full SHA for both script and package.
Its `install` fully replaces the previous package; alternatively run that newly
downloaded engine's `update` against an existing installation. Do not run the old
installed engine for this first migration. Subsequent updates use the new installed
engine at the unchanged technical path below. There are no old-name aliases.
See the [complete 39-command map](skill-command-naming-migration.md#compact-command-migration--39).

The first update to the client `/ris-help` package needs the **new plugin-aware
engine** via the same checked-download bootstrap pinned to the new revision.
Old engines do not ship plugins; do not use an old self-update for this migration.
The shipped ownership manifest begins with `format=2`, so pre-plugin engines
reject acquisition before target writes rather than recording false ownership.
The obsolete `.opencode/command/ris-help.md` is removed to avoid a collision.
After migration use the plugin-aware engine for update, uninstall and recovery;
an old external engine does not manage the complete new package.

```bash
bash '/absolute/project/.opencode/skills/ris-port-op-manage-installation/scripts/ris-install.sh' update --project '/absolute/project' # Optional --ref TAG_OR_SHA
bash '/absolute/project/.opencode/skills/ris-port-op-manage-installation/scripts/ris-install.sh' uninstall --project '/absolute/project'
```

`install` fully replaces an existing or manual installation. `update` requires
at least one managed element or version file. `uninstall` removes the managed
package and rejects `--ref`; repeating it is an offline successful no-op.
After the installed script is gone, an external copy of the engine can perform
that repeated request.

**Quit and restart OpenCode after package changes.** A running session retains
its loaded instructions.

## What changes and what is preserved

The reserved package paths are:

- `.opencode/skills/ris-*` — complete skill folders and their resources.
- `.opencode/command/ris-*.md` — reserved legacy templates, including removal of
  the obsolete agent-backed `ris-help.md` facade, without aliases.
- `.opencode/command/risp-*.md` and `risb-*.md` — compact command templates,
  only after package ownership has been established.
- `.opencode/ris-installation` — four-line format/source/full revision/harness record.
- `.opencode/plugins/ris-help/` — paired server/TUI plugin and its bilingual
  fixed Markdown pages, only with proven installed package ownership.

**Local edits to proven package paths and legacy reserved paths are overwritten**,
and retired elements are removed. Short-name ownership is recorded by the shipped
management-skill resource `references/command-ownership.txt`, whose list must
cover the selected package's compact command files without extra paths after
its `format=2` capability header (not a command or alias). The
separate `references/plugin-ownership.txt` proves ownership of the exact
`ris-help` plugin directory, never an arbitrary `ris-*` prefix. An existing plugin
at that name without installed ownership evidence, including a symlink, causes a
preserved conflict. Do not extend these resources to claim foreign files.
`ris-help.md` remains in the reserved legacy overwrite/removal namespace.
The management command and four-line version record are unchanged.
An old version marker or the new prefix alone is insufficient. Pre-existing
unproven short files/links cause a conflict before replacement/removal: preserve
them, inspect their ownership and explicitly resolve the collision (for example,
move your own command to a non-package name) before repeating. Ordinary proven
package updates require no extra per-file approvals. Keep this ownership resource
with complete manual package copies; do not extend it to claim foreign files.
Use names outside `ris-`, `risp-` and `risb-` for project additions. No timestamp or
backup history is kept in the unchanged four-line version record.

Other skills, commands and plugins, OpenCode settings, `ris.yaml`, `AGENTS.md`, docs/tasks,
alternate `skill/` and `commands/` locations, and global installations are preserved.
Check alternate/global locations for shadowing; the installer does not migrate them.
For old identifiers and consumer/config changes, see the
[namespace transition guide](skill-command-naming-migration.md).

Ordinary parent directories are required: symlink parents and unsafe managed
objects are refused. Old managed links are replaced as links without touching
their external targets.

Verify the full SHA and skill/command counts in the success report, inspect
`.opencode/ris-installation` and ordinary `git status`. Installed files and the
version record remain subject to the project's normal Git workflow. The installer
does not add ignores, initialize Git, commit or push, and does not override
existing project ignore rules.

## Interruption and recovery

The engine serializes cooperating processes for the same OS user and physical
project root. A busy lock exits without target writes. Before replacing its own
script, it continues from a private external copy.

A verified snapshot and schema-2 journal at `.opencode/.ris-install-transaction/`
support offline recovery **before any network operation**. A pre-commit failure
restores old bytes, types, modes and link targets. After SIGKILL, the next valid
request repeats the restore from immutable backup. Committed or rolled-back
terminal markers permit cleanup only, even after partial backup removal. The new
engine also reads historical schema-1 journals, retaining their foreign plugin
classification. Old engines must not recover a schema-2 transaction.

Exit **0** means verification and cleanup completed. Nonzero diagnostics distinguish
not changed, restored, recovery required, or applied/restored with cleanup incomplete.

- Repeat a valid request to finish recovery or cleanup.
- If the installed script was removed by interruption, use the README bootstrap
  again for the same project with the new plugin-aware engine.
- If the journal is unknown or damaged, preserve its exact reported path for
  diagnosis; do not delete it or try another install over it.

Guarantees cover process interruption on a working filesystem, not power loss,
storage corruption, ACLs/xattrs or concurrent edits by other tools.

## Client help

OpenCode V2 discovers `.opencode/plugins/ris-help/index.ts` and its `tui.tsx`
automatically (checked on 2.0.32); no global `cli.json` or `opencode.json` edits
are needed. The paired server entry is a no-op. Fixed daily/full Markdown is
rendered by the client with no model call, including without credentials/session.
English/Russian whole-argument selectors and locale defaults are in the README.
Semantic questions resolve the installed `ris-proj-op-show-help` skill and queue
one prompt with that attachment, creating a location-scoped help session from Home
only when needed. Missing/ambiguous skill or request failure produces an error,
not a fake alias or silent model fallback. This is a TUI entry, not a server/CLI
`opencode run --command` facade. Clients without this TUI plugin can directly load
the help skill; that is agent-backed and does not promise a no-model page.

Fixed pages have one source at `plugins/opencode/ris-help/pages/`; the installer
copies it into the plugin, and direct help-skill requests read that same installed
location. A manual complete-help copy needs the plugin/pages as well as the skill.

## Manual installation of a portable skill

Copy the **complete** skill folder, including resources, into a client-supported
discovery location. For example, the autonomous interview needs no RIS config or
other RIS skill. In OpenCode copy:

- `skills/ris-port-op-interview/` → `.opencode/skills/ris-port-op-interview/`.
- Optional: `commands/opencode/risb-interview.md` → `.opencode/command/risb-interview.md`.

Quit and restart OpenCode. Directly loading `ris-port-op-interview` needs no
command. A selective copy lacks the complete package's ownership evidence: before
a subsequent full install, explicitly reconcile that manually copied short
command if it causes a collision. Legacy reserved skill folders are replaced.
