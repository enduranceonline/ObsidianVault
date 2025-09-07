# Capítulo 7 — Routing  
## Session 2: Network Address Translation (**NAT**)

> **Idioma:** Español manteniendo términos clave en **inglés** (NAT, PAT, static NAT, dynamic NAT) para el examen **CompTIA Network+**.

---

## 1. Problema original: escasez de direcciones IPv4

- IPv4 ≈ 4.300 M IPs → agotamiento en los 90.  
- Cada host público requería IP **única**.  
- Solución: **NAT** permite que múltiples dispositivos internos (private IP) compartan **una o pocas** IP públicas.

---

## 2. Cómo funciona NAT (ejemplo básico)

```
PC (192.168.1.50) ──>  [Router NAT]
                     LAN: 192.168.1.1
                     WAN: 203.0.113.10
```

1. PC envía paquete hacia **8.8.8.8:80**  
2. Router reemplaza **source IP** 192.168.1.50 → 203.0.113.10 y guarda entrada en la **NAT table**.  
3. Google responde a 203.0.113.10.  
4. Router consulta tabla, restaura IP original, reenvía al PC.

---

## 3. Tipos de NAT

| Tipo            | Alias           | Característica principal                                 | Ejemplo uso |
|-----------------|-----------------|----------------------------------------------------------|-------------|
| **Static NAT**  | 1‑to‑1 mapping  | IP pública fija ↔ IP privada fija.                       | Publicar Web/FTP server interno. |
| **Dynamic NAT** | Pooled NAT      | Pool de IP públicas; asignación temporal.                | Pequeña empresa con pocas IP públicas. |
| **PAT**         | NAT Overload, **Port Address Translation** | Muchos hosts comparten **una** IP pública; distingue por **TCP/UDP port** origen. | Hogares, SOHO routers. |

### 3.1 Static NAT (port forwarding)

```
203.0.113.20  →  192.168.1.80:80
```

Todos los paquetes destinados a 203.0.113.20 puerto 80 se dirigen al servidor web interno .80.

### 3.2 Dynamic NAT

```
Pool público: 203.0.113.20‑21
Host A (192.168.1.10) ↔ 203.0.113.20
Host B (192.168.1.11) ↔ 203.0.113.21
Host C (192.168.1.12) espera hasta liberar pool
```

### 3.3 PAT (NAT Overload)

| Conexión         | Traducción WAN            |
|------------------|---------------------------|
| 192.168.1.10:1025 → 203.0.113.10:**40001** |
| 192.168.1.11:1042 → 203.0.113.10:**40002** |

---

## 4. NAT table (ejemplo PAT)

| Inside Local | Inside Global | Outside Global | Estado |
|--------------|--------------|----------------|--------|
| 192.168.1.10:1025 | 203.0.113.10:40001 | 8.8.8.8:80 | ESTABLISHED |
| 192.168.1.11:1042 | 203.0.113.10:40002 | 1.1.1.1:443| ESTABLISHED |

---

## 5. Ventajas y desventajas

| Ventaja                         | Desventaja                         |
|--------------------------------|------------------------------------|
| Conservar IPv4 públicas         | Rompe extremo‑a‑extremo (IP real). |
| Oculta topología interna (**security by obscurity**) | Complica VoIP, VPN, P2P (requiere port‑forward o ALG). |
| Permite superposición de **private IP** | Aumenta latencia ligera (traducción). |

---

## 6. Configuración básica (Cisco IOS PAT)

```cisco
interface Gig0/1        ! interfaz LAN
 ip nat inside
interface Gig0/0        ! interfaz WAN
 ip nat outside
ip access-list NAT_LAN permit 192.168.1.0 0.0.0.255
ip nat inside source list NAT_LAN interface Gig0/0 overload
```

---

## 7. NAT y el examen Network+

1. Identifica **10.0.0.0/8, 172.16/12, 192.168/16** como private → necesitan NAT para Internet.  
2. **Static NAT / Port Forwarding** expone un servicio interno.  
3. **Dynamic NAT** falla si pool se agota.  
4. **PAT** ≈ “NAT Overload”; 1 IP pública, muchos hosts.  
5. NAT opera en la frontera LAN↔WAN (router/firewall).

---

*Fin de la Session 2. Próxima sesión: Static vs Dynamic Routing Protocols (RIP, OSPF, EIGRP).*