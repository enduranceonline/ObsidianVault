# Capítulo 7 — Routing  
## Session 5: **Tour of a SOHO Router**

> **Idioma:** Español con términos clave en **inglés** (WAN, LAN, NAT, firmware, firewall, port forwarding, reset).  
> **Objetivo:** Reconocer la interfaz, menús y buenas prácticas de un **SOHO router** típico para el examen **CompTIA Network+**.

---

## 1. Información que NO puedes perder

| Dato                             | Ubicación típica                     |
|----------------------------------|--------------------------------------|
| **Default IP** del router        | `192.168.0.1` ó `192.168.1.1`        |
| **Default username / password**  | Manual impreso, pegatina inferior    |
| Manual PDF / quick‑start         | Sitio web del fabricante             |

Sin estos valores no podrás entrar en la GUI.

---

## 2. Conexión inicial

1. Conecta tu **laptop** a un puerto **LAN** con un patch‑cord.  
2. Obtén IP vía **DHCP** (`ipconfig` / `ifconfig`).  
3. Abre navegador → `http://<default‑IP>`.  
4. Empieza sesión con credenciales por defecto → ¡cambia la contraseña!

---

## 3. Menú típico (GUI)

| Sección               | Función clave (palabra en inglés)                         |
|-----------------------|-----------------------------------------------------------|
| **Status / Overview** | Muestra WAN IP pública, LAN IP, uptime, wireless status. |
| **Basic Setup**       | Configura **WAN** (DHCP, Static, PPPoE) y **LAN IP**.    |
| **Wireless**          | SSID, security (WPA2/WPA3), channel.                     |
| **Services**          | Activa opciones como **SSH**, **Telnet**, **SNMP**.      |
| **Security / Firewall** | Stateful firewall, SPI, bloqueo de **ping**.            |
| **NAT / Port Forward**| Reglas de **port forwarding**, DMZ, UPnP.                |
| **Administration**    | Cambiar password, **remote management**, **firmware upgrade**. |

---

## 4. Configuraciones clave

### 4.1 WAN Setup  
- **DHCP** (por defecto) toma IP del ISP.  
- **Static** requiere IP, máscara, gateway y DNS manuales.  
- Clona la **MAC address** del PC si el cable‑modem la espera.

### 4.2 LAN Setup  
- Cambia el rango por defecto (`192.168.15.1`) para reducir ataques “drive‑by”.  
- Activa / desactiva el **DHCP server** interno (scope, lease time).

### 4.3 Wireless AP  
- Deshabilita WPS.  
- Usa **WPA2‑PSK** o mejor **WPA3**.  
- Ocultar SSID no da seguridad real.

### 4.4 Services  
- Habilita **SSH/Telnet** sólo cuando lo necesites, y restringe por red.  
- Deshabilita **UPnP** salvo que una app lo requiera.

### 4.5 Remote Management  
- Desactiva acceso **HTTP/HTTPS** remoto, o usa puerto no estándar y **HTTPS** con contraseña fuerte.

### 4.6 Firmware Upgrade  
1. Descarga BIN del sitio oficial (o **DD‑WRT/OpenWrt** si lo soporta).  
2. Backup config.  
3. Sube archivo → **flash**.  
4. No interrumpas: power loss = *brick*.

---

## 5. Seguridad básica

- Cambia **admin password** inmediatamente.  
- Actualiza **firmware** cuando haya CVE.  
- Deshabilita servicios innecesarios.  
- Revisa el **log** del router para escaneos.  
- Crea ACL para limitar horarios o dominios si hace falta.

---

## 6. Hard Reset (regla **30‑30‑30**)

| Paso | Acción                                     | Tiempo |
|------|--------------------------------------------|--------|
| 1    | Mantén pulsado **reset button**            | 30 s   |
| 2    | Sin soltar, **desconecta** el adaptador AC | 30 s   |
| 3    | Sin soltar, **vuelve a enchufar**          | 30 s   |

Restaura valores de fábrica → IP y credenciales vuelven a “default”.

---

## 7. Tips Network+

1. GUI varía, pero siempre hay **Status, Setup, Security, Administration**.  
2. WAN casi siempre es **DHCP** en routers SOHO.  
3. Cambiar el **LAN IP** y desactivar **remote GUI** mejora seguridad.  
4. **Firmware upgrade** puede “brickear” si falla → procede con UPS.  
5. El **30‑30‑30 reset** limpia todo; necesitarás reconfigurar.

---

*Fin de la Session 5. Próximo tema: Routing estático vs dinámico (RIP, OSPF).*