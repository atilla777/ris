# Operation index and short cards

Read the index to locate a name, then only the relevant card(s). Each heading is
an exact technical owner; links refer to installed sibling skills, not a source
repository. Each card has purpose, choose-when, inputs, result/stop and example.
Examples are prompts, not automatic calls or proof of command discovery. `Load`
means ask the agent to load that exact skill with its skill tool and supply the
stated inputs. Replace example IDs/paths with actual selected inputs. Permissions,
project rules and missing-input handling remain the owner's, not granted by help.

## Index

| Topic/label | Facade, or exact direct-load owner |
| --- | --- |
| help | Client `/ris-help`; semantic questions attach `ris-proj-op-show-help` |
| init | `/risp-init` → `ris-proj-flow-initialize-project` |
| product-proposal* (portable product foundation) | `ris-port-op-formulate-product-foundation` |
| product-author* (project product foundation) | `ris-proj-op-author-product-foundation` |
| roadmap | `/risp-roadmap` → `ris-proj-op-plan-roadmap` |
| refine-epic | `/risp-refine-epic` → `ris-proj-op-refine-epic` |
| plan-epic-features | `ris-proj-op-plan-epic-features` (direct load) |
| prepare-feature | `/risp-prepare-feature` → `ris-proj-flow-prepare-feature` |
| interview-feature | `ris-proj-op-interview-feature` |
| specify-feature | `/risp-specify-feature` → `ris-proj-op-specify-feature` |
| design-feature | `/risp-design-feature` → `ris-proj-op-design-feature` |
| decompose-feature | `/risp-decompose-feature` → `ris-proj-op-decompose-feature` |
| run-task | `/risp-run-task` → `ris-proj-flow-execute-task` |
| run-simple-task | `/risp-run-simple-task` → `ris-proj-flow-execute-simple-task` |
| prep-copy* | `ris-proj-op-prepare-task-worktree` |
| implement/check* | `ris-proj-op-implement-task-tdd` |
| docs* | `ris-proj-op-update-documentation` |
| review-task | `/risp-review-task` → `ris-proj-op-review-task` |
| publish-task | `/risp-publish-task` → `ris-proj-op-publish-task` |
| complete-container | `/risp-complete-container` → `ris-proj-op-complete-container` |
| register-bug* | `ris-proj-op-register-bug` |
| investigate-bug* | `ris-proj-op-investigate-bug` |
| fix-bug* | `ris-proj-flow-fix-bug` |
| next | `/risp-next` → `ris-proj-op-suggest-continuation` |
| status | `/risp-status` → `ris-proj-op-show-plan` |
| retro | `/risp-retro` → `ris-proj-op-retrospect-session` |
| architecture rules | `ris-proj-op-author-architecture-rules` |
| development rules | `ris-proj-op-author-development-rules` |
| project OKF | `ris-proj-op-manage-okf-bundle` |
| integrated skill author | `ris-proj-op-author-skill` |
| installation | `/risb-installation` → `ris-port-op-manage-installation` |
| interview | `/risb-interview` → `ris-port-op-interview` |
| review-change | `/risb-review-change` → `ris-port-op-review-change` |
| skill | `/risb-skill` → `ris-port-op-author-skill` |
| portable requirements | `ris-port-op-formulate-feature-spec` |
| portable design | `ris-port-op-design-feature` |
| portable decomposition | `ris-port-op-decompose-feature-spec` |
| portable roadmap | `ris-port-op-plan-roadmap` |
| portable worktree | `ris-port-op-prepare-worktree` |
| portable implementation | `ris-port-op-implement-change` |
| portable bug research | `ris-port-op-investigate-bug` |
| portable retrospective | `ris-port-op-retrospect-session` |
| integrated verification | `ris-port-op-verify-feature` |
| architecture proposal | `ris-port-op-formulate-architecture-rules` |
| engineering proposal | `ris-port-op-formulate-development-rules` |
| autonomous OKF | `ris-port-op-manage-okf-bundle` |

Service details are outside the public menu. Only for a question about map labels
`exact task completion*` / `tracker publication*`, read **Tracker effects** below;
only for a context question read **Service context**. No facade is implied by `*`.

## Feature preparation

