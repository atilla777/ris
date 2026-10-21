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

The package also owns `.opencode/plugins/ris-help/` once the installed management
resource proves ownership. An unproven plugin-directory collision stops unchanged;
foreign plugins and all global settings are preserved. Local edits inside the
proven package plugin are replaced. No global CLI/plugin configuration is written.

**Quit and restart OpenCode** after installation or any package change so it
discovers the updated skills, commands and client plugin (OpenCode V2, checked on 2.0.32).

## Start using RIS

### Current readiness and limits

This section is the current readiness entrypoint; the catalog supplies exact
contracts, while delivery records retain their original revisions and limits.
The earlier readiness baseline is source revision
[`00d012fe35e70f1857ef12216b76a33318e77e37`](https://github.com/atilla777/ris/tree/00d012fe35e70f1857ef12216b76a33318e77e37),
not a certification of every project or runtime. The feature-preparation source
change ris-b1a.3 is integrated and Git-published in
[`c5de3e112c9e35813a5af91b290acccbe1758ec1`](https://github.com/atilla777/ris/commit/c5de3e112c9e35813a5af91b290acccbe1758ec1).
This source-publication fact does not itself certify independent review, live
behavior or the rest of the accepted S1 lifecycle; review evidence retains its
own snapshot, provenance and scope.

| Route | Prerequisites and boundary |
| --- | --- |
| Portable interview, formulation, planning or review | Supply the selected operation's inputs and scope; no RIS config or tracker is required. |
| Project initialization | Install first, select the project and agree writes/decisions. `/risp-init` checks that specific local setup and names deferred or blocked operations, not whole-system readiness. |
| Roadmap and feature preparation | Applicable product/rules, capable tracker and precise requirements/design acceptance; preparation uses one early ID/copy and dialogue through reviewed published inputs, verified decomposition and separate tracker publication. |
| Task or registered-bug execution | Sufficient accepted inputs, actor/claim/blocker checks, safe own copy/branch, available executors and independent review. Bug investigation and fix readiness are distinct. |
| Publication and completion | Established target, direct-push rights, applicable checks and exact reviewed snapshot; Git, exact tracker completion and Dolt publication are separate effects. PR-only projects cannot use this direct-push route. |
| Status, continuation and retrospective | Status/next inspect current facts; retrospective needs accessible identified session evidence. None grants execution authority or proves lifecycle readiness. |

- **Installed is not discovered:** restart OpenCode after package changes and check
  the actual client command/skill availability. The client-help baseline is
  **OpenCode 2.0.32**, not a claim about every client/version.
- **Tracker limits:** the Beads adapter baseline is **1.3.1**. Claims, native row/
  close guards, `--sandbox` and fresh read/write/read are not general content/graph
  CAS or distributed exclusion. Unsupported required guarantees block the dependent
  write; see the [adapter contract](skills/ris-proj-adapter-beads-tasks/SKILL.md).
- **Feature documents, not JSON readiness cards:** new features use
  `sources.specs/<full feature ID>/spec.md` (default specs root `docs/specs/`),
  readable H1 and column-zero `Feature-ID:`, `Summary:`, optional `Keywords:`.
  Requirements and sufficient inline/adjacent design retain actual independent
  scope/version acceptance. Beads holds ordinary goal/scope/criteria/state/edges,
  not duplicate accepted refs, identity pins or saved verification. Successful
  verify-and-close still checks the whole feature but needs no persisted assessment.
  Early registration needs a chosen feature, title/goal and stable key, not
  spec/design/epic; the same ID can obtain a safe preparation copy. ID/copy is not
  readiness. Existing explicit links/readable legacy hints lead to actual documents
  and decisions without migration; missing/old/malformed JSON alone never blocks
  this route. Historical data/specifications remain untouched. This scoped
  [ris-wcv amendment](docs/specs/ris-wcv/spec.md) supersedes old JSON refusal/pin/
  verification norms, not substantive acceptance or review/Git/close/Dolt gates.
- **Recovery:** task notes are local, not automatically synchronized or mandatory
  remote inputs. Resume reconciles accessible exact evidence and actual effects;
  missing notes do not justify invented acceptance, review or publication. See the
  [execution contract](skills/ris-proj-flow-execute-task/SKILL.md).
- **Evidence:** source/static checks establish instruction structure and consistency;
  actually executed program checks establish only their tested mechanisms/versions.
  Observed agent behavior remains tied to its session, inputs and revision. Neither
  documents nor program tests establish general agent reliability, cost or
  repeatability; historical unverified obligations remain unverified. See
  [verification levels](docs/product/05-adoption-and-validation.md#4-три-уровня-проверки)
  and [program checks](docs/development.md).
- **Operational boundary:** RIS does not supply release, deploy, rollback or
  production operations. Source publication is not deployment or production readiness.
- **Operation authority and delivery:** a full request includes its ordinary
  constituent actions through existing owners; narrower limits and substantive
  acceptance/review gates remain. Context selects shared primary paths by explicit
  input → verified saved association → verified ordinary Git source copy, never
  the first worktree. This grants no right to change that copy. New assignments
  can use a verified current-session actor fallback, never to take over old work.
  Confirmed remote Git is complete independently of optional safe local updating;
  skipped/failed maintenance does not block exact close or Dolt. An explicitly
  requested local update remains a separate unfinished part of that request.
  Shared Dolt publication follows the selected project's accepted policy (RIS
  permits accumulated shared history), not an automatic policy change elsewhere.

### Available commands and operations

The current source menu has 21 explicit entries (16 project + 4 portable + one
help exception), adding `/risp-status`, `/risp-run-simple-task`, `/risp-init` and
`/ris-help` to the historical 18-entry v1 set and retiring `/risp-plan-task`.
`risp-` selects a project contract, `risb-` a portable contract. `/ris-help` is the
sole naming exception, supplied by a client/TUI plugin rather than a Markdown
command facade, with no aliases. All 51 source skills
are listed in the catalog; operations without
a slash command can be loaded directly by their exact technical skill name. Examples:

| Goal | Command |
| --- | --- |
| Prepare an agreed local RIS setup after installation | `/risp-init <project and scope>` |
| See daily SDLC help, detailed pages or explain a route without execution | `/ris-help`, `/ris-help full` or `/ris-help <question>` |
| Explore a topic through an interview | `/risb-interview <topic>` |
| Review a concrete change | `/risb-review-change <change and scope>` |
| Prepare a feature through one requirements/design dialogue and verified decomposition | `/risp-prepare-feature <ID, epic or context>` |
| Independently decompose or resume decomposition of accepted published inputs | `/risp-decompose-feature <ID>` |
| Execute or resume one project task | `/risp-run-task <ID>` |
| Execute or resume one clear, already assigned simple request | `/risp-run-simple-task <request and optional ID>` |
| See the complete unclosed plan and one next action | `/risp-status` or `/risp-status <ID>` |
| Find the next step for selected work | `/risp-next <ID>` |

Replace angle-bracket placeholders with your inputs. Skills clarify missing
information and required permissions. Project-integrated work checks its own
prerequisites; installing the package does not initialize a project or tracker.
Use `/risp-init` separately for a new or existing project's settings, bounded
`AGENTS.md` addition, separately accepted product/architecture/engineering documents
and checked RIS infrastructure. It preserves usable existing material, keeps one
human dialogue and applies authorized owners directly or delegates standalone
operations to the agreed available executor (`project-initialization`). Missing
tools, Git/Beads setup and project agent definitions require their specific
permissions. The result distinguishes local
readiness, deferrals and remaining work; commit/push is offered separately.
Init checks project-owned `standard`/`advanced` subagents with explicitly pinned
models, recommends choices from the target's current available catalog and agrees
missing choices/changes without re-asking suitable saved decisions. Its proposed
role split is Standard for selection/decomposition/orchestration and Advanced for
requirements/design/implementation/review. No global edits or silent upgrades;
see [tier setup and readiness limits](docs/installation.md#standardadvanced-project-agents).
It does not start roadmap/features/development or configure build/test/format/CI.

Role bindings select executors for delegation, not mandatory delegation of each
internal step. Delegation uses the configured role and verified actual launch;
an unavailable role blocks that delegated route, without silent substitution.
Required independent review actually launches separately from all authors/repairers.
Bindings alone prove neither model, invocation, independence nor Advanced
implementation. Direct authorized work does not require unused roles.

Feature preparation uses early registration and one safe ID-associated copy before
document writes. One dialogue yields two precisely accepted scopes (one explicit
act may accept both), sufficient inline design, independent review and Git
publication; the same record then reaches verified decomposition and separate
tracker publication. Direct specify/design/decompose calls remain scoped alternatives,
not mandatory extra steps. Preparation does not start implementation.

Decomposition can describe dependent tasks before a sufficiently defined accepted
prerequisite is implemented, retaining necessary directed blocks (dependent →
prerequisite). Unknown or disputed contracts block only the dependent portion;
independently sufficient results remain usable without a claim of full coverage.
Execution readiness is checked separately against accepted inputs, needed
integrated prerequisites, current blockers and authority. Planning permission or
task existence never grants permission to implement; native refusal is preserved.

Help needs no configured project, `ris.yaml`, Beads or source checkout. Empty input
displays fixed daily Markdown locally, **without any model call**: status/next, feature preparation/decomposition
and task execution. `/ris-help full` (`/ris-help полный` in Russian) shows detailed
thematic pages locally without a model, including installation/init, roadmap,
individual execution stages, bugs, acceptance and retrospective. Use arrows/j/k,
PgUp/PgDn, Home/End to scroll and Esc to close. Empty input uses the terminal's
`LC_ALL`/`LC_MESSAGES`/`LANG` (Russian for `ru`, otherwise English); `simple`/`brief`
and `full`/`detailed` explicitly select English, `простой`/`кратко` and
`полный`/`подробная справка` Russian. Only exact whole arguments select fixed pages.
Questions invoke the agent with `ris-proj-op-show-help` attached: they are queued
in the current session, or open a new location-scoped help session from Home.
Unlike fixed pages, these questions use the model. The help skill recommends but
never writes or launches work, and does not certify readiness.
Actual task continuation remains `/risp-next`, actual plan/status `/risp-status`.
Package availability is not proof that the current client has discovered the command.

Simple-task execution uses a clear bounded request without mandatory interview,
spec/design, decomposition, plan or report files. The main agent implements and
publishes through existing owners; a separate independent subagent reviews, with
high/medium repair and re-review. It requires its own branch; a suitable current
copy is allowed, and isolation needs activate worktree preparation. When that own
copy is also the verified primary root, the publisher may safely return it from
the task branch to the established primary branch and fast-forward only after
remote confirmation. Busy/foreign/dirty copies remain protected; skipped/failed
local updating neither invalidates remote Git nor blocks close/Dolt, and never
calls for repeating a confirmed push. Checks are
proportionate and mandatory project checks/TDD still apply. A supplied ID keeps
its real contract; mandatory project accounting creates/reconciles a short task
(**Beads remains mandatory in RIS**). Empty input asks for work, never selects a
queue item. Direct push requires rights, checks, independent review and remote
confirmation; tracker result, exact close and publication are separate effects.
Full task/bug execution likewise needs no saved plan or implementation report;
its safe-copy, TDD, ordinary YAML review and publication/completion gates remain.

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
separate justified disposition. One assigned investigator is sufficient
organizational control for ordinary saving with authorized targeted native writes,
fresh comparison, preserved original/foreign content and independent read-back;
this is not CAS or exclusion of every parallel writer. Missing authority/capability
or observed conflict can block saving without blocking research. See the separately
accepted [persistence policy amendment](docs/specs/local-bugfix/investigation-persistence-policy.md).
For supplied inputs without a tracker,
load `ris-port-op-investigate-bug`. Investigation stops before fixing.

To fix an exact registered native bug, load `ris-proj-flow-fix-bug` with the
selected project, ID, actor and authorized fix/publication scope. It checks the
saved report and criteria, returns precise gaps when insufficient, obtains separate
acceptance for material design when needed, preserves a full historical input
snapshot in bug notes, then uses the complete existing task execution flow.
A sufficient report replaces formal spec/design files. Implementation starts from
sufficient accepted inputs and current code, without a standalone planner, saved
plan/omission-decision or implementation report. Code TDD, independent review,
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

**First update to client `/ris-help`:** use that same new-revision bootstrap,
even if `risp-`/`risb-` commands or the older agent-backed `/ris-help` are installed.
Old engines reject the new ownership-manifest `format=2` header before writes,
because they cannot ship client plugins. The new engine removes the obsolete
`ris-help.md` facade so it cannot collide with the client command; subsequent
updates use the new installed engine. Use a plugin-aware bootstrap for recovery.

For shell commands, version selection, manual installation and interrupted-operation
recovery, see the **[installation guide](docs/installation.md)**. For old names and
consumer/config changes, see the [namespace transition guide](docs/skill-command-naming-migration.md).

## Documentation and development

Ordinary project review saves one local `review.yaml` using
[ris.review/1](skills/ris-proj-op-review-task/references/report-format.md); Beads
keeps only its address/round. Fast retains independent session-only review, with
the same format for optional saves. Format validity alone is not current-snapshot
approval; local reports are not automatically available on another machine.
The source contract introduced by ris-b1a.4 removes both standalone task planners
and `/risp-plan-task`, without aliases,
and removes plan/implementation-report producers and consumers under accepted
[S1 §4 / D1 §5](docs/specs/sdlc-feature-lifecycle/acceptance.md). Source availability
does not establish Git publication, independent approval, live behavior or whole-S1
acceptance; those require their own applicable evidence. Execution checks current-input sufficiency and a viable approach;
review/recovery assess final results, not author RED/GREEN history. TDD remains
the executor's duty; missing history is not proof and known violations stay visible.
Historical plans and delivery records remain unchanged optional context.

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
