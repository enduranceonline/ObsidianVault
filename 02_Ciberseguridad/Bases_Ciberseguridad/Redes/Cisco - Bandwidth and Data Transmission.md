---
tags: [redes, networking-basics, practice]
source: NetAcad Networking Basics — Module 1
---
---
# Cisco - Bandwidth and Data Transmission

## Signal Transmission
Three ways a signal physically travels over a network medium:
- **Electrical** — pulses on copper wire.
- **Optical** — light pulses, used in fiber.
- **Wireless** — infrared, microwave, or radio waves through the air.

![[Pasted image 20260618164234.png]]

---
## Bandwidth vs Throughput vs Data Rate
- **Bandwidth** — the *theoretical maximum* capacity of a medium to carry data.
- **Throughput** — the *actual* measured rate of data transfer; includes the effect of latency and overhead, so it's always ≤ bandwidth. In practice this is the term you'll hear most.
- **Data rate** — NetAcad uses this as effectively synonymous with throughput.

**Bottleneck rule**: in a path with multiple segments, the overall throughput can never exceed the slowest segment in that path — the rest being fast doesn't help once you hit that bottleneck.

![[Pasted image 20260618164210.png]]

---
## Bandwidth Units

| Unit | Meaning               |                                           |
| ---- | --------------------- | ----------------------------------------- |
| Kbps | thousands of bits/sec | 1 Kbps = 1.000 bps = 10³ bps              |
| Mbps | millions of bits/sec  | 1 Mbps = 1.000.000 bps = 10⁶ bps          |
| Gbps | billions of bits/sec  | 1 Gbps = 1.000.000.000 bps = 10⁹ bps      |
| Tbps | trillions of bits/sec | 1 Tbps = 1.000.000.000.000 bps = 10¹² bps |

---
## Personal Data Types
*(privacy-relevant — revisit when covering Dominio 5 - Seguridad de Aplicaciones y Datos)*
- **Volunteered** — data you give directly (e.g. filling out a form).
- **Observed** — data collected by watching your behavior (e.g. location tracking).
- **Inferred** — data deduced by analyzing other data (e.g. a credit card company inferring habits from purchase history).

---
## Connected Device Vocabulary
- **Sensor** — detects/measures something in the environment.
- **Actuator** — produces physical movement.
- **RFID tag** — uses radio frequency to identify/track an object.
- **SOHO network** — Small Office/Home Office network; lets devices in a home or small office connect to a corporate network or shared resources.

---