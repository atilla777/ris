---
name: ris-proj-op-interview-feature
description: >-
  Interview for a selected feature's functional and material quality requirements
  and return a sourced, status-aware handoff without writing. Use when asked to
  elicit or clarify feature requirements through a dialogue; not for selecting
  the next feature, stress-testing an idea, drafting or accepting its full
  specification, creating tracker tasks, or asking a single clarification.
---

# Interview about feature requirements

For an existing confirmed feature read/apply installed specify-feature's owned
`references/stage-prerequisites.md` before dependent requirements interviewing.
Use exact readable prerequisite decision references even if native blocks is empty;
implementation-only dependencies do not by themselves prevent independent questions.
Unknown/real requirements blockers stop the dependent action, not unrelated inquiry.

Own the **project-specific coverage and final handoff**. Use the installed
`ris-port-op-interview` when an interview is needed, for the decision-tree method in the **same conversation**;
do not conduct a second interview or restate its question algorithm. This is
one RIS project skill because identifying applicable project evidence and
checking feature-requirement coverage are its own result; no additional
portable subject-matter base is needed. Stop before specification authoring.

## Establish scope and evidence

Establish the target project and the selected feature's identity, expected
outcome and bounds from the request and accessible evidence. An ID is optional:
use one only if confirmed. If the feature or its boundary is ambiguous, clarify
that prerequisite before treating any other questions as a feature interview;
do not select a feature or infer an ID from a title. Gather answers from this
conversation, an explicitly supplied earlier handoff and accessible project
sources; do not assume access to an old chat.

Ensure installed `ris-proj-lib-common` is available and apply its rules. Read its
conditional dialogue, artifact and quality resources before the respective
actions. Use installed `ris-proj-op-resolve-context` and **its configuration resource** to
prepare the selected project's `sources.rules`, `sources.product` and
`sources.specs` needed for this operation. Check status, provenance, relevant
paths, diagnostics and read-only scope before using them. Read applicable
project instructions and rules, then select only documents relevant to this
feature by links, subject and acceptance status; do not read every file in
the configured directories or mistake directory presence for acceptance.
Select an available project-specific feature-requirements profile if present;
its absence does not block the interview. A project's own path and rules take
precedence over examples from RIS. Research accessible facts (including code
where relevant) yourself rather than asking the user to look them up. If a
material source is inaccessible, name it, why, and the affected requirement.
For competing sources, identify both, their statuses and the impacted decision;
ask for resolution where evidence cannot settle it, rather than silently
choosing one. Treat a prior handoff by its actual answers and gaps, not the
assertion that an interview once happened.

Author-owned product material may freely mix mechanics, world, content and
examples across systems. Extract only the selected feature's relevant decisions;
do not require chapters matching components, feature boundaries or numbered
product requirements. Distinguish accepted descriptions, drafts, examples and
open questions. Carry exact paths/headings and available source revisions into
the handoff. Compare linked sources to the versions underlying reused answers;
missing baseline versions make applicability unconfirmed. Surface changed
behavior and affected known AC/design/task references for a focused decision,
without scanning the entire product or editing it. Preserve existing `AC-nnn`
identities when supplied; candidate outcomes do not acquire accepted status.

When a material choice about feature behavior has established alternatives,
check accessible relevant standards, common solutions and practices before
recommending an option or asking the person to choose. Compare their
fit with the feature's goal, accepted requirements and project rules; cite
the source and explain applicability. Surface a conflict as a decision rather
than overriding project rules or promoting an external practice to an accepted
requirement. Do not require a survey for a small feature or an already
confirmed choice, or turn this evidence gathering into implementation design.

## Map the material requirements

This map and **Check and hand off** below are the single reusable project
coverage method for direct specification and feature preparation. Consumers load
and apply these sections to available scope, answers and evidence **before**
deciding whether an interview is needed, and check their resulting content
before dependent acceptance. Reusing them is not an interview invocation and
does not activate the interview-only evidence gathering or decision tree.

Use the following **semantic map**, not mandatory headings or a questionnaire.
Compare what is known with what this feature needs; mark an area inapplicable
with a reason instead of manufacturing requirements. A project's applicable
content profile may refine this map. It cannot silently override accepted
requirements: expose any conflict with its sources and impact.

- Purpose, actors, primary and alternative scenarios; scope and exclusions.
- Behavior, data, states/transitions, errors and edge cases.
- Interfaces, compatibility, numerical limits and negative constraints **when
  material** to the feature.
- Material quality properties such as performance, security, accessibility or
  reliability, with their applicability conditions. Do not defer a requirement
  essential to defining the outcome merely because it sounds technical.
- Observable acceptance outcomes and ways to verify the useful result.
- Sources and status of decisions, dependencies, unresolved questions and their
  effect on preparing a specification.

For each material question retain a confirmed answer with its source/status,
an open decision with its impact, or a reason for inapplicability. Proposed,
disputed, deferred and unknown answers remain open; merely listing one does not
close a dependent acceptance gate. Reuse current confirmed answers. With
sufficient evidence, proceed directly to formulation or validate the supplied
accepted candidate, without questions, an interview, a new executor or a separate
coverage report. Return only material gaps or conflicts to the human (to the
caller in noninteractive work); preserve independent useful work. A single
clarification does not require an interview when the other material areas are checked.

Only when missing material answers require an interview, ensure installed
`ris-port-op-interview` is available and **apply** its method to
the bounded feature and this map: give it the known answers, sources, statuses,
open areas and intended handoff, and maintain one dialogue. Default to full
mode across all material branches within the feature; use limited mode only on
the user's explicit request with a named stopping criterion for this result.
If that criterion is missing, ask for it. A small feature needs only its
material areas, not a tour of every quality attribute. An unresolved or
deferred decision does not become accepted and does not prevent exploration
of independent material areas. Do not re-ask already confirmed answers absent
a material conflict. If a required dependency or resource is unavailable,
identify the blocked part and return only independently verified evidence;
do not label it a completed interview.

## Check and hand off

Check each material area against evidence and, if used, the actual decision-tree result:
separate confirmed, proposed, disputed, deferred and unknown answers; give
reasons for inapplicability and identify unexamined branches in limited mode.
Apply this same check to a consumer's candidate, using current known answers and
sources; a plausible draft or approval alone does not establish coverage.
An open essential decision blocks acceptance of its dependent result, not
independent work. Consumers keep this evidence in their existing dialogue or
handoff, without a separate checking operation, file or report.
If an essential answer is absent, specify its impact instead of claiming
requirements are accepted or complete. Return **in the response**, without
writing: project, feature identity and bounds (confirmed ID only), relevant
sources with status, material map areas and answers with their sources/status,
inapplicable areas with reasons, unresolved decisions and dependent areas,
applicable recommendations with sources and proposed status (if any), impact
on subsequent specification work, interview mode and stopping reason when used.
An earlier handoff is reusable only insofar as its content is current and
accessible; a later conversation needs this handoff explicitly or an accessible
confirmed document. The owner of subsequent specification work decides
sufficiency, formulation, acceptance, file format and path.
Do not create a specification, intermediate interview file, Beads issue or
link, choose a specification path, or start the next stage here.
