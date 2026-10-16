---
name: ris-proj-op-author-skill
description: >-
  Create or improve RIS package skills and project skills that actually
  integrate with RIS, using ris-port-op-author-skill and checking the combined
  result. Use for RIS-dependent skill source authoring; route standalone skill
  requests to the base instead. Not for installing skills or executing them.
---

# Author a RIS-integrated Agent Skill

Own the complete RIS skill source result, including correct integration and
verification. First classify the target by its **responsibility**, not merely
the presence of RIS in its project. For an autonomous skill (even inside a RIS
project), load `ris-port-op-author-skill` via the host skill loader or its actual
installed location and hand the request to its method **before** loading
`ris-proj-lib-common`, `ris-proj-op-resolve-context`, or any RIS-only resource. Do not add RIS rules to
that target. If the base is unavailable, report the blocker; do not silently
substitute an incomplete method. Direct base invocation has the same scope.

For a RIS package skill or a project skill whose operation actually integrates
with RIS, ensure `ris-port-op-author-skill` and `ris-proj-lib-common` (including the
applicable conditional resources it owns) are available and applied, not just
named. Use the base's authoring method to examine worked-out requirements,
build source and check structure and selection/execution instructions; **this** skill
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
then load and apply `ris-proj-op-resolve-context` and its owned configuration resource via the
host loader or actual installed location; check its status, provenance,
relevant paths, diagnostics and permission scope before using them. A missing
optional `ris.yaml` uses package defaults; an explicitly chosen inaccessible
or invalid file is an error, never a fallback. A target skill's future context
needs do not imply the author needs context today. Loading a dependency does
not authorize writing or install the resulting skill.

## Integrate the target

For a package skill use `ris-<port|proj>-<op|flow|lib|adapter>-<verb-object|purpose>`
naming: lowercase ASCII words with single hyphens, at most 64 characters;
directory and frontmatter `name` must match. `port` takes direct inputs without
requiring RIS configuration, structure or tracker; `proj` owns necessary RIS
integration. `op` owns one useful result, `flow` transitions between independent
operations, `lib` shared instructions, and `adapter` bounded tool operations.
For every op/flow provide one thin OpenCode command with exactly the same name;
lib/adapter have none. `skills/` and `commands/opencode/` own source; installation
is synchronized output. Do not add aliases, a dispatcher or dependencies merely
to satisfy a name. Identify the applicable supplied
RIS result/operation contract, owner, inputs, boundary, checks and stop
condition. For a project-owned skill retain its conventions and apply only
RIS rules relevant to its real RIS responsibilities; do not force package
naming or unrelated infrastructure. Do not claim future or illustrative
components are installed. Determine dependencies **from the target's actual
operation**, not a preselected list: shared RIS scope, dialogue, artifact and
quality rules belong to `ris-proj-lib-common`; selected project configuration and
paths belong to `ris-proj-op-resolve-context` only when needed; a portable method can be a
base skill; restricted tracker operations require an actually available
adapter. Declare how and when direct invocations load applicable dependencies
and owned resources and verify availability and application. Do not embed
their methods or claim that merely listing them performs their work.

For each action, identify its owner, input, output, activation condition and
verification: necessary work toward this result, a dependency's work, or a
separate operation. Distinguish a portable base, an optional reusable domain
or format specialist with its own contract, a project wrapper, an adapter and
an end-to-end scenario. When specifying a RIS package skill, record why an
autonomous portable base plus RIS wrapper is warranted, or why one skill
suffices; do not create layers for symmetry. A portable base must work without
RIS rules, config and project directories; a wrapper has an actual RIS result
beyond loading it and handles project inputs, permissions and output format.
An adapter executes bounded tool operations, not subject-matter decisions.
A scenario owns the sequence, permissions to advance, one dialogue and the
sufficiency and verification of the combined result; its component skills
retain their own results and direct invocation. A standalone wrapper may name
dependencies required for **its** result and describe a possible next result
in plain terms, but must not name, select or start the next skill. Only an
explicit scenario, human or external workflow decides that transition. A
standalone read-only navigation operation is the narrow exception: its own
result may select/name an available owner and recommend a prompt from current
facts and actual contracts, but it never executes the transition, accepts content
or grants readiness/authority. This does not add next-skill assignment to ordinary
wrappers or common reports. Keep optional
branches conditional without losing necessary instructions; do not move an
unrelated operation into a mandatory resource just to shrink the main file.
Declare an execution role only when an actual caller consumes it; describe
the kind of work, not a model or an unverified isolation guarantee. Direct
invocation must still work without a configured role.
For critical risks, ensure the resulting skill includes concrete subject-
specific shortcuts and observable failure signals with corrective reactions.

## Verify and stop

Apply the base's result-appropriate static, reading/review and, for executable
changes, ordinary program checks under the actual target project's rules.
Ordinary instruction edits need no new live run or repeated question about one;
source readiness is distinct from observed agent behavior. Additionally inspect
the **combined RIS result**:
responsibility boundaries, dependency availability and cycles, correct
activation on direct invocation, project-path provenance where applicable,
permissions, negative requirements, links and installed-relative resources.
Check typical and conditional instruction loading, adjacent operations and
improvement before/after prescriptions: the ordinary request must not require another
operation's instructions or a rare branch without cause; a conditional request
must apply that branch when needed. For a scenario, verify each component's
contribution, transition permissions and the combined result in its promised
form, including persisted state only when writing is part of its contract;
do not accept mere mentions of dependencies. Read/review the direct-invocation
contract of a wrapper independently of its caller and a neighboring request that
belongs to another owner. This does not require executing those requests. Inspect
actual saved source files; claims about execution effects need applicable existing
observations, not only an agent's success statement. Preserve historical versions,
unmet obligations and untested-client limits without converting them into a pass
or an automatic blocker for an ordinary instruction edit. A task with an explicitly
accepted behavioral objective needs separately agreed scope under project rules.

Deliver only the requested ready-to-use source folder or explicitly unsaved
draft. Do not install it into the user's working project, publish it, change
tracker state or perform its future subject-matter operation without separate
authorization. Report location, changes, structural/routing/behavioral
evidence, limitations and blockers; do not call a partial result complete.
