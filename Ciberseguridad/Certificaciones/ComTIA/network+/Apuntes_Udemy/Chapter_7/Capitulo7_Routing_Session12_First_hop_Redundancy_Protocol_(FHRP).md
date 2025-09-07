
# Capitulo 7 – Routing  
## Session 12 – **First Hop Redundancy Protocol (FHRP)**  

> Nota: el texto está redactado en **español**, pero se conservan los **términos clave en inglés** tal como solicita el curso.

---

### ¿Por qué necesitamos FHRP?
1. En una LAN típica todos los hosts envían su tráfico saliente a **un único Default Gateway** (primer salto).  
2. Si ese router falla, toda la red pierde conectividad externa.  
3. **First Hop Redundancy Protocol** crea un *Gateway virtual* altamente disponible compartido por **dos o más routers físicos**, garantizando continuidad aun cuando el router activo deje de responder.

---

### Conceptos básicos
| Concepto | Descripción |
|----------|-------------|
| **Virtual IP (VIP)** | Dirección IP que los hosts configuran como *Default Gateway*. |
| **Virtual MAC** | Dirección MAC asociada a la VIP; los switches la aprenden como si fuera un único dispositivo. |
| **Active Router** | Router físico que actualmente reenvía el tráfico para la VIP. |
| **Standby / Backup Router** | Router(es) que monitorizan al activo y toman su rol si éste falla. |

---

### Modos / variantes de FHRP
| Protocolo | Vendor / Estándar | Tipo | Características clave |
|-----------|------------------|------|-----------------------|
| **HSRP** (Hot Standby Router Protocol) | Propietario **Cisco** | *Active/Standby* | Prioridad configurable, _pre‑emption_, mensajes **hello** UDP 1985 cada 3 s. |
| **VRRP** (Virtual Router Redundancy Protocol) | **RFC 5798** (estándar) | *Master/Backup* | Operación similar a HSRP; el *Master* es el router con prioridad más alta o con la VIP física. |
| **GLBP** (Gateway Load Balancing Protocol) | Propietario **Cisco** | *Load‑balancing* | Distribuye hosts entre varios routers mediante diferentes **virtual MAC**; balanceo **round‑robin** o **weighted**. |

---

### Funcionamiento general
```mermaid
sequenceDiagram
    participant Host
    participant Gateway_Virtual as "Gateway Virtual (VIP/MAC)"
    participant R1 as "Router 1 (Active)"
    participant R2 as "Router 2 (Standby)"

    Host->>Gateway_Virtual: ARP Request
Who has VIP?
    Gateway_Virtual-->>Host: ARP Reply
Virtual MAC

    Note over Host: El Host guarda la MAC virtual en su ARP cache
 y la usa como next‑hop permanente.

    Host-)R1: Tráfico (L3) hacia Internet
MAC destino = MAC virtual
    R1-->>Internet: Reenvío normal

    alt Falla R1
        R2-->>R1: No tiene hellos -> Timeout
        R2->>Switch: Anuncio gratuitous ARP
(MAC virtual ahora en R2)
        Host-)R2: Tráfico continúa sin cambio
    end
```

---

### Timers y *convergence*
| Parámetro | Valor típico HSRP | Significado |
|-----------|------------------|-------------|
| **Hello Timer** | 3 s | Intervalo entre mensajes hello. |
| **Hold Timer** | 10 s | Tiempo de espera antes de considerar caído al Active. |
| **Convergence** | ≈ 3–10 s | Tiempo total para que el Standby asuma el rol. |

> En VRRP los valores por defecto son **1 s / 3 s**, lo que brinda convergencia más rápida.

---

### Métricas de prioridad
* Cada protocolo permite asignar un **priority** (0‑255).  
* Con **pre‑emption** activado, si un router con prioridad mayor vuelve a la red, retomará el rol de Active/Master automáticamente.

---

### Buenas prácticas de diseño
1. **Emparejar routers** en chasis o racks distintos y con fuentes de energía independientes.  
2. Ajustar **timers** sólo si se necesita convergencia sub‑segundo (implica mayor carga de CPU y tráfico hello).  
3. Colocar la **VIP** dentro de la misma subred que los hosts; no necesita estar asignada físicamente a ninguna interfaz.  
4. Supervisar con **SNMP / Syslog** los cambios de estado _Active → Standby_ para detectar flaps.

---

### Resumen visual
```
LAN 192.168.50.0/24
+----------------------+           +----------------------+
|  Router 1            |           |  Router 2            |
|  Gi0/0 = .1 (HSRP)   |           |  Gi0/0 = .2 (HSRP)   |
|  Priority 110        |           |  Priority 100        |
+----------+-----------+           +----------+-----------+
           |  VIP = 192.168.50.254  MAC = 0000.0C9F.FFFE |
           +------------------------(Switch)-------------+
                               |
                        +-------------+
                        |  Hosts      |
                        |GW = .254    |
                        +-------------+
```

Los hosts solo conocen la **VIP (.254)**.  
Si Router 1 cae, Router 2 asume la MAC virtual y continúa el servicio sin intervención de los usuarios.

---

### Conclusión
Los protocolos **FHRP** (HSRP, VRRP, GLBP) proporcionan **alta disponibilidad** en el *primer salto* de cualquier red IP, evitando cortes cuando falla el Default Gateway y, en el caso de GLBP, añadiendo además **balanceo de carga** automático.
