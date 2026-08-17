---
tags: [linux, shell, text-processing, log-analysis, practice, security]
source: Bandit Level 8 + general reference
---

# Linux - Sorting and Deduplication

> Related: [[Linux - Piping and Redirection]] covers how streams connect between programs. This note covers the three tools that turn a raw stream of lines into an answer: `sort`, `uniq` and `wc`.

---

## Why This Trio Matters Beyond Bandit

A log file is just lines of text. Almost every question an analyst asks of one reduces to counting or ranking those lines:

- Which IP hit us most in the last hour?
- Which user account failed to authenticate the most times?
- Which single host contacted a domain nobody else in the estate contacted?

`sort | uniq -c | sort -rn` answers the first two. `sort | uniq -u` answers the third. Neither needs a SIEM, a script, or a language — they work on any Unix box, over SSH, on a machine you've never seen before. This is why the pattern survives in incident response: it's always available.

---

## `uniq` — The Adjacency Rule

The single most important fact about ==`uniq`==: it compares each line **only against the line immediately before it**. It holds no memory of the rest of the file.

```bash
# File contents:      a  b  a  b  a
uniq -u file          # → a b a b a   (nothing is adjacent, everything looks unique)
sort file | uniq -u   # → (empty)     (correct: nothing occurs exactly once)
```

This is a deliberate design decision, not a limitation. Because it only ever holds one line in memory, `uniq` can stream a 50 GB log file on a machine with 2 GB of RAM. The cost of that efficiency is that **you must sort first**, which is the expensive step.

| Flag | Effect |
|---|---|
| `-u` | only lines occurring **exactly once** |
| `-d` | only lines that are **duplicated** (prints each once) |
| `-D` | **all** copies of every duplicated line |
| `-c` | prefix each line with its occurrence count |
| `-i` | case-insensitive comparison |
| `-f N` | skip the first N fields before comparing |
| `-w N` | compare only the first N characters |

`-f` and `-w` are the underrated ones: they let you deduplicate on *part* of a line — for example, ignoring a leading timestamp so that otherwise-identical events collapse together.

---

## `sort` — The Flags That Actually Matter

```bash
sort file.txt              # lexicographic (dictionary) order
sort -n file.txt           # numeric — 2 before 10
sort -h file.txt           # human-readable numeric — handles 4K, 2M, 1G
sort -r file.txt           # reverse
sort -u file.txt           # sort + drop duplicates in one pass
sort -k2 file.txt          # sort by the 2nd whitespace-separated field
sort -t: -k3 -n /etc/passwd   # custom delimiter (:) — sorts users by UID
sort -V file.txt           # version sort — handles 1.9 before 1.10
```

**`sort -n` vs plain `sort` is a real bug source.** Lexicographically, `"100"` sorts before `"9"` because it compares character by character. Any time the field is a byte count, a port number, or a response time, `-n` is mandatory.

**`sort -u` vs `sort | uniq`** — `sort -u` is faster and shorter, but it can *only* deduplicate. The moment you want `-c` (counts), `-d` (only duplicates) or `-u` in the `uniq` sense (only singletons), you need the explicit two-stage pipe. Rule of thumb: `sort -u` when you just want a clean list, `sort | uniq -c` when you want to *know something* about the distribution.

**Locale gotcha.** `sort` respects `$LC_ALL`/`$LANG`, which changes how case and accented characters are ordered. Two machines with different locales can produce different sort orders for the same file — which silently breaks `uniq`, `comm` and `diff` downstream. When the ordering must be reproducible (scripts, comparing outputs across hosts), force it:

```bash
LC_ALL=C sort file.txt
```

---

## `wc` — Counting

```bash
wc -l file.txt     # lines
wc -w file.txt     # words
wc -c file.txt     # bytes
wc -m file.txt     # characters (differs from -c on multi-byte encodings)
```

Piping into `wc -l` is how you sanity-check every stage of a pipeline. Before trusting a filter, compare its output count against the input count — if `uniq -u` returns 98% of your lines, the filter didn't filter, and that's the signal something upstream is wrong. Exactly what happened in [[Bandit - Level 08]].

Note the formatting difference: `wc -l file.txt` prints the count *and the filename*; `wc -l < file.txt` prints only the number, which is what you want when assigning to a variable.

---

## The Canonical Pipeline

```bash
sort | uniq -c | sort -rn | head
```

Read right to left as intent: *show me the top of the ranking, ordered by count descending, of how often each distinct line appeared.* Four stages, each doing one thing:

1. `sort` — group identical lines so `uniq` can see them
2. `uniq -c` — collapse each group to one line + a count
3. `sort -rn` — rank by that count, highest first
4. `head` — cut to the top N

**Build it incrementally.** Run stage 1, look at the output, add stage 2, look again. A four-stage pipe written in one go and debugged blind wastes more time than it saves.