### ris-proj-op-show-help
[Owner](../SKILL.md). Purpose: explain RIS capabilities and routes.
Choose when: how-to help, not actual work/status. Inputs: optional question.
Result/stop: card, comparison or recommendation; zero writes/launch. The client
plugin owns fixed daily/full no-model pages, shared with direct skill requests.
Example: `/ris-help`, `/ris-help full` or `/ris-help run-task`.

### ris-proj-flow-initialize-project
[Owner](../../ris-proj-flow-initialize-project/SKILL.md). Purpose: agreed local RIS setup.
Choose when: onboard a new/existing project after package installation, not install
the package, refresh all rules or start roadmap/product development.
Inputs: selected project, existing evidence/decisions, setup/write scope and agreed
available executors; empty input establishes target/scope, never selects a task.
Result/stop: checked settings, bounded AGENTS addition, separately accepted product
and rules through their authors, RIS infrastructure and explicit readiness limits.
One leading dialogue; standalone operations use actual agreed executors. Tools,
Git/Beads side effects and project agents need specific permissions. Commit/push
is offered separately; an absent remote does not invalidate checked local setup. No
build/test/format/CI setup, roadmap or feature/task development follows.
Checks project-owned `standard`/`advanced` with explicit models and agreed RIS role
bindings; recommends models from the target's current available catalog, reuses
suitable saved choices and agrees changes. No global edits, silent upgrades or
inherited tier models; missing/refused setup limits dependent readiness.
Example: `/risp-init <project>, preserve existing material and agree local setup`.

### ris-proj-op-plan-roadmap
[Owner](../../ris-proj-op-plan-roadmap/SKILL.md). Purpose: combined epic/feature roadmap.
Choose when: plan product outcomes, not implementation tasks. One MVP epic is valid.
Inputs: project, product evidence, goal/state, write scope and depth `epic-only`,
`nearest` (default) or `all`; nearest stage follows accepted goals/constraints.
Result/stop: agreed epic+preliminary-feature proposal or verified tracker graph
with separate publication; no specs/design/implementation. Proposals reconcile
cross-epic overlaps before agreement and serial writes, preserving partial IDs.
Example: `/risp-roadmap propose an MVP roadmap for <project>, without writes`.

### ris-proj-op-refine-epic
[Owner](../../ris-proj-op-refine-epic/SKILL.md). Purpose: clarify one unclear epic.
Choose when: its goal/boundary is actually unclear, not to construct the feature graph.
Inputs: project, exact epic, current evidence and optional update authority.
Result/stop: goal/boundary clarification, no-op or verified agreed epic-content update;
no second feature-graph method.
Example: `/risp-refine-epic <epic ID>, propose only`.

### ris-proj-op-plan-epic-features
[Owner](../../ris-proj-op-plan-epic-features/SKILL.md). Purpose: preliminary feature graph.
Choose when: fill an empty existing epic or replan an evidenced coverage/product gap,
not merely because existing features are blocked. Inputs: project, exact epic,
sources, all-state work/neighbor context and write/publication scope.
Result/stop: concrete human-agreed feature graph, verified bounded tracker effects
and separate publication (full default); explicit proposal/local-only limits retained.
No spec/design/AC required for preliminary registration, no claims/implementation.
Example: `Load ris-proj-op-plan-epic-features for <epic ID>; propose only`.

### ris-port-op-plan-epic-features
[Owner](../../ris-port-op-plan-epic-features/SKILL.md). Purpose: read-only graph method.
Choose when: supplied epic/product/work context needs coverage, dedup, cycles,
stage prerequisites, parallel sets and neighbor-impact proposal; no RIS required.
Result/stop: unsaved bounded graph with local labels versus actual existing IDs,
explicit gaps and delta; no persistence, next-work selection or task splitting.

### ris-proj-flow-prepare-feature
[Owner](../../ris-proj-flow-prepare-feature/SKILL.md). Purpose: whole preparation route.
Choose when: prepare or resume one feature through verified decomposition.
Inputs: project, feature ID or epic/context, actor, known decisions and permitted
claim/copy/document/Git/tracker effects.
Result/stop: early same-ID record and one safe preparation copy, one dialogue and
precise acceptance of both complete requirements/design scopes (one act allowed),
independent review, published inputs and verified one-task or child-task/edge
coverage with separate tracker publication. Sufficient inline design needs no
design.md. Optional drafts are not acceptance/publication. No implementation/close.
One author context reuses stable preflight, with fresh live guards and native
preparation assignment, not a second execution claim. Only new material questions;
related ordered blocks allowed. Draft review optional; final independent review/
reassessment required. Short spec/design has AC/how-to-check, not a backlog.
Full composition/combined check precedes final tracker publication; partial resume
does only the missing effects, without a required readiness marker or child count.
Example: `/risp-prepare-feature <existing feature ID>`; with an epic, choose existing
needed-stage candidates; an empty epic first needs agreed graph planning. Parallel
candidates remain visible; all-blocked diagnoses prerequisites, not new features.

