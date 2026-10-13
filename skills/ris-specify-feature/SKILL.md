---
name: ris-specify-feature
description: >-
  Formulate, obtain acceptance for, and save a selected feature's specification
  in its RIS project, then verify its feature task under a confirmed epic, or
  complete an explicitly requested document-only specification before a task exists.
  Use for accepted project requirements, including bounded noninteractive save;
  not for selecting a feature, interviewing alone, decomposing it into child
  tasks, technical design, or drafting portable content without project writes.
---

# Specify a selected feature in a RIS project

By default own the **combined project result**: a specific accepted specification, its
verified saved version and a correctly linked feature `task` under a confirmed
`epic`. `ris-formulate-spec-base` owns portable content; `ris-interview-feature`
owns a feature-requirements handoff when material answers are missing; the
selected task adapter owns bounded tracker operations. Apply their results and
check the whole, rather than repeating their methods or treating a loaded name
as an executed operation. This is the project wrapper for the portable base:
project sources, acceptance, document format, permission and tracker identity
cannot be determined by the base. Direct invocation works in the current agent;
no execution role or encompassing workflow is required.

An explicitly requested **document-only** operation instead owns a complete
accepted, saved and checked requirements document and decision evidence, without
a tracker ID. It is not an implicit fallback for a failed combined operation.
In a scenario, interview, discussion and separate acceptance stay in the leading
dialogue; bounded formulation and save may run noninteractively in a subagent.
For save, require the verified candidate address/revision, its exact destination
path/section, the authorized acceptance decision and write scope as inputs.
Read and check them yourself; never infer acceptance from a caller's "done".
A noninteractive executor returns missing decisions to the caller and asks no
user questions, including through dependencies. Do not reformulate accepted
content while saving. No new skill or execution role is required for these modes.

Own **functional requirements**, not the feature's technical design. Accepted
requirements can create a feature task even when design is absent; this does not
establish readiness for decomposition or implementation. Preserve behavioral
interfaces/quality constraints, but do not decide component ownership, new
implementation contracts or test seams here. Do not start another stage.

## Establish project, feature and authority

Identify the selected project and feature, its bounded result and confirmed
parent epic ID (if already known), existing feature/task/spec links and
acceptance evidence. A feature proposal is not a chosen feature; a title is not
an epic or task ID. Do not select the next feature or refine an unclear epic.
Establish combined or explicitly requested document-only mode and permission
for the exact document/evidence paths and, in combined mode, the feature task.
Without the necessary rights return an unsaved proposal or block the dependent
effect; do not call a smaller result combined success. A general request to work
toward tasks does not accept the particular requirements that will be formulated.

Ensure installed `ris-common` is available and apply its rules; read its
conditional dialogue, artifact and quality resources before their respective
actions. Use installed `ris-context` with its configuration resource to prepare
this project's `sources.rules`, relevant `sources.product` and `sources.specs`,
and, only for task operations, `adapters.tasks.skill`. Check status, provenance,
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

At creation agree a permanent feature slug and check existing document paths;
the selected adapter owns all-status tracker collision checks when needed. The
tracker task is the sole ID ↔ slug ↔ spec link, not a second registry. A title
change never renames the slug or path. Default to ordinary
`sources.specs/<slug>/spec.md` without OKF index/frontmatter; a documented project
override takes precedence. Read a legacy record before any migration: never
guess its slug from its title or silently relocate its accepted document.

## Compose one content and acceptance dialogue

Read `references/acceptance-and-save.md` relative to this installed skill before
selecting the accepted section, accepting or saving. If unavailable block that
part. It defines candidate identity, separate decisions and publication gates.
For a bounded save with checked accepted candidate inputs, skip formulation
and interview and apply the persistence resource below. For noninteractive
formulation use supplied decisions and return the checked candidate proposal
address/revision and open choices to the leading dialogue; this is not an
accepted saved specification. Do not execute interactive branches in a subagent.

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

