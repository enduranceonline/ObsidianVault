---
tags: [linux, shell, binary, forensics, malware-analysis, practice, security]
source: Bandit Level 9 + general reference
---

# Linux - Extracting Strings from Binaries

> Related: [[Linux - File Type Detection]] covers identifying *what* a file is. This note covers reading *inside* one when it isn't text.

---

## The Core Idea

Text tools assume text. `grep`, `sort`, `cut`, `awk` all work on lines delimited by `\n` bytes — a model that breaks the moment the input is binary, because `\n` (`0x0A`) then appears at random positions with no structural meaning.

==`strings`== bridges that gap. It scans a file byte by byte looking for runs of **printable characters** and prints each run as its own line, discarding everything else. It doesn't parse or understand the file format — it just harvests whatever happens to be readable.

That crude approach is exactly why it's useful: it works on **any** file type, including ones nobody has written a parser for. Executables, memory dumps, firmware images, disk fragments, proprietary formats, corrupted files.

```bash
strings binary_file              # printable runs, one per line
strings binary_file | grep -i password
```

---

## The Default That Bites: Minimum Length

By default `strings` only reports runs of **4 or more** printable characters. Anything shorter is treated as coincidental noise — and in a real binary, most short runs genuinely are.

```bash
strings -n 8 file      # only runs of 8+ — much less noise, good for triage
strings -n 3 file      # shorter runs too — catches things the default misses
```

**This cuts both ways.** Raising `-n` is the fastest way to make a noisy binary readable. Lowering it matters when what you're hunting is short: a 3-character file extension, a two-letter command code, a short mutex name. If a string you expect to be present doesn't show up, the minimum length is the first thing to check.

---

## Encoding: The Flag Most People Never Learn

`strings` defaults to **7-bit ASCII, one byte per character**. Windows binaries overwhelmingly store text as **UTF-16LE** ("wide chars"), where every ASCII character is followed by a `0x00` byte. That null byte breaks the printable run, so the default scan misses those strings entirely.

```bash
strings -e l file.exe     # 16-bit little-endian (UTF-16LE) — Windows default
strings -e b file         # 16-bit big-endian
strings -e s file         # single-7-bit-byte (the default)
strings -e S file         # single-8-bit-byte — includes extended/accented chars
```

**Practical consequence:** running plain `strings` on a Windows executable and concluding "there are no interesting strings" is a false negative. Windows binaries need both passes:

```bash
strings suspicious.exe        > ascii.txt
strings -e l suspicious.exe   > wide.txt
```

Missing this is one of the most common mistakes in first-pass malware triage.

---

## Offsets — Locating What You Found

```bash
strings -t x file      # prefix each string with its offset in hexadecimal
strings -t d file      # offset in decimal
strings -t o file      # offset in octal
```

