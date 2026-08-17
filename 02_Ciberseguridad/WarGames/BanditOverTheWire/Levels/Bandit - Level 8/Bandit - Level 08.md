---
tags: [linux, bandit, wargame, shell, practice]
source: OverTheWire Bandit — Level 8
date_completed: 2026-08-15
---

# Bandit - Level 08

## Goal
The password for the next level is stored in `data.txt`, on the **only line that occurs once**. Every other line in the file is repeated.

## Connection
```bash
ssh -p 2220 bandit8@bandit.labs.overthewire.org
```
Use the password retrieved at the end of [[Bandit - Level 07]].

## Concepts

==`uniq`== does **not** search the whole file for duplicates. It only compares each line against the **immediately preceding one**. Lines that are identical but sit far apart in the file are invisible to it.

That single behavior is why `sort` is not decoration here — it's a **precondition**. Sorting groups identical lines into adjacent blocks so that `uniq` can actually see them as repeats.

| Flag | Effect |
|---|---|
| `-u` | print only lines that appear **exactly once** |
| `-d` | print only lines that are **repeated** |
| `-c` | prefix each line with its occurrence count |
| `-i` | ignore case when comparing |

Full stream/pipe mechanics: [[Linux - Piping and Redirection]].

## Attempts

```bash
# Reflex from previous levels — reached for find to locate the file first
find / data.txt
# → dumped the entire filesystem and errored out.
# "data.txt" without -name is parsed as a second STARTING PATH, not a search criterion.

# The file was in the home directory all along
pwd              # /home/bandit8
cat data.txt     # printed 1001 lines — readable, but far too many to scan by eye
```

Then, before solving, three commands run deliberately to **prove** the `uniq` adjacency behavior instead of taking it on faith:

```bash
wc -l data.txt
# → 1001 data.txt          total lines in the file

uniq -u data.txt | wc -l
# → 981                    WRONG. Without sorting, uniq only catches adjacent
#                          repeats, so 981 lines falsely look "unique"

sort data.txt | uniq -c | head
# →   10 0LTDNpAmqqfuE0FlE0ksGF6c0Kraspzs
#     10 1cKKjk7M0Pl2cPUbYgc9W4307bYC0ohF
#     10 1PesxCa7cihwvCvzBeKAcjKkjUwp7i2z
#     ...                  every line appears exactly 10 times
```

The arithmetic closes cleanly: **100 distinct lines × 10 repetitions = 1000, plus 1 unique line = 1001.** The structure of the file was fully mapped before the answer was extracted.

## Solution

```bash
sort data.txt | uniq -u
# → EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl
```

`sort` groups the identical lines into adjacent blocks; `uniq -u` then discards every block with more than one member, leaving the single orphan line.

## Points of Friction

**1. Reached for `find` again to locate a file that was in the home directory.** Same friction as [[Bandit - Level 07]] — second consecutive level. In Bandit, unless the level text explicitly points elsewhere (as Level 5 does with `inhere/`), the target file is in `~`. New standing rule: **`pwd` and `ls -la` before any `find`.** Cheap reconnaissance first.

**2. `find / data.txt` is not a search.** `find`'s syntax is `find [starting-paths...] [tests] [actions]`. Any bare word that doesn't begin with `-` is consumed as a **starting path**, so this asked find to recurse through `/` *and* through a nonexistent directory named `data.txt`. The criterion only exists once `-name` is present: `find / -name data.txt 2>/dev/null`. Detailed in [[Linux - find Command]].

**3. `uniq -u` alone looked like it worked.** It returned output, no error, 981 lines. A command that runs successfully is not a command that answered the question — the same trap already recorded in [[Linux - File Type Detection]], in a different disguise.

## Key Takeaway

==`uniq`== is a **line-adjacency filter**, not a deduplicator. It has no memory of the file beyond the previous line, which is what makes it fast enough to stream gigabytes — and what makes `sort` mandatory in front of it whenever duplicates aren't already grouped.

The pipeline `sort | uniq -c | sort -rn` is the single most reused pattern in log analysis: it turns a raw stream of events into a frequency table ranked by volume. `uniq -u` is its mirror image — instead of finding what happens most, it finds **what happened only once**, which in a security context is usually the interesting part. Full treatment: [[Linux - Sorting and Deduplication]].

## Next
```bash
ssh -p 2220 bandit9@bandit.labs.overthewire.org
```

---
◀ Previous: [[Bandit - Level 07]] · Next ▶ [[Bandit - Level 09]]
