#certificacion #network #apuntes
# 🧩 Sección 1: What Is Ethernet?

---

### 📌 Introducción

**Ethernet** es un término comúnmente malinterpretado. Técnicamente, hace referencia al estándar **IEEE 802.3**, publicado en 1980, que define cómo se deben construir y operar las redes Ethernet. Incluye especificaciones de velocidad, medios de transmisión, formatos de tramas, y más.

---

### 📘 IEEE 802.3

- Ethernet es el nombre informal del estándar **IEEE 802.3**.
- Este estándar contiene:
  - Tipos de cables y medios.
  - Velocidades soportadas.
  - Formato de trama.
  - Métodos de acceso al medio.

---

### 🧱 Estructura de la trama Ethernet

Una **trama Ethernet** contiene:

- **Dirección MAC de destino**
- **Dirección MAC de origen**
- **Datos (Payload)** – hasta 1500 bytes
- **FCS (Frame Check Sequence)** – para detección de errores

![[Pasted image 20250607141018.png]]

- El **tamaño máximo estándar** de una trama Ethernet es de 1500 bytes (sin incluir cabeceras adicionales).
- El formato de la trama **no ha cambiado significativamente desde 1980**, lo que garantiza compatibilidad entre dispositivos antiguos y modernos.

---

### 🔄 Compatibilidad de medios

Debido a que el marco Ethernet no cambia, es fácil:
- Interconectar **fibra óptica y par trenzado** mediante convertidores de medios.
- Usar una tarjeta moderna con una red antigua, ajustando solo la velocidad.

---

### ⚙️ Nomenclatura de estándares Ethernet

Ejemplo clásico: `10BASE-T`

| Elemento     | Significado                                 |
|--------------|---------------------------------------------|
| `10`         | Velocidad en Mbps                           |
| `BASE`       | Banda base (un solo canal de transmisión)   |
| `T`          | Tipo de medio (en este caso, twisted pair)  |

Otros sufijos históricos:
- `5` = 500 m (Ethernet coaxial grueso)
- `2` = 200 m (Ethernet coaxial fino)
- `F` = fibra óptica
- `T` = par trenzado

---

### 🚀 Evolución de Ethernet

| Estándar      | Velocidad       | Medio                          |
|---------------|------------------|-------------------------------|
| 10BASE5       | 10 Mbps          | Coaxial grueso                |
| 10BASE-T      | 10 Mbps          | UTP                           |
| 100BASE-TX    | 100 Mbps         | UTP (Cat 5/5e)                |
| 1000BASE-T    | 1 Gbps           | UTP (Cat 5e/6)                |
| 1000BASE-LX   | 1 Gbps           | Fibra óptica monomodo         |
| 10GBASE-T     | 10 Gbps          | UTP (Cat 6a/7/8)              |

---

### 📝 Para el examen

- Reconoce el estándar **IEEE 802.3** como la base de Ethernet.
- Identifica la **estructura de una trama Ethernet**.
- Comprende el significado de cada parte de la nomenclatura (e.g., `100BASE-TX`).
- Recuerda que **la trama Ethernet no cambia**, solo los medios y velocidades.

---

### ✅ Conclusión

Ethernet ha evolucionado mucho desde 1980, pero su núcleo —la estructura de la trama— se mantiene. Esto permite compatibilidad entre generaciones de hardware y medios físicos distintos. Entender estos fundamentos es clave para diagnosticar redes y aprobar el examen Network+.

---
# 🧩 Sección 2: Ethernet Frames

---

### 📌 Introducción

Las tramas Ethernet son el tipo de trama más común y fundamental en redes modernas. Comprender su estructura permite analizar y diagnosticar redes con precisión, lo cual es esencial tanto para el examen Network+ como para la práctica profesional.

---

### 🧱 Estructura de una trama Ethernet

Una trama Ethernet típica incluye los siguientes campos (de izquierda a derecha):

1. **Preámbulo**
   - Patrón alternante de 1s y 0s.
   - Permite que la tarjeta de red detecte el inicio de una trama.

2. **Dirección MAC de destino**
   - A quién va dirigida la trama.
   - 48 bits (6 bytes).

3. **Dirección MAC de origen**
   - Quién envía la trama.
   - 48 bits (6 bytes).

4. **Tipo (EtherType)**
   - Indica el protocolo de capa superior (ej: 0x0800 para IPv4).
   - 2 bytes.

