---
tags: [linux, shell, text-processing, log-analysis, practice, security]
source: Bandit Levels 8-9 + general reference
---

# Linux - Sampling and Inspecting Output

> Related: [[Linux - Piping and Redirection]] covers how streams connect. This note covers the tools used to *look* at a stream — before, during and after building a pipeline.

---

## The Core Idea

Most terminal work fails not because the wrong command was chosen, but because it was chosen **before looking at the data**. A 4 GB log, a binary of unknown structure, the output of a tool used for the first time — none of these can be reasoned about until a sample has been seen.

`head`, `tail` and `less` are **orientation tools**, not analysis tools. They contribute nothing to a result. What they contribute is the certainty that the next command is worth running.

```bash
head -30 file      # first 30 lines
tail -30 file      # last 30 lines
less file          # scrollable, searchable, loads nothing extra into memory
```

The number is arbitrary — whatever fits a screen without scrolling. With no number, both default to **10**.

---

## `head`

```bash
head file              # first 10 lines (default)
head -30 file          # first 30 lines
head -n 30 file        # identical, POSIX form — preferred in scripts
head -c 100 file       # first 100 BYTES, not lines
head -q *.log          # suppress the ==> filename <== headers when reading many files
head -n -5 file        # everything EXCEPT the last 5 lines (GNU only)
```

`-c` is the underrated one: it works on files with no line breaks at all, which is exactly the case with binary data.

```bash
head -c 64 unknown.bin | xxd     # inspect the magic bytes safely
```

Never pipe a raw binary into `head` without `-c` and a hex viewer — control bytes reaching the terminal can corrupt the session. Same reasoning behind `grep`'s binary refusal in [[Bandit - Level 09]].

**Efficiency matters more than it looks.** `head` stops reading once it has what it needs, sending `SIGPIPE` upstream to kill the producing command. `head -5 huge.log` on a 40 GB file returns instantly and reads only a few kilobytes — it does **not** read the file and then discard the rest.

---

## `tail`

```bash
tail file                  # last 10 lines
tail -50 file              # last 50 lines
tail -n +2 file            # from line 2 to the END — skips a header row
tail -f /var/log/syslog    # follow: stream new lines as they're written
tail -F /var/log/syslog    # follow BY NAME — survives log rotation
tail -f app.log | grep -i error   # live filtered monitoring
```

**`-n +N` vs `-n N` is a real trap.** `tail -n 5` gives the last five lines. `tail -n +5` gives everything **from** line 5 onward. The `+` inverts the meaning entirely. This is the idiom for stripping a CSV header or the `total N` line from `ls -l` — already used in [[Linux - Piping and Redirection]].

**Use `-F`, not `-f`, on system logs.** When logrotate renames a file and creates a fresh one, `tail -f` keeps following the old inode and goes silent forever — with no error. `tail -F` follows the *filename* and reattaches. Silent monitoring failures during an incident are exactly the kind of thing that gets discovered too late.

---

## Combining Them — Windowing

```bash
head -30 file | tail -10       # lines 21 to 30
sed -n '21,30p' file           # same result, one command, clearer intent
```

The `head | tail` chain is the classic idiom; `sed -n` is more precise once ranges get non-trivial. Both are worth recognising — the first appears constantly in older scripts and documentation.

---

## When to Use Which

| Situation | Tool |
|---|---|
| Check structure/format of an unfamiliar file | `head` |
| See what just happened | `tail` |
| Watch events as they occur | `tail -F` |
| Explore, search, scroll freely | `less` |
| Cap output of an unbounded pipeline | `head` |
| Preview binary safely | `head -c` + `xxd` |

`less` is the right choice when you don't yet know what you're looking for — inside it, `/pattern` searches forward, `G` jumps to the end, `g` to the start, `q` quits (already covered in [[Linux - Command Line Reference]]).

---

## Real-World Applications

### Learning a log's format before parsing it
The mandatory first step before writing any `awk`. Field positions can't be guessed:

