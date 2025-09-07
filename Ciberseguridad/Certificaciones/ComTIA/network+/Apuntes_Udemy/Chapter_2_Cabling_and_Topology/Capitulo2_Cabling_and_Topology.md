#certificacion #network #apuntes
# 🧩 Sección 1: Topologías de Red, Arquitecturas y Tipos

---

### 📌 Introducción

Una parte esencial del trabajo de un técnico de redes es el diseño de la red, especialmente su **topología**, que determina cómo se conectan los dispositivos entre sí y cómo se transmite la información. Existen dos tipos de topologías:

- **Topología física**: disposición física de los dispositivos y el medio de transmisión.
- **Topología lógica**: define cómo fluyen los datos por la red, sin importar la disposición física.

---

### 🛠️ Topologías físicas comunes

#### 🔗 Punto a punto
- Conecta **dos nodos directamente**.
- Puede usar cobre, fibra, serie, paralelo o enlaces inalámbricos.
- Simple y confiable.

#### ⭐ Estrella (Star / Hub-and-Spoke)
- Todos los nodos se conectan a un **dispositivo central** (switch, router, servidor).
- Común en redes LAN modernas.
- Fácil de gestionar y escalar.

![[star-topology.png]]

#### 🔄 Malla (Mesh)
- Cada nodo se conecta con todos los demás.
- Alta redundancia: múltiples rutas disponibles.
- Puede ser **total** (todos con todos) o **parcial** (algunos enlaces).

![[mesh-topology.jpg]]
#### 🧬 Híbrida
- Combinación de dos o más topologías físicas.
- Usada en redes grandes que necesitan adaptabilidad y segmentación por departamentos.
- Ej.: combinación de estrella, anillo y malla.

![[Hybrid-Topology-300x188.jpg]]

---

### 🧠 Topologías lógicas

#### 🏗️ Modelo jerárquico de tres niveles
Separación de funciones en 3 capas:

| Capa                     | Función principal                                                 |
| ------------------------ | ----------------------------------------------------------------- |
| **Capa de núcleo**       | Alta velocidad. Backbone de red. Conecta distribución con la WAN. |
| **Capa de distribución** | Filtrado, ACLs, enrutamiento interno, balanceo de carga.          |
| **Capa de acceso**       | Conecta usuarios finales. Aplica políticas QoS y protección L2.   |
![[three-tier-model.webp]]

- **ACLs**: listas de control de acceso para seguridad.
- Protocolos: OSPF, EIGRP, etc.

#### 🧩 Núcleo colapsado (Collapsed Core)
- Fusiona núcleo y distribución en un solo dispositivo (ej. router-switch de capa 3).
- Simplifica redes pequeñas y medianas.
![[collapsed-core-model.webp]]
#### 🌿 Spine-Leaf (Columna vertebral y hoja)
- Dos capas: conmutadores **spine** (capa 3) y **leaf** (capa 2).
- Ideal para centros de datos.
- Optimiza tráfico este-oeste (entre servidores).
- Baja latencia y alta disponibilidad.

![[spine-and-leaf-architecture-768x296.webp]]

---

### 📝 Conclusión

Comprender las topologías es clave para construir redes seguras, escalables y eficientes. Tanto el diseño físico como el lógico impactan en el rendimiento y la facilidad de mantenimiento de la red. El examen Network+ requiere conocer estas estructuras y saber cuándo usar cada una.

# 🧩 Sección 2: Cables Coaxiales

---

### 📌 Introducción

El **cable coaxial** es uno de los medios de transmisión más antiguos aún en uso, originado en la Segunda Guerra Mundial. Su diseño robusto y capacidad para resistir interferencias electromagnéticas lo hacen útil en entornos exigentes, aunque hoy en día ha sido en gran medida reemplazado por otros medios más flexibles y económicos.

---

### 🧪 Estructura del cable coaxial

Un cable coaxial está formado por 4 componentes principales:

1. **Conductor interno** (núcleo): transporta la señal.
2. **Aislante dieléctrico**: separa el núcleo del conductor exterior.
3. **Malla o blindaje externo**: actúa como tierra y protege contra EMI.
4. **Cubierta de PVC**: da forma y protección al cable.

![[coaxial-cable-structure.png]]

---

### 📏 Tipos de cable coaxial (grado RG)

