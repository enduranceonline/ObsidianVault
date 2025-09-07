#certificacion #network #apuntes
# 🧠 Capítulo 1: Network Models
# 🧩 Sesión 1: The OSI Model

---
### 📌 Resumen General

El modelo OSI (Open Systems Interconnection) es un estándar creado por la ISO para facilitar la interoperabilidad entre diferentes sistemas de red. Divide el proceso de comunicación en siete capas lógicas, cada una con funciones específicas y bien definidas. Este modelo ayuda a entender, diagnosticar y diseñar redes al separar tareas complejas en unidades manejables.

---

### 🧱 Las 7 Capas del Modelo OSI

#### 1️⃣ Capa 1 - Física (Physical Layer)
- **Función principal:** Transmitir bits (0s y 1s) a través de medios físicos.
	- Define los **medios físicos** por los que se transmiten los datos: cobre, fibra óptica, aire (inalámbrico).
	- Especifica **requisitos eléctricos y físicos** del hardware.
	- Convierte datos digitales en **señales** (eléctricas, ópticas, radio).
	- Describe la **topología física** (estrella, bus, anillo, malla...).
	- Aplica técnicas de **modulación** para la transmisión.
	- Se encarga de la **encapsulación** inicial y oculta la complejidad del hardware.
	- Representa el **nivel más bajo** del modelo.
- **Responsabilidades:**
  - Señales eléctricas, ópticas o de radio.
  - Tipo de cables y conectores (cobre, fibra óptica, etc.).
  - Voltajes, pines, sincronización.
- **Ejemplos:** Cables Ethernet, conectores RJ-45, repetidores, hubs, Wi-Fi (en su forma más básica).

#### 2️⃣ Capa 2 - Enlace de Datos (Data Link Layer)
- **Función principal:** Transferencia fiable de datos entre dos nodos conectados directamente.
	- Garantiza la **transmisión confiable** de tramas a través del medio físico.
	- Agrupa los bits en **tramas de datos**.
	- Utiliza **direcciones MAC** para identificar dispositivos en una LAN.
	- **Codifica y decodifica** tramas.
	- Encapsula paquetes de nivel superior (capa 3).
	- Divide paquetes grandes en tramas más pequeñas.
- **Responsabilidades:**
  - Direccionamiento físico mediante direcciones MAC.
  - Detección y posible corrección de errores a nivel de enlace.
  - Control de flujo entre nodos.
- **Ejemplos:** Switches, bridges, tramas Ethernet, protocolos ARP y PPP.

#### 3️⃣ Capa 3 - Red (Network Layer)
- **Función principal:** Determinar la ruta y direccionamiento lógico de los datos.
	- Determina la **mejor ruta** para los paquetes entre redes.
	- Utiliza **direcciones IP** y tablas de enrutamiento.
	- Soporta **multiplexación** de múltiples conexiones.
	- Permite **broadcast y multicast**.
	- Se encarga de la **subnetting** o división de redes.
- **Responsabilidades:**
  - Uso de direcciones IP.
  - Enrutamiento entre redes diferentes.
  - Fragmentación de paquetes si es necesario.
- **Ejemplos:** Routers, protocolos IP, ICMP, OSPF, BGP.

#### 4️⃣ Capa 4 - Transporte (Transport Layer)
- **Función principal:** Asegurar la entrega completa y correcta de datos entre hosts.
		
| TCP (Protocolo de Control de Transmisión) | UDP (Protocolo de Datagrama de Usuario) |
| ----------------------------------------- | --------------------------------------- |
| Orientado a conexión                      | No orientado a conexión                 |
| Control de errores y entrega secuencial   | Sin control de errores ni orden         |
| Acuses de recibo (ACK, NACK)              | Sin acuses de recibo                    |
| Mayor sobrecarga                          | Baja latencia                           |

		TCP usa el **handshake de 3 vías**.
		UDP ideal para **streaming**, VoIP, DNS.
- **Responsabilidades:**
	  - Segmentación y reensamblaje de datos.
	  - Control de errores extremo a extremo.
	  - Control de flujo.
- **Ejemplos:** TCP (confiable, orientado a conexión), UDP (rápido, no confiable).

#### 5️⃣ Capa 5 - Sesión (Session Layer)
- **Función principal:** Establecer, mantener y finalizar sesiones de comunicación.
	- Inicia, **mantiene y finaliza** sesiones entre aplicaciones.
	- **Sincroniza** y organiza el intercambio de datos.
	- Controla la **concurrencia** entre procesos simultáneos.
	- Usa **tokens** para administrar las sesiones.
