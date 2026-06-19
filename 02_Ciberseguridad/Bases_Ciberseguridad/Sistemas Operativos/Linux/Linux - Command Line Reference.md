---
tags: [linux, commands, basics, practice]
source: Linux Journey — Command Line module
---

# 🐧 Linux Command Line Reference

## 🐚 The Shell

The shell takes what you type and passes it to the OS to run. A "Terminal" or "Console" app is just a window that opens a shell session. Bash (Bourne Again Shell) is the default shell on most distros — other shells exist (`ksh`, `zsh`, `tcsh`), but Bash is the safe baseline to learn first.

Prompt format: `username@hostname:current_directory$` — the `$` just means "ready for input", you don't type it yourself.

Commands come in three flavors: *built-in* (handled directly by the shell itself, like `cd` and `echo`), *external* (separate binaries on disk, like `cp` and `ls`), and whatever *aliases/functions* you define yourself.

```bash
echo Hello World   # prints the text back to the terminal
```

## 📂 File Navigation & Management

**`pwd`** — absolute path of the current directory.
```bash
pwd
```

**`cd`** — change directory. Absolute paths start with `/`; relative paths are relative to where you currently are.
```bash
cd /home/user/Pictures   # absolute
cd Hawaii                # relative, from inside Pictures
```
Shortcuts: `.` current dir · `..` parent dir · `~` home dir · `-` previous dir

**`ls`** — list directory contents.
```bash
ls -a    # show hidden files (dotfiles)
ls -l    # long format: permissions, links, owner, group, size, date, name
ls -r    # reverse order
ls -la   # flags can be combined, order doesn't matter
```

**`tree`** — directory structure as a tree (may need installing).
```bash
tree
tree -L 1   # limit how many levels deep it shows
```

**`touch`** — create empty files / update timestamps.
```bash
touch new_file.txt
touch -r file1.txt file2.txt          # copy file1's timestamp onto file2
touch -d "2023-01-01 12:30:00" file   # set a specific timestamp
```

