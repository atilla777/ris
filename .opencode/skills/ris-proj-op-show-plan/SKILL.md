---
name: ris-proj-op-show-plan
description: >-
  Show the complete compact unclosed plan of a selected RIS project or exact ID
  subtree, with real hierarchy, directed blockers and one evidence-based next
  action and existing feature candidates for the needed stage. Use for read-only
  status/selection; not graph planning, execution, acceptance or tracker changes.
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
Render one **continuous nested outline**: each epic is a section, its confirmed
features and other children sit directly under it, and each feature's tasks sit under
that feature. Use nested Markdown list items (`-`, then two more spaces per level)
instead of a flat list or raw whitespace indentation: a line indented four or more
spaces without a list marker renders as a code block, and a separate flat block of
features or tasks loses the real parent. Keep the whole epic block contiguous: every
child line immediately follows its parent item, with no intervening paragraph,
preamble sentence or second list elsewhere. Put shared notes and the legend after the
tree, never between a parent and its children. Standalone branches stay separate (no
artificial epic). Assign each epic a distinct colored emoji
marker from a small fixed palette for this overview (for example 🔵 🟢 🟠 🟣 🟡 🔴);
assign markers deterministically in stable epic-ID order, reusing a color only after
the palette is exhausted. The marker distinguishes epic sections only, never status,
priority or readiness. Use emoji rather than ANSI/color-only styling so the distinction
survives ordinary Markdown clients. Give each confirmed feature its own `🧩 ФИЧА`
list item nested inside its actual parent. Do not group task records as a feature
unless actual
feature kind and membership are established under the adapter's feature-reading
contract. Other children retain their actual hierarchy/type; never invent a feature
item to improve the layout.

For each record put a copyable exact `ID — title` in inline code and make its native
type and raw Beads status visually prominent. Localize type labels and explanatory
text, but do not translate IDs, titles or raw status values. Preserve priority (P0 is
highest), assignee, due date and other material fields under the rules below on the
record's own line. Put a shared native type on each affected row in compact form
(for example `· task ·`) instead of in an epic-wide preamble sentence. Keep closed records out of the tree: only unclosed work gets a list
item, including `open`, `in_progress`, native `blocked`, and any other observed
non-closed status with its raw value/diagnostic. Closed tasks and closed features get
no row at all, not even a prerequisite line; a closed ancestor required to explain real
hierarchy may appear only as compact `closed, context`. A closed prerequisite is not a
separate line: mention one inline on the dependent row only when it explains an
inactive edge, otherwise leave it to the container counter.

Use a compact localized form such as:

```text
- 🔵 **ЭПИК** · `ID — title` · **open** · P2 · дети: 1/24 closed
  - 🧩 **ФИЧА** · `ID — title` · **open** · P2 · задач: 2 · ▶ 1 · 🔒 1
    - ○ **ЗАДАЧА** · `ID — title` · **open** · P2
    - ▶ **ЗАДАЧА** · `ID — title` · **in_progress** · P2 · 🔒 waits `ID — title` [open]
  - ○ **ЗАДАЧА** · `ID — title` · **open** · P2

- 🟢 **ЭПИК** · `ID — title` · **open** · P2 · дети: 0/0 closed
```

- The list level is the only hierarchy signal: a feature is a child item of its epic,
  and each task is a child item of its feature or confirmed container. Never collect
  features or tasks into their own flat block, even when a parent has many children or
  all its children are closed; a parent with no unclosed children keeps only its own
  counters. Do not put a per-epic summary paragraph between the epic item and its
  children; keep its counters on its own line. Separate epic sections with a blank line
  between top-level items so each epic reads as one block. An unclosed task never
  appears in a separate global task list outside its parent branch; a missing or
  contradictory parent belongs to the diagnostic group below.
- Localize the sample labels. Use a distinct, consistent icon for raw statuses where
  useful (for example `○ open`, `▶ in_progress`, `🔒 blocked`), but always print the
  raw value. Status/type/priority are separate facts; icons and colors never replace
  them. A copyable inline-code identity is the exact native ID and title, not a
  fabricated shortened title.
- For each confirmed feature show a count of its unclosed direct native `task`
  children on the feature's own line, plus known `in_progress` and
  active/unresolved-blocker subtotals; closed task rows remain hidden. These
  subtotals may overlap (a task may be in progress and
  blocked), so label them rather than implying they add up. Validate the complete
  direct-child set and each task's typed blocker edges before giving exact counts; if
  incomplete, say `unknown/incomplete`. Do not turn an empty child list into proof of
  a one-task feature or accepted composition. For a separately confirmed one-task
  feature, count its open feature task as `1 (сама задача-фича)` rather than reporting
  misleadingly that the feature has no work. Epic/container `closed/all` counters
  continue to count complete direct children (including hidden closed children);
  state that these are status counts, not acceptance or criteria completion. Never
  use recursive totals.
