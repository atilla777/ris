---
name: ris-proj-flow-initialize-project
description: >-
  Initialize or safely resume a selected new or existing project's local RIS
  setup after package installation: agreed settings, agent instructions,
  separately accepted product/rules and checked RIS infrastructure. Use for
  project onboarding; not package installation, automatic rule updates, roadmap,
  feature preparation, product development or build/test/format/CI setup.
---

# Initialize a project's local RIS setup

Own the sequence, one human dialogue, bootstrap writes and combined checked local
result. This is a RIS-specific scenario coordinating independent owners, not a
portable initialization method or an installer extension. Component authors own
their subject methods, separate content acceptance and scoped saves; context
remains read-only. Direct invocation and `/risp-init` use the same contract.

## Establish the target and inspect first

Establish the selected project/current copy independently of this skill's
installation, requested outcome, authorized writer/acceptance authority and allowed
effects. Empty input establishes the target and scope; it never selects a task or
starts a lifecycle. Read applicable instructions, existing documents/decisions,
configuration, code, Git state, tracker and available tools/agents before asking
the person to restate facts. Distinguish accepted, observed, proposed, disputed,
unknown and deferred information with sources and currency. A file's presence is
not acceptance. Preserve existing useful structures, settings and unrelated work.

Load/apply installed `ris-proj-lib-common` and its dialogue/artifact/quality
resources before their actions. Load/apply `ris-proj-op-resolve-context` and its
owned configuration/path resources for prospective sources, workspace, selected
adapter and the execution settings this scenario consumes. Check the whole v2
config, status, provenance, diagnostics and actual paths. Shared workspace paths
need context's checked primary selection and association; do not select primary
from Git listing order or `.sdlc/`. Missing optional root `ris.yaml` supplies
package defaults **for the proposal**. An invalid/inaccessible explicitly selected
config is diagnosed, never replaced by defaults; agree its bounded repair before
dependent preparation. Do not merge omitted required fields from defaults.

Before the first initialization file write, establish whether the requested result
is local-only or includes intended optional Git publication. For a publishable
result require the caller to supply an already prepared, confirmed own branch/safe
copy and its work identity/association, repository/path/branch/base, checked state
and permissions. Validate that input and use that copy/config for all writers;
isolation/project rules may require a worktree. Init bootstrap and the publisher
do not create/switch a document branch or transfer dirty primary files. Missing
preparation limits the result to authorized local/unpublished setup, or blocks
the dependent publishable request; do not silently narrow it. Local-only init
still works without Git, a remote or a publication decision granting push rights.
Do not promise that a later offer can safely publish changes saved on primary.

For material interdependent setup gaps, load and actually apply installed
`ris-port-op-interview` here, with the bounded topic, decision dependencies, known
answers/statuses and intended initialization result. Keep its discussion and later
subject interviews in this single leading dialogue. A single clarification needs
no interview; sufficient inputs need no questionnaire. Pass confirmed answers to
every owner; revisit only a material conflict, not each owner's checklist. Missing
dependencies block dependent results, not permission to imitate their methods.

Before the corresponding branch, read resources relative to **this installed
skill's directory**, not the target or source repository:

| Condition | Resource |
| --- | --- |
| Git is absent or agreed Git/ignore adjustments are needed | [references/git.md](references/git.md) |
| Beads is selected and its workspace needs checking/preparation | [references/beads.md](references/beads.md) |
| A required RIS tool is missing or installation is proposed | [references/tools.md](references/tools.md) |
| Every initialization, including reuse/resume: check Standard/Advanced, pinned models and role bindings | [references/agents.md](references/agents.md) |
| Repeat/resume, partial or uncertain effects, or concurrent changes | [references/recovery.md](references/recovery.md) |

The agents check is part of the ordinary path; other branches remain conditional.
Installation of this package alone authorizes none of these project changes.

## Agree one settings/change set, then bootstrap

Present ONE complete justified set: target/config path, document and workspace
paths, selected task adapter/options, project `standard`/`advanced` definitions,
their explicitly pinned models and RIS role bindings, local directories/ignore/
Git/tracker changes, bounded `AGENTS.md` delta
and decision-record location. For each value explain existing project practice or
RIS default, preservation/reuse, proposed change and consequences. Do not import
the RIS repository's own Beads, TDD or publication policy into a consumer project.
Explain a proposed move/conversion to RIS conventions and get agreement before
changing structure; no forced relocation or silent Markdown-to-OKF conversion.

