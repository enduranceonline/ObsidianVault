---
tags: [linux, bandit, wargame, shell, practice]
source: OverTheWire Bandit — Level 7
date_completed: 2026-06-22
---

# Bandit - Level 07

## Goal
The password for the next level is stored in `data.txt`, next to the word **millionth**.

## Connection
```bash
ssh -p 2220 bandit7@bandit.labs.overthewire.org
```
Use the password retrieved at the end of [[Bandit - Level 06]].

## Concepts
`grep` searches for a pattern **inside the content** of what it receives — whether that's a file passed as an argument or data piped into it from another command. The key distinction this level forces: `grep` filters lines, not filenames.

## Attempts

```bash
# Tried to locate the file first — unnecessary, it was already in the home directory
find / -name data.txt 2>/dev/null

# Piped find output into grep — grep was filtering file *paths*, not file *content*
find / -name data.txt | grep 'millionth' 2>/dev/null   # returned nothing

# Same mistake, different stderr placement — still filtering paths
find / -name data.txt 2>/dev/null | grep 'millionth'   # returned nothing
```

## Solution

```bash
ls               # data.txt is right here in the home directory
cat data.txt | grep 'millionth'
# → millionth    VR1ljMayciFxbnUokuQmJFw6QC9VKtub
```

Or equivalently, passing the file directly to grep:
```bash
grep 'millionth' data.txt
```

## Points of Friction
Reached for `find` first — unnecessary since `data.txt` was already in the home directory. Then piped `find` output into `grep`, which filtered file *path names* for the word "millionth" rather than the file's content. The fix was simply `cat data.txt | grep 'millionth'`, which pipes the file's content into grep instead.

## Key Takeaway
==`grep`== filters the **content of lines**, not filenames or paths. When you pipe `find` into `grep`, grep is searching through the list of paths that `find` prints — not inside those files. To search inside a file: either `grep 'pattern' file.txt` or `cat file.txt | grep 'pattern'`. Both are equivalent; the direct form is faster.

## Next
```bash
ssh -p 2220 bandit8@bandit.labs.overthewire.org
```

---
◀ Previous: [[Bandit - Level 06]] · Next ▶ [[Bandit - Level 08]]
