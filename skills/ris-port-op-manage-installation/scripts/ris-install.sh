#!/usr/bin/env bash
# RIS installation engine. Bash 3.2+; no project initialization.
export LC_ALL=C
set -o pipefail
die() { printf 'RIS: %s\n' "$*" >&2; return 1; }
parse() {
    OP=${1-}; [ "$#" -gt 0 ] && shift
    case "$OP" in install|update|uninstall) ;; *) die 'expected install/update/uninstall'; return 1;; esac
    PROJECT= REF=; local seen_project=0 seen_ref=0
    while [ "$#" -gt 0 ]; do
        case "$1" in
            --project) [ "$seen_project" = 0 ] || { die 'duplicate --project'; return 1; }; seen_project=1; [ "$#" -ge 2 ] || return 1; PROJECT=$2; shift 2;;
            --ref) [ "$seen_ref" = 0 ] || { die 'duplicate --ref'; return 1; }; seen_ref=1; [ "$#" -ge 2 ] || return 1; REF=$2; [ -n "$REF" ] || return 1; shift 2;;
            *) die "unknown argument: $1"; return 1;;
        esac
    done
    [ "$seen_project" = 1 ] && [[ "$PROJECT" = /* ]] && [ -d "$PROJECT" ] || { die 'existing absolute --project required'; return 1; }
    [ "$OP" != uninstall ] || [ "$seen_ref" = 0 ] || { die 'uninstall rejects --ref'; return 1; }
}
SOURCE=https://github.com/atilla777/ris.git
MANAGEMENT=ris-port-op-manage-installation
exists() { [ -e "$1" ] || [ -L "$1" ]; }
dependencies() {
    local tool version major minor
    [ "${BASH_VERSINFO[0]}" -gt 3 ] || { [ "${BASH_VERSINFO[0]}" = 3 ] && [ "${BASH_VERSINFO[1]}" -ge 2 ]; } || { die 'Bash 3.2+ required'; return 1; }
    for tool in git flock cp mv rm mkdir rmdir mktemp chmod cmp diff id ls readlink; do
        command -v "$tool" > /dev/null || { die "missing dependency: $tool (install externally)"; return 1; }
    done
    version=$(git --version) || return 1
    version=${version#git version }; major=${version%%.*}; version=${version#*.}; minor=${version%%.*}
    [[ "$major" =~ ^[0-9]+$ ]] && [[ "$minor" =~ ^[0-9]+$ ]] &&
        { [ "$major" -gt 2 ] || { [ "$major" = 2 ] && [ "$minor" -ge 20 ]; }; } || { die 'Git 2.20+ required'; return 1; }
}
ordinary_dir() { [ -d "$1" ] && [ ! -L "$1" ]; }
parents() {
    local p
    for p in "$ROOT/.opencode" "$ROOT/.opencode/skills" "$ROOT/.opencode/command"; do
        if exists "$p"; then ordinary_dir "$p" || { die "unsafe parent: $p"; return 1; }; fi
    done
}
# OpenCode mapping only. All transaction code consumes relative paths.
managed() {
    local p
    PATHS=()
    for p in "$ROOT"/.opencode/skills/ris-*; do
        exists "$p" || continue
        [ -L "$p" ] || [ -d "$p" ] || { die "invalid skill type: $p"; return 1; }
        PATHS[${#PATHS[@]}]=${p#"$ROOT/"}
    done
    for p in "$ROOT"/.opencode/command/ris-*.md "$ROOT/.opencode/ris-installation"; do
        exists "$p" || continue
        [ -L "$p" ] || [ -f "$p" ] || { die "invalid file type: $p"; return 1; }
        PATHS[${#PATHS[@]}]=${p#"$ROOT/"}
    done
}
acquire() {
    git -c core.hooksPath=/dev/null clone --no-checkout -- "$SOURCE" "$WORK/repo" || return 1
    local expr entry info path mode type oid name file first line found closed names
    if [ -z "$REF" ]; then expr=HEAD
    elif [[ "$REF" =~ ^[0-9a-fA-F]{40}$ ]]; then
        [ "$(git -C "$WORK/repo" cat-file -t "$REF")" = commit ] || { die 'full SHA must name a commit object'; return 1; }
        expr=$REF
    else
        git check-ref-format "refs/tags/$REF" || return 1
        git -C "$WORK/repo" show-ref --verify --quiet "refs/tags/$REF" || { die 'exact tag not found'; return 1; }
        expr="refs/tags/$REF"
    fi
    SHA=$(git -C "$WORK/repo" rev-parse --verify "$expr^{commit}") || return 1
    [[ "$SHA" =~ ^[0-9a-f]{40}$ ]] || return 1
    mkdir -p "$WORK/stage/.opencode/skills" "$WORK/stage/.opencode/command" || return 1
    git -C "$WORK/repo" ls-tree -rz "$SHA" > "$WORK/tree" || return 1
    SKILLS=(); COMMANDS=()
    while IFS= read -r -d '' entry; do
        info=${entry%%$'\t'*}; path=${entry#*$'\t'}
        IFS=' ' read -r mode type oid <<< "$info"
        case "$path" in
            skills/ris-*/*)
                name=${path#skills/}; name=${name%%/*}
                [[ "$name" =~ ^ris-[a-z0-9]+(-[a-z0-9]+)*$ ]] && [ "${#name}" -le 64 ] || return 1
                file="$WORK/stage/.opencode/${path}"
                found=0; for entry in "${SKILLS[@]}"; do [ "$entry" != "$name" ] || found=1; done
                [ "$found" = 1 ] || SKILLS[${#SKILLS[@]}]=$name;;
            commands/opencode/ris-*.md)
                name=${path#commands/opencode/}; [[ "$name" != */* ]] || continue
                file="$WORK/stage/.opencode/command/$name"
                COMMANDS[${#COMMANDS[@]}]=$name;;
            skills/ris-*) die "incomplete skill: $path"; return 1;;
            *) continue;;
        esac
        [ "$type" = blob ] && { [ "$mode" = 100644 ] || [ "$mode" = 100755 ]; } || { die "unsafe tree entry: $path"; return 1; }
        mkdir -p "${file%/*}" || return 1
        git -C "$WORK/repo" cat-file blob "$oid" > "$file" || return 1
        if [ "$mode" = 100755 ]; then chmod 755 "$file"; else chmod 644 "$file"; fi || return 1
        [ "$(git hash-object --no-filters -- "$file")" = "$oid" ] || return 1
    done < "$WORK/tree"
    [ "${#SKILLS[@]}" -gt 0 ] && [ "${#COMMANDS[@]}" -gt 0 ] || { die 'empty package: missing management package'; return 1; }
    for name in "${SKILLS[@]}"; do
        file="$WORK/stage/.opencode/skills/$name/SKILL.md"
        [ -f "$file" ] || { die "missing SKILL.md: $name"; return 1; }
        first=1; found=0; closed=0; names=0
        while IFS= read -r line; do
            if [ "$first" = 1 ]; then [ "$line" = --- ] || return 1; first=0; continue; fi
            if [ "$line" = --- ]; then closed=1; break; fi
            case "$line" in name:*) names=$((names + 1));; esac
            case "$line" in "name: $name"|"name: \"$name\""|"name: '$name'") found=$((found + 1));; esac
        done < "$file"
        [ "$found" = 1 ] && [ "$closed" = 1 ] && [ "$names" = 1 ] || { die "SKILL frontmatter/name mismatch: $name"; return 1; }
    done
    [ -f "$WORK/stage/.opencode/skills/$MANAGEMENT/SKILL.md" ] &&
    [ -x "$WORK/stage/.opencode/skills/$MANAGEMENT/scripts/ris-install.sh" ] &&
    [ -f "$WORK/stage/.opencode/command/$MANAGEMENT.md" ] || { die 'missing management package'; return 1; }
    printf 'format=1\nsource=%s\nrevision=%s\nharness=opencode\n' "$SOURCE" "$SHA" > "$WORK/stage/.opencode/ris-installation"
}
lock() {
    local uid key dir attrs
    uid=$(id -u) || return 1
    dir=/tmp/ris-install-locks-$uid
    if ! exists "$dir"; then (umask 077; mkdir "$dir") || return 1; fi
    ordinary_dir "$dir" && [ -O "$dir" ] || { die "unsafe lock directory: $dir"; return 1; }
    attrs=$(LC_ALL=C ls -ld "$dir") || return 1
    [ "${attrs%% *}" = drwx------ ] || return 1
    key=$(printf '%s' "$ROOT" | git hash-object --no-filters --stdin) || return 1
    LOCK=$dir/$key.lock
    if exists "$LOCK"; then [ -f "$LOCK" ] && [ ! -L "$LOCK" ] && [ -O "$LOCK" ] || return 1; fi
    exec 8>>"$LOCK" || return 1
    flock -n 8 || { die "busy: $ROOT (not changed)"; return 1; }
}
remove_managed() {
    managed || return 1
    local p
    for p in "${PATHS[@]}"; do rm -rf -- "$ROOT/$p" || return 1; done
}
copy_stage() {
    local p
    mkdir -p "$ROOT/.opencode/skills" "$ROOT/.opencode/command" || return 1
    for p in "$WORK/stage/.opencode/skills"/*; do cp -pPR "$p" "$ROOT/.opencode/skills/" || return 1; done
    for p in "$WORK/stage/.opencode/command"/*; do cp -pP "$p" "$ROOT/.opencode/command/" || return 1; done
    cp -pP "$WORK/stage/.opencode/ris-installation" "$ROOT/.opencode/.ris-version.tmp" &&
        mv -f "$ROOT/.opencode/.ris-version.tmp" "$ROOT/.opencode/ris-installation"
}
# A binary ledger independent of the backup copy. Bash glob order is stable in C
# locale. Link targets are hashed as data, never traversed. Directory modes and
# empty directories participate; inode/time/ACL/xattrs deliberately do not.
# Schema 1 requires raw bytes, regardless of caller Git filters/EOL settings.
# A mismatching historical filtered ledger is not rewritten or trusted here.
record_tree() {
    local base=$1 rel=$2 strict=$3 p attrs kind value child
    p=$base/$rel
    attrs=$(ls -ld -- "$p") || return 1
    attrs=${attrs%% *}; attrs=${attrs:0:10}
    if [ -L "$p" ]; then
        kind=link; value=$(readlink -- "$p" | git hash-object --no-filters --stdin) || return 1
    elif [ -d "$p" ]; then kind=dir; value=
    elif [ -f "$p" ]; then kind=file; value=$(git hash-object --no-filters -- "$p") || return 1
    else
        [ "$strict" = no ] || { die "unsafe special file: $p"; return 1; }
        kind=special; value=
    fi
    printf '%s\0%s\0%s\0%s\0' "$rel" "$kind" "$attrs" "$value"
    if [ "$kind" = dir ]; then
        for child in "$p"/* "$p"/.[!.]* "$p"/..?*; do
            exists "$child" || continue
            record_tree "$base" "${child#"$base/"}" "$strict" || return 1
        done
    fi
}
managed_ledger() {
    local old=$ROOT base=$1 p
    ROOT=$base; managed || { ROOT=$old; return 1; }; ROOT=$old
    for p in "${PATHS[@]}"; do record_tree "$base" "$p" yes || return 1; done
}
foreign_walk() {
    local base=$1 rel=$2 p child
    case "$rel" in
        .opencode/.ris-install-transaction|.opencode/.ris-version.tmp|.opencode/skills/ris-*|.opencode/command/ris-*.md|.opencode/ris-installation) return 0;;
    esac
    p=$base/$rel
    # Container existence can change; their foreign children cannot.
    case "$rel" in .opencode|.opencode/skills|.opencode/command)
        if [ -d "$p" ]; then
            for child in "$p"/* "$p"/.[!.]* "$p"/..?*; do
                exists "$child" || continue
                foreign_walk "$base" "${child#"$base/"}" || return 1
            done
        fi;;
        *) record_tree "$base" "$rel" no || return 1;;
    esac
}
marker() {
    printf '1\n' > "$J/$1.tmp" && mv -f "$J/$1.tmp" "$J/$1"
}
check_marker() { [ -f "$J/$1" ] && [ ! -L "$J/$1" ] && [ "$(<"$J/$1")" = 1 ]; }
snapshot() {
    mkdir -p "$ROOT/.opencode" || return 1
    (umask 077; mkdir "$J") || return 1
    marker schema || return 1
    mkdir -p "$J/backup/.opencode/skills" "$J/backup/.opencode/command" || return 1
    managed_ledger "$ROOT" > "$J/oracle.tmp" && mv "$J/oracle.tmp" "$J/oracle" || return 1
    foreign_walk "$ROOT" .opencode > "$J/foreign.tmp" && mv "$J/foreign.tmp" "$J/foreign" || return 1
    managed || return 1
    local p
    : > "$J/manifest.tmp" || return 1
    for p in "${PATHS[@]}"; do
        printf '%s\0' "$p" >> "$J/manifest.tmp" || return 1
        cp -pPR "$ROOT/$p" "$J/backup/${p%/*}/" || return 1
    done
    mv "$J/manifest.tmp" "$J/manifest" || return 1
    validate_backup || return 1
    marker prepared
}
valid_path() {
    local tail
    case "$1" in
        .opencode/ris-installation) return 0;;
        .opencode/skills/ris-*) tail=${1#.opencode/skills/};;
        .opencode/command/ris-*.md) tail=${1#.opencode/command/};;
        *) return 1;;
    esac
    [[ "$tail" != */* ]] && [ -n "$tail" ]
}
validate_backup() {
    local p
    for p in backup backup/.opencode backup/.opencode/skills backup/.opencode/command; do ordinary_dir "$J/$p" || return 1; done
    for p in manifest oracle foreign; do [ -f "$J/$p" ] && [ ! -L "$J/$p" ] || return 1; done
    while IFS= read -r -d '' p; do valid_path "$p" || return 1; done < "$J/manifest"
    managed_ledger "$J/backup" > "$WORK/backup-ledger" && cmp -s "$J/oracle" "$WORK/backup-ledger" || return 1
    managed_ledger "$J/backup" > /dev/null || return 1
    : > "$WORK/paths" || return 1
    for p in "${PATHS[@]}"; do printf '%s\0' "$p" >> "$WORK/paths" || return 1; done
    cmp -s "$WORK/paths" "$J/manifest"
}
verify_foreign() {
    foreign_walk "$ROOT" .opencode > "$WORK/foreign-now" && cmp -s "$J/foreign" "$WORK/foreign-now"
}
rollback() {
    validate_backup || { die "recovery required: invalid backup at $J; preserve evidence"; return 1; }
    remove_managed || return 1
    local p
    mkdir -p "$ROOT/.opencode/skills" "$ROOT/.opencode/command" || return 1
    while IFS= read -r -d '' p; do cp -pPR "$J/backup/$p" "$ROOT/${p%/*}/" || return 1; done < "$J/manifest"
    rm -f "$ROOT/.opencode/.ris-version.tmp" || return 1
    managed_ledger "$ROOT" > "$WORK/restored" && cmp -s "$J/oracle" "$WORK/restored" && verify_foreign || return 1
    marker rolled-back
}
cleanup() {
    local p terminal=$1
    TERMINAL=$terminal
    # Never recursively remove the journal: terminal is the final file removed.
    for p in "$J"/* "$J"/.[!.]* "$J"/..?*; do
        exists "$p" || continue
        [ "$p" != "$J/$terminal" ] || continue
        rm -rf -- "$p" || return 1
    done
    if [ -n "$terminal" ]; then rm -f "$J/$terminal" || return 1; fi
    rmdir "$J"
}
recover() {
    exists "$J" || return 0
    ordinary_dir "$J" && [ -O "$J" ] || return 1
    local p name terminal= attrs
    attrs=$(ls -ld "$J") || return 1
    [ "${attrs%% *}" = drwx------ ] || return 1
    # Recognize only this engine's building/cleanup shapes, including mkdir ->
    # schema and last-marker -> rmdir windows. Unknown evidence is retained.
    for p in "$J"/* "$J"/.[!.]* "$J"/..?*; do
        exists "$p" || continue
        name=${p##*/}
        case "$name" in schema|prepared|committed|rolled-back)
            [ -f "$p" ] && [ ! -L "$p" ] && [ "$(<"$p")" = 1 ] || return 1;;
            schema.tmp|prepared.tmp|committed.tmp|rolled-back.tmp)
                [ -f "$p" ] && [ ! -L "$p" ] || return 1
                # Redirection can be interrupted before printf. An unpublished
                # empty marker has no state-transition authority.
                [ ! -s "$p" ] || [ "$(<"$p")" = 1 ] || return 1;;
            backup) ordinary_dir "$p" || return 1;;
            oracle|oracle.tmp|foreign|foreign.tmp|manifest|manifest.tmp) [ -f "$p" ] && [ ! -L "$p" ] || return 1;;
            *) return 1;;
        esac
    done
    if exists "$J/committed" && exists "$J/rolled-back"; then return 1; fi
    if exists "$J/committed"; then terminal=committed
    elif exists "$J/rolled-back"; then terminal=rolled-back
    elif exists "$J/prepared"; then
        check_marker schema && check_marker prepared || return 1
        rollback || { die "recovery required at $J; repeat bootstrap after fixing the filesystem error"; return 1; }
        terminal=rolled-back
    elif exists "$J/schema"; then check_marker schema || return 1
    else
        # Only the empty initial/cleanup directory or first schema temp is safe.
        for p in "$J"/* "$J"/.[!.]* "$J"/..?*; do
            exists "$p" || continue
            [ "$p" = "$J/schema.tmp" ] || return 1
        done
    fi
    cleanup "$terminal" || { die "${terminal:-not changed}/cleanup incomplete: $J; repeat request"; return 1; }
}
failed_transaction() {
    trap '' INT TERM
    if [ "${TERMINAL:-}" = committed ] || exists "$J/committed"; then die "applied/cleanup incomplete: $J; repeat request"; return 1; fi
    if [ "${TERMINAL:-}" = rolled-back ]; then die "restored/cleanup incomplete: $J; repeat request"; return 1; fi
    if exists "$J/prepared"; then
        if rollback; then
            cleanup rolled-back || { die "restored/cleanup incomplete: $J"; return 1; }
            die 'restored previous installation'
        else die "recovery required: $J; repeat bootstrap/request"; fi
    else
        recover || { die "not changed; inspect recovery evidence: $J"; return 1; }
        die 'not changed'
    fi
    return 1
}
transaction() {
    snapshot || return 1
    remove_managed || return 1
    if [ "$OP" != uninstall ]; then copy_stage || return 1; fi
    managed_ledger "$ROOT" > "$WORK/actual" || return 1
    if [ "$OP" = uninstall ]; then : > "$WORK/expected"
    else managed_ledger "$WORK/stage" > "$WORK/expected" || return 1; fi
    cmp -s "$WORK/expected" "$WORK/actual" && verify_foreign && marker committed || return 1
    cleanup committed || return 1
}
main() {
    parse "$@" || return 1
    dependencies || return 1
    # A sentinel preserves even trailing newlines through command substitution.
    ROOT=$(cd -P "$PROJECT" && printf '%s.' "$PWD") || return 1
    ROOT=${ROOT%.}
    WORK=$SELF_DIR/work
    mkdir "$WORK" || return 1
    lock && parents || return 1
    J=$ROOT/.opencode/.ris-install-transaction
    recover || { die "not changed; invalid/incomplete journal: $J; preserve evidence and use compatible bootstrap"; return 1; }
    TERMINAL=
    if exists "$ROOT/.opencode/.ris-version.tmp"; then die 'not changed: foreign .ris-version.tmp collision'; return 1; fi
    managed || return 1
    [ "$OP" != update ] || [ "${#PATHS[@]}" -gt 0 ] || { die 'no installation; use install'; return 1; }
    if [ "$OP" != uninstall ]; then acquire || { die 'not changed: package acquisition/validation failed'; return 1; }; fi
    if [ "$OP" = uninstall ] && [ "${#PATHS[@]}" = 0 ]; then
        printf 'RIS uninstall: %s source=%s skills=0 commands=0; already absent (offline no-op). Restart OpenCode; check git status.\n' "$ROOT" "$SOURCE"
        return 0
    fi
    trap 'failed_transaction; exit 1' INT TERM
    if ! transaction; then failed_transaction; return 1; fi
    trap - INT TERM
    printf 'RIS %s: %s source=%s revision=%s skills=%s commands=%s. Restart OpenCode; check git status.\n' "$OP" "$ROOT" "$SOURCE" "${SHA:-none}" "${#SKILLS[@]}" "${#COMMANDS[@]}"
}
self_cleanup() {
    local result=$?
    trap - EXIT
    if ! rm -rf -- "$SELF_DIR"; then
        die "engine cleanup incomplete: $SELF_DIR; installation outcome reported above; remove this temporary engine after inspection"
        result=1
    fi
    exit "$result"
}
if [ "${BASH_SOURCE[0]}" = "$0" ]; then
    # Re-exec through a private external copy; installed files can now disappear.
    SELF_DIR=$(mktemp -d /tmp/ris-install.XXXXXXXX) || exit 1
    cp -p -- "${BASH_SOURCE[0]}" "$SELF_DIR/engine" && chmod 700 "$SELF_DIR/engine" || { rm -rf "$SELF_DIR"; exit 1; }
    shopt -s execfail
    exec "$BASH" -c 'SELF_DIR=$1; shift; . "$SELF_DIR/engine" || exit 1; trap self_cleanup EXIT; main "$@"' ris-engine "$SELF_DIR" "$@"
    die 'could not execute temporary engine; not changed'
    rm -rf -- "$SELF_DIR"
    exit 1
fi
