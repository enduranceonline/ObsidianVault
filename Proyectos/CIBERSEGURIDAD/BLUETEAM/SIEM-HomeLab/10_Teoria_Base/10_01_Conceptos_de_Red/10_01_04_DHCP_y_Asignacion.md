

---

DHCP es uno de los componentes fundamentales de toda red. Más allá de asignar IPs, define **la identidad operacional** de cada dispositivo y determina cómo será interpretado por el firewall, el IDS y el SIEM.

En un SIEM-HomeLab con segmentación avanzada, DHCP es la columna vertebral que mantiene orden, trazabilidad y seguridad.

---

# **1. Qué es DHCP**

DHCP (Dynamic Host Configuration Protocol) asigna automáticamente:

- IP
    
- máscara
    
- gateway
    
- DNS
    
- lease time
    
- parámetros adicionales de red
    

Esto evita configuraciones manuales y garantiza que todos los dispositivos se integren correctamente en su VLAN y en la arquitectura de seguridad.

Sin DHCP bien organizado:

- la red se vuelve inconsistente
    
- aparecen colisiones de IP
    
- el firewall pierde contexto
    
- el SIEM deja de correlacionar correctamente
    

---

# **2. Cómo funciona DHCP (flujo completo)**

1. **DHCP Discover** — el host anuncia que necesita una IP
    
2. **DHCP Offer** — el servidor propone una IP disponible
    
3. **DHCP Request** — el cliente la solicita
    
4. **DHCP Ack** — el servidor confirma la asignación
    

Este intercambio establece la identidad base del dispositivo dentro de su subred.

---

# **3. Qué parámetros asigna DHCP en tu SIEM-HomeLab**

El servidor DHCP del firewall (OPNsense/pfSense) entrega:

- **IP dentro del rango de la VLAN**
    
- **Gateway** correspondiente
    
- **DNS** (controlado por el firewall)
    
- **Máscara /24**
    
- **Lease time**
    
- **Opciones avanzadas (NTP, TFTP, rutas, DNS privados)**
    

El control del DHCP por VLAN es esencial en un SOC porque garantiza que **cada dispositivo recibe la configuración adecuada para su nivel de seguridad**.

---

Aquí tienes una versión **más explicada, más técnica y más profundamente fundamentada** del apartado:

---

## 💡3.1 Por qué el firewall es el mejor servidor DHCP

En una red simple, DHCP podría estar en el router del ISP o incluso en un NAS.  
Pero en una red segmentada y orientada a seguridad —como tu SIEM-HomeLab— **el único lugar correcto para colocar DHCP es el firewall**.

La razón es que _todos los mecanismos de control, aislamiento, auditoría y trazabilidad dependen del firewall_, y DHCP participa directamente en estos procesos.

A continuación se explica qué capacidades tiene el firewall que ningún otro dispositivo posee.

---

### **3.1.1 El firewall es el único punto que ve _todas_ las VLAN**

Un servidor DHCP necesita:

- escuchar peticiones desde cualquier VLAN
    
- entregar configuraciones distintas según la VLAN
    
- saber qué gateway asignar en cada caso
    

El firewall:

- tiene una interfaz virtual por VLAN
    
- conoce la topología completa
    
- sabe qué dispositivos se conectan a qué segmento
    
- tiene contexto de seguridad asociado a cada red
    

Un NAS, un AP o un router ISP **no tienen esta visibilidad global**.

---

### **3.1.2 Controla los gateways, así que controla la ruta del tráfico**

Como cada VLAN tiene un **gateway diferente**, DHCP debe entregar el gateway correcto.

Ejemplo:

- VLAN LAN → 10.10.0.1
    
- VLAN IoT → 10.20.0.1
    
- VLAN LAB → 10.30.0.1
    
- VLAN Honeypots → 10.40.0.1
    

El firewall es quien:

- define quién puede salir a Internet
    
- define qué VLAN puede comunicarse con cuál
    
