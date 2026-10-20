---
name: ris-proj-op-show-plan
description: >-
  Show the complete compact unclosed plan of a selected RIS project or exact ID
  subtree, with real hierarchy, directed blockers and one evidence-based next
  action. Use for read-only plan/status overview; not for executing work, choosing
  a feature within an epic, planning tasks, accepting delivery or changing Beads.
---

# Show the plan and one next action

Own the overview scope, complete compact tree, candidate selection and sufficiency
of the combined response. One project-only skill suffices: this result depends on
RIS project/tracker semantics and installed navigation owners, not an independent
portable method. Work in the current agent; no execution role or subagent is
required. The continuation owner supplies the evidence-based action for the exact
candidate; it does not own this whole-plan selection.

Make zero persistent changes. Do not save a report, claim/heartbeat, accept content,
create/update/repair/close records, install/synchronize a package, pull/push, block
writers or launch the recommendation. Recommendation is neither authority nor
proof of readiness; another assignee never authorizes takeover. Stop at the response.

## Establish scope and apply dependencies

1. Establish the selected project/current copy and optional **exact ID** from the
   request. Empty arguments mean the entire selected project's plan, not a question
   for an ID. An ambiguous project or non-exact locator needs only that clarification;
   never select a project from this skill's installation path or another backlog.
2. Load/apply installed `ris-proj-lib-common`, its quality resource before assessing
   evidence, dialogue for questions/decisions and artifacts under its actual transfer/
   partial-result triggers. Load/apply installed `ris-proj-op-resolve-context` and its
   owned configuration resource for this project, applicable rules and selected
   tasks adapter. Check returned status, provenance, paths and diagnostics. Do not
   require product, shared notes, workspace paths or execution roles just to list
   tracker work. If a recommendation needs a missing source, expose that dependent
   gap; never substitute concepts for a missing configured product directory.
3. Load/apply the selected **installed** adapter and verify it supports complete
   all-working-type/status inventory, exact actual-type reads, complete children,
   actual parent membership and directed blocks. These are not guaranteed by
   task-only `tasks` v1. With `ris-proj-adapter-beads-tasks`, read/apply its owned
   `references/plan-overview.md` before these reads. Other adapters must supply an
   equivalent checked read contract; do not invent native routes or silently use
   a partial task-only inventory. Resolve every resource from its actual installed
   owner, not the source checkout or a presumed sibling directory.

This skill combines and checks these contributions; merely loading or naming them
is insufficient. Missing dependency/capability blocks its dependent claims, retaining
independent observations and explicit limitations. Do not initialize a tracker.

## Read the bounded working set

- **No ID:** obtain the complete project candidate set, all types and statuses,
  including normally hidden working categories. Closed records support hierarchy,
  counters and inactive-blocker checks. Apply the adapter's proven work versus
  infrastructure/template classification; unknown types/roles remain visible.
- **Exact ID:** read that one record without presupposing type, then recursively
  enumerate all direct children including closed records. Read necessary ancestors
  and external blockers by exact ID. Do not demand the entire project inventory or
  expand independent trees of external records. A closed selected root is still
  explicit context; an unknown ID is an exact read gap, not an empty project.

Build only a temporary ID map and separate membership and blocked → prerequisite
edges. Never derive parenthood from ID punctuation. Retrieve missing parent/edge
fields with bounded exact/typed reads; a brief omission or count is not absence.
Fetch required row attributes or potential feature descriptions as needed. For RIS
feature interpretation apply the adapter's current feature-reading contract and
conditional resource. Neither native `feature` nor any task under an epic proves
RIS feature kind. Preserve ordinary, unsupported historical, malformed and unknown
records with their diagnostics, without conversion or artificial parents.

Validate complete output, IDs, scope and edge shapes through the adapter. Do not
silently truncate or collapse branches. Recover truncated host output with its
saved-output reader/bounded read route; otherwise report exactly what is incomplete.
Failed, malformed, unsupported or partial reads are not successful empty selections.
Do not audit every linked spec, decision, Git publication or lifecycle history for
the ordinary tree. Expand those only for a named question affecting the one final
recommendation. Unknown values stay unknown.

## Render one compact tree

Use the person's language. Show every unclosed working record in scope exactly
once as a primary short line; no hidden cap, collapsed branch or copied description.
Use indentation for actual parents, with separate standalone branches (no artificial
epic) and an explicit diagnostic group for cyclic, missing-parent or contradictory
hierarchies. Preserve all affected records there once rather than dropping them or
inventing reparenting. Display closed ancestors of unclosed work, and a closed selected
root, marked **closed, context**. Closed descendants otherwise need no primary lines.
External blockers of an ID scope get separate short contextual rows with ID, title
and raw status, not independent trees; reuse references for endpoints already shown.

Line form (localize labels):

```text
<ID> <title> [native type/RIS role; raw status; Pn; assignee; waits ID; due; progress; stage]
```

- Always ID, title, native type/role, **raw** Beads status and priority (P0 is highest).
  Mark unknown required fields explicitly. Add assignee, due and active blocker IDs
  when present; disclose material unknowns instead of implying none. `waits X` means
  this row depends on X, including cross-branch prerequisites. Checked closed blockers
  are inactive; unknown endpoint status must not establish readiness.
- Containers show **closed/all direct children**, including administrative closures.
  State that denominator in a short legend: status counter, not acceptance or criteria
  completion. Never use recursive totals; if direct composition is incomplete, label
  the counter unknown/incomplete rather than exact. Zero children is not proof that
  the container's mandatory work is fully specified or accepted.
