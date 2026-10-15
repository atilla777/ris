# History, episodes and causes

Read before analysis. Use existing source representations and authorized read
tools; this method does not require a collector, scripts or a database.

## Overview and coverage

Record session/purpose and changed requests, source versions and snapshot/cutoff,
stopping status, proven participant links and per-participant available ranges.
Unknown stopping status means a snapshot report, not a completed-session claim.
Maintain a compact ledger: source/participant, range, substantively overviewed,
continuation, omission/unavailable reason. Read the content of every available
page before investigating selected episode detail. A metadata index, summary or
search match does not establish substantive coverage of the rest of the history.
For split events track each range and read its continuations. Preserve findings
from first, middle and last ranges rather than letting recent events dominate.

Reconstruct request → decisions → skills/tools → handoffs → checks → result.
Follow only proven branch links; mark missing children and uncertain ancestry.
Compaction summaries and pruned output do not restore the lost original.
Distinguish a snapshot captured at cutoff from a later export filtered to a
historical boundary. For an event crossing cutoff, do not import its later
result. Undated mutable fields, usage or participant links in a later source do
not prove their historical state: retain them as later evidence with a gap,
outside exact historical totals/conclusions unless temporal membership is proven.

When the history exceeds available resources, work sequentially in bounded
chunks and preserve the ledger and episode register. Identify what remains
unseen and limit the result to an intermediate/partial analysis. Do not silently
skip pages or claim final absence of findings. Missing data limits dependent
conclusions, not the useful independent analysis.

## Signal and bypass register

Keep an addressable episode register, with signal, evidence needed and disposition:
investigated, justified, confirmed problem, or unknown because of a named gap.
Every observed one-off Python/Bash/other script, direct SQL, hand-assembled
adapter operation and internal-storage/interface bypass must appear. For each
establish need, then-available alternative, discoverability, observed costs,
potential risks and cause alternatives. A script is not itself a defect:

- Necessary one-off data processing can be justified.
- A missing/insufficient public operation points to its tool/adapter owner.
- An existing operation that could not reasonably be found points to navigation,
  selection description or examples, not a duplicate implementation.
- Ignoring an available, discoverable operation is a distinct method/usage issue.

Do not replay an episode to investigate it. The register must account for every
observed bypass, including gap-limited ones, not just those judged problematic.

Investigate these other signal families independently of token/time thresholds:

| Family | Questions to test against events |
|---|---|
| Errors/recovery | Wrong commands, arguments or API? Ignored failure? Identical retry without changed approach? Repeat of an already successful action? Was recovery bounded and effective? |
| Context/information | Repeated reads, unnecessary dependencies/output, lost decisions after compaction, expensive restoration? Load metrics resource when measurements or gaps matter. |
| Progress/time | Stalled loops, duplicate investigation, unnecessary approval or serial work, wrong skill selection? Distinguish waits from avoidable work. |
| Handoffs/delegation | Lost constraint/input, duplicate work, unverified child report, missing required independent review? Verify actual source evidence rather than accepting “done”. |
| Delivery stages | Missing required checks, claimed TDD without observed RED, inapplicable checks, unjustified review cycles, confusion between publication and tracker completion? |
| Outcome reliability | Success/push/completion without evidence, unmet criteria, final answer contradicted by actions? |
| Instructions/project | Conflicting or impossible requirements, harmful literal obedience, excess load, missing navigation, stale fact or broken check manifested in this session? |

The catalog is a discovery aid, not an automatic finding generator or a closed
list. A recoverable error or reload can be justified; investigate its actual cost.

## Evidence and causal restraint

For each material episode cite what happened, observed consequences, actually
received instructions, then-available tools and how they could be discovered.
Separate historical file existence/version from proven receipt: a recorded
skill/read output proves receipt; a file at a commit alone does not. Unrecorded
system instructions/tool schemas remain unknown. Current files cannot fill that
historical gap or create a retroactive violation.

Explain candidate mechanisms and competing explanations. Correlation, sequence
and plausible reconstruction do not prove cause. A single episode supports a
local finding, not multi-session recurrence. Keep confidence in the problem
independent from confidence in its cause; state what evidence would distinguish
alternatives. Do not invent a loss from a possible risk.

Compare outcome claims only with the criteria required then. A claimed successful
push without a receipt is unverified, not proven failed. An explicit failed push
plus a contrary final claim demonstrates failure/contradiction for that attempt;
do not infer there was no later recovery outside coverage. Read only targeted
supplied artifacts when reconciling contradictions: no full code review, test,
build, push, tracker query or reproduction to manufacture new historical evidence.

For each confirmed defect inspect its targeted current counterpart if supplied
and allowed. Mark persists / eliminated / unknown with source revision and basis.
A historical defect fixed now remains a historical finding; do not recommend
reimplementing an existing fix. Missing current material means unknown, not persists.
An unchanged available alternative is not evidence that the agent's selection
defect persists: distinguish the current tool/document fact from current workflow
behavior. Without a defective current counterpart or observed recurrence, mark
that behavior's current applicability unknown.

## Minimal improvement

Merge duplicates by underlying episode/cause without conflating unrelated causes.
For a justified proposal specify episode refs, concrete owner and minimal change:
navigation/example for discoverability; tool/adapter for missing operation;
mechanical check for mechanically detectable error; skill/handoff method for lost
decisions or boundaries; project docs for stale facts; combine/shorten/delete
redundant or harmful rules. Assess the requirements themselves, not only obedience.

Explain counterfactually how the change would alter the observed episode, what
test or observable comparison would demonstrate improvement, and its context,
extra-action and maintenance costs. Do not add a rule by default or fix anything.
