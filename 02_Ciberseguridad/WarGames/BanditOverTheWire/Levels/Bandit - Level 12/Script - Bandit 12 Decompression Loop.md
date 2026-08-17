---
tags: [bash, python, scripting, automation, compression, practice]
source: Bandit Level 12 — automation exercise
---

# Script - Bandit 12 Decompression Loop

Two implementations of the same task: unwrap a repeatedly compressed file until plain text is reached. Written **after** solving [[Bandit - Level 12]] by hand — automating a process not yet understood produces a script that can't be debugged.

Concepts: [[Linux - Nested Archives and Compression Layers]]

---

## The Problem Shape

The task cannot be a fixed sequence of commands, because **each layer's type determines the next step's tool**, and that type is unknown until the previous layer is removed. That makes it a loop with a branch:

```
identify → decompress → identify → ...  until plain text
```

Three properties drove every design decision:

1. **Output filenames are unpredictable** — `tar` extracts under the name stored inside the archive, `bunzip2` invents `.out` when it can't strip a suffix. Nothing can be assumed; it has to be discovered.
2. **`gunzip`/`bunzip2` consume their input, `tar` doesn't** — inconsistent state after each iteration.
3. **The loop needs a hard stop.** If a layer is misidentified and the data stops changing, an unbounded loop runs forever. Anything driven by external data needs an escape hatch.

---

## Bash version — `unwrap.sh`

```bash
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
```

```bash
./unwrap.sh data.txt          # after xxd -r, on the binary
./unwrap.sh <file> 50         # raise the layer limit
```

Wraps the same commands used manually, so the trace matches what the terminal showed step by step.

**Key decisions:**

```bash
gunzip  -c -- "$current" > "$next"
bunzip2 -c -- "$current" > "$next"
```
`-c` writes to stdout, which **skips the extension check** and preserves the input. Every `mv ... .gz` from the manual solve disappears. Understanding *why* the rename was needed is what makes it safe to drop.

```bash
mapfile -t members < <(find "$extract_dir" -type f)
if (( ${#members[@]} != 1 )); then ... fi
```
`tar` output is discovered by listing the extraction directory, never assumed — the exact mistake that cost time manually (`tar -xf next2.tar` when the file was `next2.out`). More than one member means the single-chain assumption doesn't hold, so it stops rather than guessing.

```bash
WORKDIR="$(mktemp -d "${TMPDIR:-/tmp}/unwrap.XXXXXXXX")"
```
Extraction happens in a disposable directory. A malicious archive member named `../../../etc/cron.d/backdoor` would otherwise write outside it.

```bash
set -uo pipefail
```
`-u` catches unset variables; `pipefail` makes a pipeline fail if **any** stage fails, not just the last. `-e` is deliberately omitted — the script handles its own error paths and wants control over them.

**Trace on the real file:**
```
[00] layer_00   gzip compressed data, was "data2.bin"
[01] layer_01   bzip2 compressed data, block size = 900k
[02] layer_02   gzip compressed data, was "data4.bin"
[03] layer_03   POSIX tar archive (GNU)
[04] layer_04   POSIX tar archive (GNU)
[05] layer_05   bzip2 compressed data, block size = 900k
[06] layer_06   POSIX tar archive (GNU)
[07] layer_07   gzip compressed data, was "data9.bin"
[08] layer_08   ASCII text
[+] Plain text reached after 8 layers.
```

---

## Python version — `unwrap.py`

