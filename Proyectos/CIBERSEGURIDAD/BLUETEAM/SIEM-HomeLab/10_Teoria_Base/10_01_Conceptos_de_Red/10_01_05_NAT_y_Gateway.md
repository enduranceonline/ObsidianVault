

---

NAT y Gateway son dos elementos esenciales que determinan **cómo salen los dispositivos de tu red hacia Internet** y cómo se **rutea** el tráfico entre VLANs dentro de tu SIEM-HomeLab.  
Ambos conceptos están estrechamente relacionados con DHCP, subredes y segmentación.

Esta nota explica de forma clara:

- qué es NAT,
    
- qué tipos existen,
    
- qué es un gateway y su papel en cada VLAN,
    
- cómo funcionan juntos,
    
- y cuál es su impacto en un entorno SOC doméstico.
    

---

## **1️⃣ Qué es NAT (Network Address Translation)**

NAT es un mecanismo del firewall que permite que varias direcciones IP privadas **compartan una única IP pública** para acceder a Internet.

Ejemplo clásico:

```
Privadas: 

10.10.0.0/24
10.20.0.0/24
10.30.0.0/24

IP pública del ISP: 

84.92.X.X
```

Sin NAT, ningún dispositivo con IP privada podría salir a Internet.

---

## **2️⃣ Por qué NAT es necesario**

NAT no es simplemente un “traductor de direcciones”; es un componente crítico que permite que redes privadas funcionen en Internet **sin exponer su estructura interna**.  
En un SIEM-HomeLab con múltiples VLAN, NAT se convierte en el eje que garantiza:

- conectividad,
- seguridad,
- privacidad,
- aislamiento,
- inspección IDS,
- coherencia con Wazuh,
- y control total del tráfico saliente.

A continuación se explican las razones técnicas por las que NAT es imprescindible.

---

### **2.1 Internet solo enruta direcciones públicas**

Internet funciona mediante **ruteo global BGP**, un protocolo que gestiona bloques de direcciones **únicas y públicas**.  
Las direcciones privadas definidas en el RFC1918:

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

son **no enrutable** en Internet.  
Es decir:

- ningún router de Internet aceptará tráfico cuyo origen sea una IP privada,  
- ningún ISP enviará tráfico hacia una IP privada de tu red doméstica,  
- los routers descartan automáticamente ese tipo de paquetes.

Sin NAT, un paquete saliente así:

```

src: 10.10.0.25 → dst: 142.250.187.46 (Google)

```

sería descartado por el primer router del ISP, porque **no tiene una IP origen válida** para Internet.

NAT convierte ese paquete en:

```

src: 84.92.X.X → dst: 142.250.187.46

```

dándole una dirección válida y enrutable globalmente.

---

### **2.2 NAT te protege de exponer tu red interna**

Con NAT, ningún dispositivo dentro de tu red es visible desde Internet.  
Esto significa que un atacante externo:

- no puede escanear tus VLAN,  
- no puede descubrir cuántos dispositivos tienes,  
- no puede identificar tus rangos internos,  
- no puede localizar servicios vulnerables,  
- no puede apuntar directamente a tus dispositivos.

NAT introduce una capa de **opacidad estructural**:

#### NAT oculta:

- **tu topología interna** (cuántas VLAN existen)
- **tus rangos de red** (10.10.0.0/24, 10.20.0.0/24…)
- **el número de hosts** (no se ve si tienes 2 o 200 dispositivos)
- **los servicios internos** (NAS, Wazuh, honeypots, IoT…)
- **las IP privadas** (10.10.0.25 jamás aparece fuera)

Desde Internet, solo se ve:

```

1 IP pública ↔ firewall

```

El firewall decide si cualquier tráfico se permite o no, gracias a:

- la tabla de estados,
- las reglas de firewall,
- la inspección IDS.

Sin NAT, tu red entera sería escaneable y atacable directamente.

---

### **2.3 NAT permite segmentar sin depender del ISP**

