# RIS — Ready-to-use Infrastructure Skills

RIS supplies reusable Agent Skills for software development. Each skill owns a
bounded result; the two explicit workflows coordinate existing operations.
Source folders include every owned reference, asset and script needed after
installation. A source folder is not automatically installed in a client.

## Names and available source skills

Package identifiers use
`ris-<port|proj>-<op|flow|lib|adapter>-<verb-object|purpose>`.
`port` accepts direct inputs without requiring RIS project configuration,
document structure or tracker. `proj` supplies necessary RIS integration;
it does not make every configuration field or execution role mandatory.
`op` owns one useful result; `flow` coordinates independently useful operations;
`lib` contains shared instructions; `adapter` implements bounded tool operations.
Names are lowercase ASCII words separated by single hyphens, at most 64 characters.
Source directory, frontmatter `name`, installed directory, command basename and
slash command agree. Every op/flow has one same-name command; lib/adapter have none.

The following 41 folders are the current package source inventory. This branch
prepares their coordinated namespace migration; publication and primary installation
are separate gates. The linked SKILL.md files define actual inputs, dependencies,
permissions, checks and stopping points.

| Skill (source) | Result | Command |
| --- | --- | --- |
| [ris-port-op-author-skill](skills/ris-port-op-author-skill/SKILL.md) | Autonomous skill source authoring | same name |
| [ris-port-op-interview](skills/ris-port-op-interview/SKILL.md) | Bounded decision-tree interview | same name |
| [ris-port-op-formulate-feature-spec](skills/ris-port-op-formulate-feature-spec/SKILL.md) | Portable feature requirements proposal | same name |
| [ris-port-op-design-feature](skills/ris-port-op-design-feature/SKILL.md) | Portable technical design proposal | same name |
| [ris-port-op-decompose-feature-spec](skills/ris-port-op-decompose-feature-spec/SKILL.md) | Verifiable work-unit proposal | same name |
| [ris-port-op-plan-roadmap](skills/ris-port-op-plan-roadmap/SKILL.md) | Goal-level roadmap proposal | same name |
| [ris-port-op-plan-task](skills/ris-port-op-plan-task/SKILL.md) | Technical task plan | same name |
| [ris-port-op-prepare-worktree](skills/ris-port-op-prepare-worktree/SKILL.md) | Checked copy/environment handoff | same name |
| [ris-port-op-implement-change](skills/ris-port-op-implement-change/SKILL.md) | Bounded implementation or finding repair | same name |
| [ris-port-op-review-change](skills/ris-port-op-review-change/SKILL.md) | Read-only change assessment | same name |
| [ris-port-op-retrospect-session](skills/ris-port-op-retrospect-session/SKILL.md) | Retrospective from supplied history | same name |
| [ris-port-op-verify-feature](skills/ris-port-op-verify-feature/SKILL.md) | Integrated all-criterion feature verification | same name |
| [ris-port-op-formulate-architecture-rules](skills/ris-port-op-formulate-architecture-rules/SKILL.md) | Portable architecture-rules proposal | same name |
| [ris-port-op-formulate-development-rules](skills/ris-port-op-formulate-development-rules/SKILL.md) | Portable engineering-rules proposal | same name |
| [ris-port-op-manage-okf-bundle](skills/ris-port-op-manage-okf-bundle/SKILL.md) | Explicit-root autonomous OKF read/create/edit/check | same name |
| [ris-proj-op-author-skill](skills/ris-proj-op-author-skill/SKILL.md) | Combined RIS skill authoring | same name |
| [ris-proj-op-resolve-context](skills/ris-proj-op-resolve-context/SKILL.md) | Read-only project configuration/path preparation | same name |
| [ris-proj-op-plan-roadmap](skills/ris-proj-op-plan-roadmap/SKILL.md) | Project roadmap and authorized tracker persistence | same name |
| [ris-proj-op-refine-epic](skills/ris-proj-op-refine-epic/SKILL.md) | One unclear epic's outcome/boundaries | same name |
| [ris-proj-op-select-feature](skills/ris-proj-op-select-feature/SKILL.md) | Read-only next-feature recommendation | same name |
| [ris-proj-op-interview-feature](skills/ris-proj-op-interview-feature/SKILL.md) | Project feature-requirements interview handoff | same name |
| [ris-proj-op-specify-feature](skills/ris-proj-op-specify-feature/SKILL.md) | Accepted saved requirements and conditional feature task | same name |
| [ris-proj-op-design-feature](skills/ris-proj-op-design-feature/SKILL.md) | Independently accepted saved design and conditional record update | same name |
| [ris-proj-op-decompose-feature](skills/ris-proj-op-decompose-feature/SKILL.md) | Ready accepted inputs and necessary tasks/dependencies | same name |
| [ris-proj-op-prepare-task-worktree](skills/ris-proj-op-prepare-task-worktree/SKILL.md) | Claim-aware task copy/environment handoff | same name |
| [ris-proj-op-plan-task](skills/ris-proj-op-plan-task/SKILL.md) | Verified saved task plan | same name |
| [ris-proj-op-implement-task-tdd](skills/ris-proj-op-implement-task-tdd/SKILL.md) | Claim-aware implementation with mandatory TDD | same name |
| [ris-proj-op-review-task](skills/ris-proj-op-review-task/SKILL.md) | Checked project review, saved when authorized | same name |
| [ris-proj-op-update-documentation](skills/ris-proj-op-update-documentation/SKILL.md) | Authorized documentation synchronization | same name |
| [ris-proj-op-publish-task](skills/ris-proj-op-publish-task/SKILL.md) | Reviewed primary-branch integration and verified Git push | same name |
| [ris-proj-op-complete-container](skills/ris-proj-op-complete-container/SKILL.md) | Explicit verified feature/epic closure | same name |
| [ris-proj-op-retrospect-session](skills/ris-proj-op-retrospect-session/SKILL.md) | Selected OpenCode history plus project evidence | same name |
| [ris-proj-op-manage-okf-bundle](skills/ris-proj-op-manage-okf-bundle/SKILL.md) | Explicit project/root/scope OKF operation | same name |
| [ris-proj-op-author-architecture-rules](skills/ris-proj-op-author-architecture-rules/SKILL.md) | Accepted scoped architecture rules in project OKF | same name |
| [ris-proj-op-author-development-rules](skills/ris-proj-op-author-development-rules/SKILL.md) | Accepted scoped engineering rules in project OKF | same name |
| [ris-proj-flow-prepare-feature](skills/ris-proj-flow-prepare-feature/SKILL.md) | Feature choice through accepted published inputs to verified ID | same name |
| [ris-proj-flow-execute-task](skills/ris-proj-flow-execute-task/SKILL.md) | One task's fresh run or safe resume through separate publications | same name |
| [ris-proj-lib-common](skills/ris-proj-lib-common/SKILL.md) | Shared conditional dialogue/artifact/quality rules | none |
| [ris-proj-adapter-beads-tasks](skills/ris-proj-adapter-beads-tasks/SKILL.md) | Bounded Beads tasks and separately authorized Dolt operations | none |
| [ris-port-adapter-git-worktrees](skills/ris-port-adapter-git-worktrees/SKILL.md) | Git worktrees/1 operations | none |
| [ris-port-adapter-worktrunk-worktrees](skills/ris-port-adapter-worktrunk-worktrees/SKILL.md) | Explicitly selected Worktrunk worktrees/1 operations | none |

