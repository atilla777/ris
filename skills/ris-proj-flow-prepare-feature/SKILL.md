---
name: ris-proj-flow-prepare-feature
description: >-
  Guide one RIS project feature from a roadmap choice through separately accepted,
  reviewed and published requirements/design to a remotely verified feature ID.
  Use for interactive feature preparation; not for only selecting, interviewing,
  drafting, decomposing an accepted feature, technical planning or implementation.
---

# Prepare and publish one feature

Own the sequence, one human dialogue and combined result. Component skills own
their complete subject results and checks; the adapter owns tracker identity,
concurrency and publication. This project-specific scenario needs no portable
base. Stop at a published feature ID and inputs, **without decomposition**.
Decomposition is a separate invocation/session starting from that ID.

## Scope, permissions and execution

Establish project/current copy, explicit epic or roadmap scope, accepted goal,
known answers, linked prior work, applicable rules and permitted document,
decision, Git and tracker effects. Workflow authorization does not accept unseen
content. Apply installed `ris-proj-lib-common` and its conditional dialogue/artifact/
quality resources, and `ris-proj-op-resolve-context` with its configuration resource for relevant
sources, adapter and execution settings. Shared workspace paths require an
explicit primary root in a worktree. Do not derive a task directory before ID
confirmation, invent filenames from config, or require a draft store.

The scenario consumes `execution.roles.feature-selection` for selection and
`execution.roles.feature-preparation` for the other noninteractive component
operations, including independent review and publication. Verify that each
configured agent is an available subagent and actually launches. The reviewer
must be a fresh invocation independent of content authors. Direct component
calls need no roles. Missing executor blocks its dependent operation; do not
silently run it in the leading context, choose a fallback or require the
`task-decomposition` role for preparation.

Before writable preparation, delegate bounded read-only preflight: the adapter
checks actual operations, create/read feature-record support, local-write
isolation, configured remote, outgoing scope and publication guarantees; a Git
executor checks the authorized destination/ref, outgoing commits, hooks,
preservation and independent remote verification. Establish actual publication
permissions, including full outgoing tracker history. No remote or guarantee
means a blocker for the dependent effect. Direct document-only components may
still return their authorized local result. Explain protected update windows
before dependent writes; permission, claim and sandbox are not technical locks.

For **every standalone noninteractive operation**, launch a bounded subagent.
Do not load all child methods merely to route work, split each internal read
into an agent, or copy their algorithms here. Pass selected skill/operation,
goal, project/config provenance, permitted scope, known decisions and input/
output addresses. The executor loads/applies that component and dependencies,
checks its result and stores any full report at an agreed address. Require:

```text
status; operation/scope; verified result address; revision or confirmed ID;
evidence address; actual effects; limitations; decision needed
```

Check actual launch, completion status and accessible result/evidence address,
not an unsupported “done”. The consumer reads the full artifact and checks its
applicability. Do not repeat the owner's field, digest, SQL or publication
algorithm. Repeat a component check when its inputs or effects changed, or its
evidence no longer applies; independent review checks its subject independently.
Subagents never ask the human or accept content on their behalf: return choices
here. Human interview, discussion and acceptance stay in this dialogue.

## Choose and accept requirements

Delegate read-only `ris-proj-op-select-feature`; confirm the person's chosen small
outcome and epic. If an unclear epic boundary blocks selection, apply
`ris-proj-op-refine-epic` only for that ambiguity: its interactive decisions stay here,
its standalone noninteractive investigation/write operations use the executor.
Do not refine just because the epic is large or create speculative tasks.

For unknown requirements apply `ris-proj-op-interview-feature` in this dialogue, using
known answers. Clarify desired result, actors, behavior, constraints and relevant
alternatives before recommending architecture. Delegate `ris-port-op-formulate-feature-spec`
with the resulting decisions and permitted candidate output address. Read the
candidate for human discussion; unresolved choices return here, not to an
executor's guessed answers. Show the concrete requirements and obtain their
**separate** acceptance under project rules. Keep the accepted candidate identity
and actual authority/decision recoverable; generic workflow approval is not
acceptance. Delegate `ris-proj-op-specify-feature` in explicitly requested document-only,
bounded save mode with that exact candidate, acceptance and write scope. It owns
saved content/decision matching. No feature task is created yet.

