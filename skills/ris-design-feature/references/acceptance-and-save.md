# Scoped acceptance and persistence

Read before selecting a design scope, accepting or saving a project design.
The wrapper owns sufficient design and decisions; the adapter owns its record
encoding and conditional operations. Do not use a second feature registry.

## Independent versions

Use the selected adapter's supported scoped-version contract. With
`tasks.feature-record/1`, requirements and design each have `path`, `scope`,
SHA-256 and acceptance (accessible address, approved scope/version, decision).
Paths resolve from the target project root. A separate `design.md` can use
`whole-file`; place its acceptance evidence outside hashed content. In shared
`spec.md`, use `heading:<exact Markdown heading line>`: it must occur exactly
once. Hash raw UTF-8 bytes starting at that heading line, including its newline,
up to the byte before the next same-or-higher-level heading, or EOF. Nested
headings remain part of the scope. No whitespace/newline normalization. The
requirements/design scopes cannot overlap, and evidence containing the digest
must live outside that scope (e.g. sibling acceptance heading or project decision
store). Check old requirements bytes and acceptance before and after adding or
revising design; an unchanged digest retains its decision.

If old requirements are `whole-file`, adding design there changes their accepted
version: prefer separate `design.md`. Changing the requirements scope, ambiguous
headings or overlapping areas is not a purely technical bookkeeping operation;
use separate files or obtain acceptance of the affected scope/version. Never
assert that the old decision approves different bytes. Existing project designs
with safely hashable regions need not move into a new file for uniformity.

Show the actual candidate content, scope/digest and material impact to the
authorized acceptance mechanism. Record its real decision in the project's
permitted accessible channel; no mandatory acceptance file/manifest is introduced.
No missing decision is invented from a historical chat or future tracker ID.
Check that the address resolves for another session and approves the same
scope/digest. A simple design may explicitly confirm existing contracts and the
minimal approach, but still needs its independent decision and verifiable scope.

## Preflight, save, update, verify

1. Before writing, check exact paths, permitted file protocol, current content
   and separately authorized record update. Preflight the capability, expected
   old block, preservation of unrelated prose/slug/spec/requirements/history,
   and its concurrency guarantee. For Beads this is an independently established
   exclusive writer window across all actors touching the feature, children,
   blockers and evidence through read-back. Claim/lease/local lock/status guard
   or read/write/read is insufficient. Obtain decisions outside the window;
   establish/renew the actual short write window afterwards, naming provider,
   scope and duration. Without it return `conflict` before dependent writes.
   A separately authorized document-only proposal is a narrower result, not
   the combined accepted-record result. Check required blocker operations and
   agreement before promising their effects; never bypass an unsupported scope.
2. Reread expected files and record/children/blockers immediately before writing;
   unexpected changes stop the write. Save only accepted content/evidence under
   the prescribed file protocol, preserving requirements and unrelated sections.
   No unaccepted draft is placed at the accepted path. Read bytes back, compute
   scoped hashes and resolve links/decision evidence against accepted versions.
3. Invoke `tasks.features.update` with confirmed ID, expected prior record and
   exact new design path/scope/digest/acceptance. Preserve immutable slug/spec,
   requirements decision and unrelated fields/text. Append displaced design and
   its acceptance to history. On substantive design revision, prior verification
   is no longer proof of this version: preserve it in history and invalidate the
   current verification under the approved update rather than silently reusing
   its verdict. Do not call record-verification or complete here. If agreed
   blocker writes are part of the permitted design result, execute through the
   supported adapter, check endpoints/direction/cycles and reread them; proposed
   but unsaved blockers remain explicit handoff limitations.
4. Read the full feature-record back with exact task/epic/slug/spec, both scopes,
   versions, decision addresses, history, preserved prose and changed blockers.
   Rehash saved files, verify the design decision and unchanged requirements
   evidence; match everything to the intended effect before `ok`. For an exact
   repeated invocation verify matching design bytes/decision/record and return
   unchanged, not a new acceptance or duplicate history entry.

If file or tracker writing is nonzero/ambiguous or partial, reread actual state
before any retry. Return confirmed paths/IDs/versions and effects with
`blocked|conflict|error`; stop further writes rather than rollback, blind retry,
or claim consistency from a command's exit code. A saved new design with an old
record is partial, not ready. A later recipient reconciles that state under
fresh authority and guarantees. Git and tracker remote availability remain
separate checks owned by the calling publication workflow; local read-back is
not evidence of either remote channel.
