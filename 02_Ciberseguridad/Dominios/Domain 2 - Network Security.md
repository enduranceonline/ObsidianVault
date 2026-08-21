---
tags: [domain-overview, kasiu, fase0, mes1]
domain: 2
status: panoramic-read
source: "Kasiu Tech - Cybersecurity Domains"
read_date: 2026-08-20
deep_dive: false
exam_score: 9/10
exam_date: 2026-08-20
exam_notes: "Q4 (Split Tunneling vs Full Tunnel)"
---

# Domain 2 — Network Security

> **Status:** Panoramic read — Month 1 · Deep dive pending (Month 2 if prioritized)
> **Source:** Kasiu Tech - Cybersecurity Domains · Domain 2 (pp. 17–35)

---

## What this domain is about

The goal is to **control and monitor the flow of information**. The network is the circulatory system of an organization: if an attacker owns the network, they own everything.

The mindset here is that of a **Traffic Engineer and Watchman**, constantly asking two questions: *"Does this packet have permission to be here?"* and *"How do I stop an attacker moving laterally once they clear the first fence?"*

The most critical asset in this domain is **visibility**. You cannot protect what you cannot see.

> **Kasiu tip:** In network security, less is more. Always apply ==Default Deny==. If no specific rule permits the traffic, the system destroys it. Better someone calls because something doesn't work than because your data was stolen.

---

## Domain map — 7 modules

| # | Module | Core concept |
|---|--------|-------------|
| M1 | Secure architectures | DMZ, segmentation, Zero Trust |
| M2 | Firewalls | Evolution, rules, drop vs reject |
| M3 | IDS/IPS | Detection vs prevention, false positives |
| M4 | VPNs & remote access | IPsec, SSL/TLS, split tunneling, ZTNA |
| M5 | Wi-Fi security | WEP→WPA3, 802.1X, wireless attacks |
| M6 | Traffic analysis | Wireshark (packets) vs NetFlow (flows) |
| M7 | Microsegmentation & SDN | East-West traffic, attribute-based policy |

---

## M1 — Secure network architectures

The perimeter model ("inside good, outside bad") is dead. Modern design is **defense in depth**.

### DMZ topologies

| Topology | Description | Trade-off |
|---|---|---|
| **Single Firewall (three-legged)** | One device with ≥3 interfaces: WAN, LAN, DMZ | Cheap, but **total single point of failure** |
| **Back-to-Back (dual firewall)** | Two firewalls in series: exterior handles Internet↔DMZ, interior handles DMZ↔LAN | More robust, more cost and complexity |

> **DMZ golden rule:** traffic must **never** flow directly from Internet to LAN. It terminates in the DMZ (reverse proxy, web server) and *that* system makes a **new request** to the LAN.

### Segmentation

- **VLANs (802.1Q)** — split the broadcast domain at Layer 2. Limitation: *once an attacker lands in a VLAN, every device in that subnet is reachable*.
- ==Microsegmentation== — policy per **workload**, not per subnet. Implemented via SDN or host agents. Two servers on the same VLAN can't talk without an explicit rule.
- ==PVLAN== (Private VLAN) — Layer 2 technique isolating ports **within** the same VLAN (isolated / community / promiscuous ports).

### Zero Trust Architecture (ZTA)

Not a product — a strategy defined by **NIST SP 800-207**. Three components:

| Component | Role |
|---|---|
| ==PE== (Policy Engine) | The brain — decides access based on risk scoring |
| ==PA== (Policy Administrator) | Executes the decision, issues tokens/credentials |
| ==PEP== (Policy Enforcement Point) | Where access is granted or cut (gateway, agent, NGFW) |

> **Kasiu tip:** Zero Trust in three variables — **Identity + Device + Context**. Being in the office on a cable means nothing: outdated antivirus (context) plus a 3 AM login attempt (context) equals denial. Trust is ephemeral and re-evaluated per packet.

### Advanced isolation

- ==Air Gapping== — total physical isolation, no connection to the outside. Nuclear plants, military control systems.
- ==Bastion Host== (Jump Server) — hardened server that is the **only** entry point for administering critical systems. Access via SSH/RDP, then hop onward.
- ==Honeypot== — segment designed to look vulnerable, attracting attackers so their techniques can be studied without risking production.

