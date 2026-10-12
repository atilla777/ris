---
name: ris-prepare-feature-work
description: >-
  Guide one RIS project feature from a verified roadmap choice through an
  independently accepted published requirements and design, and remotely
  verified tracker tasks in one
  conversation.
  Use for the full interactive feature-preparation workflow; not for only
  selecting a feature, interviewing, drafting a specification, decomposing an
  already accepted feature, technical planning, or implementing work.
---

# Prepare one feature for technical planning

Own the **end-to-end readiness and handoff**, not the methods or independent
results of the component skills. This is one RIS scenario skill: it coordinates
project-specific sources, two actual execution roles, a single user dialogue,
independent requirements/design acceptance and tracker state. There is no useful independent RIS-free base
method to extract. Direct invocation runs in the primary conversation; no
universal orchestrator, separate CLI session or mandatory draft store is
required. Publish preparation artifacts as part of the combined result; stop
before technical planning, claiming, implementation or closing a tracker
record. Never treat a workflow request as approval of
specific, not-yet-shown requirements or tracker mutations.

## Establish project and gates

Identify the selected project/current copy and, if shared workspace paths are
needed, its established primary-copy root. Obtain an explicit epic ID or
accessible roadmap scope, accepted goal, applicable project rules and sources,
prior work and linked artifacts, read/write permissions, and how this project
records acceptance of specific requirements and independently scoped design.
Distinguish confirmed IDs and
decisions from proposals. Do not use a local development queue as a feature
tracker; do not substitute a historical roadmap pointer for a current tracker
read. An ambiguous project or prohibited read/write blocks only dependent
work, not an independently supportable read-only handoff.

Ensure installed `ris-common` is available and apply it and its conditional
dialogue, artifact and quality resources before governed actions. Apply
installed `ris-context` with **its configuration resource** for this project's
rules, related product, specs, selected tasks adapter and both `execution.roles`.
Check status, provenance, diagnostics, project/worktree paths and scope. An
invalid explicit config is an error, not a reason to use package defaults;
`sources.specs` and `workspace.tasks` are base directories, not required
filenames. Select relevant documents by links, content and acceptance state.

Because `ok` promises remote availability, preflight publication **before
writing accepted requirements/design or tracker records**: determine the
project's authorized Git destination/branch and publication rules for the
specific documents and decision evidence, the selected adapter's separately supported remote
publication mechanism (not assumed from `tasks` v1), configured destination
and ability to verify it. Establish permission to commit/push the accepted
document and publish these tracker records; permission to save locally or the
command invocation alone does not grant remote rights. Inspect current Git
branch, index, working changes and remote tracking without including other
work. Inspect all commits outgoing to the destination and active commit/push
hooks for side effects (including tracker auto-publication); require a way to
keep tracker writes local until their own publication gate. Ask the adapter to
check outgoing tracker history and unrelated records now, not only at push
time. If either channel or isolation cannot be established, return a read-only
proposal or `blocked`; do not knowingly create artifacts that cannot reach
this scenario's required result. Direct component invocations retain their own local stop
conditions. Do not require a Git/Dolt remote from a project using a different
authorized publication mechanism; require equivalent checked availability.
For Beads pass the checked `bd --sandbox` isolation condition to both the
feature-task creation, design-record updates and child/edge operations; verify none publishes
implicitly. A local adapter success is not remote evidence.

Preflight the selected adapter's `tasks.feature-record/1` read and conditional
update support, supported initial feature-record creation and all needed v1
reads/child writes. Require its independent writer guarantee before dependent
record writes; for Beads, initial unique-slug creation covers all project feature
creators, and updates cover the feature, children, blockers and evidence through
read-back. Establish short actual write windows after dialogue/acceptance, never
treat claim, sandbox or read/write/read as locks. Ensure installed design owner
and its portable method/resources are available before promising this route.

The scenario requires semantic roles `feature-selection` and
`task-decomposition` for its two bounded operations. From the prepared project
configuration, verify each named agent actually exists as an available
**subagent** in the current host and can be invoked; check both before promising
a fully writable workflow, and again before the dependent call if the host
changed. A configured string, a loaded skill, or a summary in this conversation
does not establish availability or launch. Do not silently execute either role
in the primary context, pick a fallback agent, or assume a model tier. If a
role cannot be launched, mark its step blocked and preserve any independent
verified results. Direct calls of component skills do not need these roles.

## Select, confirm and, only when needed, refine

