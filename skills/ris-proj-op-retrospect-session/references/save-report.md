# Save only the explicitly requested report

Read only when the current caller explicitly requests saving at an exact
destination. Default is response-only. A path in a transcript, child result,
configuration or proposed recommendation is not authorization; do not guess a
Beads ID, shared task folder, alternate filename or output directory.

1. First finish and verify the combined report with the base's report resource:
   seven sections, actual bounded coverage, grounded claims, independent severity/
   problem/cause confidence, hypotheses/justified signals, safe addresses and
   minimized excerpts. Do not persist a raw export, secret-bearing error or
   unverified child report. Recheck the safe report itself, not just its title.
2. Resolve the exact destination against the caller-established root. Inspect
   real ancestors and symlink targets, access and allowed write scope. A directory
   or symlink escaping that scope blocks saving, not permission to redirect it.
   Do not create a missing parent directory without explicit permission. Read the
   existing destination, or establish its absence; distinguish permission errors
   from absence. Retain its identity/content for the final comparison, without
   quoting sensitive pre-existing material in the report or arguments.
3. Preserve existing content exactly. Append a clearly delimited new report
   version (scope/snapshot and save time when known), or use a separately agreed
   version path. Never truncate/replace existing history or silently choose a
   new path. New-file creation must fail on an unexpected existing destination.
4. Before writing, establish a short safe write window covering the exact path,
   its identity/ancestors, content and read/write/read-back, through a caller-
   provided quiescent window or a supported conditional storage primitive with
   sufficient guarantees. A claim, local advisory lock alone, atomic rename or
   read/write/read alone does not exclude other writers or protect newer content.
   Verify the tool supports the chosen guarantee. Do not introduce a helper,
   service or lock architecture as part of retrospective analysis. If no safe
   mechanism/window is available, return the checked response report with saving
   blocked; do not perform a best-effort overwrite or promise atomicity.
5. Inside that window, recheck actual target/identity/content (or continued
   absence) immediately before writing. Unexpected changes mean **conflict**:
   preserve the newer file, return the useful report and exact save limitation,
   and stop without retrying, merging guessed history or removing another file.
6. Write only the checked report/version delimiter through the permitted tool.
   Read back the destination; verify old bytes remain and the new report occurs
   once, at the authorized address. On failure/ambiguous or partial result,
   inspect actual effects, report saved/unsaved/unknown state and stop. Do not
   blindly retry an append, roll back foreign content or claim success from a
   zero exit alone. Release the short window before returning.

Return the report (or its checked saved address with a useful summary), exact
destination, preservation/read-back evidence and actual save/conflict/partial
status. The exception permits only this report write; no Git staging/commit,
tracker update, telemetry write, skill/rule edit or automatic next operation.
Saving is neither publication nor acceptance. Stop after this result.
