

---

# Definición de entidades  
## Laboratorio SIEM

---

## Introducción

En este apartado se detallan las **entidades del modelo de datos**, definiendo sus principales atributos y el propósito de cada uno dentro del sistema.

El objetivo es proporcionar una visión clara de **qué información se almacena**, manteniendo un diseño coherente con la arquitectura y el alcance del proyecto.

---

## Entidades y atributos

### • Source (Fuente)

Representa el origen lógico de los eventos.

Atributos principales:

- `id  
  Identificador único de la fuente.
- `name  
  Nombre descriptivo de la fuente (por ejemplo: Linux, Windows).
- `type  
  Tipo de fuente (sistema operativo, servicio, aplicación).
- `description  
  Descripción opcional de la fuente.
- `created_at  
  Fecha de registro de la fuente en el sistema.

---

### • Event (Evento)

Representa un evento normalizado recibido por el sistema.

Atributos principales:
- `id  
  Identificador único del evento.
- `timestamp  
  Fecha y hora en la que se produjo el evento.
- `source_id  
  Referencia a la fuente que generó el evento.
- `event_type  
  Tipo de evento (login_failed, login_success, privilege_use, etc.).
- `severity  
  Nivel de severidad asignado al evento.
- `message  
  Descripción breve del evento.
- `metadata  
  Información adicional asociada al evento (por ejemplo, IP, usuario).
- `created_at  
  Fecha de almacenamiento del evento en el sistema.

---

### • Rule (Regla)

Representa una regla de detección utilizada por el sistema.

Atributos principales:
- `id  
  Identificador único de la regla.
- `name  
  Nombre descriptivo de la regla.
- `description  
  Explicación funcional de la regla.
- `condition  
  Representación lógica de la condición evaluada.
- `severity  
  Severidad asociada a la alerta generada.
- `enabled  
  Indica si la regla está activa.
- `created_at  
  Fecha de creación de la regla.

---

### • Alert (Alerta)

Representa una alerta generada como resultado de la evaluación de una regla.

Atributos principales:
- `id  
  Identificador único de la alerta.
- `rule_id  
  Referencia a la regla que generó la alerta.
- `status  
  Estado de la alerta (abierta, cerrada).
- `severity  
  Severidad de la alerta.
- `description  
  Descripción de la alerta.
- `created_at  
  Fecha de generación de la alerta.
- `closed_at  
  Fecha de cierre de la alerta (si aplica).

---

### • AlertEvent (Alerta–Evento)

Entidad intermedia que relaciona alertas y eventos.

Atributos principales:
- `id  
  Identificador único de la relación.
- `alert_id  
  Referencia a la alerta.
- `event_id  
  Referencia al evento.
- `created_at  
  Fecha de creación de la relación.

---

### Relaciones y claves

Las relaciones entre las entidades del sistema se establecen mediante **claves primarias y foráneas**, permitiendo mantener la coherencia de los datos y la trazabilidad del proceso de detección.

- **Source.id → Event.source_id**  
    Cada evento almacenado se asocia a una única fuente que indica el sistema u origen lógico que lo generó. Esta relación permite agrupar y filtrar eventos según su procedencia.
    
- **Rule.id → Alert.rule_id**  
    Cada alerta generada está vinculada a la regla que ha provocado su creación. Esta relación permite identificar qué lógica de detección ha sido responsable de cada alerta.
    
- **Alert.id → AlertEvent.alert_id**  
    La entidad intermedia AlertEvent permite asociar una alerta con uno o varios eventos, representando el conjunto de eventos que han contribuido a su generación.
    
- **Event.id → AlertEvent.event_id**  
    Esta relación permite vincular cada evento con las alertas en las que participa, facilitando el acceso al detalle de una alerta y la reconstrucción del contexto que la originó.
    

En conjunto, estas relaciones garantizan la **trazabilidad completa del sistema**, permitiendo seguir el flujo de información desde la fuente que genera un evento, pasando por la regla que lo analiza, hasta la alerta final que se presenta al usuario.

---