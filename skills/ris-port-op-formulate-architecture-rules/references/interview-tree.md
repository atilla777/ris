# Architecture subject decision tree

Use when material answers are missing. This resource supplies subject branches
to `ris-port-op-interview`, which owns interview procedure and status-aware handoff.
It is not a fixed questionnaire or a full feature-design exercise. Full coverage
means all material branches **inside this authoring scope**, not all product
capabilities. A narrower interview mode requires the caller's explicit request
and sufficiency criterion; a bounded update already defines a bounded topic.

## Prerequisites and branches

```text
Operation + subject + scope
├─ create → purpose, nearest goal, constraints, new/existing baseline
└─ update → existing norm/version + requested delta + retained exceptions
        ↓
Known decisions, source status, actual/proposed stack and related norms
        ↓
Necessary responsibilities and public/internal boundary
├─ state/data owner → read/write paths → invariants
│       ├─ persistence → consistency scope → partial failure/retry
│       └─ transient resources → init/reset/shutdown → lifetime errors
├─ cross-boundary consumer → public contract + owner → dependency direction
│       └─ external/async interaction → compatibility + errors + authority
└─ nearest material risks → observable boundary checks

Stack + nearest scope → applicable profile branches (below)
Game + candidate responsibilities → reuse consideration
        └─ evidence of benefit → internal module vs library → applicability,
           contract, state/lifecycle and dependency obligations

Relevant existing rules + candidate delta → conflict/transition policy
Material norm changes/exceptions → decision authority and return conditions
```

The ownership and contract branches may be interdependent: establish the
responsibility before guessing its state or interface. Verification follows
the actual invariant, not an arbitrary test framework choice. Authority and
transition policy can proceed independently once their affected scope is known.

## Subject prompts and gates

| Node | Question only if unknown and material | Dependent decisions |
|---|---|---|
| Boundary | Which nearest work must these rules govern? For update, which existing norm changes? | Eligible branches and completeness of the result |
| Baseline/stack | What is selected, observed, merely discussed, unavailable or contradictory? | Applicable profile; no synthetic implemented components |
| Responsibility | Who owns this behavior and what may consumers rely on? | Data mutation path and public/internal distinction |
| State | Who changes each significant state group, and under which invariants? | Transaction/step, sharing and lifecycle policy |
| Interaction | Which known consumers cross this boundary, and what result/failure do they need? | Allowed dependencies, compatibility and contract owner |
| Failures | What must remain true after rollback, timeout, repeated operation, reset or failed initialization? | Necessary atomicity/lifetime rules; not all failure modes everywhere |
| Verifiability | How can a significant invariant be observed without internal coupling? | Architectural test seams, not tool installation |
| Reuse (games) | Is there a real independent consumer or repetition; what benefit justifies separation now? | Retain subsystem, internal module or library; never automatic extraction |
| Governance | Who can accept a substantial norm/contract change or scoped exception? | Proposed approval policy; do not assign a person from a job title alone |
| Existing code | Which new/touched-code obligations and temporary exceptions are needed? | Transition proposal, not exhaustive code audit or migration tasks |

## Profile branch activation

- **Rails web:** known domain responsibilities → controllers/models/jobs in use
  → placement of business invariants and authorized data access. Persistence and
  cross-record invariants activate transaction questions; external APIs/jobs
  activate commit visibility, failure/retry and authorization-context questions.
  Do not interview for a queue or Service Layer when neither is needed.
- **DragonRuby game:** loop owner → input/step/presentation responsibilities →
  state writer and initialization/reset. Saves activate durable format/restore
  questions; replay or reproducibility needs activate time/RNG policy. Reuse
  activates runtime/loop dependency questions, not a forced pure Ruby library.
- **Odin game:** necessary package responsibilities → public/private contract →
  memory/resource owner and allocator/lifetime → cleanup/error path. Rendering
  or platform calls activate handle/FFI boundaries; actual concurrency needs
  activate thread access and synchronization, not an automatic worker model.

For a deferred choice record its reason/status, the dependent rules that cannot
yet be finalized, a return trigger if known and independently usable norms.
Do not answer descendant questions by assuming ECS, a storage engine, a scene
model or threading. A supplied confirmed answer closes its node; profile
recommendations are not a reason to reopen it without material conflict.
