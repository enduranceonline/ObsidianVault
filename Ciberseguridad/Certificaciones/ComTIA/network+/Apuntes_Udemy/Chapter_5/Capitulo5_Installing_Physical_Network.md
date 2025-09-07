#certificacion #network #apuntes
# Capítulo 5 — Installing Physical Network  
## Session 1: Introduction to Structured Cabling

> **Nota:** El texto está redactado en español, manteniendo las **palabras clave** y nombres de estándares en **inglés** tal como los encontrarás en el examen **CompTIA Network+**.

---

### 1. ¿Por qué Structured Cabling?

Configurar una red Ethernet **ad‑hoc** es tan simple como conectar un **switch** a un **PC** con un cable UTP.  
Sin embargo, en un entorno corporativo esto genera problemas:

- Cables sueltos por el suelo → riesgo de tropiezos y daños.  
- Dificultad para escalar y documentar conexiones.  
- Complejo mantenimiento cuando se reorganiza la oficina.

La solución profesional es implementar un **sistema de Structured Cabling** (cableado estructurado) que normaliza la instalación y facilita la administración.

---

### 2. Componentes clave del Structured Cabling

Structured Cabling se organiza en **tres dominios principales**:

1. **Telecom Closet / Equipment Room**  
2. **Horizontal Run**  
3. **Work Area**

#### 2.1 Telecom Closet / Equipment Room

- Conocido también como **MDF (Main Distribution Frame)** o **IDF (Intermediate Distribution Frame)**.  
- Incluye **racks de 19″**, **switches**, **routers**, **patch panel** y fuentes de alimentación.  
- Norma TIA‑569 define dimensiones, ventilación y requisitos de seguridad.  
- **Backbone cabling** conecta el MDF con cada IDF usando fibra óptica o cobre de alta categoría (Cat6a/Cat7).

**Patch panel:**  
- Termina físicamente cada **Horizontal Run** (cable sólido Cat6/Cat6a).  
- Conexión mediante **punch‑down blocks** (110).  
- Etiquetado según **TIA‑606** para rastrear fácilmente cada puerto.

> ⚙️  *Tip*: El cable horizontal **no se toca** tras la instalación; todos los cambios se efectúan con **patch cords** (cables trenzados).

#### 2.2 Horizontal Run

- Segmento de hasta **90 m** de cable **solid core** (Cat5e/6/6a) que va desde el patch panel hasta el **Work Area Outlet**.  
- Debe respetar radio de curvatura, puntos de sujeción y separaciones respecto a líneas eléctricas (TIA‑569).  
- Opciones especiales:
  - **Plenum‑rated cable** (CMP) para falsos techos con flujo de aire.  
  - **Riser‑rated cable** (CMR) para conducciones verticales.  
- Se recomienda **firestopping** para mantener la resistencia al fuego de los muros.

#### 2.3 Work Area

- Punto final donde el usuario conecta su equipo.  
- Incluye la **face‑plate** (toma de pared) y el **Work Area Cable** (patch cord) hacia el PC, VoIP phone o impresora.  
- Norma TIA‑862 sugiere al menos **2 outlets** (data + voice) por 3,5 m de pared en oficinas.

---

### 3. Estándares TIA relevantes

| Norma            | Propósito principal                                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **ANSI/TIA‑568** | Especifica categorías de cable (Cat5e…Cat8), pin‑outs **T568A** y **T568B**, longitudes máximas y pruebas de certificación. |
| **TIA‑569**      | Canales, ductos y diseño de cuartos de telecomunicaciones.                                                                  |
| **TIA‑606**      | Esquema de **labeling** y documentación.                                                                                    |
| **TIA‑942**      | Requisitos de cableado para **data center**.                                                                                |

#### 3.1 Pin‑outs T568A vs T568B

| Par | Color T568A | Color T568B |
|-----|-------------|-------------|
| 1   | White/Green – Green | White/Orange – Orange |
| 2   | White/Orange – Orange | White/Green – Green |
| 3   | White/Blue – Blue   | White/Blue – Blue |
| 4   | White/Brown – Brown | White/Brown – Brown |

- **Straight‑through cable**: ambos extremos con el mismo pin‑out.  
- **Crossover cable**: un extremo T568A y el otro T568B (poco usado hoy gracias a *auto‑MDI/MDIX*).

---

### 4. Tipos de cable y prácticas de instalación

| Tipo de cable | Núcleo     | Uso                                   |
|---------------|-----------|---------------------------------------|
| **Solid core**| Sólido    | Horizontal Run (menor atenuación).   |
| **Stranded**  | Trenzado  | Patch cord (mayor flexibilidad).     |

**Buenas prácticas:**

- Mantener < 100 m (90 m horizontal + 10 m patch cords).  
- Respetar el **bend radius**: 4× diámetro del cable.  
- No exceder **25 lb (110 N)** de tensión al tirar.  
- Utilizar **Velcro** para el cable management; evitar bridas plásticas ajustadas.  
- Realizar **certificación** con un **cable tester** (Fluke DSX, etc.) que mida NEXT, RL, PSNEXT, delay‑skew.