- **RG-6**: estándar moderno más común. Impedancia de **75Ω**.
- **RG-59**: obsoleto.
- El **grado RG** determina el grosor, tipo de conductor y uso.

---

### 🔌 Tipos de conectores coaxiales

#### 🔸 Conector Tipo F
- El más utilizado actualmente.
- Conexión roscada con pin central.
- Usado en módems, cajas de TV por cable, etc.

![[f-type-connector.jpg]]
#### 🔸 Conector BNC
- Más antiguo, de tipo bayoneta.
- Conexión con giro y bloqueo.
- Aún presente en equipos antiguos o señales de video.

![[conector-bnc.jpg]]

---

### 🧯 Twinax (Twinaxial Cable)

- Similar al coaxial pero con **dos conductores internos** gemelos que comparten el mismo blindaje exterior.
- Se usa en **cables SFP+**, conexiones de alta velocidad y sistemas como SATA.
- Importante para el examen: **conocer que Twinax ≠ Coaxial**.

![[twinax-cable.webp]]

---

### ✅ Ventajas del cable coaxial

- Alta **resistencia a interferencias electromagnéticas (EMI)**.
- Alta **durabilidad física**.
- Útil en entornos con mucho ruido eléctrico.

### ⚠️ Desventajas

- **Rigidez**: difícil de instalar.
- **Costo elevado** en comparación con cables de par trenzado.
- Cada vez menos común en nuevas instalaciones.

---

### 📝 Puntos clave para el examen

- El tipo de cable **RG-6**, con **impedancia de 75Ω**, es el más común.
- Conector principal: **tipo F**.
- Diferenciar **coaxial** de **twinaxial**.
- Conocer las ventajas/desventajas del coaxial.

---
# 🧩 Sección 3: Twisted Pair Cabling

---

### 📌 Introducción

El **cable de par trenzado** es uno de los medios más comunes para redes actuales, incluyendo Ethernet y telefonía. Su diseño con **pares de hilos trenzados** reduce la interferencia electromagnética (EMI) y la diafonía, permitiendo una transmisión eficiente.

---

### 🧵 Tipos de par trenzado

#### 🔓 UTP (Unshielded Twisted Pair)
- No tiene blindaje externo.
- Común en oficinas, hogares, redes estándar.
- Longitud máxima: **100 metros**.
- Más económico y flexible.
- Usa conectores **RJ-45**.

![[utp-cable.jpg]]

#### 🛡️ STP (Shielded Twisted Pair)
- Posee un blindaje metálico (como papel aluminio).
- Ofrece mayor protección contra interferencias.
- Se utiliza en entornos industriales o con alto ruido eléctrico.

![[Portada-Para-Blog4-820x505.png]]

---

### 🔗 Conectores y estándares

- **RJ-45**: conector más utilizado para cables UTP/STP.
- **Normas TIA/EIA 568A y 568B**: definen el orden de colores de los cables en RJ-45.
- **Tipos de núcleo**:
  - **Sólido**: un solo hilo de cobre. Más rígido, usado en cableado estructurado.
  - **Trenzado**: múltiples hilos finos. Más flexible, ideal para cables de conexión.

---

### 📐 Clasificación por Categorías

| Categoría | Velocidad máxima           | Distancia | Comentario adicional                            |
|-----------|----------------------------|-----------|--------------------------------------------------|
| Cat 5     | 100 Mbps – 1 Gbps          | 100 m     | Obsoleta para nuevas instalaciones               |
| Cat 5e    | 1 Gbps                     | 100 m     | Mejor protección contra EMI que Cat 5           |
| Cat 6     | 10 Gbps (hasta 55 m)       | 55 m      | Alta velocidad, limitada en distancia            |
| Cat 6a    | 10 Gbps                    | 100 m     | Totalmente compatible con 10GBASE-T             |
| Cat 7     | 10+ Gbps                   | 100 m     | Protección EMI mejorada, más caro               |
| Cat 8     | 25–40 Gbps (hasta 30 m)    | 30 m      | Usado en centros de datos, cumple con 40GBASE-T |
![[cabling-utp-categories.png]]

---

### 📝 Consejos para el examen

- Diferenciar entre **UTP** y **STP**.
- Conocer bien las categorías **Cat 5 hasta Cat 8** y sus especificaciones.
- Reconocer que el **conector RJ-45** se utiliza para este tipo de cableado.
- Recordar que el límite típico es **100 m** para la mayoría de las categorías excepto Cat 6 (55 m) y Cat 8 (30 m).

