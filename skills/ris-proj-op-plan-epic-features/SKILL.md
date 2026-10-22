---
name: ris-proj-op-plan-epic-features
description: >-
  Plan or revise one existing RIS epic's preliminary feature graph from product
  sources and actual all-state work, agree concrete changes and verify bounded
  tracker writes plus separate publication. Use for empty or incomplete epic
  planning/replanning; not next-work selection, spec/design, task splitting or execution.
---

# Plan an epic's preliminary feature graph

Own project discovery, reconciliation, concrete human graph agreement and the
checked persisted whole. Apply installed `ris-port-op-plan-epic-features` to actual
inputs; it owns the graph method, not tracker discovery or writes. This wrapper
adds real project integration; merely loading the base is not its application.
Direct invocation works in the current agent with no role or subagent requirement.
Optional isolated proposal analysis may use caller-selected `task-decomposition`;
the caller checks availability/launch, forwards shared sources and neighbor scope,
and validates overlaps before agreement and serial bounded writes. No new role,
queue or concurrent graph writers. A child proposal cannot approve its own changes.

## Discover and propose

Full checked planning including separate tracker publication is default. Explicit
proposal-only makes zero writes; explicit local-only is a bounded contribution
whose caller owns publication. Neither nesting nor a draft implies local-only.
Establish project, exact existing epic ID, goal, requested scope and permissions.
Roadmap callers may request a proposal contribution for an anticipated epic;
that is unsaved with local labels until the caller creates/verifies its exact ID.
Do not create epics here or turn a direct missing epic into automatic creation.

Apply installed `ris-proj-lib-common` and its conditional resources before governed
actions; apply `ris-proj-op-resolve-context` and its configuration/path resources
for relevant `sources.product`, `sources.rules`, `sources.specs` and tasks adapter.
Check status, provenance and permissions. Read applicable product sources in their
own structure, accepted goals/constraints and linked current decisions. Use common's
published-input method for acceptance-dependent claims, not a whole-history audit.
No product rewrite, mandatory source IDs, registry or parallel Markdown backlog.

Load/apply the selected installed tasks adapter. Require compatible `tasks` v1
epic read/list, all-status items read/list, complete epic children and directed
dependency reads. Verify actual endpoint kind from scope/content/source association,
not native task type, title or parent membership alone. Read the epic's outcome,
boundary, all relevant open/started/closed features, their edges/needed content,
observed results and neighboring roadmap boundaries. Complete dedup scope extends
beyond one parent's children when overlap is possible. Brief omitted content is
unknown. Incomplete/failed reads cannot prove absence. Preserve foreign ownership,
accepted documents, status and completed results. Do not claim or transfer work.

Pass these actual inputs and source versions/baselines to the portable base;
apply and inspect its coverage/dedup/cycle/stage/parallelism/neighbor checks. Return
material ambiguity for one human decision rather than inventing product outcomes.
Do not call this operation merely because a nonempty epic's work is blocked:
diagnose existing prerequisites first. Proven coverage gaps/product changes can
justify a bounded replan; blocked work alone cannot justify new features.

## Agree and apply controlled changes

Before any graph write show the concrete whole proposal: retained exact IDs,
draft labels, per-feature title/capability/result/membership/product rationale,
classified prerequisite edges and explicit reasons, removals, coverage and gaps,
parallel sets and neighbor impacts. Obtain attributable human agreement to that
specific graph/delta; general planning or write permission is not graph agreement.
Reuse an unchanged already agreed scope; material changes require agreement again.
Cross-epic endpoints require explicitly approved scope including both epics;
otherwise return the boundary decision without moving/creating neighbor scope.
Roadmap composition reconciles overlaps across all selected epic proposals before
this agreement and before any graph writes; return proposals to its lead for that.

Before mutation confirm adapter capabilities for exactly needed actions:
`tasks.items.create`, optional bounded feature-content `tasks.items.update`,
and `tasks.feature-dependencies.add|remove` for approved feature endpoints.
`tasks.dependencies.add` remains confined to tasks within one feature; do not
widen it. Missing capabilities block dependent writes, not independent proposals.
Preflight separate publication through its owner before remote-gated writes.

Fresh-read expected fields, IDs/kind/membership/ownership and affected edges before
each bounded action. Reconcile all-state stable retry identities and semantic
matches before create; ambiguous match is not absence. Preliminary registration
needs approved ordinary content and stable retry identity, no spec/design/AC/children.
After each create independently verify exact ID, type, content, membership, status
and preserved fields. Only then resolve that local label to its exact ID. Never
store draft labels as prerequisite IDs or guess IDs from titles/parent punctuation.
Create required endpoints before edges, using the verified mapping.
When a readable prerequisite still targets a draft label, create only the agreed
ordinary core content first; after all needed IDs are verified, finalize that
agreed prerequisite prose with bounded `items.update` and read-back before declaring
the graph complete. Do not persist placeholders as IDs or treat partial records
as requirements-ready; a failed finalization preserves exact IDs and stops writes.

Store implementation dependencies as native directed `blocks` with explicit
result/reason in readable feature content; requirements-only prerequisites as
readable **exact ID + required accepted decision/contract reference and scope**
in dependent feature content; informational links as ordinary nonblocking links.
No stage/ready metadata, JSON card or native requirements blocker. Existing unknown
edge scope stays conservative until clarified with evidence and agreement; do not
remove/reclassify it automatically. Requirement readiness waits for the specified
accepted contract, not raw closure of the other feature.

Update only approved fields through adapter targeted fresh expected-content checks,
preserving unrelated prose and accepted specifications. Never replace create with
update, close/delete stale candidates, change assignees/status, reparent or silently
reshape started/accepted/foreign work. Changes to such commitments require their
explicitly agreed scope/coordination, not planner authority alone. Add/remove only
agreed exact typed edges with both endpoints rechecked, direction/cycle checks and
independent read-back. Informational relationships never become blocks.

No graph/document CAS or strict concurrent uniqueness is promised. On any failed,
conflicting or ambiguous write stop further writes (including independent later
edges), reread affected records and preserve verified IDs/partial effects. No
rollback or blind recreate. Resolve unknown effects before retrying only the missing
actions; an already-created parent/feature remains the same identity.

## Verify, publish and stop

Re-enumerate the bounded all-state set and reread affected content/membership/typed
edges. Compare the persisted whole with agreed coverage, identities, classification,
directions, parallel sets, preserved work and neighbor boundaries. In full mode
invoke the selected adapter's separate tracker-publication owner, checking actual
outgoing-history authority/destination and its fresh remote revision/reachability
receipt. No synthetic Git commit, copied Dolt algorithm or push per feature.
Roadmap/local-only contributions return verified effects and exact publication
debt to the caller; proposal-only never implicitly advances to writes. No-change
checks actual availability/outstanding debt, not an empty push.

Return `ok|blocked|conflict|error`, selected project/config/epic/scope, proposal and
agreement, verified label→ID mapping, actual changes/edge directions and source
rationale, coverage/gaps/parallel sets, evidence/limits and separate local versus
published tracker facts. Preserve partial effects and exact remainder; do not call
a local-only child result full success. Stop without spec/design/interview,
implementation-task decomposition, claim, implementation or automatic next operation.