### Comparison table

| Feature | Traditional segmentation | Microsegmentation | Zero Trust |
|---|---|---|---|
| Control point | Router / perimeter FW | Switch / SDN / hypervisor | Identity & application |
| Visibility | By subnet (IP/port) | By workload | By user and process |
| Trust | Implicit by location | Limited to segment | **None** (continuous verification) |
| Scalability | Hard (network changes) | High (software-defined) | Very high (policy-based) |

---

## M2 — Firewalls: types, rules and management

### Technical evolution (follows the OSI layers)

| Type | Layer | How it works | Limitation |
|---|---|---|---|
| **Packet Filtering** | 3–4 | Stateless. Inspects headers: src/dst IP, port, protocol | No memory of the connection — return traffic must be opened manually |
| **Stateful Inspection** | 3–5 | Maintains a ==State Table== tracking active connections (SYN, SYN-ACK, ACK) | Doesn't see payload content |
| **Application Gateway / Proxy** | 7 | Real intermediary: client → proxy → new request to server | Slowest, heavy processing |
| ==NGFW== | 3–7 | All of the above plus DPI, App-ID, User-ID, integrated IPS | Cost, and blind to encrypted traffic without SSL inspection |

**NGFW capabilities:**
- ==DPI== (Deep Packet Inspection) — looks inside the payload
- ==App-ID== — identifies the application regardless of port (distinguishes "Facebook Chat" from "Facebook Video")
- ==User-ID== — binds rules to users via Active Directory, not just IPs
- Integrated IPS — detects and blocks known exploits in real time

### Rule management

Rules are read **top to bottom** and the **first match applies**.

Rule structure: `Order | Source | Destination | Service/Port | Action | Log`

- ==Implicit Deny== — the last rule of any firewall must be *Deny All*
- ==Shadow Rules== — a common management error where a broader rule above prevents a more specific rule below from ever executing
- **Least privilege** — don't open port 80 to the whole network if only the web server needs it
- **Logging** — log only what's needed, but always capture critical DMZ denies

### Network vs Host firewall

- **Network firewall** — protects the perimeter or segments. Usually dedicated hardware (Fortinet, Palo Alto, Checkpoint)
- **Host-based firewall** — software on the OS (`iptables`, Windows Defender Firewall). **Last line of defense** when the attacker is already on the same segment

> **Kasiu tip:** ==Drop vs Reject==. *Drop* silently discards the packet — the attacker waits for a timeout, which slows down scanning. *Reject* replies with ICMP Port Unreachable, confirming something is there. On the perimeter, **always Drop**: give the enemy no information.

### Modern challenge: encrypted traffic

Over 90% of web traffic is HTTPS, and a firewall can't see inside encrypted packets.

==SSL Decryption / Break-and-Inspect== — the firewall acts as an **authorized man-in-the-middle**: decrypts outbound traffic, inspects it for malware, re-encrypts and forwards. Without it, an NGFW is blind to attacks hidden in encrypted traffic.

> Connects directly to [[Bandit - Level 15]]: the difference between `nc` (readable on the wire) and `openssl s_client` (opaque) is exactly the problem this solves.

---

## M3 — IDS/IPS: detection and prevention

### The operational difference

| | ==IDS== | ==IPS== |
|---|---|---|
| Mode | **Passive** | **Active (in-line)** |
| Placement | SPAN port or network TAP — receives a **copy** | Traffic passes **through** it |
| Action | Alerts, doesn't stop traffic | Drops malicious packets in real time |
| Risk | Attack succeeds while you watch | **False positive = service outage** |

### Detection methods

- **Signature-based** — matches known byte patterns, like an antivirus. Excellent against known attacks (e.g. a specific Log4j exploit), **useless against zero-days**.
- **Anomaly-based** — establishes a ==baseline== of normal traffic. A sudden 50 GB spike on a server that normally moves 1 GB/hour triggers an alert. Can catch unknown attacks.
- **Protocol Analysis** — verifies traffic conforms strictly to RFC standards. Catches malformed packets designed to overflow buffers.

### NIDS vs HIDS

