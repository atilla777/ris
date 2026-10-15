# Local OpenCode reader

Read from the installed wrapper before collection/interpretation. This resource
owns mechanics; the portable base owns retrospective reasoning. Baseline is
OpenCode **1.18.33**, Python 3 standard library. Unknown semantic versions preserve
content but give unknown request metrics. No dependency install is needed.

## Invocation and permissions

Resolve `scripts/opencode_read.py` from the folder containing this resource's
parent `SKILL.md`. Run `python3 -B <installed-reader> <operation> --project <root>`.
Operations: `list`, `overview`, `pages`, `detail`, `metrics`. Output is JSON;
`status: error` exits 2, `partial` returns useful evidence plus gaps, `ok` describes
only the returned mechanics, not completed analysis or acceptance.

Every raw JSON boundary (export, GET, list and continuation) rejects duplicate
object keys before normalization, including conflicting identity/usage fields.
Input is UTF-8; JSON and in-memory normalization/redaction have a 128-container
nesting cap. Brackets inside quoted strings do not count. Parser/serializer/
redaction recursion exhaustion produces a secret-safe `status: error`, exit 2,
not a traceback. An invalid/deep optional child or unavailable child GET leaves
independent valid root evidence usable with an explicit gap. The cap also applies
to normalization envelopes; it is a resource bound, not unlimited JSON support.

For example (substitute the actual authorized paths):

```text
python3 -B <reader> overview --project <root> --export <supplied-export>
python3 -B <reader> pages --project <root> --export <supplied-export> --budget 8192
python3 -B <reader> pages --project <root> --export <supplied-export> --cursor '<returned next JSON>'
python3 -B <reader> metrics --project <root> --export <supplied-export> --version 1.18.33
python3 -B <reader> detail --project <root> --export <supplied-export> --ref ses_ID/msg_ID/prt_ID
```

`--export -` reads stdin. Repeated `--child-export <path>` supplies branches.
`--session` asserts exact identity; `--participant` selects a **confirmed** branch
for pages/detail. `--version` is an explicitly established semantic version,
never a convenient guess. `--cutoff` is Unix milliseconds. Only use
`--captured-boundary` with independent evidence that the supplied snapshot was
captured then; an export obtained later does not qualify.

With no supplied export, `--session <exact-ID> --allow-cli` permits fixed
`opencode --pure --version` and `opencode --pure export <ID>`, cwd=selected project,
shell=False. `list --allow-cli` runs `opencode --pure session list --format json
--max-count 5` and returns selection-required, never a selected session. CLI
permission is supplied by the retrospective request unless the caller or project
restricts CLI use. Pass `--allow-cli` for these fixed reads; it acknowledges
permission, not independently verified initialized storage or a fitness witness.
Do not inspect SQLite, enumerate service paths or request an export solely to
prove readiness. Prefer a supplied export when one is already provided.

Ordinary OpenCode metadata, DB/WAL/checkpoint housekeeping and own logs outside
the developed project are accepted service effects. Message/part content and
semantic history links, project files/config/docs/Git, task state/edges and
telemetry stay protected. This is not permission for arbitrary outside-project
writes, plugins or analyst storage edits. A known service path inside the
developed project or another concrete out-of-scope effect blocks CLI use; an
absent service-path inventory alone does not.

Stop CLI acquisition on a bootstrap/migration indication, request for setup,
unsupported version, reader/CLI error (including timeout/invalid JSON), identity
mismatch or known prohibited effect. Do not confirm prompts, initialize, upgrade,
repair or retry around the failure. Offer a supplied export or permitted existing
GET instead. The reader checks version/fixed argv and suppresses raw stderr;
its generic error is already sufficient to stop, not a reason to inspect storage.
After a child CLI acquisition fails, the reader makes no further CLI acquisitions
in that call; it retains collected history and marks skipped children with
`cli-acquisition-stopped` gaps. Do not retry another reader operation through
CLI to bypass that partial result; switch to supplied evidence/permitted GET.
It does not detect or prevent every automatic client migration or prove zero
storage writes. If the caller requires that stronger guarantee, use supplied
evidence or an already permitted read-only interface rather than claiming CLI
is isolated. Linux stdout capture is an anonymous memfd, closed on
all exits; other platforms use a pipe. Stderr is captured separately, never
reproduced in diagnostics. Exit 0 alone does not validate a complete export.

The historical v2 scoped oracle compared protected history/schema/project/Git/tasks/
telemetry witnesses with actual calls and separately classified allowed metadata,
housekeeping and log effects. It is historical evidence, not a runtime prerequisite
for ordinary retrospective reads. Test-owner instrumentation
is separate from retrospective runtime and does not authorize analyst SQL,
service startup, export capture files or experiments.

`--endpoint <authorized-base-URL>` uses an already available endpoint for missing
participants and recursive children/status reads. No discovery/start/import:
allowlisted GET `/session/status`, `/session/<ID>`, `/session/<ID>/children`,
`/session/<ID>/message`, `/session/<ID>/message/<messageID>` only. Directory query
is the exact selected canonical project. No redirects, proxies, embedded URL
credentials, mutation methods or other paths. Caller must establish endpoint
identity/version and access; this delivery does not handle authenticated endpoints.
Public no-limit messages response is expected complete; continuation headers,
unsupported schema/errors/limits produce explicit gaps/errors, not guessed pages.
Malformed selected root is not silently replaced by another transport/session.

