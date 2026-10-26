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
  not duplicate accepted refs, identity pins or saved verification. Explicit
  verify-and-close still checks the whole feature but needs no persisted assessment.
  Ordinary parent closure instead trusts a nonempty complete set of closed direct
  children and checks parent blockers, without recursive acceptance/Git/review
  reconstruction. Closure-eligibility questions use those same reads without writes;
   zero-child features retain own-result verification. After confirmed task close
   and tracker publication, full execution (including bugfix via full)
   delegates the actual ancestor chain to one fresh `container-completion` subagent
   (`standard` recommendation); Fast applies the same tail inline in the main agent,
   without a mandatory closure role/subagent. Both close eligible parents with separate publication.
   It stops at the first unfinished/blocked parent; explicit limits win. Leaf
   completion and failed/unverified cascade effects are reported separately.
   Direct status/verification/container-close calls do not cascade. See the
  [container rules](docs/rules/development.md#отдельные-намерения-для-контейнера).
  Early registration needs a chosen feature, title/goal and stable key, not
  spec/design/epic; the same ID can obtain a safe preparation copy. ID/copy is not
  readiness. Existing explicit links/readable legacy hints lead to actual documents
  and decisions without migration; missing/old/malformed JSON alone never blocks
  this route. Historical data/specifications remain untouched. Substantive
  acceptance and review/Git/close/Dolt remain separate gates. The current
  [artifact contract](docs/product/06-artifacts-and-handoff.md) owns these norms;
  the historical [ris-wcv decisions](docs/specs/ris-wcv/spec.md) retain their versions.
- **Recovery:** task notes are local, not automatically synchronized or mandatory
  remote inputs. Resume discovers saved sources by project+ID and asks existing
  owners to reconcile actual effects, then continues only the missing operation.
  An explicit human request to continue/execute that task already authorizes
  guarded session reassignment without another takeover question or proof the
  previous session ended. Reuse its verified worktree/branch and preserve changes;
  old actor/lease alone neither blocks that request nor authorizes unrequested work.
  Lost required review is restored exactly or replaced by honest new independent current
  review; lost reproducible affected checks are rerun, and only lost acceptance
  scope needs a new human decision if the original cannot be found. None proves
  historical pass or requires replaying confirmed push/close. No handoff file,
  registry or transition log is required. Eligible Fast never owes absent,
  inapplicable review; known adverse findings remain. See the
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
  acceptance/review gates remain. In the supported one-repository/one-project layout,
  context derives the ordinary source folder from the actual common `.git`
  directory, without saved-primary discovery. Shared workspace leaves default to
  `.sdlc/tasks/` and `.sdlc/worktrees/` there, even with a selected config; explicit
  valid leaf overrides win. Sources resolve in the current worktree. Unsupported
  layouts get a bounded diagnostic, not another-copy discovery. This grants no
  right to change the source checkout. New assignments
   can use a verified current-session actor fallback, not as reassignment authority
   by itself; explicit human continuation follows the recovery rule above.
   Publication is remote-only without local authority. An explicit request or
   applicable accepted project policy can authorize separate safe local FF, never
   branch switching. Callers check/forward actual policy provenance, targets and
   boundaries; the publisher verifies it and all existing guards. Dependency
   refresh needs its own bounded authorization, not merely FF permission.
   Confirmed remote Git remains complete independently; skipped/failed maintenance
   does not block exact close or Dolt. Any policy-required or explicitly requested
   update remains unfinished in the combined result. RIS itself permits guarded
   post-confirmation source `main` FF from `origin/main`, with no dependency setup;
   this is not a global policy. See the [policy amendment](docs/specs/policy-primary-sync/amendment.md).
  Shared Dolt publication follows the selected project's accepted policy (RIS
  permits accumulated shared history), not an automatic policy change elsewhere.

### Available commands and operations

The current source menu has 20 explicit entries (15 project + 4 portable + one
help exception), adding `/risp-status`, `/risp-run-simple-task`, `/risp-init` and
`/ris-help` to the historical 18-entry v1 set and retiring `/risp-plan-task`.
`risp-` selects a project contract, `risb-` a portable contract. `/ris-help` is the
sole naming exception, supplied by a client/TUI plugin rather than a Markdown
command facade, with no aliases. The retired feature selector has no alias;
roadmap now owns preliminary feature planning. All 52 source skills
are listed in the catalog; operations without
a slash command can be loaded directly by their exact technical skill name. Examples:

| Goal | Command |
| --- | --- |
| Prepare an agreed local RIS setup after installation | `/risp-init <project and scope>` |
| Plan epics and preliminary features (nearest stage by default) | `/risp-roadmap <goal, epic-only / nearest / all>` |
| See daily SDLC help, detailed pages or explain a route without execution | `/ris-help`, `/ris-help full` or `/ris-help <question>` |
| Explore a topic through an interview | `/risb-interview <topic>` |
| Review a concrete change | `/risb-review-change <change and scope>` |
| Prepare a feature through one requirements/design dialogue and verified decomposition | `/risp-prepare-feature <ID, epic or context>` |
| Independently decompose or resume decomposition of accepted published inputs | `/risp-decompose-feature <ID>` |
| Execute or resume one project task | `/risp-run-task <ID>` |
| Execute or resume one bounded request or idea (also selectable naturally) | `/risp-run-simple-task <request and optional ID>` |
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