- **Responsabilidades:**
  - Manejo de sesiones múltiples (como varias pestañas en un navegador).
  - Sincronización de diálogo entre aplicaciones.
- **Ejemplos:** Sesiones SMB, RPC, NetBIOS.

#### 6️⃣ Capa 6 - Presentación (Presentation Layer)
- **Función principal:** Traducir y dar formato a los datos para que la capa de aplicación los entienda.
	-  Convierte los datos a un **formato comprensible** para la aplicación.
	- Aplica **compresión y cifrado**.
	- Reduce tamaño para mejorar el rendimiento.
	- Verifica **autenticación y autorización**.
	- Protocolos relevantes:
	  - **MIME**
	  - **HTML**
- **Responsabilidades:**
  - Codificación y decodificación (ej. ASCII vs UTF-8).
  - Compresión y descompresión.
  - Cifrado y descifrado.
- **Ejemplos:** SSL/TLS, JPEG, MP3, formatos de archivo como PDF, DOCX.

#### 7️⃣ Capa 7 - Aplicación (Application Layer)
- **Función principal:** Proporcionar servicios de red directamente al usuario final o a la aplicación.
	- Interactúa con el usuario mediante **interfaces gráficas o CLI**.
	- Proporciona una **arquitectura cliente-servidor**.
	- Traduce los datos para su interpretación.
	- Establece sesiones y permite **acceso a archivos remotos**.
	- Protocolos típicos:
	  - **HTTP, FTP, SSH, SMTP, DNS, DHCP, LDAP**
- **Responsabilidades:**
  - Protocolos que permiten interacción directa con el software del usuario.
  - Proporciona interfaces (APIs) para el uso de red en aplicaciones.
- **Ejemplos:** HTTP, FTP, SMTP, DNS, Telnet, aplicaciones como navegadores o clientes de correo.

---

### 🧠 Consejos para el examen CompTIA Network+
- Comprender la **función práctica de cada capa** más allá de solo memorizarlas.
- Capas más frecuentemente mencionadas en problemas: **capa 3 (IP)** y **capa 4 (TCP/UDP)**.
- Pensar en términos de "¿en qué capa se rompe algo?" ayuda a diagnosticar problemas.
- No se espera que memorices la estructura completa de una trama Ethernet, pero sí entender su propósito.

---

### 📷
![[osi-model-diagram.png]]

---

### 🧰 Aplicación práctica del modelo OSI
- **Diagnóstico de red:** Saber en qué capa está fallando una conexión (ej. sin señal = capa 1, IP incorrecta = capa 3).
- **Seguridad:** Un ataque DoS puede detectarse en capa 3 o capa 4; el cifrado ocurre en capa 6 o 7.
- **Diseño:** Permite desarrollar dispositivos y software que operen en capas independientes y compatibles.

---

### 📝 Mnemotecnia para recordar las capas (de capa 7 a capa 1)
**"All People Seem To Need Data Processing"**
- Application
- Presentation
- Session
- Transport
- Network
- Data Link
- Physical

# 🧩 Sesión 2: Meet the Frame

---

### 📌 Resumen General

La creación de redes modernas es extremadamente compleja, pero esa complejidad es lo que hace posible la comodidad y conectividad actuales. Para poder entender los fundamentos, es útil retroceder a configuraciones básicas como una red de área local (LAN) simple, compuesta por ordenadores, tarjetas de red y un concentrador (hub).

---

### 💡 Conceptos Clave

#### 🔌 Red Local Básica
- **NIC (Network Interface Card):** Tarjeta que conecta un equipo a la red.
- **Hub:** Dispositivo que conecta varios ordenadores para que compartan recursos.
- **Recursos compartidos:** Archivos, juegos, servicios, etc., accesibles entre dispositivos de la red local.

#### 🧱 ¿Cómo se mueven los datos?
- Los datos **no** se transmiten como un flujo continuo.
- Se envían en **fragmentos discretos** llamados **tramas** (frames).
- Este modelo de datos empaquetados permite control, segmentación y eficiencia.

---

### 📦 ¿Qué es una trama (frame)?

Una **trama** es una unidad de datos estructurada que se transmite por una red. Contiene tanto la **información útil** (payload) como **datos de control** (como direcciones, comprobación de errores, etc.).