- determina si un host puede hablar con un servidor
    
- inspecciona todo el tráfico entre segmentos
    

Si DHCP estuviera fuera del firewall, **el gateway sería externo al control de seguridad**, lo cual rompe la estructura del SOC.

---

### **3.1.3 Puede registrar logs muy valiosos para el SIEM**

Cuando DHCP está integrado en el firewall, cada asignación queda registrada con:

- MAC
    
- IP
    
- timestamp
    
- VLAN
    
- interfaz
    
- hostname (si lo reporta el cliente)
    
- opciones asignadas
    

Estos logs permiten en el SIEM:

- correlación de identidad
    
- rastreo de cuándo un host empezó actividad
    
- análisis de patrones (por ejemplo, IoT que renueva DHCP cada minuto)
    
- detección de nuevos dispositivos desconocidos
    
- identificación de ataques DHCP spoofing o starvation
    

Si DHCP está en un NAS o en un router externo:

❌ no tienes logs centralizados  
❌ no aparecen correlacionados con firewall + IDS  
❌ no puedes auditar los eventos desde una única fuente

---

### **3.1.4 Protege contra servidores DHCP falsos (Rogue DHCP)**

Un atacante podría:

- conectar un portátil a la red
    
- activar un servidor DHCP falso
    
- entregar gateways incorrectos
    
- redirigir tráfico
    
- capturar información
    
- lanzar ataques Man-in-the-Middle
    

El firewall puede:

- detectar intentos rogue DHCP
    
- bloquearlos automáticamente
    
- generar alertas en Suricata
    
- registrar todo para el SIEM
    

Un router ISP o un NAS **no tiene mecanismos de seguridad para esto**.

---

### **3.1.5 Centraliza todas las funciones relacionadas: DHCP + DNS + NAT + Firewall Rules**

DHCP forma parte de una cadena:

```
DHCP → DNS → Firewall rules → NAT → SIEM
```

El firewall es el único dispositivo capaz de:

- entregar DHCP
    
- forzar DNS interno
    
- aplicar reglas por IP
    
- hacer NAT
    
- inspeccionar tráfico
    
- alimentar el SIEM con logs de red
    
- detectar comportamientos anómalos
    

Separar esto en dispositivos diferentes crea inconsistencias:

- DHCP da una IP
    
- DNS está en otro sitio
    
- NAT está en otro
    
- logs no están sincronizados
    
- reglas pueden fallar
    

En entornos profesionales, **todo esto se centraliza en un único dispositivo: el firewall**.

---

### **3.1.6 Mantiene correlación MAC ↔ IP ↔ VLAN ↔ Dispositivo (fundamental para un SOC)**

Un SOC necesita saber en todo momento:

- qué IP corresponde a qué dispositivo
    
- en qué VLAN está
    
- qué MAC lo identifica
    
- cuándo se conectó
    
- qué tráfico generó
    
- qué alertas produjo
    

El firewall mantiene esta relación de forma automática y consistente.

Si DHCP estuviera en otro dispositivo:

❌ perderías correlación  
❌ aumentaría el ruido del SIEM  
❌ sería más difícil investigar incidentes  
❌ complicarías los análisis de Suricata  
❌ fragmentarías los logs de red

---

### **3.1.7 Centraliza auditorías, reservas y gestión de dispositivos**

Desde el firewall puedes:

- ver todos los dispositivos de la red
    
- gestionar qué IP le toca a cada uno
    
- reservar direcciones
    
- cambiar rangos sin tocar dispositivos
    
- ver intentos de conexión sospechosos
    
- identificar hosts comprometidos
    
- controlar dispositivos desconocidos
    

Si DHCP está fuera:

- tendrías dos lugares diferentes para revisar
    
- se multiplican los puntos de fallo
    
- se complica toda la administración
    
- los logs no coinciden con los eventos de seguridad
    

---

Si quieres, puedo:

- **insertar este bloque automáticamente en la nota completa**,
    