---

## Real-World Applications

### Top talkers in a web access log
```bash
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -20
```
Field 1 of a combined-format log is the client IP. This is the first command run against a web server suspected of being scanned or brute-forced — a single IP with 40,000 requests against a baseline of 30 is not subtle.

### Failed SSH authentications by source IP
```bash
grep 'Failed password' /var/log/auth.log \
  | awk '{print $(NF-3)}' \
  | sort | uniq -c | sort -rn | head
```
`$(NF-3)` counts backwards from the last field, which survives the fact that the message wording shifts depending on whether the username was valid. Feeding the top offenders straight into a firewall block is a two-line escalation from here.

### Which accounts were targeted
```bash
grep 'Failed password' /var/log/auth.log \
  | grep -oP 'for (invalid user )?\K\w+' \
  | sort | uniq -c | sort -rn
```
Distinguishes a **spray** (many accounts, few attempts each) from a **brute force** (one account, thousands of attempts). Same log, different pivot, completely different incident classification and response.

### HTTP status code distribution
```bash
awk '{print $9}' access.log | sort | uniq -c | sort -rn
```
A sudden mass of `404`s is directory enumeration. A mass of `401`/`403` is credential stuffing. A mass of `500` is either an outage or someone fuzzing inputs successfully enough to crash the app.

### The one-off — finding the anomaly with `-u`
```bash
awk '{print $1}' access.log | sort | uniq -u
```
Inverts the whole logic: instead of "who is loudest", it asks **"who appeared exactly once"**. In a network where every host beacons to the same handful of update servers, the host that contacted a domain nobody else contacted is the interesting one. This is the manual, no-tooling version of the rare-event hunting described in the Kasiu Domain 2 material on ==beaconing== and ==DNS tunneling== detection — the same idea that a SIEM implements as a "rare value" or "first seen" detection rule.

### Comparing two lists — drift detection
```bash
# Lines present in only ONE of the two files
sort authorized_ports.txt actual_ports.txt | uniq -u

# Lines present in BOTH
sort authorized_ports.txt actual_ports.txt | uniq -d
```
Feed it a documented asset inventory and a fresh `nmap` output and `uniq -u` gives you, in one command, everything that drifted: services running that shouldn't be, and services documented that are gone. Same trick for authorized-users vs actual-users, or a baseline SUID inventory vs a current one — pairs directly with the privesc recon patterns in [[Linux - find Command]].

> For comparing two files specifically, ==`comm`== is the more precise tool (it labels which file each line came from in three columns), but it requires both inputs pre-sorted. `sort | uniq -u/-d` is the quick-and-dirty version that needs no setup.

### Unique users writing to a shared directory
```bash
ls -l /shared | tail -n +2 | awk '{print $3}' | sort | uniq -c | sort -rn
```
`tail -n +2` skips the `total N` header line that `ls -l` prints. Same shape as the ownership pattern already in [[Linux - Piping and Redirection]].

### Deduplicating a wordlist
```bash
sort -u raw_wordlist.txt > clean_wordlist.txt
wc -l raw_wordlist.txt clean_wordlist.txt   # confirm how much was removed
```
Concatenated wordlists are full of duplicates; removing them cuts attack or audit time proportionally, with zero loss of coverage.

---

## Gotchas Worth Remembering

**Sorting IP addresses lexicographically is wrong.** `10.0.0.9` sorts after `10.0.0.10` in dictionary order. Use `-V` (version sort handles dotted-decimal correctly) or an explicit field sort:
```bash
sort -V ips.txt
sort -t. -k1,1n -k2,2n -k3,3n -k4,4n ips.txt
```

**`uniq -c` output is right-aligned with padding.** The count column is space-padded, so a naive `cut -d' ' -f1` on it returns empty strings. Use `awk '{print $1}'` instead, which collapses runs of whitespace automatically.

**`uniq` is case-sensitive and whitespace-sensitive by default.** `Admin` and `admin` are different lines; so are `foo` and `foo ` (trailing space). Add `-i` for case, and strip whitespace upstream when the source is untrustworthy.

**Sorting is the expensive stage.** On very large files, `sort` writes temporary files to disk. `sort -S 2G` raises its memory buffer; `LC_ALL=C sort` is also measurably faster because it skips locale-aware collation.

---

## Key Takeaway

`sort` and `uniq` are a **pair**, not two independent tools. `uniq` compares adjacent lines only, so `sort` is the step that makes it meaningful — forgetting it produces plausible-looking output that is silently wrong, which is more dangerous than an error message.

Once that's internalized, `sort | uniq -c | sort -rn` becomes the default first question asked of any unfamiliar log ("what's frequent here?"), and `sort | uniq -u` becomes the second ("what's unique here?"). Between them they cover both halves of detection work: **volume anomalies** and **rare events**.