---

### 5. Herramientas y materiales esenciales

- **Punch‑down tool (110/66)**  
- **Cable crimper (RJ‑45)**  
- **Cable tracer / toner probe**  
- **Cable tester & certifier**  
- **Label printer** (compliant con TIA‑606)  
- **Fish tape / cable pullers** para pasar cables en conduit.

---

### 6. Consejos para el examen Network+

1. Memoriza los **100 m** máximos de un cable channel (90 m + 10 m).  
2. Diferencia **MDF** (core) e **IDF** (distribución por planta).  
3. Reconoce la función de **patch panel** y por qué se usan **patch cords** stranded.  
4. Identifica las categorías de cable (Cat5e, Cat6, Cat6a) y su **bandwidth**.  
5. Comprende las normas **TIA‑568/T568A/T568B** y la capacidad de **auto‑MDI/MDIX** de los switches modernos.  
6. Conoce la diferencia entre **plenum** y **riser** cable.

---

*Fin de la Session 1. En la próxima sesión profundizaremos en la instalación de racks y el proceso de certificación de enlaces.*

## Session 2: Terminating Structured Cabling

---

### 1. Objetivo de la terminación

La **terminación** es el proceso de conectar de forma permanente los conductores de un **Horizontal Run** a:

1. Un **patch panel** en el **Telecom Closet** (MDF/IDF).  
2. Un **keystone jack** o **wall outlet** en la **Work Area**.

Una correcta terminación garantiza:

- Continuidad eléctrica y mínima pérdida (low attenuation).  
- Cumplimiento de la categoría (**Cat5e/Cat6/Cat6a**) en todo el enlace (**link**).  
- Facilidad de mantenimiento y cambios futuros (Moves, Adds, Changes).

---

### 2. Herramientas esenciales

| Herramienta           | Función                                   |
|-----------------------|-------------------------------------------|
| **110 Punchdown tool**| Inserta y corta cada conductor en el block 110. |
| **Cable stripper**    | Desnuda la chaqueta exterior sin dañar pares. |
| **Flush cutters**     | Recorta excedentes de conductor.          |
| **Cable tester/certifier** | Verifica continuidad, NEXT, RL, PSNEXT. |
| **Label printer**     | Identificación conforme a **TIA‑606**.    |

> ✔️ Consejo: usa puntas de repuesto para el punchdown; el filo se desgasta con el tiempo.

---

### 3. Terminación en el Patch Panel (Telecom Closet)

#### 3.1 Verificar la categoría

- Asegúrate de que **patch panel**, jack 110 y **cable solid core** comparten la misma **Cat rating** (ej. Cat6a).  
- Mezclar categorías degrada el rendimiento general (*weakest link*).

#### 3.2 Asignar el puerto

1. Identifica el puerto RJ‑45 frontal (p. ej. **Port 12**).  
2. Localiza el block 110 correspondiente en la parte trasera — normalmente numerado.

#### 3.3 Ordenar los conductores

- Sigue el esquema de colores **T568A** o **T568B** del patch panel.  
- Los bloques internos hacen la división de pares, por lo que los cables se colocan en orden lineal.

```
T568B (más común):
1 Blanco/Naranja
2 Naranja
3 Blanco/Verde
4 Azul
5 Blanco/Azul
6 Verde
7 Blanco/Marrón
8 Marrón
```

#### 3.4 Punchdown

1. Coloca cada conductor en la ranura correspondiente usando tus dedos.  
2. Orienta la **blade** de la punchdown tool de modo que el filo corte el sobrante hacia el canal lateral.  
3. Golpea perpendicularmente; deberías oír/ sentir un *click*.  
4. Repite con los ocho conductores.  
5. Verifica visualmente que el cobre quedó firmemente crimpado y sin pelado excesivo.

> 🔍 Mantén el **twist** hasta ≤ 13 mm (½ inch) del punto de terminación para preservar la impedancia y evitar **NEXT**.

#### 3.5 Gestión de cables

- Acomoda el cable en **cable management bars** y asegúralo con **Velcro**.  
- Etiqueta el cordón conforme a **TIA‑606** (ej. _FL‑01‑12_).

---

### 4. Terminación en el Wall Outlet (Work Area)

#### 4.1 Keystone jack

- Confirma **Cat rating** impresa en el jack (Cat6, Cat6a…).  
- Muchos keystones muestran los dos esquemas; selecciona **T568B** si tu patch panel está en B.

#### 4.2 Preparar el cable

1. Pela la chaqueta ± 3 cm.  
2. Quita cualquier **ripcord** o **cinta separadora**.  
3. Conserva el par trenzado lo máximo posible.

#### 4.3 Punchdown en el keystone

- Inserta pares según el código de colores.  
- Perfora con la punchdown tool (cuchilla hacia afuera).  
- Recorta sobrantes.  
- Cierra la cubierta protectora del jack y encájalo en la **face‑plate**.

