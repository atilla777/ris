---
name: ris-proj-op-plan-roadmap
description: >-
  Create or update a project's roadmap as verified tracker epics and preliminary features,
  or propose it without writing. Use for project MVP outcomes, epic boundaries
  and dependencies, including bounded product/architecture impact on revision;
  not for a single feature's tasks, raw tracker operations,
  initializing a tracker, or implementing an epic.
---

# Project roadmap

Own the **combined project result**: selected accepted inputs, a checked
goal-level proposal, reconciliation with all existing tracker epics and a
verified saved roadmap when authorized. `ris-port-op-plan-roadmap` owns the
portable proposal method; this skill owns project selection, integration and
the adequacy of the persisted whole. Do not duplicate its planning algorithm.

## Combined epic and feature depth

One invocation/session owns epics **and** the selected preliminary feature graphs.
Depth comes from the request: `epic-only`, `nearest` (default), or `all`. One MVP
epic with several features is a complete roadmap; never split it artificially.
Determine the nearest stage from accepted goal/constraints and observed starting
state, not tracker ordering or guessed priority; ask if materially ambiguous.
`epic-only` may be detailed later by a standalone epic-graph operation. Planning
does not start requirements interviews, specs/design or implementation tasks.

After the portable epic proposal and before human agreement or any graph writes,
apply installed `ris-proj-op-plan-epic-features` as an explicitly **proposal-only**
contribution for selected nearest/all epics. Its base can receive anticipated epic
context/local labels before parent creation. Supply shared product sources,
all-state work, other proposed epic boundaries and actual neighbor context.
Optional isolated parallel proposals use existing `task-decomposition` only when
delegated; no direct-invocation role requirement. The lead reconciles cross-epic
coverage, overlaps, identities and dependencies across the whole result before
presenting one concrete epic+feature graph for human agreement. Endpoints outside
approved epic scope require an explicit scope decision. Do not run graph planning
on every nonempty blocked epic: all-blocked requires diagnosis, not new features.

Agreement below includes the selected concrete feature graph and material deltas,
not just epic boundaries. A consultation waiver for epic breakdown does not waive
feature graph agreement. Proposal-only stays zero writes. With agreed write scope,
the lead applies epics serially through their adapter owner and verifies exact IDs,
then requests explicitly local-only graph-owner contributions for those parents
and approved graphs. Labels resolve only after create/read-back; retain the graph
owner's full reconciliation and targeted-write checks. No per-epic duplicate pushes:
the lead checks the whole persisted epic+feature result and owns separate tracker
publication. Any parent/feature/edge failure stops further writes, preserves IDs
and reports exact partial effects; no fake atomicity, rollback or blind recreate.
Resume reconciles effects before only missing agreed operations.

## Prepare the operation

Full finished planning is default; explicitly proposal-only or local-write-only
contributions name their boundary and remaining publication. Nesting/Gas City
does not silently select limited mode. Full mode publishes tracker effects,
not a synthetic Git roadmap commit. Missing write/publication authority returns
an honest proposal or blocked full result, not implicit limited success.

Establish the selected project/root (and context-checked explicit or verified
saved primary selection/provenance if shared paths are needed from a worktree),
chosen goal and evidence of its acceptance,
`mode: create|update`, and precise write scope. An explicit proposal-only
request has `write: false`; without permission default to no write. Do not
infer goal acceptance from a file's presence or infer present capabilities
from a target vision. An absent accepted goal permits a labelled draft goal,
not a claim of a complete accepted roadmap. Ask for a missing mode before a
write; never turn an `update` into a `create` or vice versa.

Ensure the installed `ris-proj-lib-common` is available and apply its rules and
conditional resources before their governed actions. Use installed
`ris-proj-op-resolve-context` and its configuration resource for **this project operation**:
resolve applicable `sources.product`, `sources.rules`, `sources.specs` when
needed, and `adapters.tasks.skill` for tracker operations. Check the returned
status, provenance, paths and scope; a configured adapter is not an available
adapter. Select the actual applicable accepted high-level documents from the
prepared directories, explicit inputs and their links; read project rules,
relevant specifications and evidence of the current state. Do not require
OKF, all documents in a directory, or a pre-existing output directory. If
accepted sources conflict, identify the affected content and stop its write.

