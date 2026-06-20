---
tags: [linux, shell, security, argument-injection, practice]
source: Bandit Level 1 + LabEx — Handling Dash-Prefixed Filenames
---

# Linux - Argument Parsing, Special Filenames & Injection Risks

## The Core Problem

Command-line tools don't get a clean list of "filenames" and "options" handed to them — they get a flat array of strings (`argv`), and *each program's own argument parser* decides what's an option and what's a filename, almost always using the same inherited convention: **anything starting with `-` is treated as an option**, not a filename, unless told otherwise.

This means the filesystem will happily let you create a file called `-rf` or `-l` or just `-`, but the moment you try to reference it normally, the command reads it as a flag instead of a target:

```bash
cat -file.txt     # cat tries to parse "-file.txt" as a cluster of options: -f, -i, -l, -e...
rm -file.txt      # same problem — rm sees options, not a filename
```

This is **not a shell bug or a filesystem restriction** — bash lets you create and reference these filenames just fine. It's each individual program's `getopt`-style parser making an assumption that breaks the moment a filename happens to start with `-`.

## The Lone Dash: A Second, Different Convention

A filename that is *exactly* `-` (a single dash, nothing else) hits a **different** convention on top of the option-parsing one: by long-standing Unix tradition, many tools (`cat`, `tar`, `curl`, `openssl`, `gpg`...) treat a bare `-` argument as shorthand for **"read from stdin"** or **"write to stdout"** instead of a real file.

So `cat -` doesn't error out the way `cat -file.txt` does — it succeeds, but reads from your keyboard input instead of opening the file named `-`. No error message, just unexpected behavior: the terminal appears to hang, waiting for you to type something. This is a distinct trap from the option-parsing one above, and it's exactly the shape of the file Bandit Level 1 hands you.

## Disambiguation Techniques

Three reliable ways to tell a command "the next thing is a filename, not an option," in increasing order of explicitness:

```bash
# 1. The -- separator (POSIX convention — but NOT universal, see warning below)
rm -- -file.txt
cp -- -file.txt /dest/

# 2. Explicit relative path — there's no ambiguity once it doesn't start with -
cat ./-file.txt
cat ./-

# 3. Absolute path — equally unambiguous
cat /home/user/-file.txt
```

> ⚠️ **`--` is opt-in per program, not a shell guarantee.** Most GNU coreutils (`rm`, `cp`, `mv`, `grep`) honor `--` as "end of options." But `cat` is a notable exception for the *bare* `-` case specifically: even with `--` in front, `cat -- -` still treats the lone `-` as "read from stdin" in many implementations (confirmed firsthand on Bandit Level 1 — `cat -- -` hung waiting for keyboard input, exactly like `cat -` alone). For a file literally named `-`, the relative or absolute path (`./-` or `/full/path/-`) is the technique that reliably works across tools. `--` is still worth trying first for *dash-prefixed* names (`-file.txt`) on most commands — just don't assume it overrides the bare-dash stdin convention on every tool.

**Common misconception**: quoting does *not* fix this. `cat "-file.txt"` still gets handed `-file.txt` as the argument, and `cat`'s own parser still sees a leading dash. Quoting only protects against the *shell's* word-splitting and glob expansion — it does nothing about how the called program interprets its own arguments. The fix has to happen via `--` (where supported), `./`, or an absolute path — and when in doubt, the explicit path is the one technique that works everywhere, every time.

## Why This Is a Security Topic, Not Just a Syntax Quirk

This exact ambiguity is a real, named class of vulnerability: **argument injection** (CWE-88), sometimes called **wildcard injection** when it happens through glob expansion rather than a literal filename.

The pattern: a script or scheduled job runs a command against a wildcard in a directory that's writable by someone untrusted —
```bash
tar -czf backup.tar.gz *
```
If an attacker can drop a file with a crafted name into that directory before the job runs, the shell expands `*` into the file list *before* `tar` ever sees it — and a filename like `--checkpoint=1` or `--checkpoint-action=exec=sh\ shell.sh` gets handed to `tar` as if it were a legitimate flag. The wildcard silently became a way to inject arbitrary options into a privileged command. The same class of issue applies to `chown`, `rsync`, `zip`, and other tools that accept wildcards and have "dangerous" flags.

This is exactly why the disambiguation habit matters beyond Bandit: any script that loops over user-writable filenames without `--` or explicit paths is a potential privilege-escalation vector — relevant later for [[Permissions & Process Management]] and for pentesting/privesc work (HTB, eJPT).

## Key Takeaway
"It's just syntax I don't know yet" is the right read on this — it's a documented, learnable convention, not an arbitrary trick. Once internalized, `--` and explicit paths become reflexive, the same way `pwd`-before-any-relative-path already has.
