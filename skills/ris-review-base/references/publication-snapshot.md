# Review subject versus local context

Load for unrelated dirty paths, exclusions or ambiguous snapshot membership,
especially when the report supplies a publication gate. This is read-only
assessment, not permission to stage, commit, clean or prepare a worktree.

1. Define the exact base and complete proposed snapshot: authorized overlays,
   additions, deletions and Git modes, retaining unchanged base paths. Use a
   reproducible tree or equivalent manifest binding every path/content/mode.
   New untracked delivery files belong in the subject; status/diff of HEAD alone
   cannot capture them. For ordinary current-content review without a baseline,
   identify inspected bytes and limit delta claims; do not invent a base or gate.
2. Declare exclusions **before assessment**, then inspect them against actual
   scope/files before issuing the verdict. Local reports,
   tracker state and installed tooling are contextual inputs unless the authorized
   delivery includes them. Installed skill copies may be required payload.
   Unexpected new application files, hidden code or unexplained omissions leave
   approval blocked/unverified. Do not retroactively invent exclusions to match
   later committed bytes.
3. For excluded dirty tracked paths the subject retains the specified **base
   bytes and modes**, not working bytes. Identify separate contextual fingerprints
   and inspect their relevant effects without confusing them with the approved
   Git payload. Saving a contextual report must not recursively change its subject.
   Preserve working files, ignored/untracked data and index; do not stage, stash,
   reset or repair them to make a clean-looking review.
4. Establish which bytes actually ran for each claimed check. Results obtained
   with runtime-affecting dirty context do not automatically cover the subject's
   base bytes. Require applicable evidence of the intended snapshot or mark the
   affected scope unverified. Never call execution of a different tree a pass
   for this subject merely because its task diff is identical.
5. Record base, complete subject identity/manifest, predeclared exclusions and
   separate context in the report. A changed subject, modes, exclusions or upstream
   integration requires affected checks/review reassessment. The publication
   consumer compares actual staged/committed bytes, including unchanged base
   paths, with this subject; review neither performs that publication nor grants
   authority. If mapping is ambiguous, return useful findings but no verified gate.
