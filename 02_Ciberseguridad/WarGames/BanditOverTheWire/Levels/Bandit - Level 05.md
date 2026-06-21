---
tags: [linux, bandit, wargame, shell, practice]
source: OverTheWire Bandit — Level 5
---

# Bandit - Level 05

## Goal
The password for the next level is stored in the `inhere` directory tree, in a file that is: human-readable, exactly 1033 bytes, and not executable. 20 subdirectories (`maybehere00`–`maybehere19`), each holding several decoy files.

## Connection
```bash
ssh -p 2220 bandit5@bandit.labs.overthewire.org
```
Use the password retrieved at the end of [[Bandit - Level 04]].

## Concepts
The core question this level forces: how do you search *recursively*, across many nested directories, by file properties (type, size, permissions) instead of by name? `find` is built exactly for this — it walks the whole subtree from a starting point automatically. This level was the trigger for giving `find` its own dedicated reference: [[Linux - find Command]].

## Attempts Explored
- `du -sh ./*` — shows directory sizes, useful for a first look but doesn't single out an individual file or its properties.
- `file ./*` — every result came back `directory`. Important realization: **`file` doesn't recurse** — it only reports on the literal items it's given, not on what's inside them. Going one level deeper would mean repeating this by hand for all 20 folders — exactly the "search them all at once" problem that needed a different tool.

## Solution
```bash
find . -type f -size 1033c ! -executable
# → ./maybehere07/.file2

file ./maybehere07/.file2     # ASCII text, with very long lines (1000)
ls -l ./maybehere07/.file2    # 1033 bytes exactly
cat ./maybehere07/.file2      # HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```

**Side discovery**: `du -sh` reported `4.0K` for a file that `ls -l` confirms is exactly 1033 bytes. Not a contradiction — `du` measures actual disk space allocated (rounded up to the filesystem's block size, commonly 4KB), while `ls -l` shows the exact logical size of the content. A 1033-byte file still consumes a full 4096-byte block on disk because that's the smallest unit the filesystem allocates.

## Key Takeaway
`file` and `find` solve different problems: `file` identifies what one item *is*, `find` locates items matching criteria *anywhere in a subtree*. When the question becomes "search through many nested folders at once," `find`'s recursion is the default behavior to reach for — no manual looping required. `find` earned a full dedicated reference after this level — worth the investment given how often it resurfaces in security work.

## Next
`ssh -p 2220 bandit6@bandit.labs.overthewire.org` using the password found above.

---
◀ Previous: [[Bandit - Level 04]] · Next ▶ [[Bandit - Level 06]]