- **Tamaño máximo:** 1500 bytes (es decir, unos 12.000 bits aprox.).
- **Transmisión:** Las tramas se generan en la NIC y se consumen también por la NIC.
- **Formato físico:** Aunque no veamos los bits, el hardware interpreta los unos y ceros que representan las tramas.

![[Frame.svg]]

---

### 🧰 Datos empaquetados

Este es el **principio fundamental del networking moderno**:

> 🔐 "Toda la comunicación en red se basa en el envío y recepción de tramas (paquetes de datos estructurados)."

Los datos se "empaquetan" para:
- Facilitar su envío y recepción.
- Detectar errores.
- Asegurar el orden y la estructura.

---

### 🧪 Analogía del marco con bloques
- Cada bloque representa una trama.
- Una aplicación como Word genera datos → bajan a la NIC → se encapsulan en una trama.
- La NIC lanza la trama a la red.
- Otra NIC la recibe, la procesa y entrega los datos a la aplicación correspondiente.

---

### 📝 Conclusión

Entender que los datos viajan en tramas discretas es esencial para comprender cómo funciona una red. Este modelo permite segmentar, identificar, direccionar y asegurar la información, sentando las bases para protocolos más complejos como Ethernet, TCP/IP, y más.

## 🧩 Sesión 3: The MAC Address

---

### 📌 Resumen General

Las tramas son esenciales para transmitir datos en redes, pero por sí solas no tienen forma de saber a qué dispositivo deben llegar. Por eso, cada tarjeta de red necesita un identificador único: la dirección MAC. Esta dirección permite identificar de forma inequívoca cada dispositivo dentro de una red local.

---

### 🖧 ¿Qué ocurre en una red con un concentrador (hub)?

- Un **hub** es un dispositivo que actúa como **repetidor**: copia cualquier señal que recibe y la envía a todos los demás puertos.
- Esto provoca que **todas las máquinas reciban todas las tramas**, aunque solo una sea la destinataria.
- Por tanto, **cada trama necesita una dirección** que indique quién debe procesarla.

---

### 🧭 Dirección MAC

#### ¿Qué es?
- **MAC (Media Access Control)**: Dirección física única grabada en cada tarjeta de red (NIC).
- **Formato:** 48 bits representados en 6 pares hexadecimales (ej. `00:1A:2B:3C:4D:5E`).
- **Dos partes:**
  - **OUI (Organizationally Unique Identifier):** Los primeros 3 pares identifican al fabricante (ej. Intel).
  - **ID del dispositivo:** Los últimos 3 pares son únicos para cada tarjeta.

#### ¿Para qué sirve?
- Indica si una trama está dirigida a una tarjeta concreta.
- Permite la **comunicación entre dispositivos locales**.
- Se usa para direccionar **tramas Ethernet**.

---

### 🧪 Visualización práctica

> Analiza la red como si las tramas fueran cartas y la dirección MAC fuera la dirección postal del destinatario.

- Cada tarjeta de red tiene una "bandeja de entrada".
- Cuando llega una trama, la tarjeta revisa la **MAC de destino**.
  - Si coincide, **acepta** la trama y la pasa al sistema.
  - Si no coincide, **descarta** la trama.
- Además, cada trama incluye la **MAC de origen**, para que se pueda responder.

---

### ⚙️ ¿Cómo ver tu dirección MAC en Windows?

Abre **PowerShell** o el **Símbolo del sistema** y ejecuta:

```bash
ipconfig /all
```

Busca tu adaptador de red activo (normalmente "Ethernet" o "Wi-Fi") y localiza la línea:

```
Dirección física . . . . . . . . . . . : 00-1A-2B-3C-4D-5E
```

---

### 📦 Contenido típico de una trama Ethernet

- **MAC de destino**
- **MAC de origen**
- **Datos**
- **CRC (Cyclic Redundancy Check):** Verifica integridad del mensaje

---

### 📝 Conclusión

Las direcciones MAC son fundamentales para que los dispositivos identifiquen si una trama les pertenece. Aunque los hubs envían tramas a todos, solo las tarjetas con la dirección MAC correcta responderán. Este principio es el primer paso hacia una red direccionable y eficiente.

# 🧩 Sesión 3: The MAC Address

---

### 📌 Resumen General

Las tramas son esenciales para transmitir datos en redes, pero por sí solas no tienen forma de saber a qué dispositivo deben llegar. Por eso, cada tarjeta de red necesita un identificador único: la dirección MAC. Esta dirección permite identificar de forma inequívoca cada dispositivo dentro de una red local.