En una arquitectura con múltiples VLAN:

```

LAN → 10.10.0.0/24  
IoT → 10.20.0.0/24  
LAB → 10.30.0.0/24  
Honeypots → 10.40.0.0/24

```

cada VLAN necesita:

- su propia puerta de salida (gateway),
- su aislamiento,
- sus reglas de firewall,
- sus restricciones,
- su control de tráfico.

#### Sin NAT tendrías 3 opciones (todas inviables en casa):

---

### **❌ Opción 1: Pedir múltiples IP públicas al ISP**
Para que cada VLAN salga sin NAT, necesitarías:

- una IP pública para LAN,  
- otra para IoT,  
- otra para LAB,  
- otra para Honeypots,  
- etc.

Los ISPs no ofrecen esto en servicios domésticos, y además sería:

- carísimo,  
- inseguro,  
- innecesario,  
- difícil de configurar,  
- imposible de controlar desde un firewall doméstico.

---

### **❌ Opción 2: Exponer dispositivos directamente a Internet (no NAT)**

Esto implicaría que:

- cámaras IoT,
- móviles,
- NAS,
- Wazuh,
- honeypots,
- switches

estarían **directamente accesibles desde Internet**.

Cualquier escaneo del tipo:

```

nmap 84.92.X.X/20

```

podría:

- encontrar servicios vulnerables,  
- descubrir tu topología,  
- identificar dispositivos,  
- detectar puertos activos,  
- explotar fallos del NAS o IoT.

Sería un desastre de seguridad.

---

### **❌ Opción 3: Usar routing público dentro de casa**

Esto implicaría que tus VLAN internas tendrían direcciones públicas variadas del ISP.  
Aparte de ser carísimo, esto:

- anula la privacidad,  
- rompe la segmentación,  
- impide inspección IDS pre-NAT,  
- destruye correlación SIEM,  
- expone toda tu red.

---

### **✔ Solución real: NAT por VLAN (lo que hace tu firewall)**

Tu firewall traduce tráfico de **todas tus VLAN** hacia la misma IP pública:

```

LAN → NAT → IP pública  
IoT → NAT → IP pública  
LAB → NAT → IP pública  
Honeypots → NAT → (opcional) IP pública o sin salida

```

Esto permite:

- segmentación real,
- aislamiento total,
- salida controlada,
- inspección IDS previa al NAT,
- análisis SOC completo,
- políticas específicas por VLAN,
- privacidad total.

En resumen:

**NAT es el eje que permite mezclar segmentación avanzada con acceso seguro a Internet en un entorno doméstico.**

---

## 3️⃣ Tipos de NAT 

NAT no es un único mecanismo: el firewall implementa varias formas de traducir direcciones y puertos dependiendo de si el tráfico **sale**, **entra**, o debe **multiplexarse** entre muchos dispositivos.  
Comprender estos tipos es esencial para tu SIEM-HomeLab, ya que afectan directamente a:

- cómo se inspecciona el tráfico en Suricata,  
- cómo se correlacionan eventos en Wazuh,  
- cómo se gestionan las políticas de firewall por VLAN,  
- cómo se expone (o no) un servicio interno.

---

### **3.1 Source NAT (SNAT)** – *El NAT de “salida”*

El **Source NAT** es el tipo de NAT que se aplica cuando un dispositivo interno quiere acceder a Internet.  
Su función es **reemplazar la IP origen privada** del paquete por la **IP pública del firewall**.

Ejemplo:

```

Dispositivo interno: 10.30.0.50  
IP pública del firewall: 84.92.X.X

```

Traducción SNAT:

```

10.30.0.50 → 84.92.X.X

```

#### **3.1.1 ¿Por qué ocurre SNAT?**

Porque Internet solo enruta direcciones públicas.  
El firewall:

1. recibe un paquete proveniente de una VLAN,  
2. inspecciona reglas de firewall,  
3. lo pasa por Suricata (pre-NAT),  
4. lo traduce (NAT),  
5. lo envía a Internet.

