# Capítulo 6 — TCP/IP Basics  
## Session 8: Special **IP Addressing**

> **Idioma:** Español con palabras clave en **inglés** (private, loopback, APIPA) para el examen **CompTIA Network+**.

---

## 1. Private IP addresses (RFC 1918)

| Bloque (CIDR)       | Rango decimal               | Tamaño | Uso típico |
|---------------------|-----------------------------|--------|-----------|
| **10.0.0.0/8**      | 10.0.0.0 – 10.255.255.255   | 16 M   | Data centers, grandes LAN |
| **172.16.0.0/12**   | 172.16.0.0 – 172.31.255.255 | 1 M    | Redes corporativas |
| **192.168.0.0/16**  | 192.168.0.0 – 192.168.255.255| 65 K   | Home/SOHO routers |

Características:

- **No** son ruteables en Internet pública.  
- Usan **NAT** o **PAT** para salir a la red exterior.  
- Frecuentes en laboratorios y VPN.

---

## 2. Loopback addresses

| Protocolo | Dirección            | Descripción               |
|-----------|----------------------|---------------------------|
| IPv4      | **127.0.0.1** (cualquier 127.x.x.x)| Prueba de pila TCP/IP local. |
| IPv6      | **::1**              | Equivalente IPv6.         |

```bash
ping 127.0.0.1   # comprueba stack IPv4
ping ::1         # comprueba stack IPv6
```

> Todo el bloque **127.0.0.0/8** responde a sí mismo, pero en el examen recuerda **127.0.0.1**.

---

## 3. APIPA (Automatic Private IP Addressing)

- Bloque **169.254.0.0/16**  
- Asignado automáticamente por el cliente **DHCP** si no recibe oferta.  
- Permite comunicación **local** dentro del mismo broadcast domain, pero **sin acceso a Internet**.

### Identificar APIPA en Windows

```powershell
ipconfig
# Resultado:
# Autoconfiguration IPv4 Address . . : 169.254.x.y
```

> Diagnóstico típico: servidor DHCP caído o problemas de alcance. Solución: revisar DHCP/relay.

---

## 4. Otras direcciones reservadas (mención rápida)

| Bloque             | Finalidad                          |
|--------------------|------------------------------------|
| 224.0.0.0/4        | **Multicast** IPv4                |
| 240.0.0.0/4        | Experimentos / futuro             |
| 100.64.0.0/10      | NAT interno de ISPs (**CGNAT**)   |
| fe80::/10          | **Link‑local** IPv6 (auto)        |

---

## 5. Buenas prácticas y examen tips

1. **10.x / 172.16‑31 / 192.168** → privadas, requieren NAT para Internet.  
2. **Loopback** sirve para test local; no depende de NIC física.  
3. **169.254.x.x** indica fallo DHCP, pero permite compartir archivos localmente.  
4. Solo un **servidor DHCP** por broadcast domain; usa **ip helper‑address** si está en otra subred.  
5. Windows muestra “Autoconfiguración IPv4” para APIPA; Linux usa `link-local`.

---

*Fin de la Session 8. Próximo módulo: ARP cache poisoning y seguridad de capa 2.*