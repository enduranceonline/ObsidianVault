#PostgreSQL

---

# Esquema de base de datos

## Laboratorio SIEM

---

## Introducción

En este apartado se define el **esquema físico de la base de datos** del Laboratorio SIEM, derivado directamente del modelo entidad–relación presentado en el apartado anterior.

Se detallan las tablas que componen el sistema, sus campos, tipos de datos recomendados, índices y restricciones, con el objetivo de disponer de un diseño **implementable**, **coherente** y **alineado con el alcance académico del proyecto**.

El diseño de la base de datos debe permitir:

- Persistir eventos y alertas de forma estructurada.
    
- Mantener trazabilidad completa entre fuentes, eventos, reglas y alertas.
    
- Realizar consultas habituales del sistema de forma eficiente.
    
- Servir como base para el desarrollo del backend y la interfaz web.
    

---

## Gestor de base de datos

Se utilizará un **sistema gestor de bases de datos relacional (RDBMS)**, concretamente:

**PostgreSQL**

### Justificación de la elección

PostgreSQL se ha seleccionado por los siguientes motivos:

- Soporte sólido de **integridad referencial** y restricciones.
    
- Tipos de datos avanzados (por ejemplo, `JSONB`) útiles para metadatos de eventos.
    
- Buen rendimiento en consultas estructuradas.
    
- Amplia adopción en entornos reales y educativos.
    
- Adecuación tanto para desarrollo local como para despliegues más avanzados.
    

No se contemplan bases de datos NoSQL, ya que el modelo del sistema es claramente relacional y prioriza la trazabilidad entre entidades.

---

## Criterios generales de diseño

Antes de definir las tablas, se establecen los siguientes criterios:

- Todas las tablas disponen de un **identificador único (PK)**.
    
- Se utilizan **claves foráneas** para reflejar las relaciones del modelo ER.
    
- Se incluyen **campos temporales** para trazabilidad y auditoría.
    
- Los índices se definen pensando en las consultas más habituales del sistema.
    
- La lógica compleja (validaciones avanzadas) se delega al backend, no a la base de datos.
    

---

## Convenciones y notación del esquema de base de datos

Antes de describir las tablas del sistema, es necesario aclarar la **notación utilizada para definir los campos**, así como el significado de los distintos tipos de claves y tipos de datos empleados en el esquema.

Esta explicación permite interpretar correctamente definiciones como:

```
id (PK) — UUID
```

---

### Notación general de los campos

Cada campo de una tabla se describe siguiendo la siguiente estructura:

```
nombre_del_campo (tipo_de_clave) — tipo_de_dato
```

Donde cada parte tiene un significado concreto.

---

### Nombre del campo

La parte situada a la izquierda indica el **nombre del campo** tal y como se define en la base de datos.

Ejemplos:

- `id`
    
- `source_id`
    
- `created_at`
    

Se utilizan nombres en **inglés**, en **minúsculas** y con **snake_case**, siguiendo una convención ampliamente extendida en bases de datos relacionales y especialmente común en PostgreSQL.

Esta convención:

- mejora la legibilidad,
    
- evita conflictos con palabras reservadas,
    
- y facilita la interoperabilidad con lenguajes de programación.
    

---

### Tipo de clave (PK, FK)

La parte entre paréntesis indica el **rol del campo dentro de la tabla**.

#### • PK (Primary Key – Clave primaria)

Indica que el campo es la **clave primaria** de la tabla.

Ejemplo:

```
id (PK)
```

Una clave primaria:

- Identifica de forma **única** cada registro.
    
- No puede ser nula.
    
- No puede repetirse.
    
- Permite que otras tablas referencien ese registro.
    

Todas las tablas del sistema disponen de una clave primaria, lo que garantiza la identificación inequívoca de cada entidad.

---

#### • FK (Foreign Key – Clave foránea)

Indica que el campo es una **clave foránea**, es decir, un campo que referencia a la clave primaria de otra tabla.

Ejemplo:

```
source_id (FK → sources.id)
```

Una clave foránea:

- establece una relación entre tablas,
    
- garantiza integridad referencial,
    
- impide referencias a registros inexistentes.
    

En este esquema, las claves foráneas reflejan directamente las relaciones definidas en el modelo entidad–relación.

---

### Tipo de dato

La parte situada a la derecha del guion (`—`) indica el **tipo de dato recomendado**, según PostgreSQL.

Ejemplo:

```
— UUID
```

Los tipos de datos definen:

- qué tipo de información puede almacenarse,
    
- cómo se almacena internamente,
    
- y cómo puede consultarse posteriormente.
    

---

### Tipos de datos utilizados en el esquema

A continuación se describen los principales tipos de datos empleados.

#### • UUID (Universally Unique Identifier)

Se utiliza como identificador principal en todas las tablas.

Características:

- valor único a nivel global,
    
- no depende de un contador incremental,
    
- adecuado para sistemas distribuidos o simulaciones realistas.
    

El uso de `UUID` evita colisiones y permite generar identificadores desde la aplicación sin depender de la base de datos.

---

#### • VARCHAR

Se utiliza para almacenar cadenas de texto de longitud variable.