```bash
head -3 /var/log/nginx/access.log
```
Only once you can see that field 1 is the client IP and field 9 the status code does `awk '{print $1}' | sort | uniq -c | sort -rn` make sense — the pipeline from [[Linux - Sorting and Deduplication]]. Writing the `awk` first and adjusting field numbers by trial and error is slower and produces silently wrong output when a field is missing.

### Establishing a log's time range
```bash
head -1 /var/log/auth.log      # oldest entry
tail -1 /var/log/auth.log      # newest entry
```
Two commands that answer "does this file even cover the window I'm investigating?" — before spending twenty minutes grepping a log that was rotated the day before the incident.

### Live monitoring during an incident
```bash
tail -F /var/log/auth.log | grep -i 'failed password'
tail -F /var/log/nginx/error.log | grep -v 'favicon'
```
Watching authentication failures in real time while applying a firewall rule shows immediately whether the block took effect. This is the no-tooling equivalent of a live SIEM query, and it works on a box you SSH'd into thirty seconds ago.

### Capping an unbounded pipeline
```bash
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -20
find / -perm -4000 2>/dev/null | head -20
```
Top-N is the natural closing stage of most ranking pipelines — the tail of the distribution is rarely the interesting part, and printing 40,000 lines to a terminal helps nobody.

### Sampling a huge file cheaply
```bash
head -1000 enormous.log > /tmp/sample.log
```
Develop and debug a parsing pipeline against a 1,000-line sample, then run the finished version against the full file once. Iterating against 4 GB is an unnecessary wait multiplied by every attempt.

### CSV and data file inspection
```bash
head -1 data.csv                    # column names
head -5 data.csv | column -t -s,    # aligned preview of the first rows
tail -n +2 data.csv | wc -l         # row count excluding the header
```

### Safe binary preview
```bash
head -c 16 suspicious.bin | xxd
# 00000000: 4d5a 9000 0300 0000 0400 0000 ffff 0000  MZ..............
```
`MZ` at offset 0 is a Windows PE executable, regardless of what the file is named. `%PDF` is a PDF, `PK` a zip-family archive. This is the manual version of what `file` automates ([[Linux - File Type Detection]]) — useful when you want to see the raw bytes rather than trust an interpretation.

### Sanity-checking before something destructive
```bash
find . -name "*.tmp" | head -20     # look at what matched
find . -name "*.tmp" -delete        # only then delete
```
The single highest-value habit on this list. Previewing what a destructive command *would* affect costs one second; recovering from `-delete` against a bad pattern can cost a day.

### Verifying an unfamiliar tool's output
The Bandit Level 9 case: `strings data.txt | head -30` confirmed that `strings` produced one readable string per line, and that the `===` pattern was present — before committing to a `grep`. When a filter on unverified output returns nothing, there's no way to know whether the fault lies in the tool, the pattern, or the assumption about the data.

---

## Gotchas

**`head -30` vs `head -n 30`.** The bare-number form is a legacy syntax kept for compatibility. It works everywhere in practice, but `-n 30` is the POSIX form and the safer choice in scripts.

**Reading a file that's actively being written.** `head` on a live log gives the oldest entries, which is usually the opposite of what's wanted. Reach for `tail` by default on anything under active write.

**`tail -f` dies silently on rotation.** Covered above — `-F` is the correct default for system logs.

**`head` on multiple files inserts headers.** `head *.log` prints a `==> filename <==` banner before each file. Convenient when reading, corrupting when piping into another tool. Suppress with `-q`.

**Multi-line records break line-based sampling.** Java stack traces, multi-line JSON and XML don't have one record per line, so `head -10` may cut a record in half. Not an error, but the sample can be misleading about the structure.

---

## Key Takeaway

`head` and `tail` produce no answers. Their value is **removing uncertainty from the next command** — confirming a file's format, an unfamiliar tool's output shape, a time range, or the blast radius of something destructive.

The working method they enable: **add one pipeline stage, look at the output, add the next.** Debugging a four-stage pipe written blind means guessing which stage broke it; building it incrementally means never having to. The cost is a few seconds per stage, which is always cheaper than being confidently wrong.