5. **Datos (Payload)**
   - Información que se transporta.
   - Mínimo: 46 bytes / Máximo: 1500 bytes (MTU).
   - Si hay menos de 46 bytes → se añade **padding** para alcanzar el mínimo.

6. **FCS (Frame Check Sequence)**
   - Verificación de errores (CRC de 32 bits).
   - Detecta alteraciones en la trama durante la transmisión.

---

### 📏 Tamaño de trama y MTU

| Concepto              | Valor estándar |
|------------------------|----------------|
| Tamaño mínimo de trama | 64 bytes       |
| Tamaño máximo (MTU)    | 1500 bytes     |
| Tamaño con encabezados | Hasta 1518 bytes (con preámbulo y FCS) |

- **Jumbo frames**: tramas extendidas para redes de alta velocidad → hasta **9000 bytes**.

---

### 📐 Vocabulario técnico

- **Octeto**: Sinónimo de byte (8 bits), común en documentación técnica.
- **MTU (Maximum Transmission Unit)**: Tamaño máximo de datos que se pueden enviar en una sola trama.

---

### 🔁 Fragmentación y secuenciación

- Si los datos a enviar superan el MTU, se dividen en múltiples tramas.
- Cada fragmento incluye su propio encabezado y puede tener un número de secuencia para reensamblaje.

---

### 📝 Consejos para el examen

- Memoriza cada campo del **marco Ethernet**.
- Entiende la función de la **FCS** y la importancia del **preámbulo**.
- Relaciona **MTU** con problemas de red (como pérdida de paquetes por fragmentación).
- Reconoce que los **Jumbo Frames** solo se usan en redes específicas de alto rendimiento.

---

### ✅ Conclusión

Dominar la estructura de la trama Ethernet te permitirá analizar el tráfico con herramientas como Wireshark, detectar errores y entender cómo fluye realmente la información por una red. Este conocimiento es tanto teórico como práctico, y es esencial para cualquier técnico en redes.

---

# 🧩 Sección 3: Terminating Twisted Pair

---

### 📌 Introducción

Confeccionar tus propios cables Ethernet puede parecer una tarea tediosa, pero es una habilidad esencial para técnicos de redes. Esta sección cubre las herramientas necesarias, los pasos para crimpar cables de par trenzado y las normas de cableado más comunes.

---

### 🛠️ Herramientas necesarias

- **Crimpadora RJ45** (8P8C)
- **Tijeras o cortador de cable**
- **Conectores RJ45 (8P8C)**
- **Probador de cables** (opcional pero recomendado)
- **Cable UTP (Cat 5e, Cat 6...)**

![[Pasted image 20250607140530.png]] 
![[Pasted image 20250607140754.png]]

![[Pasted image 20250607140827.png]]

---

### ✂️ Pasos para terminar un cable de par trenzado

1. **Corta la longitud deseada de cable** desde el rollo.
2. **Pela unos 2-3 cm del revestimiento exterior** del cable.
3. **Desenreda los pares trenzados** (4 pares → 8 hilos).
4. **Organiza los hilos según la norma elegida** (ver abajo).
5. **Corta los hilos uniformemente** dejando unos 13 mm expuestos.
6. **Inserta los hilos en el conector RJ45**, asegurándote de que lleguen hasta el fondo.
7. **Crimpa con la herramienta adecuada**.
8. **Prueba la continuidad con un tester** si está disponible.

---

### 📏 Normas de cableado TIA/EIA

#### 🔹 568B (más común en redes modernas)

1. Blanco/Naranja  
2. Naranja  
3. Blanco/Verde  
4. Azul  
5. Blanco/Azul  
6. Verde  
7. Blanco/Marrón  
8. Marrón  

#### 🔹 568A

1. Blanco/Verde  
2. Verde  
3. Blanco/Naranja  
4. Azul  
5. Blanco/Azul  
6. Naranja  
7. Blanco/Marrón  
8. Marrón  

![[Pasted image 20250607140202.png]]

---

### 🔄 Tipos de cableado

| Tipo de cable  | Norma en cada extremo      | Uso común                                    |
|----------------|-----------------------------|----------------------------------------------|
| **Recto**      | 568B en ambos extremos      | PC a switch/router                           |
| **Cruzado**    | 568A en un extremo, 568B en el otro | Conexión directa entre switches o PCs antiguos |

> Hoy en día, la mayoría de dispositivos modernos (auto-MDI/MDI-X) detectan y ajustan automáticamente.

---

