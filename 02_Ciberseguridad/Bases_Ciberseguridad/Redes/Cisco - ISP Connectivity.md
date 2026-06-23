---
tags: [redes, networking-basics, isp, connectivity]
source: NetAcad Networking Basics — Module 2
date: 2026-06-22
---

# Cisco - ISP Connectivity

## What is an ISP?

An ==ISP== (Internet Service Provider) provides the link between a private network and the internet. It can be a cable provider, telephone company, cellular carrier, or an independent provider leasing bandwidth from another company.

ISPs connect to each other in a hierarchical mesh to form the internet backbone — a high-speed fiber-optic infrastructure that interconnects major metropolitan areas globally. The backbone ensures traffic takes the shortest path from source to destination.

**Additional ISP services** (beyond connectivity): email hosting · web hosting · FTP hosting · application and media hosting · VoIP · equipment co-location · technical support.

---

## Home Connection Options

### Direct vs Router

| Setup | Description | Recommended? |
|-------|-------------|-------------|
| Single PC + modem | Direct connection to ISP | ❌ No security |
| Integrated router + modem | Router between devices and ISP | ✅ Standard setup |

A router provides IP address assignment, security for internal hosts, wired switch ports, and a wireless access point — all typically combined in a single home device.

---

## ISP Connection Types

| Type | Medium | Notes |
|------|--------|-------|
| ==DSL== | Existing telephone copper wire | High speed · always-on · splits into 3 channels (voice / download / upload) · speed degrades with distance from central office |
| ==Cable== | Coaxial cable (same as TV) | High bandwidth · always-on · requires cable modem |
| ==Cellular== | Cell phone network | Available anywhere with signal · carrier meters bandwidth · may charge for overages |
| ==Satellite== | Radio waves via orbiting satellite | Works anywhere with clear sky view · good speeds · high equipment/install cost · needs line of sight |
| ==Dial-up== | Standard telephone line | Very low bandwidth · not always-on · only when no other option exists |
| ==Fiber-optic== | Fiber cable (metro areas) | Highest bandwidth · supports internet + phone + TV · increasingly common in cities |

---

## DSL — How the 3 Channels Work

==DSL== splits a single telephone line into three channels so voice and internet coexist without interfering:

1. **Voice channel** — regular phone calls, unaffected by internet use.
2. **Download channel** — faster, for receiving data from the internet.
3. **Upload channel** — slightly slower, for sending data.

Speed and quality depend on the quality of the copper line and the **distance from the telephone company's central office** — the further away, the slower the connection.

---

## Choosing the Right Connection

```
No mobile coverage + no wired infrastructure → Satellite
No wired infrastructure but mobile coverage → Cellular
Existing phone line available → DSL
Existing cable TV service → Cable
Last resort / traveling / nothing else → Dial-up
```

> **Exam trap — DSL vs Satellite:** "high speed digital over phone lines" = ==DSL==. Satellite also provides high speed but uses radio waves through the air, not phone lines. The discriminator is always the medium.

> **Exam trap — Satellite vs Dial-up:** a remote area with *no mobile coverage and no wired connectivity* eliminates DSL, cable, and cellular. Dial-up also requires a telephone line (wired infrastructure) — so it's also eliminated. Only ==satellite== works without any ground infrastructure.

---

## Exam — Module 2 ISP Connectivity (5 questions)

> Self-test. Answers below.

**Q1.** What is a service that provides an internet data signal on the same network that delivers broadcast television?
- a) Cellular · b) DSL · c) Guest access · d) Cable internet

**Q2.** What is a service that provides high bandwidth, always-on connection using existing land-line telephone wires?
- a) Cellular · b) Guest access · c) Cable · d) DSL

**Q3.** What ISP connection type provides high speed digital transmission over regular phone lines?
- a) Satellite · b) DSL · c) Cell modem · d) Dial-up · e) Cable modem

**Q4.** What type of internet connection would be best for a residence in a remote area without mobile phone coverage or wired connectivity?
- a) DSL · b) Satellite · c) Cellular · d) Dial-up

**Q5.** Which term correctly describes the function of an ISP?
- a) Responsible for providing the link between a private network and the internet
- b) Responsible for managing local networks
- c) Responsible for the maintenance of SOHO networks
- d) Responsible for providing security on private networks

<details>
<summary>✅ Answers</summary>

1. **d) Cable.** Cable internet uses the same coaxial cable as TV service.
2. **d) DSL.** Digital Subscriber Line runs over existing telephone copper wires.
3. **b) DSL.** "Phone lines" is the discriminator — satellite uses air, not phone lines.
4. **b) Satellite.** No mobile → eliminates cellular. No wired → eliminates DSL and cable. Dial-up also needs a phone line (wired). Only satellite works with no ground infrastructure, as long as there's a clear view of the sky.
5. **a) Responsible for providing the link between a private network and the internet.** ISPs don't manage your LAN or secure your network — they provide the external connection.

</details>

---

## Links
- [[Cisco - Network Components]]
- [[Cisco - Bandwidth and Data Transmission]]
- [[MOC - Redes]]