---

### ✅ Conclusión

El cable de par trenzado sigue siendo el más usado en redes LAN gracias a su bajo coste, facilidad de instalación y soporte para altas velocidades. Para el examen, asegúrate de entender las diferencias entre tipos, conectores, categorías y usos óptimos.

---
# 🧩 Sección 4: Fiber Optic Cabling

---

### 📌 Introducción

El cableado de **fibra óptica** es clave en redes modernas que requieren gran velocidad, ancho de banda y alcance. A diferencia del cobre, la fibra utiliza **luz** para transmitir datos, lo que elimina interferencias electromagnéticas (EMI) y permite distancias más largas.

---

### 🔍 Estructura de un cable de fibra óptica

1. **Núcleo**: lleva la luz láser o LED.
2. **Revestimiento (Cladding)**: refleja la luz hacia el núcleo, permitiendo su propagación.
3. **Cubierta de protección**: aislamiento físico del conjunto.

![[fiber-optic-cable-structure.webp]]

---

### 🧪 Tipos de fibra óptica

| Tipo       | Fuente de luz | Color típico | Uso principal            | Distancia               |
|------------|---------------|--------------|---------------------------|--------------------------|
| **Multimodo** | LED           | Naranja/Aqua | Redes LAN, corta distancia | Hasta 600 m aprox.       |
| **Monomodo** | Láser         | Amarillo     | Larga distancia, WAN       | Hasta varios kilómetros  |

- El **multimodo** tiene núcleo más grueso y menor coste.
- El **monomodo** tiene núcleo más delgado y se usa para enlaces de gran alcance.

---

### 🔌 Conectores de fibra óptica

| Conector | Forma    | Método de conexión     | Observaciones                           |
|----------|----------|-------------------------|------------------------------------------|
| **ST**   | Redondo  | Empuje y giro (bayoneta) | Antiguo, aún presente                    |
| **SC**   | Cuadrado | Empuje directo           | Muy común en instalaciones actuales      |
| **FC**   | Redondo  | Enroscar                | Similar al ST, pero con rosca            |
| **LC**   | Miniatura| Alta densidad, push-pull | Dúplex compacto, muy común hoy en día    |
| **MT-RJ**| Recto    | Alta densidad, dúplex    | Parecido a RJ-45, ideal en poco espacio  |
![[fiber-connectors-types 1.webp]]

---

### 🧵 Duplex vs Simplex

- **Dúplex**: dos fibras en un solo conector, una para TX y otra para RX (común en redes).
- **Simplex**: una sola fibra, usado en algunas aplicaciones especiales.

![[duplex-vs-simplex.png]]

---

### 🎯 Tipos de pulido (polish)

| Tipo de pulido | Identificación | Forma del extremo | Pérdida de retorno | Comentarios                     |
|----------------|----------------|-------------------|--------------------|----------------------------------|
| **PC**         | Color azul     | Redondeado        | Media              | Estándar tradicional             |
| **UPC**        | Color azul     | Más redondeado    | Baja               | Menor pérdida de señal           |
| **APC**        | Color verde    | Angulado (8º)     | Muy baja           | Requiere precisión, alto rendimiento |
![[connector-polish-types.webp]]

---

### 📝 Claves para el examen

- **Multimodo** = LED, **Monomodo** = láser.
- Colores comunes: naranja (MM), amarillo (SM), aqua (OM3 MM).
- Conectores: **ST, SC, FC, LC, MT-RJ** → saber reconocer visualmente.
- Pulido: **PC, UPC, APC** → relacionar forma, color y pérdida de señal.

---

### ✅ Conclusión

La fibra óptica es esencial para redes modernas, especialmente en centros de datos y enlaces troncales. Dominar los tipos de cable, conectores y acabados te preparará para responder correctamente en el examen Network+ y diseñar infraestructuras de alto rendimiento.

---
# 🧩 Sección 5: Fire Ratings: Plenum vs. Non-Plenum

---

### 📌 Introducción

La **clasificación contra incendios del cableado de red** es un aspecto crítico en instalaciones seguras, especialmente en edificios comerciales. El material del recubrimiento de los cables afecta directamente su resistencia al fuego y la producción de gases tóxicos.

---

### 🔥 ¿Qué es un plenum?

