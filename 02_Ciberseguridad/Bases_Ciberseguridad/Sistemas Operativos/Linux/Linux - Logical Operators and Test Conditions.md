---
tags: [linux, bash, scripting]
source: personal note — Kali Linux Introducción
---

# Linux - Logical Operators and Test Conditions

## Chaining commands
```bash
cmd1 && cmd2   # run cmd2 only if cmd1 succeeded
cmd1 || cmd2   # run cmd2 only if cmd1 failed
! cmd          # negate the result
```

## Test conditions (used in `if`, `test`, `[ ]`)

**Numbers**

| Operator | Meaning |
|---|---|
| `-eq` | equal |
| `-ne` | not equal |
| `-lt` | less than |
| `-le` | less than or equal |
| `-gt` | greater than |
| `-ge` | greater than or equal |

**Strings**

| Operator | Meaning |
|---|---|
| `=` | equal |
| `!=` | not equal |
| `-z` | string is empty |
| `-n` | string is not empty |

**Files**

| Operator | Meaning |
|---|---|
| `-e` | exists |
| `-f` | is a regular file |
| `-d` | is a directory |
| `-r` | is readable |
| `-w` | is writable |
| `-x` | is executable |

## Logic inside tools
```bash
grep 'error\|warning' log.txt         # OR — matches either word
find . -name "*.txt" -and -size +1M   # AND — both conditions must be true
```

These are the building blocks for writing Bash scripts and conditionals later on.
