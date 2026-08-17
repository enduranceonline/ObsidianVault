---
tags: [linux, shell, compression, forensics, malware-analysis, practice, security]
source: Bandit Level 12 + general reference
---

# Linux - Nested Archives and Compression Layers

> Related: [[Linux - File Type Detection]] covers identifying a single file. This note covers what happens when the answer is *another file*, several times over.

---

## Archiving vs Compressing — Two Different Jobs

Constantly conflated, and the distinction explains why Unix tools chain the way they do.

| | Archiving | Compressing |
|---|---|---|
| Job | Bundle many files into one stream, preserving names, permissions, timestamps | Shrink one stream of bytes |
| Tool | `tar`, `cpio` | `gzip`, `bzip2`, `xz`, `zstd` |
| Filenames? | Yes — that's the point | `gzip` stores one, optionally; `bzip2` stores none |

`gzip` compresses **a single stream** and knows nothing about directories. `tar` bundles **many files with metadata** and compresses nothing. `.tar.gz` is both, chained — and the order matters: tar first, then compress the resulting archive, which is why `gzip` on a tarball compresses across file boundaries and achieves better ratios than `zip` (which compresses each member separately).

This is also why `zip` exists as a single tool on Windows: it does both jobs at once, at the cost of that cross-file compression.

---

## Magic Numbers — What a File Actually Is

Nearly every format begins with a fixed byte signature. `file` reads these; it never trusts the extension.

| Bytes (hex) | ASCII | Format |
|---|---|---|
| `1f 8b` | | gzip |
| `42 5a 68` | `BZh` | bzip2 |
| `fd 37 7a 58 5a` | `7zXZ` | xz |
| `28 b5 2f fd` | | zstd |
| `50 4b 03 04` | `PK` | zip / docx / xlsx / jar / apk |
| `75 73 74 61 72` at offset 257 | `ustar` | tar |
| `7f 45 4c 46` | `.ELF` | Linux executable |
| `4d 5a` | `MZ` | Windows PE executable |
| `25 50 44 46` | `%PDF` | PDF |
| `89 50 4e 47` | `.PNG` | PNG |

Reading them by hand:
```bash
head -c 16 unknown | xxd
file unknown
```

Two consequences worth internalising:

**Renaming changes nothing.** A tar archive called `photo.jpg` is still a tar archive, and `gzip` will refuse it with `not in gzip format` because it read the bytes.

**`tar`'s signature sits at offset 257**, not offset 0 — the first 257 bytes are the header of the first member file. That's why a tarball's opening bytes look like a filename rather than a magic string.

---

## The Extension Requirement

`gunzip` and `bunzip2` check the filename before doing anything, and they differ:

```bash
gunzip stage1
# → gzip: stage1: unknown suffix -- ignored          REFUSES

bunzip2 next2
# → bunzip2: Can't guess original name for next2 -- using next2.out
#   WARNS but decompresses, inventing an output name
```

The check exists so the tool knows what to name the output and doesn't overwrite something unintended. It is **not** required to read the data.

`-c` (`--stdout`) bypasses it entirely, writes to stdout, and preserves the input — the correct form in scripts:

```bash
gunzip -c  input > output
bunzip2 -c input > output
xz -dc     input > output
zstd -dc   input > output
```

`zcat`, `bzcat` and `xzcat` are shorthands for the same thing.

---

## Behaviour Differences That Break Loops

| | Deletes input? | Output name |
|---|---|---|
| `gunzip file.gz` | **yes** | `file` (suffix stripped) |
| `bunzip2 file.bz2` | **yes** | `file` (or `file.out` if no suffix) |
| `gunzip -c` / `bunzip2 -c` | no | wherever stdout goes |
| `tar -xf file.tar` | no | **the names stored inside the archive** |

`tar`'s output name is the one that breaks naive automation: it cannot be predicted from the input. After every extraction, list the directory rather than assuming:

```bash
tar -xf archive.tar && ls -lt | head
tar -tf archive.tar          # list contents WITHOUT extracting — safer
```

---

## Safety: Never Extract Blindly

```bash
tar -tf  unknown.tar          # list before extracting
unzip -l unknown.zip
```

Two real attack classes make this a habit rather than a nicety:

**Path traversal (Zip Slip).** An archive member named `../../../../etc/cron.d/backdoor` writes outside the extraction directory. Modern GNU `tar` strips leading `/` and refuses `..` by default, but older versions and many language libraries (Python's `tarfile` before 3.12, various Java and Node unzip packages) do not. CVE after CVE has come from this.

**Decompression bombs.** A few hundred kilobytes expanding to petabytes, filling the disk and taking the host down. `42.zip` is the canonical example — 42 KB, 4.5 PB unpacked, and deliberately nested exactly like this Bandit level. Defences: check the declared size first, extract inside a container or a size-limited filesystem, and cap the number of layers.

Always extract untrusted archives into a fresh, empty, disposable directory.

---

## Real-World Applications

### Malware sample unpacking
Delivery chains are deliberately nested to defeat scanners and mail filters: an `.eml` containing a password-protected `.zip` containing an `.iso` containing an `.lnk` that pulls a `.dll`. The workflow is identical to this level — `file`, unwrap, `file` again — and every layer is a decision point.

```bash
file sample
7z l sample            # list, don't extract
binwalk -e firmware.bin  # find and extract embedded archives automatically
```

`binwalk` is the specialised version of this loop: it scans a blob for **every** known magic number at **any** offset and extracts what it finds, which is how embedded filesystems inside firmware images get pulled apart.

### Compressed logs in incident response
Rotated logs stack up as `.gz` and `.bz2`. Searching them without unpacking to disk:

```bash
zgrep 'Failed password' /var/log/auth.log.*.gz
zcat /var/log/nginx/access.log.*.gz | awk '{print $1}' | sort | uniq -c | sort -rn | head
```

`zgrep`/`zcat` decompress on the fly, which matters when the disk is nearly full or the evidence must not be modified. Pairs with the pipeline from [[Linux - Sorting and Deduplication]].

### Office documents are zip archives
`.docx`, `.xlsx`, `.pptx` all begin with `PK` — they are zip containers of XML. Malicious macros can be examined without opening the document in Office:

```bash
unzip -l suspicious.docx
unzip -p suspicious.docx word/document.xml | head -c 2000
```

`.jar`, `.apk` and `.war` are the same trick in the Java and Android worlds.

### Exfiltration staging
Attackers commonly `tar czf` a directory of stolen data before transferring it. A large, recently created archive in `/tmp`, `/dev/shm` or a web root is a strong indicator:

```bash
find /tmp /dev/shm /var/www -type f \( -name '*.tar*' -o -name '*.zip' -o -name '*.7z' \) -mmin -1440 2>/dev/null -ls
```

Uses the time and type tests from [[Linux - find Command]].

### Backup verification
```bash
tar -tzf backup.tar.gz > /dev/null && echo "archive intact"
gzip -t backup.gz && echo "checksum OK"
```
Testing without extracting confirms integrity cheaply. Kasiu Domain 11 (BCP/DRP) makes the point that an untested backup is not a backup — this is the one-line version of that test.

---

## Key Takeaway

Unwrapping nested data is a **loop, not a sequence**: each layer's identity determines the next layer's tool, so the operation has to be *inspect → branch → act → re-inspect* rather than a fixed set of commands.

`file` and magic numbers are what make the inspection reliable, because filenames carry no guarantee. That's the reusable skill — the same loop applies to a malware delivery chain, a firmware image, a rotated log directory or an Office document, and in every one of those the extension is the least trustworthy piece of information available.
