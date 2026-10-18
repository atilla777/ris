---
name: ris-proj-op-specify-feature
description: >-
  Accept, save and publish RIS requirements and reconcile an epic-backed feature,
  explicit standalone task/container, or document-only subject. Discover existing
  inputs by ID; support explicitly limited formulation/save/record contributions.
  Use for accepted project requirements, including bounded noninteractive save;
  not for selecting a feature, interviewing alone, decomposing it into child
  tasks, technical design, or drafting portable content without project writes.
---

# Specify a selected feature in a RIS project

By default own the **combined project result**: a specific accepted specification, its
verified saved/published version and a correctly linked record: a feature `task`
under a confirmed `epic`, or an explicitly selected ordinary standalone task or
task-container. `ris-port-op-formulate-feature-spec` owns portable content; `ris-proj-op-interview-feature`
owns the reusable material-coverage map/check and an interview handoff when needed; the
selected task adapter owns bounded tracker operations. Apply their results and
check the whole, rather than repeating their methods or treating a loaded name
as an executed operation. This is the project wrapper for the portable base:
project sources, acceptance, document format, permission and tracker identity
cannot be determined by the base. Direct invocation works in the current agent;
no execution role or encompassing workflow is required.

An explicitly requested **document-only** operation instead owns a complete
accepted, saved, checked and published requirements document and decision evidence, without
a tracker ID. It is not an implicit fallback for a failed combined operation.
In a scenario, interview, discussion and separate acceptance stay in the leading
dialogue; bounded formulation and save may run noninteractively in a subagent.
For save, the caller supplies the full exact candidate text and distinguishable
version/scope, or a recipient-accessible file at an exact address/version, its
exact destination path/section, separate attributable requirements acceptance
decision and write scope as inputs.
Read and validate complete content, version/scope and decision/provenance yourself;
never infer acceptance from a caller's "done" or access to foreign chat. Return
incomplete, inaccessible, ambiguous or changed candidates to the caller before save.
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
From an existing ID use context and the selected adapter's exact read, complete
children and directed blocker reads to discover kind/key, scope, current sources
and separate decisions. Read linked versions and compare current applicability;
ask only for the exact missing/ambiguous/stale dependency. Existing ID never
authorizes a new record. Establish feature, standalone task/container or
document-only subject explicitly; a failed feature parse is not a standalone
selector. Standalone requires no artificial epic, slug or feature-record;
preserve approved paths and structural parent if any. Simple tasks need accepted
sufficient constraints, not a ceremonial separate design document.
Establish combined or explicitly requested document-only mode and permission
for the exact document/evidence paths and, in combined mode, the selected record.
Without the necessary rights return an unsaved proposal or block the dependent
effect; do not call a smaller result combined success. A general request to work
toward tasks does not accept the particular requirements that will be formulated.

Ensure installed `ris-proj-lib-common` is available and apply its rules; read its
conditional dialogue, artifact and quality resources before their respective
actions. Use installed `ris-proj-op-resolve-context` with its configuration resource to prepare
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

Before any document/evidence write intended for Git publication, require the
caller to supply an already prepared, confirmed own branch and safe copy, with
work identity/association, repository/path/branch/base, checked current state and
adequate write/publication authority. A suitable current copy is allowed; isolation
or project rules may require a worktree. This applies to full combined/document-only
calls and limited local saves intended for a caller's later publication. Validate
the supplied evidence and resolve destinations in that copy; this wrapper saves
content but does not create/switch branches or prepare copies, and the publisher
does not do so later. Without that prerequisite, block dependent publication before
writing. Only independently authorized local/unpublished saving may proceed within
project rules, with that limitation explicit and no publisher call; never silently
downgrade a full request or promise later publication from a dirty primary copy.
Proposal-only and record-only calls need no new document working copy.

For a feature at creation agree a permanent slug and check existing document paths;
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
Ensure installed `ris-proj-op-interview-feature` is available and apply its
**Map the material requirements** and **Check and hand off** sections to the
known answers, sources and candidate. This reuses the coverage method, not an
interview invocation or a separate checking operation. Check current applicability
before acceptance; keep evidence/gaps in the existing dialogue or handoff.
For a bounded save with checked accepted candidate inputs, use that same check
to validate substantive coverage without reformulation, interview or questions;
return a material gap/conflict to the caller before dependent save. With valid
inputs, skip formulation and interview and apply the persistence resource below. For noninteractive
formulation use supplied decisions and return the full checked proposal with a
distinguishable version/scope, or an accessible file address/version when separately
authorized, and open choices to the leading dialogue; this is not an
accepted saved specification. Do not execute interactive branches in a subagent.

