# Separate checked publication content from local context

Read before checks/handoff when unrelated dirty files, exclusions or ambiguity
make the proposed snapshot differ from the observed working tree. This is evidence
preparation, not permission to stage, commit, clean or publish files.

1. Identify the exact base snapshot and authorized overlays/additions/deletions.
   Bind path/content and Git modes where applicable, including new files and
   unchanged base paths, in a reproducible snapshot or equivalent manifest.
2. Declare exclusions **before review**. Local reports, tracker data, installed
   tooling and generated outputs are not automatically publication content; project
   rules and the authorized change decide. Installed skill copies may be required
   delivery files, so do not exclude them merely because they are called installed.
3. For excluded dirty tracked paths retain their specified base bytes in the
   proposed snapshot, not the dirty working bytes. Report contextual changes and
   effects separately; never hide application code or an unexplained new file
   through an exclusion. Preserve the existing working copy and index.
4. Establish which bytes actually ran in each check. If contextual code/config
   affected execution, those results do not automatically cover the proposed
   snapshot. Obtain checks of the intended content in an authorized suitable
   environment or mark the affected criteria unverified; do not prepare/reset a
   worktree as an implicit workaround.
5. Hand off the snapshot/manifest and separate contextual evidence. Changing the
   snapshot, including upstream integration or later document edits, requires
   reassessment of checks/review applicability. A matching task diff alone is not
   evidence that the full reviewed tree is unchanged. Never invent exclusions
   later to justify different published bytes.