### 📘 Nota técnica

- **RJ45** es el nombre comercial común.
- El nombre técnico es **8P8C**: 8 posiciones, 8 contactos.

---

### 📝 Consejos para el examen

- Reconocer las normas 568A y 568B.
- Saber diferenciar un cable **recto** de uno **cruzado**.
- Conocer los pasos correctos para crimpar un cable.
- Entender cuándo se usa cada tipo de terminación.

---

### ✅ Conclusión

Terminar cables de par trenzado es una habilidad esencial para los técnicos de red. Aunque cada vez menos común en instalaciones modernas, sigue siendo una herramienta útil tanto para laboratorio como para diagnóstico. Saber hacerlo bien marca la diferencia.

---

# 🧩 Sección 4: Networking Appliances

---

### 📌 Introducción

Las redes modernas emplean una variedad de dispositivos —físicos y virtuales— para enrutar, proteger, distribuir y almacenar datos. Conocer el propósito de cada uno es esencial para el examen Network+ y para cualquier trabajo en redes.

---

### 📡 Routers

- Dispositivo de capa 3 del modelo OSI.
- Encargado de **enrutar paquetes IP** entre redes distintas.
- Usa **tablas de enrutamiento** para decidir el mejor camino.
- Compara con el sistema de **códigos postales** en el correo.

---

### 🔥 Firewalls

- Puede ser **hardware o software**.
- Filtra tráfico entrante/saliente según políticas de seguridad.
- Protege la red frente a accesos no autorizados.
- Funciona como una "puerta cerrada" que controla el acceso.

---

### 🔍 IDS / IPS / IDPS

| Sistema | Función principal                           | Acción típica                 |
|---------|----------------------------------------------|-------------------------------|
| **IDS** | Detección de intrusos                        | Genera alertas                |
| **IPS** | Prevención de intrusos                       | Bloquea tráfico malicioso    |
| **IDPS**| Combinación de IDS + IPS                     | Detección + bloqueo           |

- Basados en **firmas** o **anomalías**.
- Detectan desviaciones respecto a una **línea base** de tráfico.
- Pueden generar **falsos positivos** o **falsos negativos**.

---

### ⚖️ Load Balancer (Equilibrador de carga)

- Distribuye tráfico entre múltiples servidores.
- Mejora **rendimiento, disponibilidad y tolerancia a fallos**.
- Actúa como **despachador de tráfico** o “policía de tránsito”.

---

### 🛡️ Proxy Server

- Actúa como intermediario entre el cliente y el servidor.
- Mejora **privacidad**, **rendimiento** y **control de acceso**.
- Puede almacenar datos en caché, filtrar contenido o anonimizar conexiones.

---

### 💾 NAS vs SAN

| Característica     | NAS                                  | SAN                                   |
|--------------------|---------------------------------------|----------------------------------------|
| Tipo de acceso     | A nivel de archivo                    | A nivel de bloque                      |
| Uso típico         | Compartir archivos entre usuarios     | Almacenamiento empresarial intensivo  |
| Estructura         | Dispositivo autónomo con SO propio    | Red completa de almacenamiento         |
| Escalabilidad      | Limitada                              | Alta                                   |

- **NAS (Network Attached Storage)**:
  - Nodo conectado a la LAN.
  - Proporciona acceso centralizado a archivos.
- **SAN (Storage Area Network)**:
  - Red especializada de almacenamiento.
  - Acceso de bajo nivel similar a un disco duro.

---

### 📝 Claves para el examen

- Identifica los **propósitos y ubicaciones** de cada dispositivo.
- Diferencia IDS (detecta) de IPS (bloquea).
- Conoce cuándo usar **proxy, firewall, NAS, SAN**, etc.
- Relaciona los dispositivos con sus **capas OSI** cuando sea posible.

---

### ✅ Conclusión

Entender los dispositivos que conforman la infraestructura de red es esencial tanto para el diagnóstico como para el diseño y la administración. Cada uno cumple una función única, desde el filtrado de amenazas hasta el equilibrio de carga o el almacenamiento de datos.

---

# 🧩 Sección 5: Hubs vs Switches

---

### 📌 Introducción

Los **hubs** y los **switches** son dispositivos utilizados para interconectar equipos dentro de una red Ethernet. Aunque los hubs están obsoletos, siguen apareciendo en el examen Network+ y es importante conocer sus diferencias con los switches.

---

### 🔄 ¿Qué es un hub?

