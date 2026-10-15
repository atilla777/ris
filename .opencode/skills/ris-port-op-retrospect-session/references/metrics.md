# Context and duration evidence

Read when metrics are supplied or a metric gap is relevant. Apply only the
declared source/version semantics; no client field formula is universal.

## Request context and usage

For the lead and each proven participant separately identify request units,
addresses, source/version, units and coverage (known requests / available
requests, plus unknown enumeration). Keep separate:

- maximum known **single-request input context** and quality of that value;
- sums of nonoverlapping request input/output usage and cache metrics;
- compaction/recovery and evidenced sources of growth.

A session aggregate is not request context. Aggregate 900000 with individual
peak 100000 does not meet the peak threshold. Input/cache fields may be inclusive
or disjoint: add cache only if their declared semantics establish disjoint input
components. Unknown semantics means unknown context or labeled estimate/bound,
not an assumed sum. Output/reasoning are not input context; do not add overlapping
output/reasoning fields to each other without an explicit disjoint contract.

Deduplicate multiple representations of one proven request; do not sum a request
record and its message summary. A message link alone does not establish which
request a metric describes when there are multiple requests. Preserve conflicting
source versions with provenance, not averages. Numeric union across sources
requires proven one-to-one request mapping and compatible semantics; unmatched
measurements can remain separate source-specific evidence.

Missing usage is unknown, not zero. Report a zero known to be an SDK default as
unmeasured; a numerical zero without a measurement guarantee cannot prove no
usage. A maximum over partial known requests is a known-subset peak / lower
bound on the whole participant peak, not a fully measured peak. Do not invent
token estimates from bytes without a declared estimation method.

**Strictly greater than 150000 tokens** requires episode deep dive independently
for each participant. Exactly 150000 does not trigger this rule; 150001 does.
An estimate or lower bound >150000 also triggers, retaining its quality limits.
Unknown peak cannot rule out an exceedance. Below-threshold episodes still merit
investigation when other signals exist. Threshold crossing is not a defect:
check necessary loads, repeated reads, available alternatives and observed losses.

## Time

State units, clock basis, source and interval quality. Distinguish event wall
span, active-work estimate, model generation, tools, retries/recovery, human and
external waits, and unclassified time. Session created/updated or an assistant
message span can include idle/tools and does not prove pure generation.
Generation duration is not “thinking time” without a corresponding measurement.

For each category sort intervals and merge overlapping/nested intervals before
measuring their union. Across participants compute active union rather than
summing child work with parent task-wait. For child A [1,6] and B [4,9], active
union is [1,9] = 8 time units, not 10; parent wait [0,10] adds no separate active
work. Tools [2,5] and [4,7] have union [2,7] = 5, not 6. Categories can overlap
and need not sum to wall time; do not subtract overlaps twice. Use an evidenced
critical path only when its dependencies are known.

Human wait [10,110] = 100 is not agent loss. Unclassified [110,120] = 10 remains
unclassified. Generation [120,122] = 2 is generation, not cognition. Investigate
even a short repeated failure [122,123] = 1 without an absolute time threshold;
whether it is avoidable loss depends on actions and available alternatives.
Long elapsed time alone does not establish inefficiency. Similar-session
comparisons require already supplied comparable authorized data and do not
expand this operation into a cross-session audit.

For every reported number retain participant/request or interval references,
provenance, exact/estimate/bound/unknown quality and coverage. Keep severity
based on observed consequences, not metric size or confidence. Missing metrics
limit measurement, not independent qualitative investigation.
