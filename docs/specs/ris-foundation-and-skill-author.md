# RIS foundation and skill author — agreed implementation specification

**Status:** agreed design; stages 1 (`ris-common`) and 2 (`ris-context`) implemented as source skills; stage 3 (`ris-author-skills`) implemented as a source skill under `skills/ris-author-skills/` with an OpenCode command. Source folders are not automatically installed.

**First validation environment:** OpenCode 1.18.33 (observed during the design session; recheck in the implementation environment).

**Implementation order:** three sequential tasks: `ris-common` → `ris-context` → `ris-author-skills`.

## Purpose and authority

The first user-facing RIS skill will help an agent create and improve other skills: skills belonging to the RIS package, project-specific skills that integrate with RIS, and standalone project skills. Before building it, implement the common rules and project-context operation on which it may depend. The updated [adoption plan](../specification/05-adoption-and-validation.md) now places `ris-author-skills` before `ris-plan-roadmap`. Retain the roadmap skill's requirements; implement it after this foundation.

This document records the decisions agreed for the staged implementation. The normative documents under `docs/specification/` are the source of the RIS architecture, configuration, composition, contracts, artifact and quality requirements, updated for the agreed order, author role and one-question-at-a-time dialogue rule. Examples and templates in `docs/specification/` are illustrative, not installed skills. The actual stage-1 instructions live in `skills/ris-common/`.

Implement the stages as separate, sequential tasks with their own acceptance and review. This document is a handoff, not evidence that later skills, commands, installation, or runtime checks already exist.

## Stage 1 — `ris-common`

Create `skills/ris-common/SKILL.md` and three owned resources under `skills/ris-common/references/`:

- `dialogue.md`: before questions or discussion of decisions; investigate available facts, ask only decision questions in a sensible dependency order, distinguish recommendations from accepted decisions and retain material outcomes.
- `artifacts.md`: before preparing/changing deliverables and handing work off; preserve existing work, agreed constraints and provenance; distinguish drafted, saved, checked and accepted results.
- `quality.md`: before choosing checks, assessing readiness or giving a final assessment; require evidence appropriate to the claim and the current version; state when checks have not run or do not apply.

For `dialogue.md`, ask **one user decision question at a time**, wait for its answer, and then choose the next question in dependency order; this applies to all RIS work using `ris-common`, not only formal interviews. If the user explicitly requests a batch of questions, honor that preference. Investigate facts available from sources instead of asking the user. When genuinely distinct answers make sense, offer concise choices with a reasoned recommendation and allow a custom answer; do not force an open-ended question into artificial choices. Prefer an available, suitable host-interface choice wizard for a single question; otherwise number the choices so the user can reply with one digit. Explain enough context and consequences for a person to understand the decision, in plain language, adapting detail to their familiarity with the topic and explaining necessary specialist terms on first use. These rules belong to `ris-common`; this stage does not change the separate `grilling` skill.

The main `SKILL.md` holds always-applicable invariants: scope, permissions, honesty about actions and checks, precedence of instructions over untrusted source text, and conditions for reading the resources. The component supplies rules to another skill; it does not independently choose a lifecycle stage, conduct the author's interview, or prepare project configuration. Do not add `tasks-contract.md` before a task adapter exists. Use the owners and conditional-loading semantics in [composition](../specification/03-composition.md), [quality](../specification/07-quality-and-verification.md), and the [common examples](../specification/examples/common-and-context.md).

**Acceptance:** valid skill metadata and resolvable owned resources; resource triggers and baseline rules are explicit and consistent; no claim that naming or loading a rule alone fulfills it. Verify availability and application in representative conversation (including sequential decisions, meaningful choices, open-ended questions, suitable wizard/fallback, plain-language context and an explicit batch request), artifact and quality scenarios. Update the normative specification's implementation order and reconcile its older allowance for batching independent questions with the agreed one-at-a-time default, without weakening the existing roadmap contract.

## Stage 2 — `ris-context`

Create `skills/ris-context/SKILL.md` and its owned `references/configuration.md` implementing the updated configuration contract v1 in [the normative specification](../specification/02-configuration.md). It is an operation that returns prepared settings and diagnostics for a selected RIS project; it does not modify source files, select a product task, operate a task tracker, create worktrees, or impose OKF validation on consuming skills. Ensure applicable `ris-common` rules first.