- Dispositivo de red que actúa como **repetidor multipuerto**.
- No distingue entre dispositivos: **reenvía cualquier trama a todos los puertos**.
- Trabaja en la **Capa 1** del modelo OSI.
- Usa **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)** para gestionar colisiones.
- Todos los dispositivos conectados comparten el **mismo dominio de colisión**.

#### ❌ Inconvenientes de los hubs:
- Generan muchas **colisiones**.
- **Bajo rendimiento** en redes con múltiples dispositivos.
- Todo el tráfico es **broadcast**, sin eficiencia.

---

### 🔀 ¿Qué es un switch?

- Dispositivo **inteligente** que reenvía tramas basándose en **direcciones MAC**.
- Aprende y mantiene una **tabla MAC** para conmutar tramas solo al puerto correcto.
- Trabaja en la **Capa 2** del modelo OSI.
- Reduce las colisiones → cada conexión es **punto a punto** virtual.
- Todos los puertos están en **diferentes dominios de colisión**.

#### ✅ Ventajas de los switches:
- Mayor **eficiencia**.
- **Mejor rendimiento** de red.
- Soporte de **tráfico full-duplex**.
- Gestionan **broadcasts**, pero no los evitan (dominio de difusión compartido).

---

### 📡 CSMA/CD en hubs

- Detectan colisiones comparando señales.
- Esperan un tiempo aleatorio (generador aleatorio interno) para reenviar.
- Muy común en redes Ethernet **antiguas**.

---

### 📊 Comparativa rápida

| Característica       | Hub                     | Switch                     |
|----------------------|--------------------------|----------------------------|
| Capa OSI             | Capa 1 (física)          | Capa 2 (enlace de datos)   |
| Tráfico              | Broadcast total          | Unicast según MAC          |
| Tabla de direcciones | No                      | Sí (tabla MAC)             |
| Dominio de colisión  | Único compartido         | Uno por puerto             |
| Dominio de difusión  | Uno                      | Uno                        |
| Velocidad            | Menor                    | Mayor                      |
| Seguridad            | Baja (captura sencilla)  | Alta (tráfico dirigido)    |

---

### 🕵️‍♂️ Nota: Captura de tráfico

- En hubs es fácil "sniffear" tráfico, ya que todo se envía a todos.
- En switches es más difícil, pero pueden usarse **puertos espejo (SPAN)** para ese propósito.

---

### 📝 Para el examen

- Saber que los **hubs son obsoletos**, pero **preguntados** en Network+.
- Distinguir **dominio de colisión** vs **dominio de difusión**.
- Relacionar los dispositivos con las **capas OSI**.
- Identificar casos de uso especiales (ej: análisis de tráfico).

---

### ✅ Conclusión

Aunque los **switches** han reemplazado completamente a los **hubs** en redes modernas, entender sus diferencias es crucial para diseñar, mantener o actualizar una red. Si todavía tienes hubs, ¡reemplazarlos por switches es una mejora inmediata!

---
# 🧩 Sección 6: Connecting Switches

---

### 📌 Introducción

En redes Ethernet, es común tener que **interconectar múltiples switches** para expandir el número de dispositivos conectados o extender la red. Esta sección explica cómo conectar correctamente switches y evitar errores críticos como los **loops de conmutación**.

---

### 🔌 Métodos para conectar switches

#### 🔗 Cable cruzado (crossover)
- Antiguamente necesario para conectar switch ↔ switch.
- Un extremo con norma **568A** y el otro con **568B**.

![[Pasted image 20250607134033.png]]
#### 🔗 Cable recto (straight-through)
- Hoy en día se puede usar gracias a la función **auto-MDI/MDI-X**.
- El switch detecta automáticamente el tipo de conexión y ajusta los pines.

![[Pasted image 20250607134115.png]]

---

### 📥 Puerto de enlace ascendente (uplink)

- Algunos switches antiguos tienen un **puerto especial** o un botón para convertir un puerto normal en uplink.
- Este puerto realiza internamente el cruce de señales.
- Permite conectar switches con **cable recto**.

---

### ⚙️ Auto MDI/MDI-X

- Funcionalidad moderna en la mayoría de switches.
- **Detecta si la conexión es hacia un switch o dispositivo final**.
- Ajusta automáticamente la interfaz sin necesidad de cable cruzado.

---

### ⚠️ Switch Loop (Bucle de conmutación)