#### 4.4 Ensamblar la placa de pared

- Atornilla la face‑plate a la caja de superficie o caja empotrada.  
- Coloca un **label** (ej. _FL‑01‑12_) para correlacionar con el puerto de patch panel.

---

### 5. Pruebas y certificación

| Prueba        | Parámetros clave                        | Límite Cat6   |
|---------------|-----------------------------------------|---------------|
| **Continuity**| Pin‑to‑pin correcto (1↔1, 2↔2…)         | *Pass/Fail*   |
| **Wire map**  | Sin *split‑pairs* ni inversión de pares | *Pass*        |
| **NEXT**      | Near‑End Crosstalk                      | ≤ 30 dB (100 MHz)|
| **RL**        | Return Loss                             | ≥ 19 dB       |
| **Delay‑Skew**| Diferencia de propagación entre pares   | ≤ 45 ns       |

- Usa un **certifier** (Fluke DSX, Viavi, AEM).  
- Imprime los reportes y archívalos; muchas garantías de fabricante requieren la certificación.

---

### 6. Errores comunes y cómo evitarlos

| Error                          | Impacto               | Solución                       |
|--------------------------------|-----------------------|--------------------------------|
| Exceder ½ inch de untwist      | Aumenta **NEXT**      | Mantén twist hasta el block.   |
| Cuchilla de punchdown invertida| Conductores sin cortar| Orienta filo hacia afuera.     |
| Categoría mixta (Cat5e + Cat6) | Pérdida de rendimiento| Mantén la misma Cat end‑to‑end.|
| Falta de strain relief         | Rotura a futuro       | Usa **cable saddles** y Velcro.|

---

### 7. Tips para el examen Network+

1. **110 Punchdown** se usa para **Permanent Links**; **crimpers RJ‑45** solo para **patch cords**.  
2. Diferencia entre **Patch panel** (Telecom Closet) y **Keystone jack** (Work Area).  
3. Memoriza la longitud máxima: **90 m Horizontal + 10 m Patch**.  
4. Reconoce la importancia de mantener el **twist** y usar la **blade** correcta.  
5. Comprende los parámetros de certificación (**NEXT, RL, Delay‑Skew**).

---

*Fin de la Session 2. La próxima sesión cubrirá Cable Testing avanzado y solución de problemas en instalaciones físicas.*

---
## Session 3: Equipment Room

---

### 1. ¿Qué es un Equipment Room?

El **Equipment Room** (sala de equipos) es el corazón del **Structured Cabling**:  
- Aloja el **MDF (Main Distribution Frame)** o, en plantas adicionales, los **IDF (Intermediate Distribution Frame)**.  
- Integra todos los enlaces **backbone**, la interconexión con el **Demarc** y los servicios de refrigeración y energía.

> 💡 **MDF**: punto central donde confluyen todas las conexiones externas (ISP, PSTN).  
> 💡 **IDF**: racks secundarios en otros pisos que distribuyen el cableado horizontal de cada planta.

---

### 2. Rack de 19 inches y la medida “U”

| Concepto   | Detalle                                                                          |
|------------|----------------------------------------------------------------------------------|
| **Rack 19″** | Estándar EIA‑310 para montar equipos de red y servidores.                       |
| **1 U**     | Unidad de altura = **1,75 inches** (44,45 mm).                                   |
| Distribución| Los equipos se especifican en múltiplos de U (ej. **1U switch**, **2U UPS**).     |

### Ejemplo de rack típico

```
| 1U  | Patch Panel (24‑ports)      |
| 1U  | Cable Management Bar       |
| 1U  | Core Switch                |
| 1U  | Development Router         |
| 1U  | Cable Management           |
| 1U  | Server 1U (Web/Dev)        |
| 1U  | Server 1U (Database)       |
| 5U  | NAS / File Server          |
| 2U  | UPS (Battery Backup)       |
```

---

### 3. Componentes esenciales del Equipment Room

| Componente          | Función clave                                            |
|---------------------|-----------------------------------------------------------|
| **Patch Panel**     | Termina los **Horizontal Runs** en bloques 110; facilita cambios. |
| **Cable Management**| Mantiene ordenados los **patch cords**; mejora flujo de aire. |
| **Switch**          | Conecta todos los dispositivos de la red local (LAN).    |
| **Router**          | Proporciona encaminamiento, NAT, acceso a Internet.      |
| **Servers**         | Servicios críticos: DHCP, DNS, File, Web, Virtualization.|
| **UPS**             | Energía ininterrumpida; evita apagados bruscos.          |
| HVAC                | Controla temperatura y humedad para fiabilidad.          |
| **Grounding**       | Protección contra descargas eléctricas y EMI.           |

---

### 4. Gestión del cableado

