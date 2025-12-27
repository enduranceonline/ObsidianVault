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

 Esto introduce dos ideas fundamentales:

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

### 🔧 Vinculación del router con el servidor AAA (RADIUS)

Tras crear los usuarios en el servidor AAA y activar el servicio, es necesario **registrar el router WRT300N como “cliente RADIUS”**. Sin esta vinculación, el router no sabrá a qué servidor enviar las peticiones de autenticación WPA2-Enterprise.
#### ⚙️ Pasos en el router

**Router → GUI → Security → Wireless → RADIUS**

Completar con:

- **Server IP Address:** `192.168.1.2`
    
- **Port Number:** `1812`
    
- **Shared Secret:** `123456789`
    
- **Status:** Enabled

![[Pasted image 20251120115734.png]]

Este proceso establece la relación de confianza router ↔ servidor y activa la autenticación centralizada (**AAA**). A partir de aquí, cada conexión WiFi enviará un challenge al servidor para verificar credenciales.

#### Por qué es necesario

- El router deja de usar clave PSK.
    
- Todas las conexiones WiFi pasan por el servidor AAA.
    
- Cada usuario se valida individualmente (ana, pedro…).
    
- El router se convierte en un **Access Point empresarial**, no en un router doméstico.

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

Hasta este momento, el servidor había asumido únicamente dos grandes responsabilidades dentro de la red: autenticar usuarios mediante AAA (es decir, actuar como un servidor RADIUS que permite o deniega el acceso a la WiFi) y repartir direcciones IP a todos los dispositivos a través del servicio DHCP. Gracias a esto, la red ya tenía orden, autenticación y una asignación de direcciones coherente. Sin embargo, todos los dispositivos IoT —las puertas, ventanas, cámaras, el garaje e incluso la lectora RFID—, aunque ya disponían de una dirección IP y podían comunicarse a través de la red, seguían siendo elementos aislados, incapaces de coordinarse entre sí o de reaccionar a condiciones concretas. Faltaba un componente clave: un cerebro.

Ese “cerebro” es el **IoT Server**, un módulo adicional que se activa dentro del propio servidor AAA-DHCP. Cuando entra en funcionamiento, el servidor deja de ser un mero gestor de usuarios y direcciones IP para convertirse en una plataforma capaz de recibir eventos, registrar dispositivos, almacenar estados y ejecutar reglas que reaccionen ante lo que ocurre en la red.

En arquitecturas reales, este componente equivale a lo que haría Home Assistant en una casa inteligente, un broker MQTT en un despliegue moderno de IoT, o un servidor SCADA en un entorno industrial. Packet Tracer lo simplifica, pero su propósito es el mismo: convertir una red de dispositivos sueltos en un sistema coordinado capaz de comportarse inteligentemente.

Para activarlo, basta con entrar en el servidor desde la sección **Services** y encender el apartado IoT.

![[Pasted image 20251120120747.png]]

En el momento en que se activa este módulo, el servidor empieza a escuchar las peticiones de registro de cualquier dispositivo IoT que quiera asociarse a él. Si el servicio permanece desactivado, ningún dispositivo podrá registrarse ni aparecer en el IoT Monitor, y todas las reglas automáticas quedarían en un estado inservible. Activarlo es equivalente a encender un sistema operativo domótico que, de golpe, convierte la red en una plataforma automatizada.

Una vez habilitado el servicio, la siguiente parada se encuentra en el escritorio del servidor, concretamente en la aplicación llamada **IoT Monitor**, que actúa como consola de control del ecosistema IoT.

![[Pasted image 20251111130323.png]]

El IoT Monitor solicita que introduzcamos la dirección del servidor IoT (en este caso, el propio servidor local con IP **192.168.1.2**) y un usuario con privilegios administrativos. Estos usuarios **no tienen nada que ver** con los usuarios que se conectan a la WiFi mediante AAA (como ana o pedro). Son credenciales internas del sistema IoT y funcionan de forma totalmente independiente. Inicialmente, como ocurre en muchos dispositivos reales, Packet Tracer proporciona un usuario por defecto: **admin / admin**.

