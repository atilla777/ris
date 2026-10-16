# Skills and commands

RIS includes portable operations, project-integrated operations, two workflows,
shared instructions and tool adapters. Each linked `SKILL.md` defines its actual
inputs, dependencies, permissions, checks and stopping point.

All 43 skills are listed below, independently of the compact 18-command menu.
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
For older names, use the
[namespace transition guide](skill-command-naming-migration.md); there are no aliases.

## Compact command menu — 18

| Command | Exact skill target |
| --- | --- |
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
| `/risp-review-task` | `ris-proj-op-review-task` |
| `/risp-publish-task` | `ris-proj-op-publish-task` |
| `/risp-complete-container` | `ris-proj-op-complete-container` |
| `/risp-retro` | `ris-proj-op-retrospect-session` |
| `/risb-interview` | `ris-port-op-interview` |
| `/risb-review-change` | `ris-port-op-review-change` |
| `/risb-skill` | `ris-port-op-author-skill` |
| `/risb-installation` | `ris-port-op-manage-installation` |

`next` recommends; `select-feature` chooses a feature; `run-task` executes one
authorized task. `skill` authors autonomous source, without selecting the RIS
author or installing it. Empty inputs, permissions, recovery and stopping points
remain those of each linked owner. No aliases are shipped.

### Explicit calls without a slash command

Ask the agent to load the exact skill with its skill tool and supply the inputs:

