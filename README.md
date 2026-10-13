# RIS — Ready-to-use Infrastructure Skills

RIS is a growing collection of source skills for AI agents working across the
software development lifecycle. The portable `ris-author-skills-base` creates
and improves autonomous Agent Skills source folders. `ris-author-skills`
composes that method with RIS integration for package and RIS-integrating
project skills. Neither installs the skills it creates. Two OKF skills operate
on Open Knowledge Format bundles.

## Available source skills

- `skills/ris-author-skills-base/` — author or revise an autonomous agent skill
  and check its source, selection, and behavior without RIS dependencies.
- `skills/ris-author-skills/` — own and check the combined result for a RIS
  package or RIS-integrating project skill, using the base method.
- `skills/ris-common/` — shared rules applied by RIS skills.
- `skills/ris-context/` — read-only preparation of project settings when an
  operation needs them; an optional `ris.yaml` can override package defaults.
- `skills/ris-okf-base/` — autonomously read, create, edit and check an explicit
  OKF bundle using the pinned official OKF 0.2 specification, without other
  RIS skills or project configuration.
- `skills/ris-okf/` — apply that method to an explicitly rooted bundle in a
  selected RIS project's authorized rules, product or other area, with project
  rules, path checks and configuration provenance.
- `skills/ris-plan-roadmap-base/` — prepare and check a bounded roadmap proposal
  from explicitly supplied inputs, marking unaccepted goals and gaps, without
  RIS project dependencies or tracker writes.
- `skills/ris-plan-epic/` — refine one unclear roadmap epic into bounded
  candidate feature outcomes and prerequisites; optionally verify an agreed
  update of the existing epic through the selected adapter.
- `skills/ris-interview-base/` — interview about interdependent decisions within
  a bounded topic, with a full or explicitly limited mode and a read-only handoff;
  runs without RIS or `grilling`.
- `skills/ris-formulate-architecture-rules-base/` — formulate portable normative
  architecture rules or a bounded amendment from explicit evidence; conditionally
  interview unresolved decisions, without acceptance or project writes.
- `skills/ris-author-architecture-rules/` — apply that method to a selected RIS
  project, obtain scoped acceptance and save/check architecture rules as OKF in
  `sources.rules`, preserving neighboring rules and the project's process.
- `skills/ris-formulate-development-rules-base/` — propose portable engineering
  rules and bounded amendments with justified, customizable tool/practice sets
  for Rails web and DragonRuby/Odin games, preserving existing tools and process.
- `skills/ris-author-development-rules/` — apply that engineering method to a
  selected RIS project, obtain scoped acceptance and save/check only its accepted
  engineering rules as OKF in `sources.rules`.
- `skills/ris-formulate-spec-base/` — formulate portable feature specification
  content from supplied decisions, preserving provenance and open questions;
  does not save or approve a project document.
- `skills/ris-decompose-spec-base/` — propose verifiable work units from a
  supplied requirements and sufficient design, tracing criteria, contracts,
  test seams and necessary
  dependencies without creating tracker records.
- `skills/ris-plan-task-base/` — prepare a portable technical plan for one
  selected task from requirements, inspected code and constraints; return
  approach, ordered steps and acceptance-check coverage without project writes.
- `skills/ris-plan-task/` — verify one tracker task and its accepted technical
  inputs and supplied current copy, then save its local plan without requiring
  a claim or preparing a worktree.
- `skills/ris-prepare-worktree-base/` — autonomously prepare or safely reuse a
  confirmed working copy, with a selected `worktrees/1` adapter and optional
  authorized environment setup; no RIS configuration or tracker is required.
- `skills/ris-prepare-task-worktree/` — apply that method to one exact RIS task
  with checked claim, project/shared roots and a self-contained copy/environment
  handoff; optional local witness writing needs separate permission.
- `skills/ris-git-worktree-adapter/` — bounded `worktrees/1` list/read/create
  operations through ordinary Git, verified against exact path/branch/commit.