Tras iniciar sesión, la interfaz ya permite crear usuarios administradores reales. En el escenario se crea uno llamado **manuel**, con contraseña **1234**, que será la cuenta utilizada por todos los dispositivos IoT para registrarse y, más adelante, para que el administrador humano gestione reglas, revise estados o añada nuevos elementos. Este paso recuerda a las buenas prácticas reales: nunca se debe operar un sistema con la cuenta por defecto, ya que comprometería toda la seguridad del sistema.

Desde este punto es importante entender que ahora existen claramente tres niveles de identidad dentro de la red. Por un lado, están los usuarios que se autentican en la WiFi mediante AAA, como ana o pedro. Por otro, el administrador del ecosistema IoT (manuel), encargado de vincular dispositivos y definir reglas. Y, como cuenta de fondo, el usuario inicial por defecto admin/admin, equivalente a una llave maestra que solo se debe usar para la puesta en marcha. Esta separación ayuda a que cada capa de la red tenga su propio conjunto de permisos, como ocurre en empresas reales.

---

## 1️⃣4️⃣ Vincular los dispositivos IoT al servidor IoT

Llegados a este punto, el servidor ya está preparado para recibir y gestionar dispositivos IoT, pero ellos aún no saben que existe un controlador central. A diferencia de otros sistemas “plug and play”, en IoT casi nunca ocurre un emparejamiento automático. Cada dispositivo debe declarar explícitamente a qué servidor quiere reportar. Es un proceso similar al de emparejar un sensor Zigbee con un hub doméstico, o registrar un nuevo dispositivo industrial dentro de un SCADA.

Cada actuador y sensor del escenario —la ventana, el garaje, la puerta, la cámara y especialmente la **LECTORA RFID**— debe configurarse desde la pestaña **Config → IoT Server → Remote Server**, indicando tres datos esenciales:

- la dirección del servidor IoT,
    
- el usuario administrador (`manuel`),
    
- y la contraseña (`1234`).
    

Solo después de introducir estos datos y pulsar **Connect**, el dispositivo queda oficialmente registrado en la plataforma.

A nivel interno, ese clic desencadena un intercambio muy simple, pero conceptualmente profundo: el dispositivo envía una solicitud al servidor IoT, el servidor valida las credenciales, agrega el dispositivo a su base de datos y confirma el registro cambiando el botón a **Refresh**. Desde ese momento, el dispositivo se considera online, aparece en el IoT Monitor y puede participar en reglas.

![[Pasted image 20251111125844.png]]

Si este proceso no se hace, el dispositivo, aunque conectado a la WiFi y con una IP válida, queda huérfano: no puede recibir órdenes, no aparece en el panel de control y no participa en ninguna lógica de automatización.

El caso más importante es el de la **LECTORA RFID**, ya que ella es la encargada de generar los eventos que darán vida a todo el sistema. La lectora no es un dispositivo pasivo: detecta el ID de la tarjeta, lo envía al servidor y desencadena las acciones programadas. Si no estuviera registrada, el servidor no recibiría ningún evento, y el sistema entero —por muchos IoT que tuviera conectados— quedaría completamente inerte.

Por su parte, la tarjeta RFID (IoT4) funciona de manera opuesta: no se registra, no se vincula y no tiene IP. Es un objeto puramente pasivo que contiene un identificador, como un llavero NFC o una tarjeta magnética real. Su única función es ser presentada ante la lectora RFID, que es quien se comunica con el servidor.

Este modelo de comunicación refleja muy bien cómo se construyen las arquitecturas IoT modernas: los dispositivos hablan con un servidor central, los servidores contienen la lógica y las tarjetas o sensores físicos actúan como desencadenantes de eventos.

---

## 1️⃣5️⃣ La tarjeta RFID: un identificador, no un dispositivo de red

