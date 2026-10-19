# Bounded primary resolution

This context owner resolves primary identity; consumers use its checked result
rather than duplicating discovery. Read only when shared paths or the primary
copy's identity for publication synchronization are needed; resolution grants no
permission to mutate that copy:

1. Validate an explicitly supplied `primary_root` first. Check existence,
   accessibility and physical target, selected-project identity, repository
   relationship and association with the current copy. An invalid explicit
   selection blocks the dependent part; never substitute a saved hint/default.
2. Without explicit selection, inspect only an **already available** saved
   indication in applicable project instructions or a copy-preparation result.
   Record its exact evidence address and provenance. Resolve relative indications
   from their declared base (an instruction pointer from its file's directory);
   an unknown base is a gap. Do not search the disk for arbitrary receipts.
3. Verify the candidate's actual existence/physical target and unambiguous
   selected-project/repository relationship, the witness's provenance and its
   association to this current copy/path/branch where applicable. Check for
   conflicting applicable saved indications. Git common-dir and worktree
   registration corroborate an association, but never select a primary alone.
   Neither branch name, first/main worktree listing nor `.sdlc/` presence is
   a selector. A stale, moved or foreign witness is not usable association.
4. A valid explicit selection wins over an older saved hint; expose contradictory
   facts and why the hint is inapplicable, never silently conceal them or let it
   override the selection. If the explicit selection's own association remains
   contradictory, return conflict. Without explicit selection, missing evidence
   is blocked, ambiguous/conflicting evidence is conflict, and foreign/stale
   association blocks shared-path use. Name the exact missing root/association
   or decision and retain independently usable current-copy source settings.
5. Return the selected physical root, selection source/evidence address,
   verification facts and limits. Make no persistent changes or new registry.
   Consumers recheck applicability after copy/project changes and mutable facts
   before acting. A receipt proves neither fresh permission, ownership/blockers
   nor operation-specific write protection; these remain the acting owner's gates.
