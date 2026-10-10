---
name: ris-author-skills
description: >-
  Create or improve RIS package skills and project skills that actually
  integrate with RIS, using ris-author-skills-base and checking the combined
  result. Use for RIS-dependent skill source authoring; route standalone skill
  requests to the base instead. Not for installing skills or executing them.
---

# Author a RIS-integrated Agent Skill

Own the complete RIS skill source result, including correct integration and
verification. First classify the target by its **responsibility**, not merely
the presence of RIS in its project. For an autonomous skill (even inside a RIS
project), load `ris-author-skills-base` via the host skill loader or its actual
installed location and hand the request to its method **before** loading
`ris-common`, `ris-context`, or any RIS-only resource. Do not add RIS rules to
that target. If the base is unavailable, report the blocker; do not silently
substitute an incomplete method. Direct base invocation has the same scope.

For a RIS package skill or a project skill whose operation actually integrates
with RIS, ensure `ris-author-skills-base` and `ris-common` (including the
applicable conditional resources it owns) are available and applied, not just
named. Use the base's authoring method to examine worked-out requirements,
build source and check structure, selection and execution; **this** skill
chooses RIS dependencies, applies the integration rules below, checks the
combined result and owns its stop condition. Follow the person's language in
conversation, the project's/user's language for a project skill, and English
for RIS-distributed operational instructions and metadata. Use project rules
and actual permissions. If a dependency or required resource is unavailable,
report the independent progress and block the dependent claim.

## RIS scope and inputs

Use sufficiently worked-out requirements in a request or document, without
requiring a saved specification or a separate interview skill. Inspect local
facts, existing contracts, consumers and neighboring skills. If a substantive
behavior decision or essential subject-matter contract is absent, state the
gap for clarification without inventing it or starting a full interview.
Preserve accepted behavior in improvements and compare affected before/after
cases. Match the finished skill to accepted constraints and exclusions.

Determine whether **this authoring operation** needs RIS project settings,
for instance to locate a configured project document input or output. Only
then load and apply `ris-context` and its owned configuration resource via the
host loader or actual installed location; check its status, provenance,
relevant paths, diagnostics and permission scope before using them. A missing
optional `ris.yaml` uses package defaults; an explicitly chosen inaccessible
or invalid file is an error, never a fallback. A target skill's future context
needs do not imply the author needs context today. Loading a dependency does
not authorize writing or install the resulting skill.

## Integrate the target

For a package skill use `ris-*` naming and identify the applicable supplied
RIS result/operation contract, owner, inputs, boundary, checks and stop
condition. For a project-owned skill retain its conventions and apply only
RIS rules relevant to its real RIS responsibilities; do not force package
naming or unrelated infrastructure. Do not claim future or illustrative
components are installed. Determine dependencies **from the target's actual
operation**, not a preselected list: shared RIS scope, dialogue, artifact and
quality rules belong to `ris-common`; selected project configuration and
paths belong to `ris-context` only when needed; a portable method can be a
base skill; restricted tracker operations require an actually available
adapter. Declare how and when direct invocations load applicable dependencies
and owned resources and verify availability and application. Do not embed
their methods or claim that merely listing them performs their work.

For each action, distinguish necessary work toward the promised result from
another owner's operation. A composed skill owns coordination, sufficiency
and verification of the combined result. When specifying a RIS package skill,
record why an autonomous portable base plus RIS wrapper is warranted, or why
one skill suffices. A portable base must work without RIS rules, config and
project directories; a wrapper has an actual RIS result beyond loading it.
Keep optional branches conditional without losing necessary instructions.
For critical risks, ensure the resulting skill includes concrete subject-
specific shortcuts and observable failure signals with corrective reactions.

## Verify and stop

Apply the base's structural, natural-request routing and representative
execution checks, then additionally inspect the **combined RIS result**:
responsibility boundaries, dependency availability and cycles, correct
activation on direct invocation, project-path provenance where applicable,
permissions, negative requirements, links and installed-relative resources.
Check typical and conditional instruction loading, adjacent operations and
improvement before/after behavior. Inspect actual files and effects, not only
an agent's success statement. Label unrun checks and untested clients honestly.

Deliver only the requested ready-to-use source folder or explicitly unsaved
draft. Do not install it into the user's working project, publish it, change
tracker state or perform its future subject-matter operation without separate
authorization. Report location, changes, structural/routing/behavioral
evidence, limitations and blockers; do not call a partial result complete.
