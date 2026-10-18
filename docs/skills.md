# Skills and commands

RIS includes portable operations, project-integrated operations, five workflows,
shared instructions and tool adapters. Each linked `SKILL.md` defines its actual
inputs, dependencies, permissions, checks and stopping point.

All 53 source skills are listed below, independently of the 22-command menu.
Only selected operations/workflows have slash commands. Command sources live in
[`commands/opencode/`](../commands/opencode/); each explicitly loads one skill
and passes `$ARGUMENTS` through its existing contract.

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
The single accepted exception is `/ris-help` → `ris-proj-op-show-help`, without
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
**22 entries (17 project + 4 portable + one help exception)**;
availability in a project requires installation
of the chosen package and client restart.

| Command | Exact skill target |
| --- | --- |
| `/risp-init` | `ris-proj-flow-initialize-project` |
| `/ris-help` | `ris-proj-op-show-help` |
| `/risp-status` | `ris-proj-op-show-plan` |
| `/risp-next` | `ris-proj-op-suggest-continuation` |
| `/risp-roadmap` | `ris-proj-op-plan-roadmap` |
| `/risp-refine-epic` | `ris-proj-op-refine-epic` |
| `/risp-select-feature` | `ris-proj-op-select-feature` |
| `/risp-prepare-feature` | `ris-proj-flow-prepare-feature` |
| `/risp-specify-feature` | `ris-proj-op-specify-feature` |
| `/risp-design-feature` | `ris-proj-op-design-feature` |
| `/risp-decompose-feature` | `ris-proj-op-decompose-feature` |
| `/risp-plan-task` | `ris-proj-op-plan-task` |
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
`next` recommends for an already selected subject; `select-feature` chooses a feature; `run-task` executes one
authorized task. `skill` authors autonomous source, without selecting the RIS
author or installing it. Empty inputs, permissions, recovery and stopping points
remain those of each linked owner. No aliases are shipped.

