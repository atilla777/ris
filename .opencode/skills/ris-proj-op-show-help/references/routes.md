# Intent and neighboring results

Read only the section relevant to the question, plus the named cards. These are
capability explanations, not prescribed stages or confirmed task readiness.

## Feature and task

- "I want to add authorization": if this is a new feature needing decisions,
  explain `/risp-prepare-feature <epic/context>`: select a bounded result, accept
  requirements and design separately, publish inputs and feature ID. Decomposition
  is outside that scenario: `/risp-decompose-feature <ID>` is a separate request.
  If it might instead be an already assigned clear fix, clarify that distinction,
  or conditionally mention `/risp-run-simple-task <bounded request>`; do not
  demand the full SDLC for every simple change.
- `prepare-feature` vs `specify-feature`: the former owns the combined preparation
  route through separately accepted design and published feature ID; the latter
  owns requirements and their permitted document/record effects, not design or
  decomposition. Their atomic stages are alternatives to manually orchestrating
  preparation, not mandatory extra calls after the scenario.
- `select-feature` chooses a small outcome within an epic; `refine-epic` clarifies
  an unclear epic; `roadmap` proposes/records goal-level epics. None implements.
- `interview-feature` elicits requirements without saving; portable
  `formulate-feature-spec` makes a proposal from known decisions; project
  `specify-feature` owns actual acceptance/save/publication within authority.
- `design-feature` owns technical choices from accepted behavior, with separate
  acceptance; `decompose-feature` determines one-task sufficiency or child tasks;
  `plan-task` plans implementation of one confirmed task in its supplied copy.
- `run-task` owns the complete one-task cycle, including prepared copy/claim,
  plan when required, implementation/checks, independent review, Git, separate
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
when permitted and protected; it separates confirmation from fix readiness.
Unsupported content protection can block a report write without blocking useful
research. Proved-correct/duplicate disposition is not fixing. Fix-bug needs an
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

## Container, verification and publication

Leaf Git publication, exact leaf completion and tracker publication are separate
effects. Completing a child never accepts/closes its parent. Ask
`/risp-complete-container verify <ID>` for read-only fulfillment; explicit
administrative close changes status, not acceptance, without delivery reconstruction;
verify-and-close requires successful full current verification and separate
authorized save/closure. No automatic recursive closure. Portable `verify-feature`
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