- **NIDS** — monitors a whole network segment. Placed behind the firewall or in the DMZ.
- **HIDS** — installed on the host itself. Sees system logs, file integrity and kernel calls. **Vital for attacks that arrive encrypted and only decrypt at the host.**

### The noise problem

| Outcome | Meaning |
|---|---|
| True Positive | Real attack detected — the goal |
| **False Positive** | Legitimate traffic flagged — causes outages |
| **False Negative** | Attack goes unnoticed — **worst case** |
| True Negative | Benign traffic correctly ignored |

> **Kasiu tip:** Order matters. An IPS placed *outside* the firewall gets bombarded with junk traffic and saturates. Correct design: **Internet → Firewall → IPS → Internal network.** The firewall filters the mass noise; the IPS does the surgical work of finding exploits.

**Leading tools:** ==Snort== (open-source standard, rule-based) · ==Suricata== (Snort's evolution, multithreaded, deep protocol inspection) · ==Zeek== (formerly Bro — focused on metadata and network analysis rather than signature prevention).

---

## M4 — VPNs and secure remote access

A VPN creates an encrypted point-to-point tunnel, guaranteeing **confidentiality and integrity** across public networks.

### The two types

| Type | Connects | Typical technology |
|---|---|---|
| **Site-to-Site** | Two entire networks (HQ ↔ branch) | IPsec. Transparent to users |
| **Remote Access (Client-to-Site)** | One user to the corporate network | SSL/TLS or L2TP/IPsec, via client software |

### Tunnel protocols

**==IPsec==** — Layer 3.
- ==IKE== (Internet Key Exchange) — negotiates keys and algorithms
- ==AH== (Authentication Header) — integrity and authentication, **no encryption** (rarely used today)
- ==ESP== (Encapsulating Security Payload) — the gold standard: encryption + integrity + authentication
- Modes: **Transport** (encrypts payload only) vs **Tunnel** (encrypts the entire original packet, including internal IPs)

**==SSL/TLS VPN==** — Layers 4–7.
- Easier to traverse firewalls (uses port 443, same as web browsing)
- Allows granularity: access to a single web application instead of the whole network

### Advanced concepts

- ==Split Tunneling== **enabled** — only corporate traffic goes through the VPN; Netflix and Spotify go out via the user's own internet. Saves bandwidth, **less secure**.
- ==Full Tunnel== (split tunneling disabled) — **all** user traffic passes through the company, so corporate firewall and IPS apply to their browsing too. More secure.
- **Always-on VPN** — the tunnel comes up automatically as soon as the PC detects internet, before the user even logs in.
- **Endpoint Compliance (Posturing)** — the VPN refuses entry unless requirements are met (active antivirus, current patches).

> **Kasiu tip:** Encryption ≠ VPN. Encryption is the tool (the tunnel walls); the VPN is the complete system including authentication. A 256-bit tunnel with the password `123456` is a steel tunnel with a cardboard door. **MFA is mandatory on any modern VPN.**

### Modern alternative: ZTNA

==ZTNA== (Zero Trust Network Access) is replacing traditional VPN:

- **VPN:** once inside, you have visibility of the network — access by *location*
- **ZTNA:** no persistent tunnel. An invisible connection to a **specific application** after verifying identity and context. The user never touches the internal network.

---

## M5 — Wi-Fi and wireless security

### Protocol evolution (IEEE 802.11)

| Protocol | Encryption | Status |
|---|---|---|
| ==WEP== | RC4 with short IVs | **Completely broken** — crackable in minutes |
| ==WPA== | TKIP (dynamic keys), still RC4 | Temporary fix, obsolete |
| ==WPA2== | **AES** + CCMP | Current standard. Vulnerable at the **4-Way Handshake**: capture it and crack offline. Also vulnerable to ==KRACK== |
| ==WPA3== | **SAE** replaces PSK exchange | Blocks offline dictionary attacks, provides ==Perfect Forward Secrecy== |

**Perfect Forward Secrecy:** discovering today's network password does **not** allow decrypting traffic captured yesterday.

### Authentication modes

- **Personal (PSK)** — everyone shares one password. Doesn't scale: an employee leaves and you must change it for everyone.
- **Enterprise (==802.1X==/EAP)** — the corporate standard. Each user authenticates with their own credentials or a digital certificate. Requires a ==RADIUS== server. **EAP-TLS** is the most secure variant, requiring certificates on both server and client.

### Wireless-specific threats

| Attack | What it is |
|---|---|
| ==Rogue Access Point== | An employee plugs their home router into the office network for better signal — a backdoor with no security |
| ==Evil Twin== | Attacker broadcasts an SSID identical to the corporate one. Devices auto-connect; attacker becomes MITM |
| **Deauthentication attack** | Forged packets force a device to disconnect so the attacker can capture the handshake on reconnect |
| **War Driving** | Locating vulnerable networks from a moving vehicle with high-gain antennas |

> **Kasiu tip:** Does hiding the SSID or MAC filtering improve security? **No.** That's security by obscurity. Aircrack-ng reveals a hidden SSID the moment a legitimate client connects, and MAC addresses are spoofed in seconds. Don't waste time — focus on **WPA3 or 802.1X**.

### Best practices

- **Guest segmentation** — guest network on a fully isolated VLAN with internet access only, never the internal network
- ==WIPS== (Wireless Intrusion Prevention System) — sensors that scan the spectrum to detect and block rogue APs automatically
- **Power control** — tune antenna output so the signal doesn't spill into the street or public areas

---

## M6 — Network traffic analysis

Two approaches: reading the whole letter, or just looking at the envelope to see who writes to whom.

### Packet analysis — Wireshark

The most important protocol analyzer in the world. Captures traffic on an interface and decodes it layer by layer per the OSI model.

**Capture points:**
- ==Port Mirroring / SPAN== — the switch copies traffic from one port to another where the analyzer sits
- ==Network TAP== — physical device inserted in the cable that copies the electrical signal. More reliable than SPAN because it doesn't load the switch CPU

**Critical capabilities:**
- ==Follow Stream== — reconstruct an entire TCP conversation to see, for example, which files were downloaded over HTTP
- Display filters — e.g. `ip.addr == 192.168.1.1 && tcp.port == 443`
- Anomaly detection — excessive retransmissions, malformed packets, SYN scans

### Flow analysis — NetFlow / IPFIX

NetFlow stores **metadata**, not payload. A flow is defined by the ==5-tuple==:

1. Source IP · 2. Destination IP · 3. Source port · 4. Destination port · 5. Protocol

- Far more scalable than full packet capture — visibility across an entire enterprise without saturating storage
- **Security use: detecting data exfiltration.** If an internal server sends 50 GB to an unknown foreign IP, NetFlow catches it **even if the content is encrypted**

### Management protocols

- ==SNMP== — queries device health (CPU, bandwidth, temperature). **Warning:** v1 and v2 send the community string in **plaintext**. Only **SNMPv3** is acceptable today — it supports encryption and strong authentication.
- ==Syslog== — the standard for sending network event logs to a centralized server (SIEM)

> **Kasiu tip:** Investigating an incident? Use **NetFlow** for the *when* and the *who* — it's the phone call log. Once you locate the suspicious flow, use **Wireshark** for the *what* — that's the recording of the call.

### Malicious traffic patterns

| Pattern | Signature |
|---|---|
| ==Beaconing== | Periodic, small communications from an infected host to a ==C2== (Command and Control) server |
| ==DNS Tunneling== | DNS used to exfiltrate data, since port 53 is almost always open |
| ==ARP Spoofing== | Unsolicited ARP replies indicating a man-in-the-middle attack on the local network |

> Both beaconing and DNS tunneling detection reduce to frequency analysis on log data — the `sort | uniq -c | sort -rn` pattern from [[Linux - Sorting and Deduplication]], and `sort | uniq -u` for the rare-event side.

---

## M7 — Microsegmentation and SDN

### SDN: Software Defined Networking

Traditionally the brain (control plane) and muscles (data plane) live in the same box. SDN separates them.

- **Control Plane** — centralized in a software controller. Decides where traffic goes.
- **Data / Forwarding Plane** — physical devices only execute the controller's orders.
- **Advantage:** apply security changes across the entire network instantly from one point.
- **Risk:** if the controller is compromised, the attacker owns the whole infrastructure. **Controller security is critical.**

### Microsegmentation

Isolates each **workload** individually, even within the same network segment.

- **Implementation:** distributed firewall at the hypervisor level (e.g. VMware NSX) or agents on the OS
- ==Attribute-based policies== — rules by **tag** instead of IP: *"any server tagged 'Database' may only receive traffic from tag 'App Server' on port 3306"*. The rule follows the server even if its IP changes.

### East-West vs North-South

| Direction | What it is | Controlled by |
|---|---|---|
| ==North-South== | Traffic entering or leaving the data center (Internet ↔ server) | Perimeter firewalls |
| ==East-West== | Traffic **between** servers or VMs inside the network | ❗ Perimeter firewalls **don't see it** |

**Reality: 80% of current traffic is East-West.** Microsegmentation is the only way to stop an attacker moving laterally once past the perimeter.

### NFV — Network Functions Virtualization

Replacing dedicated hardware (physical firewalls, physical IPS) with software virtual appliances.

- Enables ==Service Chaining== — logically chaining security services: a packet arrives, the SDN controller sends it first to the virtual FW, then the virtual IPS, then the server, **without changing a single cable**.

### Summary table

| Technology | Scope | Enforcement point | Agility |
|---|---|---|---|
| VLAN (802.1Q) | Network level (broadcast domain) | Physical switch | Low (manual) |
| SDN | Full orchestration | Central controller | Very high (API) |
| Microsegmentation | Application / VM level | Hypervisor / agent | Extreme (tag-based) |

> **Kasiu tip:** To understand microsegmentation, forget IPs. Think of it as *"security centred on process identity"*. If a web server is compromised, microsegmentation prevents it from talking to **another web server in its own group** — something traditional segmentation would allow, since they share a subnet.

---

## Exam — Domain 2 (10 questions)

> Self-test after panoramic read. **Result: 9/10** — only miss was Q4.

**Q1.** Designing an architecture for a web server that must be reachable from the Internet but needs to query an internal database. Most secure configuration?
- a) Both servers in the LAN, protected by the perimeter firewall
- b) Web server in the DMZ, database in the LAN, allowing only web→DB traffic on the specific port (e.g. 3306)
- c) Both in the DMZ so they don't infect the LAN if hacked
- d) Open a direct port from the Internet to the database to improve latency