1. **Horizontal Cabling** llega al Patch Panel (cable **solid core Cat6/6a**).  
2. Se utilizan **patch cords** (**stranded**) para conectar cada puerto del Patch Panel al Switch.  
3. Los cables se enrutan por bandejas o **vertical managers** y se fijan con **Velcro**.  
4. Todo puerto se etiqueta según **TIA‑606** (ej. _ER‑01‑A12_).

> ⚠️ Mezclar cables sueltos con cables de alimentación incrementa **EMI**; mantén rutas separadas.

---

### 5. Demarc y Demarc Extension

| Término          | Descripción                                                     |
|------------------|-----------------------------------------------------------------|
| **Demarc**       | Punto donde finaliza la responsabilidad del proveedor y comienza la del cliente (TIP/Ring, ONU, NID, etc.). |
| **Demarc Extension** | Cableado adicional (cu‑)ubicado dentro de la empresa para acercar el servicio al Equipment Room. |

Ejemplo: el ISP deja un **coax splitter** en la sala técnica del edificio (Demarc).  
> Un **cable coax** adicional hasta tu MDF constituye la **Demarc Extension**, tras la cual instalas tu **cable modem**.

---

### 6. Buenas prácticas para Equipment Rooms

- **Power**: circuitos dedicados, UPS + generador (si procede).  
- **Cooling**: temperatura objetivo 18–27 °C; sensor de humedad (< 60 %).  
- **Security**: acceso restringido (badge, CCTV).  
- **Fire suppression**: sistemas sin agua (FM‑200, Inergen) preferidos.  
- **Housekeeping**: pasillos libres, cables etiquetados, documentación actualizada.  

---

### 7. Tips para el examen Network+

1. Diferencia **MDF** y **IDF** por su función y localización.  
2. Recuerda que un **rack** estándar es **19 inches** de ancho y la altura se mide en **U**.  
3. Comprende la separación entre **Demarc** y **Demarc Extension**.  
4. Identifica los elementos clave del rack: **Patch Panel → Cable Management → Switch → Router → Server → UPS**.  
5. Reconoce la importancia de **HVAC**, grounding y seguridad física en la fiabilidad de la red.  

---

*Fin de la Session 3. En la próxima sesión revisaremos Cable Testing avanzado y troubleshooting físico.*

## Session 4: Alternative Distribution Panels

---

### 1. Introducción

Aunque el bloque **110 Punchdown** es el estándar moderno para terminar cableado de cobre en redes de datos, existen **paneles de distribución alternativos** que todavía aparecen en instalaciones heredadas o en topologías específicas:

1. **66 Punchdown Block** – legado telefónico.  
2. **Fiber Distribution Panel (FDP)** – para enlaces **fiber‑optic**.  

Conocerlos ayuda a identificar y mantener infraestructuras mixtas durante migraciones a **VoIP** o **backbones** de alta velocidad.

---

### 2. 66 Punchdown Block (Legacy)

| Característica            | Detalle                                                  |
|---------------------------|----------------------------------------------------------|
| Origen                    | Instalaciones de telefonía analógica (POTS, PBX).        |
| Cable típico              | **25‑pair cable** (Amphenol) → telco color code.         |
| Estructura               | Filas dobles de terminales metálicos; seccionadas por fila.|
| Herramienta              | **66 Punchdown tool** (cuchilla distinta del 110).        |
| Limitaciones             | No cumple **Cat5e/Cat6** – no apto para Ethernet > 10 Mbps.|

### Uso híbrido con redes modernas
- A veces se reutiliza cableado existente haciendo **cross‑connect** entre un 66 block (telefonía) y un **110 Patch Panel** (datos).  
- Facilita coexistencia de **voice** (analógico) y **data** (Ethernet) en el mismo rack.

> ⚠️ Tendencia: el 66 block está desapareciendo por migración a **VoIP** y **SIP trunks**.

---

### 3. Fiber Distribution Panel (FDP)

| Elemento                | Función                                                      |
|-------------------------|--------------------------------------------------------------|
| **Adapter plate**       | Módulo con puertos **LC / SC / ST / MPO**.                   |
| **Splice tray**         | Aloja empalmes de fusión o mechero (**fusion splice**).      |
| **Cable management**    | Protege el radio de curvatura y numeración de fibras.        |
| **Patch cords (fiber)** | Conectan el FDP al **fiber switch**, **media converter** o **OTDR**.|

### Ventajas del FDP

1. **Organización**: Centraliza todas las fibras en un solo chasis.  
2. **Protección**: Evita micro‑curvaturas y suciedad de conectores ópticos.  
3. **Escalabilidad**: Se agregan placas MPO/MTP para **40 G / 100 G** enlaces troncal.  
4. **Documentación**: Etiquetado conforme a **TIA‑606** para seguimiento de circuitos ópticos.

> 💡 Para Network+: recuerda que la fibra **no** se termina con bloques 66/110, sino con **Fiber Patch Panels** que usan conectores **LC** o **SC**.

---

### 4. Comparativa rápida