- o **pasar al siguiente apartado: 10_01_05 NAT y Gateway**.

---

## **🔐 3.2 DHCP, DNS y SOC — Relación crítica en un entorno de seguridad**

En una red normal, DHCP da una IP y DNS permite navegar.  

En un SOC, esta relación define quién es cada dispositivo, cómo aparece en los logs y cómo se correlacionan los eventos.

Esta relación DHCP → DNS → SIEM es **uno de los pilares más importantes de tu proyecto**.

---

### **3.2.1 DHCP y DNS crean identidad dual (IP + nombre)**

DHCP asigna la IP.  
DNS asigna el nombre del host.

En el SIEM verás eventos como:

```
src.ip: 10.10.0.25
src.hostname: david-desktop.lan
src.mac: AB:CD:00:12:9F
vlan: LAN
event: suspicious outbound traffic
```

Esto permite:

- identificar qué dispositivo exacto genera una alerta
    
- diferenciar eventos de IoT vs LAN
    
- rastrear movimientos laterales
    
- detectar actividad fuera de lo normal
    

Sin DNS controlado → solo verías IPs sueltas.

---

### **3.2.2 Por qué un firewall debe controlar DNS en tu red**

Si usas DNS externos:

- NO verás consultas sospechosas
    
- NO podrás detectar dominios maliciosos
    
- Suricata no verá tráfico DNS relevante
    
- Wazuh no correlacionará eventos
    
- un atacante podría usar DNS para exfiltrar información sin ser detectado
    

Por eso en un SOC:

✔ LAN → usa DNS del firewall  
✔ IoT → DNS filtrado  
✔ LAB → DNS flexible  
✔ Honeypots → DNS bloqueado o restringido

---

### **3.2.3 DNS como fuente de inteligencia para el SIEM**

El SIEM puede detectar:

- dominios maliciosos
    
- DGA (dominios aleatorios generados por malware)
    
- beaconing
    
- DNS tunneling
    
- IoT hablando con servidores desconocidos
    
- consultas anómalas a horas inusuales
    

Nada de esto es visible si los hosts usan DNS externos.

---

### **3.2.4 Integración DHCP → DNS → Firewall → Suricata → SIEM**

El ciclo completo ideal de tu SIEM-HomeLab:

1. DHCP da IP + DNS
    
2. El dispositivo consulta DNS a tu firewall
    
3. El firewall registra consultas
    
4. Suricata analiza tráfico DNS
    
5. Wazuh recoge logs DNS + logs de red
    
6. El SIEM correlaciona:
    
    - dominio
        
    - IP
        
    - hostname
        
    - VLAN
        
    - MAC
        
    - reglas del firewall
        
    - alertas del IDS
        

Resultado: **visibilidad completa**, como en un SOC real.

---

# **4. Scope o rango de DHCP por VLAN**

### **LAN (10.10.0.0/24)**

- Rango: 10.10.0.100–10.10.0.200
    

### **IoT (10.20.0.0/24)**

- Rango: 10.20.0.50–10.20.0.200
    

### **LAB (10.30.0.0/24)**

- Rango: 10.30.0.50–10.30.0.200
    

### **HONEYPOTS (10.40.0.0/24)**

- Rango: 10.40.0.100–10.40.0.150
    

Esto asegura orden, aislamiento y trazabilidad.

---

Aquí tienes una **versión mucho más explicada, clara y profunda** del apartado **5. Reservas DHCP**, completamente alineada con tu proyecto SIEM-HomeLab y con un enfoque profesional SOC.

Este bloque está listo para **reemplazar** al actual dentro de la nota 10_01_04.

---

# **5. Reservas DHCP**

Una **reserva DHCP** es un mecanismo mediante el cual el servidor DHCP asigna **siempre la misma dirección IP** a un dispositivo concreto basándose en su **MAC address**.

No es una IP estática configurada manualmente en el dispositivo:  
es una **IP dinámica fija**, controlada desde el firewall.

