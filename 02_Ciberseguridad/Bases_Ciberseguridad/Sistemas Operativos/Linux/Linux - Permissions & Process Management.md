---
tags: [linux, permissions, processes, practice]
source: Linux Journey — Permissions & Processes modules
---

# Linux - Permissions & Process Management

## File Permissions

Three permission types: read (`r`), write (`w`), execute (`x`). Three classes: owner (`u`), group (`g`), others (`o`).

`ls -l` output breakdown:
```
-rwxr-xr--  1 user group  4096 Jun 17 10:00 file.sh
```
First character is the file type (`-` regular file, `d` directory, `l` symlink). The next 9 characters are three groups of `rwx`, in order: owner, group, others.

## Symbolic vs Numeric (octal) Notation

Each permission has a numeric value: `r`=4, `w`=2, `x`=1. Sum them per class to get the octal digit for that class.

| Octal | Permissions | Meaning |
|---|---|---|
| 7 | rwx | read + write + execute |
| 6 | rw- | read + write |
| 5 | r-x | read + execute |
| 4 | r-- | read only |
| 0 | --- | nothing |

```bash
chmod 755 script.sh    # owner: rwx, group: r-x, others: r-x
chmod 644 file.txt     # owner: rw-, group: r--, others: r--
chmod u+x script.sh    # symbolic: add execute for the owner
chmod g-w file.txt     # symbolic: remove write from the group
chmod o=r file.txt     # symbolic: set others to read-only
chmod -R 755 folder/   # recursive — applies to a folder and everything inside it
```

## Ownership

```bash
chown user file.txt          # change the owner
chown user:group file.txt    # change owner and group together
chgrp group file.txt         # change the group only
chown -R user:group folder/  # recursive
```

## Special Permission Bits

- **SUID** (`u+s`, leading `4`) — the file runs with the *owner's* privileges, regardless of who runs it. Classic example: `passwd`, which needs root privileges to edit `/etc/shadow` even when a regular user runs it.
- **SGID** (`g+s`, leading `2`) — runs with the file's *group* privileges; on a directory, new files created inside inherit that directory's group.
- **Sticky bit** (`+t`, leading `1`) — on a directory, only the file's owner (or root) can delete it. Used on shared directories like `/tmp`.

```bash
chmod u+s file
chmod g+s folder/
chmod +t /tmp
chmod 4755 file    # SUID + 755
```

> Worth remembering for later: privilege escalation (in Bandit and beyond) is largely about finding misconfigured permissions and SUID binaries.

## Process Management

**`ps`** — snapshot of running processes.
```bash
ps        # processes in this shell session
ps aux    # every process on the system, in detail
```

**`top` / `htop`** — live, continuously updating view of processes and resource usage. `htop` is the friendlier, color version (may need installing).
```bash
top
htop
```

**Jobs and the background**
```bash
sleep 100 &    # & runs it in the background, frees up the shell
jobs           # list background jobs in this session
fg %1          # bring job 1 back to the foreground
bg %1          # send job 1 back to the background
# Ctrl+Z       # suspend the current foreground process
```

**`kill`** — send a signal to a process by PID.
```bash
kill 1234            # SIGTERM — politely ask it to stop
kill -9 1234         # SIGKILL — force-stop, no cleanup
killall firefox      # kill all processes with that name — no need to know the PID
pkill -f "pattern"   # kill matching a command-line pattern
```

`killall` is the practical choice when a process has multiple child processes (like Spotify or Brave) — kills the whole tree by name instead of hunting down each PID manually.

**`nice` / `renice`** — set a process's scheduling priority (lower number = higher priority).
```bash
nice -n 10 some_command   # start a process with lower priority
renice 5 -p 1234           # change priority of an already-running process
```
