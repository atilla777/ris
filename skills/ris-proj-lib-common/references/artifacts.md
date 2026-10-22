# Artifacts and handoff

Use for substantive artifacts, execution transfer and partial/uncertain effects
under the main skill's triggers, not merely for every response.
The calling skill determines the content and destination of its result; do not
invent a universal roadmap, decision log, or project path.

Use actual sources, decisions, and evidence. Distinguish drafted, saved,
checked, and accepted: a successful write does not imply acceptance, and a
structure check does not establish semantic completeness. Before editing,
inspect the existing artifact, its purpose, and the authorized scope. Preserve
valid identifiers, links, agreed constraints, and unfinished work belonging to
another task. Do not silently replace a project document or storage protocol.

When writing is permitted, capture material accepted decisions in the
designated artifact as work progresses, then compare the result with those
decisions before handoff. Preserve quantities, order, exclusions, and negative
requirements without weakening them. A glossary or ADR does not substitute for
requirements in the next stage's actual input. Create such extra files only
when needed and authorized.

For unpublished documents, retain the current accepted content and its separate
actual decision, with an exact version and accessible input for the next stage.
Briefly record a material replacement: the superseded version/decision, what
changed and the new actual acceptance. Do not infer or manufacture acceptance.
No full archive of intermediate accepted snapshots, draft log, intermediate
publication or commit per acceptance is required; local drafts/commits remain
optional. Preserve published versions/decisions in Git history and their original
immutable references; copying a decision does not renew it or rebind
`containing-commit`. Recheck applicability of dependent accepted results when
inputs change; unchanged compatible content retains its original acceptance,
while materially changed content needs its own separate decision. Uncertainty
blocks only dependent work.

If writing is not allowed, provide the draft in the response and state that it
was not saved. If only some changes succeeded, identify saved and unsaved
parts; do not claim the downstream input is ready when it requires a saved
artifact. Respect the designated write mechanism and concurrency rules. On a
conflict, inspect current state and resolve it or report it; do not overwrite
someone else's work. Do not hold a storage lock while discussing decisions
with the user. After writing, check content and accessibility, resolving
relative links from the document's directory and paths in the recipient's
environment rather than assuming the sender's layout.

## Recoverable operation result

Use only `ok|blocked|conflict|error` for operation status: missing required input,
permission, dependency, decision or check is `blocked`; contradictory state or
concurrent change is `conflict`; technical execution failure is `error`. Partial
coverage/effects are facts, never a fifth status. `ok` means the explicitly
requested bounded operation succeeded and was checked. An expressly limited
proposal/save can be `ok` with downstream work remaining; never silently narrow
a full request to claim success or imply acceptance/publication from that `ok`.
An internal local-save/record-only boundary limits the child's contribution, not
the parent's authorized operation. Return it to the lead, who continues the
remaining route. Only the user's scoped request or an agreed scope change can
make that intermediate boundary the final requested result; a blocker preserves
the unfinished full scope instead of redefining it.

For an ordinary list, exact read or short recommendation, give the requested
outcome and material limits under common's baseline; no universal handoff is
required. Do not reconstruct versions, acceptance or channels unrelated to the
conclusion. A caller's more specific result obligations still apply.

For saved artifacts, substantive response-only candidates, execution transfer,
and partial/interrupted or uncertain effects (including read-only work when
being transferred), provide enough inspectable information to recover what exists.
Include the following where material to that result or its continuation:

- Full exact response-only proposal with a distinguishable version/scope, or
  exact result/evidence locator, or a checked discovery convention with all
  required keys and filename. State project/config/current-copy provenance and,
  for shared paths, context's checked Git-derived source-folder association.
- Material input and result versions, and separate acceptance decisions with
  their actual scope/version/address. A later copy of a decision does not renew
  acceptance; unchanged decisions remain bound to their original versions.
- Distinct prepared/saved/checked/accepted facts and publication state for each
  applicable channel (e.g. Git revision/ref/remote, local tracker write, exact
  completion, tracker publication/read-back). Mark unknown/unperformed effects
  honestly; one successful channel cannot prove another.
- Actual preserved effects and evidence, the factual stopping cause, limitations,
  unsaved parts and exact unfinished operation/remainder, separately from status.
  On retry inspect real effects and current applicability before repeating an
  action; neither a status token nor a stale success marker is proof. Reuse known
  IDs/commits/closure and verify uncertain remote effects before another write;
  pending read-back does not require repeating a confirmed push or close.

No universal schema, registry, draft store or mandatory next-skill prompt is
introduced. A nested operation returns its result to its caller; transitions
belong to the caller/workflow. Do not invent IDs, commands, refs or
`workspace.tasks/<ID>` for no-ID work. Use an authorized existing source/address
when available; otherwise return the unsaved result and exact discovery gap.
For a requirements/design candidate, the caller (the lead in a flow) conveys
the full exact text with its distinguishable version/scope, or a file accessible
to the recipient at an exact address/version, together with the separate
attributable acceptance decision when saving accepted content. Requirements and
design need independently identifiable accepted scopes. One attributable act and
decision address may cover both only when it explicitly identifies both complete
content selectors/versions and acceptance of each; generic approval of one never
accepts the other. Each receiving owner checks its own scope without re-asking
unchanged acceptance. The recipient reads and validates complete
content, version/scope and actual decision/provenance before dependent writes,
then compares saved content with that accepted candidate and decision. Incomplete,
inaccessible, ambiguous or changed candidates return to the caller; never infer
foreign-chat content or reformulate accepted meaning. Optional candidate files
need an authorized destination; no intermediate file or intermediate publication is required.
These explicit transfers concern intermediate unsaved/not-yet-discoverable results,
not a new session consuming a completed saved stage. For the latter apply common's
`published-inputs.md`: project plus exact ID/saved associations must discover the
content and decisions without a prior chat or receipt. Response-only content
requires explicit forwarding to a new session. Local
notes are usable only where accessible, never mandatory remote inputs for another
copy. A receiver re-resolves paths and checks actual content/version, fresh
permissions and, where required, ownership, blockers and write guarantees.
Neither a handoff, old lease/window nor existing worktree supplies those gates.

For execution handoff, convey the goal, scope, selected skill, project and configuration,
input artifacts and their acceptance state, material decisions and assumptions,
open questions, write permissions, actual changes, evidence, and expected next
result. Use the project's existing channel; do not rely on the recipient having
the chat history or automatically inheriting instructions. Report what was
prepared, saved, checked, and accepted without conflating these states.
