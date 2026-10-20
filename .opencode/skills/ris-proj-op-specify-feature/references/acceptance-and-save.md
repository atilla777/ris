# Requirements acceptance and bounded save

Read before selecting accepted content, acceptance or persistence. This wrapper
owns the requirements result; the adapter owns tracker encoding and operations.

## Identify content and its separate decision

Use project-relative `path` and `section: null` for a whole file or an unambiguous
semantic section, such as `Requirements / Failure behavior`. Requirements and
design must be independently identifiable without ambiguous/overlapping
selectors. Prefer separate spec.md/design.md where useful; retain safe existing
sections instead of relocating them for uniformity. Appending design to an
accepted whole requirements file changes that content: use a separate design
file instead. No mandatory Markdown heading/EOF digest protocol is introduced.

Before noninteractive save, the caller supplies either the full exact candidate
text with a distinguishable version and scope, or a recipient-accessible file at
an exact address/version (published Git commit/path/section or explicitly agreed
local address/version). Both forms require destination path/section, real separate
requirements acceptance decision, authorized acceptor/provenance and exact permitted
writes. Read the complete candidate and decision yourself; validate version/scope
and that the actual decision approves this content, without assuming foreign-chat
access. Return incomplete, inaccessible, ambiguous or changed candidates to the
caller before dependent writes; do not invent answers or reformulate accepted meaning.
Full text needs no intermediate file, mandatory hash, registry or intermediate publication.
Optional candidate storage requires its own authorized destination; portable
authors remain read-only.
Optional local fingerprints can detect candidate changes; they are not tracker
refs or a required scoped hashing scheme. An absent or changed candidate is
blocked/conflict, not permission to invent its acceptance or revision.

Record the actual authorized requirements decision in a permitted Git document
or decision section; no mandatory acceptance file/manifest. It names accepted
content path, section (including null), revision and `decision: accepted`, with
acceptor provenance. Each result has its own decision. A published decision
address pins repository, full decision commit, path and any unique decision
section. A branch URL, local note, file presence or commit alone is insufficient.
If content and decision will share a commit, the decision may name content
revision `containing-commit`; resolve it from the immutable decision address
after publication. Otherwise name the actual full content commit. Do not invent
a future SHA or immutable URL. Local accepted content/evidence may be saved
before publication with immutable refs explicitly pending; record the checked
local candidate identity so publication can match it to the accepted result.
Never rebind a copied `containing-commit` decision to a later changed document:
retain its original immutable decision/content reference. For unpublished
revisions, keep the current accepted content and its separate actual decision
accessible to the next stage. For a material replacement, briefly identify the
superseded version/decision, what changed and the new actual acceptance; do not
invent a decision while saving. A full archive of intermediate accepted
snapshots, draft log, intermediate publication or commit per acceptance is not
required; voluntary local drafts/commits are allowed. Preserve already published
versions, decisions and their pinned references in Git history.
When requirements change, require a design-owner applicability check for any
dependent design. Compatible unchanged design retains its original acceptance;
materially changed design needs its own separate acceptance. Uncertainty blocks
the dependent action, not independently authorized work.

## Save, check and gate tracker effects

For full mode preflight the existing Git publisher and, when records are part
of the result, adapter publication before dependent writes: exact subject,
destinations, authority, whole outgoing scope and required guarantees. Missing
publication prerequisites block the full claim, while independently authorized
local saving may proceed with preserved effects. Full mode returns the stopping
cause's `blocked|conflict|error`, plus completed channels and exact remainder;
only an expressly limited successful local save can be `ok` at that boundary.
Never infer authority from nesting.

Record-only reconciliation discovers already published accepted content/decisions
and applicable independent review/publication evidence from saved associations
(or a supplied checked result within an unfinished flow), skipping formulation, renewed
acceptance and file saving. Enter step 5 with verified inputs; perform no push
in this explicitly limited mode. No particular receipt file or previous chat is
required; missing actual evidence remains a precise dependent gap, never invented.
Return its local record result and remainder.

1. Check exact file/evidence paths, rights, format and current state under the
   project's writer protocol. Reread existing files before update, preserve
   unrelated content and decisions, and return conflict on unexpected change or
   missing required concurrency protection. Ordinary Markdown uses project rules;
   only an actual selected OKF bundle requires the suitable installed OKF skill.
2. Save only the accepted content and actual authorized decision evidence. A
   bounded save does not rerun interview/formulation or ask the user. Read back
   and compare selected content with the exact accepted candidate and separate
   requirements decision, for either supplied form; check
   substantive coverage, format, links and preserved sections. Never put an
   unaccepted intermediate candidate at the accepted path.
3. For an explicitly limited local save this is its complete contribution: return checked addresses,
   candidate revision, decision, effects and any pending immutable refs. No task
   ID, epic or tracker capability is needed. Local addresses are explicitly local,
   not mandatory remote inputs for another session.
4. In full mode, after saving apply independent `ris-proj-op-review-task` for
   the project document subject, with or without an ID; it composes portable
   assessment and saves the full local YAML under its references/report-format.md.
   Pass publication-gate purpose and an explicit authorized report path before ID;
   do not invent a task folder.
   Consume its address/round through validity and external applicability checks,
   not a copied verdict or old approval bypassing later adverse/unknown rounds.
   Supply exact whole candidate snapshot (base/overlay/add/delete/modes), content,
   decisions, rules and substantive checks. The reviewer must be independent of
   all authors/repair authors; self-review does not grant approval. Return
   high/medium findings to their content owner, repair/check and obtain fresh
   independent assessment of the actual snapshot. Then invoke
   `ris-proj-op-publish-task` with the checked document/change subject, separate
   decisions, checks, review/provenance, destination evidence and allowed effects.
   Inspect its commit/tree/ref/remote receipt and independent remote evidence;
   match published selected content to the accepted candidate and decisions.
   Inspect the publisher's primary-sync evidence too: full mode requires its
   full result, unless this operation was explicitly bounded to remote-only Git
   publication. Confirmed remote with pending local sync remains a preserved
   partial effect; do not replay push or silently waive the full-result gate.
   Integration drift requires applicable independent reassessment, not self-approval.
   Requirements-only needs no future design, implementation evidence or task ID.
   Already published matching content reuses verified publication without empty
   commit/push. A limited record-only call instead consumes an applicable existing
   Git receipt; a limited local save stops before review/publication.
5. For combined mode require actual published content/decision before tracker
   create/update. Check both via fetched selected-remote evidence and read actual
   content at full Git revision, semantic section and separate pinned decision.
   Resolve containing-commit and match decision path/section/revision to the ref.
   Tracker stores the full published commit, never containing-commit. The wrapper
   invokes the existing Git owner in full mode, never copies its algorithm.
   Failed Git blocks dependent record writes. With published accepted inputs,
   reconcile the selected feature or ordinary standalone record and then invoke
   adapter publication in full mode. Inspect its required revision/fresh remote
   reachability receipt alongside locally verified IDs/refs before combined
   success; remote revision assurance does not independently compare all fields.
   Limited record-only stops at its
   verified local effect with tracker publication explicitly remaining.

On error/ambiguous write, inspect actual file and any attempted tracker effects
before retry. Return `blocked|conflict|error` according to the actual stopping
cause, known addresses/IDs/revisions, verified effects and exact
recovery (publish checked content/decision, resolve immutable refs, then reconcile
adapter create/update). Git and tracker publication are separate facts; neither
local read-back nor one published channel means full remote success. Reuse
unchanged acceptance after checking content/applicability; materially changed
requirements return to their acceptance owner. Do not rollback, blind-retry or
maintain displaced decision history in the tracker.