### ris-proj-op-interview-feature
[Owner](../../ris-proj-op-interview-feature/SKILL.md). Purpose: elicit requirements.
Choose when: feature behavior/quality decisions need dialogue, not acceptance/save.
Inputs: selected feature/project, known answers, evidence and interview scope.
Result/stop: sourced status-aware handoff, without writing a specification.
Example: `Load ris-proj-op-interview-feature for authorization in <project>`.

### ris-proj-op-specify-feature
[Owner](../../ris-proj-op-specify-feature/SKILL.md). Purpose: accepted requirements,
or explicitly limited early native-task registration of an already selected feature.
Choose when: formulate/accept/save/publish behavior, not technical design.
Inputs: project and feature ID/epic or explicit standalone/document subject,
known decisions, separate acceptance and allowed effects; ID discovers own refs.
Result/stop: accepted saved/published requirements and reconciled record, or the
explicitly limited contribution; no decomposition/implementation.
Example: `/risp-specify-feature <ID>, requirements scope <scope>`.
Early example: `/risp-specify-feature early registration only: <title/goal>,
stable key <project-scoped-key>, optional epic <ID>; no documents yet`.
The registration result is an ID with honest null inputs, not acceptance or
readiness. The existing copy owner accepts that ID with purpose
`feature-preparation` before document writes; execution purpose keeps its gates.

### ris-proj-op-design-feature
[Owner](../../ris-proj-op-design-feature/SKILL.md). Purpose: sufficient technical design.
Choose when: design or revise bounded accepted behavior, not choose requirements.
Inputs: project, ID or document-only subject, accepted requirements/current code,
separate design acceptance and permitted save/publication/record effects.
Result/stop: independently accepted versioned design and aligned refs, or explicit
limited contribution. New/materially changed designs get a plain-language explanation
before separate acceptance of the complete accessible candidate, not just a summary;
an explicitly authorized draft save can precede acceptance without publishing it.
No task decomposition or code.
Example: `/risp-design-feature <ID>`.

### ris-proj-op-decompose-feature
[Owner](../../ris-proj-op-decompose-feature/SKILL.md). Purpose: sufficient task set.
Choose when: accepted inputs are ready for one-task assessment/decomposition.
Inputs: project, confirmed feature or explicit standalone ID, accepted inputs,
design/contracts and authorized tracker effects.
Result/stop: verified one-task case or necessary children/dependencies and tracker
publication; no technical plan for one task or implementation.
Example: `/risp-decompose-feature <ID>`.

## Execution and distinct effects

### ris-proj-flow-execute-task
[Owner](../../ris-proj-flow-execute-task/SKILL.md). Purpose: full single-task execution.
Choose when: execute/resume ready work, not just plan/review or run a container.
Inputs: project, optional exact ID, actor, accepted basis, execution/publication
rights and available configured executors; explicit native bug needs readable versioned inputs.
Result/stop: checked independently reviewed change, verified Git, separate exact
completion and tracker publication, or exact preserved remainder.
Example: `/risp-run-task <ID>, actor <actor>`.

### ris-proj-flow-execute-simple-task
[Owner](../../ris-proj-flow-execute-simple-task/SKILL.md). Purpose: complete one bounded request/idea.
Choose when: explicit or suitable natural request; small, locally bounded, understood,
checkable work, not product-logic/architecture/material-contract changes, coordinated
independent outcomes, broad/unknown effects or queue selection. File type/diff size
is not the admission test; code/config/docs/tools/ignored/external can qualify.
Inputs: project, attributable request/criteria, optional real ID, constraints/rights.
Result/stop: one main agent/default zero subagents, mandatory self-check/checks/TDD;
independent review only for explicit request, mandatory target policy or explained
material risk, not code/Git alone. Inactive review loads no role/format/skip report;
active review is really independent with finding/repair gates, no mandatory YAML.
Versioned edits use one own branch/worktree with reuse; local-only actual targets
need no dummy Git, mixed checks both. Git/local/no-change outcomes and separate
tracker result/exact close/publication when used, short Beads mandatory in RIS.
Fast ancestor tail runs inline, full/bug delegation unchanged. No mandatory preparation/
plan/log/handoff/review files; no feature/bug/container downgrade. Empty asks for work.
Resume reconciles actual effects with same ID/copy and no confirmed push/close replay;
absent inapplicable review is not debt. Scope expansion is targeted, not SDLC restart.
Example: `/risp-run-simple-task correct the documented flag in <file>; check links`.