## Commands and installation

[`commands/opencode/`](commands/opencode/) is the canonical source of all
37 thin command templates (35 op and 2 flow). The inventory above is also the
complete command inventory: each `same name` row exposes `/` followed by its
full skill name. A template explicitly loads that one skill, passes `$ARGUMENTS`
and follows its existing input, permission and stop contract. It does not select
port/proj implicitly or require a subagent for a direct operation.

For example, `/ris-port-op-interview <topic>` uses the autonomous interview.
Without a topic it asks what to discuss; full mode is the default and limited
mode needs an explicit request and sufficiency criterion.
`/ris-proj-op-interview-feature` asks which feature to discuss when none is given.
`/ris-proj-flow-prepare-feature` establishes epic scope as needed and ends at the
published feature ID; decomposition is separate.
`/ris-proj-flow-execute-task [ID or context]` preserves an explicit target; with
no ID it reconciles confirmed own unfinished work before ready-task selection.
Its existing recovery route preserves applicable effects and closed status.
`/ris-proj-op-retrospect-session` follows the permitted list-and-selection
procedure without an ID/export and returns a response by default; saving needs
an explicit exact authorized destination.

Install complete skill folders with their resources into a client-supported
discovery location. For OpenCode 1.18.33 this repository uses
`.opencode/skills/<name>/` and `.opencode/command/<name>.md`. For manual installation
of the autonomous interview in another project, copy
`commands/opencode/ris-port-op-interview.md` to that project's
`.opencode/command/ris-port-op-interview.md`, and the complete
`skills/ris-port-op-interview/` folder to `.opencode/skills/ris-port-op-interview/`.
It needs no RIS configuration or other RIS skill. Quit and restart OpenCode after
installation so it discovers the changed files; a running session is not updated.