Ejemplos de uso:

- nombres de fuentes,
    
- tipos de eventos,
    
- estados de alertas.
    

Es adecuado para campos cortos y descriptivos.

---

#### • TEXT

Se utiliza para almacenar texto de longitud libre.

Ejemplos de uso:

- descripciones,
    
- mensajes de eventos,
    
- condiciones de reglas.
    

No impone un límite estricto de tamaño y es adecuado para contenido descriptivo.

---

#### • SMALLINT

Se utiliza para valores numéricos pequeños.

En este esquema se emplea para:

- niveles de severidad.
    

Permite representar prioridades de forma eficiente y fácilmente comparable.

---

#### • BOOLEAN

Se utiliza para valores lógicos (`true` / `false`).

Ejemplo:

- habilitación o deshabilitación de reglas.
    

---

#### • TIMESTAMP

Se utiliza para representar fechas y horas.

Ejemplos:

- momento en que ocurre un evento,
    
- fecha de creación de registros,
    
- fecha de cierre de alertas.
    

Es fundamental para el análisis temporal y la trazabilidad.

---

#### • JSONB (PostgreSQL)

Tipo específico de PostgreSQL para almacenar datos en formato JSON.

Se utiliza en el esquema para:

- metadatos de eventos no estructurados.
    

Permite:

- flexibilidad en el almacenamiento,
    
- búsquedas eficientes dentro del contenido JSON,
    
- mantener el modelo relacional sin perder información adicional.
    

---

### Campos obligatorios y opcionales

Cuando un campo se marca como **nullable**, indica que puede no contener valor.

Ejemplo:

```
description — TEXT (nullable)
```

Esto significa que:

- el campo es opcional,
    
- el registro puede existir sin ese dato,
    
- y la lógica de aplicación decide cuándo utilizarlo.
    

Los campos no marcados como nullable se consideran obligatorios.

---

## Relación entre notación y modelo ER

La notación utilizada en este apartado traduce directamente el **modelo entidad–relación** al **esquema físico** de la base de datos.

- Las entidades del ER se convierten en tablas.
    
- Las relaciones se implementan mediante claves foráneas.
    
- Las cardinalidades se reflejan mediante restricciones y tablas de unión.
    

De este modo, el esquema físico mantiene coherencia total con el diseño conceptual del sistema.

---

## Tablas del sistema

En este apartado se describen las tablas que componen la base de datos del Laboratorio SIEM. Para cada tabla se explica su finalidad dentro del sistema, así como el significado de sus campos principales, los tipos de datos utilizados y las restricciones aplicadas.

El diseño sigue criterios de claridad, normalización y trazabilidad, priorizando la comprensión del modelo frente a optimizaciones avanzadas que quedan fuera del alcance académico del proyecto.

---

### • sources

**Propósito:**  
La tabla `sources` almacena las **fuentes lógicas** desde las que se generan los eventos que llegan al sistema. Una fuente representa el origen conceptual de un evento, como puede ser un sistema operativo, un servicio o una aplicación concreta.

Esta tabla permite identificar y agrupar los eventos según su procedencia, facilitando el análisis posterior y la aplicación de reglas de detección.

**Campos:**

- `id` (PK) — `UUID`  
    Identificador único de la fuente. Se utiliza como clave primaria y permite referenciar la fuente desde otras tablas de forma inequívoca.
    
- `name` — `VARCHAR`  
    Nombre descriptivo de la fuente (por ejemplo, _Linux_, _Windows_). Se utiliza para identificar la fuente de forma legible para el usuario.
    
- `type` — `VARCHAR`  
    Tipo de fuente, que permite clasificarla según su naturaleza (sistema operativo, servicio, aplicación, etc.).
    
- `description` — `TEXT` (nullable)  
    Campo opcional destinado a incluir  información adicional sobre la fuente.
    
- `created_at` — `TIMESTAMP`  
    Fecha y hora en la que la fuente se registra en  el sistema.
    

**Restricciones:**

- Se establece una restricción `UNIQUE(name)` para evitar la creación de fuentes duplicadas con el mismo nombre.
    

---

### • events

**Propósito:**  
La tabla `events` almacena los **eventos normalizados** que recibe el sistema desde las distintas fuentes. Un evento representa una acción o suceso relevante ocurrido en el entorno de laboratorio.

Esta tabla constituye la base del sistema, ya que los eventos son el punto de partida tanto para el análisis mediante reglas como para la generación de alertas.

**Campos:**

- `id` (PK) — `UUID`  
    Identificador único del evento.
    
- `timestamp` — `TIMESTAMP`  
    Fecha y hora en la que el evento ocurrió en el  sistema origen. Este campo permite realizar análisis cronológicos y reconstruir secuencias de eventos.
    
- `source_id` (FK → sources.id) — `UUID`  
    Clave foránea que indica la fuente desde la que se ha generado el evento. Garantiza la trazabilidad del evento hacia su origen.
    
- `event_type` — `VARCHAR`  
    Tipo de evento, utilizado para clasificarlo (por ejemplo, autenticación, error de sistema, acceso denegado).
    