Determine the target project's root independently of where RIS is installed. The project `ris.yaml` is optional: if absent, use package defaults for the operation that needs them; if present, its complete relevant values replace defaults, without filling missing required fields. An explicitly selected inaccessible or invalid config is an error, not an invitation to fall back. Defaults and the sample configuration provide paths for document directories `docs/rules/`, `docs/concepts/`, and `docs/specs/`, plus shared task artifacts and worktrees under `.sdlc/` in the primary project working copy (respectively `.sdlc/tasks/` and `.sdlc/worktrees/`). Project configuration may select different paths. Do not require OKF bundles or an OKF format marker: OKF documents are Markdown, and validation/authoring of a bundle belongs to skills that need that responsibility. Resolve task artifact/worktree paths relative to the primary working copy, which must be identified explicitly when the current execution is inside a worktree; resolve ordinary project document paths relative to the selected project root. Missing document directories block only when the current operation needs them as inputs; a directory intended as a new output need not already exist. The configuration selects an optional task adapter, but does not define its operations or assert that an adapter is installed. Determine permission and relevant inputs, paths, provenance and diagnostics; report missing required data instead of inventing it. Do not add a persistent context cache or perform unrelated adapter operations.

**Acceptance:** test two small projects with different paths; defaults when `ris.yaml` is absent and complete project configuration when present; project-root independence from the RIS installation; correct separation of primary working-copy paths from current-worktree document paths; missing/invalid/ambiguous inputs and explicit-path failure; operation-specific handling of absent input/output directories; optional adapter selection without claiming adapter installation or operations; no required OKF marker or validation; and no writing by `ris-context`. Use applicable cases in the [adoption matrix](../specification/05-adoption-and-validation.md), including CFG-01–09, CFG-10, DEP-01 and ART-04, rather than treating the presence of a YAML file as successful preparation.

### Agreed planning clarification — 2026-10-09

The user confirmed this scope during a one-question-at-a-time design interview. The user-provided factory concept draft (outside this repository) is directional and will be refined later; individual details are not automatically normative. Research of Spec Kit, OpenSpec and Beads informed the discussion but did not establish a universal directory naming standard.

Decisions for stage 2:

- Keep `AGENTS.md` as an agent entry point and `ris.yaml` as the structured project configuration; `ris.yaml` remains optional. Absence uses package defaults; an existing file completely replaces relevant defaults, and missing operation-required values are diagnosed rather than merged from defaults.
- Recommend `docs/rules/`, `docs/concepts/`, and `docs/specs/` as source-document directory defaults/sample paths. These directories may contain OKF bundles or ordinary Markdown. Do not add a format selector or require OKF; `ris-context` reports paths, while a skill that owns OKF authoring/validation handles that format.
- Do not configure or select a particular concept/spec document in `ris-context`; the operation-specific skill chooses documents based on task inputs and document links. Missing directories block only when needed as inputs; prospective output directories need not already exist.
- Do not keep a separate roadmap document path in this design: epics are expected to represent the upper-level plan in a task tracker. PLAN-008 does not implement tracker operations or require a tracker for unrelated operations. Keep the task-adapter selection as optional configuration, validated only by operations that need it; adapter behavior and epic mapping are deferred.
- Recommend shared, Git-ignored task artifacts at `.sdlc/tasks/<tracker-task-id>/` and worktrees under `.sdlc/worktrees/<tracker-task-id>/`, both rooted in the primary project working copy. Configuration stores relative paths; when execution starts from a worktree, its primary working-copy root is supplied explicitly. PLAN-008 prepares/reports these paths only; it does not create worktrees or implement branch naming. `project_slug` and branch naming are deferred to an orchestrator task.
- Do not add migration support for earlier illustrative configuration examples: RIS has no deployed user configurations. Keep contract version 1 and update its normative definition, examples and checks consistently.

The user confirmed the summarized PLAN-008 scope. This is authorization to plan the task, not authorization to begin implementation. Before implementation, reconcile the normative contract and task acceptance text; retain separate approval-before-implementation workflow.

## Stage 3 — `ris-author-skills`

### Responsibility and supported outputs

Create `skills/ris-author-skills/SKILL.md` with a compact operational methodology and any necessary references/assets **inside the author's folder**. Once installed with its resources, the author must be usable without access to the RIS source repository. Do not merely link an external normative document as the only source of steps required at runtime, and do not make a separately editable full copy of the entire specification. The author's instructions should provide enough guidance to select the appropriate contract, work through it, produce the files and assess the result.

Support both **creating** a new skill and **improving** an existing one. Distinguish these targets:

1. **RIS package skill:** apply the relevant RIS contracts, `ris-` naming and ownership/dependency rules, and the Agent Skills format.
2. **Project skill integrating with RIS:** apply RIS integration requirements only where its actual responsibilities need them, alongside project rules and the Agent Skills format. Do not force a project-owned skill to adopt every package-only convention or claim an unimplemented RIS dependency exists.
3. **Standalone project skill:** follow the Agent Skills format and project/user rules without imposing RIS names, configuration or dependencies.