### ris-proj-op-prepare-task-worktree
[Owner](../../ris-proj-op-prepare-task-worktree/SKILL.md). Purpose: claim-aware copy.
Choose when: prepare/reuse a copy for a confirmed task, not plan or implement.
Inputs: project, task ID, actor, context-checked source-folder association, selected adapter and
authorized claim/copy/setup scope.
Result/stop: verified claim/blockers, copy association and separate environment
readiness; no publication or task completion.
Example: `Load ris-proj-op-prepare-task-worktree for <ID> in <project>, actor <actor>, allowed setup <scope>`.

### ris-proj-op-implement-task-tdd
[Owner](../../ris-proj-op-implement-task-tdd/SKILL.md). Purpose: checked task change.
Choose when: code/test implementation or review-finding repair with mandatory TDD.
Inputs: project/task/actor, suitable supplied copy, fresh claim/unblocked state,
accepted inputs/current code and allowed code/tests/docs paths.
Result/stop: observed RED/GREEN, affected checks and exact code/tests/docs snapshot;
no independent approval, commit/push or closure. Text-only work uses its content owner.
Example: `Load ris-proj-op-implement-task-tdd for <ID> in <copy>, actor <actor>, within <accepted scope and permissions>`.

### ris-proj-op-update-documentation
[Owner](../../ris-proj-op-update-documentation/SKILL.md). Purpose: synchronize affected docs.
Choose when: inspected implementation makes authorized guidance stale, not redesign.
Inputs: project/copy, exact change/integration state and explicitly allowed documents.
Result/stop: checked bounded docs or justified no-change; no autonomous product rewrite.
Example: `Load ris-proj-op-update-documentation for <project/copy>, snapshot <base+overlay>, allowed docs <paths>`.

### ris-proj-op-review-task
[Owner](../../ris-proj-op-review-task/SKILL.md). Purpose: assess a project change.
Choose when: independent review/re-review, not repair or acceptance of design.
Inputs: project, optional ID, full concrete snapshot, criteria and review purpose.
Result/stop: one local review.yaml with compact ris.review/2 rounds (existing /1
continues under conditional compatibility without migration); no-ID save
needs an explicit path. Fast review is conditional; when active it permits sufficient session-only evidence, optional
save uses the same format. Format validity is not approval applicability.
Self-review does not supply independent publication approval.
Example: `/risp-review-task <ID>, full candidate <snapshot>`.

### ris-proj-op-publish-task
[Owner](../../ris-proj-op-publish-task/SKILL.md). Purpose: verified primary Git publication.
Choose when: independently reviewed task/change or pre-ID documents need integration.
Inputs: project, confirmed own branch/dedicated worktree, complete approved snapshot and check/
independence evidence, destination and whole-outgoing direct-push authority.
Only verified eligible Fast can supply its narrow no-required-review basis instead
of independent approval; arbitrary waiver/direct documents/full/feature/bug cannot.
Changed not-required Fast snapshots get affected self-check and renewed admission/risk
assessment, not fictional independent approval; required review gets reassessment.
Result/stop: integrated reviewed commit and fresh remote confirmation, remote-only
without local authority; an explicit request or applicable accepted project policy
permits separate safe FF, no branch switching. Caller checks/forwards actual policy
provenance and boundaries; dependency effects need their own authorization. Required
unfinished maintenance prevents combined completion, not confirmed Git/close/Dolt. No PR/deploy,
content acceptance, tracker publication or leaf/container closure.
Example: `/risp-publish-task <ID>, approved snapshot <snapshot and review locator>`.