#### **3.1.2 Impacto en tu arquitectura SOC**

- Suricata ve el tráfico **antes** de la traducción (clave para el análisis).  
- Wazuh correlaciona conexiones usando la IP privada y la pública.  
- La tabla de estados guarda ambos valores.

#### **3.1.3 Cuándo se usa SNAT**

→ **99% del tráfico saliente**  
Web, DNS, actualizaciones, API, IoT… todo usa SNAT.

---

### **3.2 Destination NAT (DNAT)** – *El NAT de “entrada”*

El **Destination NAT** actúa sobre el tráfico que **llega desde Internet hacia tu red interna**, traduciéndolo hacia:

- un servidor interno,
- un servicio expuesto,
- un honeypot en pruebas.

Ejemplo conceptual:

```

Internet → 84.92.X.X:443 → DNAT → 10.10.0.10:443

```

#### **3.2.1 Usos típicos en entornos domésticos normales**

- Port forwarding para videojuegos  
- Acceso remoto (no recomendado sin VPN)  
- Exponer un servidor NAS (inseguro si no se controla)

#### **3.2.2 Usos controlados en tu SIEM-HomeLab**

- Honeypots que simulan servidores vulnerables  
- Pruebas controladas de ataques externos  
- Segmentación estricta para exponer únicamente un objetivo falso

#### **3.2.3 Cuándo evitar DNAT**

❌ IoT  
❌ NAS  
❌ Dispositivos de uso personal  
❌ Wazuh  
❌ PC sobremesa  
❌ Switches  
❌ APs  

Exponer estos dispositivos comprometería tu seguridad real.

#### **3.2.4 Relación DNAT → Firewall → IDS**

Todo paquete entrante DNAT pasa por:

1. firewall,  
2. tabla de estados,  
3. Suricata,  
4. reglas de segmentación.

Esto permite *analizar ataques reales* en honeypots de forma segura.

---

### **3.3 PAT (Port Address Translation)** – *Multiplexación de conexiones*

PAT es una extensión de SNAT.  
Además de traducir la IP origen, también traduce el **puerto origen** para diferenciar conexiones simultáneas de muchos dispositivos usando una sola IP pública.

Ejemplo real:

```

10.10.0.10:43321 → 84.92.X.X:50110  
10.10.0.50:49211 → 84.92.X.X:50111

```

Ambos comparten IP pública, pero cada flujo utiliza un puerto traducido distinto.

#### **3.3.1 ¿Por qué es necesario?**

Porque:

- decenas de dispositivos pueden salir a Internet a la vez,  
- cada uno necesita un canal único,  
- la IP pública es una sola,  
- NAT debe diferenciar cada sesión.

#### **3.3.2 Cómo lo gestiona el firewall**

Cada entrada de la tabla de estados guarda la tupla 5-tuple del flujo:

```

(src IP, src port, dst IP, dst port, protocolo)

```

El firewall usa esta información para:

- reconstruir cada conexión,  
- saber a qué dispositivo interno pertenece,  
- permitir o bloquear paquetes de retorno.

#### **3.3.3 Impacto en el SIEM**

Wazuh y Suricata pueden ver:

- qué dispositivo interno abrió la conexión,  
- qué servicio externo se contactó,  
- si el puerto origen es sospechoso,  
- si un malware usa puertos aleatorios para comunicarse con su C2.

---

### **3.4 Resumen profesional del uso en tu HomeLab**

| Tipo NAT | Dirección | Uso principal | Seguridad / SOC |
|----------|-----------|---------------|------------------|
| **SNAT** | Interno → Internet | Navegación normal | Suricata analiza pre-NAT; Wazuh correlaciona |
| **DNAT** | Internet → Interno | Honeypots | Control total por firewall; análisis de ataques reales |
| **PAT** | Interno → Internet (múltiples hosts) | Multiplexar conexiones | Base para identificar flujos y detectar anomalías |

---

