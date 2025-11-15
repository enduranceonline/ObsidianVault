#ciscopackettracer #network 

---

👨‍🏫  Profesor: Carlos Quintana
📘 Unidad: Ciberseguridad  
🗓 Clase 3— 30/10/2025
🎯 Tema: Estudio de redes inhalámbricas a través de Cisco Packet Tracer y Seguridad Wifi IoT

---

# 📘 Redes inalámbricas + IoT + AAA/DHCP

---

## 1️⃣ Objetivo

Simular una red doméstica/empresarial con dispositivos IoT conectados por WiFi y preparar la base para añadir seguridad vía servidor AAA/DHCP.

---

## 2️⃣ Componentes del escenario

El montaje reproduce una red híbrida típica: parte inalámbrica para usuarios y dispositivos IoT, y parte cableada para servicios centrales. Los elementos son:

- **WRT300N Wireless Router**  
    Punto de acceso principal de la red WiFi.
    
    - SSID: `jueves`
        
    - IP LAN: `192.168.1.1/24`
        
- **Laptop-PT (x2)**  
    Dispositivos cliente conectados vía WiFi. Sirven para probar la autenticación AAA y la gestión centralizada.
    
- **Dispositivos IoT**  
    Actuadores y sensores controlados desde el servidor IoT:
    
    - Garage Door (IoT0)
        
    - Window (IoT1)
        
    - Webcam (IoT2)
        
    - Door (IoT3)
        
    - RFID Card (IoT4)
        
    - RFID Reader (IoT5)
        
- **Switch Cisco 2960-24TT**  
    Elemento central de la red cableada. Une servidor y router, permitiendo que el servidor controle toda la red.
    
- **Server-PT (renombrado a “AAA-DHCP”)**  
    Servidor con funciones críticas:
    
    - **AAA** (RADIUS) → autenticación individual de usuarios WiFi
        
    - **DHCP** → servidor de asignación de IPs

Con este conjunto podemos simular una infraestructura completa con seguridad, red cableada y automatización IoT.

![[Pasted image 20251111105507.png]]

---

### 🔍 Observación — Conexiones iniciales y tipo de cable

Antes de configurar nada, es fundamental cablear correctamente los elementos cableados:

#### 1️⃣ Conectar el servidor al switch

Se usa:

- **Cable Copper Straight-Through (cobre directo)**  
    Icono: cable azul con conectores rectos.

Usos del cable directo:

- conectar **dispositivo final → switch**
    
- conectar **router → switch**

![[Pasted image 20251111133735.png]]

En la imagen se ve cómo se selecciona el puerto **FastEthernet0** del servidor y se conecta a cualquiera de los puertos **FastEthernet0/x** del switch.

> Los puertos FASTETHERNET del switch aparecen en una lista (1–24). Se puede usar cualquiera.

#### 2️⃣ Conectar el switch al router

Se repite el mismo tipo de cable:

- **Copper Straight-Through**

![[Pasted image 20251111133606.png]]

En el router WRT300N, se selecciona el puerto **Ethernet 1** (no el puerto “Internet”, que simula conexión WAN externa).

> “Internet” es WAN. “Ethernet 1/2/3/4” son LAN.  
> Usamos Ethernet 1 para integrarlo en la LAN.

![[Pasted image 20251111133644.png]]

De esta forma se completa el backbone cableado:

`Server  →  Switch  →  Router/AP`

---

### 📌 Dónde se encuentran los componentes en Packet Tracer

- **Router WRT300N**  
    Menú inferior → categoría **Routers** → subcategoría **Wireless Devices**.
    
- **Switch 2960-24TT**  
    Menú inferior → categoría **Switches**.
    
- **Server-PT**  
    Menú inferior → categoría **End Devices**.
    
- **Laptop-PT**  
    Menú inferior → categoría **End Devices**.
    
- **Dispositivos IoT**  
    Menú inferior → categoría **IoT Devices**.
    
- **Cable Copper Straight-Through**  
    Barra inferior → icono del cable azul → “Copper  Straight-Through”.

---
## 3️⃣ Configuración del router WRT300N

El router WRT300N es el **punto de acceso inalámbrico** de toda la red. Su función principal en este escenario es ofrecer conectividad WiFi a los portátiles y a los dispositivos IoT. Más adelante lo integraremos con el servidor AAA para que delegue la autenticación, pero inicialmente se configura en modo básico para asegurar conectividad.