- Un **plenum** es un espacio de aire entre un falso techo y el techo real, o entre un piso elevado y el suelo estructural.
- Se usa normalmente para sistemas **HVAC** (calefacción, ventilación, aire acondicionado).
- También se suele utilizar para el tendido de cables, aunque no fue diseñado con ese propósito.

![[plenum-space-diagram.jpg]]

---

### 🧯 Tipos de clasificaciones de cableado

| Clasificación     | Uso principal                            | Resistencia al fuego | Costo     | Comentario                           |
|-------------------|--------------------------------------------|------------------------|-----------|--------------------------------------|
| **Plenum (CMP)**   | Espacios de aire (techos, suelos falsos) | Alta                   | Alto      | Menor producción de humo tóxico      |
| **Riser (CMR)**    | Entre pisos (vertical)                   | Media                  | Moderado  | Requiere sellado con cortafuegos     |
| **PVC / Non-Plenum (CM)** | Uso general (horizontal, áreas abiertas) | Baja                   | Bajo      | Alto humo y gases si se quema        |

---

### 📦 ¿Cómo saber la clasificación?

- La clasificación aparece **impresa en la caja del cable** o en la **chaqueta exterior**.
- Ejemplos: `CMP`, `CMR`, `CM`, `PVC`.

![[cable-labeling-example.png]]


---

### ⚖️ Comparación práctica

- **Plenum**: Recomendado por normativas locales. Hasta 3 veces más caro. Más seguro.
- **Riser**: Común en instalaciones verticales, no tan restrictivo.
- **PVC**: Nunca debe usarse en plenums ni elevadores. Económico pero riesgoso en incendios.

---

### 🧪 Prueba de combustión (ejemplo visual)

![[burn-test-pvc-vs-plenum.webp]]

- **PVC**: Fuma rápidamente, libera gases nocivos.
- **Plenum**: Mucho más difícil de encender, menos humo.
## 🧠 Conceptos Clave

- **Plenum (CMP)**: Diseñado para espacios de manejo de aire (plenums), como falsos techos o suelos elevados. Ofrece la mayor resistencia al fuego y produce menos humo y gases tóxicos. Requiere materiales como FEP o PVC de baja emisión de humo.

- **Riser (CMR)**: Adecuado para instalaciones verticales entre pisos. Tiene una resistencia al fuego menor que el plenum y no debe usarse en espacios de manejo de aire.

- **LSZH (Low Smoke Zero Halogen)**: Produce una cantidad mínima de humo y no emite gases halógenos tóxicos al quemarse. Ideal para entornos donde la seguridad humana es prioritaria, como hospitales y túneles.

## 🔍 Comparativa Rápida

|Característica|Plenum (CMP)|Riser (CMR)|LSZH|
|---|---|---|---|
|Resistencia al fuego|Alta|Media|Alta|
|Emisión de humo|Baja|Alta|Muy baja|
|Emisión de gases tóxicos|Baja|Alta|Nula|
|Costo|Alto|Medio|Medio|
|Uso común|Espacios de manejo de aire|Instalaciones verticales|Entornos sensibles|

## 🛠️ Aplicaciones Recomendadas

- **Plenum**: Espacios donde el aire circula para sistemas HVAC. Obligatorio según códigos de construcción en muchas jurisdicciones.

- **Riser**: Instalaciones verticales entre pisos, como en edificios de oficinas.

- **LSZH**: Entornos donde la emisión de humo y gases tóxicos debe minimizarse, como en hospitales, túneles y áreas públicas cerradas.


## 📌 Notas Adicionales

- El uso de cables plenum en lugar de riser es aceptable, pero no al revés.

- LSZH no tiene una clasificación específica en el NEC, pero cumple con estándares europeos como IEC 60754 e IEC 61034.

- La elección del tipo de cable debe basarse en las regulaciones locales y las necesidades específicas del entorno de instalación.

---

### 📝 Puntos clave para el examen

- **CMP** (plenum) = mayor resistencia al fuego.
- **CMR** (riser) = para tendido entre pisos.
- **CM/PVC** = uso general, nunca en plenums o risers.
- Conocer **etiquetado y normativas locales**.

---

### ✅ Conclusión

La elección correcta de cableado no es solo una cuestión técnica, sino también de **seguridad**. Plenum ofrece la mayor protección y cumple con la mayoría de los códigos contra incendios. Saber identificar y aplicar correctamente estas clasificaciones es esencial tanto en el examen como en el entorno profesional.