Esto combina lo mejor de ambos mundos:  
✔ estabilidad de IP estática  
✔ gestión centralizada de DHCP  
✔ trazabilidad completa para SOC

---

## **5.1 ¿Qué es exactamente una reserva DHCP?**

Una reserva DHCP es una entrada en tu firewall del tipo:

```
MAC → IP fija → VLAN → Nombre → Notas
```

Ejemplo real:

```
MAC: AA:BB:CC:DD:EE:FF
IP:  10.10.0.10
VLAN: LAN
Nombre: NAS
```

Significa:

- Cuando el NAS pida una IP,
    
- El firewall siempre le dará **10.10.0.10**,
    
- Esté donde esté dentro de esa VLAN,
    
- Sin que tengas que configurarlo manualmente desde el NAS.
    

---

## **5.2 ¿Para qué sirve en tu SIEM-HomeLab?**

Las reservas DHCP son fundamentales para que:

### **5.2.1 El firewall sepa exactamente qué dispositivo es cada IP**

Sin IP fija, hoy un NAS puede ser 10.10.0.45 y mañana 10.10.0.73.  
Eso rompe:

- reglas de firewall
    
- reglas de IDS
    
- correlación en el SIEM
    
- auditorías
    
- trazabilidad de incidentes
    

Con una reserva:

- “NAS = 10.10.0.10” siempre
    
- “Wazuh = 10.10.0.50” siempre
    
- “Suricata = 10.10.0.60” siempre
    

Toda la red se vuelve **determinista**.

---

### **5.2.2 El SIEM (Wazuh) pueda correlacionar eventos correctamente**

Si la IP cambia constantemente:

- un escaneo mañana parece venir de “otro dispositivo”
    
- un malware hoy parece en otro host
    
- el historial del dispositivo se fragmenta
    
- las alertas pierden contexto
    

Con una IP fija por reserva:

Wazuh puede hacer correlación continua:

```
10.20.0.40 → siempre IoT
10.30.0.25 → siempre Kali
10.40.0.15 → siempre Honeypot
```

Esto es esencial en análisis forense.

---

### **5.2.3 Suricata (IDS) identifique tráfico correctamente**

El IDS analiza paquetes según:

- IP origen
    
- IP destino
    
- VLAN
    
- Reglas activas
    

Si un honeypot cambia de IP, tus reglas de Suricata dejan de funcionar.

Con reserva:

- tus reglas funcionan siempre
    
- las alertas de IDS son consistentes
    
- el firewall sabe en qué VLAN está cada host
    
- el análisis de tráfico tiene sentido
    

---

### **5.2.4 Evitar colisiones de IP**

Las colisiones ocurren cuando dos dispositivos intentan usar la misma IP.

Sin reservas:

- un PC manualmente configurado con IP estática puede chocar con el DHCP
    
- un IoT defectuoso puede pedir una IP antigua
    
- una VM clónica puede repetir la IP base
    

Con reservas centralizadas:

✔ No hay duplicados  
✔ No hay conflictos  
✔ No hay “IPs fantasma”  
✔ El firewall tiene control total

---

### **5.2.5 Simplificar auditoría y documentación**

Una vez creadas las reservas, tienes:

- un mapa completo de tu red
    
- una tabla perfecta para tu documentación en Obsidian
    
- la lista de todos los dispositivos importantes
    
- IPs predecibles para diagramas y Excalidraw
    
- una visión clara de dónde está cada pieza de tu SOC
    

Tu 20_01 Arquitectura Lógica se beneficia directamente de esto.

---

### **5.2.6 Dispositivos donde una reserva DHCP es obligatoria en tu diseño**

#### ✔ **NAS**

Servicios, backups, archivos, permisos → necesita IP fija.

#### ✔ **Wazuh Manager**

El SIEM depende de su ubicación exacta.

#### ✔ **Suricata (IDS)**

El IDS debe tener visibilidad perfecta y consistente.