`run-simple-task` executes only already assigned clear bounded work, with an
optional existing ID; empty input asks for the request, never chooses the queue.
It adds one entry under the [D2 menu amendment](specs/compact-commands/spec.md#8-поправка-fast-task-execution-d2--один-новый-вход).

`/ris-help` immediately returns daily Markdown help on empty/simple input:
status/next, feature preparation/decomposition and task execution. `/ris-help full`
(`/ris-help полный` in Russian) returns detailed thematic pages with separate
operation blocks, including installation/init, roadmap, individual task stages,
bugs, acceptance and retrospective. A named command, comparison or intent still
yields focused short help, never execution. There are no new slash commands or
mandatory pager calls, and no fixed 80×24 layout.
Its installed resources cover all user-facing methods, not internal menus.
No `ris.yaml`, Beads, source checkout or project setup is required. One RIS-specific
skill suffices because the subject is RIS itself; no artificial portable pair.
It preserves common/context ownership, zero-write/zero-launch limits and the
boundary with actual-work `next`/`status`. Source readiness does not confirm client
discovery or live behavior.

`select-feature` and `next` recommend a direction or owner from minimum sufficient
facts; they do not certify execution readiness. A selected ID uses bounded reads,
while no-ID feature selection discovers compact suitable epics. Relevant started
work and known material blockers/conflicts matter; history, composition, acceptance
and publication evidence expand only when they can change the recommendation.
Unknown facts stay explicit. The executing owner checks current readiness,
acceptance, ownership and permissions; navigation writes nothing and launches nothing.

### Explicit calls without a slash command

Ask the agent to load the exact skill with its skill tool and supply the inputs:

```text
Load ris-proj-op-author-skill and improve the RIS-integrated skill at <source folder> within <accepted scope>; do not install it.
Load ris-proj-op-register-bug for <project>: <message and available context>; record this unconfirmed report and return its ID without investigation.
Load ris-proj-op-investigate-bug for <exact bug ID> in <project>, research/write scope <scope>; save the investigation and stop before fixing.
Load ris-port-op-investigate-bug with <message, expectation sources, code/version, evidence and allowed research scope>; return a report without tracker writes.
Load ris-proj-flow-fix-bug for <exact native bug ID> in <project>, actor <actor>, within <authorized fix/publication scope>; use the saved sufficient report and existing execution route.
Load ris-proj-op-implement-task-tdd for <ID> in <project/copy>, actor <actor>, within the accepted plan and permissions.
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
| [ris-port-op-plan-task](../skills/ris-port-op-plan-task/SKILL.md) | Technical task plan |
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
| [ris-proj-op-show-help](../skills/ris-proj-op-show-help/SKILL.md) | Read-only daily SDLC help, full thematic pages, command cards, comparisons and intent routes, without project setup |
| [ris-proj-op-resolve-context](../skills/ris-proj-op-resolve-context/SKILL.md) | Read-only project configuration/path preparation |
| [ris-proj-op-register-bug](../skills/ris-proj-op-register-bug/SKILL.md) | Unconfirmed bug registration or safe original supplementation, verified ID and stop |
| [ris-proj-op-investigate-bug](../skills/ris-proj-op-investigate-bug/SKILL.md) | Exact-ID investigation, protected current report/criteria and justified message disposition |
| [ris-proj-op-plan-roadmap](../skills/ris-proj-op-plan-roadmap/SKILL.md) | Project roadmap and authorized tracker persistence |
| [ris-proj-op-refine-epic](../skills/ris-proj-op-refine-epic/SKILL.md) | One unclear epic's outcome and boundaries |
| [ris-proj-op-select-feature](../skills/ris-proj-op-select-feature/SKILL.md) | Read-only next-feature recommendation |
| [ris-proj-op-suggest-continuation](../skills/ris-proj-op-suggest-continuation/SKILL.md) | Read-only continuation prompt, human decision or exact blocker |
| [ris-proj-op-show-plan](../skills/ris-proj-op-show-plan/SKILL.md) | Complete compact read-only project/ID-subtree plan and one checked next action |
| [ris-proj-op-interview-feature](../skills/ris-proj-op-interview-feature/SKILL.md) | Feature-requirements interview handoff |
| [ris-proj-op-specify-feature](../skills/ris-proj-op-specify-feature/SKILL.md) | Accepted published requirements and feature/standalone record, or explicit limited contribution |
| [ris-proj-op-design-feature](../skills/ris-proj-op-design-feature/SKILL.md) | Separately accepted published design and record references, or explicit limited contribution |
| [ris-proj-op-decompose-feature](../skills/ris-proj-op-decompose-feature/SKILL.md) | ID-based feature/standalone one-task check or sufficient children and tracker publication |
| [ris-proj-op-prepare-task-worktree](../skills/ris-proj-op-prepare-task-worktree/SKILL.md) | Claim-aware working-copy/environment handoff |
| [ris-proj-op-plan-task](../skills/ris-proj-op-plan-task/SKILL.md) | Verified saved task plan |
| [ris-proj-op-implement-task-tdd](../skills/ris-proj-op-implement-task-tdd/SKILL.md) | Claim-aware implementation with mandatory TDD |
| [ris-proj-op-review-task](../skills/ris-proj-op-review-task/SKILL.md) | Checked project-change review with or without ID; response-only where rules permit, saved when required and authorized |
| [ris-proj-op-update-documentation](../skills/ris-proj-op-update-documentation/SKILL.md) | Authorized documentation synchronization |
| [ris-proj-op-publish-task](../skills/ris-proj-op-publish-task/SKILL.md) | Reviewed project change with optional ID, or pre-ID document integration and verified Git push from a confirmed own branch |
| [ris-proj-op-complete-container](../skills/ris-proj-op-complete-container/SKILL.md) | Administrative exact-container close, read-only fulfillment verification, or verify-and-close on success |
| [ris-proj-op-retrospect-session](../skills/ris-proj-op-retrospect-session/SKILL.md) | Selected OpenCode history plus project evidence |
| [ris-proj-op-manage-okf-bundle](../skills/ris-proj-op-manage-okf-bundle/SKILL.md) | Explicit project/root/scope OKF operation |
| [ris-proj-op-author-architecture-rules](../skills/ris-proj-op-author-architecture-rules/SKILL.md) | Accepted scoped architecture rules in project OKF |
| [ris-proj-op-author-development-rules](../skills/ris-proj-op-author-development-rules/SKILL.md) | Accepted scoped engineering rules in project OKF |
| [ris-proj-op-author-product-foundation](../skills/ris-proj-op-author-product-foundation/SKILL.md) | Separately accepted, saved and checked initial product knowledge in sources.product |
| [ris-proj-flow-initialize-project](../skills/ris-proj-flow-initialize-project/SKILL.md) | Agreed checked local RIS setup, one dialogue, delegated document owners and separately offered publication |
| [ris-proj-flow-prepare-feature](../skills/ris-proj-flow-prepare-feature/SKILL.md) | Feature choice through accepted published inputs to verified ID |
| [ris-proj-flow-execute-task](../skills/ris-proj-flow-execute-task/SKILL.md) | One task's fresh run or safe resume through separate publications |
| [ris-proj-flow-execute-simple-task](../skills/ris-proj-flow-execute-simple-task/SKILL.md) | One clear assigned request, optional ID, proportionate checks, independent subagent review and verified direct push; separate tracker completion when used |
| [ris-proj-flow-fix-bug](../skills/ris-proj-flow-fix-bug/SKILL.md) | Exact native bug admission, necessary separately accepted design, full input snapshot and complete existing execution route |

## Shared instructions and adapters

| Skill | Result |
| --- | --- |
| [ris-proj-lib-common](../skills/ris-proj-lib-common/SKILL.md) | Shared conditional dialogue, artifact and quality rules |
| [ris-proj-adapter-beads-tasks](../skills/ris-proj-adapter-beads-tasks/SKILL.md) | Bounded Beads tasks, read-only all-work-type plan reads, ordinary bug registration/investigation, execution claim/full notes snapshot/separate fix-completion and separately authorized Dolt operations |
| [ris-port-adapter-git-worktrees](../skills/ris-port-adapter-git-worktrees/SKILL.md) | Git worktrees/1 operations |
| [ris-port-adapter-worktrunk-worktrees](../skills/ris-port-adapter-worktrunk-worktrees/SKILL.md) | Explicitly selected Worktrunk worktrees/1 operations |

## Choosing an operation

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
publisher and its gates. Init stops before roadmap/features/development and does
not configure product build/test/format/CI. It is not the installer or a whole-rules
refresh operation. See its complete [contract](../skills/ris-proj-flow-initialize-project/SKILL.md).

For simple assigned work, `run-simple-task` judges clarity, consequences and
checkability rather than diff size. The main agent applies portable implementation
(`standard|tdd` as required), documentation and the existing publisher; only
`task-review` must actually launch independently. No mandatory plan/log/review files
by default: sufficient evidence stays in the session, plus short tracker accounting
when used. RIS explicitly keeps mandatory short Beads accounting. Existing IDs
retain type, accepted inputs, ownership, composition and blocker gates. A verified
own branch in a suitable current copy is allowed; isolation/rules activate existing
worktree owners. Material decisions stop dependent work for targeted acceptance;
resume reconciles actual effects and repeats missing/inapplicable independent review.
PR-only, forbidden push or missing mandatory checks/review block publication.
This fast-only exception preserves full task/bug/feature and direct plan-task/TDD
contracts; verified Git, result persistence, exact close and tracker publication
remain separate effects.

Portable operations take supplied inputs; project operations add the applicable
context, rules, paths and persistence. The RIS skill author composes the portable
author; neither installs its output without separate authorization.

Feature preparation ends at the published feature ID; decomposition is separate.
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
the full report, criteria and accepted decisions are preserved in an addressable
historical notes snapshot; consumers identify it and reassess affected evidence
on material report drift. It is not a second current report. The complete existing
execute-task route retains copy/claim, roles, code TDD, independent review, Git,
separate real fix-completion and tracker publication; disposition is different.
Saved plans are conditional on project rules or implementation/handoff sufficiency;
RIS keeps its mandatory local plan and direct plan-task persists its own result.
See [integrated delivery checks](specs/local-bugfix/delivery-checks.md) for coverage
and revision/evidence limits, rather than inferring live reliability from contracts.
Requirements and design have separate acceptance. Task execution preserves an
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
and complete candidate, checks and review purpose. No spec/design/plan/report file
is inherently required; project-required tracking and saving still apply. Review
uses the portable assessment method; actual independence belongs to its caller.
Publication requires independent review of the complete snapshot, an already
prepared own branch and a safe copy (current copy where suitable, separate worktree
when isolation/rules require), whole outgoing authority and remote confirmation.
The ordinary Beads task may preserve the accepted self-contained request instead
of artificial specification links; supplied feature/bug contracts remain strict.

Container requests distinguish administrative close by explicit decision from
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
`worktree.md`, `execution.md` or substitute transition ledger; project-required
plan, progress/result, review and tracker result remain. A valid unused config
difference does not block preparation; tracker identity and used paths still gate
the dependent handoff. See [delivery checks](specs/worktree-preparation-simplification/delivery-checks.md)
for the pending-review/integration snapshot and static evidence limits.
Planning consumes the supplied copy without creating it or requiring a claim.
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