**Q2.** Firewall rules permit traffic on port 443, but an attacker is sending malicious application commands through it. What technology is missing?
- a) Stateful Inspection · b) Packet Filtering · c) Deep Packet Inspection (DPI) / NGFW · d) NAT

**Q3.** In an IDS/IPS deployment, what is the main disadvantage of placing an IPS "in-line"?
- a) It can't block traffic, only alert
- b) If the device fails or hits a critical false positive, it can cause a service outage
- c) It requires a SPAN copy of the traffic, saturating the switch
- d) It can only detect known signatures, not anomalies

**Q4.** A remote user connects via VPN. You observe they can browse the Internet through their own home router while keeping the connection to office files. What configuration is active?
- a) Full Tunnel · b) Split Tunneling · c) IPsec Transport Mode · d) Clientless SSL

**Q5.** Why is WPA3 significantly more secure than WPA2 against offline brute force?
- a) It mandates a longer password
- b) It hides the SSID automatically
- c) It uses SAE (Simultaneous Authentication of Equals), preventing an attacker from testing passwords without interacting with the AP
- d) It uses WEP encryption as an additional layer

**Q6.** Investigating possible mass data exfiltration to a foreign IP three days ago. No packet captures from that date. Most useful resource?
- a) Endpoint antivirus logs · b) NetFlow records from the egress router · c) A Wireshark capture taken today · d) The user's browser history

