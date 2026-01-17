

---

# Modelo entidad–relación (ER)  
## Laboratorio SIEM

### Figura1. Diagrama Entidad-Relación

[[00_Titulaciones_Oficiales/00_01_CFGS_DAM/00_01_01_Proyecto_Laboratorio-SIEM/00_01_01_09_Anexos/Diagramas/01_ERD_Laboratorio_SIEM.excalidraw.md|01_ERD_Laboratorio_SIEM.excalidraw]]

---

## 1. Introducción

En este apartado se define el **modelo entidad–relación** del sistema Laboratorio SIEM. El objetivo es identificar las entidades principales, sus atributos y las relaciones entre ellas, de forma coherente con la arquitectura y el flujo funcional descritos en los capítulos anteriores.

El modelo se ha diseñado para:

- Almacenar eventos normalizados.
- Generar y gestionar alertas derivadas de reglas.
- Permitir trazabilidad entre eventos y alertas.
- Mantener un diseño simple y adecuado al alcance académico.

---

## Entidades principales

### • Event (Evento)

Representa un evento normalizado recibido por el sistema y almacenado para su análisis y consulta.

Rol en el sistema:

- Es la unidad base de información.
- Alimenta el motor de reglas.
- Permite auditoría y consulta histórica.

---

### • Alert (Alerta)

Representa una alerta generada cuando una o varias reglas se cumplen sobre un conjunto de eventos.

Rol en el sistema:

- Materializa el resultado del análisis.
- Permite seguimiento mediante estados.
- Se visualiza en el dashboard como elemento prioritario.

---

### • Rule (Regla)

Representa una regla de detección definida en el sistema.

Rol en el sistema:

- Define condiciones para generar alertas.
- Aporta trazabilidad: “esta alerta se generó por esta regla”.
- Permite ampliar o ajustar detecciones sin cambiar el modelo de datos.

Nota:

- La implementación puede ser estática (en código) o configurable (en base de datos). En ambos casos, se modela la entidad para dejar clara la lógica del sistema.

---

### • Source (Fuente)

Representa el origen lógico de un evento (por ejemplo: Linux, Windows, servicio de laboratorio).

Rol en el sistema:

- Identifica y agrupa eventos por procedencia.
- Facilita filtros y análisis.

---

## 2. Relación entre entidades

### • Source 1 — N Event

Una fuente puede generar múltiples eventos, pero cada evento pertenece a una única fuente.

---

### • Rule 1 — N Alert

Una regla puede generar múltiples alertas, pero cada alerta se asocia a una regla principal.

---

### • Event N — M Alert

Una alerta puede estar relacionada con múltiples eventos (por ejemplo, varios intentos fallidos), y un evento podría estar implicado en una alerta.

Para resolver esta relación se utiliza una entidad intermedia.

---

## 3. Entidad intermedia

### • AlertEvent (Relación Alerta–Evento)

Entidad de unión que permite asociar múltiples eventos a una alerta y mantener trazabilidad.

Rol en el sistema:

- Permite reconstruir qué eventos causaron una alerta.
- Facilita el detalle de alertas en el dashboard.

---

## 4. Diagrama ER (descripción textual y cardinalidades)

En el diagrama entidad–relación del Laboratorio SIEM se utilizan **cardinalidades** para indicar cuántas instancias de una entidad pueden relacionarse con instancias de otra entidad. Estas cardinalidades se expresan mediante los valores **1** (uno) y **N** (muchos).

De forma general:

- **1 — 1 (uno a uno)**  
    Una instancia de una entidad se relaciona con una única instancia de otra entidad.
    
- **1 — N (uno a muchos)**  
    Una instancia de una entidad puede relacionarse con múltiples instancias de otra entidad, pero no a la inversa.
    
- **N — M (muchos a muchos)**  
    Varias instancias de una entidad pueden relacionarse con varias instancias de otra entidad.  
    Este tipo de relación **requiere una entidad intermedia** para su correcta implementación en un modelo relacional.
    

---

### • Relación Source (1) —— (N) Event

Esta relación indica que:

- Una **fuente** (_source_) puede generar **múltiples eventos**.
    
- Cada **evento** pertenece a **una única fuente**.
    

En el contexto del sistema:

- Un sistema Linux o Windows puede generar muchos eventos a lo largo del tiempo.
    
- Un evento concreto siempre tiene un origen claramente identificado.
    

Esta relación se implementa mediante una **clave foránea** en la entidad Event que referencia a Source.

---

### • Relación Rule (1) —— (N) Alert