- Features show compact requirements/design evidence: reference present, acceptance
  unverified; acceptance checked against exact version and separate decision; checked
  absent; or unknown/malformed. Include early /2 root features without inventing
  an epic: show nullable identity and refs as unfinished preparation, not ordinary
  tasks or malformed records. Known copy/identity/accepted-input gaps inform the
  continuation recommendation; no extra registry or acceptance audit for the tree.
  Brief omission cannot prove absence; a structurally
  valid feature record, file/link, closed children or no blockers cannot prove acceptance.
- Interpret stage only from sufficient facts and preserve raw status. `in_progress`
  means **in work according to Beads**, not a proven running flow. `needs design` or
  `needs acceptance` needs the relevant inspected inputs; otherwise mark stage unclear/
  unconfirmed. Ordinary tree evidence and deeper recommendation evidence stay distinct.

## Select exactly one candidate and apply continuation

Choose within the requested working scope, not contextual ancestors/external blockers
outside it. Distinguish a container's **own next result** from unfinished work
already represented by its descendants; they are not independent peers merely
because both records are open. Containers are not unconditionally excluded.
For an exact-ID request retain that selected container/subtree scope and explain
any child-level need with its exact ID; never silently substitute a child subject.

1. First consider started unfinished work; `in_progress` is a signal to inspect,
   not proof of an executing scenario. Among several, order by priority, then earlier
   start time, with stable ID as final tie-break. Disclose unknown ordering fields;
   do not infer start from ID or updated time or claim a proven order when it matters.
2. Only if none is started, before ranking a container against its descendants,
   inspect its own outcome/criteria, actual child composition and known effects.
   Identify a concrete own result needed **now** (for example acceptance/completeness,
   reconciliation, or selecting a genuinely missing feature). Open status, a broad
   goal or an old next-feature sentence is not alone such evidence. Eventual final
   acceptance is not a competing next result while its mandatory descendant work
   is unfinished, unless a concrete current acceptance/reconciliation issue needs
   container-level action. When work is
   already represented by existing descendants and no own next result is found,
   advance that existing work within the branch instead of letting its ancestor
   win by ID. This is navigation, not choosing a new product feature or defining
   tasks. Preserve a genuinely pending container result; if the distinction is
   material but unresolved, inspect bounded relevant sources/decisions or report
   the exact gap rather than treating unknown as no own result. Do not hide a
   blocked/foreign-assigned descendant by recommending new work at its parent.
   Rank the resulting candidates by priority and directed dependencies. At equal priority
   consider a prerequisite before the work depending on it; use stable ID for otherwise
   equal **independent results**, not a parent and the same represented child work.
   A cycle or unknown material ordering fact is a visible
   selection limitation, not invented readiness. Do not discard blocked work or containers
   merely to get an executable command.
3. Load and **apply** installed `ris-proj-op-suggest-continuation` for that exact ID,
   selected project, overview scope, checked facts and their limitations. Follow its
   bounded source/decision/owner inspection method in this current agent; a mention
   or an unexamined `/risp-next` prompt is not its result. Do not copy its lifecycle
   or recovery algorithm here and do not execute the contracts read as evidence.
4. Check its returned subject and action against this candidate and scope. If started
   work needs a decision, has a missing input or a foreign assignee, return that precise
   decision/gap or coordination need; do not scan new candidates for a convenient slash.
   No matching installed owner is an explicit gap, not permission to invent one.
5. Before presenting a slash prompt, verify the **actual installed command template**,
   its explicit owner target, client availability and required ID/locator/arguments.
   The continuation owner performs this check; inspect its evidence in the combined
   result. Source-only `/risp-status`, a future `/risp-run-simple-task` or a skill name
   is not an installed command. Missing command blocks the slash form: say which is
   missing. An exact natural-language prompt is permissible only for an actually
   available compatible owner, with the slash gap explicit, never as an absent-owner
   workaround or invented authority.
6. Fresh-read the candidate and material membership/blocker/evidence facts before
   finalizing. Reconsider affected conclusions after concurrent change; if its new
   status changes selection, reconsider the affected candidate ordering. Do not claim
   a transactional project snapshot. Persistent changes or an incomplete working set
   limit confidence: no globally best-candidate assertion when unseen work could win.

## Return and stop

Return compactly: selected project/scope and coverage; the tree and brief legend;
then **one next action**, short reason (including selection order), and checked slash
prompt, or one exact human decision/input/owner/command gap. Include only evidence
locators/versions needed for that conclusion, and separate unknowns from checked
facts. With incomplete input keep the available tree labeled partial; a conditional
recommendation must say it is only among observed records. If selection itself is
underdetermined, return the precise missing read/decision instead of a ranked winner.

When the recommendation concerns foreign started work or could be confused with
automatic execution selection, briefly explain: this is a project/scoped next
action, `/risp-next <ID>` continues selected work, while no-ID `/risp-run-task`
checks confirmed own unfinished work before ready tasks and stops on blocked own
work. Different results are possible; foreign work requires coordination, not takeover.

A complete set with no unclosed work says so directly and creates no artificial
action. A closed ID with open descendants still shows those descendants; a closed
ID without them says no unclosed work **in that scope**, not the whole project.
Failed reads never mean empty. Use `ok|blocked|conflict|error` when a status is useful:
`ok` covers this bounded overview/recommendation only, never downstream readiness.
Disclose read failures, malformed data, unsupported capability, command/owner gaps
and concurrent-state limits. State that nothing was changed or launched. The response
is not saved or automatically discoverable in another session. Stop here.