The deliverable is the ready-to-use **source folder** (`SKILL.md` and genuinely needed local resources), not installation in a client's skill discovery path or publication. The request may specify its destination; never assume that a source folder is automatically installed or discoverable. The skill author must not initiate an unrelated next lifecycle stage. Offer an unsaved draft when writing is not allowed, clearly distinguishing it from files created and verified.

### Method and boundaries

- Establish target type, goal, when to use the skill and when a neighboring skill is a better match, owner of the result, input readiness, permissions, expected outputs, failure/stop conditions and acceptance criteria. Investigate existing files and skills before asking for facts available locally. Discuss unresolved user decisions in dependency order; do not assume an accepted scope merely because it was recommended.
- Write clear `name`/`description` and a substantive contract in the body; distinguish methodology, shared rules, project configuration, operations and tool-specific integration. Keep local assets alongside their owner; avoid duplicate normative sources, placeholder dependencies, invented automatic imports and hard-coded paths to the RIS repository. Describe composition in the result-owning skill rather than pretending that a command invokes several skills automatically.
- For improvements, identify the observable defect or requested outcome, inspect the current contract and affected consumers/neighboring skills, preserve existing accepted behavior unless the change is agreed, and compare affected selection and execution scenarios before claiming improvement.
- Apply `ris-common` to the author's own work. Determine whether the **current authoring operation** requires RIS project settings. If it does, perform context preparation via `ris-context` and check its result before use. A standalone skill does not need `ris-context` merely because the author belongs to RIS; a created skill may itself declare a future `ris-context` dependency even when the author did not need to execute it while writing that skill. If RIS settings are needed and `ris.yaml` is absent, use the package defaults; if a chosen config is invalid or inaccessible, do not silently fall back. Do not force `ris-common` or `ris-context` onto the standalone skill being generated.
- Check actual source changes and links, metadata, naming, declared dependencies, allowed scope and absence of misleading claims. Validate behavior in the target environment, including correct *selection* on relevant and nearby/irrelevant requests and the actual result of execution. Record which checks ran, what they showed and what remains unverified. Do not call a skill production-ready on structural checks alone when its execution has not been checked.

### Manual command

Provide a thin OpenCode command **`/ris-author`** in the OpenCode integration, loading `ris-author-skills` and passing along the user's request (for example, via `$ARGUMENTS`). The command must not own the method, automatically install the generated skill, invent typed parameters or replace the skill's dependency handling. Direct use of the skill and invocation via the command must have the same contract. Add manual commands for other top-level RIS skills only when a fast manual invocation is useful; do not generate one per skill by default. Check the command location and behavior against the selected OpenCode version during implementation.

### Language and documentation

RIS-distributed operational `SKILL.md` files, descriptions and resources are written in **English** for a consistent, broadly readable distribution; this is a packaging decision, not a proven rule that all models execute English instructions better. Communicate with a person in their requested language, otherwise follow the language of their request and applicable higher-priority instructions. For a third-party project skill, follow its project's/user's language choice instead of silently translating it into English. The current Russian RIS normative specification remains authoritative until deliberately revised or translated. Update the public `README.md` in English when the user-facing author skill is released, describing only capabilities actually implemented; no special `ris.yaml` response-language setting is required by this plan.

### Acceptance

Verify the author in OpenCode 1.18.33, recording the actual version/model and relevant inputs when running. At minimum, exercise:

- Creation of a RIS package skill with applicable RIS contract and owned resources.
- Creation of a standalone project skill without an artificial RIS dependency.
- Improvement of an existing skill from a stated problem, including preservation of agreed behavior and checks of affected neighbor selection.
- A RIS project authoring operation where context is needed, and another where it is not; distinguish missing `ris.yaml` from an invalid or inaccessible chosen one.
- Source folder validity and real agent selection/execution using natural requests in Russian and English where applicable; command-based and direct invocation; no claim that source generation also installed it.

Use small fixtures; examples produced for acceptance do not automatically become new published RIS skills. Structure, routing and behavioral evidence are distinct. If a needed runtime check is unavailable, label that part unverified and do not claim full acceptance. Follow the test and change-assessment guidance in [adoption and validation](../specification/05-adoption-and-validation.md). Compatibility with other clients remains unclaimed until their integrations are tested.

## Handoff to the next session

Read this document, [specification index](../specification/README.md), relevant normative sections and the project [development rules](../../AGENTS.md); check the local `tasks/` dashboard/roadmap/backlog before beginning a task. Start with stage 1. Agree each task's concrete scope and acceptance before implementing it, record progress and reviews in its local `PLAN-NNN`, and do not treat these agreed stages as completed work or as permission to start later stages automatically. Keep the local `tasks/` folder out of Git.