#### ✔ **Puntos de acceso (APs)**

Para gestión unificada y futuras VLAN por SSID.

#### ✔ **Switch gestionable**

Para configurar VLANs, STP, trunking, SPAN/mirror…

#### ✔ **Honeypots**

No deben moverse de IP o perderías detecciones.

#### ✔ **PC personal**

Para logs consistentes y reglas personalizadas.

#### ✔ **Firewall secundario / sensores**

Cualquier equipo de infraestructura.

---

### **5.2.7 Ventajas clave**

#### ✔ **Orden**

Cada dispositivo tiene su “caja” IP bien definida.

#### ✔ **Trazabilidad**

Puedes ver el historial completo de un host en el SIEM.

#### ✔ **Coherencia SIEM**

Las alertas mantienen contexto porque la IP estática nunca cambia.

#### ✔ **Control centralizado**

Puedes reconfigurar toda la red desde el firewall, sin tocar dispositivos.

#### ✔ **Auditoría sencilla**

Puedes exportar todas las reservas y tener un documento perfecto en Obsidian.

#### ✔ **Evita colisiones**

Las IP están asignadas a MAC específicas, evitando duplicados.

---

## **6. IP manual vs DHCP con reserva

Tanto una IP manual como una reserva DHCP pueden proporcionar una dirección fija, pero **su impacto en seguridad, trazabilidad y gestión del SIEM-HomeLab es totalmente diferente**.

En un entorno segmentado con firewall, IDS y SIEM, la elección correcta es crítica.  
Esta sección explica por qué **DHCP con reserva** es la opción profesional.

---

### **6.1 IP manual (configurada directamente en el dispositivo)**

Una IP manual se introduce directamente en el equipo:

```

IP: 10.10.0.50  
Máscara: 255.255.255.0  
Gateway: 10.10.0.1  
DNS: 10.10.0.1

```

Aunque parece simple, presenta muchos riesgos en una red segmentada.

#### 🔹No está centralizada**
Cada dispositivo mantiene su propia configuración.  
Si cambias VLANs, rangos o gateways:

- hay que modificar cada host manualmente,
- puedes olvidar alguno,
- aparecen inconsistencias entre segmentos.

Esto **no escala** y provoca errores.

#### **🔹 Riesgo alto de errores humanos**
Una IP escrita incorrectamente puede causar:

- pérdida de conectividad,
- colisiones,
- tráfico fuera de VLAN,
- problemas en reglas de firewall.

En un entorno con múltiples VLAN, estos errores se multiplican.

#### **🔹 Mala trazabilidad en el SIEM**
Con IP manual:

- el firewall no registra asignación de lease,
- Wazuh recibe eventos sin correlación previa,
- Suricata ve tráfico sin contexto MAC ↔ IP,
- el análisis forense se complica.

Si la IP cambia por error, **pierdes la continuidad del dispositivo** en los logs.

#### 🔹 Auditoría distribuida y confusa**
Con IPs manuales, no existe una lista centralizada de:

- qué IP pertenece a quién,
- qué MAC corresponde a cada host,
- qué VLAN usa cada dispositivo.

Rompe completamente la filosofía de inventario SOC.

#### 🔹 Incoherencia si cambias dispositivos de VLAN**
Si mueves un host de una VLAN a otra pero su IP manual permanece:

- queda “huérfano” en la red,
- rompe reglas del firewall,
- puede saltarse inspecciones del IDS,
- queda parcialmente desconectado.

---

### **6.2 DHCP con reserva (recomendado en todas las redes segmentadas)**

En una reserva DHCP, el firewall asigna la misma IP siempre a una MAC concreta:

```

MAC: AA:BB:CC:DD:EE:FF  
→ IP fija 10.10.0.10  
→ VLAN LAN

```

Esto genera una red determinista y segura.

#### **6.2.1 100% centralizado**
El firewall concentra:

- reservas,
- rangos,
- gateways,
- DNS,
- logs de asignaciones,
- auditorías.

Si algún día cambias rangos o VLANs, modificas todo desde **un único punto**.

#### **6.2.2 Correlación perfecta MAC ↔ IP ↔ VLAN**
Con IP por reserva:

- Suricata reconoce tráfico por host real,
- Wazuh ve continuidad entre eventos,
- el firewall aplica reglas coherentes,
- puedes rastrear cualquier incidente en segundos.

Es la base de una arquitectura SOC.

#### **6.2.3 Integración total con Firewall + IDS + SIEM**

Al centralizar DHCP en el firewall:

- Suricata ve tráfico asociado a la misma IP siempre
- Wazuh correlaciona eventos a largo plazo,
- el firewall registra todo el ciclo de red del host.

Nada de esto es posible con IP manual.

#### **6.2.4 Evita conflictos y colisiones**

Con reservas:

- dos dispositivos nunca recibirán la misma IP,
- las VMs clonadas no rompen la red,
- IoT defectuoso no pide IPs antiguas,
- no hay “IPs duplicadas” difíciles de diagnosticar.

La red se mantiene estable.

#### **6.2.5 Auditoría perfecta**

Desde el firewall puedes exportar:

- lista completa de IPs,
- MACs,
- VLAN asociada,
- dispositivos críticos.

Esto se integra perfectamente en tu documentación de Obsidian.

---

### **6.3 Conclusión práctica**

| Método | Beneficios | Problemas |
|-------|------------|-----------|
| **IP manual** | Funciona en redes pequeñas | Descentralizada, errores, mala trazabilidad, rompe SIEM/IDS |
| **DHCP + reserva** | Profesional, seguro, centralizado, escalable | Requiere configurar las reservas (paso inicial) |

---

## **7. Seguridad y visibilidad SOC basadas en DHCP**

DHCP no es solo un mecanismo para asignar IPs.  

En una arquitectura SOC, DHCP determina **cómo se identifica cada dispositivo**, qué trazabilidad existe en la red y qué nivel de visibilidad tienen:

- el firewall,  
- Suricata,  
- Wazuh,  
- y los análisis de red.

Este apartado explica por qué DHCP es una pieza crítica en la seguridad de tu SIEM-HomeLab.

---

### **7.1 DHCP como origen de identidad en el SOC**

Cada vez que un dispositivo obtiene una IP, el firewall registra:

- MAC  
- IP asignada  
- VLAN  
- hostname (si está disponible)  
- hora exacta de conexión  
- duración del lease  

Estos datos se convierten en la **identidad operativa del host** dentro del ecosistema de seguridad.

Sin DHCP centralizado:

- la identidad de un host se fragmenta,  
- Wazuh no puede correlacionar eventos,  
- Suricata detecta tráfico “huérfano”,  
- el análisis forense se vuelve más lento e inexacto.

---

### **7.2 Interacción DHCP → Firewall → IDS → SIEM**

Este es el flujo de seguridad real:

1. **DHCP asigna IP**  
2. El firewall registra la asignación  
3. El tráfico que genera ese host pasa por Suricata  
4. Suricata genera alertas asociadas a esa IP  
5. Wazuh recoge logs del firewall y del IDS  
6. El SIEM correlaciona:  
   - IP  
   - MAC  
   - VLAN  
   - alertas IDS  
   - reglas de firewall  
   - timestamp  
   - hostname

==Este pipeline SOC solo funciona correctamente si DHCP, DNS y firewall están **unificados**.==

---

### **7.3 Detección de anomalías gracias a DHCP**

Con información de DHCP y reservas, puedes detectar:

- dispositivos que cambian de VLAN inesperadamente,  
- conexiones de hosts desconocidos (MAC no registrada),  
- intentos de suplantación DHCP,  
- IoT moviéndose entre redes,  
- patrones anómalos de renovación de DHCP (indicador de compromiso),  
- nuevos dispositivos que aparecen sin autorización.