### ris-proj-op-complete-container
[Owner](../../ris-proj-op-complete-container/SKILL.md). Purpose: selected container result.
Choose when: ordinary parent close/closure eligibility, administrative close,
read-only verification or explicit verify-and-close of
one feature/standalone task-container/epic; never ordinary leaf completion.
Inputs: project, exact ID/kind, explicit intent; assessment needs accepted full
scope/integrated evidence, writes need separate authority.
Result/stop: ordinary close from nonempty closed direct children and no parent blockers
(not fresh whole-result acceptance), read-only eligibility, administrative status,
read-only criterion verdict, or successful verified close and authorized tracker publication;
zero-child features retain own-result verification. No mandatory saved assessment;
no child/parent auto-close or Git publication.
Example: `/risp-complete-container verify <ID> read-only`.

## Bug and current-work navigation

### ris-proj-op-register-bug
[Owner](../../ris-proj-op-register-bug/SKILL.md). Purpose: record unconfirmed bug message.
Choose when: preserve report before investigation, not diagnose or claim it.
Inputs: project, original message/context and registration authority.
Result/stop: all-status duplicate reconciliation, verified ID/new or supplemented
original; no investigation, fix or closure.
Example: `Load ris-proj-op-register-bug for <project>: <message>; record and return ID only`.

### ris-proj-op-investigate-bug
[Owner](../../ris-proj-op-investigate-bug/SKILL.md). Purpose: investigate registered bug.
Choose when: exact-ID diagnosis/report, not registration or fixing.
Inputs: project, exact native bug ID, expectation/code/evidence and research/write scope.
Result/stop: checked current report and aligned fix criteria with one assigned
investigator, authorized native writes, fresh comparison and read-back, or exact
unsaved/partial remainder. This is not CAS; ordinary saving needs no CAS provider.
Observed conflicts stop writes; justified correct/duplicate disposition
is separate. Confirmation is not fix readiness; no automatic fix.
Example: `Load ris-proj-op-investigate-bug for <bug ID> in <project>, allowed scope <scope>; stop before fixing`.

### ris-proj-flow-fix-bug
[Owner](../../ris-proj-flow-fix-bug/SKILL.md). Purpose: fix one registered native bug.
Choose when: exact-ID fix/resume has a sufficient saved basis, not fresh diagnosis.
Inputs: project, exact bug ID, actor, current report/aligned criteria/accepted
constraints and authorized fix/publication scope. Material design needs separate acceptance.
Result/stop: reproducible exact tracker-history/Git basis, complete existing run-task route,
checked fix, independent review, Git, separate exact fix-completion/tracker publication;
no second engine, bug selection or automatic investigation.
Example: `Load ris-proj-flow-fix-bug for <bug ID> in <project>, actor <actor>, allowed fix/publication <scope>`.

### ris-proj-op-suggest-continuation
[Owner](../../ris-proj-op-suggest-continuation/SKILL.md). Purpose: actual-work continuation.
Choose when: next step for selected work, not generic how-to or execution.
Inputs: project and ID or explicit no-ID source/scope locator, permitted bounded reads.
Result/stop: one checked prompt, necessary human decision or blocker; no write/launch,
readiness certification or acceptance.
Example: `/risp-next <ID>`.

### ris-proj-op-show-plan
[Owner](../../ris-proj-op-show-plan/SKILL.md). Purpose: actual complete unclosed plan.
Choose when: project status/ID subtree overview, not a help catalog or task execution.
Inputs: selected project and optional exact ID; actual adapter/source reads.
Result/stop: compact real hierarchy, directed blockers and one continuation action;
no saving, claiming, acceptance or execution.
Example: `/risp-status` or `/risp-status <ID>`.

## Other project operations

### ris-proj-op-author-product-foundation
[Owner](../../ris-proj-op-author-product-foundation/SKILL.md). Purpose: accepted project product knowledge.
Choose when: create or make an explicitly bounded update to the product foundation,
not initialize a project, plan a roadmap or select architecture/stack.
Inputs: selected project/current copy, create/update boundary, available materials,
existing content/decisions for update, acceptance authority and allowed save scope.
Result/stop: separately accepted complete content saved and checked in sources.product
through the project OKF owner, including decision/navigation/read-back; proposal-only,
refusal or absent acceptance writes no product files. No next-stage launch, tracker,
commit/push or claim of complete project readiness.
Example: `Load ris-proj-op-author-product-foundation for <project/copy>, create product knowledge from <materials>; obtain separate content acceptance then save/check within <authorized scope>`.