---

### 🖧 ¿Qué ocurre en una red con un concentrador (hub)?

- Un **hub** es un dispositivo que actúa como **repetidor**: copia cualquier señal que recibe y la envía a todos los demás puertos.
- Esto provoca que **todas las máquinas reciban todas las tramas**, aunque solo una sea la destinataria.
- Por tanto, **cada trama necesita una dirección** que indique quién debe procesarla.

---

### 🧭 Dirección MAC

#### ¿Qué es?
- **MAC (Media Access Control)**: Dirección física única grabada en cada tarjeta de red (NIC).
- **Formato:** 48 bits representados en 6 pares hexadecimales (ej. `00:1A:2B:3C:4D:5E`).
- **Dos partes:**
  - **OUI (Organizationally Unique Identifier):** Los primeros 3 pares identifican al fabricante (ej. Intel).
  - **ID del dispositivo:** Los últimos 3 pares son únicos para cada tarjeta.

#### ¿Para qué sirve?
- Indica si una trama está dirigida a una tarjeta concreta.
- Permite la **comunicación entre dispositivos locales**.
- Se usa para direccionar **tramas Ethernet**.

---

### 🧪 Visualización práctica

> Analiza la red como si las tramas fueran cartas y la dirección MAC fuera la dirección postal del destinatario.

- Cada tarjeta de red tiene una "bandeja de entrada".
- Cuando llega una trama, la tarjeta revisa la **MAC de destino**.
  - Si coincide, **acepta** la trama y la pasa al sistema.
  - Si no coincide, **descarta** la trama.
- Además, cada trama incluye la **MAC de origen**, para que se pueda responder.

---

### ⚙️ ¿Cómo ver tu dirección MAC en Windows?

Abre **PowerShell** o el **Símbolo del sistema** y ejecuta:

```bash
ipconfig /all
```

Busca tu adaptador de red activo (normalmente "Ethernet" o "Wi-Fi") y localiza la línea:

```
Dirección física . . . . . . . . . . . : 00-1A-2B-3C-4D-5E
```

---

### 📦 Contenido típico de una trama Ethernet

- **MAC de destino**
- **MAC de origen**
- **Datos**
- **CRC (Cyclic Redundancy Check):** Verifica integridad del mensaje

---

### 🖼️ Diagramas 

![[ethernet-mac-address-diagram.png]]
![[hub-broadcasting.png]]

---

### 📝 Conclusión

Las direcciones MAC son fundamentales para que los dispositivos identifiquen si una trama les pertenece. Aunque los hubs envían tramas a todos, solo las tarjetas con la dirección MAC correcta responderán. Este principio es el primer paso hacia una red direccionable y eficiente.

# 🧩 Sesión 4: Understanding Ports and Services

---

### 📌 Resumen General

Los **números de puerto** son identificadores esenciales en redes TCP/IP. Junto con las direcciones IP, permiten dirigir los datos entrantes hacia la **aplicación o servicio correcto** dentro de un dispositivo. Están definidos en la **capa de transporte** del modelo OSI.

---

### 🔢 ¿Qué es un puerto?

- Es un **valor numérico de 16 bits sin signo**, con rango de 0 a 65535.
- Permite **distinguir entre múltiples servicios** que operan en una misma máquina.
- Cada puerto está vinculado a un servicio o aplicación específica.

---

### 🧩 Tipos de puertos

| Rango         | Tipo de Puerto       | Uso                                               |
|---------------|----------------------|----------------------------------------------------|
| 0 - 1023      | Puertos conocidos    | Reservados para servicios estándar (HTTP, DNS...) |
| 1024 - 49151  | Puertos registrados  | Aplicaciones de usuario, asignados por IANA       |
| 49152 - 65535 | Puertos dinámicos    | Usados temporalmente para conexiones salientes    |

- **IANA (Internet Assigned Numbers Authority)** gestiona la asignación oficial.

---

### 💡 Analogía: Apartamentos y buzones

Imagina un edificio:
- La **dirección IP** es la dirección del edificio.
- El **número de puerto** es el número del apartamento.
- Cada "apartamento" (puerto) tiene un **buzón (listener)** esperando datos.
- Cuando llega el "correo" (paquete), se entrega al buzón (servicio) correspondiente.

---

### 🔐 Puertos y protocolos comunes para el examen

