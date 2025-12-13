

---

Esta sección explica, con detalle y contexto, los dispositivos fundamentales que forman una red moderna. Entender cómo encaja cada pieza es crucial para diseñar y operar el SIEM-HomeLab, ya que cada dispositivo:

- genera tráfico
    
- filtra tráfico
    
- enruta tráfico
    
- produce logs
    
- o ofrece servicios necesarios para el SOC
    

Una arquitectura de seguridad no existe sin una base sólida de red, y esta nota te proporciona esa base.

---

# **1. Router del ISP (Proveedor de Internet)**

## **Contexto**

El router del ISP es el “punto de entrada” de tu casa a Internet. Es el único equipo que tiene relación directa con el proveedor y sirve de frontera entre el mundo exterior y tu red privada.

## **Características típicas**

El router doméstico suele combinar muchas funciones en un solo aparato:

- Router
    
- Firewall básico
    
- Switch de 4 puertos
    
- Punto de acceso WiFi
    
- Servidor DHCP
    

Este diseño está orientado a usuarios no técnicos, no a un entorno segmentado.

## **Por qué NO debe gestionar tu red**

Para un SIEM-HomeLab serio, este router es un cuello de botella:

- no permite VLANs reales
    
- no permite reglas detalladas
    
- no soporta port mirroring
    
- no permite integrar Suricata
    
- no permite integrar un SIEM
    
- suele tener firmware limitado/cerrado
    
- su firewall es muy básico
    

## **Rol real en tu proyecto**

→ _Un simple puente hacia tu firewall dedicado._

- Su única función será entregar la conexión WAN.
    
- No debe tener WiFi activado.
    
- No debe hacer NAT si se puede evitar.
    
- No debe tener servicios internos activos.
    

## **Notas relacionadas**

- [[10_Teoria_Base/10_01_Conceptos_de_Red/10_01_05_NAT_y_Gateway|NAT y Gateway]]
    
- [[20_Diseño_Arquitectura/20_01_Arquitectura_Logica/20_01_05_Rutas_y_Gateway|Diseño de rutas]]
    

---

# **2. Firewall Dedicado (OPNsense / pfSense)**

## **Contexto**

El firewall dedicado sustituye la lógica del router y se convierte en el **controlador central** de tu red. Es el equivalente doméstico a un firewall corporativo.

En tu arquitectura será:

- el cerebro
    
- la frontera
    
- el regulador
    
- la pieza que da orden y seguridad
    

## **Qué aporta un firewall dedicado**

Un firewall profesional permite:

- segmentación real por VLAN
    
- reglas detalladas por puerto, IP, protocolo o VLAN
    
- reglas específicas entre zonas
    
- NAT avanzado
    
- VPNs seguras
    
- DNS local seguro
    
- control de tráfico saliente
    
- integración IDS/IPS (Suricata)
    

## **Por qué es imprescindible**

Sin un firewall dedicado **no existe** un SOC funcional.

Es quien determina:

- qué tráfico puede existir
    
- qué tráfico ve Suricata
    
- qué tráfico puede llegar al SIEM
    
- dónde se puede mover un atacante
    
- cómo se aíslan los IoT y los honeypots
    

## **Notas relacionadas**

- [[10_Teoria_Base/10_02_Firewall_y_VLANs|Firewall y VLANs]]
    
- [[20_Diseño_Arquitectura/20_01_Arquitectura_Logica/20_01_03_Modelo_de_Segmentacion|Segmentación]]
    

---

# **3. Switch Gestionable L2/L3**

## **Contexto**

El switch gestionable es uno de los dispositivos menos entendidos por usuarios domésticos, pero en entornos profesionales es clave.

Un switch gestionable te permite:

- controlar cómo se mueve el tráfico
    
- decidir qué VLAN pasa por qué puerto
    
- duplicar tráfico para un IDS
    
- conectar múltiples dispositivos de forma ordenada
    

## **Por qué no sirve un switch barato**

Los switches “tontos” solo hacen una cosa: conectar cables.

Pero para un SIEM-HomeLab necesitamos:

- VLANs
    
- trunking
    
- routing interno
    
- port mirroring
    
- control de tabla MAC
    
- IGMP snooping
    

Sin esto, la arquitectura no se puede construir.

## **Rol en el SIEM-HomeLab**

El switch gestionable es el “sistema circulatorio” de la red:

- distribuye tráfico entre VLANs
    
- lleva varias VLANs hacia los APs
    
- conecta firewall, NAS y PCs
    
- permite ver tráfico en el IDS
    

