---
tags: [linux, bandit, wargame, shell, practice]
source: OverTheWire Bandit — Level 3
---

# Bandit - Level 03

## Goal
The password for the next level is stored in a hidden file inside the `inhere` directory, in the home of `bandit3`.

## Connection
```bash
ssh -p 2220 bandit3@bandit.labs.overthewire.org
```
Use the password retrieved at the end of [[Bandit - Level 02]].

## Concepts
No new concept — this level is a direct application of `ls -a` (already covered in [[Linux - Command Line Reference]]): files starting with `.` are hidden by default and don't show with a plain `ls`. The filename here (`...Hiding-From-You`) starts with three literal dots, which is just a hidden filename with an unusual name — not a special shell token like `.` (current dir) or `..` (parent dir).

## Solution Approach
```bash
cd inhere
ls -la              # -a reveals the hidden file
cat ...Hiding-From-You
```

## Points of Friction
None — solved directly on the first attempt.

## Key Takeaway
Confirms `ls -a` as a reflex for any "I know there's something here but I can't see it" situation — the most common reason a file seems to not exist is simply that it's hidden, not that it's actually missing.

## Next
`ssh -p 2220 bandit4@bandit.labs.overthewire.org` using the password found above.

---
◀ Previous: [[Bandit - Level 02]] · Next ▶ [[Bandit - Level 04]]