### ris-proj-op-retrospect-session
[Owner](../../ris-proj-op-retrospect-session/SKILL.md). Purpose: one local session retrospective.
Choose when: stopped OpenCode session postmortem in RIS, not multi-session audit.
Inputs: project, exact session/export or permitted list-and-selection, acquisition
scope; saving requires explicitly authorized destination.
Result/stop: sourced causes/costs/minimal owner-addressed improvements in response;
no repairs, full diff review or feature acceptance.
Example: `/risp-retro <session ID>, read-only, return report here`.

### ris-proj-op-author-architecture-rules
[Owner](../../ris-proj-op-author-architecture-rules/SKILL.md). Purpose: accepted architecture norms.
Choose when: create/amend project rules, not code audit or feature design.
Inputs: project, evidence/decisions, bounded topic and authorized rules destination.
Result/stop: explicitly accepted scope saved/checked as OKF in sources.rules;
no installing tools, impact delivery or library extraction.
Example: `Load ris-proj-op-author-architecture-rules for <project>, scope <boundary rules>, authorized save <scope>`.

### ris-proj-op-author-development-rules
[Owner](../../ris-proj-op-author-development-rules/SKILL.md). Purpose: accepted engineering norms.
Choose when: versions/build/style/testing/review/CI rules, not configuring CI.
Inputs: project evidence, justified customizable practices and authorized rules scope.
Result/stop: separately accepted engineering content saved/checked as project OKF;
no architecture redesign, tool install or audit.
Example: `Load ris-proj-op-author-development-rules for <project>, scope <testing rules>, allowed save <scope>`.

### ris-proj-op-manage-okf-bundle
[Owner](../../ris-proj-op-manage-okf-bundle/SKILL.md). Purpose: project-context OKF operation.
Choose when: selected bundle in an authorized RIS project area, not ordinary Markdown.
Inputs: explicit project/root/operation/scope, rules/config provenance and permissions.
Result/stop: bounded read/create/edit/check result with format/content responsibility
kept distinct; no discovery, acceptance or skill authoring.
Example: `Load ris-proj-op-manage-okf-bundle: project <path>, root <bundle>, operation check, scope <files>`.

### ris-proj-op-author-skill
[Owner](../../ris-proj-op-author-skill/SKILL.md). Purpose: combined RIS-integrated skill source.
Choose when: target actually integrates with RIS; autonomous targets use portable author.
Inputs: worked-out requirements, destination, neighboring contracts and allowed scope.
Result/stop: checked combined source/dependencies/resources; no installation or execution.
Example: `Load ris-proj-op-author-skill; improve <RIS skill folder> within <scope>; do not install`.

## Portable methods (direct inputs, no RIS setup)

### ris-port-op-formulate-product-foundation
[Owner](../../ris-port-op-formulate-product-foundation/SKILL.md). Purpose: sourced product-foundation proposal.
Choose when: purpose/users/tasks/capabilities/boundaries/constraints/unknowns need a
coherent initial proposal or bounded amendment, not a feature spec or technical design.
Inputs: create/update, product/scope, materials/versions, constraints/prior answers;
update also requires existing content and an explicit boundary.
Result/stop: checked read-only proposal with provenance, decisions/statuses and
deferred-impact limits; conditional interview only for interdependent gaps.
No acceptance, saving, initialization, roadmap, stack/architecture choice or next skill.
Example: `Load ris-port-op-formulate-product-foundation with <product/materials>, create or bounded update <scope>; return an unsaved proposal`.

### ris-port-op-manage-installation
[Owner](../../ris-port-op-manage-installation/SKILL.md). Purpose: full RIS package management.
Choose when: explicit install/update/uninstall, not project initialization or auto-update.
Inputs: operation, existing absolute target project path, optional exact tag/full
commit for install/update, package replacement authority.
Result/stop: checked filesystem outcome/version/counts or recovery diagnostic;
restart OpenCode after package changes. No Git commit/push.
Example: `/risb-installation update RIS in /absolute/project to commit <full SHA>`.

### ris-port-op-interview
[Owner](../../ris-port-op-interview/SKILL.md). Purpose: bounded decision-tree interview.
Choose when: interdependent decisions need dialogue, not a single clarification.
Inputs: topic, bounds, known answers; limited mode needs explicit sufficiency criterion.
Result/stop: sourced status-aware handoff, not a saved/accepted specification.
Example: `/risb-interview deployment tradeoffs for <system>`.