Ensure installed `ris-port-op-formulate-feature-spec` is available. Provide it the
confirmed feature scope, already known decisions with sources/status, relevant
project rules and content profile; **apply** its method to produce and check
proposed substantive behavior, exclusions, limits, exceptions and observable
criteria. Check material coverage and distinguish confirmed inputs, new
wording, proposals and decisions still open, using the coverage owner's same
map/check on the proposal before acceptance. Reuse sufficient current inputs
directly; ask only for a material gap or conflict. A single clarification need
not become an interview. When an interview is needed, apply that owner's
conditional interview route in the **same user conversation**, passing known
answers/sources and remaining gaps without re-asking confirmed decisions. Then
apply the formulation base to updated answers. Noninteractive work returns
missing decisions to the caller. Preserve supported content and independent
work while an essential gap blocks only dependent acceptance or saving.

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

Apply the resource's file preflight, save, review/publication and read-back in
either subject mode. Document-only requires no epic, tracker adapter or ID.
Full finished invocation is the default; an explicit limited contribution names
its boundary (proposal, accepted local save, or record reconciliation from an
already checked Git receipt). Nesting/Gas City never silently limits effects.
Limited record reconciliation performs no second Git or Dolt push. Never derive a task-note path from
an unconfirmed ID or introduce a mandatory draft store.

For an ordinary standalone combined result check explicit tool-specific
create/reconcile and source-update support and the adapter's owned resource;
pass approved kind, stable identity, own scope/criteria and published sources/
decisions. Verify actual ID/type/parent/content and guarantees; do not use common
feature create semantics or construct feature JSON. Existing-record updates need
fresh expected content/structure checks and bounded native operations/read-back;
changed refs invalidate dependent evidence.
The following feature-record requirements apply only to the feature branch.
For a feature combined result preflight the selected available adapter's `tasks` v1 epic
read, item list/read/create and `tasks.feature-record/1` read/initial-create
support. Check actual guarantees, confirmed open epic/scope, stable retry key,
slug/spec association and approved task content. Ordinary creation uses the
adapter's best-effort all-state collision detection, exact reuse and read-back;
it requires no global creator window or extra risk question. If the caller
explicitly requires strict uniqueness, require a real guarantee or block that
write. An unavailable adapter blocks combined completion, not authorized local
saving; report the causal non-`ok` status, preserved local effects and exact
remaining adapter operation. Never bypass it via direct storage.

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
expected old state and the adapter's targeted native-operation protocol with
fresh checks and independent read-back. Preserve the acceptance block and pins;
no manual window or graph/external-evidence transaction is required. The adapter
states native limits; claim, sandbox or a status-only guard is not full content
CAS. An explicitly required stronger unsupported guarantee blocks only that write.
Verify a new separate requirements decision and existing design applicability;
block an unsupported/materially incompatible design rather than silently reusing
it as accepted input. Changed refs invalidate verification to null. Git owns
displaced content/decisions. Historical unsupported payloads remain intact and
block dependent writes; no migration or alternate API is part of this operation.
Do not create children, add dependencies, claim or close tasks.

## Report actual outcome and stop

After verified record reconciliation in full mode, invoke the selected adapter's
separate publication operation with exact expected records/refs, authorized
outgoing scope and destination evidence. Inspect its required revision/fresh remote
reachability receipt alongside local identity/content/link checks of the promised
whole; remote assurance is not independent field equivalence. No-change
verifies required existing publication or remaining debt without empty push.
Missing authority or failed/ambiguous publication leaves the full result blocked,
preserving known Git commits/IDs for only the missing operation.

Return `ok|blocked|conflict|error`, selected project/config provenance,
mode/kind, exact ID and parent only if confirmed, feature slug where applicable, actual spec address,
requirements path/section and checked candidate or published revision,
source of its acceptance, verified task ID and parent (only when confirmed),
status of decisions (including design absent or applicability unconfirmed),
actual changes and read-back evidence, plus limitations
and next needed substantive result. Include the full unsaved proposal/version
or verified candidate address/version as applicable, and saved result addresses after saving,
acceptance decision address/status, pending immutable refs, and separate local,
Git and tracker publication facts. Full document-only `ok` requires accepted
checked content/decision and verified Git receipt. Explicit limited local save
can be `ok` for that contribution with pending immutable refs and remainder.
`ok` for the full combined result requires
the accepted published spec, matching record and verified tracker publication.
If a document write succeeds
but tracker creation fails, or a response is ambiguous, reread both states,
report the saved address and all confirmed IDs/changes, stop further writes
and leave a precise handoff for reconciliation; do not repeat unchanged acceptance,
roll back, blind-retry
or claim the task exists. On interruption before acceptance, return the known
decisions and accessible sources in the response without creating a mandatory
draft store. Give a recipient without this chat enough references, version,
statuses, rights, verified effects and unresolved decisions to continue. Stop
after the requested result is checked. Full publication is executed by existing
owners and consumed here; limited transitions belong to the caller.
Do not initiate
decomposition, technical planning or implementation.

For a noninteractive component return a short handoff: status, scope/mode,
full unsaved proposal with version/scope or verified saved result address and
candidate revision or confirmed ID, decision/evidence, limitations, actual effects
and decision needed. The caller forwards complete text/version or an accessible
file address/version with the separate decision to the next recipient; the
consumer reads and checks it without foreign chat. Never substitute an unverified
"done" for this result or require a file for a response-only proposal.
