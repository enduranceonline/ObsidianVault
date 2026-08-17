---
tags: [linux, shell, encoding, cryptography, malware-analysis, practice, security]
source: Bandit Levels 10-11 + general reference
---

# Linux - Encoding vs Encryption

> Related: [[Linux - Extracting Strings from Binaries]] covers reading binary content. This note covers what to do once that content turns out to be transformed rather than plain.

---

## The Distinction That Gets Asked in Interviews

Three operations that look superficially similar and are routinely confused. The difference is not academic — it determines whether data is protected or merely rearranged.

| | Purpose | Key? | Reversible? |
|---|---|---|---|
| **Encoding** | Make data survive a transport channel | No | Yes, by anyone |
| **Encryption** | Make data unreadable without authorisation | Yes | Only with the key |
| **Hashing** | Verify integrity / store password verifiers | No | No, by design |

**Encoding** answers *"can this data travel through this channel intact?"* — base64, URL-encoding, hex, ASCII. Public algorithm, no secret. Anyone can reverse it.

**Encryption** answers *"can an unauthorised party read this?"* — AES, RSA, ChaCha20. The security lives entirely in the key, never in the algorithm's secrecy (Kerckhoffs's principle).

**Hashing** answers *"has this changed?"* — SHA-256, bcrypt. One-way: no key exists that recovers the input.

==Encoded is not encrypted.== A base64 string in a config file marked "encrypted password" is a finding, not a control. This maps directly onto Kasiu Domain 7 (Criptografía).

---

## base64

Maps arbitrary bytes onto 64 printable characters: `A-Z`, `a-z`, `0-9`, `+`, `/`, with `=` as padding. Every 3 bytes of input become 4 output characters — a **33% size increase**, which is the cost of making binary safe for text-only channels.

```bash
base64 file              # ENCODE (default direction)
base64 -d file           # decode
echo "text" | base64     # encode from stdin
echo "dGV4dAo=" | base64 -d
base64 -w 0 file         # no line wrapping (default wraps at 76 chars)
```

**The default is encode.** Running `base64` on already-encoded data produces valid, longer base64 — no error, wrong answer. Encountered in [[Bandit - Level 10]].

**Recognising it:** alphanumerics plus `+/=` only, length a multiple of 4, trailing `=` or `==`.

**base64url variant** substitutes `-` and `_` for `+` and `/` so the string is safe inside URLs and JWTs. Standard `base64 -d` may choke on it; translate first:
```bash
echo "$s" | tr '_-' '/+' | base64 -d
```

**The `echo` newline trap.** `echo` appends `\n`, which becomes part of the encoded data:
```bash
echo "secret" | base64        # c2VjcmV0Cg==   ← includes the newline
echo -n "secret" | base64     # c2VjcmV0       ← correct
printf '%s' "secret" | base64 # most portable form
```
Encoding a password or token with a stray newline produces a value that fails authentication for reasons that are very hard to see.

---

## ROT13 and `tr`

ROT13 shifts each letter 13 positions through the alphabet. Since 13 is half of 26, **it is its own inverse** — the same operation encodes and decodes.