## **Notas relacionadas**

- [[20_Diseño_Arquitectura/20_01_Arquitectura_Logica/20_01_04_Mapa_de_VLANs|Mapa de VLANs]]
    

---

# **4. Access Points (APs) Profesionales**

## **Contexto**

Un AP profesional transforma tu WiFi en una red empresarial:

- SSIDs separados
    
- VLANs separadas
    
- seguridad mejorada
    
- roaming estable
    

Los routers domésticos mezclan todo en una única red WiFi, lo cual es crítico si tienes IoT.

## **Rol en tu arquitectura**

Tus APs gestionarán:

- WiFi personal seguro
    
- WiFi IoT aislada
    
- WiFi para invitados
    
- WiFi para LAB si lo deseas
    

Esto es clave en un piso con domótica avanzada.

## **Notas relacionadas**

- [[20_Diseño_Arquitectura/20_06_Planificacion_Espacial_Piso|Ubicación WiFi]]
    

---

# **5. NAS (Network Attached Storage)**

## **Contexto**

El NAS no es solo “un disco duro en red”. Es un mini servidor.

En un SOC doméstico sirve como:

- repositorio de logs
    
- almacenamiento para snapshots
    
- hosting de contenedores
    
- destino de backups
    
- espacio para máquinas virtuales
    
- almacenamiento de seguridad a largo plazo
    

Las empresas usan NAS y cabinas SAN para funciones similares.

## **Rol en tu SIEM-HomeLab**

Tu NAS será uno de los pilares del proyecto:

- guardará evidencias
    
- almacenará logs del SIEM
    
- permitirá versionado
    
- será tu backup de configuraciones
    
- soportará contenedores auxiliares (si aplica)
    

## **Notas relacionadas**

- [[10_Teoria_Base/10_03_NAS_y_Almacenamiento|NAS y almacenamiento]]
    

---

# **6. Endpoints (PCs personales y laborales)**

## **Contexto**

Los endpoints son los dispositivos donde ocurre la actividad “humana”: navegación, documentos, juegos, descargas, actualizaciones, errores.

Toda actividad “normal” genera telemetría valiosa para un SOC.

Tener endpoints reales es una ventaja enorme sobre un entorno 100% virtualizado.

### **Tipos en tu caso**

- **PC de tu pareja** → comportamiento real no técnico
    
- **Tu PC personal** → comportamiento mixto
    
- **Laptop Kali** → herramienta de ataque y análisis
    

Cada uno produce logs distintos, ideales para correlaciones.

## **Notas relacionadas**

- [[10_Teoria_Base/10_07_Endpoints_OSQuery_Sysmon|Telemetría en endpoints]]
    

---

# **7. Dispositivos IoT**

## **Contexto**

Los dispositivos IoT son los más vulnerables de una red doméstica:

- actualizaciones tardías
    
- firmware cerrado
    
- protocolos inseguros
    
- exposición constante a Internet
    

Incluso empresas han sido comprometidas por IoT mal segmentado.

## **En tu arquitectura**

Los IoT deben estar siempre:

- en su propia VLAN
    
- con acceso saliente controlado
    
- sin acceso directo a LAN
    
- monitorizados por anomalías
    

## **Notas relacionadas**

- [[20_Diseño_Arquitectura/20_05_Rol_de_los_Dispositivos_Personales/20_05_04_Dispositivos_IoT_en_la_Arquitectura|IoT Aislado]]
    

---

# **8. Honeypots (Cowrie, Dionaea, Honeyd)**

## **Contexto**

Los honeypots permiten:

- registrar ataques reales
    
- recopilar muestras de malware
    
- crear reglas de detección
    
- observar comportamientos de atacantes
    

En un SOC real, se usan para inteligencia de amenazas.

## **En tu SIEM-HomeLab**

Tus honeypots estarán:

- en una VLAN completamente aislada
    
- expuestos sólo a Internet si lo deseas
    
- vigilados por Suricata
    
- conectados directamente a Wazuh
    

## **Notas relacionadas**

- [[10_Teoria_Base/10_08_Honeypots|Teoría de honeypots]]
    
- [[30_Implementacion/30_05_Despliegue_Honeypots|Despliegue práctico]]
    

---

# ⭐ ¿Siguiente paso?

Dime qué ampliamos ahora:

### **A) 10_01_02 — Direccionamiento IP**

### **B) 10_01_03 — Subredes y Máscaras**

### **C) 20_01 — Arquitectura lógica (muy buena continuación)**

### **D) un resumen visual de esta nota en Excalidraw**

Tú decides.