| Servicio         | Protocolo | Puerto(s) |
|------------------|-----------|-----------|
| FTP (datos)      | TCP       | 20        |
| FTP (control)    | TCP       | 21        |
| SSH              | TCP       | 22        |
| Telnet           | TCP       | 23        |
| DNS              | TCP/UDP   | 53        |
| HTTP             | TCP       | 80        |
| HTTPS            | TCP       | 443       |

- ⚠️ Estos puertos son **muy preguntados** en el examen CompTIA Network+.
- Otros puertos también pueden aparecer, así que **no memorices solo estos**.

---

### 🔄 Puertos y conexiones

- Los **puertos de origen** son frecuentemente **dinámicos o efímeros**.
- Los **puertos de destino** suelen ser **conocidos y estandarizados** (ej. 80 para HTTP).

#### 📌 Ejemplo
```
Cliente: IP 192.168.1.20:52678 → Servidor: IP 93.184.216.34:80
```
- Puerto 52678: dinámico asignado por el cliente.
- Puerto 80: HTTP en el servidor.

---

### 🛡️ Seguridad y puertos

- La identificación de puertos permite configurar **firewalls, NATs y sistemas IDS/IPS**.
- La segmentación de servicios mediante puertos mejora la capacidad de **auditoría y monitorización**.

---

### 🖼️ Imágenes sugeridas

```
![[port-explanation-diagram.png]]
![[tcp-udp-ports-table.jpg]]
```

---

### 📝 Conclusión

Los puertos son elementos fundamentales para el direccionamiento interno de los servicios de red. Comprender qué puertos utiliza cada protocolo te permitirá identificar tráfico, diagnosticar problemas, configurar firewalls y aprobar el examen CompTIA Network+ con mayor seguridad.

# 🧩 Sesión 5: Internet Protocol (IP) Types

---

### 📌 Resumen General

En esta sesión se analizan diversos **protocolos TCP/IP clave** en redes modernas, especialmente en lo que respecta a la **entrega, fiabilidad y seguridad de los datos**. Se abordan principalmente los protocolos de **capa de transporte** (TCP/UDP), los de **capa de red** (IP, ICMP) y los de **seguridad** (IPsec).

---

### 🚚 Protocolos de Capa de Transporte

#### 🔁 TCP (Transmission Control Protocol)
- **Orientado a conexión**: Establece conexión antes de transferir datos.
- **Handshake de 3 vías**: SYN → SYN/ACK → ACK.
- **Fiable**: Verifica entrega, reenvía si es necesario.
- **Secuencia de datos**: Numera los paquetes para reensamblarlos en orden.
- **Usos típicos**: HTTP, FTP, SMTP.

#### 💨 UDP (User Datagram Protocol)
- **Sin conexión**: No garantiza entrega.
- **Baja latencia**: Rápido, sin control de errores ni secuenciación.
- **Usos típicos**: VoIP, DNS, streaming multimedia, videojuegos.

---

### 🌐 Protocolos de Capa de Red

#### 🧭 IP (Internet Protocol)
- Encargado del **direccionamiento lógico** y **enrutamiento** de paquetes.
- Funciona con TCP/UDP para entregar datos al destino correcto.
- Comparación:
  - IP = dirección postal
  - TCP = cartero que garantiza entrega

#### 🔍 ICMP (Internet Control Message Protocol)
- **Protocolo sin conexión** para diagnóstico y señalización.
- Usado por herramientas como `ping`, `traceroute`.
- Envía mensajes de eco, errores y tiempo excedido.

---

### 🔐 Seguridad: IPsec (Internet Protocol Security)

- **Conjunto de protocolos** para seguridad a nivel de red (capa 3).
- Usado en **VPNs** y redes seguras.

#### Componentes:
| Protocolo | Función |
|-----------|---------|
| AH (Authentication Header) | Autentica y garantiza integridad del paquete IP (sin cifrar carga útil) |
| ESP (Encapsulating Security Payload) | Cifra la carga útil y proporciona autenticación |
| IKE (Internet Key Exchange) | Negocia claves y establece asociaciones de seguridad (SAs) |

#### 🔒 Asociación de Seguridad (SA):
- Acuerdo entre dos sistemas sobre cómo cifrar y autenticar datos.
- Incluye algoritmos de cifrado, claves y duración del túnel.

#### Modos de funcionamiento:
| Modo         | Descripción |
|--------------|-------------|
| **Túnel**    | Cifra el paquete completo (incluye cabecera IP original). Usado entre gateways. |
| **Transporte** | Cifra solo la carga útil, no la cabecera. Usado entre hosts. |