### **Conclusión del punto 3**

Los tres métodos de NAT trabajan juntos para:

- permitir conectividad,  
- ocultar tu infraestructura,  
- mantener segmentación,  
- y proporcionar visibilidad completa al SOC.

La comprensión de estos tipos será clave cuando trabajes con:

- reglas avanzadas en OPNsense,  
- SNORT/Suricata pre-NAT,  
- correlación Wazuh agent ↔ IP privada ↔ IP pública,  
- y análisis de flujos sospechosos.

---

# **4️⃣ NAT + VLANs: la combinación crítica para tu SIEM-HomeLab**

Este es uno de los aspectos que más profundidad requiere.

Cada VLAN tiene su gateway interno:
```nginx
LAN        → 10.10.0.1
IoT        → 10.20.0.1
LAB        → 10.30.0.1
Honeypots  → 10.40.0.1
```
Pero **todas comparten una misma IP pública**, gracias a NAT.

### **4.1 Qué permite NAT por VLAN**

- LAN → salida completa a Internet
    
- IoT → salida limitada, sin acceso a LAN
    
- LAB → salida monitorizada
    
- Honeypots → sin NAT (no salen)
    

### **4.2 NAT solo aplica al tráfico que sale a Internet**

El tráfico **entre VLANs no pasa por NAT**, sino por reglas del firewall.

Esto es clave para:

- segmentación
    
- inspección IDS
    
- evitar movimiento lateral
    
- correlación SIEM
    

### **4.3 El firewall sabe exactamente de qué VLAN viene cada flujo**

Antes del NAT el firewall ve:

```css
src.ip: 10.20.0.45 (IoT)
```

Después del NAT se convierte en:

```css
84.92.X.X
```

Pero el firewall conserva contexto interno.  
Por eso Suricata y Wazuh siguen sabiendo:

- VLAN origen
    
- Dispositivo
    
- IP privada
    
- MAC

---

## **5️⃣ Qué es el Gateway**

El **gateway** es la **IP del firewall dentro de cada VLAN** y actúa como la **puerta de salida** hacia cualquier red externa: ya sea Internet o cualquier otra VLAN.  

En una red segmentada, el gateway es el componente que determina:

- qué tráfico puede salir,
- qué tráfico debe bloquearse,
- qué rutas son válidas,
- qué inspección se aplica,
- y cómo se gestiona el estado de cada conexión.

Sin gateway, un dispositivo no podría comunicarse fuera de su segmento.

Ejemplos en tu arquitectura:

```text
LAN        → 10.10.0.1
IoT        → 10.20.0.1
LAB        → 10.30.0.1
Honeypots  → 10.40.0.1
````

Cada dispositivo usa _únicamente_ la dirección del gateway asignada por DHCP para enviar:

- tráfico a otras VLAN,
    
- tráfico hacia Internet,
    
- tráfico hacia el firewall mismo,
    
- consultas DNS locales,
    
- comunicación con el SIEM (si corresponde).
    

---

### **5.1 El gateway decide absolutamente todo**

Cada paquete que sale de una VLAN pasa **sí o sí** por su gateway, lo que permite al firewall aplicar políticas granulares. Técnicamente, en este punto ocurren cinco decisiones críticas:

#### **1. Ruteo entre VLANs**

El gateway decide si el paquete puede salir a otra VLAN.  
Sin permiso explícito → paquete bloqueado.

#### **2. Salida a Internet**

El gateway determina:

- si la VLAN puede salir,
    
- por qué interfaz WAN,
    
- con qué reglas,
    
- y con qué nivel de inspección.
    

#### **3. Inspección por Suricata**

Antes de aplicar NAT, el firewall envía el paquete al IDS:

- Suricata inspecciona cabeceras y payload,
    
- aplica reglas según VLAN,
    
- identifica actividad maliciosa,
    
- bloquea si está en IPS mode.
    

#### **4. Aplicación de reglas de firewall**

El firewall consulta:

- reglas por VLAN,
    
- reglas por aplicación,
    
- reglas anti-lateral movement,
    
- reglas por horario,
    
- reglas basadas en alias dinámicos.
    

#### **5. Aplicación de NAT**

Una vez permitido el flujo:

- se aplica SNAT/PAT,
    
- se registra en tabla de estados,
    
- se asignan puertos traducidos.
    

El gateway es, literalmente, el **cerebro de la red segmentada**.

---

## **6️⃣ El papel del Gateway en una red segmentada**

Cuando un dispositivo envía tráfico hacia fuera, el firewall crea una entrada en la **tabla de estados**.  
Una _state entry_ representa exactamente:

- quién inició la conexión (IP origen),
    
- hacia dónde va (IP destino),
    
- en qué VLAN está,
    
- qué puertos usa,
    
- qué interfaz la recibió,
    
- qué NAT se aplicó,
    
- cuándo comenzó,
    
- si está abierta, establecida o cerrándose.
    

Ejemplo realista de flujo saliente:

```text
10.10.0.20:44321 → 172.217.22.14:443
NAT: 84.92.X.X:50112
VLAN: LAN
iface: LAN → WAN
state: ESTABLISHED
```

El firewall podrá reconstruir ese flujo exacto en cualquier momento.

Esto es **esencial para el SIEM**, porque Wazuh correlaciona:

- qué dispositivo generó la conexión,
    
- a qué destino fue,
    
- bajo qué VLAN,
    
- con qué usuario (si Sysmon registra el proceso),
    
- si el tráfico fue bloqueado o permitido,
    
- si hubo alertas en Suricata relacionadas.
    

---

### **6.1 Qué VLAN puede hablar con cuál**

El gateway es el único punto capaz de decidir si dos VLAN pueden comunicarse.

Ejemplo:

```
IoT → LAN  ❌ (denegado)
LAN → IoT  ✔ (acceso puntual)
LAB → LAN  ❌
LAN → Internet ✔
IoT → Internet ✔ (limitado)
Honeypots → Internet ❌
```

Estas decisiones se aplican antes de NAT, lo que permite:

- impedir movimiento lateral,
    
- aislar IoT,
    
- separar honeypots,
    
- crear entornos seguros LAB,
    
- proteger la red personal (LAN).
    

---

### **6.2 Qué VLAN puede salir a Internet**

La salida a Internet depende del gateway, no del dispositivo.  
Cada VLAN puede tener políticas completamente distintas:

- **IoT** → solo salida a Internet, sin acceso a LAN
    
- **Honeypots** → sin acceso a Internet (evita fugas o llamadas a C2)
    
- **LAB** → salida controlada y monitorizada
    
- **LAN** → salida completa, pero inspeccionada
    

Esto crea un entorno similar al de una empresa real:

- redes críticas no salen,
    
- usuarios y dispositivos tienen permisos diferenciados,
    
- IoT está aislado.
    

---

### **6.3 Qué reglas de NAT se aplican (por VLAN)**

El firewall aplica NAT **por interfaz lógica**, es decir, _por VLAN_.

Ejemplos reales:

|VLAN|NAT|Comentario|
|---|---|---|
|LAN|NAT estándar|Usuario normal|
|IoT|NAT restrictiva|Sin acceso lateral|
|LAB|NAT controlada|Para pruebas y análisis|
|Honeypots|Sin NAT|Aislamiento total|

Si una VLAN no debe salir a Internet (por ejemplo, Honeypots), basta con **no aplicar NAT** a esa interfaz.

Sin NAT → la red queda automáticamente aislada.

---

### **6.4 Punto de inspección del IDS (Suricata)**

El gateway es el punto donde Suricata puede inspeccionar el tráfico **antes del NAT**.  
Esto es muy importante porque analiza:

- IP privadas reales del host,
    
- VLAN origen,
    
- puertos originales,
    
- patrones de tráfico,
    
- ataques dirigidos a servicios internos,
    
- intentos de explotación,
    
- actividad maliciosa del IoT,
    
- exfiltración desde LAB,
    
- anomalías en honeypots.
    

Suricata siempre ve tráfico así:

```
src: 10.20.0.45 (IoT)
dst: 8.8.8.8:53
```

Antes de que se traduzca a:

```
src: 84.92.X.X
```

Esto garantiza una visibilidad TOTAL del comportamiento interno.

---

# **7️⃣ El pipeline real: DHCP → Gateway → NAT → IDS → SIEM**

Este es el flujo real que ocurre cada vez que un dispositivo de tu red sale a Internet:

```css
1. DHCP asigna IP, DNS y Gateway a un dispositivo
2. El dispositivo envía tráfico al Gateway (firewall)
3. El Gateway aplica reglas de VLAN y firewall
4. Suricata inspecciona el tráfico (pre-NAT)
5. NAT traduce la IP privada a IP pública
6. El tráfico sale a Internet
7. Suricata inspecciona respuestas
8. Wazuh correlaciona todo (IP, MAC, VLAN, reglas, alertas)
```

Este pipeline define **cómo trabaja tu arquitectura SOC**.

---

## **8️⃣ NAT y seguridad (visión SOC)**

NAT contribuye a tu seguridad en varios niveles:

### **8.1 Oculta tu red interna**

Los atacantes nunca ven:

- tus rangos privados
    
- número de dispositivos
    
- VLANs internas
    
- direcciones sensibles
    

### **8.2 Puede bloquear tráfico entrante no solicitado**

Cualquier tráfico no solicitado:

```
Internet → firewall (sin estado previo)
```

es descartado automáticamente.

### **8.3 Protege IoT**

Los dispositivos IoT no pueden ser expuestos accidentalmente.

### **8.4 Limpia tráfico para el SIEM**

Wazuh y Suricata ven tráfico real **antes de NAT**, permitiendo inspecciones precisas.

### **8.5 Control granular**

Puedes aplicar reglas por VLAN:

- IoT → NAT sin acceso lateral
    
- LAB → NAT monitorizado
    
- Honeypots → sin NAT
    

---

# **9️⃣ NAT real vs Packet Tracer**

Packet Tracer sirve para **comprender**, pero no para replicar la realidad.

### **9.1 Qué sí puedes practicar**

- NAT estático
    
- NAT dinámico
    
- PAT
    
- ACL por VLAN
    
- tráfico inter-VLAN
    
- port forwarding
    

### **9.2 Qué NO simula Packet Tracer**

- tabla de estados real
    
- inspección IDS
    
- logging del firewall
    
- NAT avanzado
    
- interacciones DHCP → Firewall → DNS → IDS → SIEM
    
- detecciones de Suricata
    
- correlación Wazuh
    

Tu HomeLab real será MUCHÍSIMO más avanzado.

En OPNsense/pfSense verás:

- reglas automáticas,
    
- tabla de estados,
    
- logs completos de traducción,
    
- opciones avanzadas para cada VLAN.
    

Esto te ayudará a comprender el flujo de tráfico entre segmentos.

---

## **🔟 Enlaces internos relacionados**

- [[10_01_02_Direccionamiento_IP|10_01_02 – Direccionamiento IP]]
    
- [[10_01_03_Subredes_y_Mascaras|10_01_03 – Subredes y Máscaras]]
    
- [[10_01_04_DHCP_y_Asignacion|10_01_04 – DHCP y Asignación]]
    
- [[10_01_06_DNS|10_01_06 – DNS]]
    
- [[10_01_07_VLANs_y_Segmentacion|10_01_07 – VLANs y Segmentación]]
    
- [[20_01_Arquitectura_Logica|20_01 – Arquitectura Lógica]]
    
- [[20_03_03_Diagrama_Firewall_y_Segmentacion|20_03_03 – Firewall y Segmentación]]
    
- [[30_03_Suricata|30_03 – Suricata (IDS)]]
    

---