This scenario consumes semantic role **`project-initialization`** when delegating
standalone noninteractive operations below. When delegation is chosen, agree its
binding to an actually available, suitable executor; the identifier is not a universal mandatory role for every RIS
operation. Agree this binding separately; `advanced` is a suitable proposal for
the complex document work, not an automatic assignment. For the working-cycle
setup propose `standard` for `feature-selection`, `task-decomposition` and
`task-execution`; `advanced` for `feature-preparation`, `task-implementation` and
`task-review`. This is init's proposed setup, not new context-schema defaults or
a universal role requirement for unrelated direct operations. Preserve existing
bindings until their change is agreed. Read the agents resource to inspect project
definitions/effective settings, recommend models from the target's current
available catalog and resolve only missing/material choices in this dialogue.
For these two tiers, parent/global model inheritance is not a pinned project
model. Reuse suitable project settings without repetitive questions; no automatic
model upgrade, fallback or rights selection. Declined/deferred tier setup limits
the dependent working-cycle readiness, not independent useful results.

Obtain attributable agreement to the exact settings/change set and write scope;
the person may accept it whole or select material points for discussion. This
approval does NOT accept unseen product or rules content. Get action-specific
installation/system/external/Beads side-effect authority separately. Do not ask
again before every file already included in an accepted write scope. Without
write permission return the explicit unsaved proposal and dependent gaps.

The **leading scenario itself** owns agreed initial config/infrastructure writes;
do not require a not-yet-configured role to bootstrap itself or ask context to
write. Before each write inspect physical targets/ancestors and symlinks, record
baseline bytes/absence and relevant dependencies; reread them immediately before
changing, and stop affected writes on foreign/concurrent changes. Preserve
unrelated bytes/settings; read back actual content/effects afterward. These checks
are conflict detection, not filesystem CAS, atomicity or blanket idempotence.
Use each infrastructure resource/owner only within its actual approved branch.

Create absent `AGENTS.md` or supplement an existing one without replacing its
applicable instructions. Include pointers to the selected config and actual rules,
and a bounded natural-request routing addition tailored to available contracts:
appropriate ordinary requests should load the matching RIS owner even without a
slash command. For example, distinguish an unconfirmed bug message (registration),
an exact-ID investigation and an authorized fix with sufficient inputs; never
infer fix permission merely from mentioning a bug. A simple question is not a
task. Preserve each owner's inputs/permissions/stop; no automatic full cycle,
queue selection, fabricated task ID or mandatory init for unrelated requests.
Check actual skill/command availability before naming a route.
Include `ris-proj-flow-prepare-feature` for a request to prepare a selected feature
through requirements/design to published verified decomposition. Direct document
requests remain scoped specify/design operations; selection does not start
preparation, and preparation never starts implementation. “No automatic full
cycle” forbids unrequested work/stages, not finishing an authorized flow. A later
“continue” preserves its established scope; clarify a genuinely ambiguous endpoint
once rather than silently narrowing it.

Agree the project's ongoing publication policy separately from this init's local
or published result. Recommend that authorized full preparation include its normal
Git commit/integration/non-force push and separate tracker publication without
step-by-step approval. Bound Git authority to the assigned result and established
remote/ref, excluding unrelated local commits/foreign edits. For shared Dolt,
explain that push sends common history, not one ID; offer a one-time standing
policy for accumulated shared history at the established destination, explicitly
distinct from accepting/editing/closing foreign records. If declined or deferred,
retain explicit outgoing-scope approval before uncovered publication. Preserve
existing prohibitions until their change is accepted; never auto-adopt RIS's own
policy. Record the agreed scope in existing project rules/AGENTS and the settings
decision, with no new config fields or permission log. Reuse accepted policy on
later operations; its establishment does not authorize init to publish itself.
Distinguish research availability, report persistence and full fix readiness:
ordinary investigation saving needs one assigned investigator, authorized native
writes, fresh comparison, preserved original/foreign content and read-back, not a
mandatory CAS provider. This is organizational control, not concurrent-write
isolation. Missing authority/capability or observed conflict can block saving
without blocking research. Init/config/claim alone certifies neither a saved
report/criteria pair nor sufficient fix inputs, a historical execution snapshot,
required design acceptance or the execution/publication route.

