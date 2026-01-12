

---

# Gestión de alertas

## Laboratorio SIEM

---

## 1. Introducción

La gestión de alertas constituye el **último eslabón del backend** del Laboratorio SIEM. Una vez que los eventos han sido ingeridos, normalizados y analizados por el motor de reglas, las alertas generadas deben ser gestionadas de forma estructurada y persistente.

Este módulo se encarga de **dar contexto, estado y ciclo de vida** a las alertas, permitiendo que el sistema no solo detecte situaciones relevantes, sino que también las registre, consulte y mantenga de forma coherente a lo largo del tiempo.

---

## 2. Rol de la gestión de alertas en el sistema

La gestión de alertas actúa como el componente encargado de **organizar y mantener las alertas generadas** por el motor de reglas, asegurando que cada una tenga un estado claro y una relación trazable con los eventos que la originaron.

Sus funciones principales son:

- Registrar las alertas generadas por el motor de reglas.
    
- Asignar un estado inicial a cada alerta.
    
- Mantener la relación entre alertas, reglas y eventos.
    
- Permitir la actualización del estado de una alerta.
    
- Facilitar la consulta de alertas desde otros módulos del sistema.
    

Desde el punto de vista arquitectónico, este módulo se sitúa **después del motor de reglas** y **antes de la capa de presentación**, utilizando la base de datos como soporte central.

---

## 3. Concepto de alerta en el Laboratorio SIEM

En el contexto del Laboratorio SIEM, una **alerta** representa una **entidad persistente** que indica que el sistema ha identificado una situación relevante tras aplicar una regla de análisis sobre uno o varios eventos almacenados.

A diferencia de los eventos, que reflejan hechos individuales ocurridos en los sistemas monitorizados, una alerta es el **resultado del proceso de correlación y evaluación lógica** llevado a cabo por el motor de reglas. Por tanto, la alerta constituye un nivel de abstracción superior, orientado a destacar situaciones que requieren atención.

Desde el punto de vista del diseño, una alerta:

- Se genera exclusivamente como consecuencia de la **evaluación de una regla activa**.
    
- Está **respaldada por uno o varios eventos** que justifican su creación.
    
- Se almacena de forma persistente en la base de datos como una entidad independiente.
    
- Mantiene relaciones explícitas con la regla que la originó y con los eventos implicados.
    

Cada alerta se caracteriza por los siguientes elementos:

- **Regla asociada**  
    La alerta referencia la regla que se ha cumplido, lo que permite identificar qué condición lógica ha motivado su generación.
    
- **Conjunto de eventos relacionados**  
    A través de la tabla de relación correspondiente, la alerta mantiene el vínculo con los eventos que han provocado su activación, permitiendo explicar su origen.
    
- **Nivel de severidad**  
    La severidad de la alerta se deriva de la regla aplicada y permite clasificar su importancia dentro del sistema.
    
- **Estado**  
    El estado indica la situación actual de la alerta dentro de su ciclo de vida, diferenciando entre alertas abiertas y cerradas.
    
- **Información temporal**  
    La alerta registra el momento en que fue creada y, opcionalmente, el momento en que fue cerrada, facilitando el análisis histórico.
    

Este enfoque permite tratar las alertas como **entidades con identidad propia**, dotadas de contexto, trazabilidad y ciclo de vida definido, alineadas con el modelo de datos y con el funcionamiento del motor de reglas.

---

### Ejemplo conceptual de alerta

A modo de ejemplo, puede considerarse la siguiente situación dentro del laboratorio:

- Se reciben varios eventos de tipo _intento de autenticación fallido_ desde una máquina Linux.
    
- El motor de reglas evalúa una regla que detecta múltiples fallos de autenticación en un intervalo determinado.
    
- Al cumplirse la condición definida por la regla, se genera una alerta asociada a dicha regla.
    
- La alerta se registra en la base de datos y se vincula con los eventos que han provocado su activación.
    

Este ejemplo ilustra cómo la alerta no existe de forma aislada, sino como resultado directo de la interacción entre eventos, reglas y persistencia de datos.

---

## 4. Ciclo de vida de una alerta

El ciclo de vida de una alerta en el Laboratorio SIEM se ha diseñado de forma **intencionadamente simple**, acorde al alcance académico del proyecto y a la funcionalidad requerida.

El objetivo del ciclo de vida es permitir un seguimiento claro del estado de cada alerta, desde su generación hasta su cierre, evitando ambigüedades o estados intermedios innecesarios.

---

### 4.1 Estados de una alerta

Se definen los siguientes estados básicos:

- **OPEN**  
    Estado inicial asignado automáticamente a una alerta en el momento de su creación. Indica que la situación detectada está pendiente de revisión o análisis.
    
- **CLOSED**  
    Estado que indica que la alerta ha sido revisada y se considera resuelta, descartada o finalizada dentro del contexto del laboratorio.
    

Estos estados se almacenan de forma persistente en la base de datos y permiten clasificar las alertas según su situación actual.

---

### 4.2 Transición entre estados

Las transiciones entre estados siguen un modelo simple y determinista:

- Toda alerta se crea en estado `OPEN`.
    
- Una alerta puede cambiar su estado a `CLOSED` como resultado de una acción de gestión.
    
- Una vez cerrada, una alerta no puede volver a abrirse dentro del alcance del sistema.
    

Este modelo de transición:

