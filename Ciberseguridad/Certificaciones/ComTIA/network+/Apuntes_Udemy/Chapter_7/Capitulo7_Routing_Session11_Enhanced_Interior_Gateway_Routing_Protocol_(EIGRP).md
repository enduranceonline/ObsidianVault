
# Capitulo7_Installing_Physical_Network_Session11_Enhanced_Interior_Gateway_Routing_Protocol_(EIGRP)

> **Nota**: Redactado en español; las *palabras clave* del protocolo se mantienen en **inglés** según lo solicitado.

---

## 🧭 Introducción

**Enhanced Interior Gateway Routing Protocol (EIGRP)** es la versión mejorada del antiguo **IGRP** (ya *deprecated*).  
EIGRP pertenece a la familia de protocolos *distance‑vector* **híbridos** (combina técnicas *distance‑vector* y *link‑state*).  
Se utiliza dentro de un **Autonomous System (AS)** como **IGP** (Interior Gateway Protocol) para lograr **convergencia rápida**, cálculo
eficiente de rutas y evitar *routing loops*.

---

## 🔑 Componentes principales

| Componente | Descripción breve | Palabras clave |
|------------|------------------|----------------|
| **Neighbor Discovery & Recovery** |  Detecta y mantiene vecinos mediante paquetes **Hello** multicast. Si un vecino no responde antes del *hold timer*, se elimina de la tabla. | `Hello`, `Hold Timer` |
| **RTP (Reliable Transport Protocol)** |  Capa de transporte propietaria (similar a TCP) que garantiza entrega *secuencial* de mensajes **Update**, **Query** y **Reply**. | `RTP`, `ACK`, `Sequence` |
| **DUAL (Diffusing Update Algorithm)** |  Algoritmo que calcula la *best path* libre de bucles. Define **Successor** y **Feasible Successor** y utiliza la **Feasibility Condition**. | `DUAL`, `Successor`, `Feasible Successor` |
| **PDM (Protocol Dependent Modules)** |  Módulos que adaptan EIGRP a varios protocolos de *layer‑3* (IPv4, IPv6, IPX, AppleTalk). | `IPv4 PDM`, `IPv6 PDM` |

---

## 📊 Tablas de EIGRP

1. **Neighbor Table** – Lista de routers vecinos detectados: dirección, interfaz y *hold time* restante.  
2. **Topology Table** – Contiene todas las rutas aprendidas; cada entrada puede estar en **Passive** (estable) o **Active** (re‑cálculo).  
3. **Routing Table** – Sólo almacena las rutas **Successor** elegidas por DUAL (las mejores) y, opcionalmente, las **Feasible Successor**.

---

## 🧮 Métrica compuesta

EIGRP calcula su **metric** combinando:

- **Bandwidth** (ancho de banda mínimo del *path*)
- **Delay** (suma de retardos interfaz‑a‑interfaz)
- (Opcionales) **Load** y **Reliability**

> Por defecto sólo se usan *bandwidth* y *delay*.  

Fórmula simplificada:  
`metric = (10^7 / bandwidth_min + delay_sum) × 256`

---

## 🔄 Tipos de paquetes

| Tipo | Función | Multicast / Unicast |
|------|---------|---------------------|
| **Hello** | Descubrir / mantener vecinos | Multicast (`224.0.0.10`) |
| **Update** | Anunciar nuevas rutas o cambios | Unicast/Multicast |
| **Query** | Solicitar rutas alternativas cuando una ruta se vuelve **Active** | Multicast |
| **Reply** | Respuesta a **Query** | Unicast |
| **ACK** | Confirmar recepción fiable (RTP) | Unicast |

---

## 🚦 Estados de ruta

- **Passive** – Ruta estable; no requiere cálculo.
- **Active** – DUAL busca nuevo *Successor* (envía **Query**, espera **Reply**).

---

## 🛠️ Configuración mínima (Cisco IOS)

```text
router eigrp 100              ! 100 = Autonomous‑System‑Number
 network 192.168.4.0 0.0.0.255
 network 10.0.0.0    0.0.0.3
! Opcional: activar para IPv6
ipv6 router eigrp 100
```

> Cambia los comandos según tu *topology* y versiones IOS/IOS‑XE.

---

## ✔️ Ventajas y consideraciones

| Ventaja | Comentario |
|---------|------------|
| **Convergencia rápida** | DUAL + feasibles successors = *failover* inmediato. |
| **Escala bien** | Soporta VLSM, CIDR, *summarization* e IPv6. |
| **Métrica compuesta** | Mejor que simples *hop‑count*. |
| **Menor *CPU* que OSPF** | Actualizaciones diferenciales sólo cuando hay cambios. |

| Consideración | Mitigación |
|---------------|------------|
| **Propietario Cisco** (aunque documentado como *open*) | Hoy la mayoría de plataformas soportan OSPF; evalúa compatibilidad. |
| **Consumo de memoria** en grandes *topologies* | Ajustar límites de sucesores o usar *stub* routers. |

---

## 📚 Resumen para examen **CompTIA Network+**

- EIGRP = **Internal, distance‑vector híbrido**, métrica basada en *bandwidth* y *delay*.  
- Utiliza **Hello**, **Update**, **Query**, **Reply**, **ACK**.  
- DUAL define **Successor** (ruta principal) y **Feasible Successor** (backup).  
- Convergencia rápida y sin bucles gracias a **Feasibility Condition**.  
- Se anuncia mediante **multicast 224.0.0.10** (IPv4) / **FF02::A** (IPv6).

¡Eso cubre los puntos esenciales del protocolo *Enhanced Interior Gateway Routing Protocol* que necesitas dominar!  
