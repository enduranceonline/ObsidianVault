

---

El direccionamiento IP define **cómo se identifican y localizan los dispositivos dentro de una red**.  
Sin comprender esto, no es posible diseñar una arquitectura SOC sólida, segmentar correctamente la red, aplicar reglas en el firewall o entender qué está detectando Suricata.

Este apartado explica **de forma progresiva y aplicada** cómo funcionan las IPs y cómo vas a usarlas en el SIEM-HomeLab.

---

# **1. Qué es una dirección IP**

Una dirección IP (IPv4) es un identificador numérico de **32 bits**, representado así:

```
192.168.1.25
```

Cada IP tiene **dos partes**:

- **Red** → Qué segmento o VLAN pertenece.
    
- **Host** → Qué dispositivo dentro de esa red.
    

La máscara de subred determinará dónde acaba cada parte (lo verás en [[10_Teoria_Base/10_01_Conceptos_de_Red/10_01_03_Subredes_y_Mascaras|10_01_03 Subredes y Máscaras]]).

En tu SIEM-HomeLab, esta estructura será crucial porque:

- cada VLAN tendrá un rango propio
    
- el firewall separará tráfico según subredes
    
- el IDS analizará tráfico por segmentos
    
- Wazuh identificará cada host por su IP
    

---

# **2. Tipos de direcciones IP**

En redes domésticas y corporativas solo trabajarás con tres tipos:

## **A) IP Privada**

Usada dentro de una LAN. No es accesible desde Internet.

Rangos oficiales:

- **10.0.0.0 – 10.255.255.255**
    
- **172.16.0.0 – 172.31.255.255**
    
- **192.168.0.0 – 192.168.255.255**
    

En tu homelab, todas tus VLAN usarán estos rangos.

Ejemplo aplicado:

- LAN → 10.10.0.0/24
    
- IoT → 10.20.0.0/24
    
- LAB → 10.30.0.0/24
    
- HONEYNET → 10.40.0.0/24
    

(Esta estructura se define en [[20_Diseño_Arquitectura/20_01_Arquitectura_Logica/20_01_04_Mapa_de_VLANs|20_01_04 Mapa de VLANs]].)

---

## **B) IP Pública**

Es la IP otorgada por tu proveedor (ISP).  
Es visible desde Internet.

El router del ISP la entrega a tu firewall dedicado.

En tu arquitectura:

- el **PC de tu pareja** nunca la verá
    
- tu **NAS nunca deberá exponerse**
    
- tus **honeypots sí podrían exponerse** (si quieres capturar ataques reales)
    

---

## **C) IP Virtual / IP de gestión**

Algunos dispositivos crean IP virtuales para:

- alta disponibilidad
    
- gestión
    
- servicios internos
    
- contenedores Docker
    

La verás más adelante en:

- [[30_Implementacion/30_02_Despliegue_Docker|Docker en el SOC]]
    
- [[30_Implementacion/30_03_Despliegue_Wazuh_SIEM|Wazuh y contenedores]]
    

---

# **3. Cómo se asignan las IPs en tu SIEM-HomeLab**

Tienes **dos métodos de asignación**:

---

## **A) IP por DHCP (Automática)**

El servidor DHCP asigna la IP al dispositivo.

En tu homelab:

- el **firewall** será el servidor DHCP para todas las VLAN
    
- cada VLAN tendrá un rango (pool) distinto
    
- puedes usar **reservas** para dispositivos críticos
    

DHCP se explica a fondo en:

- [[10_Teoria_Base/10_01_Conceptos_de_Red/10_01_04_DHCP_y_Asignacion|10_01_04 DHCP]]
    

---

## **B) IP Estática (Manual)**

La IP se fija a mano.

Se usa para:

- Firewall
    
- Switch
    
- NAS
    
- Servidores del SOC
    
- APs
    
- Honeypots
    
- Máquinas de laboratorio
    
