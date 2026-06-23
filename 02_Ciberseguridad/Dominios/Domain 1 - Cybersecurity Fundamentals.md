---
tags: [domain-overview, kasiu, fase0, mes1]
domain: 1
status: panoramic-read
source: "Kasiu Tech - Cybersecurity Domains"
read_date: 2026-06-22
deep_dive: false
exam_score: 4/6
exam_date: 2026-06-22
exam_notes: "Q4 (NIST Protect vs Recover), Q5 (Transfer vs Mitigate)"
---

# Domain 1 — Cybersecurity Fundamentals

> **Status:** Panoramic read — Month 1 · Deep dive pending (Month 2 if prioritized)
> **Source:** Kasiu Tech - Cybersecurity Domains · Domain 1 (pp. 4–16)

---

## What this domain is about

The goal of Domain 1 is to transform security from "IT spending" into a **business function**. Without these foundations, every technical tool (firewall, EDR, SIEM) gets configured blindly.

The mindset here is that of a **Security Architect**: not running commands yet, but designing the blueprint — who holds the keys, which laws apply, and what happens when the walls fail.

---

## Domain map — 5 modules

| # | Module | Core concept |
|---|--------|-------------|
| M1 | CIA Triad | The 3 pillars of information security |
| M2 | Threats & Threat Actors | Who attacks and how |
| M3 | Frameworks: NIST / ISO 27001 / CIS | Maps for managing risk |
| M4 | Risk Management & BIA | How to evaluate and treat risk |
| M5 | Compliance: GDPR / ENS / NIS2 | Legal obligations in the EU/Spain |

---

## M1 — CIA Triad

The ==CIA Triad== is the foundational model for information security policy. Strengthening one pillar can weaken another — it's a triangle of trade-offs.

**Confidentiality** — information is accessible only to those authorized.
- Mechanisms: **Encryption** (at rest / in transit), **ACLs**, data classification (Public / Internal / Confidential).

**Integrity** — data is accurate, complete, and unmodified.
- Mechanisms: **Hashing** (SHA-256, SHA-3), **Digital Signatures**, Checksums.

**Availability** — systems and data are ready when needed.
- Mechanisms: Redundancy (eliminate ==SPOF== — Single Point of Failure), **High Availability** clusters, Backups & ==DRP==, Anti-DDoS.

**Bonus concepts** (advanced level):
- ==Authenticity==: verifying the identity of user or process.
- ==Non-Repudiation==: a user cannot deny having performed an action.

---

## M2 — Threats & Threat Actors

Security design starts with understanding *who* attacks and *why*.

**Threat Actors** (classified by origin and goal):

| Actor | Motivation | Skill |
|-------|-----------|-------|
| ==Script Kiddies== | Ego / curiosity | Low — uses others' tools |
| ==Hacktivists== | Political / ideological | Variable |
| ==Cybercriminals== | Financial gain | High — organized crime |
| ==State-Sponsored / APT== | Espionage / sabotage | Very high — near-unlimited resources |
| ==Insiders== | Revenge / negligence | Variable — already inside |

**Threat Types:**
- **Malware**: Virus/Worms, ==Ransomware==, Spyware/Keyloggers.
- **Social Engineering**: ==Phishing== (email), ==Vishing== (voice), ==Smishing== (SMS).
- **Network Attacks**: DoS / ==DDoS==.
- **Vulnerability Exploitation**: ==Zero-Day== exploits.

**The Threat Nexus** — risk only exists when all three align:
```
Threat (someone who wants to attack)
  + Vulnerability (a flaw in your system)
  + Asset (something of value)
= Real Risk
```
Remove any one element → risk collapses.

> **APT tip:** The "P" in APT stands for *Persistent*. A common attacker hits and runs. An ==APT== enters, hides, creates backdoors, and can remain for months collecting data undetected. Patience is their main weapon.

---

## M3 — Frameworks: NIST / ISO 27001 / CIS Controls

A **framework** is a set of best practices designed to help organizations manage cybersecurity risk.

**NIST Cybersecurity Framework (NIST CSF)**
- Voluntary / flexible. The gold standard especially in the US.
- 5 core functions: ==Identify== → ==Protect== → ==Detect== → ==Respond== → ==Recover==.

**ISO/IEC 27001**
- Certifiable international standard.
- Implements an ==ISMS== (Information Security Management System).
- Based on ==PDCA== cycle: Plan → Do → Check → Act.
- **Annex A**: catalog of technical, organizational, physical, and legal controls.

**CIS Controls** (Center for Internet Security)
- Tactical and technical — a prioritized action list (formerly SANS Top 20).
- Divided by implementation groups: ==IG1== (basic hygiene) → IG2 → IG3.

**Quick comparison:**

| Framework | Nature | Primary goal |
|-----------|--------|-------------|
| ==NIST CSF== | Voluntary / guide | Risk management & communication |
| ==ISO 27001== | Certifiable | Governance & compliance |
| ==CIS Controls== | Technical list | Mitigate specific attacks |

> **Memory tip:** ISO 27001 gets you the *medal* (certification); NIST is the *language* you use with management; CIS Controls is the *task list* you hand to the technician tomorrow morning.

---

## M4 — Risk Management & BIA

Risk management is the process of identifying, evaluating, and responding to threats. It decides *which* controls from M3 to actually implement.