- Show each active directed blocker on its blocked epic, feature or task as
  `waits <ID> [raw status]`; include the endpoint's short title when it is not already
  visible. Checked `closed` prerequisites are inactive and may be noted inline on the
  dependent row as inactive, never as a separate row. An unknown endpoint or blocker
  read is a visible unresolved blocker, not an empty edge set. Add a compact legend
  that `open` with no
  active Beads blocker means only “no active blocker recorded in Beads”; it does not
  establish that work is ready to start. Never label an item ready/available from
  status, priority, membership or absence of blockers alone.
- Always retain native type/RIS role, raw status and priority (P0 is highest); mark
  unknown required fields explicitly. Add assignee and due date when present and
  disclose material unknowns instead of implying none. `waits X` means this row
  depends on X, including cross-branch prerequisites.
- Cyclic, missing-parent or contradictory hierarchies get an explicit diagnostic
  group. Preserve all affected records there once rather than dropping them or
  inventing reparenting. For an exact-ID scope, external blockers get short contextual
  rows with ID, title and raw status, not independent trees; reuse endpoints already
  shown.
- Features show compact requirements/design evidence on their own line: reference
  present, acceptance unverified; acceptance checked against exact version and
  sufficient direct/inherited/mixed basis under common's `published-inputs.md`;
  original sources/derivation may establish inherited content without new human
  approval. Do not recommend reacceptance merely for an absent synthetic decision;
  missing/stale/ambiguous authority or a new material choice remains a gap.
  Other evidence states are checked absent or unknown. Include explicitly confirmed early root features without
  inventing an epic or JSON: show actual missing documents/decisions as unfinished
  preparation, not ordinary fallback. Apply common's document convention/bounded
  legacy discovery; missing/old/malformed JSON alone is no blocker. Known copy/identity/accepted-input gaps inform the
  continuation recommendation; no extra registry or acceptance audit for the tree.
  Brief omission cannot prove absence; a structurally
  valid feature record, file/link, closed children or no blockers cannot prove acceptance.
- Interpret stage only from sufficient facts and preserve raw status. `in_progress`
  means **in work according to Beads**, not a proven running flow. `needs design` or
  `needs acceptance` needs the relevant inspected inputs; otherwise mark stage unclear/
  unconfirmed. Ordinary tree evidence and deeper recommendation evidence stay distinct.

## Select exactly one candidate and apply continuation

For an epic's existing feature candidates read/apply this skill's owned
`references/feature-candidates.md`. A caller may reuse that bounded contribution
without a whole-plan tree. It selects existing records by needed-stage evidence,
not new product outcomes. Empty/gapped scope recommends graph planning only;
all-blocked diagnoses prerequisites. Show parallel candidates when available,
while retaining exactly one next action in this overview.

Choose within the requested working scope, not contextual ancestors/external blockers
outside it. Distinguish a container's **own next result** from unfinished work
already represented by its descendants; they are not independent peers merely
because both records are open. Containers are not unconditionally excluded.
For an exact-ID request retain that selected container/subtree scope and explain
any child-level need with its exact ID; never silently substitute a child subject.

1. First consider relevant started own unfinished work; foreign work needs coordination,
   never takeover. `in_progress` is a signal to inspect,
   not proof of an executing scenario. Among several, order by priority, then earlier
   creation time, with stable ID as final tie-break. Disclose unknown ordering fields;
   do not infer start from ID or updated time or claim a proven order when it matters.
2. Only if no relevant started own work requires continuation or diagnosis, before ranking a container against its descendants,
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
   consider a prerequisite before the work depending on it for the needed action;
   for otherwise equal **independent results** use earlier creation time then stable
   ID, not a parent and the same represented child work.
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
   result. A source-only command template or a technical skill name
   is not an installed command. Missing command blocks the slash form: say which is
   missing. An exact natural-language prompt is permissible only for an actually
   available compatible owner, with the slash gap explicit, never as an absent-owner
   workaround or invented authority. A bounded ordinary request may fit the same
   Fast owner via explicit `/risp-run-simple-task` or natural selection, subject to
   continuation's inspected contract; no new dispatcher or readiness assertion.
   Never impose full-task review/Git-only/delegated-ancestor obligations on an
   eligible Fast recommendation or downgrade feature/bug/container work to fit it.
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