La tarjeta RFID es un elemento especialmente interesante porque, aunque Packet Tracer lo presenta como un dispositivo IoT, en realidad se parece mucho más a un objeto del mundo físico: es simplemente un portador de un valor de identificación. En este caso, el valor configurado es **Card ID = 1001**. No tiene dirección IP, no se comunica con el servidor y ni siquiera es capaz de generar eventos por sí sola. Es la lectora la que interpreta ese valor y decide si debe enviarlo al servidor IoT.

Por ello, la tarjeta no requiere ningún tipo de configuración extra ni debe vincularse al servidor. Su propósito es puramente desencadenante: representa una credencial de acceso que se usará como condición en las reglas.

---

## 1️⃣6️⃣ Creación de reglas automáticas IoT

Una vez que todos los dispositivos están registrados y conectados al servidor IoT, llega la parte más interesante del sistema: la automatización. Desde el IoT Monitor es posible crear reglas que siguen la lógica clásica de programación:

> **Si ocurre X, ejecuta Y.**

Packet Tracer lo simplifica en una interfaz donde se seleccionan condiciones (como la lectura de un `Card ID`) y se asignan acciones (como abrir una puerta o encender una luz).

La primera regla que se configura es la de **apertura**, diseñada para que el sistema reaccione cuando la tarjeta legítima, con ID 1001, es detectada por la lectora RFID. Esta regla indica: si la lectora detecta el `Card ID = 1001`, entonces activa todos los dispositivos relevantes. De esta manera, al pasar la tarjeta por la lectora, el garaje se abre, la ventana se levanta, la puerta se desbloquea y la cámara se enciende.

![[Pasted image 20251111130025.png]]

La segunda regla implementa la lógica contraria: siempre que el `Card ID` detectado **no** sea 1001 (es decir, cualquier otra tarjeta o ausencia de tarjeta), el sistema debe cerrarlo todo y devolver la red a un estado seguro. Esta regla representa la lógica de “estado seguro por defecto”, donde los dispositivos vuelven automáticamente a estar cerrados, apagados o bloqueados cuando no hay una credencial válida.

![[Pasted image 20251111130043.png]]  
![[Pasted image 20251120122109.png]]

En muchos entornos reales, este tipo de reglas se utiliza para automatizar accesos, iluminar zonas solo cuando es necesario, o gestionar sistemas de seguridad que dependen del movimiento o la presencia de un usuario autorizado.

---

## 1️⃣7️⃣ Prueba final del circuito IoT

Con el sistema completamente configurado, se realiza la prueba final. En Packet Tracer basta con arrastrar la tarjeta sobre la lectora RFID para simular la lectura del identificador. En ese momento, la lectora detecta el `Card ID`, lo envía al servidor IoT, y este evalúa todas las reglas activas. Si la tarjeta coincide, se activará la secuencia de apertura; si no, se ejecutará la secuencia de cierre.

![[Pasted image 20251111130114.png]]

Este flujo representa el ciclo real de un sistema de control de accesos basado en tarjetas: identificación → validación → acción → cambio de estado.

---

## Estado final del sistema

Al final de todo este proceso, la red deja de ser un simple conjunto de dispositivos conectados por WiFi. Lo que antes era una red doméstica básica —donde un router entrega IPs, cada aparato se conecta sin mayor control y la única seguridad real es una contraseña compartida— se transforma en una infraestructura mucho más parecida a la de un pequeño entorno profesional: ordenada, segmentada, inteligente y, sobre todo, segura.

El cambio más profundo se observa en la **forma en que se conectan y autentican los dispositivos**. La red WiFi deja de basarse en una única contraseña compartida para todos los miembros del hogar y empieza a utilizar un sistema de autenticación individual mediante **AAA (Authentication, Authorization and Accounting)**. Esto significa que cada persona, y si se quisiera, cada dispositivo, posee sus propias credenciales para entrar a la WiFi. No existe ya una “clave universal” que si alguien descubre, abre la puerta a toda la red. En su lugar, la autenticación se gestiona a través de un servidor RADIUS, que se convierte en la autoridad que decide quién puede entrar y bajo qué condiciones.

