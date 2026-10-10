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
- `skills/ris-formulate-spec-base/` — formulate portable feature specification
  content from supplied decisions, preserving provenance and open questions;
  does not save or approve a project document.
- `skills/ris-decompose-spec-base/` — propose verifiable work units from a
  supplied feature specification, tracing requirement coverage and necessary
  dependencies without creating tracker records.
- `skills/ris-decompose-feature/` — verify an accepted project feature and its
  tracker task, then check the one-task case or persist and verify child tasks
  and dependencies through the selected adapter.
- `skills/ris-specify-feature/` — obtain acceptance for a selected feature's
  specification, save it by the project's rules and verify its feature task
  through the selected adapter.
- `skills/ris-beads-adapter/` — execute and verify authorized Beads issue operations
  with `bd` 1.3.1, including optional `tasks` v1 feature-task operations;
  includes a separately authorized initialization procedure.
- `skills/ris-plan-roadmap/` — create or update a project's goal-level roadmap
  as verified epics through its selected adapter, or propose one without writing.
- `skills/ris-select-next-feature/` — recommend a small verifiable feature in a
  current epic from project evidence, without writing tracker or project state.
- `skills/ris-interview-feature/` — interview about a selected feature's
  requirements using project evidence and `ris-interview-base`; return a
  status-aware handoff without writing a specification or task.

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
`ris-interview-feature` needs `ris-common`, `ris-context` and
`ris-interview-base` installed with their resources.
`ris-specify-feature` needs `ris-common`, `ris-context`,
`ris-formulate-spec-base`, the selected task adapter and, when substantive
answers are missing, `ris-interview-feature`; OKF-specific operations are
needed only for an OKF document.
`ris-decompose-feature` needs `ris-common`, `ris-context`,
`ris-decompose-spec-base` and a selected compatible task adapter.
This repository installs seventeen source skills in `.opencode/skills/` for its
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
without arguments it asks which feature to discuss. Restart OpenCode after
changing skill or command files so a running session picks them up.

The [normative specification](docs/concepts/README.md) describes RIS architecture
and future components; it is not a list of installed skills. A staged
[implementation specification](docs/specs/ris-foundation-and-skill-author.md)
records the agreed scope of the initial source skills.
This repository's [development rules](docs/rules/development.md) and root
[`ris.yaml`](ris.yaml) identify its document and future SDLC workspace directories.
The development queue remains in Git-ignored `tasks/`; it is separate from
the configured `.sdlc/tasks/` for future tracker task artifacts.

## License

MIT — see [LICENSE](LICENSE). The pinned third-party OKF specification in
`skills/ris-okf/references/spec-v02.md` is Apache-2.0; see its
[source attribution](skills/ris-okf/references/source.md).