Un **bucle de conmutación** (switch loop) ocurre cuando dos o más switches están conectados de forma redundante sin un mecanismo de control adecuado. Esto puede provocar que los paquetes circulen indefinidamente, saturando la red y causando inestabilidad. Para prevenir estos bucles, se utiliza el **Protocolo de Árbol de Expansión** (**STP**, por sus siglas en inglés), que gestiona las rutas redundantes y asegura una topología libre de bucles.

### 🛡️ ¿Cómo previene STP los bucles?

STP crea una topología lógica en forma de árbol sin bucles mediante los siguientes mecanismos:
	Detecta y **bloquea rutas redundantes** automáticamente.
	Usa **BPDU (Bridge Protocol Data Units)** para comunicar entre switches.
	Elige un **root bridge** y calcula rutas seguras sin bucles.

- **Elección del puente raíz (root bridge)**: Todos los switches intercambian tramas especiales llamadas **BPDU** (Bridge Protocol Data Units) para determinar cuál será el puente raíz. Este se elige basándose en el **Bridge ID**, que combina la prioridad del puente y su dirección MAC. El switch con el Bridge ID más bajo se convierte en el puente raíz .
    
- **Determinación de puertos**: Una vez elegido el puente raíz, STP calcula la mejor ruta desde cada switch hacia este. Los puertos se clasifican en:
    
    - **Puerto raíz (root port)**: El puerto con el camino de menor costo hacia el puente raíz.
        
    - **Puerto designado (designated port)**: El puerto en cada segmento de red que tiene el mejor camino hacia el puente raíz.
        
    - **Puerto bloqueado**: Puertos que no son ni raíz ni designados y se bloquean para prevenir bucles .
        
- **Estados de los puertos**: Los puertos pasan por varios estados (bloqueado, escucha, aprendizaje, reenvío) para asegurar una transición segura y evitar bucles durante cambios en la topología.

https://www.youtube.com/watch?v=liRdZ5p1Xp4

![[Pasted image 20250607135830.png]]
### 🔄 Protección adicional: Loop Guard

Aunque STP es eficaz, existen situaciones donde pueden ocurrir bucles, especialmente si un puerto deja de recibir BPDUs debido a fallos unidireccionales. En estos casos, el puerto podría erróneamente pasar al estado de reenvío, creando un bucle. Para mitigar esto, se implementa **Loop Guard**, una función que:

- **Monitorea la recepción de BPDUs**: Si un puerto configurado para recibir BPDUs deja de recibirlos, Loop Guard lo coloca en un estado de inconsistencia de bucle, evitando que pase al estado de reenvío.
    
- **Previene bucles**: Al mantener el puerto en un estado bloqueado hasta que se restablezca la recepción de BPDUs, se evita la formación de bucles en la red .
    

### 🧠 Recomendaciones para evitar bucles

- **Utilizar switches con soporte para STP o RSTP**: Asegúrate de que todos los dispositivos en la red soporten y tengan habilitado STP o su versión mejorada, RSTP.
    
- **Evitar conexiones redundantes no controladas**: No conectes switches entre sí sin considerar la topología y sin mecanismos de control de bucles.
    
- **Configurar Loop Guard en puertos críticos**: Especialmente en puertos que podrían ser susceptibles a fallos unidireccionales.
    
- **Monitorear la red**: Utiliza herramientas de monitoreo para detectar cambios en la topología y posibles bucles.
    

Para una explicación más detallada sobre cómo STP gestiona los bucles y la elección del puente raíz, puedes consultar el siguiente video:

---

### 📘 Recomendaciones de buenas prácticas

- Usa **cables etiquetados** (cruzado, recto).
- Conoce el soporte de **auto-MDI/MDI-X** de tus switches.
- Evita conectar múltiples switches en anillo sin STP.
- Asegura la **configuración del protocolo Spanning Tree** en redes grandes.

---

### 📝 Para el examen

- Entiende la diferencia entre cables **crossover** y **straight-through**.
- Conoce las funciones de **uplink port** y **auto-MDI-X**.
- Reconoce los peligros de un **switch loop**.
- Identifica **BPDU** y **STP** como mecanismos de prevención.

---

### ✅ Conclusión

Conectar múltiples switches permite extender una red, pero también introduce riesgos como los bucles. Con las tecnologías actuales como **auto-MDI-X** y protocolos como **STP**, estos problemas pueden evitarse si se aplican correctamente. Saber esto no solo es útil para el examen, sino también para el diseño de redes profesionales.

