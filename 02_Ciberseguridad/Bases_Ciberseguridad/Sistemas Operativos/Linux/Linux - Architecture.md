---
tags: [linux, fundamentals]
source: adapted from HTB Academy — Linux Fundamentals
---

# Linux Architecture

Linux can be thought of as four layers stacked on top of each other:

- **Hardware** — the physical components: CPU, RAM, disk, and other peripherals.
- **Kernel** — the core of the OS. It virtualizes and arbitrates access to the hardware, giving each running process its own view of memory and CPU time, and keeping processes from interfering with each other.
- **Shell** — the command-line interface that lets a user send instructions to the kernel.
- **System utilities** — the tools and programs built on top of the kernel that expose the system's functionality to the user, from a single command like `ls` to a full desktop environment.

Each layer depends on the one below it: the shell talks to the kernel, and the kernel talks to the hardware.
