# Artifacts and handoff

Use before preparing or changing a deliverable and before handing work off.
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

Every result, including read-only, no-ID, partial and interrupted work, must
identify the actual outcome/subject and provide enough inspectable information
for its consumer to recover what exists:

- Exact result/evidence locator, or a checked discovery convention with all
  required keys and filename. State project/config/current-copy provenance and,
  for shared paths, checked primary selection source and association evidence.
- Material input and result versions, and separate acceptance decisions with
  their actual scope/version/address. A later copy of a decision does not renew
  acceptance; unchanged decisions remain bound to their original versions.
- Distinct prepared/saved/checked/accepted facts and publication state for each
  applicable channel (e.g. Git revision/ref/remote, local tracker write, exact
  completion, tracker publication/read-back). Mark unknown/unperformed effects
  honestly; one successful channel cannot prove another.
- Actual preserved effects, limitations, unsaved parts and exact unfinished
  remainder. On retry inspect real effects and current applicability before
  repeating an action; a stale success marker is not proof.

No universal schema, registry, draft store or mandatory next-skill prompt is
introduced. A nested operation returns its result to its caller; transitions
belong to the caller/workflow. Do not invent IDs, commands, refs or
`workspace.tasks/<ID>` for no-ID work. Use an authorized existing source/address
when available; otherwise return the unsaved result and exact discovery gap.
Response-only content is not automatically accessible to a new session. Local
notes are usable only where accessible, never mandatory remote inputs for another
copy. A receiver re-resolves paths and checks actual content/version, fresh
permissions and, where required, ownership, blockers and write guarantees.
Neither a handoff, old lease/window nor existing worktree supplies those gates.

For handoff, convey the goal, scope, selected skill, project and configuration,
input artifacts and their acceptance state, material decisions and assumptions,
open questions, write permissions, actual changes, evidence, and expected next
result. Use the project's existing channel; do not rely on the recipient having
the chat history or automatically inheriting instructions. Report what was
prepared, saved, checked, and accepted without conflating these states.
