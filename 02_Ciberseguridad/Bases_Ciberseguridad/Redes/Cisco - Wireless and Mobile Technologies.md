---
tags: [cisco, netacad, redes, wireless, mobile, practice]
source: Cisco Networking Basics — Module 3 (Wireless and Mobile Networks)
quiz_score: 10/11
quiz_notes: "Q6 — Cisco defines tethering as Bluetooth/USB only; Wi-Fi sharing is 'mobile hotspot'"
---

# Cisco - Wireless and Mobile Technologies

A smartphone carries **five separate radios**, each solving a different problem. Most confusion comes from treating them as interchangeable — they aren't, and the distinguishing factor is almost always **range**.

---

## The five technologies at a glance

| Technology | Range | Purpose | Direction |
|---|---|---|---|
| ==NFC== | **< 4 cm** | Contactless payment, tap-to-pair | Two-way |
| ==Bluetooth== | ~10 m (up to **100 m** class 1) | Replace cables to accessories | Two-way |
| ==Wi-Fi== | ~50–100 m indoors | Local network + internet access | Two-way |
| ==Cellular== (GSM / 4G / 5G) | Kilometres | Voice, SMS, internet anywhere | Two-way |
| ==GPS== | Global (satellite) | Geolocation, ~10 m accuracy | **Receive only** |

> **Range is the discriminator.** When a question describes a scenario, the distance usually identifies the technology on its own: centimetres → NFC · metres → Bluetooth · a building → Wi-Fi · a city → cellular.

**GPS is receive-only.** The phone never transmits to the satellites — it listens to signals from several and calculates its own position from the timing differences. That's why GPS works with no data plan and why it can't be "traced" by the satellite itself.

---

## Cellular networks

Mobile phones transmit voice via radio waves to antennas on towers. The signal relays from tower to tower until it reaches its destination, whether another mobile or a wired telephone. The same path carries SMS.

- ==GSM== is the most common type of cellular network
- **3G, 4G, 4G-LTE, 5G** describe enhanced networks optimised for fast data transmission
- **4G still dominates** as the network most phones currently use

**Transitions are seamless.** Moving from 4G coverage into 3G coverage, the 4G radio shuts off and the 3G radio turns on without dropping the connection. The user normally notices nothing.

**Priority order:** mobile devices are preprogrammed to prefer **Wi-Fi** when available and able to obtain an IP address. Cellular data is the fallback.

Two reasons that ordering exists:
1. Wi-Fi data doesn't count against the cellular plan
2. **Wi-Fi radios use less power than cellular radios** — connecting to Wi-Fi conserves battery

---

## Bluetooth

Low-power, short-range technology intended to **replace wired connections to accessories**. Wireless, automatic, minimal power draw. **Up to eight devices** connected simultaneously.

Typical uses:

| Use | Example |
|---|---|
| Hands-free headset | Earpiece with microphone for calls |
| Input devices | Keyboard, mouse |
| Audio | Home/car stereo, portable speakers |
| Car speakerphone | Speaker + microphone for calls |
| Wearables | Smartwatch ↔ smartphone |
| Tethering | Sharing a network connection |

> Bluetooth carries **both data and voice**, which is why it can form small local networks rather than just streaming audio.

### Pairing

==Pairing== is establishing a trusted connection between two Bluetooth devices so they can share resources.

The process:
1. Both radios turned on; one device begins searching
2. The other must be in ==discoverable mode== (also called *visible*) to be detected
3. A ==PIN== may be requested to authenticate the pairing
4. The PIN is **stored** by the pairing service, so it isn't needed again

That storage is why a headset reconnects automatically when switched on within range.

**What a discoverable device broadcasts when queried:**
- Name
- Bluetooth class
- Services it can use
- Technical information (features, Bluetooth specification supported)

> ⚠️ **Security consequence:** discoverable mode advertises the device's name, class and capabilities to anyone in range. Leaving it permanently on is unnecessary exposure — it's the wireless equivalent of announcing what you're running. Turn it on to pair, then off.

---

## NFC

==Near Field Communication== exchanges data between devices in **very close proximity — usually less than a few centimetres**. It uses electromagnetic fields to transmit.

Primary use: connecting a smartphone to a **payment system**. Also tap-to-pair, transit cards, access badges.

**The proximity requirement *is* the security control.** An attacker has to be centimetres away, which makes remote interception impractical in a way that doesn't apply to Bluetooth or Wi-Fi.

---

## Wi-Fi

Transmitters and receivers inside the phone connect it to local networks and the internet. The device must be within range of a wireless access point.

- Networks are usually **privately owned** but often offer guest or public access
- A ==hotspot== is an area where Wi-Fi signals are available
- Connections work essentially the same as on a laptop

### Connecting

When Wi-Fi is on, the device searches for available networks and lists them. Touch one, enter a password if required.

**Automatic behaviour:**
- Out of range of one network → attempts another in range
- No Wi-Fi in range → falls back to cellular data
- ==It automatically reconnects to any network it has connected to before==

> ⚠️ **That last behaviour is the basis of the Evil Twin attack** (see Kasiu Domain 2, M5). The phone auto-connects to a remembered SSID **without verifying it's the same access point** — an attacker broadcasting the same network name gets the connection handed to them. Deleting saved networks you no longer use is a real mitigation, not paranoia.

### Manual configuration

Needed when the network's ==SSID== broadcast is turned off, or the device isn't set to connect automatically.

