# RIS skill and command namespace transition

The historical [compact-commands v1 map](specs/compact-commands/spec.md) contains
18 explicit slash entries, 14 `risp-` project contracts and four `risb-` portable
contracts. All 43 baseline technical skill identities/resources remain; the
additional `ris-proj-op-register-bug` is directly loadable without a new command.
The current menu extends that accepted baseline with `/risp-status` targeting
`ris-proj-op-show-plan`, under [plan-status D1](specs/plan-status/design.md#8-поставка-и-совместимость).
It returns a read-only project/ID-subtree overview and one checked recommendation,
without claiming or executing work. See the current source inventory in the
[catalog](skills.md); source availability does not prove installation.
The [accepted fast D2 amendment](specs/compact-commands/spec.md#8-поправка-fast-task-execution-d2--один-новый-вход)
also adds `/risp-run-simple-task` → `ris-proj-flow-execute-simple-task` for already
assigned simple work (empty input asks for the request, never selects the queue).
The [workflow-help requirements](specs/workflow-help/spec.md) add the sole naming
exception `/ris-help` → `ris-proj-op-show-help`, without aliases. Empty input shows
one compact SDLC map; cards/comparisons/routes are conditional and read-only,
without config/tracker/source-checkout prerequisites. Actual work stays with
`next`/`status` and execution owners. One RIS-specific skill suffices; no artificial
portable wrapper pair. These help source/docs changes are locally integrated
with upstream, pending fresh combined review and primary-branch publication.
The combined current source inventory is **52 skills / four flows** and **21
commands (16 project + 4 portable + one help exception)**. Original tables/AC and acceptance remain
historical; bug operations and the product-foundation proposal/project author
remain direct-load without new commands. No aliases or
environment-dependent dispatcher are supplied. Select an actual published package
revision when distributing it; accepted requirements alone do not contain the package.
Verification and remote publication require separate revision-bound evidence;
this guide does not establish either outcome.
Accepted specifications, decisions, immutable URLs and old delivery reports keep
their original identifiers and revisions; this guide translates historical
addresses for current use without repinning acceptance.

The amendment replaces only the old v1/D1 op/flow-to-same-name-command coupling
and N1's command name with `/risb-installation`. It does not repin acceptance or
change subject contracts. The old 41-skill/37-command and eight-command maps below
are historical, not current command instructions. Later W2/U3 skills retain their
technical names, with compact commands as listed here.
The 39-row migration below still maps the exact old baseline; the fast entry is
an addition, not a renamed legacy command. The integrated A+B package was
published at [8ca6c4a](https://github.com/atilla777/ris/commit/8ca6c4ad252cadb32f0718f826c73609a51e74e5)
after complete source/install parity checks, affected deterministic delivery checks
and independent integrated review-2 without findings. The revision-bound result is
recorded in Beads `ris-1wa.1.2`, note `ris-1wa.1.2-completion-20261017-v1`;
later revisions need an evidence-applicability check. This establishes package and
instruction readiness, not live agent behavior or measured speed, and does not
replace the separate feature acceptance and closure of `ris-1wa.1`.
See the [skill catalog](skills.md) for the current inventory and
[development guide](development.md#architecture-plans-and-delivery-records)
for delivery records and their evidence limits; these additions do not repin
accepted specifications.

## Compact command migration — 39

This exhaustive baseline is the 39 files in `commands/opencode/` at
`8d1d8a5bb7c64ff246f6c266b1956e0594fe5ced`. `Load` means explicitly ask the agent
to load that exact retained skill with its skill tool, supplying the original
inputs/scope/permissions; it is not a slash alias. All long command files are removed.

| Previous long command | Current entry |
| --- | --- |
| `/ris-port-op-author-skill` | `/risb-skill` |
| `/ris-port-op-decompose-feature-spec` | Load `ris-port-op-decompose-feature-spec` |
| `/ris-port-op-design-feature` | Load `ris-port-op-design-feature` |
| `/ris-port-op-formulate-architecture-rules` | Load `ris-port-op-formulate-architecture-rules` |
| `/ris-port-op-formulate-development-rules` | Load `ris-port-op-formulate-development-rules` |
| `/ris-port-op-formulate-feature-spec` | Load `ris-port-op-formulate-feature-spec` |
| `/ris-port-op-implement-change` | Load `ris-port-op-implement-change` |
| `/ris-port-op-interview` | `/risb-interview` |
| `/ris-port-op-manage-installation` | `/risb-installation` |
| `/ris-port-op-manage-okf-bundle` | Load `ris-port-op-manage-okf-bundle` |
| `/ris-port-op-plan-roadmap` | Load `ris-port-op-plan-roadmap` |
| `/ris-port-op-plan-task` | Load `ris-port-op-plan-task` |
| `/ris-port-op-prepare-worktree` | Load `ris-port-op-prepare-worktree` |
| `/ris-port-op-retrospect-session` | Load `ris-port-op-retrospect-session` |
| `/ris-port-op-review-change` | `/risb-review-change` |
| `/ris-port-op-verify-feature` | Load `ris-port-op-verify-feature` |
| `/ris-proj-flow-execute-task` | `/risp-run-task` |
| `/ris-proj-flow-prepare-feature` | `/risp-prepare-feature` |
| `/ris-proj-op-author-architecture-rules` | Load `ris-proj-op-author-architecture-rules` |
| `/ris-proj-op-author-development-rules` | Load `ris-proj-op-author-development-rules` |
| `/ris-proj-op-author-skill` | Load `ris-proj-op-author-skill` |
| `/ris-proj-op-complete-container` | `/risp-complete-container` |
| `/ris-proj-op-decompose-feature` | `/risp-decompose-feature` |
| `/ris-proj-op-design-feature` | `/risp-design-feature` |
| `/ris-proj-op-implement-task-tdd` | Load `ris-proj-op-implement-task-tdd` |
| `/ris-proj-op-interview-feature` | Load `ris-proj-op-interview-feature` |
| `/ris-proj-op-manage-okf-bundle` | Load `ris-proj-op-manage-okf-bundle` |
| `/ris-proj-op-plan-roadmap` | `/risp-roadmap` |
| `/ris-proj-op-plan-task` | `/risp-plan-task` |
| `/ris-proj-op-prepare-task-worktree` | Load `ris-proj-op-prepare-task-worktree` |
| `/ris-proj-op-publish-task` | `/risp-publish-task` |
| `/ris-proj-op-refine-epic` | `/risp-refine-epic` |
| `/ris-proj-op-resolve-context` | Load `ris-proj-op-resolve-context` |
| `/ris-proj-op-retrospect-session` | `/risp-retro` |
| `/ris-proj-op-review-task` | `/risp-review-task` |
| `/ris-proj-op-select-feature` | `/risp-select-feature` |
| `/ris-proj-op-specify-feature` | `/risp-specify-feature` |
| `/ris-proj-op-suggest-continuation` | `/risp-next` |
| `/ris-proj-op-update-documentation` | Load `ris-proj-op-update-documentation` |

### First update and restart

An old installed engine cannot acquire this compact package. Download the **new**
engine using the [README checked bootstrap](../README.md#install-in-opencode),
with the same selected new revision for raw script and package. Its `install`
replaces the old full installation; its `update` can also migrate an existing one.
Afterwards `/risb-installation` uses the newly installed unchanged script path.
Repeat updates keep the exact compact set. Quit and **restart OpenCode** after
replacement; the running session retains loaded configuration/instructions.

The same new-engine bootstrap is needed for the first help-bearing package when
the installed compact engine predates the exact `ris-help.md` ownership exception:
the older validator rejects that entry before target writes. This does not make
an old compact self-update successful or require a new installer mode.

The engine handles legacy `ris-*.md` and compact `risp-*.md`/`risb-*.md` for
replacement, uninstall and schema-1 recovery. Pre-existing unproven short-name
files/links are preserved with a conflict; neither prefix nor old version marker
establishes ownership. Resolve their ownership explicitly before retrying; see
[installation ownership and recovery](installation.md#what-changes-and-what-is-preserved).
Do not delete journals or report a mixed set as ready. Existing same-revision
resources, types/modes and foreign-file preservation checks still apply.
The exact active `ris-help.md` fits the already reserved legacy `ris-*.md`
namespace, so existing files there are overwritten/removed rather than receiving
the compact collision guard. Its ownership-resource entry has an exact-name
validation exception, not a general `ris-*` manifest wildcard. Old 18/39-entry
tables and accepted decisions are not rewritten to include it.

## Historical complete skill replacement map — 41

The new identifier is both the source/installed folder and frontmatter `name`.
At that historical revision every op/flow additionally had a same-name command.
There were 35 op, 2 flow, 1 lib and 3 adapters: 41 skills and 37 commands.
Those command rules are superseded by the compact map above; the technical skill
replacement map remains useful for translating older paths.

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

## Historical retired command map — eight

This table records the earlier transition only. Its long replacement commands
are now retired too: apply the current 39-row map above for a usable entry.

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
     assets, scripts, file types and modes. Install only the compact command
    templates from `commands/opencode/` in the selected revision's inventory.
    For the usual project-local layout these
   go to `.opencode/skills/<name>/` and `.opencode/command/<name>.md` beneath the
   selected target, not beneath the RIS source repository by assumption.
6. Remove all 41 retired skill folders and all eight retired command files in
   the updated installation, after checking their ownership and preserving the
   agreed baseline. Overlaying the new files while leaving old discoverable
    aliases is an incomplete migration. The package now supplies the management
    skill/engine and `/risb-installation`; first migration uses the new bootstrap
    as explained above. Remove the 39 long op/flow command files as well.
7. Compare the full installed package against the selected source revision by
   relative paths, bytes, types and modes, including all resources. Verify folder
   equals frontmatter name, unique valid identifiers (at most 64 characters),
     nonempty descriptions, command basenames equal the selected revision's explicit compact map, exactly one
    mapped skill load and `$ARGUMENTS` per template, and no lib/adapter commands.
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
