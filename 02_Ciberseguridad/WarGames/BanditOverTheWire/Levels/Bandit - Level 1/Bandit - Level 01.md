---
tags: [linux, bandit, wargame, shell, practice]
source: OverTheWire Bandit — Level 1
---

# Bandit - Level 01

## Goal
The password for the next level is stored in a file called `-` in the home directory of `bandit1`.

## Connection
```bash
ssh -p 2220 bandit1@bandit.labs.overthewire.org
```
Use the password retrieved at the end of [[Bandit - Level 00]].

## Concepts
This level is pure shell syntax, not exploitation — the kind of thing where, as you put it, "either you know it or you don't." Full conceptual breakdown lives in [[Linux - Argument Parsing and Special Filenames]]; the short version:

A file named exactly `-` collides with a long-standing Unix convention: a bare `-` argument means "read from stdin" to many tools, `cat` included. So the naive `cat -` doesn't error — it just hangs, waiting for keyboard input, because it's reading from your terminal instead of opening the file.

## Solution Approach
Two of the three standard techniques resolved this cleanly; the third revealed a real exception worth knowing:
```bash
cat ./-                  # ✅ works — explicit relative path
cat /home/bandit1/-      # ✅ works — explicit absolute path
cat -- -                 # ❌ hangs — see note below
```
`cat -- -` did **not** work as expected — it hung waiting for keyboard input instead of printing the file. This isn't a mistake, it's a genuine quirk: `--` isn't honored identically by every tool, and `cat` specifically still treats a bare `-` as "read from stdin" even after `--`. The explicit path (`./-` or the absolute path) is the technique that actually works for a file named *exactly* `-`. Full explanation, now corrected with this finding: [[Linux - Argument Parsing and Special Filenames]].

## Points of Friction
- Tried `cat /home/bandit1/-.txt` first, assuming the file might have an extension — it doesn't; the filename is literally just `-`, nothing appended.
- `cat -- -` hung (had to `Ctrl+C` out) instead of erroring or working — confirmed `--` doesn't override `cat`'s bare-dash-means-stdin convention. Documented as a correction to the general note, since the original draft assumed `--` would work universally.

## Key Takeaway
Quoting the filename (`cat "-"`) would *not* have worked — that's a common trap. Quotes only stop the shell from doing word-splitting/globbing; they don't change what `cat` itself sees once it receives the argument. The fix has to be `--`, a relative path, or an absolute path — see the linked note for why.

## Next
`ssh -p 2220 bandit2@bandit.labs.overthewire.org` using the password found above.

---
◀ Previous: [[Bandit - Level 00]] · Next ▶ [[Bandit - Level 02]]
