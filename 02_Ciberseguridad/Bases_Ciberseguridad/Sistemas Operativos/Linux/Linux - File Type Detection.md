---
tags: [linux, shell, file-types, practice]
source: Bandit Level 4
---

# Linux - File Type Detection

## The Core Idea

Linux doesn't use file extensions to know what kind of content a file holds — `.txt` is a human convention, not something the OS enforces (already noted in [[Linux - Command Line Reference]] under the `file` command). That means a file can be named anything and contain anything; the only way to know what's actually inside is to look at the content itself.

This matters in practice because **a command running without an error message is not the same as a command finding the right thing.** `cat` will happily print raw binary bytes to your terminal — garbled symbols, control characters, broken formatting — without ever calling that an "error." From the shell's point of view, it did exactly what was asked: read the file, write its bytes to stdout. Whether those bytes make sense to a human is a separate question entirely.

## `file` — Identifying Content by Signature

The `file` command doesn't trust extensions or names — it inspects the actual bytes at the start of a file (its "magic number" / signature) to guess the real type.

```bash
file document.txt        # e.g. "ASCII text"
file image.png           # e.g. "PNG image data, 800 x 600"
file ./-file04           # e.g. "data" — unstructured binary, no recognizable format
```

`data` as a result isn't an error — it's `file`'s honest answer when content doesn't match any known text or format signature. It's the expected result for random/binary noise, exactly the kind of decoy content Bandit Level 4 uses.

## Checking Many Files at Once

Combine `file` with a wildcard to scan a whole batch in one command instead of checking files one by one:

```bash
file ./-file*
```

Each matching filename gets expanded by the shell before `file` ever runs (see [[Linux - Argument Parsing and Special Filenames]] for how `./` neutralizes the leading-dash problem on every one of them at once) — the result is a type report for all ten files in a single pass, instead of ten separate manual checks.

## Key Takeaway

When a command "works" but the output looks wrong, the instinct should be to question *what* was actually found, not just whether the command errored. `file` is the fast way to settle that question before spending time reading something that was never meant to be read.