Once you have the offset, you can go back and read the surrounding bytes — which often carry the structure the string belonged to (a function's parameters, a config block, an adjacent field):

```bash
strings -t d file | grep 'evil.com'      # → 48312 evil.com
dd if=file bs=1 skip=48200 count=400 2>/dev/null | xxd
```

This is the workflow that turns "there's a domain in here" into "here's the config structure that domain sits in".

Other useful flags: `-f` prefixes each line with the filename (essential when scanning many files at once), and `-a` scans the whole file rather than only the initialized-data sections of an object file.

---

## Real-World Applications

### First pass of static malware analysis
Before any disassembler, before any sandbox, `strings` is the opening move — it costs one second and frequently answers the question outright:

```bash
strings -n 8 sample.bin | grep -Ei 'http|https|\.com|\.net|\.ru|\.onion'
strings sample.bin | grep -E '([0-9]{1,3}\.){3}[0-9]{1,3}'      # hardcoded IPs
strings -e l sample.exe | grep -Ei 'HKEY|CurrentVersion\\Run'   # persistence via registry
strings sample.bin | grep -Ei 'cmd\.exe|powershell|-enc|schtasks|vssadmin'
```

What routinely falls out: ==C2== domains and IPs, User-Agent strings, ransom-note text, the mutex name the sample uses to avoid reinfecting a host, hardcoded credentials, and the developer's **PDB path** — an absolute path left by the compiler that can expose a username, project name and build environment. These become ==IoCs== (Indicators of Compromise) that get pushed straight into a SIEM or EDR blocklist. Connects directly to the Kasiu material on Domain 3 (malware/ransomware protection) and Domain 9 (DFIR).

### Absence of strings is itself a signal
A legitimate binary contains hundreds or thousands of readable strings — library names, error messages, format strings. A file that yields **almost nothing** is very likely **packed or encrypted**, with its real content unpacked into memory only at runtime.

```bash
strings sample.exe | wc -l      # 40 lines on a 2 MB executable → strongly suspicious
```

Low string count is a recognised heuristic for packing, and often the trigger to escalate from static analysis to a sandbox detonation.

### Memory dump and RAM forensics
A process memory dump or full RAM capture is binary with no useful file structure, but it holds decrypted data that never touches disk:

```bash
strings -n 6 memdump.raw | grep -Ei 'password|passwd|token|Authorization: Bearer'
strings -e l memdump.raw | grep -i 'https://'
```

This is how credentials, session tokens, chat fragments and unencrypted copies of encrypted-at-rest data get recovered during incident response — and why *unpacked in memory* means every packer eventually loses.

### Firmware and IoT analysis
Router, camera and IoT firmware images are full of hardcoded secrets:

```bash
strings firmware.bin | grep -Ei 'admin|root|passwd|telnet|ssh|BusyBox'
```

Undocumented default credentials in firmware are a recurring class of finding, and `strings` on a downloaded image is often the whole methodology.

### Triage of a suspicious document
Before opening anything, check what it says about itself:

```bash
strings -n 6 invoice.pdf | grep -Ei 'JavaScript|OpenAction|Launch|/URI|EmbeddedFile'
```

`/OpenAction` plus `/JavaScript` in a PDF that claims to be an invoice is a decision made without ever rendering the file.

### Recovering text from a corrupted file
When a document is damaged past the point where its application can open it, the file format is broken but the raw text usually survives:

```bash
strings -n 4 corrupted.docx > recovered.txt
```

Formatting is lost, content generally isn't.

---

## Limitations — Where `strings` Stops Working

**It has no concept of context.** Every result is a candidate, not a finding. A domain in the output might be a C2 server or a certificate authority the binary legitimately validates against. `strings` narrows the search space; it doesn't conclude anything.

**Attackers know it exists.** String obfuscation — XOR encoding, stack strings assembled character by character at runtime, encrypted blobs decoded in memory — is standard practice in modern malware precisely to defeat this. **Empty output proves nothing.** It only means the strings aren't stored in plaintext, which is itself informative (see the packing heuristic above).

**Encoding assumptions cause false negatives.** Covered above: always run the `-e l` pass on Windows binaries.

**It's a first pass, never the analysis.** `strings` generates hypotheses. Disassembly, dynamic analysis and sandboxing test them.

---

## Related Tools

| Tool | Use |
|---|---|
| `strings` | printable runs, no structure |
| `xxd` / `hexdump -C` | full hex + ASCII dump — see the actual bytes and their offsets |
| `file` | identify the format by magic number ([[Linux - File Type Detection]]) |
| `binwalk` | find and extract embedded files inside a blob (firmware, images) |
| `grep -a` | force text mode on binary — works, but returns whole binary lines |

`grep -a` vs `strings` is the distinction Bandit Level 9 exists to teach. `grep -a` **finds** the match; `strings` makes it **readable**. On that level both technically located the password — only one of them displayed it in a form a human could use.

---

## Key Takeaway

When a text tool reports binary input, forcing it through (`-a`) treats the symptom. **Converting the input to text first is the fix.** `strings` is that conversion, and it's the reason a completely opaque file can still be triaged in seconds.

Beyond Bandit, it's the cheapest high-yield command in security work: the first thing run against an unknown executable, a memory capture, or a firmware image. It rarely produces the final answer, but it very often produces the question worth asking next.