- `skills/ris-worktrunk-adapter/` — the same bounded operations through explicitly
  selected Worktrunk, owning its configuration, JSON, hooks and tool side effects.
- `skills/ris-implement-base/` — implement a bounded change or repair review
  findings with meaningful tests, affected checks, optional TDD and exact-tree
  evidence, independently of RIS.
- `skills/ris-tdd-implement-task/` — own claim-aware project implementation and
  repairs with mandatory TDD, composing the portable method and authorized
  documentation updates.
- `skills/ris-review-base/` — assess a concrete change read-only against
  requirements, design, architecture and evidence; report located findings.
- `skills/ris-review/` — verify task inputs and save a versioned project review
  report; self-review does not provide independent publication approval.
- `skills/ris-update-documentation/` — synchronize affected authorized documents
  with inspected implementation and integration state; apply OKF only to actual
  selected bundles and preserve author-owned product material.
- `skills/ris-publish-main/` — integrate an approved task change into the established
  primary Git branch, reassess checks/review on the integrated tree, and verify
  authorized direct push; tracker completion and Dolt publication are separate.
- `skills/ris-verify-feature-base/` — assess complete integrated feature behavior
  read-only on one identified revision, with criterion, architecture, documentation
  and source-currency evidence; portable and independent of RIS or a tracker.
- `skills/ris-complete-container/` — verify one explicitly selected feature or epic,
  persist acceptance evidence through the selected adapter, then safely close only
  that container; Git integration is an input and tracker publication is separate.
- `skills/ris-decompose-feature/` — compute readiness from independently accepted
  current requirements/design and verify the project feature and its
  tracker task, then check the one-task case or persist and verify child tasks
  and dependencies through the selected adapter.
- `skills/ris-specify-feature/` — obtain acceptance for a selected feature's
  functional requirements with stable AC IDs, save independently scoped evidence
  and verify its permanent slug/feature task; design may still be absent.
- `skills/ris-design-feature-base/` — propose sufficient technical feature design
  or a focused revision from requirements, current code and architecture;
  portable and read-only, without approval or project writes.
- `skills/ris-design-feature/` — apply that method in a RIS project, coordinate
  relevant architecture/active-design impact, obtain independent design acceptance,
  save its scoped version and verify conditional feature-record updates.
- `skills/ris-beads-adapter/` — execute and verify authorized Beads issue operations
  with `bd` 1.3.1, including optional `tasks` v1 feature-task operations and
  conditional `tasks.feature-record/1` evidence operations; includes a
  separately authorized initialization procedure.
- `skills/ris-plan-roadmap/` — create or update a project's goal-level roadmap
  as verified epics through its selected adapter, or propose one without writing.
- `skills/ris-select-next-feature/` — recommend a small verifiable feature in a
  current epic from project evidence, without writing tracker or project state.
- `skills/ris-interview-feature/` — interview about a selected feature's
  requirements using project evidence and `ris-interview-base`; return a
  status-aware handoff without writing a specification or task.
- `skills/ris-prepare-feature-work/` — coordinate one project feature from a
  roadmap choice through separately accepted, reviewed and published requirements
  and design to a remotely verified feature ID. Noninteractive component operations
  run in subagents; human decisions stay in one leading dialogue. Decomposition
  starts separately from that published ID and inputs.

Each folder contains an Agent Skills `SKILL.md`. Install the folder **with its
resources** into a skill discovery location supported by your client before
using it. For OpenCode 1.18.33, one project-local location is
`.opencode/skills/<name>/`; `ris-author-skills` needs `ris-author-skills-base`
and `ris-common`, plus `ris-context` when its authoring operation requires
RIS project settings.
`ris-okf-base` has no required RIS dependencies. Project `ris-okf` needs
`ris-common`, `ris-context` and `ris-okf-base` installed with their resources.
The incompatible [OKF contract migration](docs/specs/okf-contract-migration/spec.md)
replaces the former public contracts as one coordinated installation: remove
`ris-project-okf`, install the new pair and update consumers together. No alias
preserves the former meaning of `ris-okf`.

