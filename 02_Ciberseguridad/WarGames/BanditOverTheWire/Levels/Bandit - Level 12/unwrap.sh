#!/usr/bin/env bash
#
# unwrap.sh - Recursively unwrap a repeatedly compressed file.
# Written for OverTheWire Bandit Level 12, but works on any nested archive.
#
# Usage: ./unwrap.sh <file> [max_layers]
#
set -uo pipefail

readonly INPUT="${1:-}"
readonly MAX_LAYERS="${2:-30}"

if [[ -z "$INPUT" || ! -f "$INPUT" ]]; then
    echo "Usage: $0 <file> [max_layers]" >&2
    exit 1
fi

# --- Work in a disposable directory -----------------------------------------
# Never unpack an untrusted archive next to anything that matters: a malicious
# member named ../../etc/cron.d/x would escape the current directory.
WORKDIR="$(mktemp -d "${TMPDIR:-/tmp}/unwrap.XXXXXXXX")" || exit 1
echo "[*] Working directory: $WORKDIR"

cp -- "$INPUT" "$WORKDIR/layer_00"
cd "$WORKDIR" || exit 1

current="layer_00"
layer=0

# --- Main loop ---------------------------------------------------------------
# The loop bound is not decoration. If a layer is unrecognised and the file
# never changes, an unbounded loop spins forever. Anything driven by external
# data needs a hard stop.
while (( layer < MAX_LAYERS )); do

    filetype="$(file -b -- "$current")"
    printf '[%02d] %-20s %s\n' "$layer" "$current" "${filetype:0:60}"

    (( layer++ ))
    next="layer_$(printf '%02d' "$layer")"

    case "$filetype" in
        # ---- Terminal condition: plain text is the payload ------------------
        *"ASCII text"*|*"UTF-8"*text*)
            echo
            echo "[+] Plain text reached after $((layer-1)) layers."
            echo "----------------------------------------"
            cat -- "$current"
            echo "----------------------------------------"
            echo "[*] Files left in: $WORKDIR"
            exit 0
            ;;

        # ---- Single-stream compressors -------------------------------------
        # -c writes to stdout: no extension rename needed, input preserved.
        *"gzip compressed"*)   gunzip  -c -- "$current" > "$next" ;;
        *"bzip2 compressed"*)  bunzip2 -c -- "$current" > "$next" ;;
        *"XZ compressed"*)     xz     -dc -- "$current" > "$next" ;;
        *"Zstandard"*)         zstd   -dc -- "$current" > "$next" 2>/dev/null ;;

        # ---- Archives: output name is NOT predictable ----------------------
        # tar extracts under the name stored inside the archive, so the file
        # that appears has to be discovered, not assumed.
        *"tar archive"*)
            extract_dir="extract_$layer"
            mkdir -p "$extract_dir"
            tar -xf "$current" -C "$extract_dir" || { echo "[!] tar failed" >&2; exit 1; }

            # Expect exactly one member; more than one means this script's
            # single-chain assumption doesn't hold for this file.
            mapfile -t members < <(find "$extract_dir" -type f)
            if (( ${#members[@]} != 1 )); then
                echo "[!] Expected 1 file in archive, found ${#members[@]}:" >&2
                printf '    %s\n' "${members[@]}" >&2
                echo "[!] Inspect manually in $WORKDIR" >&2
                exit 1
            fi
            mv -- "${members[0]}" "$next"
            rmdir "$extract_dir" 2>/dev/null
            ;;

        *)
            echo "[!] Unhandled type: $filetype" >&2
            echo "[!] Stopped at $WORKDIR/$current" >&2
            exit 1
            ;;
    esac

    if [[ ! -s "$next" ]]; then
        echo "[!] Layer $layer produced an empty file - aborting." >&2
        exit 1
    fi

    current="$next"
done

echo "[!] Hit the $MAX_LAYERS layer limit without reaching plain text." >&2
echo "[!] Either the file is deeper than expected, or the loop is stuck." >&2
exit 1