Use author product material in its own structure, separating accepted rules,
examples, atmosphere and open questions; never rewrite it or demand global IDs.
For revision, retrieve the relevant prior source addresses and versions from
existing epics/specs/designs, and compare the linked scopes with current sources.
No whole-product scan: expand only through evidenced affected links. Retrieve
related active accepted designs/current contracts when a boundary may intersect;
check their acceptance scopes/versions rather than treating any design file as
accepted. Missing baselines or unavailable designs leave those claims unverified.
For task/AC/evidence tracing require the adapter's actual all-status task and
dependency reads only when needed; a roadmap-only adapter does not imply them.
Read confirmed feature identity/slug/AC/spec links through its declared capability
when needed, or use verified readable existing links; do not guess legacy slugs.
If a needed read is unavailable, return a partial impact report and block only
dependent writes. Link permanent `slug#AC-nnn`, task IDs and existing tests/evidence
where available, without creating a parallel index or requiring test annotations.

Ensure installed `ris-port-op-plan-roadmap` is available; provide the selected
high-level specification, goal, observed starting state, constraints and,
for update, existing epics and confirmed accomplishments; also provide relevant
source versions/baselines, architecture/code facts and overlapping active accepted
contract scopes. Apply its boundary/currency/impact method to these actual inputs
to obtain a bounded proposal and gaps, not merely a loaded dependency. The
base does not receive project configuration as a required input. Coordinate
one dialogue across dependencies; resolve material decisions before writing.
If essential input or the base is missing, report the independent result and
block claims depending on it.

## Reconcile before any write

For tracker reads and writes, load the **selected and available** task adapter
and apply its declared `tasks` version 1 contract. Check compatibility and the
operations and guarantees needed for this request: `tasks.epics.list/read`,
`tasks.blocks.list` for reconciliation; `tasks.epics.create/update` and
`tasks.blocks.add/remove` when the agreed changes need them. Require complete
all-status epic enumeration (including closed), confirmed-ID reads and typed
directed-edge inspection in the selected workspace. The adapter owns tracker
commands, safe retries, permissions, and concurrency; do not bypass it with
direct storage edits, another adapter or a roadmap file. If no adapter is
selected in `adapters.tasks.skill`, or the selected adapter is missing,
incompatible (version, required operation or guarantee), or the workspace is
unavailable, no tracker write is possible; an explicitly requested proposal
without writing can still be returned as **unsaved**, with
unknown tracker state identified. No implicit tracker initialization.

Determine the full applicable set, **including closed epics**. Match by
confirmed IDs, a stable goal/roadmap membership reference in saved content
or tracker metadata, and meaning against the selected accepted goal; a title
or unverified uniqueness of a label alone is insufficient. Check related
records and links for scope and conflicting ownership. If existing records
cannot be enumerated completely or ownership/identity is ambiguous, stop
before writing; do not invent IDs, silently adopt another roadmap's epics,
or treat an ambiguous match as absence. Agree a stable per-goal and per-epic
identity for new records and include the goal, accepted input references,
outcome, boundary/exclusions, completion criterion and covered scenarios in
their saved content or confirmed metadata. Preserve that identity on update.
References must be resolvable by the recipient; a link to an inaccessible
document does not carry essential decisions. No second mutable roadmap file.

`create` requires a confirmed absence of that goal's roadmap across open and
closed records. A matching existing epic is a conflict, not permission to
create another. `update` requires an existing, unambiguous goal roadmap; an
empty or unidentifiable set is not a new create. Preserve existing IDs,
verified accomplishments, closed outcomes and closed-epic content. New
necessary epics may be proposed on update, but never retroactively rewrite a
closed epic, delete it, close it or change its status/assignee. Mark a
contradiction with an accepted closed result for resolution instead of
rewriting history. Differentiate a proposed new outcome from a confirmed
existing one and identify exactly which open epics and links need change.

## Save and verify only when authorized

Before writing, check the base proposal for unresolved blocking gaps and
check the **combined** result: goal scenarios and MVP boundary/constraints,
exclusions, first verifiable end-to-end result, each epic's useful outcome,
boundary and completion condition, scenario coverage, justified acyclic
blocking dependencies and order, and a reasoned next-epic recommendation.
Check its source-currency verdicts and bounded impact against retrieved project
links. Material product changes are proposals for the requirements owner, not
automatic changes to AC or acceptance. Common-contract conflicts need an agreed
owner/version/integration prerequisite before dependent roadmap writes can claim
readiness. Propose missing coordination; do not accept design or create task-level
blockers here. Independent epics can proceed with their separate evidence. Preserve
unchanged decisions on editorial changes; unknown source currency is not approval.
Nearest epic should be actionable for refinement; farther ones may be coarser.
Do not silently drop a required scenario or weaken numerical/negative
requirements. Check that every proposed epic has a justified independent
outcome or bounded uncertainty: one epic may be sufficient; phases of one
delivery do not become separate epics just to reach a target count. If
coverage or identity cannot be demonstrated, stop dependent writes and return
the proposal with the specific gap.

