# 🚦 Capítulo 7 – Session 8: Dynamic Routing

> **Palabras clave:** Dynamic Routing, Distance Vector, Link State, Metric, Convergence, IGP, EGP, BGP, RIP, OSPF, MTU, Latency

---

## 1. ¿Por qué necesitamos *Dynamic Routing*?

En una red pequeña podemos sobrevivir con **static routes**: un técnico escribe manualmente cada ruta en la routing table.  
En redes grandes (y en **Internet**) esto resulta imposible:

- Routers pueden **caerse** o perder enlaces.  
- Proveedores añaden o retiran circuitos constantemente.  
- Necesitamos volver al estado de **convergence** (todos los routers de acuerdo sobre “dónde está todo”) *rápidamente* y sin intervención humana.

La solución es el **Dynamic Routing**, que permite a los routers **descubrir, anunciar y actualizar** rutas de forma automática.  
Cada protocolo dinámico define **cómo** se intercambia la información y **qué métricas** usa para decidir la “mejor” ruta.

---

## 2. Métricas (*Metrics*)

Una *metric* es un valor numérico que expresa la *preferencia* de una ruta: **cuanto menor, mejor**.

| Métrica típica | Significado | Ejemplo de impacto |
|---------------|-------------|--------------------|
| **Hop Count** | Nº de routers intermedios. | Menos saltos suele ser más rápido. |
| **Bandwidth** | Ancho de banda disponible en el enlace. | Preferir 10 Gb ↔ evitar 56 kb. |
| **Cost** | Valor asignado manualmente por el admin. | Rutas baratas vs. caras. |
| **MTU** | *Maximum Transmission Unit* del enlace. | Fragmentación si MTU pequeño. |
| **Latency** | Retardo de propagación/cola. | Crucial para VoIP y tiempo real. |

Cada protocolo usa **una o varias** métricas.  
Ejemplo: **RIP** v2 sólo mira *Hop Count*; **OSPF** usa *Cost* (basado en bandwidth) y puede considerar *MTU*.

---

## 3. Familias de protocolos

### 3.1 Distance Vector

*Idea:* cada router envía **su tabla de rutas completa** a sus *vecinos* en intervalos fijos.  
El vecino suma 1 al *Hop Count*, guarda la mejor métrica y reenvía la tabla.

- **Ventajas:** sencillo de configurar.  
- **Desventajas:** convergencia lenta; mucho tráfico de actualización.

**Ejemplos en Network+**

| Protocolo | Alcance | Métrica principal |
|-----------|---------|-------------------|
| **RIP v1/v2** | IGP (pequeñas LAN/WAN) | Hop Count (máx 15) |
| **RIPv2** añade soporte VLSM y auth. |

---

### 3.2 Link State

*Idea:* cada router envía pequeños **Link‑State Advertisements (LSA)** que describen *su* estado (interfaces, costes).  
Todos los routers calculan la topología completa con **Dijkstra** y construyen *su propia* routing table.

- **Ventajas:** convergencia rápida; actualizaciones sólo cuando cambia algo.  
- **Desventajas:** más RAM/CPU; configuración inicial algo mayor.

**Ejemplos en Network+**

| Protocolo | Alcance | Comentarios |
|-----------|---------|-------------|
| **OSPF v2/v3** | IGP para IPv4/IPv6 | Organiza routers en *áreas*; métrica = Cost. |
| **IS‑IS** | ISP / entornos grandes | Similiar a OSPF; muy usado en carriers. |

---

### 3.3 IGP vs EGP

- **IGP** (*Interior Gateway Protocol*) opera **dentro** de un *Autonomous System (AS)* – una red controlada por una misma organización.  
- **EGP** (*Exterior Gateway Protocol*) conecta **entre** AS.

**Único EGP moderno:** **BGP‑4 (Border Gateway Protocol)**  
BGP intercambia *prefix* + *AS‑Path*; métrica = *Path Length*, attributes (Local‑Pref, MED...).  
Mantiene la “postal mundial” de rutas de Internet.

---

## 4. Conceptos clave para el examen

| Término | Definición corta |
|---------|------------------|
| **Convergence** | Estado en que todos los routers conocen la mejor ruta. |
| **LSA / Hello** | Mensajes de descubrimiento/actualización en Link State. |
| **Split Horizon / Poison Reverse** | Técnicas Distance Vector para evitar *routing loops*. |
| **Administrative Distance** | Prioridad global cuando un router ejecuta *varios* protocolos. |
| **Default Route (0.0.0.0/0)** | Ruta usada si no existe coincidencia más específica. |

---

## 5. Buenas prácticas de *Dynamic Routing* en entornos reales

1. **Planificar AS y áreas** antes de desplegar OSPF/IS‑IS.  
2. **Ajustar los Timers** (Hello/Dead) según estabilidad del enlace.  
3. **Filtrar Rutas** con distribuciones y *route‑maps* para evitar fugas de prefijos.  
4. **Supervisar** con SNMP/NetFlow: detectar _flapping_, congestión, MTU mismatch.  
5. **Hacer Backups** de la *running‑config* y usar control de versiones.

---

### Resumen

- **Static Routes** sirven para redes pequeñas o enlaces sencillos.  
- **Dynamic Routing** usa protocolos (Distance Vector o Link State) que intercambian información automáticamente.  
- El valor **Metric** guía la elección de la mejor ruta.  
- **BGP** es el *único* EGP y “cola” de Internet; OSPF, IS‑IS y RIP compiten en el interior de los AS.  
- El objetivo final es mantener la **convergence** y redirigir el tráfico cuando un enlace o router falla.

---

*Material ampliado y adaptado para la certificación **CompTIA Network+**. “¡Aprende las rutas y nunca te perderás en la red!”  
