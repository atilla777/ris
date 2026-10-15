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

The following 41 folders form the coherent namespace package in this revision.
The source package and repository-local primary installation are synchronized.
The linked SKILL.md files define actual inputs, dependencies, permissions, checks
and stopping points. Independent verification and remote publication require
their own revision-bound evidence; this inventory does not establish those outcomes.

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
| [ris-proj-op-specify-feature](skills/ris-proj-op-specify-feature/SKILL.md) | Accepted published requirements and feature/standalone record, or explicit limited contribution | same name |
| [ris-proj-op-design-feature](skills/ris-proj-op-design-feature/SKILL.md) | Separately accepted published design and record refs, or explicit limited contribution | same name |
| [ris-proj-op-decompose-feature](skills/ris-proj-op-decompose-feature/SKILL.md) | ID-based feature/standalone one-task or sufficient children and tracker publication | same name |
| [ris-proj-op-prepare-task-worktree](skills/ris-proj-op-prepare-task-worktree/SKILL.md) | Claim-aware task copy/environment handoff | same name |
| [ris-proj-op-plan-task](skills/ris-proj-op-plan-task/SKILL.md) | Verified saved task plan | same name |
| [ris-proj-op-implement-task-tdd](skills/ris-proj-op-implement-task-tdd/SKILL.md) | Claim-aware implementation with mandatory TDD | same name |
| [ris-proj-op-review-task](skills/ris-proj-op-review-task/SKILL.md) | Checked project review, saved when authorized | same name |
| [ris-proj-op-update-documentation](skills/ris-proj-op-update-documentation/SKILL.md) | Authorized documentation synchronization | same name |
| [ris-proj-op-publish-task](skills/ris-proj-op-publish-task/SKILL.md) | Reviewed task/change or pre-ID document integration and verified Git push | same name |
| [ris-proj-op-complete-container](skills/ris-proj-op-complete-container/SKILL.md) | Explicit verified feature/standalone-container/epic closure | same name |
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
There are no aliases. The W1 installer CLI is included below; complete production
package installation remains W2 delivery.
The local foreign skill `grilling`, command `grillme`, and client configuration
are not RIS package source and must be preserved during synchronization.

### Installer CLI and bootstrap (W1; production acceptance pending W2)

The single runtime source is
[`skills/ris-port-op-manage-installation/scripts/ris-install.sh`](skills/ris-port-op-manage-installation/scripts/ris-install.sh).
W1 tests it against a local Git fixture containing minimal management skill and
command stubs. This source revision deliberately has **no production management
SKILL.md or command**: the installer rejects such an incomplete package. A raw
script URL becoming available does not establish production bootstrap acceptance.
W2 supplies and verifies the complete package; Linux and macOS evidence and
independent review are required before claiming supported production delivery.

Runtime dependencies: **Bash 3.2+, Git 2.20+, flock**, and standard Unix `cp`, `mv`,
`rm`, `mkdir`, `rmdir`, `mktemp`, `chmod`, `cmp`, `diff`, `id`, `ls`, `readlink`.
Linux uses util-linux flock. On macOS install **discoteq/flock 0.4.0** externally,
for example `brew install flock`; `/bin/bash` is sufficient. The installer reports
missing tools and never installs dependencies. `curl` is only for bootstrap;
Python 3 is development/test-only. RIS config, Beads, OpenCode and target Git are
not runtime prerequisites.

Once a complete revision is published, a human or agent can bootstrap without
installed RIS using this Bash block. Choose an **existing absolute project path**;
spaces are supported. Leave `ref` empty for upstream remote HEAD, or set it to an
exact tag or full 40-hex **commit** SHA. The raw script and `--ref` use the same pin:

```bash
(
  project='/absolute/path/to/project'
  ref='' # Or an exact tag / full commit SHA of a complete package revision.
  raw_ref=${ref:-HEAD}
  installer=$(mktemp /tmp/ris-bootstrap.XXXXXXXX) || exit 1
  trap 'rm -f "$installer"' EXIT
  url="https://raw.githubusercontent.com/atilla777/ris/${raw_ref}/skills/ris-port-op-manage-installation/scripts/ris-install.sh"
  if ! curl --fail --show-error --location "$url" --output "$installer"; then
    exit 1
  fi
  args=()
  if [ -n "$ref" ]; then args=(--ref "$ref"); fi
  bash "$installer" install --project "$project" "${args[@]}"
)
```

The default follows remote HEAD, regardless of branch name. Branch names and Git
revision expressions are not `--ref` inputs; lightweight/annotated tags are.
A 40-hex tag spelling is interpreted as a commit SHA. Download errors stop before
execution; there is no `curl | sh` path. Tags containing URL-special characters
must be URL-encoded in `raw_ref` while retaining the literal tag in `ref`.

After installation the same engine handles explicit update/removal:

```bash
bash '/absolute/project/.opencode/skills/ris-port-op-manage-installation/scripts/ris-install.sh' update --project '/absolute/project' # Optional --ref TAG_OR_SHA
bash '/absolute/project/.opencode/skills/ris-port-op-manage-installation/scripts/ris-install.sh' uninstall --project '/absolute/project'
```

