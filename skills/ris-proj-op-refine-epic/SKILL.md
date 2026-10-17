---
name: ris-proj-op-refine-epic
description: >-
  Clarify one existing RIS roadmap epic whose outcome or boundary is too unclear
  to choose a feature: propose bounded feature outcomes and prerequisites, and
  optionally verify an agreed update to that epic through the selected adapter.
  Include light product/architecture boundary and linked-source impact checks.
  Use for epic refinement, not goal-level roadmap planning, selecting a feature,
  creating feature tasks, or specifying every feature in advance.
---

# Refine one epic for feature selection

Own a checked **project-scoped epic refinement**: an evidenced outcome and
boundary, coverage by a bounded set of prospective features with necessary
prerequisites, and, only when authorized and safe, a verified update of the
existing epic. This skill has no independently useful portable planning
method to split out: the result depends on an actual epic, accepted goal,
project sources and an optional tracker update. `ris-port-op-plan-roadmap` plans
goal-level epics, not the feature boundary of one epic. Direct invocation
works in the current agent; do not require an execution role or launch another
lifecycle stage.

## Establish the epic and evidence

Full finished refinement is default; an explicit proposal-only or local-write-only
contribution names its boundary and remaining publication. Nesting/Gas City does
not select limited mode. With an ID discover accepted goal, current sources and
decisions from exact epic reads/links before asking for unavailable facts.

Identify the selected project and current worktree, confirmed epic ID, accepted
goal and its source, why the epic's outcome or boundary prevents a defensible
feature choice, prior decisions and started work, read scope and any explicit
write permission. An explicit proposal-only request remains read-only. A goal
document's mere existence does not establish acceptance; a tracker title does
not establish an epic's identity. If an epic ID or goal membership is ambiguous,
ask before dependent work; do not convert this into planning a new roadmap.

Ensure installed `ris-proj-lib-common` is available and apply it and its conditional
resources before governed actions. Use installed `ris-proj-op-resolve-context` with its
configuration resource for this project: resolve `sources.rules`, relevant
`sources.product` and `sources.specs`, and `adapters.tasks.skill` for tracker
reads and possible writes. Check status, provenance, diagnostics and permissions;
an invalid explicit configuration does not fall back to defaults. In a worktree
resolve sources from its current root, and use shared paths only after the
primary root is established. Select applicable documents by content and links,
not guessed filenames. Read the selected project's rules, accepted goal and
epic-related constraints; distinguish current tracker content from intended
future behavior.

Ensure the selected adapter is installed and available in this project, with
compatible `tasks` v1 `tasks.epics.read`, complete all-status
`tasks.epics.list` and typed `tasks.blocks.list` for the relevant goal and
epic dependencies. Apply its read operations, not direct tracker commands:
verify the epic's exact ID, `epic` type, status, goal membership, content,
existing blockers and related open/closed epics. Read accessible already-started
work and specifications through applicable project sources and adapter task
reads **only if supported and necessary** to avoid losing or duplicating it;
mark unavailable evidence rather than inferring absence. An inaccessible
adapter blocks a claim of verified tracker state, but independent documentary
analysis may be returned as an explicitly unverified proposal.

## Produce a bounded refinement

First check whether the epic already has a sufficiently clear, verifiable
outcome, boundary and completion conditions for feature selection. If so,
report that evidence and `changes: []` and apply the publication/no-debt check
below in full mode; do not subdivide an epic merely for its
size or demand detailed specifications of every future feature. If unclear,
work only on the ambiguity that prevents selection. Reconcile accepted goal
scenarios, the epic's existing outcome, exclusions and commitments, its
blockers, completed work, and overlap with other epics. Do not silently move
scope between epics, contradict a closed result or change the goal-level
roadmap. An unresolved cross-epic change requires the goal-roadmap owner, not
an implicit update here.

Extract relevant accepted behavior from freely structured product material, not
from document/module boundaries; do not require global product IDs or rewrite
author text. Compare only linked source scopes/current versions to baselines in
the epic and related specs/designs. Distinguish editorial change from material
behavior change; missing baseline leaves currency unconfirmed. Trace a material
delta via existing permanent `slug#AC-nnn`, task IDs, tests/evidence and design
links; inspect supported task/identity reads when needed and report missing links
instead of guessing slugs or creating a registry. Unavailable reads block the
dependent conclusion/write, not independent documentary analysis.

Before settling candidate boundaries do a light check against current code/rules
and related active accepted design scopes: responsibility/state ownership,
existing/shared interfaces, incompatible or undefined contracts and research risks.
For a new project use its minimal foundation; do not design every candidate or
mandate a technical style. Shared files are not themselves a conflict. Identify
conflicting owners/scopes/versions and propose one coordinating integration owner,
a common contract version to agree and necessary blocked → prerequisite direction;
keep unrelated candidate work available. Missing architecture evidence is a gap,
not permission to declare all boundaries compatible. Substantial design changes
go to their design owner, changed behavior to requirements authority and changed
global invariants to architecture authority. Preserve unaffected acceptance and
local implementation freedom. Do not accept/rewrite designs or add task blockers.