Persist the accepted settings decision and material deferrals compactly in the
agreed project document, default `docs/ris-initialization.md`. Include exact scope/
version, actual actor/date/channel when known, rationale/provenance and specific
limited operations. Preserve prior applicable decisions; no mandatory separate
journal, task folder or initialization state registry. Subject decisions stay
with their authors' results. If the chosen record is inside an OKF bundle, use
`ris-proj-op-manage-okf-bundle` for the explicit root/operation/scope, without
converting ordinary Markdown or replacing content ownership.

After actual bootstrap save, freshly apply context v2 to the selected saved
config, not the earlier proposal. Verify full validity, actual values/provenance,
source/current-copy vs workspace/checked-primary bases, all agreed role bindings
and path access/write scope. Recheck both project tier definitions and effective
agent/model/permission discovery under the agents resource, including reused
definitions. Check created infrastructure through its owner, not config
presence. No tracker tasks, worktrees or per-ID directories are created merely
because workspace base directories are configured.

## Compose the document owners

After the bootstrap/context gate, apply each document owner directly or delegate
a bounded operation. Direct authorized work needs no `project-initialization`
role. When delegating, resolve its agreed binding through context, check host
availability/permissions and verify actual launch. Missing/unlaunchable agents
block that delegated route, not independent authorized direct work; choose the
direct route explicitly, never disguise a failed delegation as success or silently
substitute an executor/model. Required independent review remains separate below.

Pass selected owner/operation, goal, project/current/checked-primary and config
provenance as needed, create/bounded-update boundary, applicable rules, sources/
versions, confirmed answers/statuses, prior decisions, precise read/write scope
and requested output. The acting context loads/applies its owner's dependencies;
naming an owner is not executing it. Load child methods in the leader only when
applying them there, not merely to route work; do not delegate individual internal
reads as separate operations.

Keep discussion/interview/content acceptance here. Apply or delegate proposal-only
work, inspect the **complete** actual candidate with version and exact scope, discuss
returned material choices, and obtain a separate attributable content decision
using that author's acceptance contract. Then apply or delegate the same project
owner in bounded accepted-save/check mode, passing full exact accepted text or a
recipient-accessible exact file/version locator plus the separate decision and
permitted files/sections. Optional draft storage needs agreed scope, is not
acceptance and is not mandatory. Subagents return questions/choices here, never
interview the human or accept for them; inaccessible/changed candidates block
saving rather than authorize reconstruction from foreign chat. Material changed
content needs targeted renewed acceptance, not reapproval of unchanged results.

Apply the following dependency order, reusing sufficient existing accepted
material only after its owner checks version, decision, applicability and files;
do not force rewriting suitable documents:

1. **Product foundation:** `ris-proj-op-author-product-foundation` actually applies
   `ris-port-op-formulate-product-foundation` and the existing conditional interview.
   Check substantive purpose, users, tasks, capabilities, boundaries, material
   constraints and unknown/deferred impact, followed by separate content acceptance
   and the author's scoped project OKF save/read-back. The format owner is not the
   subject author. This is an initial sufficient foundation, not full product design.
2. **Architecture:** `ris-proj-op-author-architecture-rules` receives the checked
   product result, constraints, project evidence and answers. It owns its portable
   method/profiles, normative proposal, separate content decision and scoped save.
3. **Engineering:** `ris-proj-op-author-development-rules` receives the applicable
   accepted architecture and actual versions/practices; it independently owns its
   content decision/save/check. Recommendations do not mean installed tools or
   passing gates. No author is assigned another author's subject or future stage.

When stack/architecture is unresolved, offer focused work through the relevant
subject owners and their available applicable profiles/examples (Rails web,
DragonRuby/Odin games, or their common method plus researched facts for another
stack). Architecture owns structural choices; engineering owns versions/practices.
The scenario must not choose a stack/profile itself or force premature decisions
to fill files. Retain an explicitly deferred decision with affected operations
and return triggers; proceed with independent sufficient content. Unknown
architecture may limit design/implementation even when local setup is complete.

