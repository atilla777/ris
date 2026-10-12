# Shared normative foundation

This is authoring material, not binding rules of the target project. Apply
within the selected subject; profile options do not duplicate this foundation.
Use the person's decisions and observed facts to instantiate norms; label
proposed owners, policies and technologies as proposals until accepted.

## Minimum substantive rules

| Concern | Content to formulate | Observable verification expectation |
|---|---|---|
| Responsibility | Each necessary part owns a coherent responsibility; identify its public interface and internal details. A module can be a namespace, package or conventions inside one process. | A representative caller can use the public contract without depending on internal layout; review identifies the responsible part. |
| Mutable state | Assign a logical owner to each significant state/data group and an allowed mutation path; distinguish storage location from authority to mutate. Define read access and who preserves invariants. | Trace a mutation and all relevant writers; check the invariant through the owned interface, not incidental fields. |
| Contracts | Cross-boundary calls use agreed inputs/results, errors and applicable lifetimes/compatibility; designate contract owner. Internal fields are not an accidental shared API. | A consumer/producer scenario exercises success and an important rejected/failed case. |
| Dependencies | State permitted direction, shared contract ownership and how an incompatible contract proposal is resolved. Physical colocating or framework capabilities do not erase logical boundaries. | Review relevant calls/imports and a conflicting proposed contract; no unexplained cycle or bypass. |
| Consistency | For material state transitions define atomic scope, partial failure/retry semantics and resource lifecycle. Do not promise atomicity across an unsupported boundary. | A rollback, interrupted operation, repeated request or reset/cleanup scenario observes a meaningful invariant. |
| Verifiability | Significant boundaries and invariants must have proportionate observable checks; pure logic can be inspected/tested independently of adapters when feasible. | Describe setup, stimulus and expected result. A list of testing tools is insufficient. |
| Evolution | Substantial boundary/state-owner/public-contract changes and exceptions require the authorized owner's explicit decision. Local reversible choices need no mandatory ADR. | The proposal identifies authority and affected rule, reason, permitted scope and, for temporary exceptions, return/expiry condition when known. |

The verification column describes checks that later design/review may perform.
Authoring checks the **document's** sufficiency and consistency; it does not
execute those checks on the implementation. Engineering rules own specific
tools/CI gates; refer to their existing norms without copying them.

## Evolution and existing code

Take decisions when needed for the nearest goal and supported by evidence.
Modularity is not a mandate for microservices, layers, engines, repositories,
ECS, a message bus or a full future component inventory. Do not ban framework
features wholesale: specify the boundary and reason a use would violate it,
and permit justified scoped exceptions through the proposed/known authority.

Distinguish stable principles from concrete confirmed decisions and optional
techniques. Keep unselected alternatives in the profile, not a long normative
menu. An open material question has status, dependent scope and a return trigger
if known. If it blocks the nearest work, say so; do not hide it as future tuning.
Rules can govern new work before corresponding components exist. Existing code
is a factual baseline, not evidence of compliance or permission to redefine
accepted norms. A proposed transition policy can govern new/touched code and
explicit temporary exceptions without promising to discover all violations.

## Game reuse: consideration is mandatory, extraction conditional

Include the norm that design and review consider reuse, recording the reason
for extracting **or keeping** a candidate when material. Evaluate:

- concrete independent consumers or repeated use, not hypothetical universality;
- stable responsibility separated from game-specific scenarios/content;
- independently observable logic and a useful explicit interface;
- cost of separation/maintenance versus benefit, realistic runtime dependencies;
- owner of state, initialization/reset/shutdown, and resources crossing calls.

A subsystem remains game-owned. An internal reusable module can serve several
consumers within the project. A library has an independently usable contract
and an explicit applicability boundary; it may be engine-specific. Separate
repositories and a universal game core are optional, never proof of quality.
Do not perform the extraction or produce its feature design here. Profile
resources specialize this rule for runtime and memory constraints.

## Sufficient rule example

**Proposal:** Only the simulation owner mutates world state during a simulation
step; presentation consumes its published view and cannot modify it. This
applies to newly designed simulation/presentation interactions, preventing
render-order-dependent gameplay. A check feeds the same initial state and input
to the step with/without presentation and compares the gameplay result. A
boundary exception requires the project's architecture authority to accept its
scope and reason. If that authority is unknown, mark it as a decision to assign,
not an invented person. This example does not choose a state representation,
ECS or renderer for the project.