Examples: “Read and check the OKF bundle rooted at `/allowed/knowledge/`
autonomously” selects `ris-okf-base`. “In this RIS project, edit/check the OKF
root `knowledge/policies/`, writing only `architecture/principles.md` and its
affected existing navigation” selects project `ris-okf`. Supply the project,
explicit root, operation and allowed scope; configured source directories do
not select or authorize a bundle. Ordinary feature Markdown uses its own
document workflow.
`ris-author-skills-base` has no required RIS dependencies. `ris-beads-adapter`
needs `ris-common` and, when project settings must be
resolved, `ris-context` installed with their resources.
`ris-plan-roadmap` needs `ris-common`, `ris-context`, `ris-plan-roadmap-base`
and an available selected adapter for tracker operations; it does not initialize
the project's tracker.
`ris-plan-epic` needs `ris-common`, `ris-context` and a selected compatible
task adapter for tracker reads and conditional epic updates; its interview-base
dependency applies only to interdependent unresolved decisions.
Installing a source folder does not install skills created by the author.
`ris-select-next-feature` needs `ris-common`, `ris-context` and a selected,
available task adapter for read operations.
`ris-interview-base` has no required RIS dependencies.
`ris-formulate-development-rules-base` has no required RIS dependencies; it
loads its engineering foundation, only applicable profiles, and
`ris-interview-base` only for interdependent unresolved decisions. It proposes
norms without accepting/saving them, configuring tools or auditing compliance.
`ris-author-development-rules` needs `ris-common`, `ris-context`,
`ris-formulate-development-rules-base` and project `ris-okf` with its dependencies.
It requires explicit acceptance before normative writes, preserves existing
tools/process and architecture, and blocks hidden storage-format migration.
Direct calls need no tracker or execution role. Document checks do not establish
tool setup, code compliance or remote publication.
`ris-formulate-architecture-rules-base` has no required RIS dependencies; it
loads `ris-interview-base` only for interdependent unresolved decisions and
loads only applicable Rails, DragonRuby or Odin profile resources.
`ris-author-architecture-rules` needs `ris-common`, `ris-context`,
`ris-formulate-architecture-rules-base` and project `ris-okf`, installed with
their resources. Direct invocation needs no tracker or execution role. It
requires explicit acceptance of the final content before normative writes,
checks only the agreed scope on update and blocks hidden format migration.
Document checks establish neither code compliance nor remote publication.
The two authors can contribute independently to one rules bundle, preserving
the neighboring subject and existing delivery process. Architecture owns what
must hold; engineering owns supporting versions, practices and tools. Neither
author configures tools or starts the other author. The portable bases return
proposals without acceptance or writes; the project authors require explicit
acceptance of the final content before saving.
`skills/ris-common/assets/rules-example/index.md` is the single **non-binding**
OKF 0.2 layout example, with architecture nested in the same bundle. Install
the complete `ris-common` folder to retain it. Authors consult only the useful
subject illustration when needed; bounded updates do not require it. Rails,
DragonRuby and Odin resources remain under each subject's portable base and
load only for the applicable stack. Project rules are assembled from facts
and accepted decisions, not installed as a template layer; they remain usable
after installed source materials change or disappear.
`ris-interview-feature` needs `ris-common`, `ris-context` and
`ris-interview-base` installed with their resources.
`ris-specify-feature` needs `ris-common`, `ris-context`,
`ris-formulate-spec-base`, the selected task adapter for tracker effects and, when substantive
answers are missing, `ris-interview-feature`; OKF-specific operations are
needed only for an OKF document. Its stable identity requires the adapter's
`tasks.feature-record/1` read/initial-create support and published document/decision
references. Ordinary creation uses best-effort all-state collision detection;
strict uniqueness needs a real guarantee only when explicitly required. An
explicit document-only result can precede an ID. A feature task with accepted
requirements and no design is not ready for decomposition or implementation.
`ris-design-feature-base` has no required RIS dependencies.
`ris-design-feature` needs `ris-common`, `ris-context`, `ris-design-feature-base`
and, for tracker effects, a selected adapter supporting `tasks.feature-record/1` read/update with
the required conditional-write guarantee; `ris-interview-base` is loaded only
for unresolved interdependent technical decisions. Direct invocation checks
the local document/record result and does not publish Git or Dolt.
`ris-decompose-feature` needs `ris-common`, `ris-context`,
`ris-decompose-spec-base` and a selected compatible task adapter with
`tasks.feature-record/1` read support. It starts from a confirmed ID and published
inputs without earlier chat/local notes. It checks both Git versions and
decisions, applicable contracts, source currency and blockers before child
writes; a feature task without accepted design remains blocked.
`ris-prepare-feature-work` needs `ris-common`, `ris-context`,
the available selection, interview, formulation and document-only save components,
and a selected adapter with feature-record create/read and separately verified
remote publication. `ris-plan-epic` applies only to an unclear epic boundary.
Configured `feature-selection` and `feature-preparation` executors must actually
launch; every standalone noninteractive operation, including independent review,
runs in a subagent. Git publication of both accepted results and separate decisions
precedes adapter creation; independent tracker publication completes the ID handoff.
Decomposition is a separate operation. Current feature-record refs use full
published Git commits, semantic sections and immutable decision addresses;
Git owns history. Historical digest payloads are diagnosed without automatic migration.
The task wrappers need `ris-common`, `ris-context` and their corresponding
portable method; task reads/claims require the selected adapter's actual
operations and guarantees. `ris-tdd-implement-task` also applies
`ris-update-documentation`, which needs `ris-okf` only for an actual selected
OKF bundle. `ris-publish-main` needs independent review evidence rather than
assuming a configured reviewer or launching a next operation. Portable
implementation and review have no required RIS dependencies. These components
are direct operations, not a universal task workflow engine.
The implementation base defaults to `standard` unless the caller, request or
project rules require `tdd`; tests and actual affected checks are required in both
modes. The TDD wrapper always requires `tdd`, including observed RED before a
behavior change and GREEN after. Its default local report is
`workspace.tasks/<ID>/implementation.md`; explicit/project-prescribed addresses
take priority and existing history is preserved. TDD details, complex publication
snapshot handling and task-specific/current-copy checks live in owned
`references/`, loaded only at their stated conditions. The public rename removes
`ris-implement-task` without an alias: update callers and install the complete new
folder with its resources, removing the old installed folder. The agreed change
is recorded in [TDD task implementation](docs/specs/tdd-task-implementation/spec.md).
`ris-prepare-task-worktree` needs `ris-common`, `ris-context`, the selected tasks
adapter's actual read/claim capabilities and `ris-prepare-worktree-base`. The base
loads only the selected `worktrees/1` adapter: an explicit choice wins, then an
unambiguous project rule, otherwise Git. Worktrunk's installed presence does not
select it; its reference version is wt 0.68.0, with other versions requiring
capability checks. Defaults are `task/<ID>` and `workspace.worktrees/<ID>` after
confirming the exact task and association. Shared tracker storage and task notes
stay in the explicitly supplied primary copy; worktrees do not isolate them.
Optional `workspace.tasks/<ID>/worktree.md` preserves history and needs write
permission. Copy and environment readiness are separate. Planning and implementation
consume the supplied copy without loading preparation skills or creating it;
implementation still checks/obtains its own authorized claim. The
[accepted design](docs/specs/task-worktree-preparation/design.md) explains the
four owners; this delivery adds no command or automatic lifecycle transition.
`ris-complete-container` needs `ris-common`, `ris-context` and a compatible selected
adapter with complete scope reads and safe result/closure operations. Its feature
branch applies `ris-verify-feature-base` and requires `tasks.feature-record/1`;
its epic branch uses the epic's own outcome and composition criteria. A claim is
not a concurrency guarantee, and closed children do not establish acceptance.
The portable verification method has no required RIS dependencies. Direct
completion does not integrate Git, create repair tasks or close ancestors.
This repository installs thirty-eight source skills in `.opencode/skills/` for its
own OpenCode project; installed copies must be kept in sync with `skills/`.
The root `ris.yaml` maps `feature-selection`, `feature-preparation` and `task-decomposition` to the
available OpenCode `general` subagent. A caller of these roles must still
verify that the agent actually launches and check its result; direct calls to
the component skills do not require an execution role.
The optional project command `.opencode/command/ris-author.md` exposes
`/ris-author <request>` in OpenCode; it selects the base for autonomous skills
and the RIS author for integrated ones. Direct requests use the corresponding
skill contract. The project command `.opencode/command/ris-next.md` exposes
`/ris-next [epic ID or context]` for read-only next-feature selection in the
current project using `ris-select-next-feature`. The project command
`.opencode/command/ris-interview-feature.md` exposes
`/ris-interview-feature [feature ID or description]` to discuss a selected
feature's requirements in the current project and return a read-only handoff;
without arguments it asks which feature to discuss. The project command
`.opencode/command/ris-prepare-feature-work.md` exposes
`/ris-prepare-feature-work [epic ID or context]` to prepare and publish one
feature from roadmap choice through accepted, reviewed and published requirements/
design to a remotely verified feature ID; decomposition starts separately. Without
arguments it establishes the epic scope with the user as needed. Restart
OpenCode after changing skill or command files so a running session picks them
up.