- Evita inconsistencias en el estado de las alertas.
    
- Facilita la consulta de alertas abiertas y cerradas.
    
- Simplifica la lógica del backend y del frontend.
    

Al mantener un ciclo de vida reducido y explícito, el sistema garantiza un comportamiento predecible y coherente con los objetivos del Laboratorio SIEM.

---

## 5. Persistencia y trazabilidad de alertas

La gestión de alertas del Laboratorio SIEM se apoya de forma directa en el **modelo relacional de la base de datos**, que actúa como elemento central de persistencia y trazabilidad del sistema.

Desde el punto de vista del diseño, las alertas no se manejan como elementos temporales ni como simples resultados de ejecución, sino como **entidades persistentes**, almacenadas y consultables a lo largo del tiempo.

Para ello, el sistema utiliza principalmente las siguientes tablas:

- **`alerts`**  
    Almacena la información principal de cada alerta, incluyendo la regla que la ha generado, su severidad, su estado y los datos temporales asociados.
    
- **`alert_events`**  
    Actúa como tabla de relación entre alertas y eventos, permitiendo asociar cada alerta con uno o varios eventos concretos que justifican su generación.
    

Esta estructura permite:

- **Identificar la causa lógica de una alerta**, a través de la regla asociada.
    
- **Reconstruir el contexto de una alerta**, consultando los eventos que la originaron.
    
- **Mantener un histórico completo** de alertas abiertas y cerradas, independiente del ciclo de ejecución del motor de reglas.
    

Gracias a la persistencia de esta información, el sistema garantiza que todas las decisiones tomadas por el backend puedan ser **explicadas, auditadas y revisadas posteriormente**, incluso cuando los eventos ya no sean recientes.

---

## 6. Relación con otros componentes del backend

El módulo de gestión de alertas se integra con el resto del backend del Laboratorio SIEM siguiendo un modelo de responsabilidades claramente definidas.

Su relación con otros componentes es la siguiente:

- **Motor de reglas**  
    El motor de reglas es el único componente autorizado a generar nuevas alertas. Una vez evaluadas las condiciones de una regla, el motor delega en el módulo de gestión de alertas el registro y mantenimiento de la alerta generada.
    
- **Base de datos**  
    La base de datos actúa como repositorio persistente tanto del estado actual de las alertas como de su historial. El módulo de gestión de alertas es responsable de mantener la coherencia de esta información.
    
- **API interna del backend**  
    La gestión de alertas expone los datos necesarios para que otros módulos, como la interfaz web, puedan consultar el estado de las alertas o acceder a su detalle sin interactuar directamente con la lógica del motor de reglas.
    

Este diseño permite desacoplar el **análisis de eventos** de la **gestión del resultado**, reforzando la separación de responsabilidades y facilitando la evolución del sistema.

---

## 7. Alcance funcional del módulo de gestión de alertas

El módulo de gestión de alertas del Laboratorio SIEM presenta un alcance funcional **limitado pero claramente definido**, alineado con los objetivos del proyecto y con el resto del backend.

Dentro de su alcance se incluyen las siguientes funcionalidades:

- Registro persistente de las alertas generadas por el motor de reglas.
    
- Asignación y mantenimiento del estado de cada alerta.
    
- Consulta de alertas en función de su estado (abiertas o cerradas).
    
- Acceso al detalle de una alerta, incluyendo los eventos asociados.
    

Quedan explícitamente fuera del alcance del módulo:

- Asignación de alertas a usuarios o grupos.
    
- Priorización automática, escalado o workflows de resolución.
    
- Gestión de comentarios, anotaciones o historiales complejos.
    
- Integración con sistemas externos de ticketing o notificación.
    

Esta delimitación funcional permite mantener el módulo enfocado en su propósito principal: **registrar y estructurar las alertas**, sin introducir mecanismos propios de plataformas SIEM de gran escala.

---

## 8. Consideraciones de diseño del módulo

El diseño del módulo de gestión de alertas se apoya en una serie de consideraciones técnicas que condicionan su comportamiento y su integración con el sistema.

- **Modelo de estados simple y explícito**  
    El uso de un número reducido de estados evita ambigüedades y simplifica tanto la lógica del backend como la visualización posterior.
    
- **Trazabilidad como requisito central**  
    Cada alerta debe poder explicarse a partir de:
    
    - la regla que la generó,
        
    - los eventos que la provocaron,
        
    - y el momento en que se produjo.
        
- **Persistencia como principio de diseño**  
    No existen alertas únicamente en memoria o derivadas de ejecuciones temporales; toda alerta relevante queda registrada en la base de datos.
    
- **Preparación para consumo por el frontend**  
    La información almacenada sobre las alertas  está estructurada para ser fácilmente consultada y mostrada por la interfaz web, sin necesidad de transformaciones complejas.
    

Estas consideraciones garantizan un diseño coherente, mantenible y alineado con el enfoque académico del Laboratorio SIEM.

---

## 9. Limitaciones del módulo de gestión de alertas

El módulo presenta una serie de limitaciones asumidas conscientemente:

- No se gestionan flujos complejos de resolución.
    
- No existe reapertura de alertas.
    
- No se implementan políticas avanzadas de priorización.
    
- No se contemplan integraciones externas.
    

Estas limitaciones son coherentes con el carácter académico del Laboratorio SIEM y dejan abiertas posibles ampliaciones futuras.

---