## Discuss and separately accept design

Delegate `ris-port-op-design-feature` for sufficient design from the accepted
requirements, actual code/architecture and alternatives. Read its candidate
and discuss material technical decisions here; use a focused technical interview
only for unresolved interdependent choices. Delegate revised analysis when
needed. A behavior change returns to requirements discussion and targeted
acceptance; unchanged requirements are not reaccepted for a design-only change.
Obtain a **separate** decision approving the actual design. Delegate
`ris-proj-op-design-feature` in document-only bounded save mode, without inventing an ID.
The owner checks accepted requirements applicability, sufficient design, versions
and preservation. A local saved result is not publication.

## Review, publish Git, then create the feature

Delegate independent review of the specific accepted requirements/design and
their decision evidence against rules, AC and actual architecture. Provide exact
candidate revisions and addresses, not just an earlier verdict. Return material
findings to their content owner; discuss/accept only changed content here,
delegate repairs and rerun affected checks and fresh review. High/medium findings
must be resolved before publication. Do not treat review as human acceptance.

Delegate authorized preparation-artifact Git publication (not implementation
delivery): check final snapshot/index and every outgoing commit, include both
accepted results and their separate decisions, preserve unrelated work, commit/
push only the confirmed destination under project rules. Hooks changing accepted
content invalidate affected acceptance/checks. Verify the actual fetched remote
tree and immutable addresses in an independent copy. The document owners supply
content/decision matching evidence; no mandatory Markdown byte-scope hashes.
Decisions can name `containing-commit`, resolved by their commit-pinned address;
tracker refs use full published commits. Git publication must be confirmed
before creating the feature record.

Then delegate selected-adapter create/reuse with confirmed epic, permanent slug,
stable key, approved task content and **published** requirements/design/decision
references. The adapter owns all-status key/slug/spec collision detection, exact
reuse or conflict, create/read-back and concurrency diagnostics. Ordinary create
is best-effort; strict uniqueness only with explicit need and real guarantee.
Beads stores task identity, state/links and current published refs, not copied
decision history or prose duplicating mutable status. Updates of existing
records still require protection against lost concurrent changes. Historical
unsupported records are preserved and block dependent writes; never migrate
on retry. Do not create children or invoke decomposition.

Delegate separate tracker publication for the verified ID and refs. The adapter
checks authorized **full outgoing history**, isolation, final gate and independent
read-back of the selected remote. It returns snapshot/ID and evidence, not raw
database internals for this scenario to reinterpret. Git and tracker results
are independently confirmed; one success cannot clear the other gate.

## Partial effects, retry and handoff

After an ambiguous/failed effect stop dependent writes. Ask the corresponding
owner to reconcile its actual local/remote state before retry. Retain saved
addresses, published commits, keys and confirmed IDs. If Git succeeded and
tracker creation/publication failed, recover that tracker operation using the
same published inputs, without repeating unchanged acceptance, recreating known
IDs or undoing another owner's work. Changed content/identity returns conflict
and focused resolution. A failed read-back after push requires remote snapshot
verification, not another blind push. A missing executor preserves independent
results and blocks that step explicitly.

Return `ok|blocked|conflict|error` for the whole scenario, project/config scope,
confirmed epic/feature ID and slug, published requirements/design and separate
decision addresses, Git revision/ref and tracker snapshot/read-back evidence,
component result addresses, actual effects, limitations and decisions needed.
`ok` requires both reviewed, independently accepted published document results
and a remotely verified feature record. For partial completion give each channel's
actual state and exact recovery. A new session can consume the ID and published
addresses without local notes or this chat. Stop without decomposition, claim,
technical planning, implementation or closure.
