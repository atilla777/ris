---
name: ris-prepare-feature-work
description: >-
  Guide one RIS project feature from a verified roadmap choice through an
  accepted saved specification to verified tracker tasks in one conversation.
  Use for the full interactive feature-preparation workflow; not for only
  selecting a feature, interviewing, drafting a specification, decomposing an
  already accepted feature, technical planning, or implementing work.
---

# Prepare one feature for technical planning

Own the **end-to-end readiness and handoff**, not the methods or independent
results of the component skills. This is one RIS scenario skill: it coordinates
project-specific sources, two actual execution roles, a single user dialogue,
acceptance and tracker state. There is no useful independent RIS-free base
method to extract. Direct invocation runs in the primary conversation; no
universal orchestrator, separate CLI session or mandatory draft store is
required. Stop before technical planning, claiming, implementation, publishing
or closing a tracker record. Never treat a workflow request as approval of
specific, not-yet-shown requirements or tracker mutations.

## Establish project and gates

Identify the selected project/current copy and, if shared workspace paths are
needed, its established primary-copy root. Obtain an explicit epic ID or
accessible roadmap scope, accepted goal, applicable project rules and sources,
prior work and linked artifacts, read/write permissions, and how this project
records acceptance of specific requirements. Distinguish confirmed IDs and
decisions from proposals. Do not use a local development queue as a feature
tracker; do not substitute a historical roadmap pointer for a current tracker
read. An ambiguous project or prohibited read/write blocks only dependent
work, not an independently supportable read-only handoff.

Ensure installed `ris-common` is available and apply it and its conditional
dialogue, artifact and quality resources before governed actions. Apply
installed `ris-context` with **its configuration resource** for this project's
rules, concepts, specs, selected tasks adapter and both `execution.roles`.
Check status, provenance, diagnostics, project/worktree paths and scope. An
invalid explicit config is an error, not a reason to use package defaults;
`sources.specs` and `workspace.tasks` are base directories, not required
filenames. Select relevant documents by links, content and acceptance state.

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

## Decompose only an accepted, identified feature

Once the saved version, acceptance evidence and feature task have been checked,
launch the configured `task-decomposition` subagent with a bounded assignment
to load and apply installed `ris-decompose-feature` and its own dependencies.
Pass the current project/config and primary root if needed, confirmed epic and
feature IDs, exact saved spec/version and accessible decision address, existing
child IDs if any, relevant rules/technical inputs, permitted task/edge write
scope and expected coverage. No user dialogue in the subagent: return unresolved
choices here before authorizing further writes. The child skill applies
`ris-decompose-spec-base`, checks the selected adapter's compatible `tasks` v1
operations and guarantees before dependent writes, reconciles all-status
children and directed blockers, and verifies actual content and IDs. The
scenario does not design tasks or issue raw tracker writes. One sufficient
feature task with a verified empty child set needs no artificial child; for
multiple units require coverage of accepted criteria and justified edges.

On a missing role, acceptance, adapter operation or guarantee, report the
verified partial state and stop the affected action. On an ambiguous, failed or
partial write, **stop further writes**, reread all affected IDs, exact saved
spec and acceptance source, complete direct-child set and relevant typed
edges through the selected adapter before retry; retain confirmed changes,
keys and links. A later invocation must reconcile the same facts first, not
blindly recreate tasks or accept stale decisions. For strict uniqueness require
an established exclusive writer window; the default best-effort create does
not promise it. Do not improvise a missing adapter operation with direct CLI
or use read/write/read as a content-update lock.

## Verify combined result and hand off

Verify the person's chosen outcome and epic, accepted **saved version** with
reachable acceptance source, open feature task and parent/link identity, all
direct children and blockers where applicable, requirement coverage and
readiness of one selected unit for subsequent technical planning. Check actual
file and adapter reads and the subagents' results; neither a status line nor
their reports alone prove the combined result. Reconcile competing or changed
sources as `conflict`; never mask partial effects with an `ok` from a component.
Return `ok|blocked|conflict|error` for the **whole scenario**, project/config
provenance, confirmed epic/feature/child IDs, exact spec/version/acceptance
address and status, scope and decisions, task coverage and directed blockers,
actual changes (`[]` if none), checked evidence and limitations. For a partial
result include confirmed saved files/records and unmade work, open decisions,
permissions and the exact recovery action. Give a future recipient accessible
addresses and sources without depending on this chat or a newly invented
handoff store. `ok` requires the whole accepted specification and verified
task set; a user may instead receive an honest unsaved proposal or blocker.
Stop without technical planning or implementation.