| Panel                 | Medio           | Velocidad soportada | Uso actual                 |
|-----------------------|-----------------|---------------------|----------------------------|
| 66 Block              | Cobre (UTP)     | ≤ 10 Mbps (voz)     | Sistemas PBX heredados     |
| 110 Patch Panel       | Cobre (UTP)     | Hasta 10 GbE (Cat6a)| Estándar LAN cobre         |
| Fiber Distribution Panel | Fibra óptica | 1 Gb–400 Gb+        | Backbone, data center, WAN |

---

### 5. Buenas prácticas de instalación

- Mantener **bend radius** mínimo (fibra: 10× diámetro).  
- Limpieza de conectores ópticos con **one‑click cleaner** antes de insertar.  
- Documentar puertos y rutas en software de gestión de cableado.  
- Al migrar a VoIP, planificar la retirada de 66 blocks para liberar espacio de rack.  
- Mantener rutas separadas de **power** y **fiber** para evitar EMI y roturas.

---

### 6. Tips para el examen Network+

1. **66 Block** = telefonía analógica; no apto para Ethernet moderno.  
2. **110 Block** = cobre Cat5e/6/6a; sigue vigente para datos.  
3. **Fiber Distribution Panel** se usa con conectores **LC/SC/MPO**.  
4. Reconoce el concepto de **Demarc Extension** incluso en instalaciones de fibra.  
5. Comprende cómo voice y data pueden coexistir mediante cross‑connects entre 66 → 110 → Switch.

---

*Fin de la Session 4. Con esto concluye el capítulo sobre instalación física de redes en el plan de estudios de CompTIA Network+.*

---

## Session 5: Using a Toner and Probe

---

### 1. ¿Qué es un Tone Generator & Probe?

Un **Tone Generator & Probe** —también llamado **Fox & Hound** (marca registrada de Triplett)— sirve para **trazar** y **identificar** cables cuando las etiquetas faltan o se han perdido:

| Componente         | Función principal                                       |
| ------------------ | ------------------------------------------------------- |
| **Tone Generator** | Inyecta una señal audible (beep) en el conductor.       |
| **Probe**          | Detecta la señal y la reproduce por su altavoz interno. |

> Normalmente se usa para localizar un **Horizontal Run** específico dentro de un **Patch Panel**.

---

### 2. Conexiones físicas

1. Conecta el **RJ‑11** del Tone Generator al jack **RJ‑45** (encaja en los pares centrales).  
2. Usa **alligator clips** si necesitas sujetar pares sueltos.  
3. Desenergiza cualquier puerto **PoE** para evitar interferencias.

---

### 3. Procedimiento paso a paso

| Paso | Acción                                                                   |
|------|---------------------------------------------------------------------------|
| 1    | Desconecta el **switch** para suprimir tráfico y ruido.                  |
| 2    | Conecta el **Tone Generator** al jack de pared.                          |
| 3    | Acércate con la **Probe** al Patch Panel y recorre los pares.            |
| 4    | Escucha el beep más fuerte → cable identificado.                         |
| 5    | Etiqueta inmediatamente el puerto según **TIA‑606**.                     |

---

### 4. Buenas prácticas

- Verificar la batería del Tone Generator antes de usarlo.  
- Usar auriculares (jack de 3,5 mm) en ambientes ruidosos.  
- Mantener separados cables de energía para reducir EMI.  
- Etiquetar durante la instalación para minimizar futuras búsquedas.

---

### 5. Limitaciones

| Problema                         | Solución alternativa           |
|----------------------------------|--------------------------------|
| Cables muy largos (> 100 m)      | Utilizar **TDR**.             |
| Señal débil por PoE activo       | Desconectar PoE o puerto.      |
| Bundles densos (Cat6a)           | Separar los cables y volver a sonar.|

---

### 6. Otros usos del Tone & Probe

- Identificar pares en un **66 Block** o **110 Block**.  
- Rastrear coax con adaptador **F‑connector**.  
- Verificar continuidad en cables de alarma o audio.

---

### 7. Tips para el examen Network+

1. **Fox & Hound** = Tone Generator + Probe.  
2. El **RJ‑11** encaja en **RJ‑45** centrado en pares 4‑5.  
3. Siempre etiqueta conforme a **TIA‑606** tras localizar el cable.  
4. Para pruebas de distancia usa **TDR/OTDR**.  
5. Desconectar PoE evita interferencia en la Probe.

---

*Fin de la Session 5. Con esto dominas el rastreo de cables con Tone & Probe.*

---

## Session 6: Testing Cable

---

### 1. ¿Por qué es necesario el cable testing?

Instalar un sistema de **Structured Cabling** no garantiza que el enlace funcione a la velocidad deseada.  
Es imprescindible **verificar** cada **Horizontal Run** para asegurar:

- Correcto **wiremap** (pin‑out).  
- Continuidad eléctrica.  
- Longitud dentro de los **90 m** especificados por **TIA‑568**.  
- Rendimiento (NEXT, RL) acorde a la **Cat rating** comprada.

---

