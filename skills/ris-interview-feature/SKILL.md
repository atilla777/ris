---
name: ris-interview-feature
description: >-
  Interview for a selected feature's functional and material quality requirements
  and return a sourced, status-aware handoff without writing. Use when asked to
  elicit or clarify feature requirements through a dialogue; not for selecting
  the next feature, stress-testing an idea, drafting or accepting its full
  specification, creating tracker tasks, or asking a single clarification.
---

# Interview about feature requirements

Own the **project-specific coverage and final handoff**. Use the installed
`ris-interview-base` for the decision-tree method in the **same conversation**;
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

Ensure installed `ris-common` is available and apply its rules. Read its
conditional dialogue, artifact and quality resources before the respective
actions. Use installed `ris-context` and **its configuration resource** to
prepare the selected project's `sources.rules`, `sources.concepts` and
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

## Map the material requirements

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

Ensure installed `ris-interview-base` is available and **apply** its method to
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

Check each material area against evidence and the actual decision-tree result:
separate confirmed, proposed, disputed, deferred and unknown answers; give
reasons for inapplicability and identify unexamined branches in limited mode.
If an essential answer is absent, specify its impact instead of claiming
requirements are accepted or complete. Return **in the response**, without
writing: project, feature identity and bounds (confirmed ID only), relevant
sources with status, material map areas and answers with their sources/status,
inapplicable areas with reasons, unresolved decisions and dependent areas,
impact on subsequent specification work, interview mode and stopping reason.
An earlier handoff is reusable only insofar as its content is current and
accessible; a later conversation needs this handoff explicitly or an accessible
confirmed document. `ris-specify-feature`, if subsequently available, owns
the decision about sufficiency, formulation, acceptance, file format and path.
Do not create a specification, intermediate interview file, Beads issue or
link, choose a specification path, or start the next stage here.