```python
#!/usr/bin/env python3
"""
unwrap.py - Recursively unwrap a repeatedly compressed file.

Written for OverTheWire Bandit Level 12, but works on any nested archive.

Unlike the Bash version, this calls no external commands. It reads magic
numbers directly and uses the standard library's gzip, bz2, lzma and tarfile
modules, so the whole chain is handled in memory.

Usage:
    ./unwrap.py <file> [--max-layers N] [--verbose]
    ./unwrap.py data.txt --hexdump      # input is an xxd-style hex dump
"""

import argparse
import bz2
import gzip
import io
import lzma
import re
import sys
import tarfile

MAX_MEMBER_SIZE = 100 * 1024 * 1024  # 100 MB — decompression-bomb guard


def revert_hexdump(text: str) -> bytes:
    """Reverse an xxd-style hex dump back into raw bytes.

    Format: OFFSET: HH HH HH HH  ASCII
    The ASCII column must be discarded, and it can itself contain characters
    that look like hex, so slicing by column is unreliable. Splitting on the
    colon and then keeping only well-formed hex groups is robust.
    """
    out = bytearray()
    for line in text.splitlines():
        if ":" not in line:
            continue
        body = line.split(":", 1)[1]
        # Hex groups are 1-4 hex chars; the ASCII column is separated by 2+ spaces
        hex_part = re.split(r"\s{2,}", body.strip())[0]
        for group in hex_part.split():
            if re.fullmatch(r"[0-9a-fA-F]+", group) and len(group) % 2 == 0:
                out += bytes.fromhex(group)
    return bytes(out)


def identify(data: bytes) -> str:
    """Identify a format by its magic number.

    This is what `file` does: read the leading bytes, ignore the filename.
    A file's extension is a human convention and guarantees nothing.
    """
    if data[:2] == b"\x1f\x8b":
        return "gzip"
    if data[:3] == b"BZh":
        return "bzip2"
    if data[:6] == b"\xfd7zXZ\x00":
        return "xz"
    if data[257:262] == b"ustar":       # tar's magic sits at offset 257
        return "tar"
    if is_text(data):
        return "text"
    return "unknown"


def is_text(data: bytes) -> bool:
    """Heuristic: no null bytes and decodable as UTF-8."""
    if b"\x00" in data[:8192]:
        return False
    try:
        data[:8192].decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False


def untar(data: bytes) -> bytes:
    """Extract a single-member tar archive, in memory.

    Never uses extractall(): a member named ../../etc/cron.d/x would write
    outside the target directory (Zip Slip / CVE-2007-4559). Reading the
    member object directly sidesteps the filesystem entirely.
    """
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        members = [m for m in tar.getmembers() if m.isfile()]
        if len(members) != 1:
            raise ValueError(
                f"expected 1 file in archive, found {len(members)}: "
                f"{[m.name for m in members]}"
            )
        member = members[0]
        if member.size > MAX_MEMBER_SIZE:
            raise ValueError(f"member is {member.size} bytes — refusing (bomb guard)")
        extracted = tar.extractfile(member)
        if extracted is None:
            raise ValueError(f"could not read member {member.name}")
        return extracted.read()


DECOMPRESSORS = {
    "gzip": gzip.decompress,
    "bzip2": bz2.decompress,
    "xz": lzma.decompress,
    "tar": untar,
}


def unwrap(data: bytes, max_layers: int = 30, verbose: bool = True) -> bytes:
    """Peel compression layers until plain text is reached.

    The layer cap is essential: if a format is misidentified and the data
    stops changing, an unbounded loop never terminates.
    """
    for layer in range(max_layers):
        kind = identify(data)

        if verbose:
            print(f"[{layer:02d}] {kind:<10} {len(data):>10,} bytes", file=sys.stderr)

        if kind == "text":
            return data
        if kind == "unknown":
            raise ValueError(
                f"unrecognised format at layer {layer}; "
                f"first bytes: {data[:16].hex(' ')}"
            )

        try:
            data = DECOMPRESSORS[kind](data)
        except Exception as exc:
            raise ValueError(f"failed to decompress {kind} at layer {layer}: {exc}") from exc

    raise ValueError(f"hit the {max_layers}-layer limit without reaching text")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file", help="file to unwrap")
    parser.add_argument("--hexdump", action="store_true",
                        help="treat the input as an xxd-style hex dump")
    parser.add_argument("--max-layers", type=int, default=30)
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="suppress the per-layer trace")
    args = parser.parse_args()

    try:
        with open(args.file, "rb") as fh:
            data = fh.read()
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    # Auto-detect a hex dump so --hexdump is usually unnecessary
    if args.hexdump or re.match(rb"^[0-9a-fA-F]{8}: ", data[:10]):
        if not args.quiet:
            print("[*] Input looks like a hex dump — reverting", file=sys.stderr)
        data = revert_hexdump(data.decode("ascii", errors="replace"))

    try:
        result = unwrap(data, args.max_layers, verbose=not args.quiet)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not args.quiet:
        print("-" * 40, file=sys.stderr)
    sys.stdout.write(result.decode("utf-8", errors="replace"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

```bash
./unwrap.py data.txt          # hex dump auto-detected, no xxd needed
./unwrap.py file -q           # password only, no trace
```

Calls **no external commands**. Reads magic numbers directly and uses `gzip`, `bz2`, `lzma` and `tarfile` from the standard library, holding everything in memory.

**Key decisions:**

```python
if data[:2] == b"\x1f\x8b":      return "gzip"
if data[:3] == b"BZh":           return "bzip2"
if data[257:262] == b"ustar":    return "tar"
```
This *is* what `file` does — read the leading bytes, ignore the name. Note tar's magic at **offset 257**, after the first member's header.

```python
members = [m for m in tar.getmembers() if m.isfile()]
extracted = tar.extractfile(member)
```
Never `extractall()`. A member named `../../etc/passwd` escapes the target directory — **CVE-2007-4559**, unpatched in Python's `tarfile` for fifteen years and only addressed in 3.12. Reading the member object avoids the filesystem entirely.

```python
if member.size > MAX_MEMBER_SIZE:
    raise ValueError(f"member is {member.size} bytes — refusing (bomb guard)")