### 2. Herramientas de prueba

| Herramienta / Equipo           | Precio aprox. | Capacidades principales                      |
|--------------------------------|---------------|---------------------------------------------|
| **Basic Cable Tester**         | 30–100 USD    | Wiremap, Continuity (LEDs secuenciales).    |
| **Fluke MicroScanner / LinkIQ**| 500–1000 USD  | Wiremap, Continuity, TDR, Longitud, PoE.    |
| **Cable Certifier**            | 5 000–12 000 USD | Certificación Cat5e/Cat6/Cat6a (NEXT, RL, PSNEXT, Delay‑Skew). |

> 🔌 Todos los testers constan de **Main Unit** y **Remote Unit** para cubrir distancias de hasta 100 m.

---

### 3. Pruebas fundamentales

#### 3.1 Wiremap

- **Objetivo:** Confirmar que cada conductor termina en el pin correcto (1 ↔ 1, 2 ↔ 2…).  
- **Indicadores típicos:** LED en secuencia ascendente 1‑8 o diagrama en pantalla.  
- **Errores comunes:** *Open*, *Short*, *Split Pair*, *Cross Pair*.

#### 3.2 Continuity

- **Objetivo:** Detectar cortes o falta de conexión en uno o más conductores.  
- **Resultado esperado:** Todos los pares muestran **pass**.  
- **Síntoma de fallo:** LEDs apagados en los pares defectuosos.

#### 3.3 Length (TDR)

- **Herramienta:** **TDR (Time Domain Reflectometer)** integrado.  
- **Medición:** Rebote de pulso; calcula distancia a la reflexión (impedancia).  
- **Límite estándar:** ≤ 90 m (Permanent Link) + 10 m (Patch Cords).  
- **Aplicación en fibra:** **OTDR** (Optical TDR) mide pérdidas y empalmes.

---

### 4. Procedimiento de prueba paso a paso

| Paso | Acción                                                       |
|------|--------------------------------------------------------------|
| 1    | Desconectar equipos activos (Switch, PoE) del Patch Panel.   |
| 2    | Conectar **Main Unit** al extremo Work Area (jack de pared). |
| 3    | Conectar **Remote Unit** al puerto correspondiente del Patch Panel. |
| 4    | Seleccionar prueba **Wiremap + Length**.                     |
| 5    | Registrar resultados; si **fail**, reparar y volver a probar.|
| 6    | Etiquetar cable como **Passed** con fecha e iniciales.       |

---

### 5. Certificación avanzada

| Parámetro (Cat6) | Acrónimo | Límite      | Descripción                                         |
|------------------|----------|-------------|-----------------------------------------------------|
| Near‑End Crosstalk | **NEXT**| ≥ 30 dB     | Interferencia entre pares en el extremo local.      |
| Return Loss       | **RL**  | ≥ 19 dB     | Energía reflejada por impedancia no coincidente.    |
| Power‑Sum NEXT    | **PSNEXT**| ≥ 24 dB   | NEXT acumulativo de pares adyacentes.               |
| Delay Skew        | —        | ≤ 45 ns     | Diferencia de propagación entre pares.              |

Los **Cable Certifiers** generan un informe PDF que se adjunta a la garantía del instalador.

---

### 6. Interpretación de fallos frecuentes

| Resultado Tester          | Causa probable                      | Acción recomendada            |
|---------------------------|-------------------------------------|-------------------------------|
| *Open Pair 1‑2*           | Cable roto o pin suelto.            | Re‑terminar jack o patch panel.|
| *Split Pair 4‑5/3‑6*      | Pareado incorrecto en punchdown.    | Rehacer terminación siguiendo T568B. |
| **Length > 100 m**        | Ruta demasiado larga.               | Reubicar IDF o usar fibra.    |
| **NEXT Fail**             | Exceso de untwist, mala Cat mix.    | Mantener twist ≤ 13 mm, usar Cat uniforme.|

---

### 7. Tips para el examen Network+

1. **Wiremap** verifica pin‑out; **Continuity** verifica conexión física.  
2. **TDR/OTDR** mide longitud y localiza fallos en cobre y fibra.  
3. Límite **90 m** (Horizontal) + **10 m** (Patch) = **100 m** Channel.  
4. Parámetros de certificación clave: **NEXT, RL, PSNEXT**.  
5. Los instaladores entregan reporte de **Cable Certification**; el técnico debe saber interpretarlo.

---

*Fin de la Session 6. Con esto concluye la unidad de pruebas y certificación de cableado para CompTIA Network+.*

---

## Session 7: Troubleshooting Cabling – PART 1 (Work Area)

---

### 1. Enfoque de troubleshooting

Una caída de red rara vez se debe al **Structured Cabling**; sin embargo, cuando ocurre, conviene **proceder de fuera hacia dentro**:

1. **Work Area** (usuario).  
2. **Horizontal Cabling** (entre jack y Patch Panel).  
3. **Equipment Room** (Switch, Patch Panel, MDF/IDF).