**Risk Management Cycle:**
1. Asset Identification — what do we have?
2. Threat / Vulnerability Identification — what can happen and where are the weaknesses?
3. Risk Analysis:
   - ==Qualitative==: expert opinion + scales (Low / Medium / High). Fast, less precise.
   - ==Quantitative==: numbers and money.
     - ==SLE== (Single Loss Expectancy) = Asset Value × Exposure Factor
     - ==ALE== (Annualized Loss Expectancy) = SLE × Annual Rate of Occurrence

**Risk Treatment Options:**

| Option | Action |
|--------|--------|
| **Mitigate** (Reduce) | Install controls — firewall, encryption |
| **Transfer** (Share) | Cyber insurance, outsourcing |
| **Accept** | Cost of control > potential loss |
| **Avoid** | Stop the activity that generates the risk |

**Business Impact Analysis (==BIA==)**
Determines how long the business can survive without a critical process. Foundation for continuity planning.

Key BIA metrics (seen again in Domain 11):
- ==RTO== (Recovery Time Objective): maximum acceptable downtime.
- ==RPO== (Recovery Point Objective): maximum acceptable data loss (in time).

> **Risk ≠ Threat:** The threat is the shark in the sea; the risk is the probability it bites you if you jump in. Security doesn't eliminate sharks — it gives you a cage (mitigation) or tells you not to swim there (avoidance).

---

## M5 — Compliance: GDPR / ENS / NIS2

Legal framework applicable in the EU and Spain. Non-compliance = significant fines or operational shutdown.

**==GDPR== / RGPD** — General Data Protection Regulation
- The world's strictest privacy regulation. Protects EU citizens' personal data.
- Key principles:
  - **Privacy by design and by default**.
  - Rights: ==ARSULIPO== (Access, Rectification, Erasure, Limitation, Portability, Opposition).
  - **Breach notification**: max ==72 hours== to notify the authority (AEPD in Spain).
  - ==DPO== (Data Protection Officer): mandatory role in certain organizations.

**==ENS==** — Esquema Nacional de Seguridad (Spain only)
- Mandatory for the **public sector** and their technology providers.
- Dimensions: Confidentiality, Integrity, Availability, Authenticity, Traceability.
- System categories: **Basic / Medium / High** (by incident impact).
- 75 security measures across three frameworks: Organizational, Operational, Protection.

**==NIS2==** — Network and Information Security Directive 2
- Covers "essential sectors" (energy, transport, health) and "important sectors" (food, postal, waste).
- Key additions:
  - **Board-level accountability**: senior management can be held personally liable.
  - **Supply chain security**: companies must audit their suppliers' security posture.
  - **Incident reporting**: early alert in ==24 hours==, detailed report in ==72 hours==.

> **Memory tip:** GDPR protects the *Person* (privacy); ENS protects *Spanish Public Administration* (digital trust); NIS2 protects *Society's Infrastructure* (so the lights and water don't go out from a hack).

**Compliance ≠ Security**
- Compliance: checking a box on a list — a static snapshot.
- Security: an ongoing active defense process.
- Goal: use compliance as a minimum baseline, then build real security on top.

---

## Exam — Domain 1 (6 questions)

> Self-test after panoramic read. Answers below — resist checking until you've committed to an answer.

**Q1.** An attacker breaks into an online store's database and changes all product prices to €0. Which CIA pillar was primarily compromised?
- a) Confidentiality
- b) Integrity
- c) Availability
- d) Non-repudiation

**Q2.** What is the main difference between qualitative and quantitative risk analysis?
- a) Qualitative uses ALE formulas; quantitative uses colors (Red/Green).
- b) Qualitative uses expert opinion and scales; quantitative uses numbers and monetary values.
- c) Quantitative is faster to perform than qualitative.
- d) No difference — both terms are synonymous in ISO 27001.

**Q3.** NIS2 introduces significant new liability. Who is directly affected?
- a) Only L1 systems technicians.
- b) EU citizens, who can now be fined.
- c) Senior management and boards of directors.
- d) Only non-EU companies operating in the cloud.

**Q4.** Which NIST CSF function is responsible for implementing safeguards to ensure critical service delivery?
- a) Identify
- b) Protect
- c) Detect
- d) Recover

**Q5.** A company buys cyber insurance to cover ransomware attack costs. Which risk treatment strategy is this?
- a) Mitigation
- b) Avoidance
- c) Acceptance
- d) Transfer

**Q6.** Which framework is best for a technical company seeking a prioritized list of "basic hygiene" controls to stop the most common attacks?
- a) ISO 27001
- b) GDPR
- c) CIS Controls (IG1)
- d) Business Impact Analysis (BIA)

<details>
<summary>✅ Answers</summary>

1. **b) Integrity.** Data was modified without authorization. It may still be available and not stolen (confidentiality intact), but it's no longer accurate.
   
2. **b) Qualitative = opinion/scales; Quantitative = numbers/money.** Memory trick: Quantitative = *Quantity* (of money).
   
3. **c) Senior management.** NIS2 makes cybersecurity a board-level priority.
   
4. **b) Protect.** This is where proactive technical and administrative controls are implemented.
   
5. **d) Transfer.** The financial impact is shared with a third party (the insurer).
   
6. **c) CIS Controls.** The most tactical and technical of the three frameworks.

> **Exam tip:** When torn between two "Risk" options — risk is never eliminated 100%; there's always residual risk. If an answer says "eliminate risk entirely", be suspicious.

</details>

---

## Links
- [[Domain 2 - Network Security]]
- [[Fase_0 - Dashboard]]
- [[Semana_02]]
