# RIS skill and command namespace transition

This is the coordinated, incompatible v1/D1 namespace migration. The source in
this change branch is pending independent review and publication. Select the
actual published package revision when distributing it; the base or accepted
design commit alone does not contain the migrated package. No aliases remain.
Accepted specifications, decisions, immutable URLs and old delivery reports keep
their original identifiers and revisions; this guide translates historical
addresses for current use without repinning acceptance.

## Complete skill replacement map — 41

The new identifier is both the source/installed folder and frontmatter `name`.
Every op/flow additionally has the slash command `/` + that exact identifier.
There are 35 op, 2 flow, 1 lib and 3 adapters: 41 skills and 37 commands.

| Retired skill | Current skill |
| --- | --- |
| `ris-author-skills-base` | `ris-port-op-author-skill` |
| `ris-interview-base` | `ris-port-op-interview` |
| `ris-formulate-spec-base` | `ris-port-op-formulate-feature-spec` |
| `ris-design-feature-base` | `ris-port-op-design-feature` |
| `ris-decompose-spec-base` | `ris-port-op-decompose-feature-spec` |
| `ris-plan-roadmap-base` | `ris-port-op-plan-roadmap` |
| `ris-plan-task-base` | `ris-port-op-plan-task` |
| `ris-prepare-worktree-base` | `ris-port-op-prepare-worktree` |
| `ris-implement-base` | `ris-port-op-implement-change` |
| `ris-review-base` | `ris-port-op-review-change` |
| `ris-retrospect-session-base` | `ris-port-op-retrospect-session` |
| `ris-verify-feature-base` | `ris-port-op-verify-feature` |
| `ris-formulate-architecture-rules-base` | `ris-port-op-formulate-architecture-rules` |
| `ris-formulate-development-rules-base` | `ris-port-op-formulate-development-rules` |
| `ris-okf-base` | `ris-port-op-manage-okf-bundle` |
| `ris-author-skills` | `ris-proj-op-author-skill` |
| `ris-context` | `ris-proj-op-resolve-context` |
| `ris-plan-roadmap` | `ris-proj-op-plan-roadmap` |
| `ris-plan-epic` | `ris-proj-op-refine-epic` |
| `ris-select-next-feature` | `ris-proj-op-select-feature` |
| `ris-interview-feature` | `ris-proj-op-interview-feature` |
| `ris-specify-feature` | `ris-proj-op-specify-feature` |
| `ris-design-feature` | `ris-proj-op-design-feature` |
| `ris-decompose-feature` | `ris-proj-op-decompose-feature` |
| `ris-prepare-task-worktree` | `ris-proj-op-prepare-task-worktree` |
| `ris-plan-task` | `ris-proj-op-plan-task` |
| `ris-tdd-implement-task` | `ris-proj-op-implement-task-tdd` |
| `ris-review` | `ris-proj-op-review-task` |
| `ris-update-documentation` | `ris-proj-op-update-documentation` |
| `ris-publish-main` | `ris-proj-op-publish-task` |
| `ris-complete-container` | `ris-proj-op-complete-container` |
| `ris-retrospect-session` | `ris-proj-op-retrospect-session` |
| `ris-okf` | `ris-proj-op-manage-okf-bundle` |
| `ris-author-architecture-rules` | `ris-proj-op-author-architecture-rules` |
| `ris-author-development-rules` | `ris-proj-op-author-development-rules` |
| `ris-prepare-feature-work` | `ris-proj-flow-prepare-feature` |
| `ris-execute-task` | `ris-proj-flow-execute-task` |
| `ris-common` | `ris-proj-lib-common` |
| `ris-beads-adapter` | `ris-proj-adapter-beads-tasks` |
| `ris-git-worktree-adapter` | `ris-port-adapter-git-worktrees` |
| `ris-worktrunk-adapter` | `ris-port-adapter-worktrunk-worktrees` |

## Complete retired command map — eight

| Retired command | Explicit replacement |
| --- | --- |
| `/ris-author` | `/ris-port-op-author-skill` for autonomous source; `/ris-proj-op-author-skill` for RIS-integrated source |
| `/ris-plan-roadmap` | `/ris-proj-op-plan-roadmap` |
| `/ris-next` | `/ris-proj-op-select-feature` |
| `/ris-interview` | `/ris-port-op-interview` |
| `/ris-interview-feature` | `/ris-proj-op-interview-feature` |
| `/ris-prepare-feature-work` | `/ris-proj-flow-prepare-feature` |
| `/ris-execute-task` | `/ris-proj-flow-execute-task` |
| `/ris-retrospect-session` | `/ris-proj-op-retrospect-session` |

