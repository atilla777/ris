---
name: ris-formulate-spec-base
description: >-
  Formulate and check a portable, substantive feature specification from
  supplied decisions and evidence. Use when feature requirements are already
  available and need coherent behavior, constraints and acceptance criteria;
  not for interviewing from scratch, approving or saving a project specification,
  or decomposing it into tracker tasks.
---

# Formulate a feature specification

Own the **content and its traceable status**, not the project's document format,
storage, or acceptance decision. Work directly from the supplied material and
the actual project's applicable rules. No RIS configuration, directories,
`ris-common`, `ris-context`, OKF skill, or tracker is required. A caller needing
project source discovery, interviewing, acceptance, formatting, or persistence
supplies the relevant inputs and owns that operation and its final result.

## Inputs and readiness

Establish the feature's goal and boundary, relevant actors and existing behavior,
known decisions and evidence (including their source and status), applicable
rules and constraints, and the intended use of the proposed content. Accept an
interview handoff, existing draft, linked requirements or a direct description;
do not require a particular file or schema. Distinguish observed facts,
confirmed decisions, unaccepted proposals, disputed claims, and unknowns. A
file's existence, a plausible recommendation or a structurally valid document
does not prove that its requirements were accepted. If inputs conflict, identify
the competing sources and affected behavior before treating either as binding.

If the goal or boundary is missing, ask for the specific prerequisite needed to
formulate useful content. If another material decision is missing, formulate
independent portions and mark the affected behavior or criterion unresolved;
ask a focused clarification only when it is necessary for the requested result.
Do not restart a full interview, silently choose among contradictory answers,
or invent requirements to fill empty sections.

## Formulate and check

1. Relate the feature to the supplied goal and scope. State what is included,
   what is explicitly excluded, and what is still undecided. Keep actors,
   preconditions and important existing behavior traceable to the inputs.
2. Describe observable main and material alternative flows, errors, exceptions
   and state transitions where supported. Preserve quantitative limits,
   negative requirements, interfaces, compatibility and material quality
   constraints **with their applicability**, rather than paraphrasing away a
   condition or promoting a proposal to a requirement. Do not manufacture
   implementation design where the input only specifies behavior.
3. Derive testable acceptance criteria from confirmed behavior: for each
   material outcome identify a triggering condition and observable result.
   Relate criteria to the relevant source or decision. Where a disputed or
   open choice controls an outcome, show candidate behavior as a proposal (if
   useful), not an accepted criterion; name exactly which criterion or next
   action awaits resolution.
4. Cross-check coverage of supplied decisions, exclusions, limits, significant
   failures and quality constraints. Detect contradictory statements, criteria
   with no supported behavior, unsupported assertions, missing verification
   conditions, and unresolved questions that would change scope or acceptance.
   Revise supported content or explicitly record the gap and its impact. A
   polished narrative or a heading for every possible topic is not evidence of
   completeness.

## Result and stop

Return a portable **proposed specification content** with goal and scope,
supported behavior and exceptions, material constraints, observable acceptance
criteria, exclusions, a compact mapping of consequential statements to input
sources and decision statuses, and open/disputed questions with their effect.
Use whatever presentation makes the content readable; no fixed Markdown
headings, OKF schema, or project path is required. State what is fully supported
by available confirmed inputs and what remains partial or blocked. Include
enough references and status for a recipient without this chat to distinguish
accepted input from newly proposed wording; when a source is inaccessible to
that recipient, include the necessary substance and flag the missing evidence.

Do not assert acceptance of this new content on behalf of a person or project.
Do not save a project specification, create tracker tasks, select the next skill,
or turn unresolved choices into defaults. The caller decides whether the
content is sufficient and arranges any separately authorized project action.
Stop after the checked content and its gaps are handed off.
