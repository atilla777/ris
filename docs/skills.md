# Skills and commands

RIS includes portable operations, project-integrated operations, five workflows,
shared instructions and tool adapters. Each linked `SKILL.md` defines its actual
inputs, dependencies, permissions, checks and stopping point.

All 52 source skills are listed below, independently of the 20-entry menu.
Only selected operations/workflows have slash commands. Command sources live in
[`commands/opencode/`](../commands/opencode/); each explicitly loads one skill
and passes `$ARGUMENTS` through its existing contract. The exception is `/ris-help`:
[`plugins/opencode/ris-help/`](../plugins/opencode/ris-help/) owns the client command,
not a Markdown slash facade. The menu has 19 agent commands plus this client entry.

## Naming

Identifiers use `ris-<port|proj>-<op|flow|lib|adapter>-<verb-object|purpose>`:

- `port`: direct inputs without requiring RIS project configuration, document
  structure or a tracker; actual target-project rules still apply.
- `proj`: necessary RIS integration, with configuration and execution roles
  required only where the particular operation needs them.
- `op`: one useful result; `flow`: coordination of independently useful operations.
- `lib`: shared instructions; `adapter`: bounded tool operations.

Names are lowercase ASCII words separated by single hyphens, at most 64 characters.
Skill source directory, frontmatter `name` and installed directory agree.
Command basenames define independent slash names: `risp-` explicitly selects a
project contract, `risb-` a portable contract, without environment-based routing.
The single accepted exception is `/ris-help` → local fixed pages or semantic
questions with `ris-proj-op-show-help`, without
`risp-`/`risb-` or technical-name aliases; other naming rules are unchanged.
For older names, use the
[namespace transition guide](skill-command-naming-migration.md); there are no aliases.

## Current compact command menu

