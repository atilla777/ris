# Intent and neighboring results

Read only the section relevant to the question, plus the named cards. These are
capability explanations, not prescribed stages or confirmed task readiness.

## Product foundation, before feature-level questions

"Prepare this project to use RIS" is `/risp-init <project and scope>` after package
installation, not a product-foundation-only call or automatic roadmap. Init owns
agreed settings/bootstrap and combined local readiness; product → architecture →
engineering content stays with existing authors and separate acceptance. Reuse
existing material; specific tool/Git/Beads/agent effects need their own permissions.
This includes project-owned Standard/Advanced, user-agreed pinned models from the
current available catalog and role bindings, not global-only/model-inherited tiers
or silent model upgrades. Suitable saved choices need no repeated questionnaire.
Roles select executors when delegating, not mandatory delegation of every internal
step: the lead may do authorized work directly. A delegated operation uses its
configured role and checks actual launch; an unavailable role blocks that route,
without silent substitution. Required independent review actually launches apart
from all authors/repairers. Bindings alone prove neither model, invocation,
independence nor Advanced implementation; changes need agreement.
Deferred choices limit dependent operations; publication is offered separately,
and absent remote does not alone block checked local setup. Init does not configure
product build/test/format/CI or start development. Help explains, never launches it.

"Help me describe what this product is for and who needs it" is product-foundation
work, not automatically a roadmap, individual feature specification or full design.
`product-proposal*` means direct `ris-port-op-formulate-product-foundation`: research
supplied materials and known answers, conditionally interview only material
interdependent gaps, return a sourced read-only proposal. `product-author*` means
direct `ris-proj-op-author-product-foundation`: selected-project context, the same
content method, separate acceptance of complete content, then bounded OKF save and
read-back in sources.product. Neither has a slash facade or initializes a project,
chooses stack/architecture, plans a roadmap, publishes or starts development.

For "write my initial product knowledge", clarify proposal-only versus accepted
project save if that effect is ambiguous; do not infer acceptance from the request
or material presence. Update needs existing content and a defined boundary, not
silent create. Sufficient existing accepted knowledge can be reused; no mandatory
new foundation file, full future design or extra SDLC stage is introduced. Deferred
choices retain their specific impact and do not certify downstream readiness.
Example proposal: `Load ris-port-op-formulate-product-foundation with <materials>,
product <subject>, create proposal only`. Example saved result: `Load
ris-proj-op-author-product-foundation for <project>, bounded update <scope>;
obtain separate content acceptance, then save/check within <authorized scope>`.

## Feature and task

- For an **already explicitly chosen** feature needing early tracking, use
  `/risp-specify-feature`: explicitly limited early registration, title/goal and
  stable project key, optional epic, no spec/design/acceptance required. It returns
  one ordinary task ID, not execution readiness. Then the
  existing task-copy owner can prepare that ID with purpose `feature-preparation`
  before documents. New documents use `sources.specs/<full feature ID>/spec.md`
  with readable H1, Feature-ID/Summary/optional Keywords, sufficient inline or
  adjacent design and actual separate acceptance. No JSON/pin/readiness registry.
  Status/next expose actual copy/input/blocker gaps; legacy schema alone never
  blocks the new route and old data is not migrated. The full prepare-flow composes these same owners below;
  a direct limited registration call does not start that flow.

- "I want to add authorization": if this is a new feature needing decisions,
  explain `/risp-prepare-feature <ID or epic/context>`: early-register the chosen
  result, prepare its one safe ID-associated copy, work out requirements/design
  in one dialogue, precisely accept both scopes (one act may cover both), review/
  publish inputs, update the same ID and verify decomposition/tracker publication.
  `/risp-decompose-feature <ID>` remains useful independently or on resume when
  accepted published inputs already exist; it is not mandatory after prepare.
  If it might instead be an already assigned clear fix, clarify that distinction,
  or conditionally mention `/risp-run-simple-task <bounded request>`; do not
  demand the full SDLC for every simple change.
- `prepare-feature` vs `specify-feature`: the former owns the combined preparation
  route through independently accepted requirements/design and published verified
  one-task or multi-task decomposition; the latter
  owns requirements and their permitted document/record effects, not design or
  decomposition. Their atomic stages are alternatives to manually orchestrating
  preparation, not mandatory extra calls after the scenario.
- `select-feature` chooses a small outcome within an epic; `refine-epic` clarifies
  an unclear epic; `roadmap` proposes/records goal-level epics. None implements.
- `interview-feature` elicits requirements without saving; portable
  `formulate-feature-spec` makes a proposal from known decisions; project
  `specify-feature` owns actual acceptance/save/publication within authority.