- `severity` — `SMALLINT`  
    Nivel de severidad asignado al evento, que  permite priorizar su análisis.
    
- `message` — `TEXT`  
    Mensaje principal del evento, normalmente descriptivo del suceso ocurrido.
    
- `metadata` — `JSONB` (nullable)  
    Campo opcional para almacenar información adicional no estructurada asociada al evento. El uso de `JSONB` en PostgreSQL permite flexibilidad sin romper el modelo relacional.
    
- `created_at` — `TIMESTAMP`  
    Fecha y hora en la que el evento se almacena en la base de datos.
    

**Índices recomendados:**

- Índice por `timestamp`, para consultas de eventos recientes.
    
- Índice compuesto por `(source_id, timestamp)`, para filtrar eventos por fuente y periodo temporal.
    
- Índice por `event_type`, para facilitar búsquedas por tipo de evento.
    

**Restricciones:**

- El campo `source_id` es obligatorio, ya que todo evento debe estar asociado a una fuente válida.
    

---

### • rules

**Propósito:**  
La tabla `rules` representa las **reglas de detección** definidas en el sistema. Estas reglas establecen las condiciones bajo las cuales se generan alertas a partir de los eventos almacenados.

Aunque la lógica de evaluación de las reglas se implemente en el backend, esta tabla permite mantener un registro claro y trazable de las reglas existentes.

**Campos:**

- `id` (PK) — `UUID`  
    Identificador único de la regla.
    
- `name` — `VARCHAR`  
    Nombre descriptivo de la regla, utilizado para su identificación.
    
- `description` — `TEXT`  
    Explicación del propósito de la regla.
    
- `condition` — `TEXT`  
    Representación textual de la condición lógica  que define la regla.
    
- `severity` — `SMALLINT`  
    Nivel de severidad asociado a las alertas  generadas por la regla.
    
- `enabled` — `BOOLEAN`  
    Indica si la regla está activa o desactivada.
    
- `created_at` — `TIMESTAMP`  
    Fecha de creación de la regla.
    

**Restricciones:**

- Se establece una restricción `UNIQUE(name)` para evitar reglas duplicadas.
    

---

### • alerts

**Propósito:**  
La tabla `alerts` almacena las **alertas generadas** como resultado de la evaluación de eventos mediante las reglas definidas.

Una alerta representa una situación que requiere atención y constituye el principal elemento visible para el usuario en la interfaz web.

**Campos:**

- `id` (PK) — `UUID`  
    Identificador único de la alerta.
    
- `rule_id` (FK → rules.id) — `UUID`  
    Clave foránea que indica la regla que originó la alerta.
    
- `status` — `VARCHAR`  
    Estado de la alerta (por ejemplo, _OPEN_ o _CLOSED_).
    
- `severity` — `SMALLINT`  
    Nivel de severidad de la alerta.
    
- `description` — `TEXT`  
    Descripción de la alerta generada.
    
- `created_at` — `TIMESTAMP`  
    Fecha y hora de creación de la alerta.
    
- `closed_at` — `TIMESTAMP` (nullable)  
    Fecha de cierre de la alerta, si procede.
    

**Índices recomendados:**

- Índice por `(status, created_at)` para priorizar alertas abiertas.
    
- Índice por `rule_id` para análisis por regla.
    

**Restricciones:**

- El campo `rule_id` es obligatorio.
    
- El campo `closed_at` solo tiene sentido cuando la alerta se encuentra cerrada, lo cual se controla desde la lógica de la aplicación.
    

---

### • alert_events

**Propósito:**  
La tabla `alert_events` actúa como **tabla de unión** para resolver la relación muchos a muchos entre alertas y eventos.

Permite asociar múltiples eventos a una misma alerta y, a su vez, que un evento pueda formar parte de diferentes alertas.

**Campos:**

- `id` (PK) — `UUID`  
    Identificador único del registro.
    
- `alert_id` (FK → alerts.id) — `UUID`  
    Referencia a la alerta asociada.
    
- `event_id` (FK → events.id) — `UUID`  
    Referencia al evento asociado.
    
- `created_at` — `TIMESTAMP`  
    Fecha en la que se establece la relación.
    

**Índices y restricciones:**

- Índice por `alert_id`, para cargar rápidamente los eventos de una alerta.
    
- Índice por `event_id`, para conocer la participación de un evento.
    
- Restricción `UNIQUE(alert_id, event_id)` para evitar duplicados.
    

---

## Integridad y trazabilidad

El esquema garantiza la integridad referencial mediante claves foráneas y permite reconstruir el flujo completo del sistema:

```
Source → Events → Rules → Alerts → Alert_Events → Events
```

Este diseño permite:

- Identificar el origen de cada evento.
    
- Conocer la regla responsable de cada alerta.
    
- Analizar qué eventos explican una alerta concreta.
    
- Facilitar auditorías y análisis históricos.
    

---

## Alcance del esquema

El esquema de base de datos se ha diseñado específicamente para cubrir las necesidades del Laboratorio SIEM definido en este proyecto. No se incluyen mecanismos avanzados como particionado, replicación o alta disponibilidad, ya que quedan fuera del alcance académico y funcional del sistema.

---