For existing installations use the **[complete namespace transition guide](docs/skill-command-naming-migration.md)**,
including all 41 skill replacements, all eight retired commands, independent
target-root selection, consumer/config updates, removal and partial-error handling.
There are no aliases. An automated installer remains a separate future delivery.
The local foreign skill `grilling`, command `grillme`, and client configuration
are not RIS package source and must be preserved during synchronization.

## Dependencies and boundaries

Portable operations take direct inputs and apply actual target-project rules;
RIS configuration is not a new prerequisite. Project operations load shared
rules and prepare context only when their actual operation requires it. Consult
each SKILL.md for required dependencies and conditional owner-relative resources.
The RIS author composes the portable author and owns the combined result;
neither author installs its output without separate authorization.

The two OKF operations retain read/create/edit/check on an **explicit bundle**.
The autonomous operation owns the pinned format resource; the project operation
adds common/context, path authorization and project-result verification. Ordinary
feature Markdown is not processed as OKF automatically. Architecture and engineering
authors independently own accepted subject content in one rules bundle; their
portable bases return proposals and load only applicable profiles/interview branches.
The shared non-binding rules example remains inside the common library's assets.

Portable implementation defaults to standard unless TDD is required; the project
TDD operation always requires observed RED before behavior changes and GREEN after.
Text-only work uses its substantive checks. Review evidence must apply to the full
actual snapshot; self-review is not independent publication approval. Git publication,
exact-task completion, parent-container acceptance and Dolt publication/read-back
remain distinct effects. A claim or worktree does not provide general CAS.

Worktree preparation retains explicit primary/shared roots and separate copy and
environment readiness. Git is the default selected worktrees adapter; installed
Worktrunk presence does not select it (reference version 0.68.0). Planning consumes
the supplied copy without creating it or requiring a claim. Feature decomposition
starts from accepted current published requirements/design and a confirmed ID;
document-only requirements/design can precede a tracker ID. Execution-role names
and configuration v2 are unchanged by naming.

The retrospective source retains its exact-identity OpenCode reader and conditional
Langfuse/delegation/save branches. Existing T3 observations are partial, final
independent reassessment/publication and combined acceptance remain outstanding;
this rename does not supply runtime safety, live telemetry identity or new behavioral
evidence. Likewise task-execution T1/T2 evidence stays bound to its original inputs
and snapshots. See the preserved [retrospective design](docs/specs/session-retrospective/design.md),
[CLI policy amendment](docs/specs/session-retrospective/cli-read-policy.md) and
[task-execution delivery checks](docs/specs/task-execution/delivery-checks.md).

## Project knowledge and development

The [normative concepts bundle](docs/concepts/index.md) and
[target SDLC methodology](docs/concepts/08-sdlc-methodology.md) describe architecture
and future components; they are not an installed inventory. The
[rules bundle](docs/rules/index.md) contains this repository's development rules
and current owner map. Both are separate OKF 0.2 bundles under the
[knowledge profile](docs/concepts/knowledge-profile.md). `docs/concepts/` does not
replace author-owned `docs/product/`. [Delivery specifications](docs/specs/README.md)
are ordinary Markdown; accepted historical names and immutable decision references
remain unchanged and are interpreted through the transition guide.

Read [AGENTS.md](AGENTS.md), the complete [development rules](docs/rules/development.md)
and root [`ris.yaml`](ris.yaml). Development state/dependencies belong to Beads
(Dolt); Git push does not synchronize them. Shared new task notes live in primary
`.sdlc/tasks/<confirmed-ID>/`; ignored `tasks/PLAN-*` remains historical archive.
The config maps feature-selection, feature-preparation, task-decomposition,
task-execution, task-implementation and task-review to `general`. A caller must
still verify actual launch where required. Roadmap, epic refinement and feature
selection retain bounded source-currency and shared-contract impact checks;
[earlier evidence](docs/specs/ris-capability-impact-checks.md) is not repinned by this migration.

## License

MIT — see [LICENSE](LICENSE). The pinned third-party OKF specification in
`skills/ris-port-op-manage-okf-bundle/references/spec-v02.md` is Apache-2.0;
see its [source attribution](skills/ris-port-op-manage-okf-bundle/references/source.md).