`install` fully replaces an existing or manual installation; `update` requires
at least one managed element or version file. Local edits and collisions in the
reserved `.opencode/skills/ris-*` and `.opencode/command/ris-*.md` namespace are
overwritten, and retired elements removed. Use other names for project additions.
The four-line `.opencode/ris-installation` records format/source/full revision/
harness. No timestamps or backup history are stored. Other skills/commands,
OpenCode settings, `ris.yaml`, `AGENTS.md`, docs/tasks, alternate `skill/` and
`commands/` and global locations are preserved. Check those alternate/global
locations for shadowing; the installer does not migrate them. Ordinary parent
directories are required; symlink parents and unsafe managed objects are refused.
Old managed links are replaced as links without touching their external targets.

The engine serializes cooperating processes for the same OS-user and physical
project root. Busy exits without target writes. Before replacing its own script
it continues from a private external self-copy. A verified snapshot and schema-1
journal at `.opencode/.ris-install-transaction/` support offline recovery before
any network operation. Pre-commit failure restores the old bytes/types/modes/link
targets; SIGKILL recovery repeats that restore from immutable backup. A committed
or rolled-back terminal marker permits cleanup only, even after partial backup
removal. Guarantees cover process interruption on a working filesystem, not power
loss, storage corruption, ACLs/xattrs or concurrent edits by other tools.

Exit **0** means verification and cleanup completed. Nonzero diagnostics distinguish
not changed, restored, recovery required, or applied/restored with cleanup
incomplete. Repeat a valid request to finish recovery/cleanup. If the installed
script was removed during an interrupted operation, use the bootstrap block again
(same project, compatible schema-1 engine). If the journal is unknown/damaged,
preserve its exact reported path and diagnose it; do not delete evidence or try
another install over it. Repeated uninstall is an offline successful no-op; after
the installed script is gone, use the bootstrap/external script for that request.

Verify the full SHA and skill/command counts in the success report and inspect
the version file and ordinary `git status`. Installed files/version remain visible
for the project's normal Git workflow; no ignores, `init`, commits or pushes are
performed. Existing project ignore rules are not overridden. **Quit and restart
OpenCode** after changes; an existing agent session retains its loaded instructions.

Developer verification (filesystem CLI tests only; no agent sessions):

```sh
python3 -m unittest discover -s tests/package_installation -p 'test_*.py' -v
bash -n skills/ris-port-op-manage-installation/scripts/ris-install.sh
```

The workflow runs G0 lock/copy first, then this suite on Linux and macOS, explicitly
using `/bin/bash` (3.2 on macOS) and externally installed flock. A workflow file is
not evidence of a successful remote job; both OS results must be checked separately.

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

Shared paths use context's checked primary root: validated explicit selection,
or an already available saved indication with verified project/repository/current-copy
association and provenance. Missing/conflicting association blocks dependent shared
actions while retaining useful current-copy source paths. Handoffs identify result
locators, versions/separate decisions, actual channel states and exact remainder;
local notes and response-only content are not automatically remote inputs.
Worktree preparation retains separate copy and environment readiness.
Git is the default selected worktrees adapter; installed
Worktrunk presence does not select it (reference version 0.68.0). Planning consumes
the supplied copy without creating it or requiring a claim. Feature decomposition
starts from accepted current published requirements/design and a confirmed ID;
document-only requirements/design can precede a tracker ID. Execution-role names
and configuration v2 are unchanged by naming.

The existing Git publisher accepts requirements-only documents before a task ID
or design exists, as well as task changes, through one publication algorithm.
Both require exact whole-snapshot independent review, authority, full outgoing
scope and remote verification. Publication does not accept proposed content,
write/close tracker records or publish Dolt. A caller checks the combined result
and publisher receipt. The U2 candidate in this task copy extends existing
planning owners: finished direct roadmap/refinement/decomposition invoke tracker
publication; specify/design apply independent document review and this Git owner
before record reconciliation and tracker publication. Explicitly limited
proposal/local-save/record-only contributions return their exact remainder.
Nesting does not silently change the mode; no-change checks required availability
or publication debt without empty commits/pushes. These instruction changes are
pending primary integration, independent review and publication.

For applicable task-bound operations, a short command plus exact ID starts
discovery through context and selected adapter reads of kind/key/content/links,
complete composition and typed blockers. Linked accepted versions and separate
decisions are read and checked; missing/ambiguous/stale inputs get exact diagnostics.
Explicit ordinary standalone tasks/containers need no artificial epic or feature
JSON; simple accepted constraints need no ceremonial design file, while material
design requires separate acceptance. Children carry their own sufficient outcome,
scope, criteria, accepted refs/decisions and contracts/seams. Structural parent
does not make a child a feature or authorize parent closure. One-task outcomes
get no artificial child. Standalone container completion checks its own accepted
whole, protected evidence and separate exact close; closed children alone are
insufficient. Beads advertises these ordinary operations as tool-specific, keeping
common tasks v1 and strict feature-record semantics intact. Both flows consume
owner receipts and preserve actual-effect recovery, including closed-pending work.
ID does not replace an actual change snapshot, document-write authority, session
history locator or explicit OKF root. U2 adds no navigator or new workflow engine.

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
