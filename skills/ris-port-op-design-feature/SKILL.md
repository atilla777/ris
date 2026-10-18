---
name: ris-port-op-design-feature
description: >-
  Propose and check sufficient technical design for one bounded feature from
  supplied requirements, current code and architectural constraints. Use for
  portable feature design or a focused design revision; not for eliciting
  product requirements, accepting or saving a project design, decomposing tasks,
  or implementing code.
---

# Design a bounded feature

Own a **portable, read-only design proposal and its checked limitations**.
Work from supplied inputs and accessible evidence under the actual project's
rules. No RIS configuration, directories, tracker, `ris-proj-lib-common`, `ris-proj-op-resolve-context`
or other installed skill is required. A project caller supplies project inputs
and owns acceptance, formatting, storage, tracker changes and the combined
result. Direct invocation returns content without writing files or records.

## Establish the design boundary

Identify the selected increment, behavior and stable acceptance criteria,
requirements version and acceptance status, current code/revision, applicable
architecture/contracts and versions, relevant accepted active designs, and
whether this is an initial design or revision of a supplied prior design.
Do not infer acceptance or actuality from a filename, status or diagram.
Distinguish observed code, binding rules, accepted future designs, proposals
and unknowns. Missing current code is legitimate for a confirmed new project;
state that baseline explicitly instead of inventing existing interfaces.
For an existing project, inaccessible/stale code limits supported conclusions.
If essential inputs conflict or are missing, block dependent decisions, return
independent analysis and identify the exact evidence/decision needed.

## Develop and check sufficient design

1. Map the bounded behavior and AC to current flows and existing interfaces or
   analogues; inspect relevant code and tests, not the entire codebase. Prefer
   reuse before introducing abstractions. Identify facts with paths/symbols and
   revisions so the proposal does not pretend that future components exist.
2. Allocate component responsibility and state ownership; show public contracts,
   allowed dependency direction, callers, compatibility and errors. Choose the
   minimum sufficient boundaries, never impose Service Layer, ECS, DDD or a
   separate stack per feature. A vertical or headless slice can reuse shared
   components. New abstractions need a concrete responsibility and reason.
3. Trace critical data/state transitions, transactions, retries and failure
   handling; include migrations, resource/performance constraints only where
   material. Explain how concurrent changes or partial failure preserve relevant
   invariants. Do not design unrelated future capabilities.
4. Define **test seams before task splitting**: stable boundaries to observe
   each AC, contract tests, necessary shared integration scenarios, architectural
   fitness checks and subjective observations. Show test setup/oracle and coverage
   without creating implementation tasks or treating a build as proof of an AC.
5. Compare material alternatives and their tradeoffs only where needed. Identify
   durable/hard-to-reverse decisions that may need an ADR and independent
   architecture review (e.g. public contract, component boundary or state owner
   change). Local reversible choices do not need formal ADR or reacceptance.
6. Check applicable architecture rules and related active accepted designs.
   Shared file edits alone are not conflicts. For incompatible common contracts,
   identify both versions/owners, affected flows/AC, a proposed single contract
   and integration owner, and necessary blocked → prerequisite relationships.
   Mark that resolution proposed until the authorized owners agree; keep
   independent work available, never halt all features by default.
7. On revision compare old/new requirements, design, linked product sources
   and contracts against available baselines. Trace changed decisions to affected
   AC, tasks, tests, ADR and neighbor designs using supplied links. Missing
   baseline makes applicability unconfirmed. Separate local implementation
   choices (no new acceptance), substantive design change (focused acceptance
   and impact), behavior change (requirements-owner decision), and global
   invariant/contract change (separate architectural authority). Do not silently
   redefine behavior or redesign the entire roadmap. Unchanged requirements
   retain their acceptance; the proposed design does not approve changed ones.

Cross-check every material AC against the proposed approach and test seam,
state/contract ownership, errors and relevant architecture constraints. A list
of components without flows or oracles is insufficient. For a simple feature,
a short justified confirmation of existing contracts and a minimal approach can
be sufficient; do not manufacture design detail or claim requirements alone
are a design. Return unresolved choices with their precise dependent scope.

## Return and stop

Lead with a plain-language explanation of the design: its essence and main flow,
reused and new technologies and why, tradeoffs, material risks and irreversible
or hard-to-reverse choices. Aim for roughly one screen as a readability guideline,
not a measured limit; never omit material decisions to fit it. Identify the exact
complete candidate version/scope and provide its full text for the caller's
separate acceptance discussion. The explanation supplements, not replaces, the
full technical proposal below. A short full design can itself supply this readable
explanation without a duplicate summary. For a long design, optional Markdown
draft storage belongs to an authorized caller/writer at an explicitly agreed
destination, not this read-only author; no draft file is required.

Return the proposed sufficient design: bounded result and input versions/status,
observed baseline and sources, components/ownership/contracts/dependencies,
critical flows/failures, AC → test seams and integration/fitness coverage,
material tradeoffs, proposed ADR/review needs, compatibility and active-design
impact, revision delta if applicable, independent portions and blockers.
Separate confirmed constraints from proposed decisions. Include enough substance
and evidence for a recipient without this conversation; identify inaccessible
sources and limits rather than asserting currency. Do not declare the proposal
accepted, save it, edit product/rules/code, change a tracker, split tasks or start
another operation. Stop after the checked content and limitations.