## Schema, coverage and boundaries

Export is `{info,messages}`; each message has `{info,parts}`. Session identity is
`info.id`, `info.directory`, `info.projectID`; child `info.parentID` must match
the task metadata's `sessionId`/`parentSessionId`. List rows instead have
`id,title,updated,created,projectId,directory`. Root listing does not enumerate
children. A directory mismatch blocks project identity. An erased directory
requires `--project-id` with independently established exact project identity;
the ID is checked against info.projectID and the erased directory remains a gap.
Without that binding sanitized acquisition is blocked. Sanitized text/tool metadata is a
gap, not evidence of no instructions or no children. Parent export does not
contain child messages. Orphan/fork exports are not added by text similarity.

Overview reports identity, capture time, updated time, last refs, fingerprints,
participants and indexed sizes with initially empty observed ranges. Pages return
safe serialized message information and every part type with session/message/part
refs and `[start,end)` ASCII-content offsets. Large events span pages. `next` binds
fingerprint/event/offset; changed source or analysis scope rejects continuation.
Detail requires an exact ref and also has bounded continuation. Retain a separate
agent-observed coverage ledger; returned/indexed content is not proof it was read.
Do not use search as a substitute for full overview.

Keep one in-memory acquisition/index per participant for a run where the host can
retain the Python process; subsequent `pages(source,cursor,budget)` calls reuse it.
Separate CLI invocations reacquire and verify fingerprints: batch reasonably sized
ranges, do not re-export per event. Supplied files avoid CLI/storage overhead.
All content remains in memory; no reader-owned disk export/cache/temp. Input cap
is 64 MiB per source, page content budget 1–65536 bytes (default 8192), acquisition
cap 256 participants, timeout 30 seconds per CLI/GET. These are local resource
limits, not universal performance promises. Limit failures disclose unprocessed
scope. Tool-output truncation remains unseen; reduce page budget and resume.

Historical cutoff: crossing text/tool output is pending/late evidence; undated
mutable usage/linkage remains unknown at cutoff. A completed assistant interval
before cutoff establishes its steps' upper bound; IDs/position do not. A late
child branch is not included in exact historical metrics.
Late participants remain readable with an explicit late-snapshot scope; overview
lists them separately and metrics returns their snapshot values separately,
excluded from every historical total. They are not proven participants by cutoff.
Compaction/pruned outputs
and removed messages cannot be reconstructed from summary/current state.

## Metrics and safety

For verified 1.18.33, step-finish defines a request. Context is noncached input +
cache.read + cache.write, excluding output/reasoning/session aggregate. A single
step missing tokens may use its message tokens once, with fallback provenance;
a missing/default/incomplete step can use a compatible positive message fallback
when the single-step mapping is verified. A partial message yields only its
known lower bound; a more complete compatible message can replace an incomplete
step reading once, without summing the representations or inventing cache zeros.
multi-step message summaries are not summed. Missing/invalid/default-all-zero
usage is unknown; partial positive context is a lower bound. Peak/sums disclose
known subset and coverage. Exactly 150000 is not the mandatory threshold signal;
150001 is. Unknown full peak cannot rule out an exceedance.

Times are milliseconds. Unions are per category and across participants; parent
task wait is separate from tool union. Assistant created/completed is elapsed,
not pure generation/thinking. Human/external wait requires content evidence;
unclassified time is not automatically waste, and overlapping categories need
not sum to wall time. Historical late intervals must not be promoted to exact
cutoff totals. Use the base to interpret gaps and evidenced waiting.

For a verified sole-step request with two positive representations, incompatible
shared input/cache/output/reasoning fields are an explicit `usage-conflict`.
`requests[].readings` retains both addressed readings and their component quality;
the reader never adds, averages or chooses one as the winner. Conflicted requests
are excluded from `context_sum`, component sums and numeric `peak`. Any remaining
numeric `peak_lower_bound` covers only unconflicted known requests; global
`peak_quality: conflict` warns that full peak is unresolved. A conflicting known
reading/lower bound above 150000 still sets `threshold_signal`, with
`threshold_evidence[].basis: conflicting-reading` and provenance. This means
investigate the conflict, not assert an actual exceedance. Late readings do not
trigger the historical cutoff signal. Multi-step message aggregates are not
compared as one request; default-zero/absent step fallback retains its separate
single-request rule above.

No transcript command is executed. Diagnostic messages omit source bodies and
stderr. Structured sensitive keys and common token/key patterns are redacted in
displayed content; this is defense in depth, **not guaranteed secret discovery**.
Prefer references and manually minimize excerpts, especially error/default/file
parts. Never treat `--sanitize` as a guarantee that all secrets disappeared.

Checked public source contracts: [export.ts](https://github.com/anomalyco/opencode/blob/v1.18.33/packages/opencode/src/cli/cmd/export.ts),
[session CLI](https://github.com/anomalyco/opencode/blob/v1.18.33/packages/opencode/src/cli/cmd/session.ts),
and [public GET documentation](https://opencode.ai/docs/server/). Runtime capability
and side-effect evidence must come from the actual installation, not these links.