The author command is split into two explicit entries. Templates do not inspect
`ris.yaml` to choose a contract. The project author's existing autonomous-request
guard remains part of its skill. Adapter/library operations remain available as
skills under their original permission contracts, without command facades.

## Update an independently selected target project

1. Establish the **target project root independently** of the RIS source or
   installed skill location. Identify its actual OpenCode discovery directories,
   applicable project instructions and authorization. This guide changes no
   external project merely by being saved or read.
2. Choose **one actual package revision** (published commit/tag) and record the
   resolved full commit. Take both `skills/` and `commands/opencode/` from that
   same revision. Inspect the real package inventory against this map; a later
   revision with additional accepted components needs its corresponding inventory,
   not blind enforcement of an eternal count of 41.
3. Inspect existing target installations, shadowing/global copies, resources,
   permissions/modes, symlinks, client config and foreign files before replacement.
   Identify ownership of retired names and any local edits. Preserve a recoverable
   baseline of the previous coherent package and consumers. Preserve foreign
   `grilling`, `grillme` and client configuration; do not recursively clean a
   discovery root. Before removing an older empty `ris-beads-tech`,
   `ris-implement-task` or `ris-project-okf` remnant, verify its ownership and
   physical emptiness including symlinks; unexpected contents need reconciliation.
4. Change **active** callers, AGENTS pointers, dependency/resource addresses,
   examples and explicit configuration selection to the new names. In a target
   using the Beads adapter, set `adapters.tasks.skill` to
   `ris-proj-adapter-beads-tasks`. Preserve other values, schema version 2,
   execution role IDs, agent names and primary/shared-root semantics. A name or
   source location does not choose a project root or grant write permission.
   Coordinate impacts to active task inputs with their owners; do not mass-edit
   accepted snapshots, closed records, reports or immutable references.
5. Replace each package-owned skill folder **completely**, including references,
   assets, scripts, file types and modes. Install all 37 same-name op/flow command
   templates from `commands/opencode/`. For the usual project-local layout these
   go to `.opencode/skills/<name>/` and `.opencode/command/<name>.md` beneath the
   selected target, not beneath the RIS source repository by assumption.
6. Remove all 41 retired skill folders and all eight retired command files in
   the updated installation, after checking their ownership and preserving the
   agreed baseline. Overlaying the new files while leaving old discoverable
   aliases is an incomplete migration. No installer or management command is
   supplied here; the separately accepted installer/N1 remains future work.
7. Compare the full installed package against the selected source revision by
   relative paths, bytes, types and modes, including all resources. Verify folder
   equals frontmatter name, unique valid identifiers (at most 64 characters),
   nonempty descriptions, 37 command basenames equal the op/flow set, exactly one
   same-name skill load and `$ARGUMENTS` per template, and no lib/adapter commands.
   Check active links/config/owner-relative resources and removal of retired
   physical paths. Compare foreign/client material with its preserved baseline.
8. Quit and **restart OpenCode** after the complete replacement. An existing
   session keeps its already-loaded configuration/skills. Static file checks do
   not prove runtime discovery or compatibility with untested client versions.

## Partial failure and recovery

Filesystem replacement is not an atomic transaction. On any failure, stop the
dependent transition and inspect actual effects before retrying. Report the exact
source revision, target root, files/folders replaced, old entries still present,
missing resources/commands, consumer edits already made, modes/type mismatches,
foreign changes and the operation/error. Do not call a mixed installation ready.
Use the recorded baseline to either complete only the missing parts of the same
coherent revision or restore the previous coherent package **and its consumers**.
Do not overwrite new foreign changes during recovery or silently select another
revision. Recheck the entire composition and preservation evidence before restart.

## Preserved contracts and historical material

This migration changes identifiers and thin entry points, not algorithms, tool
permissions or conditional resource-loading rules. Empty arguments still follow
each skill's existing behavior: interview asks its topic, project feature interview
asks its feature, feature preparation establishes scope, task execution reconciles
own unfinished work/autoselects and safely resumes, and project retrospective uses
permitted session listing/selection. No universal empty-input refusal is added.

Historical `-base`/`-tech` conventions and future component proposals in the
concepts catalog are explicitly historical, not current installation instructions.
Accepted specs/designs/decisions and delivery/test snapshots retain old paths as
evidence of their original revision; retrieve those original revisions for exact
historical bytes. They are not aliases in the migrated installation. The pinned
OKF snapshot/attribution and retrospective reader algorithms move intact. Renaming
does not renew past approvals, behavioral evidence or containing-commit decisions.