**`file`** — shows what kind of content a file actually has (a filename doesn't guarantee its content type in Linux).
```bash
file banana.jpg
```

**`mkdir`** — create directories.
```bash
mkdir new_folder
mkdir -p full/nested/path   # creates parent dirs as needed, no error if they already exist
```

**`cp`** — copy files/directories.
```bash
cp file.txt copy.txt
cp -r dir1/ dir2/        # recursive — required to copy a directory
cp -i file dest/         # ask before overwriting
cp -f file dest/         # force overwrite, no prompt (useful in scripts)
cp -p file dest/         # preserve timestamps / ownership / permissions
cp -u file dest/         # only copy if source is newer, or missing at destination
cp -v file dest/         # verbose — shows what's being copied
cp *.jpg Pictures/       # wildcards: * any characters, ? one character, [] one of a set
```
> Common mistakes: copying a directory without `-r` fails with "omitting directory"; copying several files into something that turns out not to be a directory also fails.

**`mv`** — move or rename. Same syntax does both.
```bash
mv oldname newname
mv file1 file2 /somedir     # move multiple files at once
mv -t /somedir file1 file2  # target directory first
mv -i source dest           # prompt before overwriting
mv -b file1 dest            # keep a backup (~ suffix) of the overwritten file
mv -v file1 dest            # verbose, shows what's happening
```
No `-r` flag needed for directories — `mv` handles them by default.

**`rm`** — delete files/directories. No recycle bin: deletions are permanent.
```bash
rm file
rm -i file       # ask before deleting — recommended
rm -r folder/    # recursive, deletes directory + contents
rm -f file       # force, no prompts at all — use carefully
rmdir folder/    # safer alternative: only deletes if the folder is empty
```

**`find`** — search recursively for files/directories from a starting path.
```bash
find /home -name puppies.jpg
find /home -type d -name MyFolder   # -type d = directory, -type f = regular file
```

## 🔀 Pipes and Chaining

**`|`** (pipe) — sends the output of one command as the input to the next. The most common pattern in practice:
```bash
ps aux | grep "spotify"    # filter running processes by name
cat file.txt | grep "error"
```
The pipe doesn't care about what's on either side — it just connects stdout → stdin. A subtle gotcha: `grep` appears in its own results when you search `ps aux`, because the grep process itself is running while ps is capturing. Not a problem, just expected behavior.

**`&&`** and **`||`** — chain commands based on success/failure (see [[Linux - Logical Operators and Test Conditions]]).

## ▶️ Executing Scripts

**`./script.sh`** — runs the script as an independent child process. The `./` is required because the shell doesn't look in the current directory by default (security reason). The file needs execute permission (`chmod +x` or `chmod 755`) or it fails with "Permission denied".

```bash
chmod 755 script.sh
./script.sh
```

**`. file`** (or `source file`) — executes the file *inside the current shell session*, not as a child process. Changes made (variables, directory changes) affect your current shell. Used for config files like `~/.bashrc`.

```bash
source ~/.bashrc    # reload shell config — changes apply to this session
. ~/.bashrc         # same thing, shorter syntax
```

**The critical difference**: `./script.sh` spawns a new process (isolated); `. script.sh` runs inline (affects your session). For anything you want to "run", use `./`. For config you want to "apply", use `source`/`.`.



## 🔧 Streams & Redirection

Every command has three I/O **streams**, each with a numeric file descriptor:

| Stream | Descriptor | What it carries |
|---|---|---|
| stdin | `0` | input the command reads |
| stdout | `1` | normal output |
| stderr | `2` | error messages |

`>` redirects stdout by default — that's why `command > file.txt` writes only the normal output. Errors still print to the screen, because they travel through a *separate* stream that `>` alone doesn't touch.

```bash
echo "Hello" > greeting.txt          # create or overwrite (stdout)
echo "Another line" >> greeting.txt  # append to the end
cat < greeting.txt                   # input from a file (stdin)

command 2> errors.log     # send only stderr to a file
command 2>/dev/null       # discard stderr entirely
command > out.log 2>&1    # send both stdout and stderr to the same file
command &> all.log        # shorthand for the line above (bash-specific)
```

**`/dev/null`** is a special file that discards anything written to it — a black hole, no disk space used, nothing retained. The standard way to silence noise you already expect and don't need, instead of letting it clutter the screen:
```bash
find /home -type f -name "readme" 2>/dev/null   # only real matches, no "Permission denied" spam
```

**Why this matters beyond convenience**: separating stdout from stderr means a script or pipeline can react to *only* the actual data, ignoring error chatter — critical once you start scripting or piping command output into something else that expects clean input.

For the full breakdown of `chmod`, `chown`, octal notation, and special bits (SUID/SGID/sticky), see [[Permisos y gestión de procesos]] — kept there instead of duplicated here.

## 🛠️ Administrative Commands

**`su`** / **`sudo`**
```bash
su          # switch to root
su - user
sudo apt update
```

## 📤 File Transfer

**`scp`** — copy between machines over SSH.
```bash
scp file.txt user@host:/destination/path
```

## ✍️ Text Editors

**`nano`** / **`vim`** / **`gedit`**
```bash
nano file.txt
vim file.txt
gedit file.txt &
```

## 🧾 Reading & Searching Text

**`cat`** — print/concatenate file contents; best for short files.
```bash
cat file.txt
cat dogfile birdfile     # prints both, one after the other
cat > newfile.txt        # write text into a new file directly, Ctrl+D to save & exit
cat -n file.txt          # number every line
cat -b file.txt          # number only non-empty lines
```

**`less`** — page through large files without loading the whole thing into memory.
```bash
less file.txt
```
Inside `less`: `g` go to start · `G` go to end · `/term` search forward · `?term` search backward · `n`/`N` next/previous match · `h` help · `q` quit

**`grep`** — filter lines matching some text.
```bash
grep "error" log.txt
```

## 🗜️ Compression: `zip`, `unzip` and `tar`

`zip` packs files into a single `.zip`, compressing each file individually inside it — cross-platform, friendly with Windows/macOS.
`tar` just bundles files together; by itself it doesn't compress anything. Combined with `gzip`/`bzip2`/`xz` it becomes a compressed archive: `.tar.gz`/`.tgz` = tar + gzip, `.tar.bz2` = tar + bzip2, `.tar.xz` = tar + xz.

```bash
zip archive.zip file1.txt file2.png      # create a zip with several files
zip -r folder.zip my_folder/             # zip a whole folder, recursively
unzip -l archive.zip                     # list contents without extracting
unzip archive.zip                        # extract
unzip archive.zip -d /destination/       # extract into a specific folder

tar -cvf archive.tar file1.txt file2.txt # bundle, no compression
tar -czvf archive.tar.gz folder/         # bundle + gzip compression
tar -xzvf archive.tar.gz                 # extract a .tar.gz
tar -tvf archive.tar.gz                  # list contents without extracting
tar -xzvf archive.tar.gz -C /destination/
```

| zip flag | meaning |
|---|---|
| `-r` | recursive (directories) |
| `-e` | password-protect the archive |
| `-9` | maximum compression |

| tar flag | meaning |
|---|---|
| `-c` | create |
| `-x` | extract |
| `-v` | verbose |
| `-f` | filename |
| `-z` | gzip |
| `-j` | bzip2 |
| `-J` | xz |

**`zip` vs `tar`**

| | `zip` | `tar` + compression |
|---|---|---|
| Cross-platform | High (Windows/macOS) | High on Linux/Unix |
| Per-file compression | Yes | No (single archive) |
| Built-in password option | Yes | No |
| Efficiency | Lower | Higher |
| Typical use | Sharing individual files | Full backups |

Rule of thumb: `tar -czvf` for backups and deployments, `zip -r` for sharing with non-Linux users or when you need a password.

## 🔍 System Monitoring & Management

**`ps`**
```bash
ps aux       # all processes
```

**`history`** — your command history.
```bash
history
!!                   # re-run the last command
history -c           # clear history for this session
history -w           # write current session's history to ~/.bash_history
history -d 101        # delete entry #101
```
Up arrow = cycle back through history · `Ctrl-R` = reverse search as you type · `Tab` = autocomplete commands/filenames · `clear` = wipe the terminal screen

## 🆘 Getting Help

**`help`** — info for Bash *built-in* commands (e.g. `cd`, `echo`, `pwd`).
```bash
help echo
```

**`--help`** — most external (non built-in) programs support this flag for a quick usage summary.
```bash
ls --help
```

**`man`** — full manual page for a command.
```bash
man ls
```

**`info`** — an even more detailed manual, common for GNU tools.
```bash
info ls
```

**`whatis`** — one-line description pulled from the man page.
```bash
whatis cat
```

**`apropos`** — search for commands related to a keyword, when you don't know the exact name.
```bash
apropos user
```

## 🔗 Aliases

```bash
alias ll='ls -la'   # temporary, lasts only for this session
unalias ll          # remove it
```
To make an alias permanent: add the `alias` line to `~/.bashrc`, then run `source ~/.bashrc` to reload it without restarting the terminal.

## 🚪 Ending a Session

```bash
exit      # ends the current shell
logout    # ends a login shell specifically
```
Closing the terminal window works too — it sends a signal that ends the shell running inside it.

---
✅ Good for daily review and everyday terminal use.
