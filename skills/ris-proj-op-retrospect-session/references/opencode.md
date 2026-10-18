# Local OpenCode reader

Read from the installed wrapper before collection/interpretation. This resource
owns mechanics; the portable base owns retrospective reasoning. The V2 baseline
is OpenCode **2.0.32**, Python 3 standard library. Existing **1.18.33** exports
and its fixed CLI/GET contracts remain readable. V2 CLI releases with a stable
`2.x.y` version may acquire content under the checked structural contract; other
V2 semantic versions preserve content with unknown request metrics. No dependency
install is needed. V2 skill discovery itself does not require a skill rewrite;
the changed CLI/API/transcript contracts require this reader adapter.

## Invocation and permissions

Resolve `scripts/opencode_read.py` from the folder containing this resource's
parent `SKILL.md`. Run `python3 -B <installed-reader> <operation> --project <root>`.
Operations: `list`, `overview`, `pages`, `detail`, `metrics`. Output is JSON;
operation status is `ok|blocked|conflict|error`, never `partial`. Fatal source/
parser errors emit secret-safe `error` and exit 2. A usable root with failed
required acquisition returns its payload, `gaps`, stopping `cause` and exact
`remaining` work at exit 0: inspect status and evidence, not exit alone. Technical
acquisition failure is `error`, missing source/capacity is `blocked`, contradictory
participant identity/links is `conflict` (conflict takes precedence over error,
then blocked if several causes coexist). No raw exception/stderr is included.
Child identity and explicit version-binding contradictions use the reader's
typed source conflict, including project ID, message session and part identity;
their fixed secret-safe reason is preserved for CLI/GET and supplied child exports.
Known measurement/version/cutoff/redaction limitations and unavailable optional
children enumeration alone do not fail a bounded read: retain their gaps and
coverage limits. `ok` describes only the returned mechanics, not complete history,
completed analysis or acceptance; metrics quality remains independently qualified.
In particular, `children-GET-unavailable` remains a coverage gap, not a stopping
cause. Reading a known child from task links or successful enumeration is a
required acquisition: its failure still contributes the actual causal non-`ok`.
Contradictory enumerated parent identity is instead a `children-GET-conflict`
cause; optional availability never makes a known identity contradiction successful.

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
`opencode --version`, then for V2 `opencode session export <ID>` and allowlisted
`opencode api get '<path>?<encoded-allowlisted-query>'`, cwd=selected project,
shell=False. The standard V2 client owns service discovery and authentication;
never read/copy its credentials into arguments or use an unauthenticated fallback
after an auth failure. Export and every GET use `--server <URL>` when `--endpoint`
is supplied with CLI permission. Without an explicit endpoint they use the same
standard managed-service context. The producing server version comes from
`/api/info`, not from the client version; explicit `--version` disagreement is a
conflict. `list --allow-cli` runs `opencode session list --format json
--max-count 5` and returns bounded `ok` with `selected: null` and remaining exact
session selection, never a selected session or analysis readiness. CLI
permission is supplied by the retrospective request unless the caller or project
restricts CLI use. Pass `--allow-cli` for these fixed reads; it acknowledges
permission, not independently verified initialized storage or a fitness witness.
Do not inspect SQLite, enumerate service paths or request an export solely to
prove readiness. Prefer a supplied export when one is already provided. For
1.18.33 only, export/list retain their legacy `--pure` argv and export command.
V2 has no documented `--pure` isolation contract; do not claim one.

Ordinary OpenCode metadata, DB/WAL/checkpoint housekeeping and own logs outside
the developed project are accepted service effects. Message/part content and
semantic history links, project files/config/docs/Git, task state/edges and
telemetry stay protected. This is not permission for arbitrary outside-project
writes, plugins or analyst storage edits. A known service path inside the
developed project or another concrete out-of-scope effect blocks CLI use; an
absent service-path inventory alone does not. Automatic discovery/start of the
managed V2 service by its standard client is accepted; explicit lifecycle commands,
`--standalone`, server setup/restarts and private-server fallback are not. A caller
forbidding all service startup must supply an export or an already authorized GET
source without CLI permission. No service state/DB inspection is required.

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

For V2 with `--allow-cli`, `--endpoint <authorized-base-URL>` selects the standard
client's explicit server, including its authentication context. Without CLI
permission it uses direct GET to an already available caller-authorized endpoint;
the caller must establish V2 source version with `--version 2.x.y`. V2 allowlist:
`/api/info`, `/api/session/active`, `/api/session/<ID>`,
`/api/session/<ID>/message`, and `/api/session` filtered by `parentID` for children.
Direct GET unwraps `data`; message and child lists follow body `cursor.next`,
preserving filters and omitting `order` after the first page. No arbitrary paths,
methods or caller-defined queries are accepted.
In 2.0.32, raw method/path mode ignores `--param`; the reader encodes validated
queries into the path instead. Do not drop a parent filter or pagination cursor.
V2 session scope is checked from
`projectID` and `location.directory`; it is not a legacy directory query added
to every request. Child enumeration is not directory-filtered: a moved/foreign
child must be disclosed, not silently hidden. Active means foreground execution
on the observed process only, never successful completion or absence of background
work. A changed identity is a conflict.