```bash
cat file | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

`tr` substitutes positionally between two equal-length sets. Non-letters appear in neither set and pass through unchanged.

`tr` is worth knowing well beyond ROT13:

```bash
tr 'a-z' 'A-Z'  < file        # upper-case everything
tr -d '\r'      < file        # strip carriage returns (Windows → Unix line endings)
tr -d ' '       < file        # remove all spaces
tr -s ' '       < file        # squeeze repeated spaces into one
tr -c 'a-zA-Z0-9\n' '\n' < file   # complement: replace everything NOT alphanumeric
tr ',' '\n'     < file        # split a CSV line into one field per line
```

`tr -d '\r'` alone justifies remembering the command — Windows-authored scripts fail on Linux with baffling errors caused by invisible `\r` bytes.

**`tr` reads only from stdin.** It takes no filename argument, which makes it the mirror image of the trap in [[Bandit - Level 09]]: there, `sort data.txt` inside a pipe silently ignored stdin because it *had* a file argument. Two opposite behaviours, one lesson — **know which input a command actually reads.**

---

## Real-World Applications

### HTTP Basic Authentication
```bash
echo "dXNlcjpQNHNzdzByZCE=" | base64 -d
# → user:P4ssw0rd!
```
The `Authorization: Basic` header is base64 of `username:password`. Not encrypted, not hashed — encoded. Over plain HTTP, anyone on the path reads the credentials. This is why Basic Auth without TLS is a finding, and why it turns up in pentest reports and packet captures constantly.

### JWT tokens
```bash
echo "$JWT" | cut -d. -f2 | tr '_-' '/+' | base64 -d 2>/dev/null | jq .
```
A JWT is `header.payload.signature`, with the first two parts base64url-encoded. **The payload is readable by anyone holding the token.** The signature prevents *tampering*, not *reading*. Putting secrets, internal IDs or PII in a JWT payload is a recurring application-security finding — relevant to Kasiu Domain 5.

### PowerShell encoded commands — malware triage
```bash
echo "$B64" | base64 -d | tr -d '\0'
```
`powershell -enc <base64>` is one of the most common obfuscation techniques in real attacks. The payload is **UTF-16LE**, so every character is followed by a null byte — hence the `tr -d '\0'`. Decoding it is step one of triage and usually reveals a download-and-execute one-liner outright.

This connects directly to the wide-character problem in [[Linux - Extracting Strings from Binaries]]: same UTF-16LE encoding, same reason plain tooling misses it.

### Config files with "encrypted" credentials
```bash
grep -Eo '[A-Za-z0-9+/]{20,}={0,2}' config.xml | while read s; do echo "$s" | base64 -d 2>/dev/null; done
```
Applications frequently store credentials base64-encoded and label the field `encryptedPassword`. Scanning configs for base64-shaped strings and decoding them is standard practice in both pentesting and post-compromise review. Anything recovered this way was never protected.

### PEM certificates and keys
```bash
openssl x509 -in cert.pem -text -noout
```
A `.pem` file is base64 of DER binary, wrapped in `-----BEGIN CERTIFICATE-----` markers. Understanding that the body is *encoded, not encrypted* explains why a certificate is public and a private key file must be protected by filesystem permissions or a passphrase — the base64 itself protects nothing. Kasiu Domain 7, PKI module.

### Data exfiltration over DNS
Attackers base32/base64-encode stolen data into DNS subdomain labels, because DNS is almost always permitted outbound. The signature is abnormally long, high-entropy hostnames:
```bash
awk '{print $NF}' dns.log | awk -F. '{print length($1)}' | sort -n | uniq -c | tail
```
The ==DNS tunneling== detection described in Kasiu Domain 2, done with the pipeline from [[Linux - Sorting and Deduplication]].

### Phishing pages hidden in data: URIs
`<iframe src="data:text/html;base64,...">` embeds an entire page inside an attribute, defeating URL-based blocklists. Decoding the blob reveals the credential-harvesting form.

### Weak obfuscation in scripts
ROT13, XOR with a single byte and reversed strings appear in droppers and skid-tier malware as an anti-analysis layer. **Recognising that something is obfuscated rather than encrypted is the useful skill** — it means the content is one command away, and no key hunt is needed.

---

## Identifying an Unknown Transformation

| Clue | Likely |
|---|---|
| `A-Za-z0-9+/` with `=` padding, length ÷ 4 | base64 |
| `A-Z2-7` with `=` padding | base32 (common in DNS exfil) |
| Only `0-9a-f`, even length | hex |
| `%20`, `%2F` | URL encoding |
| Readable-looking but wrong letters (`Gur` = `The`) | ROT13 / Caesar |
| Exactly 32 / 40 / 64 hex chars | MD5 / SHA-1 / SHA-256 hash — **not reversible** |
| `$2b$`, `$6$` prefix | bcrypt / SHA-512-crypt password hash |
| High entropy, no structure, no padding | probably genuinely encrypted — stop and look for the key |

The last two rows are where the distinction pays off: recognising a hash means **not wasting time trying to decode it**, and recognising real encryption means the problem is key management, not tooling.

> ==CyberChef== (GCHQ, browser-based) chains these transformations visually and has a "Magic" operation that guesses the encoding. Excellent for exploration; the CLI tools remain the right choice for anything scripted or repeated.

---

## Key Takeaway

Encoding is a **transport format**, not a control. base64 and ROT13 both reverse with a single public command and no key — which makes them useful for moving data and useless for protecting it.

The practical instinct: on meeting a transformed string, first classify it as **encoded, hashed, or encrypted**. Encoded means decode it now. Hashed means stop, it doesn't reverse. Encrypted means the real question is where the key lives. Misclassifying costs hours; classifying correctly usually costs one look at the character set.