---

### 🔹 Wireless

- **SSID:** `jueves`  
    Se define el nombre de la red WiFi a la que se conectarán los dispositivos.  
    El SSID debe escribirse **exactamente igual** en los portátiles y en los dispositivos IoT.
    
- **Seguridad desactivada (por ahora)**  
    El router usa la configuración por defecto sin cifrado WPA/WPA2.  
    Esto se hace a propósito para verificar que los dispositivos pueden asociarse antes de activar la seguridad avanzada basada en RADIUS.
    
- **Router actuando como punto de acceso**  
    El WRT300N no está configurado como servidor DHCP ni como router completo hacia Internet.  
    Solo estamos usando su interfaz inalámbrica para distribuir señal WiFi.

![[Pasted image 20251111105741.png]]

Esto facilita que los dispositivos se conecten sin restricciones iniciales y permite comprobar cobertura y conexión básica antes de introducir AAA y RADIUS.

---

### 🔹 LAN

En la pestaña LAN se configura la parte interna del dispositivo:

- **Modificar IP LAN:**
    
    - Antes: `192.168.1.0` (incorrecto como IP de host)
        
    - Después: `192.168.1.1` (IP válida del router dentro de la red local)
        
- **Máscara de subred:** `/24`  
    Es decir, `255.255.255.0`.

![[Pasted image 20251111105858.png]]

Esto define la red local:

`Red: 192.168.1.0/24 Router: 192.168.1.1`

El router se convierte así en el **gateway** que utilizarán:

- el servidor
    
- los portátiles
    
- los dispositivos IoT

---

### 💡 Observación técnica

En Packet Tracer hay que entender dos puntos clave:

1. **El router no es el servidor DHCP en este escenario.**  
    Aunque podría serlo, lo desactivaremos para  que el servidor “AAA-DHCP” sea el único que entregue IPs.
    
2. **El router solo actúa como AP inalámbrico.**  
    Esto replica un entorno corporativo donde:
    
    - los AP proporcionan cobertura
        
    - los servidores centrales gestionan autenticación y DHCP

---

## 4️⃣ Configuración de los portátiles para conectarse a la WiFi

Los portátiles vienen por defecto con un módulo Ethernet, por lo que primero hay que habilitarlos para conexión inalámbrica. Este proceso imita el reemplazo físico de un adaptador de red.

### Paso físico (pestaña **Physical**)

1. Apagar el laptop con el botón verde del lateral.
    
2. Retirar el módulo de red Ethernet existente.
    
3. Insertar el módulo **wireless WPC300N**, que le permite conectarse a redes WiFi.
    
4. Encender de nuevo el equipo.

Esto prepara al portátil para poder detectar y asociarse al SSID creado en el router.

![[Pasted image 20251111110036.png]]

---

![[Pasted image 20251111105928.png]]

---

![[Pasted image 20251111110100.png]]

---

![[Pasted image 20251111110139.png]]

---

### Paso lógico (pestaña **Config**)

- Entrar en **Wireless0**.
    
- Introducir el **SSID: `jueves`** para vincularse a la red inalámbrica del router.

✅ Una vez configurado, al iniciar la simulación con el botón **Play**, el portátil se conecta automáticamente al punto de acceso.
  ![[Pasted image 20251111110202.png]]

---

## 5️⃣ Configuración de dispositivos IoT por WiFi

Cada dispositivo IoT debe asociarse manualmente a la red inalámbrica para que pueda comunicarse con el router y, posteriormente, con el servidor.

### Pestaña **Config**

- Renombrar en **Display Name** según su función:  
    “ventana”, “garaje”, “puerta”, “camara”, etc.  
    (Esto facilita su identificación dentro del servidor IoT).
    
- En **Wireless0**:
    
    - **SSID:** `jueves`

Guardar los cambios para aplicar la configuración.

Una vez configurados, los dispositivos aparecerán conectados al router mediante líneas punteadas, indicando que se han unido a la red WiFi de forma inalámbrica.

---

## 6️⃣ Conexión del servidor y switch

Para integrar el servidor en la red cableada y permitir que actúe como punto central de autenticación y distribución de IPs, se realiza el cableado básico:

- Cable **cobre directo** entre:
    
    - **Server0 → FastEthernet0**
        
    - **Switch0 → cualquier puerto FastEthernet**
        
