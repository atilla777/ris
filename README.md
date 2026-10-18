# RIS — Ready-to-use Infrastructure Skills

RIS supplies reusable Agent Skills for software development: interviews,
requirements, design, planning, implementation, review and delivery. Use individual
operations or workflows that coordinate feature preparation and task execution.

- **Portable skills** (`ris-port-*`) work from direct inputs without RIS project
  configuration or a tracker.
- **Project skills** (`ris-proj-*`) add the applicable project rules, configuration,
  document paths and tracker integration.

## Install in OpenCode

Requires **Bash 3.2+, Git 2.20+, flock** and standard Unix utilities. Linux uses
util-linux flock; on macOS install **discoteq/flock 0.4.0** with `brew install flock`.
The download step also requires `curl`. See [full requirements](docs/installation.md#requirements).
Installation needs no `ris.yaml`, Beads or Git repository in the target project.

Choose an **existing absolute project path**. Leave `ref` empty for upstream remote
HEAD, or set an exact tag/full 40-hex commit SHA to pin a package revision:

```bash
(
  project='/absolute/path/to/project'
  ref='' # Or an exact tag / full commit SHA of a complete package revision.
  raw_ref=${ref:-HEAD}
  installer=$(mktemp /tmp/ris-bootstrap.XXXXXXXX) || exit 1
  trap 'rm -f "$installer"' EXIT
  url="https://raw.githubusercontent.com/atilla777/ris/${raw_ref}/skills/ris-port-op-manage-installation/scripts/ris-install.sh"
  if ! curl --fail --show-error --location "$url" --output "$installer"; then
    exit 1
  fi
  args=()
  if [ -n "$ref" ]; then args=(--ref "$ref"); fi
  bash "$installer" install --project "$project" "${args[@]}"
)
```

**Installation replaces local edits in `.opencode/skills/ris-*` and
reserved `.opencode/command/ris-*.md` (including `ris-help.md`) and proven package `risp-*.md`/`risb-*.md`
commands, and removes retired package entries.** Unproven short-name collisions
stop with a conflict and preserve the files. Other skills,
OpenCode settings and project documents are preserved. Use other names for your
own additions. The installer reports the full revision and installed counts;
the version is recorded in `.opencode/ris-installation`.

**Quit and restart OpenCode** after installation or any package change so it
discovers the updated skills and commands.

## Start using RIS

The current source menu has 21 explicit entries (16 project + 4 portable + one
help exception), extending the historical 18-entry v1 set with `/risp-status`,
`/risp-run-simple-task` and `/ris-help`.
`risp-` selects a project contract, `risb-` a portable contract. `/ris-help` is the
sole naming exception, with no aliases. All 52 source skills
are listed in the catalog; operations without
a slash command can be loaded directly by their exact technical skill name. Examples:

| Goal | Command |
| --- | --- |
| See the compact SDLC map or explain routes without execution | `/ris-help`, `/ris-help run-task` or `/ris-help <question>` |
| Explore a topic through an interview | `/risb-interview <topic>` |
| Review a concrete change | `/risb-review-change <change and scope>` |
| Prepare a project feature through accepted requirements and design | `/risp-prepare-feature <epic or context>` |
| Decompose an accepted feature into tasks | `/risp-decompose-feature <ID>` |
| Execute or resume one project task | `/risp-run-task <ID>` |
| Execute or resume one clear, already assigned simple request | `/risp-run-simple-task <request and optional ID>` |
| See the complete unclosed plan and one next action | `/risp-status` or `/risp-status <ID>` |
| Find the next step for selected work | `/risp-next <ID>` |

Replace angle-bracket placeholders with your inputs. Skills clarify missing
information and required permissions. Project-integrated work checks its own
prerequisites; installing the package does not initialize a project or tracker.
Feature preparation ends at a published feature ID; decomposition is a separate step.

Help needs no configured project, `ris.yaml`, Beads or source checkout. Empty input
returns only one 80×24 map; cards/comparisons/intent routes are loaded on demand.
It recommends but never writes or launches work, and does not certify readiness.
Actual task continuation remains `/risp-next`, actual plan/status `/risp-status`.
The help source/docs candidate is locally integrated with upstream and awaits
fresh combined review and primary-branch publication; package
availability is not proof that the current client has discovered the command.

Simple-task execution uses a clear bounded request without mandatory interview,
spec/design, decomposition, plan or report files. The main agent implements and
publishes through existing owners; a separate independent subagent reviews, with
high/medium repair and re-review. It requires its own branch; a suitable current
copy is allowed, and isolation needs activate worktree preparation. Checks are
proportionate and mandatory project checks/TDD still apply. A supplied ID keeps
its real contract; mandatory project accounting creates/reconciles a short task
(**Beads remains mandatory in RIS**). Empty input asks for work, never selects a
queue item. Direct push requires rights, checks, independent review and remote
confirmation; tracker result, exact close and publication are separate effects.
Full task/bug execution and direct plan-task retain their contracts.

`status` is read-only: without an ID it shows the project's complete unclosed plan;
with an ID it shows that subtree and necessary context/blockers. It recommends one
action using the continuation owner and checks the installed command, or reports an
exact gap. It saves nothing, claims no work and launches nothing. `next` inspects an
already selected subject; `select-feature` chooses a feature; `run-task` executes.

To record a bug before investigation, ask the agent to load
`ris-proj-op-register-bug` for the selected project and message, with permission
to record it. It checks duplicates, saves or supplements the report, returns a
verified ID and stops. Investigation and fixing are separate requests.

To investigate that ID, load `ris-proj-op-investigate-bug` for the selected
project and research/write scope. It saves a current report and distinguishes
defect confirmation from fix readiness; proved not-bug/duplicate messages have
separate justified disposition. Required content protection can block a report
write without blocking useful research. For supplied inputs without a tracker,
load `ris-port-op-investigate-bug`. Investigation stops before fixing.

To fix an exact registered native bug, load `ris-proj-flow-fix-bug` with the
selected project, ID, actor and authorized fix/publication scope. It checks the
saved report and criteria, returns precise gaps when insufficient, obtains separate
acceptance for material design when needed, preserves a full historical input
snapshot in bug notes, then uses the complete existing task execution flow.
A sufficient report replaces formal spec/design files. A saved plan is conditional
on execution/handoff needs and project rules; RIS itself keeps its mandatory local
plan, and a direct plan-task call still saves one. Code TDD, independent review,
working-copy/claim and publication requirements remain. Fix/checks, Git publication,
separate exact bug completion and tracker publication are distinct verified effects.
Registration, investigation and fixing are separate direct-load calls, with no new
slash commands. See the [delivery evidence](docs/specs/local-bugfix/delivery-checks.md)
for the inspected revision, coverage and limits.

See the **[complete skill and command catalog](docs/skills.md)** for all operations,
their results, naming conventions and links to individual contracts.

For initial product knowledge, directly load `ris-port-op-formulate-product-foundation`
to obtain a sourced, read-only proposal, or `ris-proj-op-author-product-foundation`
for a selected project's separately accepted, saved and checked `sources.product`
content. Both support create and bounded update; neither initializes the project,
plans a roadmap or starts development. No new slash command is added.

## Update or remove

Once RIS is available to the agent:

```text
/risb-installation update RIS in /absolute/path/to/project
/risb-installation uninstall RIS from /absolute/path/to/project
```

To pin an update, add `to tag <tag>` or `to commit <full SHA>`. Both operations use
the same Bash engine as initial installation. Restart OpenCode after changes.

**First migration from long commands:** use the checked-download bootstrap above
from the chosen **new** package revision (same pin for script and package).
An old installed engine cannot acquire compact commands. The bootstrap's `install`
replaces the previous complete package; subsequent updates use `/risb-installation`.
Old slash names are removed without aliases; see the complete
[39-command migration map](docs/skill-command-naming-migration.md#compact-command-migration--39).

**First update to `/ris-help`:** pre-help compact engines also reject its exact
ownership-resource entry. Use that same new-revision bootstrap, even if `risp-`/
`risb-` commands are already installed. A rejected acquisition leaves the target
unchanged; subsequent updates use the new installed engine.

For shell commands, version selection, manual installation and interrupted-operation
recovery, see the **[installation guide](docs/installation.md)**. For old names and
consumer/config changes, see the [namespace transition guide](docs/skill-command-naming-migration.md).

## Documentation and development

- [Skill and command catalog](docs/skills.md)
- [Installation, updates, removal and recovery](docs/installation.md)
- [Development guide and package checks](docs/development.md)
- [RIS product knowledge and target methodology](docs/product/index.md)
- [Repository rules](docs/rules/index.md) and [agent instructions](AGENTS.md)
- [Delivery specifications and plans](docs/specs/README.md)

Product knowledge and plans include future work; bundle presence does not establish
acceptance or readiness for a particular operation. Consult the catalog and linked
`SKILL.md` contracts for the available operations.

## License

MIT — see [LICENSE](LICENSE). The pinned third-party OKF specification in
`skills/ris-port-op-manage-okf-bundle/references/spec-v02.md` is Apache-2.0;
see its [source attribution](skills/ris-port-op-manage-okf-bundle/references/source.md).
