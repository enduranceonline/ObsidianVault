# 📍 Capitulo 7 – Routing  
## Session 7: **Static Routes**

### ⚙️ Introducción  
Una **static route** (ruta estática) es una entrada fija dentro de la **routing table** que un administrador escribe manualmente.  
- No cambia hasta que alguien la modifica o elimina.  
- Es el primer mecanismo histórico que permitió a los **routers** saber «por dónde enviar» el tráfico IP.  
- Se emplea aún hoy en redes **SoHo** pequeñas, enlaces dedicados o como ruta de respaldo.

> En entornos Enterprise modernos predominan los **dynamic routing protocols** (e.g., OSPF, EIGRP, BGP), pero entender las rutas estáticas sigue siendo requisito para el **CompTIA Network+**.

---

### 🗺️ ¿Qué es una *routing table*?  
Es un listado interno que cada host o router TCP/IP mantiene con al menos:  

| Campo              | Significado                        |
|--------------------|------------------------------------|
| **Destination**    | Red o host de destino              |
| **Netmask**        | Máscara que define el prefijo      |
| **Gateway**        | Próximo salto (next‑hop)           |
| **Interface**      | NIC por la que se envía            |
| **Metric**         | “Costo” o preferencia relativa     |

---

### 🔍 Ejemplo en Windows  
```powershell
C:\> route PRINT
# ↓ Salida abreviada
Network Destination        Netmask          Gateway       Interface  Metric
0.0.0.0                    0.0.0.0          192.168.4.1   192.168.4.76     25
127.0.0.0                  255.0.0.0        On‑link       127.0.0.1       331
192.168.4.0               255.255.255.0     On‑link       192.168.4.76    281
```
- La primera línea es la **default route** (0.0.0.0/0) que envía todo tráfico desconocido al **default gateway**.  
- Las líneas 127.0.0.0/8 implementan el **loopback**.  
- 192.168.4.0/24 indica que los paquetes locales no salen por la puerta de enlace.

> Comando alternativo: `netstat ‑r`

---

### 🛠️ Sintaxis típica de **static route**  

| SO / OS                | Comando (ejemplo)                                   |
|------------------------|-----------------------------------------------------|
| Windows                | `route ADD 10.10.20.0 MASK 255.255.255.0 192.168.4.1` |
| Linux / *nix           | `ip route add 10.10.20.0/24 via 192.168.4.1`        |
| Cisco IOS              | `ip route 10.10.20.0 255.255.255.0 192.168.4.1`     |

- El **next‑hop** puede ser una IP del router adyacente *o* la interfaz de salida (p.ej., `Serial0/0` en Cisco).  
- Para que persista tras reinicio, en Windows se añade `-p` (persistent); en Cisco se guarda con `write memory`.

---

### 🧭 Default route  
Una variante especial es la *quad‑zero* `0.0.0.0 0.0.0.0` (IPv4) o `::/0` (IPv6).  
Sirve como “catch‑all”: si ningún otro prefijo coincide, el paquete se envía allí.

```bash
# Cisco – enviar todo lo desconocido a la WAN
ip route 0.0.0.0 0.0.0.0 17.1.1.1
```

---

### 🧩 Métrica  
Cuando coexisten varias static routes hacia el mismo destino, la **métrica** decide la preferencia.  
- Windows: número mayor = peor ruta.  
- IOS: el comando opcional `distance` (administrative distance).

---

### ⚖️ Limitaciones de las rutas estáticas  
1. **Escalabilidad**: crecen linealmente con el número de redes.  
2. **Tolerancia a fallos**: si un enlace cae, la ruta no se actualiza sola.  
3. **Administración**: propensas a errores de digitación y difíciles de mantener.

---

### 📝 Resumen para el examen  
- Saber cómo listar (`route print`, `ip route show`) y añadir (`route add`, `ip route add`) rutas.  
- Reconocer la estructura *destination / netmask / gateway / interface / metric*.  
- Distinguir **static route** vs. **default route**.  
- Entender por qué se usarían (p.ej., enlaces dedicados, redes pequeñas, rutas de backup).  
- Recordar que todo host TCP/IP tiene su propia routing table, no sólo los routers.

---

¡Con esto dominas el núcleo de las **static routes**!  
