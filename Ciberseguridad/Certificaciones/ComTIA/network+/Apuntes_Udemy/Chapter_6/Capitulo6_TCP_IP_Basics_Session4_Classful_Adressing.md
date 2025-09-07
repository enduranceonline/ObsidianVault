# Capítulo 6 — TCP/IP Basics  
## Session 4: **Classful Addressing**

> **Idioma:** Español con términos clave en **inglés** (Class A/B/C, RIR, IANA) para el examen **CompTIA Network+**.

---

## 1. IANA y la distribución de IP addresses

- **IANA** (Internet Assigned Numbers Authority) administra el espacio global de **IP addresses**.  
- IANA delega bloques grandes a los **RIRs** (Regional Internet Registries):

| RIR      | Región       |
|----------|--------------|
| **ARIN** | EE.UU., Canadá |
| **RIPE NCC** | Europa, Rusia |
| **APNIC** | Asia‑Pacífico |
| **LACNIC** | Latinoamérica & Caribe |
| **AFRINIC** | África |

Los RIR reparten direcciones a **ISPs** y organizaciones grandes.

---

## 2. Concepto de **Classful Addressing**

Introducido en los 80 para simplificar el enrutamiento:

| Clase | Rango primer octet | Default Mask | Hosts por red | Uso típico |
|-------|--------------------|--------------|---------------|-----------|
| **A** | 0‑127*             | 255.0.0.0 (/8)   | 16 777 214 | ISPs, gobiernos |
| **B** | 128‑191            | 255.255.0.0 (/16)| 65 534     | Universidades, corporativos |
| **C** | 192‑223            | 255.255.255.0 (/24)| 254       | Pequeñas redes |
| D / E | 224‑255            | Multicast / Investigación | — | — |

\* 127.x.x.x reservado para **loopback**.

### Ventajas iniciales
- Configuración sencilla (3 tamaños fijos).  
- Enrutadores limitados podían filtrar por el primer octet.

### Problemas
- Desperdicio enorme (red /24 para 5 hosts).  
- Crecimiento exponencial de Internet agotó el espacio rápidamente.

---

## 3. Ejemplo práctico con Class B

ISP asigna **160.25.0.0/16** a una empresa.

- **Network ID:** 160.25.0.0  
- **Host range:** 160.25.0.1 – 160.25.255.254  
- **Broadcast:** 160.25.255.255  
- Total hosts posibles: 65 534

### Necesidad de subnetting

La empresa tiene 4 sitios. Con Classful, todo comparte una sola LAN—impráctico.  
Se subdivide /16 → cuatro subredes /24 (FLSM), desperdiciando > 99 %.

---

## 4. Fixed‑Length vs Classful

- **FLSM** (Fixed‑Length Subnet Mask) corta un bloque en subredes iguales (/24, /26, /30…).  
- **Classful** define tamaño **por primera vez** (A/B/C), no flexible.

| Aspecto         | Classful | FLSM / VLSM |
|-----------------|----------|-------------|
| Tamaños posible | 3 (A/B/C)| Cualquier /n|
| Desperdicio     | Alto     | Menor       |
| CIDR soporte    | No       | Sí          |

---

## 5. Puerta de enlace y decisiones de envío

Al enviar un **IP packet**:

1. Host aplica su **subnet mask**.  
2. Si destino comparte **Network ID** → **ARP** directo (local).  
3. Si no → envía al **default gateway** (router).

Classful facilita detectar red por primer octet, pero hoy se usa **CIDR** / **classless** subnetting.

---

## 6. Transición a Classless

Limitaciones de Classful originaron:

- **CIDR** (Classless Inter‑Domain Routing) 1993.  
- **VLSM** para asignar máscaras variables internamente.  
- Reducción de tablas de enrutamiento & conservación de espacio.

> Próximas sesiones profundizarán en CIDR y VLSM.

---

## 7. Tips para el examen Network+

1. Rango primer octet: A 0‑127, B 128‑191, C 192‑223.  
2. Hosts por clase: A ≈16 M, B ≈65 K, C 254.  
3. 127.0.0.0/8 = loopback, no usable en redes.  
4. Classful usa **default masks** (/8, /16, /24).  
5. Conocer por qué Classful fue reemplazado por CIDR (desperdicio, crecimiento).

---

*Fin de la Session 4. Próxima sesión: CIDR (Classless) y route summarization.*