- ==SSID== — the name assigned to a wireless network
- ==Passphrase== — what's normally called the "wireless password"

**Both must be typed exactly as configured on the router**, or the connection fails.

**Android:** `Settings → Add network` → SSID → Security type → Password → Save

![[Pasted image 20260821174746.png]]

**iOS:** `Settings → Wi-Fi → Other` → SSID → Security → Other Network → Password → Join

![[Pasted image 20260821174752.png]]

> The two pieces of information required to connect manually to a secured network are **SSID and password**. Not IP address (assigned by DHCP), not username (that's 802.1X Enterprise, not PSK).

### Cellular data configuration

**Android:** `Settings → More (Wireless and Networks) → Mobile Networks → Data enabled`
**iOS:** `Settings → Cellular Data → toggle`

---

## Tethering vs Pairing — the distinction that gets tested

These are frequently confused and describe entirely different things:

| | ==Pairing== | ==Tethering== |
|---|---|---|
| What it does | Establishes **trust** between two devices | Shares an **internet connection** |
| Category | Authentication | Network sharing |
| Technology | Bluetooth-specific | Wi-Fi, Bluetooth **or** USB cable |
| Result | Devices can exchange data | The other device reaches the internet |

**Tethering is not a technology — it's a function.** It can run over three different transports:

| Transport | Speed | Battery cost | Cisco's terminology |
|---|---|---|---|
| Bluetooth | Slow | Lowest | **Tethering** |
| USB cable | Fast | Charges the phone | **Tethering** |
| Wi-Fi | Fastest | Highest | **Mobile hotspot** |

> ⚠️ **Cisco draws a terminology line here that is not universal.** In its own words: *"Tethering is commonly done over Bluetooth or a USB cable. A mobile hotspot is another form of internet sharing and is provided over Wi-Fi."*
>
> So in a NetAcad exam, *"share an internet connection via **tethering**"* → **Bluetooth**, and *"mobile **hotspot**"* → Wi-Fi.
>
> In everyday usage — and in most vendor documentation outside Cisco — "tethering" covers all three transports, and Android literally labels the Wi-Fi option *"Wi-Fi hotspot"* under a *"Tethering"* menu. **Answer according to the source being examined**, and be aware the distinction exists.

---

## Wi-Fi security on mobile devices

The four precautions from the module:

1. **Never send login or password information as unencrypted plaintext**
2. **Use a VPN** when sending sensitive data over untrusted networks
3. **Enable security on home networks**
4. **Use WPA2 or higher** encryption

> Point 1 is [[Bandit - Level 14]] and [[Bandit - Level 15]] in a sentence: the same password over `nc` versus over `openssl s_client`. On a café hotspot, everything unencrypted is readable by anyone on that network.
>
> Point 4 says WPA2 *or higher* — and Kasiu Domain 2 M5 explains why "or higher" matters: WPA2's 4-way handshake can be captured and cracked offline. **WPA3** replaces it with SAE and blocks that attack.

---

## Quick reference — matching scenario to technology

| Scenario | Answer | Why |
|---|---|---|
| Hands-free headset | **Bluetooth** | Accessory, short range, replaces a cable |
| Wireless headphones to a computer | **Bluetooth** | Same |
| Wireless keyboard or mouse | **Bluetooth** | Same |
| Tap phone to a payment terminal | **NFC** | Centimetres |
| Touch two phones together to transfer | **NFC** | Centimetres |
| Share internet via **tethering** | **Bluetooth** | Cisco's definition — tethering is Bluetooth or USB |
| Share internet via **mobile hotspot** | **Wi-Fi** | Cisco treats this as distinct from tethering |
| Connect a tablet to the internet | **Wireless LAN** | Wi-Fi-only device — no cellular radio |
| Satellite location for a map app | **GPS** | Only technology that receives from satellites |
| Two methods for internet on a phone | **Wi-Fi + cellular** | The only two that reach the internet |
| Pairing process, up to 100 m | **Bluetooth** | Pairing is Bluetooth-specific; class 1 reaches 100 m |
| Manual connection to a secured network | **SSID + password** | Not IP, not username |

---

## Key Takeaway

The five radios are distinguished by **range and purpose**, and questions almost always encode the answer in the distance described. Centimetres is NFC, metres is Bluetooth, a building is Wi-Fi, a city is cellular, and satellites are GPS.

Two traps worth internalising:

**Pairing ≠ tethering.** One is authentication between devices, the other is sharing a connection. And tethering names a *function*, not a technology — but **Cisco reserves the word for Bluetooth and USB**, calling the Wi-Fi version a *mobile hotspot*. That split is specific to this source; elsewhere the term covers all three transports.

**NFC and Wi-Fi answer opposite questions.** NFC is for proximity where the short range *is* the security model; Wi-Fi is for reaching the internet across a building. Payments are NFC; hotspots are Wi-Fi.

Beyond the exam, two behaviours from this module carry real security weight: **automatic reconnection to remembered SSIDs** enables Evil Twin attacks, and **discoverable mode** advertises device details to anyone in range. Both are convenience features with a cost.

---

## Related
- [[Domain 2 - Network Security]] — M5 covers WEP→WPA3, 802.1X, Evil Twin, rogue APs
- [[Cisco - Network Components]]
- [[Cisco - ISP Connectivity]]
- [[Bandit - Level 14]] · [[Bandit - Level 15]] — plaintext vs encrypted transmission
