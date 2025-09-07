# 🛣️ Capítulo 7 – Sesión 9: Open Shortest Path First (OSPF)

## 🌐 ¿Qué es OSPF?

**OSPF** (Open Shortest Path First) es un protocolo **IGP** (*Interior Gateway Protocol*) de tipo **link‑state** diseñado para intercambiar información de enrutamiento *dentro* de un *sistema autónomo* (AS).  
Desde finales de los 90 desplazó a **RIP** como protocolo interno predominante gracias a su **convergencia rápida**, soporte total de **CIDR / VLSM** y uso eficiente del ancho de banda.

| Propiedad | Valor en OSPF |
|-----------|---------------|
| Tipo      | Link‑state |
| RFC       | 2328 (IPv4) • 5340 (OSPFv3 IPv6) |
| Puerto IP | **89/UDP** |
| Métrica   | **Cost** (inverso del ancho de banda) |
| Algoritmo | **Dijkstra SPF** |
| Autenticación | Claro, MD5 o SHA (OSPFv3) |

---

## 🧩 Conceptos fundamentales

### Áreas
- OSPF divide el AS en **áreas lógicas** para escalar mejor.  
- **Area 0** (backbone) debe conectar a todas las demás áreas.  
- Reduce el tamaño de la LSDB (Link‑State DataBase) y el flooding de LSAs.

### LSAs y LSDB
- Los routers anuncian su estado de enlace mediante **LSA** (*Link‑State Advertisement*).  
- Todas las LSAs de un área forman la **LSDB**, idéntica en cada router del área → *convergencia*.

### Cálculo SPF
1. Construir LSDB  
2. Ejecutar algoritmo **Dijkstra** → árbol de ruta más corta por área  
3. Llenar la **tabla de enrutamiento (RIB)** con las mejores rutas (*Cost* más bajo).

### Métrica *Cost*
\[
\text{Cost}=\frac{10^8}{\text{BW (en bps)}}
\]
> Por defecto Cisco usa 100 Mbps como referencia (Cost = 1).  
> Menor cost ⇒ mejor ruta.

| Enlace | Ancho de banda | Cost |
|--------|----------------|------|
| Fast Ethernet | 100 Mb/s | 1 |
| Gigabit | 1 Gb/s | 1 (hay que ajustar el **auto‑cost reference‑bandwidth**) |
| T1 | 1.544 Mb/s | 64 |

### Vecinos, Adyacencias y *Hello*
- Paquetes **Hello** (10 s LAN, 30 s WAN) descubren **neighbors**.  
- Si se intercambian DB‑DESC, LSU/LSR se forma la **adyacencia** completa.

### DR / BDR
- En redes multi‑acceso (Ethernet) se elige un **Designated Router** y un **Backup DR** para reducir LSAs.  
- Elección basada en *router ID* o *priority* más alta.

---

## 📨 Tipos de paquetes OSPF

| Tipo | Nombre | Propósito |
|------|--------|-----------|
| 1 | Hello | Descubrir/ mantener vecinos |
| 2 | DB‑Description | Resumen de LSDB |
| 3 | LSR | Solicitar LSA faltante |
| 4 | LSU | Enviar LSA |
| 5 | LSAck | Confirmación |

---

## 🔧 Ejemplo de configuración básica (Cisco IOS)

```plaintext
router ospf 10            ! 10 = process‑id local
 router-id 1.1.1.1        ! único en el AS
 network 192.168.4.0 0.0.0.255 area 0
 network 10.10.10.0 0.0.0.255 area 1
 passive-interface Gig0/0  ! no enviar Hellos a la LAN de usuarios
```

> **Nota**: ajusta `auto-cost reference-bandwidth 10000` para enlaces ≥10 Gb/s.

---

## 🛡️ Seguridad

- Autenticación **MD5** (IPv4) / **HMAC‑SHA** (OSPFv3).  
- Filtrado de rutas con **area range**, **summary‑address** o **route‑maps**.  
- Usa **passive‑interface** para evitar Hellos innecesarios y exploits.

---

## ⚖️ Ventajas frente a RIP (distance‑vector)

| Característica | OSPF | RIP v2 |
|----------------|------|--------|
| Convergencia   | Segundos | Minutos |
| Métrica        | Cost (BW) | Saltos (≤15) |
| VLSM/CIDR      | ✔ | ✔ |
| Escalabilidad  | Alta (áreas) | Baja |
| Seguridad      | MD5/SHA | Plain/MD5 |

---

## 📝 Consejos Network+

1. **Puerto 89/UDP** y algoritmo **Dijkstra** son preguntas frecuentes.  
2. Recuerda que OSPF es **link‑state + IGP**; BGP es **EGP**.  
3. **Area 0** es obligatorio; los *ABR* conectan áreas a backbone, *ASBR* exportan rutas externas.  
4. Métrica = **Cost** (menor es mejor).  
5. DR/BDR sólo en redes multi‑acceso (no puntos‑a‑punto).

¡Con estos conceptos dominarás OSPF en el examen CompTIA Network+!  
