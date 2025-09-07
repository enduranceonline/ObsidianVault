# Capítulo 7 – Routing  
## Session 10: **Border Gateway Protocol (BGP)**  

> **BGP** es el protocolo de enrutamiento *de facto* que mantiene unida a Internet: se encarga de mover el tráfico **entre** distintos *Autonomous Systems* (**AS**).

---

### 1. ¿Qué es un *Autonomous System* (AS)?
- Conjunto de una o más **redes de routers** operadas por la **misma organización** (ISP, gran universidad, proveedor cloud, etc.).  
- Cada AS posee un identificador numérico único: **ASN** (32‑bit).  
- Dentro del AS se suele emplear un **IGP** como **OSPF** o **EIGRP** para el enrutamiento *interno*.

---

### 2. ¿Por qué necesitamos **BGP**?
| Reto | Solución BGP |
|------|--------------|
| Existen **millones** de LANs → imposibles de almacenar en cada tabla de rutas | BGP publica **prefijos** agregados de cada AS |
| Los enlaces caen / cambian costos | BGP ajusta rutas usando **Path Attributes** |
| Políticas de negocio (coste, acuerdos de peering) | BGP aplica **políticas** mediante atributos como *Local Pref*, *MED*, *COMMUNITY* |

---

### 3. Tipos de BGP  
| Tipo | Uso | Puerto / Transporte |
|------|-----|---------------------|
| **eBGP** (*External BGP*) | Conectar *AS* distintos | TCP 179 |
| **iBGP** (*Internal BGP*) | Redistribuir prefijos **dentro** de un mismo AS muy grande | TCP 179 |

> Regla iBGP: todos los routers deben ser **full‑mesh** o usar *route‑reflector*.

---

### 4. Métrica y decisión de ruta  
BGP no utiliza *hop count*.  Evalúa, en orden:  
1. `Weight` (propietario de Cisco)  
2. `LOCAL_PREF`  
3. `AS_PATH` → prefiere **menos AS‑hops**  
4. `ORIGIN` (IGP \< EGP \< INCOMPLETE)  
5. `MED`, … hasta 10+ criterios.

---

### 5. Mensajes BGP básicos  
1. **OPEN** – negociación de versión y parámetros  
2. **UPDATE** – anuncia o retira prefijos  
3. **KEEPALIVE** – mantiene la sesión viva  
4. **NOTIFICATION** – informa errores y cierra la sesión  

---

### 6. Flujo de un prefijo

```text
LAN 10.10.0.0/16
   │  (OSPF)
RTR_A  —— eBGP ——  RTR_B (ISP) —— eBGP ——  RTR_C (otro ISP)
```
1. `RTR_A` redistribuye 10.10.0.0/16 a su **iBGP**.  
2. Su **eBGP** lo anuncia a `RTR_B` con `AS_PATH: AS65001`.  
3. `RTR_B` añade su ASN (`65002`) y propaga a socios.  
4. El mundo ya conoce la ruta hacia el AS 65001 mediante 65002.

---

### 7. Ventajas & desventajas  
**Pros**  
- Escala global ➜ ~1 M rutas IPv4  
- Soporta políticas de tráfico complejas  
- Convergencia aceptable (gracias a *Path Vector*)  

**Contras**  
- Configuración y *troubleshooting* complejos  
- Sensible a ataques de *route‑hijacking* si no se usa **RPKI** / **BGP‑sec**  
- Requiere hardware con mucha **RAM/CPU**

---

### 8. Resumen para el examen  
- **BGP = único EGP** relevante; todo lo demás es **IGP**.  
- Funciona como **Path‑Vector** (híbrido *distance‑vector / link‑state*).  
- Usa atributos como **AS_PATH**, **LOCAL_PREF**, **MED** para elegir rutas.  
- Ejecuta en **TCP 179** y mantiene sesiones con **KEEPALIVE**.  
- Necesitas un **ASN** para hablar BGP externamente.

---

> “Sin **BGP**, los paquetes no sabrían salir de su barrio.” 🌐
