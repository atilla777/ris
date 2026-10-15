---
name: ris-port-op-formulate-architecture-rules
description: >-
  Formulate a portable architecture-rules proposal or bounded amendment from
  supplied project facts, decisions and constraints, with sourced norms and
  open questions. Use for creating or revising normative architecture rules,
  including Rails web and DragonRuby/Odin games; not for accepting or saving
  project documents, code audit, feature design, tooling setup, impact delivery
  or extracting a library.
---

# Formulate normative architecture rules

Own the **checked, read-only content proposal**, not its acceptance or storage.
Operate directly under the actual project's instructions, including outside
RIS. No RIS configuration, document layout, tracker, `ris-proj-lib-common` or
`ris-proj-op-resolve-context` is required. A project caller supplies evidence and owns project
acceptance, formatting, saving and the combined result. Do not write files or
records, migrate document formats, change code/tools, audit compliance, enumerate
delivery impact or start another lifecycle operation. Rules may govern future
work; they are not a factual map of components already implemented.

## Inputs and readiness

Establish create/update, the architecture subject and requested boundary,
purpose and nearest goal, known constraints and actual/proposed stack,
available sources with currency and status, prior answers and related rules
(especially development rules when available). Direct invocation takes these
from the request and explicitly supplied or accessible evidence; no universal
input schema or filenames are necessary.

- Create can start with purpose, nearest goal, constraints and selected or
  discussed stack; full product, roadmap and future feature designs are optional.
  Distinguish a new project with no code from inaccessible existing code.
- Update additionally requires the existing rules and explicit change scope.
  Without them return the missing input; never silently switch to create.
  Preserve unaffected norms and their identities, exceptions and status.
- Keep confirmed decisions, observed facts, assumptions, proposals, examples,
  disputed/unknown/deferred questions distinct. A file or repeated recommendation
  is not evidence of acceptance. Conflicting or stale material limits dependent
  rules, not all independent work.

## Resources and conditional interview

Read local [principles](references/principles.md) for the substantive foundation;
in update apply it only to the selected scope and relevant consistency checks,
not as permission to rewrite the whole document. Resources resolve from this
installed skill folder, never the source repository root.

Read **only** the applicable profile: [Rails](references/rails.md) for Rails web,
[DragonRuby](references/dragonruby.md) for DragonRuby games,
[Odin](references/odin.md) for Odin games. A mixed project loads only affected
profiles. An unlisted stack can use the common method with researched facts;
do not invent a supported profile or impose one of these stacks.

When material decisions remain, read [the subject decision tree](references/interview-tree.md).
For interdependent unknown decisions, load and actually apply installed
`ris-port-op-interview`: supply the bounded topic, decision branches/prerequisites,
known answers with sources/status and intended rules result; join its handoff
into the same conversation. It is the only conditional skill dependency.
Do not reproduce its procedure or require it when answers are sufficient.
For a single clarification ask directly. If the needed interview skill/resource
is unavailable, report that dependent work blocked and return independent
content; do not simulate the dependency or require RIS configuration instead.
Do not repeat confirmed answers. Explicit deferral leaves dependent choices
open; investigate independent material branches and record a return trigger
when known. The base owns subject sufficiency after the interview handoff.

## Formulate and check

1. Inspect relevant supplied documents/code/configuration to establish facts,
   not to audit the entire project. Research technical facts as needed; report
   unavailable sources and the decisions they affect. Compare profile facts to
   the actual runtime and constraints before recommending a norm.
2. Determine the minimum necessary decisions for this scope/nearest work. Keep
   durable principles, confirmed concrete decisions and conditional profile
   options separate. Never pick ECS, Service Layer, an event bus, threads or all
   future subsystems just because the profile mentions them.
3. Formulate substantive norms: responsibilities/public versus internal,
   mutable-state owners/access, interfaces and dependency directions,
   applicable invariants/errors/lifetimes, consistency and partial failures,
   boundary verifiability, substantive-change approval and justified exceptions.
   Explain each significant rule's requirement, applicability, rationale,
   observable verification and exception handling; concise combined prose is
   fine. Use concrete supplied owners/interfaces where known, otherwise propose
   only supported boundaries and mark unresolved assignments visibly.
4. For games, always address **consideration** of reuse during design/review;
   extraction needs demonstrated benefit. Distinguish a subsystem, an internal
   reusable module and an independent library. Describe interface/dependencies,
   state and lifecycle obligations for justified extraction without performing
   it. A small game does not require a separate library or repository.
5. For update return the exact old → proposed norm delta, rationale and scope,
   without rebuilding unrelated rules. Identify conflicts within relevant rules
   and with adjacent engineering rules. Architecture owns what must hold and
   technology choices affecting system structure; engineering owns versions,
   tools and practices that support it. Name a necessary adjacent decision or
   amendment, do not edit or call its owner automatically.
6. Check substantive coverage within scope, state/contract ownership,
   allowed dependencies, failure/lifetime consistency, and proportionate
   verification. Keep unaccepted assumptions out of binding text. A proposal
   may include supported candidate decisions explicitly awaiting acceptance;
   unknown choices must not masquerade as selected ones. Mark meaningful
   deferred questions and triggers, exceptions and limitations. For existing
   projects propose a scoped transition policy if needed; do not claim all old
   code complies or produce a migration backlog.

## Return and stop

Return enough content to use without this chat:

- operation/scope, input sources and their versions/currency/decision status;
- proposed normative content (or bounded amendment) with rationale, verification
  expectations and exception/change authority from evidence or visibly proposed;
- confirmed decisions reused, candidate decisions awaiting acceptance,
  conditional recommendations kept out of binding text;
- deferred/unknown/disputed questions, their precise dependent scope and known
  return triggers; adjacent conflicts and independently usable parts;
- documentary sufficiency/consistency checks and their limits, unavailable
  evidence, and explicit statement that the proposal was neither accepted nor
  saved and implementation compliance was not checked.

If essentials are missing, return a partial result and exact missing
input/decision rather than a complete-looking generic template. Stop after
the checked proposal. Do not request final acceptance or save even if the
person agrees; those actions belong to the project author/caller.
