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
