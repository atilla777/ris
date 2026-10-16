---
name: ris-proj-op-register-bug
description: >-
  Register an unconfirmed bug message in a selected RIS project's tracker,
  checking all-status duplicates and safely supplementing a confirmed original;
  return a verified ID and stop. Use for recording a bug before investigation,
  not for diagnosing, fixing, claiming or closing it, or specifying a feature.
---

# Register a bug message

Own the saved message or supplemented original and its independently verified
ID. Registration is a project tracker result; no separate portable method is
required. A report is input, not proof of a defect or authority to fix it.
Do not investigate, reproduce, design, implement, claim, close or reopen work.

## Prepare the bounded operation

On direct invocation ensure current `ris-proj-lib-common` is available through
the host skill loader or its actual installed location and apply its rules.
Read its artifacts resource before preparing the saved content/handoff, quality
before selecting checks/assessing the result, and dialogue before questions.
Ensure `ris-proj-op-resolve-context` and its owned configuration resource are
available; apply them to the selected project for applicable rules and
`adapters.tasks` selection/options, unless an applicable current checked result
is already supplied. Shared workspace paths and execution roles are not needed
for ordinary registration. Do not require product/spec/design documents merely
to preserve a message. Read applicable project rules; configuration grants no
write authority. Missing dependencies block their dependent operation.

Obtain the chosen project, meaningful message and available context, bounded
write permission, and any known original ID or prior registration result/key.
Keep the user's meaning and distinguish reported observations from assumptions;
preserve available version, environment, expected/actual behavior, logs and
source addresses without filling unknowns with invented facts. Do not impose
an intake questionnaire, diagnosis, reproduction or fix-readiness gate. Ask only
about a gap preventing correct project selection, meaningful storage or authority.
Permission to record does not grant investigation, fix or Git publication rights.

Load the selected adapter through its actual available skill location and check
its advertised ordinary native bug read/list/create/reconcile/update capabilities,
complete all-status selection and actual guarantees before dependent writes.
For Beads use `ris-proj-adapter-beads-tasks` and its ordinary/concurrency resources
under their activation conditions. Configuration or a CLI flag alone is not
capability support. Do not fall back to feature-task operations or direct storage
edits. Pass the checked project, exact operation, expected type, approved content,
allowed fields and identity to the adapter; it owns bounded tool mechanics and
concurrency/read-back, this operation owns substantive duplicate decisions and
the combined saved result. Use sandbox writes to avoid implicit tracker push.

## Reconcile before recording

Establish a stable project-scoped creation identity **before** a possible write,
reusing the supplied prior key on continuation. If none exists, choose one for
this registration, communicate it in the recoverable result and persist it in
the adapter's supported stable reference field. It identifies this attempt's
intended message/context, not every report with a similar title. Do not change
the key on error or use the title alone as identity. Retain known IDs and keys
even on failure; an existing ID means exact read/reconcile, not implicit create.

Through the adapter inspect all-status, unlimited native bugs across the relevant
project, including closed records; include complete legacy task selection when
relevant originals may be ordinary tasks. Read candidate originals by exact ID
and expected type, including message/context and useful supplements. First
reconcile any prior creation key/effect; reuse only the exact matching result.
Multiple key matches, changed identity or unknown effects stop as conflict with
all known IDs. Failed or incomplete search cannot justify creation.

Judge duplicates by the actual manifestation and available context, not title
similarity alone. This is registration-level comparison of supplied reports,
not a requirement to investigate or reproduce a defect:

- **No credible original:** create an unconfirmed native `bug` with the approved
  message/context and stable key, without artificial epic/children/feature record.
- **Definite duplicate:** return the exact original ID; append useful new message
  details/context through supported ordinary update, preserving the original
  message, foreign sections and all unrelated fields. Use a stable supplement
  identity tied to this registration and original ID; reconcile its exact content
  before append/retry. Already preserved information needs no additional write.
- **Uncertain similarity:** create a new unconfirmed bug and record the possible
  related ID and uncertainty in readable context. Do not assert duplicate or add
  a blocking edge merely for similarity.
- **Closed similar original:** distinguish an actual duplicate from a new
  manifestation/regression using available context. Uncertainty follows the new
  bug branch with a possible relation. A definite duplicate may supplement the
  closed original; keep its status. Never automatically reopen or close anything.
- **Legacy original:** preserve its native type; only an explicitly supported,
  authorized ordinary task supplement may update a task original. Return that
  original ID with its actual type, never call it a newly created native bug.
  Other types or missing update support block that write with a precise diagnostic.

Before each write confirm permission for that specific target and supplement or
creation. On ambiguous create/append response ask the adapter to reconcile actual
effects by stable identity and complete reads before any bounded retry. Do not
start a replacement create because an original append failed. Preserve every
successful effect and stop further writes on conflict or an unreconciled failure.
Best-effort create/append is not concurrent exactly-once or strict uniqueness;
if a required stronger guarantee is unsupported, stop its dependent write.

## Verify, return the ID and stop

Inspect the adapter's independent exact read-back, not merely its success or
returned ID: correct ID/native type, intended message/context, creation key or
supplement identity/content, original/foreign content preservation and relevant
unchanged fields/status. Verify complete post-create identity reconciliation and
post-append effect inspection. Unexpected type/content, collisions or changed
identity are conflict with persisted effects, not success or blind retry.

Return `status: ok|blocked|conflict|error`, project/config/current-copy provenance,
verified ID and tracker address (or selected workspace plus exact ID), actual
type, creation/supplement identity, and `created|supplemented|unchanged` when
verified. Include duplicate/possible-relation basis, what message/context was
saved, read-back evidence, actual partial effects, limitations and exact remainder.
Use blocked for missing permission/input/capability, conflict for contradictory
state or unreconciled identity, error for technical failure; unknown persistence
stays explicitly unknown. Distinguish local persistence from separately requested
and verified tracker publication; registration requires no Git publication of a
future fix and performs no implicit Dolt publication. Any separately authorized
tracker publication belongs to the selected adapter, with its own gates.

`ok` means the bounded registration was saved and checked; it does not mean
confirmed defect, sufficient investigation, accepted fix criteria or readiness
to execute. Stop at the verified ID. Further investigation or fixing is a
separately requested result; do not select/name or start its next skill.
