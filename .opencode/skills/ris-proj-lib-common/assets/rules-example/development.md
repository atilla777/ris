---
type: Example
---

# Illustrative engineering norms

These are candidate examples, **not accepted project policy**.

For new/touched work, record supported runtime/build targets and locked
dependency inputs sufficient for a clean build. Retain working project tools;
select upgrades for a purpose with version-matched compatibility evidence.
Use one formatting authority per file kind, excluding generated/vendor files.
Unsupported formatter/runtime combinations remain unselected pending evidence.
Review checks reproducible inputs and compatibility rationale, not a promise
of bit-identical artifacts. Exceptions need the project's actual authority,
reason, bounded scope and revisit condition.

Tests exercise changed behavior, rejected inputs and applicable integration
paths through the [architecture-owned contracts](architecture/principles.md).
Do not copy or redefine their ownership rule here. Record setup, stimulus,
expected result and checked revision. Compiler success is not a test suite;
host-language tests do not establish target-runtime, rendering or packaging
behavior. Select dependency/security checks for actual risks, recording offline
or database-freshness limits rather than promising absence of vulnerabilities.

Keep affected usage and rule references current. Review checks correctness,
meaningful tests, related architecture decisions and justified exceptions.
When the architectural game-reuse rule applies, review records consideration
without extracting a library. Completion requires applicable checks and review
on the identified revision, affected docs and disposition of unresolved risk,
while preserving the existing task/approval/publication process. Required and
conditional CI gates must be distinguishable; unavailable CI is a visible gap,
not a fabricated passing gate or permission to configure it during authoring.

Concrete versions, commands, test/format/security tools and exception authority
must come from project evidence and the applicable engineering profile. This
example deliberately selects none; it is not a complete project tool policy.
