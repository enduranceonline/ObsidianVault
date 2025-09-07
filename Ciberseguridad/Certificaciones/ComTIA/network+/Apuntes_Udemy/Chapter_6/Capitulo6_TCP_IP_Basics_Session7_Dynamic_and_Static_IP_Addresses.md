# Capítulo 6 — TCP/IP Basics  
## Session 7: Dynamic and Static **IP Addresses**

> **Idioma:** Español con palabras clave en **inglés** (DHCP, static, lease, scope) para prepararte al examen **CompTIA Network+**.

---

## 1. Dos formas de asignar una IP address

| Método     | Configuración | Ventajas                            | Casos de uso               |
|------------|---------------|-------------------------------------|----------------------------|
| **Static** | Manual (IP, subnet mask, default gateway) | Predecible, imprescindible para servidores, impresoras, dispositivos accesibles desde Internet. | Web server, Mail server, Router WAN |
| **Dynamic**| Automática vía **DHCP** / *BOOTP* | Sin intervención manual, reutiliza direcciones, ideal para clientes cambiantes. | PCs, móviles, IoT |

---

## 2. Flujo de trabajo **DHCP**

1. **DHCP Discover** (broadcast)  
2. **DHCP Offer** (unicast desde el servidor)  
3. **DHCP Request** (broadcast/unicast)  
4. **DHCP ACK** (servidor confirma)  

![DHCP hand‑shake](text-diagram)

---

## 3. Componentes clave en un servidor DHCP

| Término           | Descripción                                                                 |
|-------------------|----------------------------------------------------------------------------|
| **Scope**         | Rango de direcciones (pool) que el servidor puede asignar.                 |
| **Lease**         | Tiempo durante el cual la IP queda reservada para el cliente (ej. 8 h).    |
| **Reservation**   | Vincula **MAC address ↔ IP** específica dentro del scope (IP “estática” vía DHCP). |
| **Options**       | Datos extra: **default gateway**, **DNS servers**, domain‑name, etc.       |
| **Exclusions**    | IPs dentro del scope **no** asignables (protegidas para manual/static).    |

---

## 4. DHCP Relay / IP Helper‑Address

Los mensajes **DHCP Discover/Request** son broadcast → no cruzan routers.  
Un **DHCP Relay Agent** (IP Helper) reenvía las peticiones a un servidor DHCP en otra subred.

```
Router(config)#interface g0/1
Router(config-if)#ip helper-address 10.1.1.5
```

---

## 5. IPv6 y asignación automática

| Modo          | Protocolo   | Descripción                                          |
|---------------|-------------|------------------------------------------------------|
| **Stateless** | **SLAAC**   | Cliente genera IP usando `prefix`+EUI‑64; router anuncia `RA`. |
| **Stateful**  | **DHCPv6**  | Similar a IPv4 DHCP; servidor entrega IP, lease, opciones. |

---

## 6. Buenas prácticas de direccionamiento

1. **Un solo** servidor DHCP por dominio de broadcast (evita conflictos).  
2. Mantén plan de **documentación** (reservas, exclusiones, scopes).  
3. Usa **reservations** para dispositivos que requieren IP fija pero quieres seguir usando DHCP.  
4. Configura **backup**/failover DHCP en redes críticas.  
5. Para servicios públicos, solicita a tu ISP un bloque estático adecuado (/29, /28, etc.).

---

## 7. Comparación rápida

| Característica   | Static                | DHCP (Dynamic)         |
|------------------|-----------------------|------------------------|
| Config inicial   | Manual               | Automática             |
| Mantenimiento    | Difícil en masa       | Centralizado           |
| Cambio de red    | Requiere editar host  | Sin acción del usuario |
| Riesgo de error  | Typos, duplicados     | Bajo (servidor controla) |

---

## 8. Tips para el examen Network+

1. Orden correcto **Discover → Offer → Request → ACK**.  
2. **Reservation** = MAC↔IP binding dentro del scope.  
3. **Lease** expira → cliente renueva; si falla, IP vuelve al pool.  
4. **ip helper‑address** reenvía DHCP broadcasts a otro segmento.  
5. **SLAAC** ≠ DHCPv6; usa Router Advertisements, no lease.

---

*Fin de la Session 7. Próximo tema: DNS y resolución de nombres.*