Launch the configured `feature-selection` subagent with a **bounded read-only**
assignment to load and apply installed `ris-select-next-feature` and its own
dependencies. Pass the selected project/root and config provenance, accepted
goal and sources, explicit epic ID if confirmed, applicable earlier work and
scope, `changes: []`, and the requested checked recommendation or blocker.
Specify that local development PLAN entries are evidence of prior work, not
automatically feature outcomes or tracker IDs. Do not delegate questions to
the user: ask them here if multiple ready epics or features need their choice,
then pass their confirmation back to the bounded selection operation. Require
the actual subagent invocation and check its returned epic status, typed
blockers, task evidence, sources and proposed versus confirmed identity;
independently inspect decisive accessible IDs/links when possible. An answer
that recommends a local work item instead of a feature, or just says “done”,
does not clear this gate. Never auto-accept the subagent's recommendation.

If the chosen epic's **outcome or boundary** prevents a defensible feature
choice, apply installed `ris-plan-epic` in this dialogue only for that ambiguity;
it owns refinement and any separately authorized update of the existing epic.
Agree material changes before its writes and verify the updated epic through
the selected adapter before requesting selection again. Do not refine merely
because an epic is large, create speculative feature tasks or alter goal-level
dependencies as a shortcut. Confirm the person's selected small, verifiable
feature outcome and epic; keep alternatives, open decisions and prior work in
the handoff without treating a candidate as an accepted specification.

## Specify in one dialogue

Apply installed `ris-specify-feature` **here in the primary conversation** with
the confirmed feature/epic, selected project, known decisions and sources,
permissions, proposed document address/format where known and acceptance
mechanism. It owns the content and substantive coverage through
`ris-formulate-spec-base`, conditional requirements interview through
`ris-interview-feature`, the actual project-specific acceptance, save and
feature-task operation through the selected compatible adapter. Coordinate
known answers so no second full interview begins; a single clarification is
not automatically an interview. Do not copy these methods into this scenario
or send acceptance decisions to a noninteractive subagent. A general request
to reach tasks does not accept the **particular content**: let the owner show
it and obtain acceptance of that version *before* writing to its accepted
path. Confirm exact path, applicable format, durable acceptance-evidence
address, permission and adapter operations before writing. Do not invent a
file name or acceptance record from config, a title, an old chat or a file's
existence. If interrupted before acceptance, return the known decisions and
accessible sources explicitly in the response; no required saved draft.

Require from `ris-specify-feature` fresh-read evidence for the accepted saved
version and matching open feature `task` under the confirmed epic (type, ID,
parent, stable key, spec link and decision address). Check accessible artifact
and tracker references, not its `ok` alone. If the file was saved but creation
failed, preserve its address and status, reread facts and stop before child
writes; never invent a feature ID or roll back another owner's change. A
proposal, missing write permission, incompatible adapter, absent acceptance
mechanism or unsupported version cannot satisfy this gate. Do not bypass the
selected adapter by calling its backing tracker directly.

## Design in the same dialogue

After requirements and the feature task are verified, apply installed
`ris-design-feature` **in the primary conversation**. Pass confirmed project/
config, epic/feature ID and permanent slug, requirements path/scope/digest and
decision address, actual code/contracts and related active accepted designs,
prior design if any, known answers and separately permitted document/ADR/record
effects. It applies `ris-design-feature-base`, owns technical decisions and
independent acceptance/save/update; do not duplicate its method or delegate
user decisions. A short design can share `spec.md` with independently hashable,
nonoverlapping scopes; use separate `design.md` when necessary, including when
requirements already hash the whole spec. Do not force a second full interview
or reaccept unchanged requirements on design revision.

Check actual saved requirements/design scoped bytes and both accessible
decisions against the fresh feature record, not a file's existence or component
`ok`. A saved design with an old record is partial and blocks child writes.
Require sufficient test seams, applicable contract versions and resolved
material product/architecture conflicts; no `ready` status is introduced.
For substantive design conflict/revision coordinate targeted impact with this
owner and reconcile affected AC/tasks/contracts before decomposition. Changed
behavior returns to the requirements owner; preserve independent results and
unchanged acceptance. Future architecture stays in design/ADR, not current
rules or unauthorized product edits. No generic restart of the whole roadmap.

## Decompose only an accepted, identified and designed feature

