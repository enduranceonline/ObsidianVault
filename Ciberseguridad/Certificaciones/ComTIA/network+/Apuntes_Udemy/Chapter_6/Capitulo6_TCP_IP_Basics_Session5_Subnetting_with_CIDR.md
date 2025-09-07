# Capítulo 6 — TCP/IP Basics  
## Session 5: **Subnetting with CIDR**

> **Idioma:** Español con palabras clave en **inglés** (CIDR, subnetting, /n) para el examen **CompTIA Network+**.

---

## 1. ¿Por qué nació **CIDR**?

El modelo **Classful** (A/B/C) desperdiciaba direcciones:

- /8 → 16 M hosts  
- /16 → 65 K hosts  
- /24 → 254 hosts  

Internet creció; se necesitó granularidad. En 1993 se introdujo **CIDR** (Classless Inter‑Domain Routing) que permite máscaras de **cualquier longitud** `/n` sin atarse a “puntos”.

---

## 2. Recordatorio de binario

Una máscara es simplemente **n** bits a 1 seguidos de **h** bits a 0.  
Ej.: `/26` = 11111111.11111111.11111111.11000000 → 255.255.255.192

- Bits **1** → Network  
- Bits **0** → Hosts  
- Hosts = 2^h − 2

---

## 3. Subnetting paso a paso

### 3.1 Caso de estudio

ISP asigna **208.25.160.0/24** (256 IPs).  
Queremos 4 subredes iguales.

#### Paso 1: Calcular bits necesarios  
4 subredes → 2^s ≥ 4 → **s = 2 bits**.

#### Paso 2: Nueva máscara  
Original /24 → /24 + 2 = **/26**  
Mask: 255.255.255.192

#### Paso 3: Tallas resultantes  
h = 32 − 26 = 6 bits host → 2^6 − 2 = **62 hosts** c/u.

### 3.2 Rangos finales (/26)

| Subred | Network ID        | Host range (usable)           | Broadcast        |
|--------|-------------------|-------------------------------|------------------|
| #0     | 208.25.160.0/26   | 208.25.160.1 – 160.62         | 208.25.160.63    |
| #1     | 208.25.160.64/26  | 208.25.160.65 – 160.126       | 208.25.160.127   |
| #2     | 208.25.160.128/26 | 208.25.160.129 – 160.190      | 208.25.160.191   |
| #3     | 208.25.160.192/26 | 208.25.160.193 – 160.254      | 208.25.160.255   |

---

## 4. Subnetting recursivo (VLSM)

Re‑subnet (#0) para dos oficinas de 30 hosts y 10 hosts:

1. Necesidad 30 hosts → /27 (32‑2 = 30)  
   - 208.25.160.0/27 (hosts .1‑30)  
   - 208.25.160.32/27 (hosts .33‑62)

2. Necesidad 10 hosts → /28 (16‑2 = 14)  
   - 208.25.160.64/28 (hosts .65‑78)  
   - 208.25.160.80/28 (hosts .81‑94)

Resultado: uso eficiente de espacio; nada se desperdicia.

---

## 5. Tabla rápida CIDR ↔ hosts

| /n | Hosts | Mask              |
|----|-------|-------------------|
| /24| 254   | 255.255.255.0     |
| /25| 126   | 255.255.255.128   |
| /26| 62    | 255.255.255.192   |
| /27| 30    | 255.255.255.224   |
| /28| 14    | 255.255.255.240   |
| /29| 6     | 255.255.255.248   |
| /30| 2     | 255.255.255.252   |

---

## 6. Comprobación rápida en CLI

```bash
# Linux / macOS
ipcalc 208.25.160.0/26

# Windows PowerShell
Get-NetIPAddress | Select IPAddress,PrefixLength
```

---

## 7. Tips para el examen Network+

1. Hosts = 2^(32 − n) − 2.  
2. Al subnetear, **suma bits** a la máscara.  
3. `/30` se usa para enlaces punto‑a‑punto (2 hosts).  
4. **VLSM** = subnetting dentro de subredes (jerárquico).  
5. Reconoce que 255.255.255.192 = **/26**; 255.255.255.248 = **/29**.

---

*Fin de la Session 5. Próximamente: Route Summarization y ejercicios de práctica CIDR/VLSM.*