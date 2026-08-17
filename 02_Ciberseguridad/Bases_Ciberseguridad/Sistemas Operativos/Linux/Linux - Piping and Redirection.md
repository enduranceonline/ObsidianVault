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

## ⚠️ A file argument silently kills the pipe

The most damaging pipeline bug, because it produces **no error at all**:

```bash
base64 -d data.txt | sort data.txt | grep "="     # BROKEN
base64 -d data.txt | sort | grep "="              # correct
```

Most Unix tools (`sort`, `grep`, `wc`, `uniq`, `cut`, `head`, `tail`, `tr`...) follow the same rule: **if given a filename argument, they read that file and ignore stdin completely.** They read from stdin *only* when no file is named.

So in the broken version above, `sort` opens `data.txt` from disk and throws away everything `base64` sent down the pipe. The pipeline still runs, still prints something, and gives no indication that a whole stage was discarded.

**The rule:** in a pipeline, only the **first** command gets a file argument. Everything after it goes bare.

```bash
cat data.txt | grep 'x' data.txt     # WRONG — grep ignores the pipe
cat data.txt | grep 'x'              # right
strings data.txt | grep '==='        # right — strings reads the file, grep reads the pipe
```

> This is the same misunderstanding as `find | grep` above, in a different disguise: assuming the pipe is what feeds the next command, when an explicit argument overrides it. Encountered in [[Bandit - Level 07]] and again in [[Bandit - Level 09]].

**Diagnostic habit:** when a pipeline returns something that looks like a stage didn't apply, check whether a downstream command has a filename attached to it.

### The mirror case: commands that read ONLY stdin

==`tr`== has no file argument at all. There is no `tr 'a' 'b' file.txt` — it's a syntax error, not an alternative form. The data must be piped or redirected in:

```bash
cat file.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'    # via pipe
tr 'A-Za-z' 'N-ZA-Mn-za-m' < file.txt        # via redirect — one less process
```

`tr`'s two arguments are the character **sets** describing the transformation, never the data. Passing file content as an argument produces `tr: missing operand` — see [[Bandit - Level 11]].

The two behaviours together are the thing worth internalising: `sort` **ignores** stdin when given a file, `tr` **only has** stdin. Before writing a pipeline stage, know which input that specific command actually reads. `--help` answers it in one second: if the usage line ends in `[FILE]...`, it takes files; if it doesn't, it's stdin-only.

---

## Binary data in a pipeline

`grep` inspects its input and, on detecting null bytes, refuses to print matching lines — reporting `binary file matches` (or `binary file (standard input) matches` when the input arrives via a pipe) instead of the content.

```bash
grep 'pattern' data.txt      # → grep: data.txt: binary file matches
grep -a 'pattern' data.txt   # force text mode — prints the match
```

**This is a safety feature, not an error.** Raw binary written to a terminal can emit control sequences that corrupt the session. And `-a` only partly helps: `grep` returns whole **lines**, and in binary data the `\n` bytes fall at random offsets, so the match arrives wrapped in hundreds of unreadable bytes.

The correct move is to convert the input to text before it enters the text pipeline:

```bash
strings data.txt | grep '==='       # strings makes it text, grep then works normally
```

Full detail: [[Linux - Extracting Strings from Binaries]].

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