### ris-port-op-author-skill
[Owner](../../ris-port-op-author-skill/SKILL.md). Purpose: autonomous skill source.
Choose when: standalone skill even in a RIS project, not actual RIS integration.
Inputs: worked-out requirements, target rules, destination and write scope.
Result/stop: ready source folder or labeled unsaved draft, not install/publication
or performance of the authored operation.
Example: `/risb-skill create <autonomous skill> from <requirements> in <folder>, source only`.

### ris-port-op-review-change
[Owner](../../ris-port-op-review-change/SKILL.md). Purpose: concrete change assessment.
Choose when: read-only review/re-review, not repair, design approval or publication.
Inputs: concrete code/doc change or WIP, baseline, criteria and review scope.
Result/stop: versioned evidence-based required fixes/optional recommendations;
no project report storage or self-approved publication.
Example: `/risb-review-change <diff/snapshot>, scope <criteria>`.

### ris-port-op-formulate-feature-spec
[Owner](../../ris-port-op-formulate-feature-spec/SKILL.md). Purpose: substantive requirements proposal.
Choose when: decisions/evidence are known, not an interview from scratch.
Inputs: bounded feature, known decisions, sources/status and constraints.
Result/stop: checked portable behavior/constraints/AC content and gaps; no acceptance,
project save or decomposition.
Example: `Load ris-port-op-formulate-feature-spec with <feature decisions/evidence>; return proposal`.

### ris-port-op-design-feature
[Owner](../../ris-port-op-design-feature/SKILL.md). Purpose: technical design proposal.
Choose when: bounded requirements need sufficient design, not implementation.
Inputs: requirements/version, actual code/architecture and technical constraints.
Result/stop: checked sufficient design/alternatives/gaps; no acceptance or project save.
Example: `Load ris-port-op-design-feature with <requirements and code>; propose only`.

### ris-port-op-decompose-feature-spec
[Owner](../../ris-port-op-decompose-feature-spec/SKILL.md). Purpose: verifiable work-unit proposal.
Choose when: requirements/design are ready to split work, not plan one task.
Inputs: spec, accepted design, criteria, test seams and necessary dependencies.
Result/stop: smallest sufficient traced work set; no tracker creation or approval.
Example: `Load ris-port-op-decompose-feature-spec with <spec/design>; return work proposal`.

### ris-port-op-plan-roadmap
[Owner](../../ris-port-op-plan-roadmap/SKILL.md). Purpose: goal-to-epic proposal.
Choose when: plan project outcomes without tracker persistence.
Inputs: explicitly supplied product knowledge/high-level spec, chosen goal and observed state.
Result/stop: checked bounded roadmap with light architecture/source impact; no task decomposition.
Example: `Load ris-port-op-plan-roadmap with <product>, goal <MVP>, current state <evidence>`.

### ris-port-op-prepare-worktree
[Owner](../../ris-port-op-prepare-worktree/SKILL.md). Purpose: checked working copy/environment.
Choose when: autonomous new/reused worktree for identified work, not claim or planning.
Inputs: exact work/repository/path/branch/base, selected adapter and optional setup authority.
Result/stop: verified copy and separate environment handoff; no repair/publication.
Example: `Load ris-port-op-prepare-worktree for <work>, repository <path>, target <path/branch>, base <SHA>, Git adapter, no setup`.

### ris-port-op-implement-change
[Owner](../../ris-port-op-implement-change/SKILL.md). Purpose: bounded change or finding repair.
Choose when: accepted change needs code/tests, not redesign or approval.
Inputs: requirements/current code, accepted constraints, allowed files/checks and
standard or required TDD mode; TDD wins when mandated.
Result/stop: checked exact candidate/tests, observed RED/GREEN in TDD; no tracker,
worktree management, independent approval or publication.
Example: `Load ris-port-op-implement-change for <change>, mode tdd, allowed scope <files/checks>`.

### ris-port-op-investigate-bug
[Owner](../../ris-port-op-investigate-bug/SKILL.md). Purpose: supplied-input defect research.
Choose when: diagnose locally without a registered project bug operation.
Inputs: message, authoritative expectations, code/version, evidence and research scope.
Result/stop: sourced confirmation/findings/fix-readiness report; no registration,
tracker write, implementation or full incident investigation.
Example: `Load ris-port-op-investigate-bug with <message/expectations/code/evidence>, scope <research>`.