Describe the smallest coherent set of **candidate feature outcomes** needed
to account for the epic's mandatory scope and a nearest verifiable slice;
one feature, or the epic itself as a feature, may suffice. State each candidate's
observable result, boundary and relevant acceptance evidence or open decision.
Map mandatory outcomes and exclusions to candidates or an explicit gap.
Express only necessary directed prerequisites and why they are necessary;
distinguish an actual typed epic blocker from a proposed prerequisite between
features. Check for cycles, duplicate or contradictory outcomes and unjustified
sequencing. Reuse still-relevant started work without treating a suggested
candidate as a tracker record or an accepted feature specification. If
interdependent material decisions cannot be resolved from sources, ask them in
one dialogue under `ris-proj-lib-common`; apply installed `ris-port-op-interview` only when
its decision-tree method is genuinely needed, confined to this epic. Neither a
second full interview nor an interview about all future features is required.

Present the proposed refinement and its coverage, uncertainties and material
changes to the epic's outcome, boundary, exclusions or completion criterion.
Obtain agreement to the **specific changes** before any write; a general
request to refine an epic or permission to write is not acceptance of their
content. Reuse already recorded explicit acceptance of the same changes;
absence of a request for consultation does not waive acceptance. If agreement
or a material decision remains open, return the supported proposal and stop
dependent writes.

## Update only the epic when permitted

Persist only agreed changed fields of the **confirmed open epic** and only
with explicitly authorized write scope. A read-only proposal, unchanged epic,
closed epic or absent permission needs no update. Proposed feature candidates
and their prerequisites may be reflected in the agreed epic's readable content
if authorized, but do not create feature `task` records: those require an
accepted specific specification and its acceptance evidence. Do not add/remove
tracker `blocks` edges between epics as a side effect of refining this epic;
if the proposal requires changing goal-level dependencies, return the gap to
the roadmap owner. Never turn a proposed feature prerequisite into an epic
edge or manufacture a feature ID.

Before a needed write require compatible `tasks.epics.update`, a selected
adapter that actually provides it, and its targeted native update/read-back
protocol and actual limits. Fresh comparison is not universal lost-update CAS;
ordinary authorized shared-epic updates require no manual window, global lock
or separate risk question. If an explicitly required stronger atomic guarantee
is unsupported, return that exact limitation and retain the unsaved proposal.
Re-read the target epic, its goal membership,
status, current fields and relevant typed blockers immediately before updating;
compare with the agreed version. An unexpected change or a closed epic is a
conflict, not permission to overwrite. Pass only approved fields and expected
state to the adapter. On an ambiguous or failed response reread actual state,
report confirmed changes, then stop further writes; a subsequent invocation
reconciles saved content rather than blindly repeating the update.

Fresh-read the epic and relevant goal records/dependencies after updating;
verify ID, status, unchanged fields, agreed fields, goal coverage and absence
of contradictory changes. A persisted edit does not itself approve the
proposed candidate features or prove that their specifications exist.

## Return and stop

In full mode, after semantic and local read-back verification invoke the selected
adapter's separate tracker publication operation with exact epic/content,
destination evidence and authority for the entire outgoing history. Preflight
remote-gated writes through that owner before mutation. Inspect its required
revision/fresh remote reachability receipt alongside local refinement checks;
remote revision assurance is not independent field equivalence. An
unchanged epic still needs required availability/debt checked, without empty
push. No synthetic Git step. Missing authority or failed/ambiguous publication
blocks full success; retain known effects and reconcile with the same owner
before retrying only the missing operation. Limited mode returns its checked
contribution and exact publication remainder, without a copied Dolt algorithm.

Report `ok|blocked|conflict|error` for this bounded result; distinguish an
`ok` **proposal** from an `ok` verified persisted refinement. Include project
and config provenance, goal source and acceptance state, epic ID/status,
observed baseline and updated fields, candidate outcomes and requirement
coverage, proposed prerequisites versus existing typed blockers, open
decisions, evidence of agreement, permission scope, `changes` (including `[]`),
read-back evidence, concurrency limits and the exact next substantive result.
Include compared source scopes/versions and currency verdict, located impact
links/gaps, light boundary-check evidence, proposed contract coordinator/version/
prerequisites, and independent candidates still available. Unresolved material
source or contract decisions block only the affected refinement/write.
Where input, approval, operation or guarantee is missing, give the verified
partial result and reason without claiming a saved refinement. Include enough
accessible addresses and IDs for continuation without this chat. Do not choose
the feature for the user, create tasks, specify features, initialize a tracker,
claim/close records or launch implementation.