```text
Load ris-proj-op-author-skill and improve the RIS-integrated skill at <source folder> within <accepted scope>; do not install it.
Load ris-proj-op-implement-task-tdd for <ID> in <project/copy>, actor <actor>, within the accepted plan and permissions.
Load ris-proj-op-update-documentation for <project/copy>, inspected change <snapshot>, authorized documents <paths>.
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
| [ris-port-op-manage-okf-bundle](../skills/ris-port-op-manage-okf-bundle/SKILL.md) | Explicit-root autonomous OKF read/create/edit/check |
| [ris-port-op-manage-installation](../skills/ris-port-op-manage-installation/SKILL.md) | Checked full-package install/update/uninstall |

## Project operations and workflows

| Skill | Result |
| --- | --- |
| [ris-proj-op-author-skill](../skills/ris-proj-op-author-skill/SKILL.md) | Combined RIS skill authoring |
| [ris-proj-op-resolve-context](../skills/ris-proj-op-resolve-context/SKILL.md) | Read-only project configuration/path preparation |
| [ris-proj-op-plan-roadmap](../skills/ris-proj-op-plan-roadmap/SKILL.md) | Project roadmap and authorized tracker persistence |
| [ris-proj-op-refine-epic](../skills/ris-proj-op-refine-epic/SKILL.md) | One unclear epic's outcome and boundaries |
| [ris-proj-op-select-feature](../skills/ris-proj-op-select-feature/SKILL.md) | Read-only next-feature recommendation |
| [ris-proj-op-suggest-continuation](../skills/ris-proj-op-suggest-continuation/SKILL.md) | Read-only continuation prompt, human decision or exact blocker |
| [ris-proj-op-interview-feature](../skills/ris-proj-op-interview-feature/SKILL.md) | Feature-requirements interview handoff |
| [ris-proj-op-specify-feature](../skills/ris-proj-op-specify-feature/SKILL.md) | Accepted published requirements and feature/standalone record, or explicit limited contribution |
| [ris-proj-op-design-feature](../skills/ris-proj-op-design-feature/SKILL.md) | Separately accepted published design and record references, or explicit limited contribution |
| [ris-proj-op-decompose-feature](../skills/ris-proj-op-decompose-feature/SKILL.md) | ID-based feature/standalone one-task check or sufficient children and tracker publication |
| [ris-proj-op-prepare-task-worktree](../skills/ris-proj-op-prepare-task-worktree/SKILL.md) | Claim-aware working-copy/environment handoff |
| [ris-proj-op-plan-task](../skills/ris-proj-op-plan-task/SKILL.md) | Verified saved task plan |
| [ris-proj-op-implement-task-tdd](../skills/ris-proj-op-implement-task-tdd/SKILL.md) | Claim-aware implementation with mandatory TDD |
| [ris-proj-op-review-task](../skills/ris-proj-op-review-task/SKILL.md) | Checked project review, saved when authorized |
| [ris-proj-op-update-documentation](../skills/ris-proj-op-update-documentation/SKILL.md) | Authorized documentation synchronization |
| [ris-proj-op-publish-task](../skills/ris-proj-op-publish-task/SKILL.md) | Reviewed task/change or pre-ID document integration and verified Git push |
| [ris-proj-op-complete-container](../skills/ris-proj-op-complete-container/SKILL.md) | Explicit verified feature/standalone-container/epic closure |
| [ris-proj-op-retrospect-session](../skills/ris-proj-op-retrospect-session/SKILL.md) | Selected OpenCode history plus project evidence |
| [ris-proj-op-manage-okf-bundle](../skills/ris-proj-op-manage-okf-bundle/SKILL.md) | Explicit project/root/scope OKF operation |
| [ris-proj-op-author-architecture-rules](../skills/ris-proj-op-author-architecture-rules/SKILL.md) | Accepted scoped architecture rules in project OKF |
| [ris-proj-op-author-development-rules](../skills/ris-proj-op-author-development-rules/SKILL.md) | Accepted scoped engineering rules in project OKF |
| [ris-proj-flow-prepare-feature](../skills/ris-proj-flow-prepare-feature/SKILL.md) | Feature choice through accepted published inputs to verified ID |
| [ris-proj-flow-execute-task](../skills/ris-proj-flow-execute-task/SKILL.md) | One task's fresh run or safe resume through separate publications |

## Shared instructions and adapters

| Skill | Result |
| --- | --- |
| [ris-proj-lib-common](../skills/ris-proj-lib-common/SKILL.md) | Shared conditional dialogue, artifact and quality rules |
| [ris-proj-adapter-beads-tasks](../skills/ris-proj-adapter-beads-tasks/SKILL.md) | Bounded Beads tasks and separately authorized Dolt operations |
| [ris-port-adapter-git-worktrees](../skills/ris-port-adapter-git-worktrees/SKILL.md) | Git worktrees/1 operations |
| [ris-port-adapter-worktrunk-worktrees](../skills/ris-port-adapter-worktrunk-worktrees/SKILL.md) | Explicitly selected Worktrunk worktrees/1 operations |

## Choosing an operation

Portable operations take supplied inputs; project operations add the applicable
context, rules, paths and persistence. The RIS skill author composes the portable
author; neither installs its output without separate authorization.

Feature preparation ends at the published feature ID; decomposition is separate.
Requirements and design have separate acceptance. Task execution preserves an
explicit target; without an ID it reconciles confirmed own unfinished work before
ready-task selection. The continuation operation recommends a next step read-only.

Portable implementation defaults to standard unless TDD is required; the project
TDD operation requires observed RED before behavior changes and GREEN after.
Text-only work uses substantive document checks. Self-review is not independent
publication approval. Git publication, task completion, parent acceptance and Dolt
publication remain distinct effects.

Both OKF operations require an explicitly selected bundle; ordinary feature
Markdown is not automatically OKF. Project architecture/development rule authors
own accepted content; their portable counterparts return proposals.

Worktree preparation reports working-copy and environment readiness separately.
Git is the default worktree adapter; having Worktrunk installed does not select it.
Planning consumes the supplied copy without creating it or requiring a claim.
Consult the linked skills for shared-root provenance and source-version checks.

For a retrospective without an ID/export, the project operation follows its
permitted session-list-and-selection procedure. It returns a response by default;
saving requires an explicit authorized destination.