**Q7.** In microsegmentation and data centers, what does "East-West traffic" mean?
- a) Traffic entering from the Internet toward servers
- b) Traffic flowing between servers or VMs within the same internal network
- c) Traffic leaving the network toward cloud services (SaaS)
- d) Network management traffic exclusively

**Q8.** What is the main function of the Policy Enforcement Point (PEP) in a Zero Trust architecture?
- a) The brain that analyses user risk
- b) The component storing the password database
- c) The physical or logical place (gateway, firewall) where access is permitted or cut according to policy
- d) The component that generates auditor reports

**Q9.** You receive an alert that an internal machine is "beaconing". What does this mean technically?
- a) The machine is trying to guess other servers' passwords
- b) The machine is sending periodic signals to a Command and Control (C2) server awaiting instructions
- c) The machine has a hardware fault in its network card
- d) The machine is broadcasting to find a printer

**Q10.** You want to see which applications (LinkedIn, BitTorrent) your users are running, regardless of the port they use. What technical feature do you need?
- a) Standard port-based ACLs · b) SNMPv3 · c) Application Identification (App-ID) in an NGFW · d) MAC address filtering

<details>
<summary>✅ Answers</summary>

1. **b) Web server in DMZ, database in LAN.** Standard n-tier design. Never expose the database directly, and don't co-locate it with the web server if avoidable.

