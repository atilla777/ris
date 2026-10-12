---
name: ris-specify-feature
description: >-
  Formulate, obtain acceptance for, and save a selected feature's specification
  in its RIS project, then verify its feature task under a confirmed epic.
  Use when preparing an accepted feature specification and linked tracker record;
  not for selecting a feature, interviewing alone, decomposing it into child
  tasks, technical design, or drafting portable content without project writes.
---

# Specify a selected feature in a RIS project

Own the **combined project result**: a specific accepted specification, its
verified saved version and a correctly linked feature `task` under a confirmed
`epic`. `ris-formulate-spec-base` owns portable content; `ris-interview-feature`
owns a feature-requirements handoff when material answers are missing; the
selected task adapter owns bounded tracker operations. Apply their results and
check the whole, rather than repeating their methods or treating a loaded name
as an executed operation. This is the project wrapper for the portable base:
project sources, acceptance, document format, permission and tracker identity
cannot be determined by the base. Direct invocation works in the current agent;
no execution role or encompassing workflow is required.

Own **functional requirements**, not the feature's technical design. Accepted
requirements create a feature task even when design is absent; this does not
establish readiness for decomposition or implementation. Preserve behavioral
interfaces/quality constraints, but do not decide component ownership, new
implementation contracts or test seams here. Do not start another stage.

## Establish project, feature and authority

Identify the selected project and feature, its bounded result and confirmed
parent epic ID (if already known), existing feature/task/spec links and
acceptance evidence. A feature proposal is not a chosen feature; a title is not
an epic or task ID. Do not select the next feature or refine an unclear epic.
Confirm the permission to write the exact specification and feature task;
without it prepare an explicitly unsaved proposal, `changes: []`, and stop
before either write. A general request to work toward tasks does not accept the
particular requirements that will be formulated.

Ensure installed `ris-common` is available and apply its rules; read its
conditional dialogue, artifact and quality resources before their respective
actions. Use installed `ris-context` with its configuration resource to prepare
this project's `sources.rules`, relevant `sources.product` and `sources.specs`,
and `adapters.tasks.skill` for task operations. Check status, provenance,
diagnostics, project root and write scope. Select applicable instructions,
accepted documents, profile and existing linked artifacts by relevance and
status, not by listing every file or using RIS's own document layout. Resolve
document paths from this project's sources and links, including in a worktree;
`sources.specs` is a directory, not a default filename. An explicit missing or
invalid project configuration is a blocker, not a reason to use package defaults.
For a new file establish its exact project-approved path and format under the
permitted scope before writing; for an existing file read and reconcile its
actual content and status. An unresolved ownership, path or feature identity
conflict blocks dependent writes. No path or acceptance evidence is inferred
from a proposed tracker ID, file presence, or a past conversation not supplied.

At creation agree a permanent feature slug and search all-status project tasks
and existing spec directories for collisions, including closed records. The
tracker task is the sole ID ↔ slug ↔ spec link, not a second registry. A title
change never renames the slug or path. Default to ordinary
`sources.specs/<slug>/spec.md` without OKF index/frontmatter; a documented project
override takes precedence. Read a legacy record before any migration: never
guess its slug from its title or silently relocate its accepted document.

## Compose one content and acceptance dialogue

Ensure installed `ris-formulate-spec-base` is available. Provide it the
confirmed feature scope, already known decisions with sources/status, relevant
project rules and content profile; **apply** its method to produce and check
proposed substantive behavior, exclusions, limits, exceptions and observable
criteria. Check material coverage and distinguish confirmed inputs, new
wording, proposals and decisions still open. Before deciding that an interview
is unnecessary, check the feature's material areas against accessible evidence:
outcome and actors, main/alternative behavior, exceptions, interfaces and
constraints where applicable, material quality conditions, observable criteria
and decision provenance. For each area identify its confirmed source, the
decision still needed, or why it does not apply; a catalogue entry or plausible
draft alone does not close a branch. If readiness of inputs, handling of
conflicting or stale evidence, or another material area remains unresolved,
ensure installed `ris-interview-feature` is available and apply its
project-specific coverage and handoff in the **same user conversation**; pass
known answers and sources, do not start a second full interview or re-ask
confirmed decisions. Use its `ris-interview-base` decision tree across remaining
material branches, not a fixed question count; then apply the base to updated
answers. A single clarification suffices only if other material branches have
been checked. If an essential dependency or answer is unavailable, preserve
the supported partial content and name what prevents acceptance or saving.
Report evidence and reasons when no interview was needed; user approval of a
draft alone does not establish that unexamined branches were covered.

Use only related author product passages, retaining source path/heading,
available version and accepted/draft/example/question status without reorganizing
them by technical systems. Apply the base's stable `AC-nnn` rules; links use the
agreed permanent `slug#AC-nnn`. Reused decisions with missing baseline versions
have unconfirmed applicability; changed linked behavior needs focused impact
resolution, not a silent edit of product or all existing feature documents.

Show the **specific proposed content** and material open questions to the
person or the acceptance authority defined by this project's rules. Obtain and
verify acceptance of **this version and scope** by that mechanism *before*
writing to the agreed accepted-spec path; a generic request, approval of an
earlier version or a successful format check is insufficient. If acceptance
occurs in the current dialogue, establish how the decision and version will be
recoverable to a later recipient, with a precise accessible address under the
project's rules. If no project mechanism or durable verifiable address for the
decision is available, do not create a tracker feature task. Never manufacture
an acceptance record or treat an unaccepted candidate as the accepted file.
After a material change to accepted content, obtain acceptance of the changed
version again; do not silently append requirements during formatting.

