---
name: ris-interview-base
description: >-
  Investigate interdependent decisions within a bounded topic using a decision
  tree and return a sourced, status-aware interview handoff. Use for a multi-step
  interview with prerequisite and independent questions, either fully within
  scope or explicitly limited by a sufficiency criterion; not for a single
  clarification, stress-testing an idea, selecting feature requirements, or
  writing and approving a specification.
---

# Interview through a decision tree

Own the **method and the interview handoff**, not the subject matter, acceptance
of requirements, or a saved specification. Work directly under the actual
project's rules, including outside RIS. No `ris-common`, `ris-context`,
`ris.yaml`, Beads, project layout, `grilling`, or OpenCode command is required.
A caller that owns a subject-specific result supplies the topic and its relevant
decision areas, joins this method into **one** dialogue, and checks its own
result; do not start a second interview or an ensuing workflow stage.

## Establish inputs and mode

Obtain a topic, boundaries, intended next result, available documents/facts
and constraints, and prior answers with their sources and status (confirmed,
proposed, disputed, unknown, or deferred). Use only answers actually available
in this conversation, provided handoff, or accessible sources; the existence
of a document does not prove its decisions were accepted. If the topic or
boundary is missing or too broad, establish that prerequisite first with one
question, or report the blocking gap if it cannot be established. Do not invent
the agenda. A direct invocation may take its bounded subject from the user's
request; it need not have a RIS project.

Default to **full mode**: cover all material branches *within those bounds*,
not every conceivable product question. Enter **limited mode only on an
explicit request** with a sufficiency criterion for the named next result.
If that criterion is absent, ask for it before treating the interview as
limited; do not silently substitute a question count or time limit.

## Investigate and maintain the tree

1. Inspect accessible relevant documents, code and prior answers before
   asking a person. Research technical facts with available means instead of
   asking the user to look them up; no subagent is required. Record source,
   currency and status. For an unavailable material source name what is
   unavailable, why, and which decision/result it affects. For a conflict
   identify both sources and the affected decision; do not infer acceptance
   from either. Attribute only answers actually present in each source; do
   not fill a missing answer from a different branch, a recommendation, or an
   inaccessible conversation. Do not re-ask a confirmed answer unless a
   material conflict calls it into question.
2. Build a working tree: which decisions are prerequisites, which depend on
   each possible answer, and which material branches are independent. Mark
   known answers, conditional branches, unknowns and deferred decisions. The
   currently answerable material questions form the **frontier**. Consider
   alternative paths only if relevant within the topic; avoid hypothetical
   branches just to make the tree look complete.
3. Choose the next material frontier question. Explain its context and the
   consequences of genuinely different options; offer short options with a
   reasoned recommendation and room for a free answer when choices are useful
   and a recommendation is supportable. For an open or factual question do not
   fabricate a menu. When continuing, distinguish the confirmed previous
   answer from proposals before asking the next question; use the caller's
   dialogue presentation rules when provided, without requiring RIS or a
   particular visual format for direct use. Ask **one decision question
   per message**, wait for the answer, update its status and dependencies, then
   recompute the frontier. Ask several independent questions in one message
   only if the user expressly requests that; never ask a dependent question
   before its prerequisite is answered. Do not equate agreement with one
   recommendation to agreement with adjacent decisions.
4. If a decision is deferred, retain it and its impact without guessing its
   descendants; continue investigating independent material branches. If an
   answer removes a branch or opens new ones, update the tree rather than
   following a fixed questionnaire. A proposed answer is not confirmed by
   repetition. Surface genuine unresolved conflicts and ask for a decision
   only where evidence cannot resolve it.

## Stop and hand off

In full mode, stop once every material branch inside the topic has been
investigated as far as evidence and current decisions permit. Distinguish a
branch **considered** from a decision **accepted**; explain what unresolved or
unavailable information blocks, and what independent work remains possible.
In limited mode stop when the supplied criterion for the next result is met
without material gaps **or** a blocking gap that cannot now be closed is
established. Identify remaining nonblocking branches as **not covered**, not
as investigated. The owner of the next result decides whether the handoff is
sufficient for its work.

Return a portable handoff in the response: topic, bounds, intended result,
mode and stopping reason; material decisions/answers with status and sources;
their prerequisites and affected dependent branches; deferred, disputed,
unknown and uninvestigated questions with their impact on the next result.
Separate facts from decisions and proposals from acceptance. If blocked, give
the exact missing input and useful independently established information.
The handoff must be explicitly passed to a future conversation or backed by
an accessible source: do not assume access to an earlier chat. Do not write a
file, create a task, accept requirements for the person, or initiate a
specification or another stage by default. Stop after the handoff.
