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
    registration corroborate an association. A stale, moved or foreign witness
    is not usable association and must not be silently bypassed by inference.
4. A valid explicit selection wins over an older saved hint; expose contradictory
   facts and why the hint is inapplicable, never silently conceal them or let it
   override the selection. If the explicit selection's own association remains
    contradictory, return conflict. Ambiguous/conflicting evidence is conflict;
    foreign/stale association blocks shared-path use, not fallback permission.
5. Only when explicit and applicable saved selections are absent, inspect native
    Git facts for the ordinary non-bare source working copy: resolve the current
    top-level/common Git directory and worktree registrations (for example
    `git rev-parse --show-toplevel --git-common-dir` and `git worktree list --porcelain`).
    Verify the common directory's ordinary source copy by its actual Git mapping,
    physical accessible path, non-bare status and registration, shared repository
    identity and selected-project location/config/instruction association. For a
    subproject preserve its verified repository-relative project location. Do not
    choose the first listing, a branch named main or a directory containing `.sdlc`.
    Bare repositories, missing source copies, ambiguous project mapping or
    contradictory facts block this fallback; do not choose an arbitrary linked
    worktree. No saved receipt is required for an unambiguous verified Git source
    copy. Name the exact gap and retain independent current-copy settings.
6. Return the selected physical root, selection source/evidence address or Git facts,
   verification facts and limits. Make no persistent changes or new registry.
   Consumers recheck applicability after copy/project changes and mutable facts
   before acting. A receipt proves neither fresh permission, ownership/blockers
    nor operation-specific write protection; these remain the acting owner's gates.
    Resolving shared review/worktree addresses never authorizes branch switching
    or mutation of primary files; copy ownership and local synchronization safety
    are separate checks.
