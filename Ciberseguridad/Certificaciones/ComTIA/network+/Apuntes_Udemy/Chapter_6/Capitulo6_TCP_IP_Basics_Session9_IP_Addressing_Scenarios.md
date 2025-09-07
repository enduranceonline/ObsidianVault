# Capítulo 6 — TCP/IP Basics  
## Session 9: **IP Addressing Scenarios**

> **Idioma:** Español con palabras clave en **inglés** (duplicate IP, DHCP lease, APIPA) para el examen **CompTIA Network+**.

---

## 1. Escenario: **Duplicate IP address**

### Síntomas  
- Windows muestra alerta “Windows has detected an IP address conflict”.  
- Hosts Linux/Mac presentan pérdida intermitente de conectividad.

### Causas  
1. **Rogue DHCP** emitiendo la misma IP.  
2. Configuración **static** duplicada.

### Solución  
1. Ejecutar `ipconfig` / `ifconfig` y comparar IPs.  
2. Verificar **DHCP scope** o base de datos de direcciones estáticas.  
3. Eliminar DHCP no autorizado o reconfigurar una de las máquinas.

---

## 2. Escenario: **Duplicate MAC address** (VM labs)

### Síntomas  
- Switch virtual entra en modo hub; tráfico inestable.  
- Puertos alternan entre learning/forwarding.

### Causas  
- Clonado de máquinas virtuales sin cambiar MAC (hypervisor).

### Solución  
- Regenerar MAC en VM clone.  
- Revisar inventario de **MAC reservations**.

---

## 3. Escenario: **Incorrect Default Gateway**

| Síntoma                      | Diagnóstico                     |
|------------------------------|---------------------------------|
| Pings locales OK, Internet NO| `ipconfig` muestra gateway erróneo (ej. 192.168.1.4 vs 192.168.4.1). |

- Puede ser **rogue router** o error de tipeo en configuración **static**.

### Acciones  
1. Confirmar gateway oficial en documentación.  
2. Revisar servidor DHCP (option 3).  
3. Escanear red para routers no autorizados.

---

## 4. Escenario: **Wrong Subnet Mask**

### Ejemplo  
- Red correcta `/24` 255.255.255.0  
- PC1 usa 255.255.255.0 → OK  
- PC2 mal escribe 255.255.0.0

### Resultado  
- PC2 puede hacer ping a PC1, pero PC1 no vuelve (mismatch de red).  
- Comunicación Internet posible (si NAT), pero tráfico local fallará.

### Solución  
- Uniformar máscara en todos los hosts del broadcast domain.  
- Implementar **DHCP** para evitar typos.

---

## 5. Escenario: **Expired DHCP lease**

### Flujo normal  
- Lease 8 h → T1 = 4 h → PC renueva sin problema.

### Problema  
- Servidor DHCP caído; lease expira.  
- Windows mantiene IP hasta fin de lease; tras reinicio asigna **APIPA 169.254.x.x**.

### Diagnóstico  
```powershell
ipconfig /all   # Autoconfiguration IPv4 Address . . : 169.254.54.23
```

### Solución  
- Restaurar servicio DHCP o configurar gateway alterno con **DHCP failover**.  
- Como contingencia, asignar IP static temporal.

---

## 6. Resumen de comandos útiles

| OS      | Ver IP/MAC        | Renovar DHCP          | Flush DNS / ARP          |
|---------|-------------------|-----------------------|--------------------------|
| Windows | `ipconfig /all`   | `ipconfig /renew`     | `arp -d *` / `ipconfig /flushdns` |
| Linux   | `ip addr` / `ip a`| `dhclient -r; dhclient` | `ip neigh flush all`     |
| macOS   | `ifconfig`        | `sudo ipconfig set en0 DHCP` | `dscacheutil -flushcache` |

---

## 7. Tips para el examen Network+

1. **Duplicate IP** → broadcast storm/conflict; Windows avisa.  
2. **169.254.x.x = APIPA** ⇒ fallo DHCP.  
3. Mismatch de máscara produce comunicación unidireccional.  
4. Gateway errónea = sin salida WAN.  
5. Verifica primero configuración **local** antes de culpar al router.

---

*Fin de la Session 9 y del módulo de direccionamiento IP. ¡Practica analizando diagramas y usando tus comandos de red!*