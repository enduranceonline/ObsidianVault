---
tags: [linux, bandit, wargame, shell, practice]
source: OverTheWire Bandit — Level 6
date_completed: 2026-06-22
---

# Bandit - Level 06

## Goal
The password for the next level is stored **somewhere on the server** — not just in the home directory. The file is owned by user `bandit7`, group `bandit6`, and is exactly 33 bytes in size.

## Connection
```bash
ssh -p 2220 bandit6@bandit.labs.overthewire.org
```
Use the password retrieved at the end of [[Bandit - Level 05]].

## Concepts
Same `find` syntax as [[Bandit - Level 05]] — `-type f`, `-size`, `-user`, `-group` — but the key shift is the **search scope**. The challenge says "somewhere on the server," which means the whole filesystem, not just the current directory or `/home`. That single word ("somewhere") is the entire puzzle.

Also reinforces `2>/dev/null` as a standard reflex when running `find` across the full filesystem: hundreds of `Permission denied` lines from system directories would otherwise bury the real result.

## Attempts

```bash
# Started from /home — wrong scope
find -size 33c                            # no -type, no owner filter — too broad, wrong root
find -size 33c -file f -user bandit7 -group bandit6   # typo: -file instead of -type
find -size 33c -type f -user bandit7 -group bandit6   # correct flags, still wrong root (/home)
find . -type f -user bandit7 -group bandit6 2>/dev/null  # added stderr redirect — still /home
```

## Solution

```bash
cd /
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
# → /var/lib/dpkg/info/bandit7.password

cat /var/lib/dpkg/info/bandit7.password
```

## Points of Friction
Searched from `/home` across all attempts before realizing the starting path was wrong. The file lives in `/var/lib/dpkg/info/` — completely outside `/home`. The flags and syntax were correct from the second attempt; the only error was the search root.

## Key Takeaway
`find .` and `find /` are not interchangeable. ==`find .`== searches from the current directory downward. ==`find /`== searches the entire filesystem. When a challenge says "somewhere on the server" — always start from `/`. The `2>/dev/null` redirect is standard practice for full-filesystem searches: silence the noise, surface the signal.

## Next
```bash
ssh -p 2220 bandit7@bandit.labs.overthewire.org
```

---
◀ Previous: [[Bandit - Level 05]] · Next ▶ [[Bandit - Level 07]]
