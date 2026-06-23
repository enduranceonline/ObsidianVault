---
tags: [linux, shell, piping, redirection, practice]
source: Ryan's Tutorials — Linux Tutorial (piping.php) + Bandit Level 7
---

# Linux - Piping and Redirection

> Related: [[Linux - Command Line Reference]] covers the basics of streams (`stdin`, `stdout`, `stderr`) and the operators. This note goes deeper on how to combine them into real workflows.

---

## The Three Streams (recap)

Every program has three data streams connected automatically:

| Stream | Number | What it carries |
|--------|--------|----------------|
| ==STDIN== | `0` | Input fed into the program |
| ==STDOUT== | `1` | Normal output (defaults to terminal) |
| ==STDERR== | `2` | Error messages (defaults to terminal) |

Piping and redirection connect these streams between programs and files.

---

## Redirection to a File

```bash
ls > myoutput       # STDOUT → file (creates file if it doesn't exist; overwrites if it does)
ls >> myoutput      # STDOUT → file (appends — does not overwrite)
wc -l < myoutput    # file → STDIN (feeds file content into the program anonymously)
```

**Key behavior:** when you redirect to a file that already exists, its contents are cleared first, then the new output is written. Use `>>` to avoid destroying existing data.

**Anonymous input:** using `<` to feed a file into a program hides the filename from the program — `wc -l < file.txt` prints just the count, not `7 file.txt`. Useful when you want clean output without the filename appended.

---

## Redirecting STDERR

```bash
ls blah.foo 2> errors.txt       # STDERR → file (errors saved, normal output still on screen)
ls blah.foo 2>/dev/null         # discard errors entirely
ls blah.foo > out.txt 2>&1      # both STDOUT and STDERR → same file
ls blah.foo &> all.txt          # shorthand for the above (bash-specific)
```

`2>&1` means "redirect stream 2 (STDERR) to wherever stream 1 (STDOUT) is currently going." The order matters — redirect STDOUT to the file first, then point STDERR at STDOUT.

---

## Piping — Connecting Programs

The ==pipe== `|` feeds the STDOUT of one program directly into the STDIN of the next. The data never touches a file — it flows in memory.

```bash
ls | head -3              # first 3 items from ls
ls | head -3 | tail -1    # only the 3rd item — pipe chains are unlimited
ls | head -3 | tail -1 > myoutput   # pipe + redirect combined
```

**Build pipes incrementally.** Run the first command alone, verify the output, then add the next stage. Don't write a 4-stage pipe in one go and debug it blind — you won't know which stage broke it.

---

## Pipe vs Redirection — the key difference

| | Redirection (`>`, `<`) | Pipe (`\|`) |
|---|---|---|
| Connects | Program ↔ File | Program ↔ Program |
| Data goes through | Disk | Memory |
| Typical use | Save output, read input | Chain programs together |

---

## grep over a file vs grep over a pipe

This is a distinction that bites often:

```bash
# grep searches CONTENT of the file
grep 'millionth' data.txt          # reads data.txt, filters lines containing 'millionth'
cat data.txt | grep 'millionth'    # same result — pipes file content into grep

# grep searches what find PRINTS (file paths, not file content)
find / -name data.txt | grep 'millionth'   # searches the string "millionth" in path names — almost never what you want
```

==`grep`== always filters **the lines it receives as input** — whether that input comes from a file argument or from a pipe. It never "opens" files on its own when used in a pipe.

---

## Practical patterns

```bash
# View long output one page at a time
ls -l /etc | less

# Count lines matching a pattern
grep 'error' logfile.txt | wc -l

# Find unique owners in a directory
ls -l /projects | tail -n +2 | awk '{print $3}' | sort | uniq -c

# List only files the group can write to
ls -l ~ | grep '^.....w'

# 20th last file in /etc
ls /etc | tail -20 | head -1
```

---

## Key Takeaway

Pipes don't move files — they move **data streams**. A pipe connects what one program *prints* to what the next program *reads*. Understanding which stream carries what (and which stream `grep`, `wc`, `sort` actually read from) is the foundation for writing any non-trivial shell workflow.