The [normative specification](docs/concepts/index.md) and its
[target SDLC methodology](docs/concepts/08-sdlc-methodology.md) describe RIS architecture
and future components; it is not a list of installed skills. A staged
[implementation specification](docs/specs/ris-foundation-and-skill-author.md)
records the agreed scope of the initial source skills.
This repository's [development rules](docs/rules/development.md) and root
[`ris.yaml`](ris.yaml) (configuration v2) identify its documents, Beads task adapter and workspace
directories. RIS development tasks and their status are tracked in Beads (Dolt);
Git push does not sync Beads, which requires separate Dolt publication. The
Git-ignored `tasks/` retains the completed PLAN-001–054 history; new local,
Git-ignored working notes live under `.sdlc/tasks/<confirmed Beads ID>/`.
Accepted specifications remain published in `docs/specs/`.
Roadmap, epic refinement and feature selection perform light responsibility/
shared-contract boundary checks and compare relevant product source versions
with decision baselines. Material changes yield linked AC/task/evidence impact
and coordination proposals; missing baselines leave currency unconfirmed, and
independent work remains available. Representative checks are recorded in
[`ris-capability-impact-checks.md`](docs/specs/ris-capability-impact-checks.md).
The v2 `sources.product` path is reserved for author-owned product material.
This repository's `docs/concepts/` and `docs/rules/` are separate OKF 0.2
bundles with root `index.md` files, as described in the
[knowledge profile](docs/concepts/knowledge-profile.md). The concepts bundle
contains RIS's normative methodology; the [rules bundle](docs/rules/index.md)
contains this repository's development rules and current architecture map.
`docs/concepts/` does not replace `docs/product/`. `docs/specs/` remains ordinary
Markdown, including existing flat specification paths. The former
`docs/concepts/README.md` address retains a transition to the overview and
index for historical links.

## License

MIT — see [LICENSE](LICENSE). The pinned third-party OKF specification in
`skills/ris-okf-base/references/spec-v02.md` is Apache-2.0; see its
[source attribution](skills/ris-okf-base/references/source.md).