Este enfoque tiene una implicación directa en la seguridad doméstica: si un vecino roba la contraseña del WiFi, si un invitado la comparte sin permiso o si un servicio del hogar queda comprometido, la solución no consiste en cambiar la contraseña a todo el mundo —dramático y molesto— sino en revocar ese usuario concreto, tal como se haría en una empresa. Además, cada intento de acceso queda registrado (la “A” de Accounting), lo cual permite detectar actividad inusual, intentos fallidos reiterados o comportamientos sospechosos.

Por otro lado, la gestión de direcciones IP queda centralizada en el servidor mediante el servicio DHCP. Esto aporta orden, control y visibilidad. En una casa normal, el router asigna direcciones sin más, pero en este tipo de arquitectura el servidor documenta cada asignación, sabe qué dispositivo es quién y permite diagnósticos más precisos. Si un dispositivo empieza a comportarse de forma rara, es más sencillo localizarlo y actuar. A nivel doméstico, esto abre la puerta a monitorizar mejor la actividad de dispositivos IoT —especialmente los más problemáticos— como enchufes inteligentes baratos, bombillas WiFi desconocidas o cámaras de origen dudoso.

El router, al adoptar el rol de **punto de acceso puro**, se convierte en un elemento mucho más simple y estable. Ya no gestiona la lógica de los accesos ni las reglas de red: solo transmite la señal WiFi. Esto reduce su superficie de ataque y lo vuelve menos vulnerable. Muchos fallos de seguridad en redes domésticas ocurren en routers con demasiadas funciones integradas. Delegar las funciones de autenticación y DHCP al servidor elimina una buena parte de estos riesgos.

En cuanto a los dispositivos IoT, la diferencia es incluso más drástica. En una red doméstica típica, los dispositivos IoT se conectan directamente al router sin supervisión: una cámara entra, una bombilla se conecta, un enchufe recibe internet… pero nadie sabe si están enviando datos extraños, si se comunican con direcciones desconocidas o si alguien está accediendo desde fuera. Con un servidor IoT centralizado —como el que ofrece Packet Tracer en esta simulación— cada dispositivo queda registrado, autenticado y bajo supervisión continua. El servidor sabe qué dispositivos existen, qué estados tienen y qué acciones realizan, lo cual facilita detectar irregularidades y permite establecer reglas de comportamiento.

Este modelo también habilita automatizaciones seguras basadas en condiciones del mundo real. En nuestro caso, una tarjeta RFID actúa como disparador y el servidor decide si debe abrir puertas, encender luces o activar cámaras. En un hogar real, esa misma arquitectura podría replicarse con:

- un lector NFC o una app móvil como credencial,
    
- sensores de movimiento o presencia,
    
- cerraduras inteligentes,
    
- iluminación automatizada,
    
- detección de apertura o vibración.
    

El servidor conocería cada evento y aplicaría lo que esté programado, garantizando que todo ocurre bajo control y no de manera caótica. Además, al centralizar la lógica IoT se evita que cada aplicación de fabricante (TP-Link, Xiaomi, Philips, etc.) abra agujeros externos en la red para comunicarse con sus servidores propios, uno de los mayores riesgos en una casa moderna.

En conjunto, lo que se ha construido es un modelo de red doméstica que se asemeja más a una pequeña infraestructura empresarial:

- usuarios con credenciales únicas,
    
- autenticación robusta basada en AAA,
    
- asignación de direcciones coherente,
    
- control centralizado de dispositivos IoT,
    
- automatizaciones seguras,
    
- y una superficie de ataque notablemente menor.
    

Y lo más importante: esta arquitectura no solo da más control y seguridad, sino que permite escalar la red —añadiendo más dispositivos, automatizaciones o usuarios— sin que se vuelva caótica o vulnerable. En un mundo donde los hogares tienen cada vez más dispositivos conectados, integrar un servidor AAA y un controlador IoT deja de ser un lujo técnico y empieza a ser una forma realista de proteger un entorno doméstico moderno.