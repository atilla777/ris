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
- `skills/ris-okf/` — read, create, edit and check a selected OKF bundle using
  a pinned local copy of the official OKF 0.2 specification; direct use does
  not require RIS project configuration.
- `skills/ris-project-okf/` — resolve a RIS project's configured specifications
  directory and operate on an explicitly rooted OKF specification via `ris-okf`.
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
  inputs, save its local plan, and optionally prepare an authorized worktree
  after confirming claim ownership.
- `skills/ris-implement-base/` — implement a bounded change or repair review
  findings with tests and exact-tree evidence, independently of RIS.
- `skills/ris-implement-task/` — own claim-aware project implementation and
  repairs, composing the portable method and authorized documentation updates.
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
  verified roadmap choice through independently accepted, published requirements
  and design to remotely verified tracker tasks in a single dialogue, using two real
  subagent roles. Direct component calls retain their narrower results.

Each folder contains an Agent Skills `SKILL.md`. Install the folder **with its
resources** into a skill discovery location supported by your client before
using it. For OpenCode 1.18.33, one project-local location is
`.opencode/skills/<name>/`; `ris-author-skills` needs `ris-author-skills-base`
and `ris-common`, plus `ris-context` when its authoring operation requires
RIS project settings.
`ris-okf` needs `ris-common`; `ris-project-okf` needs `ris-common`,
`ris-context` and `ris-okf` installed with their resources.
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
`ris-formulate-architecture-rules-base` has no required RIS dependencies; it
loads `ris-interview-base` only for interdependent unresolved decisions and
loads only applicable Rails, DragonRuby or Odin profile resources.
`ris-author-architecture-rules` needs `ris-common`, `ris-context`,
`ris-formulate-architecture-rules-base` and direct `ris-okf`, installed with
their resources. Direct invocation needs no tracker or execution role. It
requires explicit acceptance of the final content before normative writes,
checks only the agreed scope on update and blocks hidden format migration.
Document checks establish neither code compliance nor remote publication.
`ris-interview-feature` needs `ris-common`, `ris-context` and
`ris-interview-base` installed with their resources.
`ris-specify-feature` needs `ris-common`, `ris-context`,
`ris-formulate-spec-base`, the selected task adapter and, when substantive
answers are missing, `ris-interview-feature`; OKF-specific operations are
needed only for an OKF document. Its stable identity requires the adapter's
`tasks.feature-record/1` read/initial-create support and an independently
confirmed exclusive window over project feature creators; unavailable guarantees
block the combined write. A feature task with accepted requirements and no
design is not ready for decomposition or implementation.
`ris-design-feature-base` has no required RIS dependencies.
`ris-design-feature` needs `ris-common`, `ris-context`, `ris-design-feature-base`
and a selected adapter supporting `tasks.feature-record/1` read/update with
the required conditional-write guarantee; `ris-interview-base` is loaded only
for unresolved interdependent technical decisions. Direct invocation checks
the local document/record result and does not publish Git or Dolt.
`ris-decompose-feature` needs `ris-common`, `ris-context`,
`ris-decompose-spec-base` and a selected compatible task adapter with
`tasks.feature-record/1` read support. It checks both scoped versions and
decisions, applicable contracts, source currency and blockers before child
writes; a feature task without accepted design remains blocked.
`ris-prepare-feature-work` needs `ris-common`, `ris-context`,
`ris-select-next-feature`, `ris-specify-feature`, `ris-design-feature`,
`ris-decompose-feature`, a selected compatible task adapter with conditional
feature-record update support and separately verified remote publication,
and `ris-plan-epic` only if the epic's boundary needs refinement; its two
subagent roles must actually launch. A successful full scenario also requires
authorized publication of both accepted scopes and their decision evidence in
the project's Git remote, independently checked against the remote feature record.
The task wrappers need `ris-common`, `ris-context` and their corresponding
portable method; task reads/claims require the selected adapter's actual
operations and guarantees. `ris-implement-task` also applies
`ris-update-documentation`, which needs `ris-okf` only for an actual selected
OKF bundle. `ris-publish-main` needs independent review evidence rather than
assuming a configured reviewer or launching a next operation. Portable
implementation and review have no required RIS dependencies. These components
are direct operations, not a universal task workflow engine.
This repository installs thirty source skills in `.opencode/skills/` for its
own OpenCode project; installed copies must be kept in sync with `skills/`.
The root `ris.yaml` maps `feature-selection` and `task-decomposition` to the
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
feature from roadmap choice through an accepted specification to remotely
verified tasks; without
arguments it establishes the epic scope with the user as needed. Restart
OpenCode after changing skill or command files so a running session picks them
up.

The [normative specification](docs/concepts/README.md) and its
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
The v2 `sources.product` path is reserved for author-owned product material;
this repository's existing `docs/concepts/` is RIS normative documentation,
not a substitute for `docs/product/`. Its own OKF migration is a separate task.

## License

MIT — see [LICENSE](LICENSE). The pinned third-party OKF specification in
`skills/ris-okf/references/spec-v02.md` is Apache-2.0; see its
[source attribution](skills/ris-okf/references/source.md).