- `design-feature` owns technical choices from accepted behavior, with separate
  acceptance; `decompose-feature` determines one-task sufficiency or child tasks.
  Implementation determines its approach from sufficient accepted inputs/current
  code, without a standalone planner, saved plan or implementation report.
  For new/materially changed design, both the design owner and prepare-feature
  explain essence/flow, reused/new technologies and why, tradeoffs, material risks
  and hard-to-reverse choices in plain language before asking acceptance. Roughly
  one screen is a readability guideline, not a fixed help-layout limit.
  Acceptance is of the complete identified accessible candidate, not merely its
  summary. Optional explicitly authorized full Markdown draft storage can precede
  approval; it is not accepted-content save/publication or a mandatory draft store.
- `run-task` owns the complete one-task cycle, including prepared copy/claim,
  implementation/checks from sufficient accepted inputs, independent review, Git, separate
  completion and tracker publication. An explicit ID is the sole target; no ID
  reconciles own unfinished work before ready-task selection. A multi-task
  container is not executed as one leaf.
- `run-simple-task` executes a clear already assigned request, optional ID, not
  queue selection. No mandatory interview/spec/design/decomposition/plan or report
  files by default; actual project rules and required TDD remain. RIS itself
  requires short Beads accounting. Own branch, real independent review, verified
  direct Git publication and separate tracker effects remain. Existing feature/
  bug IDs retain their contracts; fast is no escape from required preparation.
- `implement-task-tdd` stops at checked code/tests/authorized docs, not independent
  approval or publication. `review-task` returns findings, does not repair or
  publish. `publish-task` requires independently reviewed whole-snapshot inputs
  and stops at verified Git, not task closure, tracker push or parent acceptance.

## Bug

"There is a bug" is materially ambiguous: record the message, investigate an ID,
or fix a researched bug? Ask only that distinction if the request does not settle
it. Do not diagnose through help or launch the suggested owner.

Registration records an **unconfirmed** message/verified ID and stops.
Investigation checks expectations, code and evidence, saves aligned report/criteria
with one assigned investigator, write authority and bounded fresh-compare/native
sandbox-write/read-back, preserving original/foreign sections. This is sufficient
organizational control, not CAS or exclusion of all parallel writers; a CAS
provider is not mandatory for ordinary saving. Missing authority/capability or
observed conflict can block persistence without blocking useful research. Saving
does not establish fix readiness: aligned sufficient inputs are checked separately.
Proved-correct/duplicate disposition is not fixing. Fix-bug needs an
exact native bug and sufficient saved basis, separate acceptance of material design
if needed, and a recoverable historical input snapshot before reusing the whole
run-task engine. It does not silently register or investigate anew. All three
bug owners are direct-load, not invented slash commands.

## Continuation, status and help

"How do I use RIS?" belongs here. "What should I do next with ID?" belongs to
`/risp-next <ID>`, which inspects selected work read-only and recommends a prompt,
decision or blocker. "Show the project's plan" belongs to `/risp-status [ID]`,
which shows real hierarchy/blockers and one recommendation. Help explains those
inputs but never reads their tracker set or certifies readiness on their behalf.
Recommendation, readiness, acceptance and permission remain distinct.

These answer different questions: status chooses one project/specified-subtree
next action, next continues the selected ID, and no-ID `/risp-run-task` selects
work for the current actor. Status first considers started unfinished work in
its scope, including a foreign assignee; `in_progress` is not proof of a running
flow. A foreign-work recommendation calls for coordination, never takeover.
No-ID run-task first reconciles confirmed own unfinished execution, then selects
a ready task only if none exists. Blocked selected own work stops that flow,
not a switch to fresh work. Different recommendations are therefore expected;
status is read-only navigation, not an execution-readiness gate. With an explicit
ID, run-task keeps that target. Next retains the selected container's scope;
run-task does not replace a container with a child or execute a multi-task
container as a leaf. Container verification/completion is a separate intent.

## Container, verification and publication

Leaf Git publication, exact leaf completion and tracker publication are separate
effects. Completing a child never accepts/closes its parent. An explicit ordinary
parent close checks a nonempty complete set of direct children (all closed) and
parent blockers; no recursive delivery/acceptance reconstruction. A question about
closure eligibility makes only those reads, without writing. Zero-child features
retain own-result verification. Ask
`/risp-complete-container verify <ID>` for read-only fulfillment; explicit
administrative close changes status, not acceptance, without delivery reconstruction;
explicit verify-and-close requires successful full current verification and
authorized closure, with no mandatory saved assessment. No automatic recursive closure. Portable `verify-feature`
assesses integrated criteria on a revision, not a diff or tracker closure.

## Other operations and portable counterparts

Portable methods take supplied evidence and return proposals/checked results,
without RIS config/tracker. Project counterparts add applicable accepted-content,
path, rules and authorized persistence responsibilities, not universal mandatory
infrastructure. Use autonomous skill authoring (`/risb-skill`) even inside a RIS
project when the skill does not integrate with RIS; integrated authoring is direct.
Neither author installs its output. Installation manages the whole RIS package,
not project initialization. OKF operations require an explicitly selected bundle;
ordinary Markdown is not automatically OKF. Rule authors propose or accept/save
norms, not audits, tooling installation or CI configuration. Retrospective returns
evidence-based causes/improvements, not code repairs or multi-session analytics.
