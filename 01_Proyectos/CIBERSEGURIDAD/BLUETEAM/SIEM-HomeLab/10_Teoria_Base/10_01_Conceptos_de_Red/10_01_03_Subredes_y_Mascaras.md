

---

Las subredes y las máscaras permiten **dividir**, **organizar** y **asegurar** una red en segmentos independientes.  
Son esenciales para controlar el tráfico, diseñar VLANs, aplicar reglas de firewall y dar estructura a tu SIEM-HomeLab.

	Nota importante:  

> En esta fase NO necesitas aprender “subnetting avanzado” (cálculos de /25, /26, /27, etc.).  
> Para tu arquitectura real, todas las subredes serán /24, lo cual simplifica el diseño sin perder profesionalidad.  
> Más adelante, si lo necesitas, veremos subnetting avanzado en  
> [[20_Diseño_Arquitectura/20_01_Arquitectura_Logica/20_01_03_Modelo_de_Segmentacion|20_01_03 – Modelo de Segmentación]]  
> y también durante las simulaciones con Packet Tracer.


---

# **1. Qué es una subred**

Una subred es una **división lógica** dentro de una red mayor.  
Permite separar dispositivos en grupos independientes, con reglas y rutas específicas.

Ejemplos:

```
10.10.0.0/24   → LAN
10.20.0.0/24   → IoT
10.30.0.0/24   → LAB
10.40.0.0/24   → Honeypots
```

Cada subred tiene:

- su rango propio
    
- su máscara
    
- su gateway
    
- su conjunto de hosts
    
- sus reglas específicas en el firewall
    

Esto evita que un IoT acceda a un PC, que un malware pivote, o que un atacante navegue por tu red sin restricciones.

---

# **2. Qué es la máscara de subred**

La máscara determina cuántos bits de la dirección IP pertenecen:

- a la **red**
    
- a los **hosts**
    

Ejemplos típicos:

```
/24 → 255.255.255.0
/23 → 255.255.254.0
/16 → 255.255.0.0
```

Una máscara **más grande** (más bits bloqueados) implica:

- más redes
    
- menos hosts por red
    

---

# **3. Separación entre red y host**

Ejemplo:

```
IP:      10.10.0.57
Mascara: /24
```

Interpretación:

- **10.10.0** → red
    
- **57** → host
    

Con un /16:

- **10.10** → red
    
- **0.57** → host
    

Esto determina el tamaño y la estructura de cada segmento.

---

# **4. Por qué usamos /24 en todas las VLAN**

En tu SIEM-HomeLab, /24 es el tamaño ideal porque:

- es claro y fácil de administrar
    
- es estándar profesional
    
- permite hasta 254 dispositivos por VLAN
    
- simplifica el firewall
    
- simplifica DHCP
    
- simplifica el diseño visual
    
- no requiere subnetting avanzado
    

Y sobre todo:

✔ **evita complejidad innecesaria en esta etapa del proyecto.**

---

# **5. Network, Broadcast y Hosts**

Ejemplo:

```
10.30.0.0/24
```

- **Network:** 10.30.0.0
    
- **Gateway:** 10.30.0.1
    
- **Hosts:** 10.30.0.2 – 10.30.0.254
    
- **Broadcast:** 10.30.0.255
    

Esto es fundamental para:

- DHCP
    
- Firewall
    
- Routing
    
- IDS
    
- SIEM
    

---

# **6. Ejemplos aplicados a tu SIEM-HomeLab**

### **LAN**

```
10.10.0.0/24
```

### **IoT**

```
10.20.0.0/24
```

### **LAB**

```
10.30.0.0/24
```

### **Honeypots**

```
10.40.0.0/24
```

Cada subred tendrá:

- reglas propias
    
- su propio gateway
    
- su propio pool DHCP
    
- su propio uso (LAN, IoT, LAB, etc.)
    

---

# **7. Subredes en Packet Tracer, Firewall y SIEM**

### ✔ Packet Tracer

Te permite ver:

- VLANs
    
- routing interno
    
- subinterfaces
    
- ACL básicas
    

### ✔ Firewall (OPNsense/pfSense)

Cada subred será una interfaz virtual con:

- DHCP propio
    
- reglas específicas
    
- NAT controlado
    

### ✔ IDS (Suricata)

Las subredes definen:

- qué tráfico inspeccionar
    
- qué VLAN produce qué alerta
    

### ✔ SIEM (Wazuh)

Las IP identifican:

- el tipo de dispositivo
    
- su ubicación lógica
    
- la superficie de ataque
    

---

# **8. Máscaras sin cálculos avanzados**

Tabla útil:

|Máscara|Uso típico|Hosts|
|---|---|---|
|/30|Enlaces punto a punto|2|
|/29|DMZ pequeñas|6|
|/24|VLAN estándar|254|
|/23|Redes medianas|510|
|/16|Redes grandes|65k|

En tu SIEM-HomeLab:  
→ **todas /24** por simplicidad, claridad y seguridad.

---

# **9. Errores comunes**

- Mezclar todo en 192.168.1.0/24
    
- Crear subredes que se solapan
    
- No poner un gateway único por subred
    
- Meter IoT dentro de LAN
    
- Dar DHCP desde varios sitios sin querer
    

Esto se corrige más adelante en:

➡ [[20_Diseño_Arquitectura/20_01_Arquitectura_Logica/20_01_03_Modelo_de_Segmentacion|Modelo de segmentación]]

---