- Del **switch al router**:
    
    - Switch0 → Ethernet 1 del router

Esta topología es estándar: el switch actúa como distribuidor central y el router como salida de red inalámbrica. El servidor queda accesible desde todos los dispositivos a través del switch.

El servidor se renombra a **AAA-DHCP**, indicando claramente sus funciones:

- **AAA**: servidor de autenticación, autorización y accounting (RADIUS).
    
- **DHCP**: servidor encargado de entregar direcciones IP a toda la red local.

Con esta configuración, el servidor queda en el centro lógico de la red y preparado para gestionar seguridad y direcciones IP.
  
![[Pasted image 20251111110337.png]]

---

## 7️⃣ Estado actual de la red

- Todos los elementos están conectados al SSID “jueves”.
    
- El switch y servidor ya quedan integrados en la topología.
    
- No hay seguridad en la WiFi.
    
- No hay AAA ni DHCP aún configurados.
    
- La red funciona pero está **abierta y vulnerable**.

---

# 📘 Seguridad WiFi + AAA + DHCP + IoT + RFID en Cisco Packet Tracer

El objetivo práctico de esta sesión es simular una red inalámbrica realista que integra **seguridad empresarial**, **gestión centralizada de usuarios**, **distribución IP controlada** y **automatización IoT basada en condiciones**. La idea es entender cómo una organización evita accesos no autorizados, monitoriza dispositivos conectados y aplica lógica automática según eventos (por ejemplo, una tarjeta RFID válida).

Todo el proceso replica de forma simplificada lo que se usa en empresas para controlar accesos físicos, activar sistemas inteligentes, registrar actividad y mantener un control centralizado de la red.

Antes de añadir seguridad, ya habíamos montado una red inalámbrica funcional. Todos los dispositivos podían conectarse al SSID “jueves” sin control de acceso, lo que equivalía a una red doméstica abierta y vulnerable. En este punto el profesor introduce el concepto de **AAA (Authentication, Authorization, Accounting)**, que es el modelo real que utilizan las empresas para controlar quién se conecta a la WiFi y bajo qué credenciales.

Vimos cómo el **Server-PT** se configura para actuar como servidor AAA —es decir, como la “base de datos de usuarios” que autoriza o deniega el acceso a la WiFi—. Al asignarle una IP estática dentro de la red (`192.168.1.2`) lo fijamos como un recurso permanente, accesible tanto por el router como por los clientes.

![[Pasted image 20251111124840.png]]
### Esto introduce dos ideas fundamentales:

- El **router deja de autenticar por sí mismo**, pasa a delegar en el servidor.
    
- Los **usuarios se gestionan de forma centralizada** en la pestaña Services → AAA.

![[Pasted image 20251111124911.png]]

En la captura del servidor AAA se observa la creación de los usuarios iniciales:

- `ana / 1234`
    
- `pedro / 1234`

Y la configuración del router como “cliente RADIUS”:

- Client Name: wrt
    
- Client IP: `192.168.1.1`
    
- Secret compartido: `123456789`

Esto construye una relación de confianza entre el router y el servidor, similar a la que hay entre un Access Point corporativo y un servidor de autenticación (por ejemplo, Active Directory + RADIUS).

Con este contexto, pasamos al proceso de autenticación y seguridad.

---

## 8️⃣ Autenticación desde clientes

En este punto ya tenemos el servidor AAA funcionando como autoridad de autenticación. La WiFi ya no utiliza una contraseña PSK compartida. En redes reales, esto soluciona un problema serio: los usuarios no comparten la misma clave, y la baja seguridad del WPA2-PSK desaparece.

Al conectar cada laptop o dispositivo IoT:

**Config > Wireless0**

- WPA2
    
- User ID: `ana` o `pedro`
    
- Password: `1234`

![[Pasted image 20251111125025.png]]

>Ahora cada usuario se valida contra el **servidor AAA**, que acepta o rechaza conexiones según su base de datos interna. La red deja de depender de una contraseña única y pasa a un sistema basado en **credenciales individuales**.

Esto es el principio de un entorno corporativo seguro.

---

## 9️⃣ Preparar DHCP centralizado

En redes reales nunca se dejan múltiples servidores DHCP activos en el mismo segmento. Provoca asignaciones inconsistentes, conflictos de IP y comportamientos impredecibles.

Por eso se prepara el servidor AAA para cumplir doble función (AAA + DHCP):