Estos eventos son visibles en Wazuh y permiten actuar rápido.

---

### **7.4 DHCP y análisis forense**

Durante una investigación, puedes responder en segundos a preguntas clave:

- ¿Qué dispositivo tenía esta IP hace 3 días a las 15:41h?  
- ¿Cuál era su MAC?  
- ¿En qué VLAN estaba?  
- ¿Qué tráfico generó en Suricata?  
- ¿Qué alertas produjo en Wazuh?  
- ¿Qué reglas del firewall se aplicaron?  
- ¿Qué hostname reportaba?  

Sin DHCP centralizado y reservado, muchas de estas respuestas serían imposibles.

---

### **7.5 Integración con Zero Trust (versión doméstica)**

Aunque no vas a aplicar Zero Trust empresarial, sí puedes aplicar una versión “lite”:

- ningún dispositivo es de confianza por defecto,  
- DHCP asigna identidad,  
- el firewall valida la segmentación,  
- Suricata inspecciona su tráfico,  
- el SIEM analiza el comportamiento.

Con reservas DHCP correctamente definidas, tienes un modelo de identidad estable para poder aplicar reglas más estrictas por VLAN.

---

### **7.6 Conclusión del punto 7**

DHCP es mucho más que un servicio de asignación automática de IPs.  
En tu SIEM-HomeLab es:

- **la base de la identidad del host**,  
- **el origen de la trazabilidad**,  
- **el inicio de la cadena de análisis para IDS/SIEM**,  
- **la clave del orden en una red segmentada**,  
- **un punto crítico de seguridad**,  
- **y un componente obligatorio para un SOC realista**.

Por eso, todo el proyecto —segmentación, IDS, SIEM, honeypots, firewalling— depende de que DHCP esté **centralizado, reservado y correctamente documentado**.

---

## **8. Enlaces internos**

Estos enlaces amplían o complementan los conceptos necesarios para entender DHCP, reservas, DNS y su papel dentro del SIEM-HomeLab:

- [[10_01_01_Dispositivos_Basicos|10_01_01 – Dispositivos básicos]]
  (Interfaces de red, switches, routers y cómo interactúan con DHCP)

- [[10_01_02_Direccionamiento_IP|10_01_02 – Direccionamiento IP]]
  (Qué es una IP, máscaras, gateways y por qué DHCP las asigna así)

- [[10_01_03_Subredes_y_Mascaras|10_01_03 – Subredes y Máscaras]]
  (Por qué tus VLAN serán /24 y cómo se organiza el espacio de red)

- [[10_01_06_DNS|10_01_06 – DNS]]  
  (Nota clave: DHCP y DNS trabajan juntos para identidad y trazabilidad)

- [[10_01_07_VLANs_y_Segmentacion|10_01_07 – VLANs y Segmentación]]
  (DHCP entrega IPs distintas según VLAN y define la identidad del host)

- [[20_01_Arquitectura_Logica|20_01 – Arquitectura Lógica]]
  (Dónde se ubican los rangos DHCP en el diseño general de la red)

- [[20_01_03_Modelo_de_Segmentacion|20_01_03 – Modelo de Segmentación]]
  (Cómo cada rango DHCP asigna roles según la VLAN: LAN, IoT, LAB, Honeypots)

- [[20_03_03_Diagrama_Firewall_y_Segmentacion|20_03_03 – Firewall y Segmentación]]
  (DHCP forma parte del firewall y participa en las reglas de tráfico)

- [[30_02_Wazuh_Agentes|30_02 – Agentes Wazuh]]
  (Cómo DHCP + IP fija impacta en la correlación de agentes dentro del SIEM)

- [[30_03_Suricata|30_03 – Suricata]]
  (El IDS depende de IP fija para identificar tráfico y alertas)

- [[30_05_DNS_Logging|30_05 – DNS Logging]]
  (Base para comprender por qué DHCP debe forzar DNS del firewall)

---