Once both saved scopes/versions, independent decisions, design/contracts and
feature record have been checked,
launch the configured `task-decomposition` subagent with a bounded assignment
to load and apply installed `ris-decompose-feature` and its own dependencies.
Pass the current project/config and primary root if needed, confirmed epic and
feature IDs/slug, exact saved requirements and design paths/scopes/digests and
both accessible decision addresses, applicable contracts/versions and test seams, existing
child IDs if any, relevant rules/technical inputs, permitted task/edge write
scope and expected coverage. No user dialogue in the subagent: return unresolved
choices here before authorizing further writes. The child skill applies
`ris-decompose-spec-base`, checks the selected adapter's compatible `tasks` v1
operations plus `tasks.feature-record/1` read and guarantees before dependent
writes, computes current readiness, reconciles all-status
children and directed blockers, and verifies actual content and IDs. The
scenario does not design tasks or issue raw tracker writes. One sufficient
feature task with a verified empty child set needs no artificial child; for
multiple units require coverage of accepted criteria and justified edges.

On a missing role, acceptance, adapter operation or guarantee, report the
verified partial state and stop the affected action. On an ambiguous, failed or
partial write, **stop further writes**, reread all affected IDs, exact saved
requirements/design and both acceptance sources, complete direct-child set and relevant typed
edges through the selected adapter before retry; retain confirmed changes,
keys and links. A later invocation must reconcile the same facts first, not
blindly recreate tasks or accept stale decisions. For strict uniqueness require
an established exclusive writer window; the default best-effort create does
not promise it. Do not improvise a missing adapter operation with direct CLI
or use read/write/read as a content-update lock.

## Publish the verified preparation result

After the task set and acceptance source are verified, run project-required
checks and independent review of the **specific requirements/design versions**
and their compatibility before publishing. If findings change an accepted scope,
obtain focused acceptance of that changed result and reconcile dependent tasks;
unchanged requirements need no renewed approval for a design-only change. In
projects using Git, stage only authorized specification files, inspect the
index/final diff and refuse to include unrelated staged or working changes.
Include the separate design and authorized acceptance/ADR evidence when needed;
do not publish only `spec.md` while design remains local. Commit only those files;
after hooks ran, inspect the new commit's tree and
every commit outgoing to the confirmed remote ref. If hooks changed accepted
content or published tasks before the tracker gate, stop and reconcile; never
push a changed or unrelated commit. Push only to the confirmed project-authorized
branch/remote. Check the remote ref and that the pushed version contains the
exact accepted requirements/design scopes and both decision addresses. Hash
both scopes from the actual remote Git tree in an independent fetched copy;
also resolve permitted ADR/contract evidence there. Never assume a branch named `main`, silently force-push,
or treat a successful local commit as publication. The scenario owns this
limited preparation-artifact publication; it does not invoke an
implementation-change publisher or publish unrelated source code.

Then request the selected adapter's **separate** remote-publication operation
for the confirmed feature (including its complete requirements/design record),
all required children and typed edges. For Beads it
must verify the configured Dolt remote, not infer publication from Git push;
for another tracker require its own checked mechanism and guarantees. Check
remote-backed reads of exact task IDs, content, parent, spec link and decision
addresses and both scoped digests, children and blockers, and confirm both
published logical results and their decisions can be
resolved from the recipient's project copy. Neither command output alone nor
local read-back clears this gate. If Git publication fails, stop before tracker
publication; if tracker publication fails after Git succeeded, do not undo or
claim an atomic result. Report each channel's actual state and recovery action.
On retry reread remote Git requirements/design scopes, both decisions and all
affected remote tracker records before any new push or creation; reconcile
changed identity, content or edges as `conflict`. Do not overwrite someone
else's concurrent changes or blindly repeat writes.

## Verify combined result and hand off

Verify the person's chosen outcome and epic, accepted **published version** with
reachable independent requirements/design decisions and matching scopes/digests,
open feature task and parent/slug/link identity, all
direct children and blockers where applicable, requirement coverage and
readiness of one selected unit for subsequent technical planning and remote
availability of the specification and tasks. Check actual file, remote Git
and adapter reads and the subagents' results; neither a status line nor
their reports alone prove the combined result. Reconcile competing or changed
sources as `conflict`; never mask partial effects with an `ok` from a component.
Return `ok|blocked|conflict|error` for the **whole scenario**, project/config
provenance, confirmed epic/feature/child IDs and permanent slug, requirements/
design paths, scopes, digests, acceptance addresses/status, contract versions/
test seams, computed readiness, scope and decisions, task coverage and directed blockers,
actual local and remote changes (`[]` if none), Git commit/ref and tracker
publication evidence, checked limitations. For a partial
result include confirmed saved files/records and unmade work, open decisions,
permissions and the exact recovery action. Give a future recipient accessible
addresses and sources without depending on this chat or a newly invented
handoff store. `ok` requires both independently accepted published results and
remotely verified task set; a user may instead receive an honest unsaved
proposal or blocker, or a saved but not fully published partial result.
Stop without technical planning or implementation.