---

### 📝 Conceptos Clave para el Examen

- TCP garantiza **entrega ordenada y fiable** → mayor latencia.
- UDP es **rápido y sin control** → ideal para tiempo real.
- IPsec combina **cifrado, autenticación y gestión de claves**.
- Saber **cuándo y por qué se usan** estos protocolos es esencial para diagnóstico y diseño de redes seguras.

---

### 🖼️ Imágenes sugeridas

```
![[tcp-handshake-diagram.png]]
![[ipsec-tunnel-vs-transport.png]]
```

---

### ✅ Conclusión

Los protocolos de red son la base del funcionamiento de Internet y de redes privadas. Conocer sus diferencias y aplicaciones permite **diseñar redes robustas, resolver problemas de conectividad y aplicar medidas de seguridad efectivas**.


# 📝 Capítulo 1: Cuestionario 1 - Network Models Quiz

---

### ✅ Pregunta 1
**¿En qué capa del modelo OSI operan los routers?**

- [ ] Capa 1  
- [ ] Capa 2  
- [x] Capa 3  
- [ ] Capa 4  

**Explicación:**  
Los routers operan en la **Capa 3 (Red)** del modelo OSI. Se encargan del direccionamiento lógico mediante direcciones IP y permiten el enrutamiento entre redes diferentes.

---

### ✅ Pregunta 2
**¿Cuántos bytes puede contener una trama Ethernet?**

- [x] Aproximadamente 1500 bytes  
- [ ] 512 bytes  
- [ ] 2048 bytes  
- [ ] 65535 bytes  

**Explicación:**  
Una trama Ethernet estándar puede contener hasta **1514 bytes**, de los cuales **1500** corresponden al campo de datos, lo que da lugar a esta aproximación habitual.

---

### ✅ Pregunta 3
**¿Cuál de las siguientes es una dirección MAC válida?**

- [ ] GG:00:45:ZC:00:4F  
- [x] 0A:24:D3:00:00:FF  
- [ ] Z0:4F:9H:6F:22:00  
- [ ] 99:00:FF:FF:FH:11  

**Explicación:**  
Las direcciones MAC se componen de **valores hexadecimales** (0-9 y A-F) y siguen el formato `XX:XX:XX:XX:XX:XX`. La única opción válida en este caso es `0A:24:D3:00:00:FF`.

---

### ✅ Pregunta 4
**¿Cuál de los siguientes NO es un grupo definido por la IANA para la asignación de puertos TCP/UDP?**

- [ ] Dinámico (Privado o Efímero)  
- [ ] Registrado  
- [x] No asignado  
- [ ] Bien conocidos (System)  

**Explicación:**  
La IANA define tres grupos: **Bien conocidos (0–1023)**, **Registrados (1024–49151)** y **Dinámicos o efímeros (49152–65535)**. No existe una categoría oficial llamada "No asignado", aunque algunos puertos no estén en uso.

---

### ✅ Pregunta 5
**¿Qué protocolo TCP/IP está orientado a la conexión y utiliza un "handshake" de tres vías para establecer la conexión?**

- [ ] ICMP  
- [ ] IP  
- [x] TCP  
- [ ] UCP  

**Explicación:**  
**TCP (Transmission Control Protocol)** es un protocolo orientado a la conexión que utiliza un **"three-way handshake"** (SYN → SYN/ACK → ACK) para establecer una conexión antes de enviar datos de forma fiable.

---

### ➕ Preguntas adicionales sugeridas

#### Pregunta 6
**¿Qué protocolo se utiliza comúnmente para el streaming en tiempo real y no garantiza entrega?**

- [ ] TCP  
- [x] UDP  
- [ ] ICMP  
- [ ] HTTP  

**Explicación:**  
**UDP** es ideal para transmisión en tiempo real (VoIP, juegos, video), ya que no requiere confirmación de recepción ni secuencia de paquetes, lo que permite baja latencia.

#### Pregunta 7
**¿Qué protocolo permite verificar conectividad entre dos dispositivos usando mensajes de eco?**

- [ ] TCP  
- [ ] FTP  
- [x] ICMP  
- [ ] ARP  

**Explicación:**  
**ICMP (Internet Control Message Protocol)** es usado por herramientas como `ping` y `traceroute` para enviar solicitudes de eco y respuestas.

---

