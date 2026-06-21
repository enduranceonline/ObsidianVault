---
tags: [linux, find, practice, security]
source: Bandit Level 5 + general reference
---

# Linux - find Command

## Why `find` Matters Beyond Bandit

`find` is the tool for "locate things matching criteria, anywhere in a directory tree" — and that exact need shows up constantly in security work: hunting for SUID/SGID binaries during privilege escalation, locating files modified around the time of an incident (forensics), finding world-writable files, or just locating a config buried six folders deep. Worth dominating properly rather than treating as a one-off command.

## Basic Syntax
```bash
find [starting-path] [tests] [actions]
```
- **Starting path** — where to begin recursing. Defaults to `.` (current directory) if omitted.
- **Tests** — conditions a file must match (name, type, size, time, permissions...).
- **Actions** — what to do with matches. Defaults to `-print` (just list them) if no action is given.

## Tests by Category

**Name & path**
```bash
find . -name "*.log"           # case-sensitive glob match on filename
find . -iname "*.LOG"          # case-insensitive version
find . -path "*/config/*"      # match against the full path, not just filename
```

**Type**
```bash
find . -type f      # regular files
find . -type d      # directories
find . -type l      # symbolic links
```

**Size** (see [[Linux - Command Line Reference]] for the unit-suffix gotcha)
```bash
find . -size 1033c     # exactly 1033 bytes
find . -size +10M      # larger than 10 MiB
find . -size -1k       # smaller than 1 KiB
```
`+` and `-` before the number mean "greater than" / "less than" — without either, it means exact match.

**Time** (in days unless using the `min` variants, which are in minutes)
```bash
find . -mtime -1       # modified in the last 1 day
find . -mtime +7       # modified more than 7 days ago
find . -newer file.txt # modified more recently than file.txt
find . -mmin -30       # modified in the last 30 minutes
```
`-mtime` = content modified, `-atime` = last accessed, `-ctime` = metadata/inode changed (permissions, ownership) — distinct timestamps, easy to confuse.

**Permissions, ownership & special bits**
```bash
find . -perm 644              # exact permission match
find . -perm -u+x             # owner has execute (at minimum)
find . -user bandit5          # owned by this user
find . -group bandit5         # owned by this group
find . ! -executable          # NOT executable
find / -perm -4000 2>/dev/null   # SUID bit set — classic privesc recon command
```

**Depth & emptiness**
```bash
find . -maxdepth 1     # don't recurse past 1 level — useful to avoid huge trees
find . -mindepth 2      # skip the top level, only go deeper
find . -empty            # empty files or directories
```

## Combining Tests

Multiple tests are AND'd together by default — no operator needed:
```bash
find . -type f -size 1033c ! -executable   # all three must be true
```

Explicit logical operators:
```bash
find . -name "*.txt" -o -name "*.log"      # OR
find . -type f -a -size +1M                # AND (explicit, same as default)
find . \( -name "*.tmp" -o -name "*.bak" \) -delete   # group with parentheses
```
`!` negates a single test (seen above with `! -executable`). Parentheses need to be escaped (`\(` `\)`) or quoted, since bash would otherwise try to interpret them itself.

## Actions

```bash
find . -name "*.tmp" -delete                  # delete matches directly
find . -type f -exec chmod 644 {} \;           # run a command on each match, one at a time
find . -type f -exec chmod 644 {} +            # same, but batches matches into fewer command calls — faster
find . -name "*.sh" -ok rm {} \;               # like -exec, but asks for confirmation each time
```
`{}` is the placeholder for the matched file inside `-exec`/`-ok`. The trailing `\;` (escaped semicolon) or `+` ends the command — `\;` runs the command once per file, `+` bundles as many files as possible into fewer invocations of the command, which is significantly faster on large result sets.

## Common Real-World Patterns

```bash
find / -perm -4000 2>/dev/null              # SUID binaries — privesc recon
find / -perm -2000 2>/dev/null              # SGID binaries
find / -writable -type d 2>/dev/null        # world-writable directories
find . -type f -newer /tmp/marker -mtime -1  # files touched since a reference point
find / -name "*.conf" -user root 2>/dev/null # root-owned config files
```

## Key Takeaway
`find`'s power is in composition: small, simple tests (`-type`, `-size`, `-perm`, `-mtime`) combine into precise searches that would otherwise mean manually walking a directory tree. The investment in learning the test flags pays off well beyond Bandit — this is a daily-driver command in pentesting, forensics, and sysadmin work alike.