Apply the resource's content/decision matching checks. A later design decision never substitutes for
the requirements decision. Reuse acceptance of unchanged content after checking
its applicability; do not ask for repeated approval just to retry persistence.

## Save and reconcile the selected document

Apply the resource's file preflight, save and read-back in either mode. For
document-only do not require an epic, tracker adapter or feature ID, and stop
after the checked document/decision result. Never derive a task-note path from
an unconfirmed ID or introduce a mandatory draft store.

For combined mode preflight the selected available adapter's `tasks` v1 epic
read, item list/read/create and `tasks.feature-record/1` read/initial-create
support. Check actual guarantees, confirmed open epic/scope, stable retry key,
slug/spec association and approved task content. Ordinary creation uses the
adapter's best-effort all-state collision detection, exact reuse and read-back;
it requires no global creator window or extra risk question. If the caller
explicitly requires strict uniqueness, require a real guarantee or block that
write. An unavailable adapter blocks combined completion, not authorized local
saving; report any local effect as partial. Never bypass it via direct storage.

Only published document and decision inputs may enter a tracker reference.
Invoke create/reuse through the adapter with type `task`, confirmed epic,
approved content/key and current `ris.feature-record/1`: immutable slug/spec_path,
requirements reference `{path, revision, section, acceptance: {address,
decision: "accepted"}}`, design and verification `null` for requirements-only
creation. Do not add scope hashes or tracker history. If a separately accepted
published design is supplied, validate its independent decision before including
it. Check the returned actual ID, type, parent, identity and exact refs from
adapter read-back; a detected duplicate remains conflict with known IDs.

For an existing exact record preserve all refs and unrelated prose; never send
an initial block over it. A requirements revision needs explicit update rights,
expected old state and the adapter's real independently established writer window
against lost updates, with provider/scope/duration through read/write/verify.
Claim, sandbox, local lock, status guard, permission and read/write/read are not
protection against remote writers; missing protection blocks the update.
Verify a new separate requirements decision and existing design applicability;
block an unsupported/materially incompatible design rather than silently reusing
it as accepted input. Changed refs invalidate verification to null. Git owns
displaced content/decisions. Historical unsupported payloads remain intact and
block dependent writes; no migration or alternate API is part of this operation.
Do not create children, add dependencies, claim or close tasks.

## Report actual outcome and stop

Return `ok|blocked|conflict|error`, selected project/config provenance,
mode, feature ID and parent only if confirmed, permanent slug, actual spec address,
requirements path/section and checked candidate or published revision,
source of its acceptance, verified task ID and parent (only when confirmed),
status of decisions (including design absent or applicability unconfirmed),
actual changes and read-back evidence, plus limitations
and next needed substantive result. Include verified candidate address/revision,
acceptance decision address/status, pending immutable refs, and separate local,
Git and tracker publication facts. `ok` for document-only means its complete
accepted saved/read-back result, even before publication, with that limit explicit.
If the requested document-only result requires publication, pending refs mean
partial/blocked rather than `ok`; report each required channel separately.
`ok` for the combined result requires both
the accepted saved spec and matching tracker task. If a document write succeeds
but tracker creation fails, or a response is ambiguous, reread both states,
report the saved address and all confirmed IDs/changes, stop further writes
and leave a precise handoff for reconciliation; do not repeat unchanged acceptance,
roll back, blind-retry
or claim the task exists. On interruption before acceptance, return the known
decisions and accessible sources in the response without creating a mandatory
draft store. Give a recipient without this chat enough references, version,
statuses, rights, verified effects and unresolved decisions to continue. Stop
after the requested document-only or combined result is checked. Publication
belongs to the authorized caller; this skill does not commit/push Git or Dolt.
Do not initiate
decomposition, technical planning or implementation.

For a noninteractive component return a short handoff: status, scope/mode,
verified result address and candidate revision or confirmed ID, decision/evidence
address, limitations, actual effects and decision needed. The consumer reads
full content by address; never substitute an unverified "done" for this result.
