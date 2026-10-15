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

Before noninteractive save, require a verified candidate address and revision
(published Git commit/path/section, or an explicitly agreed local candidate
address/version), destination path/section, real separate acceptance decision,
authorized acceptor/provenance and exact permitted writes. Read the candidate
and decision, match approved content and resolve material gaps with the caller.
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
retain its original immutable decision/content reference. Before publication of
multiple accepted revisions, preserve each accepted content/decision snapshot
in Git history (or equivalent explicit immutable addresses), not only the latest.

## Save, check and gate tracker effects

1. Check exact file/evidence paths, rights, format and current state under the
   project's writer protocol. Reread existing files before update, preserve
   unrelated content and decisions, and return conflict on unexpected change or
   missing required concurrency protection. Ordinary Markdown uses project rules;
   only an actual selected OKF bundle requires the suitable installed OKF skill.
2. Save only the accepted content and actual authorized decision evidence. A
   bounded save does not rerun interview/formulation or ask the user. Read back
   and compare selected content with the accepted candidate and decision; check
   substantive coverage, format, links and preserved sections. Never put an
   unaccepted intermediate candidate at the accepted path.
3. For document-only this is a complete local result: return checked addresses,
   candidate revision, decision, effects and any pending immutable refs. No task
   ID, epic or tracker capability is needed. Local addresses are explicitly local,
   not mandatory remote inputs for another session.
4. For combined mode require actual published content/decision before tracker
   create/update. Check both via fetched selected-remote evidence and read actual
   content at full Git revision, semantic section and separate pinned decision.
   Resolve containing-commit and match decision path/section/revision to the ref.
   Tracker stores the full published commit, never containing-commit. The wrapper
   does not publish Git; a direct caller with local-only inputs receives saved
   partial state and precise publication/re-entry prerequisites. With published
   accepted inputs and rights, direct invocation completes doc+feature task.

On error/ambiguous write, inspect actual file and any attempted tracker effects
before retry. Return known addresses/IDs/revisions, verified effects and exact
recovery (publish checked content/decision, resolve immutable refs, then reconcile
adapter create/update). Git and tracker publication are separate facts; neither
local read-back nor one published channel means full remote success. Reuse
unchanged acceptance after checking content/applicability; materially changed
requirements return to their acceptance owner. Do not rollback, blind-retry or
maintain displaced decision history in the tracker.
