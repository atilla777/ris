---
name: ris-proj-op-show-help
description: >-
  Explain RIS commands, compare neighboring operations or suggest a route from
  intent without executing it; empty input shows daily SDLC help, and an explicit
  full-help request shows detailed thematic pages.
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

- **Empty input or explicit simple help** (`простой`, `кратко`, `simple`, `brief`):
  read only `references/map.md` (besides applicable common rules) and immediately
  return its daily Markdown view. No initial question, fenced map, ASCII frames,
  complete catalog, cards or appended explanation. Preserve all commands and short
  explanations; omit installation, init, roadmap, bugs, acceptance and retro here.
  Use full slash names, section icons, blank lines after headings and horizontal
  separators **between sections**, not directly below the main title. There is no
  fixed 80x24 geometry: prioritize readable daily help, not denser one-line chains.
- **Explicit full help** (`полный`, `подробная справка`, `full`, `detailed`): read
  only `references/full.md` (besides applicable common rules) and return its detailed
  thematic pages in order. Each operation has its own heading, exact call and short
  explanation. Pages are sections of one answer, not extra commands, a client pager
  or an execution sequence. Do not collapse distinct operations into one line.
  A request for a specific topic/card/comparison still takes the narrower route
  below; the word "full" within a question does not automatically select all pages.
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
- **Exhaustive inventory requested:** use the card index; omit internal lib/adapters
  from the public menu. Explain service context or tracker effects only if asked.

For both packaged views, localize descriptive labels to the person's language;
keep exact command/skill identifiers unchanged. In Russian, daily section labels
are `ГДЕ МЫ`, `ПРОРАБОТАТЬ ФИЧУ (ПОДГОТОВИТЬ ЗАДАЧИ)`,
`ВЫПОЛНИТЬ ОЧЕРЕДНУЮ ПОДГОТОВЛЕННУЮ ЗАДАЧУ` and `ПОДРОБНЕЕ`.
The title is `RIS · ОСНОВНОЕ`; the full-help link is `/ris-help полный`
(`/ris-help full` in English). These are arguments to the existing help command,
not new slash facades or executable parser flags. Never append an implementation
disclaimer about the two views: they are this skill's current source contract.

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