Before any tracker mutation, show the proposed epic boundaries, outcomes,
exclusions, completion conditions, first end-to-end slice, and material
dependencies to the person and obtain agreement to the **specific breakdown**.
For `update`, show and agree material changes to existing outcomes, boundaries,
exclusions, completion conditions, dependencies or order, and any new epics;
do not demand renewed acceptance of unchanged content. A generic
"create/update the roadmap" request or write permission does not approve the
breakdown. An explicit instruction to plan the epics **without consulting the
person** waives this agreement step, even when the person did not supply the
breakdown; a specific breakdown already explicitly accepted by the person
does not need re-approval. Neither exception supplies write permission,
accepted inputs, a mode, or adapter guarantees. If agreement is needed but
not obtained, return the unsaved proposal with `changes: []` and stop. If a
material change to the agreed breakdown becomes necessary before writing,
present the changed part again unless the explicit waiver applies. Do not
hold a tracker lock while waiting for a decision.

Translate agreed (or explicitly consultation-waived) changes into bounded
adapter operations on confirmed IDs: create or update only roadmap epics in
scope; add required `blocks` edges and remove **only** explicitly agreed
obsolete edges (blocked epic → prerequisite). Confirm exact endpoints, type,
direction, existing edge, scope and deletion permission before removal. Require
the adapter's bounded native removal and exact read-back with its honest limits;
an explicitly demanded stronger unsupported guarantee blocks that removal.
Never silently retain an agreed obsolete edge and claim a complete update.
Do not use a parent-child edge as a blocking edge, create tasks or modify unrelated
records, except preliminary feature records through the scoped graph owner above.
Authorized epic creation uses best-effort semantics without a
separate concurrency-risk question only when supported by the selected adapter;
if the caller requires no-duplicate creation, require its proven strict writer
guarantee or report its exact limitation before creation, without a pause request.
For content updates use the adapter's fresh expected-value checks, targeted native
fields/guards and read-back without manual windows or separate risk questions.
Preserve unrelated content and report native atomicity limits. Never present a mere
read/write/read sequence or an identity reference as a lock. Re-read relevant
records and edges before each mutation, compare with expected state, execute
one bounded action, and verify the returned ID, content, status and links by
fresh reads before proceeding. An uncertain response requires full
reconciliation before any retry; never blindly repeat a create. On a failed
or partial operation re-read all affected records, report confirmed changes
and unsaved parts, then **stop before further writes**, including link edits.
No automatic rollback, close, assignment or launch of the recommended epic.

Finally include selected feature graphs in coverage, preservation and publication
checks. Re-enumerate the goal's complete open and closed set, re-read saved
records and typed dependencies, and compare the **persisted whole** with the
accepted goal and agreed or explicitly consultation-waived proposal: content,
coverage, first result, exclusions, unchanged closed accomplishments, IDs,
status, links, order and recommendation.
For full mode, after this check invoke the selected adapter's separate tracker
publication operation with exact expected epics/links, destination evidence and
permission for the entire outgoing history. Preflight remote-gated writes through
that owner before mutation. Consume its required revision/fresh remote reachability
receipt alongside local IDs/content/direction checks of the agreed whole; remote
revision assurance is not independent field equivalence. No-change verifies
required existing availability or outstanding authorized debt without empty push.
On failure/ambiguity preserve local IDs/changes and ask the same publication
owner to reconcile actual remote effects before only the missing operation;
do not recreate epics or repeat unchanged acceptance. Explicit limited mode stops
at its declared contribution with this remainder. No Git/Dolt algorithm is copied.
If the check or required publication is incomplete, do not claim full success. Report
`ok|blocked|conflict|error`, mode, project, goal/input acceptance, actual
confirmed IDs and changes (including partial changes), breakdown agreement or
explicit waiver, evidence and its limits, unsaved proposal/gaps and the
recommended next epic with readiness.
Include source addresses and compared versions/scopes, currency/impact verdicts,
affected existing epic/AC/task/test/design links, proposed owner/contract version
and blocker direction, missing evidence, and available independent work. No
read-only impact finding authorizes changes outside the agreed roadmap epic scope.
Without write permission, return only a labelled unsaved proposal and
`changes: []`; even a complete proposal is not an accepted or persisted
roadmap. Stop at the epic/preliminary-feature roadmap: no technical task decomposition, implementation,
tracker initialization, Dolt setup or transition of source of truth.