Esta primera parte se centra en la **Work Area**.

---

### 2. Indicadores en el puesto de trabajo

| Síntoma                               | Verificación rápida                              |
|---------------------------------------|--------------------------------------------------|
| Icono “sin Internet” en Windows       | **Network & Sharing Center** → Sin redes activas |
| **Link light** apagado en NIC         | Comprueba **patch cord** y puerto del switch     |
| Ping 127.0.0.1 (loopback) fallido     | Posible driver NIC o deshabilitado en *Device Manager* |

```powershell
ping 127.0.0.1
```

Si responde, la **NIC** está operativa a nivel de pila TCP/IP local.

---

### 3. Checklist de la Work Area

1. **Patch cord** dañado:  
   - Dobladuras, grapas o pisotones de equipos de limpieza.  
   - Reemplazar por uno **Cat** igual o superior.

2. **Link light**:  
   - **Sólida** = enlace físico.  
   - **Parpadeo** = tráfico.  
   - **Apagada** = sin enlace → revisar cable/puerto.

3. **Device Manager** (Windows):  
   - NIC con flecha ↓ = **disabled**.  
   - Habilitar y probar de nuevo.

4. **Wall plate** floja o tironeada:  
   - Contactos IDC pueden soltarse.  
   - Re‑punch con herramienta 110 y nuevo **keystone** si es necesario.

5. **Loopback plug** (legacy):  
   - Plug físico que “devuelve” la señal a la NIC.  
   - Hoy poco común, pero **127.0.0.1** sigue siendo pregunta de examen.

---

### 4. Ejemplo de flujo de diagnóstico

1. Usuario reporta “sin Internet”.  
2. Técnico observa **link light** apagado.  
3. Cambia **patch cord** → luz sigue apagada.  
4. Revisa **wall plate**; cable arrancado — se vuelve a **punch down**.  
5. Link restablecido; etiqueta actualizada según **TIA‑606**.

---

### 5. Buenas prácticas

- **Cable management**: mantener cables fuera del paso de aspiradoras.  
- **Velcro**, no bridas plásticas, para evitar pellizcos.  
- Etiquetar jack y patch panel durante la instalación para evitar Fox & Hound posteriores.  
- Documentar incidentes para prevenir repeticiones.

---

### 6. Tips para el examen Network+

1. Loopback = **127.0.0.1**; confirma pila TCP/IP local.  
2. Empieza el troubleshooting en la **Work Area**, no en el **Equipment Room**.  
3. **Link light** apagada → problema físico (cable, puerto o NIC).  
4. Conocer diferencia entre **patch cord** (stranded) y **horizontal cable** (solid).  
5. Re‑terminar con herramienta **110 Punchdown** si el jack está dañado.

---

*Fin de la Session 7 – PART 1. La siguiente parte cubrirá pruebas en el Horizontal Cabling y Equipment Room.*

---


## Session 8: Troubleshooting Cabling – PART 2 (Equipment Room & Horizontal)

---

### 1. ¿Cuándo mirar fuera del Work Area?

* **Un solo usuario** sin red → culpa probable de **patch cord** o **wall plate** (ver PART 1).  
* **Todos los usuarios** conectados a un **switch** caen → problema en **Equipment Room**.  
* **Múltiples usuarios** de distintos switches → posible fallo de **backbone** o **facility power**.

> 📘 **Network+ ALERT:** Diferencia clave entre *one‑user‑down* vs *everyone‑down*.

---

### 2. Fallos en el Equipment Room

| Problema                    | Herramienta / Acción                              |
|-----------------------------|---------------------------------------------------|
| **Power outage / brownout** | Medir con **multimeter** AC voltage.              |
| **Voltage fluctuation log** | Instalar **voltage monitor** (24×7 logging).      |
| **Switch dead**             | Probar otra toma UPS; revisar **LED status**.     |
| **No backup during blackout** | Añadir **rack‑mount UPS** con SNMP alerts.     |

### Multimeter vs Voltage Monitor

* **Multimeter**: medición puntual de **AC/DC Voltage**, continuidad, resistencia.  
* **Voltage monitor**: registra picos y caídas; útil para problemas “a las 03:00 AM”.

---

### 3. Horizontal Cabling Issues

| Síntoma                          | Herramienta   | Interpretación                        |
|----------------------------------|---------------|---------------------------------------|
| Longitud anómala (10 m vs 70 m)  | **TDR**       | Corte a 10 m del Patch Panel.         |
| Pérdida intermitente / EMI       | **Cable certifier** | Re‑medir **NEXT/RL**.            |
| Caídas diarias a las 17 h        | Logs + TDR    | Ascensor/HVAC induce ruido.           |

```text
TDR reading: 9.8 m open
⇒ Break between conduit and ceiling tile.
```

---

### 4. Interference & Crosstalk