2. **c) DPI / NGFW.** A traditional firewall only sees that port 443 is open; an NGFW inspects the content of HTTPS traffic (with SSL inspection) to identify the real application.

3. **b) Single point of failure / service outage.** Being physically in the path, if the IPS errs or powers off, traffic stops.

4. **b) Split Tunneling.** Traffic is *divided*: corporate through the tunnel, personal through the user's own internet. ❌ **Answered a) Full Tunnel.**

5. **c) SAE protocol.** WPA3 eliminates the vulnerable WPA2 exchange that allowed capturing the handshake and attacking it offline at high speed.

6. **b) NetFlow.** Ideal for historical network forensics — small storage footprint, records volume in bytes plus source/destination IPs.

7. **b) Traffic between internal servers.** This is what microsegmentation protects to prevent lateral movement.

8. **c) Where access is permitted or cut.** The PEP is the executing arm of Zero Trust policy.

9. **b) Signals to a C2 server.** Typical behaviour of malware awaiting orders from its botnet operator.

10. **c) App-ID in an NGFW.** Next-gen firewalls don't trust ports — they analyse the traffic signature to identify the application.

> **Exam tip:** In network exams, always identify **which OSI layer** the problem occurs at. If the question mentions *applications*, the answer is usually Layer 7 (NGFW, WAF, Proxy). If it mentions *routes* or *IPs*, look at Layer 3.

</details>

---

## Error analysis — Q4

**Answered:** a) Full Tunnel · **Correct:** b) Split Tunneling

The confusion is in the direction of the definition. The distinguishing clue in the question is *"can browse the Internet using their own home router"*:

| | Where user's internet traffic goes | Security |
|---|---|---|
| **Full Tunnel** | Through the company. Corporate FW and IPS apply | More secure |
| **Split Tunneling** | Directly through the user's own connection | Less secure — corporate controls don't see it |

**Memory hook:** the traffic **splits** in two — corporate through the tunnel, personal out the local door. If the user reaches the Internet without passing through the company, it's split.

Full Tunnel is the more secure option precisely because it's the more inconvenient one: everything routes through the company, so everything is inspected.

---

## Connections to practical work

Concepts from this domain already met hands-on during Bandit:

| Domain 2 concept | Where it appeared |
|---|---|
| Ports, localhost, TCP sockets | [[Bandit - Level 14]] — `nc localhost 30000` |
| Plaintext vs encrypted channel | [[Bandit - Level 14]] vs [[Bandit - Level 15]] |
| TLS handshake, cipher suites, PFS | [[Bandit - Level 15]] — `openssl s_client` output |
| Self-signed certificate / broken chain of trust | [[Bandit - Level 15]] — SnakeOil cert, verify error 18 |
| Key-based authentication | [[Bandit - Level 13]] — `ssh -i`, `authorized_keys` |
| Bastion host concept | [[Bandit - Level 13]] — pending in the homelab |
| Beaconing / DNS tunneling detection | [[Linux - Sorting and Deduplication]] — frequency analysis |

Architecture applied to a real project: `Homelab - Arquitectura de red segura (teoría aplicada)`.

---

## Links
- [[Domain 1 - Cybersecurity Fundamentals]]
- [[Domain 3 - Endpoint Security]]
- [[Fase_0 - Dashboard]]
- [[Semana_03]]
