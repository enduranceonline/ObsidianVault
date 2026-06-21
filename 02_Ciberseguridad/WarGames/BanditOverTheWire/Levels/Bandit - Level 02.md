---
tags: [linux, bandit, wargame, shell, practice]
source: OverTheWire Bandit — Level 2
---

# Bandit - Level 02

## Goal
The password for the next level is stored in a file with spaces in its name, in the home directory of `bandit2`.

## Connection
```bash
ssh -p 2220 bandit2@bandit.labs.overthewire.org
```
Use the password retrieved at the end of [[Bandit - Level 01]].

## Concepts
Same family of problem as Level 1 — an unconventional filename — but a different mechanism: this time it's **word splitting**, not option parsing. The filename here combines *two* issues at once: a leading `--` and embedded spaces. Full breakdown, including the spaces-specific section added after this level: [[Linux - Argument Parsing and Special Filenames]].

## Solution Approach
```bash
ls
# --spaces in this filename--

cat ./--spaces\ in\ this\ filename--
```
The `./` defuses the leading-dash-as-option problem (same fix as Level 1). The backslash before each space stops bash from splitting the filename into multiple arguments. Both fixes were needed together, applied correctly on the first attempt.

## Points of Friction
None — solved directly. The `./` habit from Level 1 carried over automatically, and the spaces were escaped correctly on the first try.

## Key Takeaway
Unconventional filenames in Linux aren't all the same problem wearing different clothes — leading dashes break *option parsing*, spaces break *word splitting*. Same general defense (be explicit, don't let the shell guess), two different reasons why guessing goes wrong. Tab-completion is the practical habit to build going forward — it sidesteps manual escaping entirely.

## Next
`ssh -p 2220 bandit3@bandit.labs.overthewire.org` using the password found above.

---
◀ Previous: [[Bandit - Level 01]] · Next ▶ [[Bandit - Level 03]]