Choose an independently verifiable requirements scope before acceptance:
`whole-file` only when no design will be appended to that file, otherwise a
unique exact Markdown heading (e.g. `heading:## Requirements`). For a heading,
hash raw UTF-8 bytes from its line inclusive up to the next heading of the same
or higher level or EOF, without normalization. Keep decision evidence outside
the hashed scope to avoid a self-referential hash. Match its approved scope and
SHA-256 to the proposed and later saved bytes. Use the adapter's supported
scope representation; ambiguous/overlapping areas require separate files or
fresh acceptance of the affected scope, never assumed validity. A later design
decision cannot substitute for this requirements decision.

## Save and reconcile the selected document

Before any write, identify the selected available task adapter and verify a
compatible `tasks` v1 with the **optional** `tasks.epics.read`, `tasks.items.list`,
`tasks.items.read` and `tasks.items.create` operations and required guarantees:
complete all-status search, confirmed type/parent, stable retry identity,
specification link and acceptance-evidence address, read-back and applicable
concurrency level. Also require separately advertised `tasks.feature-record/1`
with `tasks.features.read` and initial-record support in `tasks.items.create`:
immutable project-unique slug, spec path and separately scoped requirements
digest/acceptance. Creation of this identity requires an independently confirmed
exclusive writer window covering all feature creators across the all-status
slug search, creation and read-back, not best-effort duplicate avoidance.
If these guarantees are unavailable, block the combined write. Confirm an open
parent epic by exact ID and its intended
scope; agree the feature's stable key in that epic/goal and approved task
content. A configured adapter name alone proves none of this. Preflight these
requirements before saving to avoid a predictable orphan file; if an
independent document-only result is explicitly authorized, report that smaller
scope as such rather than calling this combined result complete. Never bypass
an unavailable/incompatible adapter by editing its storage or calling `bd`
directly. Strict no-duplicate creation requires a separately established
exclusive writer window; do not downgrade the promised unique slug to ordinary
best-effort v1 creation.

Choose the project's actual document format. Ordinary Markdown can be written
directly under its rules; for an OKF bundle apply the installed suitable OKF
operation and its format checks only when OKF is actually chosen. Do not impose
OKF on other projects or assume validation establishes acceptance. Check write
permissions and concurrent state of the exact path, reread an existing file
before a permitted update and preserve unrelated decisions/links; do not
silently overwrite a draft or a different accepted version. Follow the
project's prescribed writer or file concurrency protocol; if it is unavailable
or state changed, return `conflict` instead of using a different storage path.
Write only the accepted content and evidence address in the agreed location,
with no intermediate draft there. Read the saved document/bundle back; check
its substantive coverage, actual format/links, version and acceptance evidence
against the agreed content. An uncertain write is reconciled from disk before
any retry; never treat an apparent success or mere file presence as proof.

Only after the document and acceptance evidence are verifiable, have the
selected adapter search all relevant feature tasks including closed ones and
apply `tasks.items.create` with `type: task`, confirmed open epic parent,
approved title/content, scoped stable retry key, exact saved-spec link and
verifiable acceptance-decision address. The adapter may return an existing ID
only on a full match including content, parent, link and decision address; a
stale task, moved parent, changed specification or multiple matches are a
`conflict`, not permission to update it silently. Verify from fresh reads the
real ID, type, status, parent membership, saved content, spec link and
acceptance decision for the **same** version. Do not create children, add task
dependencies, claim or close anything in this operation.

Supply the adapter's initial feature-record encoding in the approved content:
permanent slug, exact spec path, requirements path/scope/SHA-256 and acceptance
address with matching approved scope/version/decision; design and verification
are absent (`null` in Beads), with empty initial history. Verify the entire
stored identity block and project-wide slug uniqueness by fresh adapter reads.
For an existing exact record preserve slug, design, history and unrelated text;
never send an initial payload over an existing record. A legacy record or a
requirements revision needs an explicitly authorized conditional
`tasks.features.update`, expected old values, preservation of prior decisions,
and the capability's exclusive writer guarantee; otherwise report conflict or
unsupported legacy state. Do not erase an accepted design: on requirements
change identify its applicability as unconfirmed until reviewed, preserving
history. A design-null feature task is a valid requirements-only result.

## Report actual outcome and stop

Return `ok|blocked|conflict|error`, selected project/config provenance,
feature ID, permanent slug and parent epic identity, actual spec address,
requirements scope/digest and accepted version,
source of its acceptance, verified task ID and parent (only when confirmed),
status of decisions (including design absent or applicability unconfirmed),
actual changes and read-back evidence, plus limitations
and next needed substantive result. `ok` for the combined result requires both
the accepted saved spec and matching tracker task. If a document write succeeds
but tracker creation fails, or a response is ambiguous, reread both states,
report the saved address and all confirmed IDs/changes, stop further writes
and leave a precise handoff for reconciliation; do not roll back, blind-retry
or claim the task exists. On interruption before acceptance, return the known
decisions and accessible sources in the response without creating a mandatory
draft store. Give a recipient without this chat enough references, version,
statuses, rights, verified effects and unresolved decisions to continue. Stop
after this feature specification and task are checked; do not initiate
decomposition, technical planning or implementation.