```
Decompression-bomb guard. `42.zip` is 42 KB and expands to 4.5 PB, nested exactly like this level.

```python
hex_part = re.split(r"\s{2,}", body.strip())[0]
```
Reverting the hex dump can't slice by fixed column, because the ASCII column may itself contain hex-looking characters. Splitting on 2+ spaces separates the hex from the ASCII reliably.

---

## Comparison

| | Bash | Python |
|---|---|---|
| Dependencies | `file`, `gzip`, `bzip2`, `tar`, `xxd` | standard library only |
| Where data lives | temp files on disk | memory |
| Format detection | delegated to `file` | own magic-number table |
| Hex dump | needs `xxd -r` first | built in, auto-detected |
| Best for | quick work on a box you just SSH'd into | repeatable tooling, integration |

**Bash wins** when you're already in a shell on an unfamiliar host with no Python available. **Python wins** for anything reused, tested, or integrated — better error handling, no subprocess overhead, no temp files, and precise control over the security guards.

The general rule: **shell for gluing existing tools, a real language once there's state, error handling or logic to manage.** This task sits right on that boundary, which is why it's worth writing both.

---

## Limitations

- Assumes a **single chain** — one file per archive. Both stop with a clear error otherwise.
- Bash version needs `xxd -r` run first; Python handles the hex dump itself.
- No support for `zip`, `7z`, `rar` or `cpio`. Adding a format is one `case` branch or one dict entry.
- The Python bomb guard checks tar member sizes only; a gzip bomb would still decompress into memory. A production version would stream with a size cap.

---

## What This Exercise Teaches Beyond Bandit

The *inspect → branch → act → re-inspect* loop is the shape of real unpacking work: a malware delivery chain (`.eml` → `.zip` → `.iso` → `.lnk`), a firmware image, a set of rotated logs. `binwalk` is essentially this loop generalised — scanning for every known magic number at every offset.

And the reflex worth keeping from writing it: **automate second.** Doing it by hand first is what surfaced the three awkward cases — unpredictable output names, inconsistent input consumption, and the need for a loop bound. None of them were visible from the problem statement, and a script written before the manual solve would have hit all three as mysterious bugs.
