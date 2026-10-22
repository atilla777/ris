# Conditional `ris.review/1` history

Part of conditional `report-format-v1.md`, not a separate format or assessment method. Read only for /1 before
appending/consuming multiple rounds, prior-finding dispositions or conflicting
historical evidence. First-round review with no prior findings does not load it.

`rounds` is chronological, without forks/cycles: first `previous: null`, each
later `previous` equals the preceding element's ID. Never renumber IDs. Re-review
retains earlier finding IDs and their current statuses/dispositions; new defects
receive new IDs. All prior findings remain represented. A resolved finding needs
the reviewer's reasoned Disposition. High/medium cannot be resolved by `deferred`;
author's repair never rewrites a past round as approval. Low permits collective
reasoned prose disposition; per-ID dispositions may be used, without a new round
for low alone.

Read the whole report, not just the selected approval. A later applicable unresolved
high/medium or blocked result forbids fallback to an old approval until independently
resolved. Later invalid/unknown rounds require reconciliation, never fallback.
Preserve prior rounds and compare before append/read-back under the storage rules
in `report-format-v1.md`. Its mechanical validator checks intrinsic history; actual
evidence, independence and applicability remain external consumer predicates.