Esta relación expresa que:

- Una **regla** (_rule_) puede generar **múltiples alertas** a lo largo del tiempo.
    
- Cada **alerta** está asociada a **una única regla** que la ha originado.
    

En el sistema:

- Una misma regla de detección puede activarse en diferentes momentos.
    
- Cada alerta conserva la trazabilidad de la regla que la generó.
    

Esta relación permite analizar qué reglas generan más alertas y facilita la auditoría del sistema.

---

### • Relación Alert (1) —— (N) AlertEvent —— (N) Event (1)

Esta relación representa un caso de **muchos a muchos (N — M)** entre Alert y Event, resuelto mediante la entidad intermedia **AlertEvent**.

Su significado es el siguiente:

- Una **alerta** puede estar asociada a **varios eventos**  
    (por ejemplo, múltiples intentos fallidos de acceso).
    
- Un **evento** puede formar parte de **una o varias alertas**, según las reglas aplicadas.
    

Para modelar correctamente esta relación:

- Se introduce la entidad intermedia AlertEvent.
    
- Cada registro en AlertEvent vincula **una alerta concreta con un evento concreto**.
    

Este diseño permite:

- Mantener trazabilidad completa.
    
- Consultar el detalle de una alerta y los eventos que la originaron.
    
- Evitar duplicidad de datos y problemas de integridad.
    

---

### Justificación del uso de entidades intermedias

==En los modelos relacionales, las relaciones **N — M** no pueden implementarse directamente==. Por este motivo, se utilizan entidades intermedias que transforman la relación en dos relaciones **1 — N**.

En el Laboratorio SIEM, la entidad AlertEvent cumple esta función, garantizando:

- Claridad en el modelo.
    
- Escalabilidad.
    
- Coherencia con el diseño del sistema.
    

---

### Conclusión sobre las cardinalidades

El uso de estas relaciones y cardinalidades permite reflejar de forma precisa el comportamiento real del sistema, asegurando que el modelo de datos sea coherente, flexible y alineado con el flujo funcional del Laboratorio SIEM.

---

### Consideraciones de diseño

El modelo se ha diseñado con criterios de:

- Normalización y trazabilidad.
- Simplicidad estructural.
- Compatibilidad con consultas típicas del sistema:
- “Eventos recientes por fuente”
- “Alertas abiertas”
- “Detalle de alerta con eventos asociados”
- “Alertas generadas por regla”

---

## 5. Observaciones sobre los tipos de campos

Aunque el modelo entidad–relación no define tipos de datos concretos, es conveniente incluir algunas observaciones generales sobre el significado de los principales campos utilizados en las entidades del sistema, de cara a su correcta interpretación e implementación posterior.

### • Identificadores

- **Identificador** (*identifier / id*):  
  Campo utilizado como clave primaria para identificar de forma única cada registro dentro de una entidad.
  En la implementación podrá corresponder a un valor numérico incremental o a un identificador único universal (*UUID*).

- **Clave foránea** (*foreign key / FK*):  
  Campo que referencia al identificador de otra entidad, permitiendo establecer relaciones entre registros y garantizar la integridad referencial.

---

### • Campos temporales

- **Marca temporal** (*timestamp*):  
  Representa la fecha y hora en la que ocurre un evento o se genera una alerta. Es fundamental para el análisis cronológico y la reconstrucción de incidentes.

- **Fecha de creación** (*created_at*):  
  Indica el momento en el que un registro es almacenado en el sistema. Puede diferir de la marca temporal del evento.

- **Fecha de cierre** (*closed_at*):  
  Campo opcional utilizado para indicar cuándo una alerta ha sido gestionada y cerrada.

---

### • Clasificación y severidad

- **Tipo de evento** (*event type*):  
  Campo descriptivo que clasifica la naturaleza del evento (por ejemplo, intento de acceso fallido, acceso correcto, acción administrativa).

- **Severidad** (*severity*):  
  Indica el nivel de importancia o impacto asociado a un evento o alerta. Se utiliza para priorizar la atención y facilitar el filtrado de información relevante.

---

### • Estado

- **Estado** (*status*):  
  Campo utilizado principalmente en alertas para reflejar su situación actual, como abierta o cerrada. Permite simular el ciclo de vida básico de un incidente.

---

### • Campos descriptivos

- **Nombre** (*name*):  
  Identificador legible utilizado para describir reglas o fuentes de eventos.

- **Descripción** (*description*):  
  Campo de texto destinado a aportar contexto adicional, facilitando la comprensión del propósito de reglas y alertas.

---