- Router ISP (modo bridge o similar)
    

Ejemplo recomendado:

```
Firewall: 10.10.0.1
Switch:   10.10.0.2
NAS:      10.10.0.10
Wazuh:    10.10.0.50
Suricata: 10.10.0.60
```

---

# **4. Estructura de una dirección IP**

Ejemplo:

```
10.30.0.57
```

Descomposición:

- **10** → red principal
    
- **30** → subred asociada a VLAN (ej. LAB)
    
- **0** → parte secundaria del segmento
    
- **57** → host concreto (un PC, el Kali, etc.)
    

Cuando implementes VLANs, verás que cada segmento sigue su propio patrón.

Esto se desarrolla en:

- [[10_Teoria_Base/10_01_Conceptos_de_Red/10_01_03_Subredes_y_Mascaras|Subredes]]
    
- [[20_Diseño_Arquitectura/20_01_Arquitectura_Logica/20_01_03_Modelo_de_Segmentacion|Segmentación Lógica]]
    

---

# **5. Dirección de Gateway**

Es la dirección que indica _“por dónde salgo de mi red hacia otras redes”_.

En tu arquitectura:

- el firewall será el **gateway de todas las VLAN**
    
- cada VLAN tendrá su puerta de enlace propia
    

Ejemplo:

```
VLAN LAN → 10.10.0.1
VLAN IoT → 10.20.0.1
VLAN LAB → 10.30.0.1
VLAN HONEY → 10.40.0.1
```

Esto permite:

- aislar segmentos
    
- controlar acceso
    
- registrar rutas
    
- inspeccionar tráfico
    

Relacionado con:

- [[10_Teoria_Base/10_01_Conceptos_de_Red/10_01_05_NAT_y_Gateway|NAT y Gateway]]
    

---

# **6. Clases de IP (A, B, C)**

Son una clasificación antigua pero útil para comprender la escala de redes.

- **Clase A:** 10.x.x.x → muy grandes
    
- **Clase B:** 172.16.x.x → medianas
    
- **Clase C:** 192.168.x.x → pequeñas
    

En redes modernas se usa **CIDR** (notación /xx), que veremos en detalle en:

- [[10_Teoria_Base/10_01_Conceptos_de_Red/10_01_03_Subredes_y_Mascaras|Subredes y Máscaras]]
    

---

# **7. Ejemplo aplicado SIEM-HomeLab**

## **VLAN LAN**

```
Rango: 10.10.0.0/24
Gateway: 10.10.0.1
Dispositivos:
- NAS (10.10.0.10)
- Tu PC (10.10.0.20)
- Wazuh (10.10.0.50)
```

## **VLAN IoT**

```
Rango: 10.20.0.0/24
Gateway: 10.20.0.1
Dispositivos:
- bombillas
- robots
- electrodomésticos
```

## **VLAN LAB**

```
Rango: 10.30.0.0/24
Gateway: 10.30.0.1
Dispositivos:
- Kali Linux
- Máquinas vulnerables
- Honeypots auxiliares
```

## **VLAN Honeypots (Aislada)**

```
Rango: 10.40.0.0/24
Gateway: 10.40.0.1
Dispositivos:
- Cowrie
- Dionaea
- Honeyd
```

Cada VLAN:

- tiene su propio rango
    
- tiene su propio gateway
    
- está controlada por reglas del firewall
    
- será visible en Suricata si así lo decides
    
- puede ser monitorizada por tu SIEM
    

---

# **8. Cómo usarás todo esto en el SOC**

El direccionamiento IP permite:

- identificar dispositivos en los logs
    
- correlacionar eventos en Wazuh
    
- visualizar flujos en Suricata
    
- aplicar reglas por VLAN
    
- aislar hosts comprometidos
    
- detectar movimientos laterales
    
- analizar escaneos de red reales
    

El SOC no funciona sin una estructura IP clara y ordenada.

---