For each operation require actual executor/completion (and launch when delegated),
`ok|blocked|conflict|error`,
scope, full proposal/version or exact accessible saved-result/decision addresses,
sources, actual effects, content/format/link/read-back checks, preserved content,
limitations and needed decisions. Read the returned complete result and inspect
accessible saved effects; “done” or an OKF success alone is insufficient. Do not
repeat the owner's subject/format algorithm. Recheck an operation when inputs or
effects change or its evidence loses applicability.

## Reconcile, report readiness and stop

Delegate combined read-only reconciliation and independent review of the actual
complete candidate (settings, AGENTS delta, documents/decisions and infrastructure
receipts) against the agreed scope and project rules. Use existing
`ris-proj-op-review-task` for this bounded initialization change, with no invented
task ID; supply the baseline, complete candidate, actual Git/branch state (including
absence), decisions and check limits. The reviewer is a fresh
invocation independent of **all** content authors/fixers, including bootstrap
authors; the same configured agent identifier alone proves neither independence
nor a launch. Resolve the agreed `task-review` binding for this review (the tier
proposal uses `advanced`), rather than assuming the authoring executor is the
reviewer. Check role/availability as above; no review self-approval. Material
high/medium findings return to their owners and this dialogue for affected decisions,
repairs, checks and fresh independent re-review; record dispositions for optional
low findings. Missing required checks/review blocks the
dependent readiness claim; preserve the checked partial result.

The scenario checks the combined result against the actual agreed set: config
read-back/context, correct AGENTS pointers/routes, sufficient accepted/saved/checked
documents and accessible decisions, actual tool/tracker/executor availability,
project `standard`/`advanced` definitions with pinned and effective model IDs,
agreed role mappings, path access/ignores and unresolved conflicts. Do not call
files alone ready, a
declaration a working tool, or document checks product implementation compliance.

Report readiness per specific operation with its checked inputs, tool/backend
versions and remaining gates, not as a blanket lifecycle or production claim.
Distinguish installed package files from actual client discovery, static source
checks from executed program checks and version-bound observed agent behavior;
none implies general agent reliability or repeatability. With Beads, apply the
adapter's checked baseline/capabilities: claim, native guards and read/write/read
are not general content/graph CAS. Feature inputs use common's document convention
and actual acceptance, not a JSON registry. Preserve legacy payloads without
migration; their missing/old/malformed shape alone is no dependent blocker. Local notes
are not automatically remote inputs; recovery uses accessible evidence, not an
assumed mandatory transition ledger. State the direct-push/PR-only boundary for
publication. RIS setup does not supply release/deploy/rollback/production operations.

Return `ok|blocked|conflict|error`, selected project/copy/config provenance, agreed
scope/decision address, actual changed/reused files and versions, component and
independent-review evidence, available tools/executors, both tier model IDs and
definition paths, effective-discovery results and agreed role mappings,
accepted/saved/checked
facts, deferred decisions and their specific operation limits, remaining actions
and exact cause/recovery for incomplete effects. An expressly agreed setup scope
may finish with accepted deferrals, but never call dependent operations or the
whole working cycle fully ready while material obstacles remain. Separate local
readiness from publication; unperformed publication is **unpublished**, not failed
local setup. Use the recovery resource before replaying any uncertain effect.

Offer commit/push separately when Git and a suitable remote exist, but execute it
only from the confirmed prepared own copy established before writes. If it was
not supplied, report local/unpublished results and the exact preparation gap;
do not invoke the publisher or improvise a dirty-copy transfer/late branch switch.
Only with explicit authority and its actual independent-review/own-branch/whole-outgoing/
remote gates, apply directly or delegate existing `ris-proj-op-publish-task` for the
exact no-ID initialization change or applicable confirmed task subject; inspect its full
snapshot and remote evidence separately from local primary maintenance. Skipped or
failed local sync leaves confirmed Git successful and never blocks independent
tracker actions. An explicit local-update request retains that unfinished part,
not a reason to repeat initialization or push. No remote or declined push leaves the checked local
result intact. Beads init's separately approved commit side effect is not source
publication authority. Tracker/Dolt publication remains separate and is not
implied by Git. Never create a default remote or claim local saves published.

Stop before roadmap, feature specifications/tasks, product implementation or
build/test/format/CI setup. List missing product tooling only as later actions;
do not install it under RIS infrastructure permission. No global configuration
edits, automatic whole-rules refresh or lifecycle launch follows initialization.
