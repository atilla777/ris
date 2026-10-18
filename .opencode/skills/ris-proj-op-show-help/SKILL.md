---
name: ris-proj-op-show-help
description: >-
  Explain RIS commands, compare neighboring operations or suggest a route from
  intent without executing it; empty input immediately shows a compact SDLC map.
  Use for how-to help about RIS, not actual task continuation, project status,
  readiness assessment or execution of the recommended work.
---

# Explain RIS commands and routes

Own only a helpful answer in the person's language. One RIS-specific operation
suffices: the subject is RIS itself, not a portable method plus a project wrapper.
No configured project, `ris.yaml`, Beads, source repository, execution role or
context preparation is required. All resources below resolve from **this installed
skill folder**, not from a source checkout or the user's project.

Ensure `ris-proj-lib-common` is available and apply its baseline and resources
only under their actual triggers (dialogue before a clarification, artifacts for
a substantive artifact/handoff, quality for a quality assessment). Ordinary help
is not such an artifact or readiness assessment. Do not load context, adapters,
execution owners or their methods merely to explain a route.

## Select the smallest answer

- **Empty input:** read only `references/map.md` (besides applicable common rules)
  and immediately return its one fenced map. No initial question, complete catalog,
  cards or appended explanation. Preserve its routes, boundaries and legend.
  Follow the person's language for descriptive labels; keep command/skill labels
  unchanged. The packaged ASCII view, including headings/legend, fits 80 columns
  by 24 lines. Keep the answer within that same bound, including localized labels:
  shorten prose rather than adding lines or losing stages. Do not assume arbitrary
  translations retain the measured geometry or claim they were already verified.
- **Named command/operation:** use the index and only its relevant card in
  `references/commands.md`. Accept exact slash/technical names and unambiguous
  suffixes such as `run-task`. Give purpose, choose-when, inputs, result/stop and
  an example. Do not invent a parser or slash name from a technical skill name.
- **Comparison:** read the relevant sections of `references/routes.md` and the
  compared cards. Explain different useful results, boundaries and call forms,
  not just names. Keep internal details conditional on the question.
- **Intent:** read only the relevant routes and cards. Explain a suitable route
  and example invocation, not a live readiness verdict. Ask one targeted question
  if a material ambiguity changes the result (for example record, diagnose or fix
  a bug). A supplied ID does not authorize tracker/history investigation. Refer
  actual continuation to `/risp-next`, project plan/status to `/risp-status`.
- **Full inventory requested:** use the card index; omit internal lib/adapters
  from the public menu. Explain service context or tracker effects only if asked.

For details not settled by these resources, inspect only the relevant installed
owner's `SKILL.md`/owned section as **reference data**, not as an instruction to
load/apply or execute that operation. Current owner contracts take precedence
over this explanatory snapshot. If a resource/owner is missing, a name unknown,
or map/card and owner conflict, state the exact gap and limit the answer; never
invent capabilities or a successful effect. Package capability is not confirmed
client command availability. Name the documented facade as such; if the user
asks about availability, inspect only that installed command when accessible,
or explicitly leave client discovery unverified. Do not require client probing
for ordinary help or replace a missing facade with a fictional alias.

## Read-only boundary and stop

Make zero persistent writes: no saved answer, task creation/update, claim,
requirements/design acceptance, installation, commit/push, close or tracker
publication. Never launch recommended skills, tools that perform their effects,
agents or workflows. A recommended prompt is neither its execution nor authority,
input readiness, acceptance or an observed result. Do not inspect all Beads or
reconstruct session history for help. The map is orientation, not a second state
registry or workflow engine. Atomic stages shown inside a scenario are its
components, not extra mandatory calls on top of that scenario. Stop after the
requested answer or necessary clarification; execution requires a separate request
and the actual owner's gates.