**Server-PT > Services > DHCP**

- On
    
- Default Gateway: `192.168.1.1`
    
- Start IP: `192.168.1.10`

El servidor se convierte en la autoridad central para entregar direcciones IP dentro de la LAN.

Esto permite:

- llevar control de todos los dispositivos conectados
    
- registrar asignaciones
    
- generar auditoría (útil en ciberseguridad)

---

## 🔟 Desactivar DHCP del router

Los routers domésticos suelen traer su propio DHCP, pero en entornos empresariales el router/AP actúa solo como **punto de acceso**. Toda la gestión de IP debe centralizarse para mantener orden y control.

![[Pasted image 20251111125455.png]]

Por eso:

**Router > GUI > Setup**

- DHCP Server: Disabled

Esto evita que el router asigne IPs al margen de la infraestructura de control.

---

## 1️⃣1️⃣ Refrescar IP de todos los dispositivos

Como los clientes recuerdan su última IP, la red queda temporalmente “inconsistente”.

El refresco manual fuerza a todos los dispositivos a pedir IP nueva al servidor:

- Static → DHCP

Esto genera un “lease” nuevo en el servidor y garantiza que toda la red está bajo la misma autoridad de asignación.

---

## 1️⃣2️⃣ Configurar RFID Reader (LECTORA)

La **RFID Reader (LECTORA)** es un dispositivo IoT especial dentro del escenario. A diferencia de la mayoría de dispositivos IoT (como la ventana o el garaje), que simplemente reciben órdenes del servidor IoT, la lectora **produce eventos**. Esta diferencia es clave para entender su función:

- Los actuadores IoT → ejecutan acciones
    
- La lectora RFID → genera información

La lectora detecta el **Card ID** de la tarjeta RFID cada vez que la tarjeta pasa por delante. Ese evento debe ser enviado al servidor IoT para activar las reglas de automatización.

---

### 🔹 ¿Por qué necesita IP?

Porque es un dispositivo que **se comunica activamente con el servidor IoT**.

Necesita:

- una IP válida
    
- estar dentro de la misma subred
    
- tener un gateway correcto
    
- poder enviar paquetes al servidor IoT (`192.168.1.2`)

Sin IP, la lectora no puede transmitir el evento “Card ID detectado” al servidor.  
Y por tanto ninguna regla automática podría ejecutarse.

---

### 🔹 ¿Por qué se configura por cable y no por WiFi?

En Packet Tracer:

- La lectora RFID **solo tiene interfaz Ethernet (FastEthernet0)**.
    
- No dispone de módulo WiFi.
    
- Esto simula un lector fijo, instalado en pared o en puerta, cableado a la red interna.

Es el comportamiento que tienen muchas lectoras RFID reales en sistemas empresariales: van cableadas a un switch y no wifi.

---

### 🔹 Configuración

**Config > FastEthernet0 > IP Configuration**

Seleccionar:

- **DHCP**

Al hacerlo, el servidor AAA-DHCP le asigna una IP del rango programado:

- `192.168.1.10+`

Esto la integra en el “mapa” de la red bajo la autoridad del servidor.

---

### 🔹 ¿Qué ocurre después de recibir su IP?

La lectora:

1. aparece como dispositivo conectado en la tabla DHCP
    
2. puede ser registrada en el **IoT Server**
    
3. puede enviar eventos “Card ID”
    
4. puede actuar como disparador de automatizaciones

Es el elemento que convierte la red IoT en un sistema interactivo, no solo en un conjunto de interruptores.

---

### Concepto clave

La lectora es el **sensor** principal.  
El servidor IoT es el **cerebro**.  
Los dispositivos IoT son los **actuadores**.

Si el sensor no puede comunicarse con el cerebro, los actuadores nunca responderán.

---

## 1️⃣3️⃣ Activar IoT Server en AAA-DHCP

Hasta este punto el servidor solo cumple dos funciones:

- **AAA (RADIUS)**: autenticar usuarios que se conectan a la WiFi.
    
- **DHCP**: entregar direcciones IP a clientes e IoT.

Pero aún **no existe ningún mecanismo central para gestionar los dispositivos IoT**.  
Cada IoT está conectado a la WiFi, tiene su IP y puede recibir órdenes, pero no hay un “cerebro” que controle el conjunto.

Ese “cerebro” es el **IoT Server**, un módulo adicional dentro del propio servidor que:

- registra los dispositivos IoT
    
- mantiene una base de datos de estados (encendido/apagado, bloqueado/desbloqueado, etc.)
    
- permite aplicar reglas automáticas
    
- coordina acciones entre dispositivos

En un entorno real esto equivaldría a:

- un servidor MQTT
    
- Home Assistant
    
- un controlador IoT industrial
    
- un backend de gestión domótica

En Cisco Packet Tracer este módulo se activa manualmente porque no viene activo por defecto.

---

### 🔹 Paso 1: activar el servicio IoT

**Ruta:**  
`Server-PT > Services > IoT`

- **IoT Service: On**

Con esto habilitamos el “motor” que permite al servidor comunicarse con cada dispositivo IoT de la red.

Si no está activado, cualquier intento de conectar los dispositivos al servidor IoT fallará.

---

### 🔹 Paso 2: abrir la interfaz de gestión IoT

**Ruta:**  
`Desktop > IoT Monitor`

El IoT Monitor es la ventana de administración.  
Al abrirlo, el servidor nos pide:

- **Dirección del servidor IoT** → `192.168.1.2`
    
- **Usuario y contraseña**

Estos son credenciales internos para gestionar todo el sistema IoT, **no son los usuarios WiFi del AAA**, no son ana/pedro.

Aquí usamos por defecto:

- **User:** admin
    
- **Password:** admin

![[Pasted image 20251111130323.png]]

Es el acceso inicial del administrador del sistema.  
Equivale a entrar al “panel de control” de un sistema IoT.

---

### 🔹 Paso 3: crear un administrador IoT real

Tras autenticarnos como admin-admin, el sistema permite crear un nuevo usuario.

Creamos:

- **manuel / 1234**

Este es el usuario que tendrá permisos para:

- añadir dispositivos
    
- modificar estados
    
- crear reglas
    
- controlar remotamente el sistema

Actúa como **usuario administrador IoT** de la infraestructura.

En un entorno corporativo esto sería el responsable de domótica, automatización industrial, control de accesos o sistemas SCADA.

---

### Concepto clave

Aquí se separan **tres identidades distintas**:

1. **Usuario WiFi** → ana/pedro
    
2. **Administrador IoT interno** → manuel
    
3. **Admin inicial del sistema** → admin/admin

Esto imita la separación de roles que existe en seguridad real:

- usuarios finales
    
- administradores de red
    
- administradores de sistemas

Cada uno con permisos distintos y funciones distintas.

---

## 1️⃣4️⃣ Vincular dispositivos IoT al servidor IoT

Hasta este punto hemos habilitado el servidor IoT, hemos creado el usuario administrador y hemos activado la infraestructura que permite gestionar dispositivos.  
Pero todo esto no sirve de nada hasta que **cada dispositivo IoT declara explícitamente a qué servidor debe reportar**.

En otras palabras:

- Los dispositivos IoT no “se conectan solos” al servidor.
    
- Deben ser configurados uno por uno.
    
- Deben usar credenciales válidas del administrador IoT.

Esto es intencional y refleja el comportamiento **real** de dispositivos IoT profesionales.  
Cada sensor/actuador debe ser registrado en una plataforma central antes de poder ser controlado.

Si no se realiza esta vinculación, el servidor no sabe:

- qué dispositivos existen
    
- qué estados tienen
    
- qué acciones puede ejecutar
    
- qué reglas aplicar

---

### 🔹 Paso por paso en Packet Tracer

En cada dispositivo IoT:

**Config > IoT Server > Remote Server**

Completar:

- **Server Address:** `192.168.1.2`
    
- **User Name:** `manuel`
    
- **Password:** `1234`
    
- Pulsar **Connect**

---

### 🔹 ¿Qué ocurre internamente al pulsar "Connect"?

Técnicamente pasa esto:

1. El dispositivo envía una solicitud al servidor IoT.
    
2. El servidor valida credenciales (manuel / 1234).
    
3. Si son correctas, el servidor registra el dispositivo en la lista interna.
    
4. El dispositivo pasa a estado “online”.
    
5. El botón cambia a **Refresh**, indicando vinculación exitosa.
    
6. A partir de aquí el dispositivo es controlable desde el servidor (encendido, apagado, apertura, bloqueo, etc).
   ![[Pasted image 20251111125844.png]]

Esto es igual que cuando:

- un sensor Zigbee se empareja con un hub
    
- un dispositivo industrial se registra en un SCADA
    
- un sensor se conecta a un broker MQTT

---

### 🔹 Repetir el proceso en cada IoT

Debemos vincular cada uno de los siguientes:

- garaje
    
- ventana
    
- puerta
    
- camara
    
- LECTORA (RFID Reader)

Cada uno debe aparecer “Online” en el panel del IoT Monitor después de conectarlo.

---

### 🔹 ¿Por qué también la LECTORA (RFID Reader)?

Porque la LECTORA no es un dispositivo pasivo.  
Actúa como **sensor de eventos**.  
Debe comunicar al servidor:

- Card ID detectado
    
- Estado (Waiting, Valid, Invalid, etc)
    
- Cambios en tiempo real

El servidor usa estos eventos para activar reglas.  
Si la lectora no estuviera vinculada, nunca enviaría el evento “Card ID = 1001” al servidor.

---

### 🔹 ¿Por qué no se vincula la tarjeta?

La tarjeta RFID (IoT4) es un **elemento estático con un valor ID**.  
No tiene conectividad ni IP.  
Solo se “lee” desde la LECTORA.

---

### 🔹 Concepto de arquitectura IoT que se refleja aquí

Lo que estamos construyendo es:

`Dispositivos IoT  →  Servidor IoT  →  Reglas/Acciones  →  Estado final`

En un flujo real sería:

1. Dispositivo produce evento.
    
2. Servidor recibe evento.
    
3. Servidor evalúa condiciones.
    
4. Servidor ejecuta acciones en otros dispositivos.
    
5. Dispositivos cambian de estado.

Esto es la base de:

- Domótica
    
- Automatización industrial
    
- Control de accesos
    
- Sistemas inteligentes

---

### Resumen conceptual claro

❗ No basta con activar el servidor IoT.

✅ Hay que decirle a cada dispositivo “a quién debe obedecer”.

✅ Solo entonces el servidor puede monitorizar y controlar el ecosistema.

✅ Y solo entonces las reglas automáticas tienen efecto.

---

## 1️⃣5️⃣ Configurar tarjeta RFID

La tarjeta RFID (IoT4) no es un dispositivo conectado a la red. No tiene IP ni interfaz de comunicación. Es simplemente un **identificador físico** con un valor numérico programado:

- **Card ID = 1001**

Su único propósito es ser detectada por la **LECTORA** cuando se pasa por delante. La tarjeta actúa como:

- un “token de acceso”
    
- un disparador de eventos
    
- una clave vinculada a reglas de automatización

No se configura nada más porque no participa en la red. Su función es proporcionar el dato que activará las acciones en el servidor IoT.

---

## 1️⃣6️⃣ Creación de reglas automáticas IoT

El servidor aplica lógica condicional, una forma de “programación sin código”.

### ✅ Regla 1 — abrir (cuando la tarjeta es válida)

**If Card ID = 1001 → Then activar todo**

Esto imita un sistema de acceso inteligente tipo:

![[Pasted image 20251111130025.png]]

- apertura de garaje
    
- subida de persianas
    
- encendido de luces
    
- apertura de puerta

---

### ✅ Regla 2 — cerrar (cuando la tarjeta no es válida o está fuera de alcance)

**If Card ID != 1001 → Then apagar todo**

Esto simula:

![[Pasted image 20251111130043.png]]

- cierre automático
    
- bloqueo de puerta
    
- desactivación de sensores
    
- apagado de cámara
    
- desconexión del garaje

---

## 1️⃣7️⃣ Prueba final

Arrastrar la tarjeta sobre la lectora simula una **lectura RFID real**.

Acciones:

- LECTORA detecta ID
    
- Módulo IoT envía evento al servidor
    
- El servidor verifica la condición
    
- Ejecuta las acciones vinculadas en tiempo real

![[Pasted image 20251111130114.png]]

Es un flujo completo de autenticación → autorización → acción.

---

# ✅ Estado final del sistema

- WiFi protegido con autenticación RADIUS
    
- Control central AAA con usuarios individuales
    
- DHCP unificado para toda la red
    
- Router convertido en un AP puro
    
- IoT monitorizado desde un único servidor
    
- Automatización RFID funcionando

En conjunto, la red es más ordenada, más segura y más predecible, imitando arquitecturas de empresas modernas.

---