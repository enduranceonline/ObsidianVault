---
tags: [linux, fundamentals, filesystem]
source: adapted from HTB Academy — Linux Fundamentals
---

# Linux Filesystem Hierarchy (FHS)

Linux organizes everything as a single tree starting at the root (`/`). Every other filesystem gets mounted as a subdirectory under it. Standard top-level directories, per the Filesystem Hierarchy Standard:

| Path | What lives there |
|---|---|
| `/` | Root of the tree — holds what's needed to boot before anything else is mounted. |
| `/bin` | Essential command binaries needed by all users. |
| `/boot` | Bootloader and kernel files needed to start the system. |
| `/dev` | Device files — how the system exposes hardware devices. |
| `/etc` | System-wide configuration files, including for installed apps. |
| `/home` | Each user's personal directory. |
| `/lib` | Shared libraries required during boot. |
| `/media` | Mount point for removable media (USB drives, etc.). |
| `/mnt` | Temporary mount point for filesystems. |
| `/opt` | Optional, usually third-party, software. |
| `/root` | Home directory of the root user. |
| `/sbin` | Binaries for system administration tasks. |
| `/tmp` | Temporary files — usually cleared on reboot, can be wiped at any time. |
| `/usr` | User programs, libraries, and documentation. |
| `/var` | Variable data: logs, mail queues, web app files, cron data, etc. |

Worth remembering ahead of later domains: most configuration-based hardening happens in `/etc`, and most monitoring/logging work starts in `/var/log`.