### ris-port-op-retrospect-session
[Owner](../../ris-port-op-retrospect-session/SKILL.md). Purpose: one supplied-history retrospective.
Choose when: transcript/event history is already supplied, even outside RIS.
Inputs: one session and proven participant branches, question/scope and metric semantics.
Result/stop: evidence-based causes/costs/minimal improvements in response; no history
collection, full diff review, repairs or multi-session Langfuse audit.
Example: `Load ris-port-op-retrospect-session with <transcript>, question <bottleneck>; read-only report`.

### ris-port-op-verify-feature
[Owner](../../ris-port-op-verify-feature/SKILL.md). Purpose: full integrated criterion verification.
Choose when: assess delivered feature on one revision, not diff review.
Inputs: complete requirements/AC, accepted design, identified integrated revision,
architecture/docs and applicable evidence.
Result/stop: pass/fail/unverified per criterion and limits; no code, acceptance of
new design or tracker closure. Actual project prohibitions on checks apply.
Example: `Load ris-port-op-verify-feature for <feature> at <full revision>, inputs <accepted refs>; read-only`.

### ris-port-op-formulate-architecture-rules
[Owner](../../ris-port-op-formulate-architecture-rules/SKILL.md). Purpose: architecture norms proposal.
Choose when: formulate/amend justified rules, not code audit or feature design.
Inputs: supplied project facts, decisions, sources and bounded constraints.
Result/stop: sourced portable proposal/open questions; no acceptance/save, tooling
setup, impact delivery or library extraction.
Example: `Load ris-port-op-formulate-architecture-rules with <facts/decisions>, scope <boundaries>`.

### ris-port-op-formulate-development-rules
[Owner](../../ris-port-op-formulate-development-rules/SKILL.md). Purpose: engineering norms proposal.
Choose when: choose versions/build/style/testing/review/CI practices, not install tools.
Inputs: project evidence, justified customizable tool/practice needs and constraints.
Result/stop: checked proposal/compatibility limits; no acceptance/save, CI config,
code audit, feature design or extraction.
Example: `Load ris-port-op-formulate-development-rules with <project evidence>, scope <testing/review>`.

### ris-port-op-manage-okf-bundle
[Owner](../../ris-port-op-manage-okf-bundle/SKILL.md). Purpose: autonomous OKF 0.2 operation.
Choose when: direct selected-bundle work in any authorized location, no RIS context.
Inputs: explicit bundle root, read/create/edit/check operation, bounded scope/rights.
Result/stop: checked bounded OKF result and limits; not ordinary Markdown or skill authoring.
Example: `Load ris-port-op-manage-okf-bundle: root <absolute bundle>, operation check, scope <files>`.

## Tracker effects (conditional service explanation, not public menu)

`exact task completion*` and `tracker publication*` use the **selected tasks
adapter's** advertised operations, not fictional slash commands. In the shipped
Beads integration the exact direct owner is
[ris-proj-adapter-beads-tasks](../../ris-proj-adapter-beads-tasks/SKILL.md).
Purpose: bounded native result/exact close and separately authorized Dolt publication.
Choose when: an authorized execution owner reaches those effects, not generic help
or automatic parent acceptance. Inputs: selected project, exact ID/type, explicit
effect/authority, fresh criteria/children/blockers and published Git/check/review
evidence where required; publication additionally needs authorized shared-history
scope and actual remote/revision. Result/stop: independently verified local effect
or selected-remote revision reachability, not a guarantee that both occurred.
Example: `Load ris-proj-adapter-beads-tasks for <project>, exact task <ID>; persist supplied published result then separately verify native exact completion within <authority>`.
Publication example: `Load ris-proj-adapter-beads-tasks for <project>; separately publish authorized Dolt history <scope>, required revision <S>, selected remote <R>`.
Another selected adapter must actually support the needed operations; tasks v1
alone does not promise claim, close or publication. Do not configure one via help.

## Service context (only when asked)

[ris-proj-op-resolve-context](../../ris-proj-op-resolve-context/SKILL.md) prepares
selected project settings/paths/optional role names for a caller, not domain
readiness, tracker execution or files. Inputs: project, operation, required fields
and config provenance. Result/stop: checked settings/diagnostics, zero writes.
Example: `Load ris-proj-op-resolve-context for <project>, calling operation <operation>, needed settings <fields>, read-only`.
Shared common instructions and worktree adapters are internal dependencies, not
extra required user stages; their presence is not proof of tool or agent availability.
