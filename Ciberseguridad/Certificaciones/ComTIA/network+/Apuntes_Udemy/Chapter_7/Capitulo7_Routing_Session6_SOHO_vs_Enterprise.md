
# Capítulo 7 – Routing  
## Session 6: **SOHO vs Enterprise**

> Esta sesión compara los **SOHO router** (Small Office/Home Office) con los **Enterprise router** de clase empresarial, resaltando diferencias de hardware, software y operaciones que CompTIA Network+ espera que domines.  
> Palabras clave conservadas en *inglés*.

---

### 1. ¿Qué entendemos por “router” en cada contexto?

| Tipo de equipo | Papel principal | Usuarios objetivo | Ejemplo típico |
|----------------|-----------------|-------------------|----------------|
| **SOHO router** | *Gateway* todo‑en‑uno que **NAT‑ea**, hace de **DHCP server**, **firewall** y **WAP** | Hogar, micro‑negocios | Linksys E2500, Netgear Nighthawk |
| **Enterprise router** | Dispositivo dedicado a **filtrar y reenviar tráfico IP** entre múltiples redes; alta disponibilidad | Datacenter, sucursales corporativas | Cisco ISR 4000, Juniper MX |

---

### 2. Hardware & factor de forma

#### SOHO router  
* ➡️ Caja plástica pequeña.  
* 1 interfaz **WAN** + switch integrado (4–8 puertos **LAN**).  
* Antenas Wi‑Fi internas/externas (802.11ac/ax).  
* Fuente de poder única (sin redundancia).  

#### Enterprise router  
* ➡️ Chasis metálico para rack **19″**; 1–2 U de altura.  
* Múltiples **interfaces modulares**: GbE, 10 GbE, SFP/SFP+, Serial, LTE.  
* Fuentes de poder **redundantes hot‑swap** y ventiladores.  
* Diseñado para funcionar 24×7 con MTBF elevado.  

---

### 3. Funciones de software

| Función | SOHO | Enterprise |
|---------|------|------------|
| **NAT/PAT** | Activado por defecto; solo *static NAT* sencillo y *port‑forwarding*. | Opcional; soporta **dynamic NAT**, **policy NAT**, VRF. |
| **Firewall** | Stateful básico + filtros de URL | ACLs avanzadas, **Zone‑Based Firewall**, inspección profunda (DPI). |
| **Routing dinámico** | N/A o RIP limitado | Soporta **OSPF, EIGRP, BGP, IS‑IS**. |
| **VPN** | IPSec “wizard” o **DMZ host** | IPSec, DMVPN, SSL‑VPN, **GRE**; hardware crypto. |
| **QoS** | Prioridad simple (WMM) | **LLQ, CBWFQ, MQC**, shaping & policing. |

---

### 4. Gestión y actualización

* **SOHO**  
  * GUI web (HTTP/HTTPS) + *wizard* de instalación.  
  * Usuario/clave *default* (¡cámbiala!) &rarr; `admin / admin`.  
  * Firmware propietario; algunas versiones soportan **DD‑WRT / OpenWrt**.

* **Enterprise**  
  * Gestión por **CLI (Cisco IOS, Junos, etc.)** mediante **SSH** / consola serie.  
  * Soporte SNMP, NETCONF/RESTCONF, Syslog, AAA (**RADIUS/TACACS+**).  
  * Imágenes IOS firmadas; instalación vía **TFTP/USB**; *hot‑patching*.

```text
# Ejemplo Cisco IOS: mostrar configuración en ejecución
Router> enable
Router# show running-config | section interface
interface GigabitEthernet0/0/0
 description LINK_TO_ISP
 ip address 203.0.113.2 255.255.255.252
!
interface GigabitEthernet0/0/1
 description LAN_CORE
 ip address 10.10.0.1 255.255.252.0
 ip nat inside
```

---

### 5. Seguridad inicial (best practices)

1. **Cambiar** credenciales por defecto inmediatamente.  
2. Desactivar **remote‑admin** en SOHO o restringirla a HTTPS + lista IP.  
3. Actualizar **firmware/IOS** y firmwares de módulos.  
4. Aplicar **ACL** de entrada: “deny all + permit what is needed”.  
5. Implementar **Syslog** y **NTP** para auditoría.

---

### 6. Preguntas tipo examen Network+

1. > *Un técnico necesita alojar un servidor web detrás de un SOHO router. ¿Qué característica debe configurar?*  
   **Respuesta** : *Port‑forwarding* (static NAT) del puerto 80/443 hacia la IP privada del servidor.

2. > *Tras añadir un segundo proveedor WAN a un Enterprise router, ¿qué métrica o mecanismo asegura salida primeramente por el ISP principal?*  
   **Respuesta** : **Default‑route** con métrica/AD más baja o **policy‑based routing**.

3. > *¿Cuál de las siguientes afirmaciones es cierta sobre un SOHO router?*  
   *A) Requiere CLI para configurarse*  
   *B) Opera normalmente como switch capa 2 y **NAT gateway*** ✅  
   *C) Soporta módulos SFP+*  
   *D) Implementa OSPF por defecto*

---

### 7. Resumen

* **SOHO router** = simplicidad + coste bajo, ideal hasta ≈ 20 hosts.  
* **Enterprise router** = escalabilidad, redundancia y funciones avanzadas.  
* Ambos siguen el mismo principio: **filtrar y reenviar paquetes IP** —pero el entorno, el rendimiento esperado y las opciones de gestión dictan cuál es el adecuado.

---

© 2025 Notas de estudio CompTIA Network+  