* **NEXT (Near‑End Crosstalk)** aumenta si se pierde el **twist** o se mezclan categorías.  
* Nuevas instalaciones mecánicas pueden introducir **EMI** tras la certificación.  
* **Time‑of‑day clues** en preguntas Network+: elevadores, motores, HVAC.

---

### 5. Herramientas recomendadas

| Herramienta            | Función                                           |
|------------------------|---------------------------------------------------|
| **Multimeter**         | Verificar 120/230 V AC, 12/5 V DC en PSUs.        |
| **Voltage Monitor**    | Registro continuo de voltaje y eventos.           |
| **TDR / OTDR**         | Localizar cortes y medir longitud.                |
| **Cable Certifier**    | NEXT, RL, PSNEXT; recertificar tras reformas.     |
| **Rack‑mount UPS**     | Protección eléctrica + SNMP trap.                 |

---

### 6. Flujo de diagnóstico sugerido

1. Verificar **power** del rack (UPS, breaker).  
2. Revisar **switch LEDs**.  
3. Medir salida AC en PDUs con multimeter.  
4. Usar **TDR** desde Patch Panel hacia jack sospechoso.  
5. Analizar logs de **voltage monitor** o SNMP.  
6. Re‑certificar cable si hay nueva fuente EMI.

---

### 7. Tips para el examen Network+

1. **Rack‑mount UPS** es defensa estándar en Equipment Room.  
2. **TDR** en cobre; **OTDR** en fibra.  
3. Eventos “a las 17 h” → piensa en **EMI** cíclico.  
4. Multimeter no mide NEXT; para eso usa **Cable Certifier**.  
5. Certificación inicial no cubre instalaciones posteriores de alto consumo.

---

*Fin de la Session 8 – PART 2. Continúa con documentación y mantenimiento preventivo.*

---

 
## Session 7: Troubleshooting Cabling – PART 1 (Work Area)

---

### 1. Enfoque de troubleshooting

Una caída de red rara vez se debe al **Structured Cabling**; sin embargo, cuando ocurre, conviene **proceder de fuera hacia dentro**:

1. **Work Area** (usuario).  
2. **Horizontal Cabling** (entre jack y Patch Panel).  
3. **Equipment Room** (Switch, Patch Panel, MDF/IDF).

Esta primera parte se centra en la **Work Area**.

---

### 2. Indicadores en el puesto de trabajo

| Síntoma                               | Verificación rápida                              |
|---------------------------------------|--------------------------------------------------|
| Icono “sin Internet” en Windows       | **Network & Sharing Center** → Sin redes activas |
| **Link light** apagado en NIC         | Comprueba **patch cord** y puerto del switch     |
| Ping 127.0.0.1 (loopback) fallido     | Posible driver NIC o deshabilitado en *Device Manager* |

```powershell
ping 127.0.0.1
```

Si responde, la **NIC** está operativa a nivel de pila TCP/IP local.

---

### 3. Checklist de la Work Area

1. **Patch cord** dañado:  
   - Dobladuras, grapas o pisotones de equipos de limpieza.  
   - Reemplazar por uno **Cat** igual o superior.

2. **Link light**:  
   - **Sólida** = enlace físico.  
   - **Parpadeo** = tráfico.  
   - **Apagada** = sin enlace → revisar cable/puerto.

3. **Device Manager** (Windows):  
   - NIC con flecha ↓ = **disabled**.  
   - Habilitar y probar de nuevo.

4. **Wall plate** floja o tironeada:  
   - Contactos IDC pueden soltarse.  
   - Re‑punch con herramienta 110 y nuevo **keystone** si es necesario.

5. **Loopback plug** (legacy):  
   - Plug físico que “devuelve” la señal a la NIC.  
   - Hoy poco común, pero **127.0.0.1** sigue siendo pregunta de examen.

---

### 4. Ejemplo de flujo de diagnóstico

1. Usuario reporta “sin Internet”.  
2. Técnico observa **link light** apagado.  
3. Cambia **patch cord** → luz sigue apagada.  
4. Revisa **wall plate**; cable arrancado — se vuelve a **punch down**.  
5. Link restablecido; etiqueta actualizada según **TIA‑606**.

---

### 5. Buenas prácticas

- **Cable management**: mantener cables fuera del paso de aspiradoras.  
- **Velcro**, no bridas plásticas, para evitar pellizcos.  
- Etiquetar jack y patch panel durante la instalación para evitar Fox & Hound posteriores.  
- Documentar incidentes para prevenir repeticiones.

---

### 6. Tips para el examen Network+

1. Loopback = **127.0.0.1**; confirma pila TCP/IP local.  
2. Empieza el troubleshooting en la **Work Area**, no en el **Equipment Room**.  
3. **Link light** apagada → problema físico (cable, puerto o NIC).  
4. Conocer diferencia entre **patch cord** (stranded) y **horizontal cable** (solid).  
5. Re‑terminar con herramienta **110 Punchdown** si el jack está dañado.

---

*Fin de la Session 7 – PART 1. La siguiente parte cubrirá pruebas en el Horizontal Cabling y Equipment Room