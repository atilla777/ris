---
type: Example
---

# Illustrative architecture norms

These are candidate examples, **not accepted project policy**.

## Responsibility, state and contracts

For new or changed domain/presentation interactions, the domain part owns
state transitions and publishes a read-only view. Presentation uses that
interface, not internal mutable fields. Each public operation defines inputs,
results, rejected inputs and material partial-failure behavior. This keeps
presentation order from changing domain behavior. A representative check uses
the same initial state and input with and without presentation and compares
the domain result. The intended dependency is presentation → public domain
contract, not domain → presentation internals; an incompatible proposal needs
the project's authorized architecture decision before changing that contract.

## Evolution and exceptions

Choose concrete boundaries only when necessary for the nearest work. One
process may contain logical modules; microservices, repositories, ECS and
Service Layer are not required. Material changes of ownership/dependencies or
exceptions require an explicit decision identifying the affected norm, reason,
scope and return condition for temporary exceptions. The real authority must
be established for the target project; this example does not appoint one.
Review checks that this decision and a meaningful boundary check are present.

## Conditional game rule

For game design and review, consider reuse and record a material decision to
extract or retain a candidate: actual consumers, stable responsibility, useful
interface, independent checks and maintenance cost. Extraction requires a
benefit, not hypothetical universality. A subsystem, reusable internal module
and independent library differ; runtime dependencies, state and resource
lifetimes remain explicit. No extraction is performed by rules authoring.

Specific testing/tool practices belong to [engineering](../development.md),
which supports these contracts rather than independently redefining them.
