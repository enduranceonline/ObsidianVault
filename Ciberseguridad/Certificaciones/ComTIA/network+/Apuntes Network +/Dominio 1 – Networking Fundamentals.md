#apuntes #certificacion #redes
## 1.1 OSI Model

### Introducción

- El **modelo OSI (Open Systems Interconnection)** es un **modelo de referencia** creado para describir cómo viaja la información a través de una red.
    
- No es un protocolo, sino un marco conceptual que ayuda a los profesionales de IT a:
    
    - **Estandarizar la comunicación** sobre problemas de red.
        
    - **Dividir las funciones de red** en capas lógicas.
        
    - **Simplificar el troubleshooting** (ejemplo: “problema en Capa 3”).
        

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
- **Ejemplos:** 
	- TCP (confiable, orientado a conexión)
	- UDP (rápido, no confiable).

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

### Nemotecnia

Para recordar las capas:

- **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing  
    (Application, Presentation, Session, Transport, Network, Data Link, Physical)

---

### Ejemplo práctico: análisis en Wireshark

- **Capa 1:** tamaño en bytes de la trama.
- **Capa 2:** direcciones MAC origen/destino.
- **Capa 3:** direcciones IP.
- **Capa 4:** protocolo TCP o UDP con puertos asociados.
- **Capas 5-7:** visibles si no hay cifrado (ej. HTTP). Con TLS, quedan encapsuladas.

---

### Diferencia OSI vs TCP/IP

- El modelo **TCP/IP** es más práctico y usado en la realidad.
    
- Tiene solo **4 capas**:
    
    - Aplicación
        
    - Transporte
        
    - Internet
        
    - Acceso a la red
        
- OSI es principalmente un marco de estudio y referencia.
    

---

### Nota de examen 📌

- CompTIA suele preguntar **qué capa está involucrada** en un fallo:
    
    - Capa 1 → cable roto.
        
    - Capa 2 → switch no reenvía tráfico.
        
    - Capa 3 → error en IP/gateway.
        
    - Capa 4 → puertos bloqueados.
        
    - Capa 7 → fallo en la aplicación (ej. web no carga, pero ping funciona).
        

---

✅ Con esto tienes la **Sección 1.1 reescrita en versión completa**.

¿Quieres que siga con la **1.2 – Network Devices** en este mismo estilo detallado?