---
tags: [redes, networking-basics, network-components]
source: NetAcad Networking Basics — Module 2
date: 2026-06-22
exam_score: 6/10
exam_notes: "Q3 (DSL vs satellite), Q4 (satellite vs dial-up), Q7 (P2P scenario), Q10 (P2P app definition)"
---

# Cisco - Network Components

## The Three Hardware Categories

Every network infrastructure is made of three types of hardware:

| Category | Role | Examples |
|----------|------|---------|
| ==End Devices== | Source or destination of data | PC, laptop, printer, IP phone, tablet, server |
| ==Intermediary Devices== | Move and direct data between end devices | Router, switch, wireless router, firewall, AP |
| ==Network Media== | The channel data travels through | LAN cable, WAN link, wireless (radio) |

**End devices** are the interface between the human and the network. Every message originates at an end device and arrives at one. They are identified by addresses — when a host sends a message, it uses the destination's address to route it correctly.

**Intermediary devices** never originate or consume data — they forward it. They make decisions about the best path for data to travel and handle failures by rerouting traffic along alternate paths.

**Network media** is the physical or wireless channel. Three types:
- ==LAN media== — copper cable, used inside a building.
- ==WAN media== — typically fiber or leased lines, connects distant networks.
- ==Wireless media== — radio frequencies or infrared, no physical cable.

---

## Client / Server Model

All hosts on a network are classified by their role in a communication:

- **Server** — has software installed that provides a service (email, web pages, files) to other hosts. Each service requires its own server software.
- **Client** — has software that requests and displays information from a server (e.g. a web browser).

A single computer can run multiple server roles simultaneously (email + web + file server) and a single client can connect to multiple servers at once.

| Server type | Software example | Client software |
|-------------|-----------------|----------------|
| Email | Mail server | Microsoft Outlook |
| Web | Web server | Browser (Chrome, Firefox) |
| File | File server | Windows File Explorer |

---

## Peer-to-Peer (P2P) Networks

In a ==P2P network==, devices act as both client and server — there is no dedicated server. Common in homes and small offices.

**Advantages:** easy to set up · low cost · no dedicated server required · good for simple tasks (file sharing, printer sharing).

**Disadvantages:** no centralized administration · less secure · not scalable · performance degrades when a device serves many requests simultaneously.

> **P2P scenario to recognize:** a user shares a printer *attached to their own workstation* — that workstation is acting as both a client (for its own user) and a server (providing the printer to others). Contrast with a *network printer with its own NIC* — that's a dedicated device, which is client/server, not P2P.

### P2P Applications

A P2P *application* (e.g. BitTorrent) takes this further: each device acts as client and server **simultaneously** within the same session — downloading from peers while uploading to others at the same time.

Architecture of a P2P app: each device runs a **user interface** (visible) + a **background service** (always on, handling requests from other peers). Resources are decentralized; some hybrid systems use a central index server only to locate resources, but the transfer itself is peer-to-peer.

> **Exam trap:** "each device can act as client and server, but *not simultaneously*" describes a basic P2P *network*. "Each device acts as client and server *simultaneously*" describes a P2P *application*. These are different answers to different questions.

---

## Network Infrastructure

The ==network infrastructure== is the platform that supports communications — the stable, reliable channel over which data flows. It includes all three hardware categories above working together.

A message's path from source to destination can be as simple as a single cable between two computers, or as complex as crossing multiple routed networks across continents. Intermediary devices handle the routing decisions along the way.

---

## Exam — Module 2 Network Components (6 questions)

> Self-test. Answers below — commit before checking.

**Q1.** What type of network is defined by two computers that can both send and receive requests for resources?
- a) campus · b) peer-to-peer · c) enterprise · d) client/server

**Q2.** What are two functions of end devices on a network? *(choose two)*
- a) They filter the flow of data to enhance security.
- b) They are the interface between humans and the communication network.
- c) They provide the channel over which the network message travels.
- d) They originate the data that flows through the network.
- e) They direct data over alternate paths in the event of link failures.

**Q6.** Which device is an intermediary device?
- a) server · b) PC · c) firewall · d) smart device

**Q7.** Which scenario describes a peer-to-peer network?
- a) A user has shared a printer attached to the workstation.
- b) Users access shared files from a file server.
- c) A user visits a webpage on the company website.
- d) Users print documents from a network printer that has a built-in NIC.

**Q8.** Which term describes a network device with the primary function of providing information to other devices?
- a) server · b) client · c) console · d) workstation

**Q9.** What is an advantage of the peer-to-peer network model?
- a) centralized administration · b) high level of security · c) ease of setup · d) scalability

**Q10.** What is a characteristic of a peer-to-peer *application*?
- a) One device is designated server and one is designated client for all communications.
- b) Each device can act both as a client and a server, but not simultaneously.
- c) The resources required for the application are centralized.
- d) Each device using the application provides a user interface and runs a background service.

<details>
<summary>✅ Answers</summary>

1. **b) peer-to-peer.** Both devices can request and provide resources.
2. **b and d.** End devices are the human interface and the origin/destination of data. Filtering is done by intermediary devices (firewalls); providing the channel is the role of network media; alternate routing is done by routers.
6. **c) firewall.** Servers and PCs are end devices. A firewall sits between networks, directing and filtering traffic — an intermediary role.
7. **a) A user has shared a printer attached to the workstation.** The workstation itself is sharing its own resource — classic P2P. A network printer with its own NIC is a dedicated device (client/server). Accessing a file server or visiting a web server are both client/server models.
8. **a) server.** A server's primary role is providing services/information to clients.
9. **c) ease of setup.** P2P is simple and cheap to configure. It lacks centralized admin, security, and scalability — those are all disadvantages.
10. **d) Each device provides a user interface and runs a background service.** Option b describes a basic P2P network, not a P2P application. In a P2P app, each device acts as client and server *simultaneously*.

</details>

---

## Links
- [[Cisco - Bandwidth and Data Transmission]]
- [[Cisco - ISP Connectivity]]
- [[MOC - Redes]]