An authorized full preparation includes its normal Git and tracker publication
without approval at every internal step. “Continue” retains that scope; a local-save
child result is not the endpoint. Missing authority requires one concrete question,
not an invented local-only limit. Explicit project/user restrictions remain binding.
Git excludes unrelated outgoing commits; shared Dolt history requires the project's
accepted policy or explicit outgoing-scope authority. Content acceptance, action
authority and verified publication remain distinct facts. Init offers this policy
for agreement, never silently changes an existing project's restrictions.

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

Fast executes one small, understood, locally bounded and checkable request or idea,
selected explicitly or by a suitable natural request. Judge consequences/boundaries/
checks, not extension, diff size or an operation allowlist: code, config, docs, tools,
versioned/ignored project parts and explicitly selected external files can qualify.
Product-logic, architecture or material shared/public-contract changes, coordinated
independent outcomes, broad/unknown consequences or insufficient verification do not.
Resolve minor ambiguity here; agree only necessary expansion, never restart all SDLC
automatically or downgrade existing feature/bug/container obligations.
One main agent applies existing owners, **zero subagents by default**, without
mandatory interview/spec/design/decomposition/plan/handoff/report files.
Self-check and mandatory checks/TDD remain. Independent review is required only for
an explicit request, mandatory applicable target-project policy or concretely explained
material risk; code, external location and Git push alone are not triggers. General
RIS review wording does not cancel this narrow exception. Inactive review loads no
role/format and needs no skip report or fictional approval. Active review is actually
independent; high/medium findings require repair/checks and applicable reassessment.
Unavailable required review blocks dependent gates. A changed subject gets affected
self-check and renewed admission/risk assessment, plus independent reassessment when required.
For versioned edits, one own branch and dedicated worktree through the same preparer
as full/feature/bug are mandatory; reuse the copy across stages/sessions.
The ordinary source folder is never a development workspace or branch-return target.
All versioned writes, including documents,
`AGENTS.md` and `ris.yaml`, follow this rule. Installation/update keep their explicit
target without Git; agreed pre-Git bootstrap permits local writes, but subsequent
edits after a usable Git repository exists need a worktree and never automatically
transfer dirty files.
Busy/foreign/dirty copies remain protected; skipped/failed
local updating neither invalidates remote Git nor blocks close/Dolt, and never
calls for repeating a confirmed push. Ignored/external-only work changes its authorized
actual effective targets, without an empty worktree, inert config replica or dummy Git.
Mixed uses the own copy for versioned edits and actual local targets; shared resources
and Beads are not isolated by the worktree and need separate conflict/preservation checks.
A supplied ID keeps
its real contract; mandatory project accounting creates/reconciles a short task
(**Beads remains mandatory in RIS**). Empty input asks for work, never selects a
queue item. Git-only retains outgoing/integration/non-force/remote confirmation
and applicable review; local-only needs verified useful actual-target effects, no Git SHA,
with honest availability/portability limits. Mixed requires both parts; no-change checks
the required existing state without empty commit/push. Tracker result, exact close/read-back
and Dolt publication remain separate; Dolt does not publish local files.
Full task/bug execution likewise needs no saved plan or implementation report;
its safe-copy, TDD, ordinary YAML review and publication/completion gates remain.

Roadmap can produce one MVP epic with several preliminary features in one session,
or several epics. It reads freely structured product sources and agrees the concrete
graph before tracker writes; planning is not requirements/design acceptance. Load
`ris-proj-op-plan-epic-features` directly to plan an existing epic, or its portable
`ris-port-op-plan-epic-features` base with supplied inputs. Preliminary features need
no spec/design/AC/technical children and keep the same ID during preparation.
Implementation blocks, readable exact-ID requirements prerequisites and informational
links stay distinct: implementation dependencies alone do not bar requirements work.

`status` is read-only: without an ID it shows the project's complete unclosed plan;
with an ID it shows that subtree and necessary context/blockers. It recommends one
action using the continuation owner and checks the installed command, or reports an
exact gap. It saves nothing, claims no work and launches nothing. `next` inspects an
already selected subject; `run-task` executes. Existing-feature candidates are ranked
for the needed stage by own ongoing work, priority, creation time and ID, with parallel
candidates visible. Empty epics need graph planning; all-blocked means diagnose existing
prerequisites, not invent more features. Neither navigation command runs planning.

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
acceptance for material design when needed, verifies the exact used tracker-history
version and immutable Git sources/decisions, then uses the complete existing task
execution flow. A short ordinary basis locator enables discovery by project+ID;
no duplicate full snapshot or new file is required. Missing/incomplete history
blocks dependent execution; old snapshots remain untouched.
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
[ris.review/2](skills/ris-proj-op-review-task/references/report-format.md); Beads
keeps only its address/round. Fast review is conditional as above; when active it permits
sufficient independent session-only evidence, with
the same schema selection for optional saves. Existing /1 files continue under
conditional compatibility without migration. Compact rounds keep new findings
and dispositions instead of repeating prior findings or six coverage mappings.
The explicit verdict selects proceed/repair/stop; blocked or invalid/unsupported
evidence never means approval or an automatic repair loop. Format validity alone is not current-snapshot
approval; local reports are not automatically available on another machine.
Execution uses sufficient accepted inputs and current code, without standalone
task planners, `/risp-plan-task`, saved plans or implementation reports. There are
no aliases or replacement journals. The current [SDLC methodology](docs/product/08-sdlc-methodology.md)
and [development rules](docs/rules/development.md) state the direct norms; historical
[lifecycle decisions](docs/specs/sdlc-feature-lifecycle/acceptance.md) and
[ris-ppw decisions](docs/specs/ris-ppw/spec.md) retain their original scope/evidence.
Source availability does not establish independent approval, Git publication or
live behavior. Execution checks current-input sufficiency and a viable approach;
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
