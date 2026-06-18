---
tags: [linux, fundamentals, distributions]
source: personal note — Kali Linux Introducción
---

# Linux Distributions

## Debian

Debian is known for stability and reliability, used across desktops, servers, and embedded systems. Package management runs through APT (Advanced Package Tool), which handles installing, updating, and patching software, either automatically or manually.

**Strengths**
- Long-term support: security updates for up to 5 years on a given release.
- Strong track record on security and privacy.
- A large contributor community, which tends to mean fast patches when vulnerabilities show up.
- High flexibility — can be configured for almost any use case.

**Trade-offs**
- Steeper learning curve than Ubuntu or Fedora.
- Initial configuration takes more manual work, though that's also what gives an advanced user more control.

**Why it matters here**: Kali Linux is built on Debian, so Debian fundamentals (APT, filesystem conventions, general security posture) carry over directly.

```bash
cat /etc/os-release    # check which distro and version you're running
```

*(extend this note with Ubuntu, Kali-specific notes, etc. as you encounter them)*