The historical [18-entry v1 set](specs/compact-commands/spec.md) is extended by
`/risp-status` under [plan-status D1](specs/plan-status/design.md#8-поставка-и-совместимость)
and `/risp-run-simple-task` under the [fast D2 amendment](specs/compact-commands/spec.md#8-поправка-fast-task-execution-d2--один-новый-вход),
plus `/risp-init` under [project-initialization D1](specs/project-initialization/design.md).
Its [tier-setup amendment](specs/project-initialization/agent-tiers-amendment.md)
adds project-owned Standard/Advanced, explicitly pinned user-agreed models from
the current available catalog and checked role mappings, without global edits or
automatic upgrades. Suitable existing choices are reused; incomplete setup has
explicit readiness limits. Package installation alone does not configure agents.
The current source map adds the [workflow-help exception](specs/workflow-help/spec.md):
**20 entries (15 project + 4 portable + one help exception)** after
[ris-a17](specs/ris-a17/spec.md) retires the standalone feature selector without alias;
availability in a project requires installation
of the chosen package and client restart.

| Command | Exact skill target |
| --- | --- |
| `/risp-init` | `ris-proj-flow-initialize-project` |
| `/ris-help` | Client plugin; only semantic questions attach `ris-proj-op-show-help` |
| `/risp-status` | `ris-proj-op-show-plan` |
| `/risp-next` | `ris-proj-op-suggest-continuation` |
| `/risp-roadmap` | `ris-proj-op-plan-roadmap` |
| `/risp-refine-epic` | `ris-proj-op-refine-epic` |
| `/risp-prepare-feature` | `ris-proj-flow-prepare-feature` |
| `/risp-specify-feature` | `ris-proj-op-specify-feature` |
| `/risp-design-feature` | `ris-proj-op-design-feature` |
| `/risp-decompose-feature` | `ris-proj-op-decompose-feature` |
| `/risp-run-task` | `ris-proj-flow-execute-task` |
| `/risp-run-simple-task` | `ris-proj-flow-execute-simple-task` |
| `/risp-review-task` | `ris-proj-op-review-task` |
| `/risp-publish-task` | `ris-proj-op-publish-task` |
| `/risp-complete-container` | `ris-proj-op-complete-container` |
| `/risp-retro` | `ris-proj-op-retrospect-session` |
| `/risb-interview` | `ris-port-op-interview` |
| `/risb-review-change` | `ris-port-op-review-change` |
| `/risb-skill` | `ris-port-op-author-skill` |
| `/risb-installation` | `ris-port-op-manage-installation` |

`status` shows the complete compact unclosed plan and one checked recommendation;
`next` recommends for an already selected subject; `run-task` executes one
authorized task. `skill` authors autonomous source, without selecting the RIS
author or installing it. Empty inputs, permissions, recovery and stopping points
remain those of each linked owner. No aliases are shipped.

`run-simple-task` executes/resumes one bounded request or idea, with optional ID;
a suitable natural request can select the same Fast without knowing the command.
Empty input asks for work, never chooses the queue.
It adds one entry under the [D2 menu amendment](specs/compact-commands/spec.md#8-поправка-fast-task-execution-d2--один-новый-вход).

`/ris-help` immediately displays fixed daily Markdown on empty/simple input,
without a model call:
status/next, feature preparation/decomposition and task execution. `/ris-help full`
(`/ris-help полный` in Russian) returns detailed thematic pages with separate
operation blocks, including installation/init, roadmap, individual task stages,
bugs, acceptance and retrospective. A named command, comparison or intent still
yields agent-backed focused help, never execution. Fixed pages open in a scrollable
client dialog (Esc closes); no fixed 80×24 layout. Exact English/Russian selectors
and locale defaults are documented in [README](../README.md#start-using-ris).
Questions are queued in the current session or create a help session from Home.
The plugin and direct skill share the same independent bilingual Markdown assets
in `plugins/opencode/ris-help/pages/`; cards/routes remain skill resources.
No `ris.yaml`, Beads, source checkout or project setup is required. One RIS-specific
skill suffices because the subject is RIS itself; no artificial portable pair.
It preserves common/context ownership, zero-write/zero-launch limits and the
boundary with actual-work `next`/`status`. Source readiness does not confirm client
discovery or live behavior.

`status` and `next` recommend from existing records and needed-stage evidence;
they do not certify execution readiness or invent new product outcomes. Relevant
own started work, priorities, creation time/ID and material prerequisites matter;
independent parallel candidates stay visible. Empty epics need graph planning,
all-blocked epics need diagnosis, not automatic new features. History, composition,
acceptance and publication evidence expand only when they change the recommendation.
Unknown facts stay explicit. The executing owner checks current readiness,
acceptance, ownership and permissions; navigation writes nothing and launches nothing.

### Explicit calls without a slash command

Ask the agent to load the exact skill with its skill tool and supply the inputs:

```text
Load ris-proj-op-author-skill and improve the RIS-integrated skill at <source folder> within <accepted scope>; do not install it.
Load ris-proj-op-plan-epic-features for <existing epic ID>; propose its preliminary feature graph without writes.
Load ris-port-op-plan-epic-features with <epic goal, product materials, existing work and neighbors>; return an unsaved graph proposal.
Load ris-proj-op-register-bug for <project>: <message and available context>; record this unconfirmed report and return its ID without investigation.
Load ris-proj-op-investigate-bug for <exact bug ID> in <project>, research/write scope <scope>; save the investigation and stop before fixing.
Load ris-port-op-investigate-bug with <message, expectation sources, code/version, evidence and allowed research scope>; return a report without tracker writes.
Load ris-proj-flow-fix-bug for <exact native bug ID> in <project>, actor <actor>, within <authorized fix/publication scope>; use the saved sufficient report and existing execution route.
Load ris-proj-op-implement-task-tdd for <ID> in <project/copy>, actor <actor>, within the accepted scope and permissions.
Load ris-proj-op-update-documentation for <project/copy>, inspected change <snapshot>, authorized documents <paths>.
Load ris-port-op-formulate-product-foundation with <product, create/update scope, materials and prior answers>; return an unsaved proposal.
Load ris-proj-op-author-product-foundation for <project/copy>, <create or bounded update>; obtain separate content acceptance and save/check in sources.product within <authorized scope>.
Load ris-port-op-manage-okf-bundle: root <absolute bundle>, operation check, scope <selected files>.
```

The same direct-load form works for every retained skill. For project OKF use
`ris-proj-op-manage-okf-bundle` with explicit project/root/operation/scope.
Loading is not acceptance, write authority or proof of readiness; the owner
checks its inputs. A missing slash facade does not remove the operation.

## Portable operations

| Skill | Result |
| --- | --- |
| [ris-port-op-author-skill](../skills/ris-port-op-author-skill/SKILL.md) | Autonomous skill source authoring |
| [ris-port-op-interview](../skills/ris-port-op-interview/SKILL.md) | Bounded decision-tree interview |
| [ris-port-op-investigate-bug](../skills/ris-port-op-investigate-bug/SKILL.md) | Direct-input evidence-based bug report, confirmation and fix-readiness conclusions |
| [ris-port-op-formulate-feature-spec](../skills/ris-port-op-formulate-feature-spec/SKILL.md) | Feature requirements proposal |
| [ris-port-op-design-feature](../skills/ris-port-op-design-feature/SKILL.md) | Technical design proposal |
| [ris-port-op-decompose-feature-spec](../skills/ris-port-op-decompose-feature-spec/SKILL.md) | Verifiable work-unit proposal |
| [ris-port-op-plan-roadmap](../skills/ris-port-op-plan-roadmap/SKILL.md) | Goal-level roadmap proposal |
| [ris-port-op-plan-epic-features](../skills/ris-port-op-plan-epic-features/SKILL.md) | Portable preliminary feature-graph proposal with coverage, stage prerequisites and parallel sets |
| [ris-port-op-prepare-worktree](../skills/ris-port-op-prepare-worktree/SKILL.md) | Checked working-copy/environment handoff |
| [ris-port-op-implement-change](../skills/ris-port-op-implement-change/SKILL.md) | Bounded implementation or review-finding repair |
| [ris-port-op-review-change](../skills/ris-port-op-review-change/SKILL.md) | Read-only change assessment |
| [ris-port-op-retrospect-session](../skills/ris-port-op-retrospect-session/SKILL.md) | Retrospective from supplied history |
| [ris-port-op-verify-feature](../skills/ris-port-op-verify-feature/SKILL.md) | Integrated all-criterion feature verification |
| [ris-port-op-formulate-architecture-rules](../skills/ris-port-op-formulate-architecture-rules/SKILL.md) | Architecture-rules proposal |
| [ris-port-op-formulate-development-rules](../skills/ris-port-op-formulate-development-rules/SKILL.md) | Engineering-rules proposal |
| [ris-port-op-formulate-product-foundation](../skills/ris-port-op-formulate-product-foundation/SKILL.md) | Sourced read-only product-foundation proposal or bounded amendment |
| [ris-port-op-manage-okf-bundle](../skills/ris-port-op-manage-okf-bundle/SKILL.md) | Explicit-root autonomous OKF read/create/edit/check |
| [ris-port-op-manage-installation](../skills/ris-port-op-manage-installation/SKILL.md) | Checked full-package install/update/uninstall |

## Project operations and workflows

| Skill | Result |
| --- | --- |
| [ris-proj-op-author-skill](../skills/ris-proj-op-author-skill/SKILL.md) | Combined RIS skill authoring |
| [ris-proj-op-show-help](../skills/ris-proj-op-show-help/SKILL.md) | Agent-backed read-only command cards, comparisons and intent routes; direct fixed requests use shared pages, without project setup |
| [ris-proj-op-resolve-context](../skills/ris-proj-op-resolve-context/SKILL.md) | Read-only project configuration/path preparation |
| [ris-proj-op-register-bug](../skills/ris-proj-op-register-bug/SKILL.md) | Unconfirmed bug registration or safe original supplementation, verified ID and stop |
| [ris-proj-op-investigate-bug](../skills/ris-proj-op-investigate-bug/SKILL.md) | Exact-ID investigation, protected current report/criteria and justified message disposition |
| [ris-proj-op-plan-roadmap](../skills/ris-proj-op-plan-roadmap/SKILL.md) | Combined epic/preliminary-feature roadmap, agreement and verified tracker publication |
| [ris-proj-op-refine-epic](../skills/ris-proj-op-refine-epic/SKILL.md) | One unclear epic's outcome and boundaries |
| [ris-proj-op-plan-epic-features](../skills/ris-proj-op-plan-epic-features/SKILL.md) | Existing epic's agreed preliminary graph, safe reconciliation and separate tracker publication |
| [ris-proj-op-suggest-continuation](../skills/ris-proj-op-suggest-continuation/SKILL.md) | Read-only continuation prompt, human decision or exact blocker |
| [ris-proj-op-show-plan](../skills/ris-proj-op-show-plan/SKILL.md) | Complete compact read-only project/ID-subtree plan and one checked next action |
| [ris-proj-op-interview-feature](../skills/ris-proj-op-interview-feature/SKILL.md) | Feature-requirements interview handoff |
| [ris-proj-op-specify-feature](../skills/ris-proj-op-specify-feature/SKILL.md) | Explicit early /2 registration, or accepted published requirements and feature/standalone record |
| [ris-proj-op-design-feature](../skills/ris-proj-op-design-feature/SKILL.md) | Separately accepted published design and record references, or explicit limited contribution |
| [ris-proj-op-decompose-feature](../skills/ris-proj-op-decompose-feature/SKILL.md) | ID-based feature/standalone one-task check or sufficient children and tracker publication |
| [ris-proj-op-prepare-task-worktree](../skills/ris-proj-op-prepare-task-worktree/SKILL.md) | Claim-aware feature-preparation/execution copy/environment handoff |
| [ris-proj-op-implement-task-tdd](../skills/ris-proj-op-implement-task-tdd/SKILL.md) | Claim-aware implementation with mandatory TDD |
| [ris-proj-op-review-task](../skills/ris-proj-op-review-task/SKILL.md) | Checked project-change review with or without ID; one compact local ris.review/2 YAML (existing /1 continued conditionally), with explicit fast no-file exception |
| [ris-proj-op-update-documentation](../skills/ris-proj-op-update-documentation/SKILL.md) | Authorized documentation synchronization |
| [ris-proj-op-publish-task](../skills/ris-proj-op-publish-task/SKILL.md) | Checked change or pre-ID document integration/push from an own branch/worktree; independent review except verified eligible Fast, remote Git and optional safe primary maintenance are separate results |
| [ris-proj-op-complete-container](../skills/ris-proj-op-complete-container/SKILL.md) | Ordinary close/eligibility from closed direct children, explicit substantive verification, or administrative close |
| [ris-proj-op-retrospect-session](../skills/ris-proj-op-retrospect-session/SKILL.md) | Selected OpenCode history plus project evidence |
| [ris-proj-op-manage-okf-bundle](../skills/ris-proj-op-manage-okf-bundle/SKILL.md) | Explicit project/root/scope OKF operation |
| [ris-proj-op-author-architecture-rules](../skills/ris-proj-op-author-architecture-rules/SKILL.md) | Accepted scoped architecture rules in project OKF |
| [ris-proj-op-author-development-rules](../skills/ris-proj-op-author-development-rules/SKILL.md) | Accepted scoped engineering rules in project OKF |
| [ris-proj-op-author-product-foundation](../skills/ris-proj-op-author-product-foundation/SKILL.md) | Separately accepted, saved and checked initial product knowledge in sources.product |
| [ris-proj-flow-initialize-project](../skills/ris-proj-flow-initialize-project/SKILL.md) | Agreed checked local RIS setup, one dialogue, delegated document owners and separately offered publication |
| [ris-proj-flow-prepare-feature](../skills/ris-proj-flow-prepare-feature/SKILL.md) | Early same-ID/copy, unified requirements/design dialogue, precise acceptance, independent review/Git and verified decomposition/tracker publication |
| [ris-proj-flow-execute-task](../skills/ris-proj-flow-execute-task/SKILL.md) | One task's fresh run or safe resume through separate publications |
| [ris-proj-flow-execute-simple-task](../skills/ris-proj-flow-execute-simple-task/SKILL.md) | One bounded request/idea, explicit or natural selection, one main agent/default zero subagents, conditional review, verified Git/local/mixed results and separate tracked completion |
| [ris-proj-flow-fix-bug](../skills/ris-proj-flow-fix-bug/SKILL.md) | Exact native bug admission, necessary separately accepted design, reproducible versioned inputs and complete existing execution route |

## Shared instructions and adapters

| Skill | Result |
| --- | --- |
| [ris-proj-lib-common](../skills/ris-proj-lib-common/SKILL.md) | Shared conditional dialogue, artifact and quality rules |
| [ris-proj-adapter-beads-tasks](../skills/ris-proj-adapter-beads-tasks/SKILL.md) | Bounded Beads tasks, read-only all-work-type plan reads, ordinary bug registration/investigation, execution claim/historical basis read/locator append/separate fix-completion and separately authorized Dolt operations |
| [ris-port-adapter-git-worktrees](../skills/ris-port-adapter-git-worktrees/SKILL.md) | Git worktrees/1 operations |
| [ris-port-adapter-worktrunk-worktrees](../skills/ris-port-adapter-worktrunk-worktrees/SKILL.md) | Explicitly selected Worktrunk worktrees/1 operations |

## Choosing an operation

`roadmap` is the combined planning entry: `epic-only`, default `nearest`, or `all`
feature depth. A single MVP epic with several preliminary features is valid.
Freely structured product sources justify many-to-many coverage; gaps and material
changes need decisions, not new assumed requirements. The lead reconciles isolated
epic proposals before agreement and serial writes. Direct epic-graph planning works
without a subagent; its portable base has no RIS/tracker/harness dependency.
Preliminary features need no spec/design/AC/implementation tasks. Preparation retains
the same ID and real acceptance gates. Implementation uses native blocks; requirements
prerequisites name exact IDs and needed accepted contracts in readable content;
information links never block. Child execution checks parent-feature prerequisites
too. Plans/files/raw closed alone are not acceptance. Replanning preserves all-state
identities, accepted/started/foreign/completed work; no new registry/state machine.

`init` prepares a selected new/existing project **after** package installation;
empty input establishes project/setup scope, never selects work. The flow owns
the justified settings/change set and agreed bootstrap writes, then reapplies
read-only context v2. `project-initialization` maps to an agreed available executor
for actual standalone noninteractive calls; no automatic model, rights or fallback.
Product foundation → architecture → engineering use existing authors, each with
separate exact-content acceptance and scoped save/check, preserving suitable
existing material. Human decisions stay in one leading dialogue; a fresh reviewer
is independent of all authors/fixers. Conditional Git/Beads/tools/agents/recovery
resources retain action-specific authority and read-back. The final result
distinguishes accepted/saved/checked, available tools/executors, deferred operation
limits and remaining work. Missing remote or declined push does not invalidate
checked local readiness: it limits publication, offered separately through the existing
publisher and its gates. Intended publication requires a caller-supplied prepared
own branch/safe copy before initialization writes; otherwise the result remains
local/unpublished, with no promise of late branching or dirty-primary transfer.
Init stops before roadmap/features/development and does
not configure product build/test/format/CI. It is not the installer or a whole-rules
refresh operation. See its complete [contract](../skills/ris-proj-flow-initialize-project/SKILL.md).

`prepare-feature` early-registers the explicitly chosen feature through specify,
then applies the existing task-copy owner with purpose `feature-preparation` before
its first document/draft/decision write. It preserves one exact /2 ID and checked
own path/branch/base, action-specific claim/blocker gates and confirmation-first
recovery. Writers, reviewers and the publisher consume that same checked copy.
Direct `specify-feature`/`design-feature` calls instead require a caller-supplied
prepared own copy before writes intended for publication, or report an explicitly
authorized local/unpublished limitation. The publisher only consumes preparation;
it never creates/switches branches or prepares worktrees. Precise scope acceptance,
independent whole-snapshot review and Git/tracker publication gates remain.

The direct early-registration contribution of `specify-feature` needs only an
explicitly chosen feature, title/goal, stable project key and write authority;
epic/spec/design are optional. It checks/reuses one native task ID with ordinary content,
without document/acceptance/claim effects. The existing task-copy wrapper accepts
that exact ID with purpose `feature-preparation`, preserving action-specific
blockers and all ownership/copy guards before documents. New feature documents use
`sources.specs/<full feature ID>/spec.md`, readable H1 and Feature-ID/Summary/optional
Keywords, with sufficient inline or adjacent design and actual separate acceptance.
No JSON/pin/duplicate refs/readiness registry or mandatory saved verification.
Execution, decomposition and verified completion retain substantive gates; legacy
links/payload hints lead to actual documents without schema refusal or migration.
The full flow composes these
same owners, one requirements/design dialogue and a possible shared acceptance act
with two exact selectors/versions. It publishes reviewed inputs before same-ID
ordinary content reconciliation and applies the existing full decomposition method, in this
session or an executor. Inline sufficient design is a distinct accepted spec section;
design.md/ADR are conditional. Independent review remains a separate context.

Fast admits one small, understood, local-consequence and checkable request/idea,
not product-logic/architecture/material shared-contract changes, coordinated
independent outcomes or broad/unknown effects. Judge consequences/boundaries/checks,
not diff size or extension: code/config/docs/tools/versioned/ignored/external can
qualify. Resolve minor ambiguity here; agree only necessary expansion, not a full
SDLC restart. The main agent applies existing owners (`standard|tdd` as required),
default zero subagents, without mandatory preparation/plan/log/handoff/review files.
Self-check and mandatory checks/TDD remain. Independent review is required by explicit
request, mandatory applicable target-project policy or concretely explained material
risk, not code/external location/Git push alone. General RIS review wording does not
override this exception; inactive review loads no role/format and needs no skip report
or fictional approval. Required `task-review` is actually independent; high/medium need
repair/checks/applicable reassessment. Unavailable required review blocks dependent gates.
RIS keeps short Beads accounting; existing IDs retain native kind, inputs, claim,
composition/blockers, never feature/bug/container downgrade. Versioned edits require
one own branch/dedicated worktree through existing preparers with reuse, not source-folder
development. Local-only uses actual authorized targets without empty copy/dummy Git;
mixed preserves/checks both parts and shared resources separately. Git retains
outgoing/integration/non-force/remote gates; local-only completion needs no Git SHA,
no-change verifies existing state without empty commit/push. Result/exact close/Dolt
remain separate; local files are not pushed by Dolt. Fast ascends actual parents inline,
full/bug retains fresh delegation. Resume reconciles real effects using the same ID/copy,
does not replay confirmed push/close or require absent inapplicable review; changed
subjects get affected self-check/risk assessment and independent review when required.
Full/feature/bug/direct-review/non-Fast publisher gates remain unchanged.

Portable operations take supplied inputs; project operations add the applicable
context, rules, paths and persistence. The RIS skill author composes the portable
author; neither installs its output without separate authorization.

Feature preparation ends at verified sufficient one-task or multi-task decomposition
and separate tracker publication, without implementation. Direct decomposition
remains available for already accepted published inputs or its bounded continuation.
Bug registration preserves a message before investigation, checks all-status
duplicates and stops at a verified ID. It does not confirm a defect or start
investigation/fixing; those are separately requested results. No bug slash command
is added to the compact menu.
Investigation applies the portable method, separates confirmation from readiness,
and stops at a checked current report/criteria or precise unsaved remainder. Its
default is a delimited description section; required file storage uses an exact
published `investigation.md` locator, not competing full copies or local-only notes.
Baseline Beads has no general content CAS: unsupported required protection blocks
report/acceptance replacement while independent diagnosis remains useful. Lack of
evidence never closes a bug; proved correct/duplicate disposition saves rationale
and separately verifies exact closure, with useful-original transfer and a typed
nonblocking relation for duplicates. Investigation does not launch a fix.
The fix flow takes the exact native bug ID and sufficient saved report/criteria/
accepted constraints, not a mandatory separate spec/design pair. Material design
uses the existing design owner and actual separate acceptance. Before execution,
the adapter verifies full used historical report/criteria/decision fields at the
exact tracker version and consumers read used immutable Git sources/decisions.
A short ordinary locator enables project+ID discovery; no duplicate full snapshot,
new file or copied text handoff is required. Missing/incomplete history blocks
dependent work. Material drift requires targeted reassessment and a new locator,
not rewriting old snapshots or replaying published/closed effects. The complete existing
execute-task route retains copy/claim, roles, code TDD, independent review, Git,
separate real fix-completion and tracker publication; disposition is different.
Full task/bug execution starts directly from sufficient accepted inputs/current
code. No standalone planner, saved plan/omission-decision or implementation report
is required. Old plans remain optional history; author TDD remains required without
a saved cycle-history audit. Review assesses the final result and current checks.
See [integrated delivery checks](specs/local-bugfix/delivery-checks.md) for coverage
and revision/evidence limits, rather than inferring live reliability from contracts.
Requirements and design have independently sufficient direct/inherited/mixed
basis under common's published-inputs owner: checked original source decisions,
versions, applicability and actual derivation, not compatibility alone. Wholly
inherited content needs no new approval/acceptor; mixed content needs decisions
only on new material in the full candidate context. Preserve original provenance
and existing inputs without schema/sidecar/registry or migration. Task execution preserves an
explicit target; without an ID it reconciles confirmed own unfinished work before
ready-task selection. The continuation operation recommends a next step read-only.

The plan overview (`/risp-status`, optionally with an exact ID) shows every unclosed
working record once, with actual parents and directed blockers; standalone work is
separate. Closed/all progress counts direct children, not fulfilled criteria. Feature
references and checked acceptance remain distinct. The tree is a lightweight tracker
read; only the one recommendation gets necessary source/decision/owner inspection
through the continuation operation. Started work is considered first. Missing data,
partial reads or an unavailable installed command are explicit gaps, never invented
readiness. The overview saves nothing, claims nothing and launches no next action.

Portable implementation defaults to standard unless TDD is required; the project
TDD operation requires observed RED before behavior changes and GREEN after.
Text-only work uses substantive document checks. Self-review is not independent
publication approval. Git publication, task completion, parent acceptance and Dolt
publication remain distinct effects.

Project review and Git publication also accept a sufficient agreed bounded request
without an ID: supply its authority, criteria/constraints, exact copy/branch/base
and complete candidate, checks and review purpose. No spec/design/plan file is
inherently required; project-required tracking still applies. Ordinary project
review saves one local `review.yaml` under the [format owner](../skills/ris-proj-op-review-task/references/report-format.md),
with complete rounds, exact Git subject and actual independence provenance.
No-ID save needs an explicit local path. Beads keeps only address/round, not copied
verdict/findings; another machine is not promised access. Eligible Fast review is
conditional as above; when active it permits
sufficient independent session-only review; optional save uses the same format.
Review uses the portable assessment method; actual independence belongs to its
caller. Structural validity is separate from current subject/input/check approval
applicability; later adverse/unknown rounds cannot be bypassed by old approval.
Publication requires independent review of the complete snapshot except the publisher's
verified eligible Fast no-review branch; arbitrary caller waiver and direct publication
do not disable review. Versioned work always needs an already prepared own branch and
dedicated worktree, whole outgoing authority and remote confirmation.
The ordinary Beads task may preserve the accepted self-contained request instead
of artificial specification links; supplied feature/bug contracts remain strict.

Ordinary container close/eligibility checks a complete nonempty set of direct
children (all closed) and parent blockers, trusting child completion without a
recursive acceptance/Git/review or decomposition audit. Eligibility is read-only;
closure uses native exact guards/read-back and separate tracker publication.
This is not fresh whole-result acceptance. Zero-child features retain own-result
verification. Container requests also distinguish administrative close by explicit decision from
read-only verification and verify-and-close. Administrative `closed` is not
independent acceptance and leaves feature verification untouched; it needs no
new delivery reconstruction, Git evidence or verification persistence. Native
child/blocker restrictions and status read-back remain. Verification reports
fulfilled / unfulfilled / insufficient-data without closing or publishing by
default. Execution of a selected one-task feature still requires full verified
completion. Confirmed closure is never repeated for pending publication.

Both OKF operations require an explicitly selected bundle; ordinary feature
Markdown is not automatically OKF. Project architecture/development rule authors
own accepted content; their portable counterparts return proposals.

The product-foundation pair follows the same content/format boundary: the portable
owner researches materials and conditionally applies the existing interview; the
project author owns separate acceptance, scoped OKF persistence and read-back.
It covers purpose, users, tasks, capabilities, boundaries, constraints and unknown
impact, not full product design. Suitable existing structure and decisions are
reused; proposal-only/refusal/no acceptance writes no product files. Neither
author runs initialization, selects a next skill or starts roadmap/development.
These are directly loadable contracts without additional slash commands.

Worktree preparation reports working-copy and environment readiness separately.
Git is the default worktree adapter; having Worktrunk installed does not select it.
The ris-17f candidate streamlines ordinary create and makes preservation details
conditional on reuse or hooks/setup. Preparation and full task execution need no
`worktree.md`, `execution.md` or substitute transition ledger; independent
review and sufficient tracker result remain, without a replacement implementation log. A valid unused config
difference does not block preparation; tracker identity and used paths still gate
the dependent handoff. See [delivery checks](specs/worktree-preparation-simplification/delivery-checks.md)
for the pending-review/integration snapshot and static evidence limits.
Implementation consumes the supplied copy and checks fresh claim/blocker gates.
Consult the linked skills for shared-root provenance and source-version checks.

For a retrospective without an ID/export, the project operation follows its
permitted session-list-and-selection procedure. It returns a response by default;
saving requires an explicit authorized destination.
The reader supports the OpenCode V2 client/server transcript contract (baseline
2.0.32) and legacy 1.18.33 exports. V2 reads use the authenticated standard client,
body-cursor pagination and confirmed `subagent` child links. Projected/unsettled
history and unknown usage semantics remain explicit limitations; the portable
analysis method is client-independent. See the owned
[OpenCode reader reference](../skills/ris-proj-op-retrospect-session/references/opencode.md).
