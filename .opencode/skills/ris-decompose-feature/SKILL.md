---
name: ris-decompose-feature
description: >-
  Verify an accepted feature specification and its tracker task in a RIS project,
  then check the one-task case or create and verify necessary child tasks and
  dependencies through the selected tasks adapter. Use for project-scoped feature
  task decomposition; not for choosing or specifying a feature, drafting a
  portable task proposal alone, or planning technical implementation.
---

# Decompose an accepted feature into verified project tasks

Own the **combined project result**: a confirmed accepted feature specification
and matching feature task, a sufficient single-task outcome or verified child
tasks and directed blockers, and traceable coverage. Apply installed
`ris-decompose-spec-base` for the substantive work proposal and its coverage
check; use the selected installed `tasks` adapter for bounded tracker reads and
writes. Neither a base proposal nor an adapter success message proves this
combined result. This wrapper owns project input selection, permissions,
reconciliation, verification and handoff, not requirement acceptance or the
base's decomposition method. The semantic execution role is
`task-decomposition` for a caller assigning a subagent; **direct invocation**
runs in the current agent without requiring an `execution` role or claiming
isolation. Do not initiate another lifecycle stage.

## Confirm inputs and scope

Identify the selected RIS project and current copy, confirmed feature `task`
ID and epic parent, exact specification address and version, accessible
acceptance decision for that version, relevant technical/project constraints,
prior task IDs and permitted read/write scope. Resolve ambiguous feature,
project, primary-copy root or acceptance source before dependent action. A
request to decompose does not accept an unapproved specification; a file,
format check, cached summary or a task description alone does not prove
acceptance. If the content or decision has changed since the linked task was
created, stop for reconciliation rather than silently rewriting that task.

Apply installed `ris-common` and its conditional resources before dialogue,
artifact work and completion checks. Use installed `ris-context` with its
configuration resource to prepare `sources.rules`, relevant `sources.product`
and `sources.specs`, `adapters.tasks.skill` and, if needed, shared workspace
paths in this project. Inspect status, config provenance, diagnostics and
permission scope; select relevant documents by actual links and content, not
assumed filenames. In a worktree, source paths use its current project root;
shared paths need an explicitly established primary root. An invalid explicit
config is an error, not a reason to fall back to defaults. The project decides
its specification format and mechanism of acceptance; verify accessible
evidence addresses and their match to the saved version, not merely a flag.

Ensure the selected adapter is installed and actually available in the chosen
project. For a read-only result require compatible `tasks` v1
`tasks.items.read`, `tasks.children.list` and `tasks.dependencies.list` with
exact-ID and complete all-status child selection and full typed directed
blocker reads (including for the feature task itself). Before a needed child
write additionally require `tasks.items.list` and `tasks.items.create`; before
a needed edge write require `tasks.dependencies.add`, with the applicable full
all-status identity search, stable scoped keys, confirmed parent/content
read-back, directed typed blockers and cycle checking. Determine missing work
from reads first, then check each operation and guarantee **before** its
dependent write, including the required concurrency level. A configured
adapter or a similarly named CLI command is not evidence of support; never
bypass the adapter by calling `bd` or editing tracker storage. Read the feature
task; confirm its `task` type, open status, epic parent, scoped identity, exact
spec link and acceptance-evidence address **in either its readable content or the
linked specification**, and reread the saved specification and decision.
Cross-check their identity and status; a closed feature or mismatched link
blocks child creation. Read all existing direct children and relevant blockers,
including closed tasks, before deciding whether new work is needed.

## Apply the method and reconcile actual work

Ensure installed `ris-decompose-spec-base` is available and **apply** its
method to the current accepted version, feature scope, relevant rules and
technical inputs, and verified existing work. Obtain its bounded work units,
observable checks, requirements mapping, justified directed prerequisites
and explicit gaps. Do not duplicate its partitioning algorithm here. If a
missing criterion or conflicting accepted decision blocks coverage, report
the supported partial proposal without creating tasks for disputed scope.
Compare the proposal with existing children, including their content, state
and source coverage; existing tasks are not automatically completed work.
Unrelated or conflicting children, unknown coverage, duplicate identity or
an unexpected blocker prevent a claim of full readiness; do not silently
delete, update, reparent or replace them. Resolve material changes to the
accepted spec with its owner before writing.

If the bounded feature can be done as **one task**, check that the existing
feature task itself expresses its outcome and completion criteria and covers
the accepted requirements. Inspect its full typed blockers as well as a
complete empty direct-child set (or reconcile any actual children); do not
create a copy of the feature as its own child. An existing feature task that
lacks required content cannot be silently updated under `tasks` v1: return
`blocked`/`conflict` with the gap, even if the base proposal is good. For
multiple units, require exact authorized scope only
for missing child or `blocks` writes; a fully persisted set can be verified
read-only. Agree approved task content and stable retry keys scoped to the
confirmed feature; preserve spec reference, requirement coverage, observable
criteria, exclusions and justified edge direction (blocked → blocker). Do not
invent tracker IDs from titles, equate parent membership with a blocker, or
turn a preferred order into a dependency.

Before each mutation, compare current all-status children, candidate identities
and blockers with expected state. Through the adapter, create only missing
children with `tasks.items.create` under the confirmed open feature task;
reuse only exact matches on key, type, parent, content and relevant links.
Different content, closed/moved parent, multiple matches or unmatched existing
children are `conflict`, not permission for an implicit update. Default create
is best-effort with full search/read-back; if strict no-duplicates is required,
establish an external exclusive writer window before searching/creating or
stop. Re-read each ID, parent-child membership and content; only then resolve
the proposal's local labels to real IDs. Add necessary `tasks.dependencies.add`
edges only with confirmed task endpoints in this feature scope after reading
their existing typed `blocks` edges; verify no cycles and exact direction on
fresh reads. Preserve an already matching edge without a fake change.

On a failed, ambiguous or partial adapter response, **stop further writes**.
Reread all affected IDs, full direct-child set and relevant edges before any
retry, report verified existing children, keys, links, actual added edges and
unwritten work. A subsequent invocation reconciles these facts and the current
accepted specification before attempting only genuinely missing operations;
do not blindly recreate children or overwrite a changed requirement. For a
stronger uniqueness or content-update guarantee than the selected adapter
provides, stop instead of substituting a direct tracker operation.

## Verify and return

Fresh-read the feature and full child set, each task's actual content, status,
parent and applicable links, and all required directed blockers. Recheck the
saved specification and its acceptance evidence for the same version; map
every accepted criterion to the verified feature or child tasks, and name where
combined behavior will be checked. Confirm no contradictory extras or cyclic
dependencies. A dependency on unconfirmed external work or a missing
criterion prevents `ok`; mere presence of children or an adapter `ok` does
not prove coverage. Report `ok|blocked|conflict|error` for **this combined
result**, the project/config source, feature and epic IDs, spec address and
version with acceptance-evidence address, actual child IDs/keys and statuses,
directed dependencies, requirement coverage, `changes` (including `[]`),
read-back evidence, limitations and exact next needed substantive result.
For partial outcomes use the reason's non-`ok` status and distinguish confirmed
changes from unmade ones; include sufficient accessible references, scopes,
permissions and open questions for continuation without this chat. Do not
plan technical steps, claim or close tasks, approve the specification, or
launch implementation.