Legacy 1.18.33 `--endpoint` retains already available recursive children/status
reads. No discovery/start/import:
allowlisted GET `/session/status`, `/session/<ID>`, `/session/<ID>/children`,
`/session/<ID>/message`, `/session/<ID>/message/<messageID>` only. Directory query
is the exact selected canonical project. No redirects, proxies, embedded URL
credentials, mutation methods or other paths. Caller must establish endpoint
identity/version and access. Direct GET does not handle authenticated endpoints;
use the permitted V2 standard client for its supported authentication context.
Only the legacy public no-limit messages response is expected complete; continuation headers,
unsupported schema/errors/limits produce explicit gaps/errors, not guessed pages.
Malformed selected root is not silently replaced by another transport/session.

## Schema, coverage and boundaries

V2 CLI export is `{data:{info,messages}}`; the inner `{info,messages}` is also
accepted as a supplied transcript. Messages have `id,type,time`; assistant items
have `content`, including text/reasoning/tool items, while system, skill, shell,
synthetic, compaction, idle and switch messages retain their own fields. Tool call
IDs are opaque strings, not `prt_*`. Pages preserve all original fields and use
`session/message/content/<zero-based-index>` refs; these are reader addresses in
the fingerprinted projection, not invented native part IDs. Message refs remain
`session/message`. Internal normalization is only for tree/metric mechanics.

V2 identity uses `info.id`, `info.projectID`, `info.location.directory` and
`info.parentID`. Subagent links use tool `name: subagent`,
`state.metadata.sessionID`, and the child's matching `parentID`; no prose/output
regex establishes ancestry. Running/progress/error metadata may retain the link.
Both foreground and background calls are supported. Repeated calls to one child
count once; forks are not participants. Without a link/enumeration, children
remain unknown. A sanitized V2 directory starts `/[redacted:session-directory:`
and needs the same independent `--project-id` binding as legacy sanitized data.
V2 transcripts are projections, not complete event logs. The standard export
omits unsettled assistant/shell/compaction messages; this is always disclosed as
a coverage gap, not silently treated as a full event history. API message reads
can include unsettled messages. System/skill messages are historical evidence;
missing historical tool/system schemas still remain unknown.

Legacy export is `{info,messages}`; each message has `{info,parts}`. Session identity is
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
cap 256 participants, timeout 30 seconds per CLI/GET. V2 pagination is capped at
256 pages and 65536 rows per list; repeated cursors/IDs or invalid page shapes
fail the acquisition rather than silently dropping a page. These are local resource
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

For verified 2.0.32, an assistant message projects one provider step; a compaction
message's tokens describe its own compaction request. Both contribute once to
request metrics (undated completion remains unknown at historical cutoff). Their tokens
are the step's normalized usage, not the session aggregate. Context is noncached
input + cache.read + cache.write, excluding output/reasoning. Missing provider
components may be normalized to zero: positive context is reported as a lower
bound, all-zero/absent usage is unknown. Retries can include unmeasured attempts;
their gap is retained, never multiplied/summed from the retry counter. Do not use
the client version, `info.tokens`, provider context/checkpoint size or accumulated
session cost to establish a per-request peak. V2 source version is not embedded
in the export: supplied evidence needs an independently established `--version`
for known semantics; absent version keeps content readable and metrics unknown.

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
task wait is separate from tool union. V2 tool execution uses `time.ran` through
`time.completed`; subagent call lifetime records dispatch/foreground blocking,
not the lifetime of a background child. Child intervals are read from that child's
own history and never added to the parent's delegation interval. Assistant created/completed is elapsed,
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

Checked V2 contracts: [migration](https://opencode.ai/v2/docs/migrate-v1),
[API/OpenAPI](https://opencode.ai/v2/docs/api), and pinned 2.0.32
[CLI export](https://github.com/anomalyco/opencode/blob/v2.0.32/packages/cli/src/commands/handlers/session/export.ts),
[transcript export](https://github.com/anomalyco/opencode/blob/v2.0.32/packages/core/src/session/transfer.ts),
[messages](https://github.com/anomalyco/opencode/blob/v2.0.32/packages/schema/src/session-message.ts),
[step mapping](https://github.com/anomalyco/opencode/blob/v2.0.32/packages/core/src/session/runner/step.ts),
[usage](https://github.com/anomalyco/opencode/blob/v2.0.32/packages/core/src/session/usage.ts),
[subagents](https://github.com/anomalyco/opencode/blob/v2.0.32/packages/core/src/tool/plugin/subagent.ts).
Legacy contracts: [export.ts](https://github.com/anomalyco/opencode/blob/v1.18.33/packages/opencode/src/cli/cmd/export.ts),
[session CLI](https://github.com/anomalyco/opencode/blob/v1.18.33/packages/opencode/src/cli/cmd/session.ts),
and [public GET documentation](https://opencode.ai/docs/server/). Runtime capability
and side-effect evidence must come from the actual installation, not these links.
