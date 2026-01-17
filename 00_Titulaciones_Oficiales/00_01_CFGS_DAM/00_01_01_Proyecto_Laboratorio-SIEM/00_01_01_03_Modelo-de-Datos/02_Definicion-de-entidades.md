

---

# Definición de entidades

## Laboratorio SIEM

---

## 1. Introducción

En este apartado se describen las **entidades que conforman el modelo de datos del laboratorio SIEM**, detallando sus atributos principales y su función dentro del sistema.

El modelo presentado refleja el **diseño final implementado**, resultado de un proceso de iteración durante la fase de desarrollo. Se prioriza un enfoque **funcional, coherente con el alcance del proyecto y alineado con los objetivos del ciclo formativo**, manteniendo la posibilidad de evolución futura del sistema.

---

## 2. Entidades y atributos

### • Event (Evento)

Representa un evento **normalizado** recibido por el sistema a través de la API de ingesta. Constituye la unidad básica de información sobre la que se aplican las reglas de detección.

Atributos principales:

- `id`  
    Identificador único del evento.
    
- `ts`  
    Fecha y hora en la que se produjo el evento.
    
- `source`  
    Origen lógico del evento (por ejemplo, `ssh`, `syslog`, `windows_security`).
    
- `severity`  
    Nivel de severidad asignado al evento.
    
- `message`  
    Descripción textual del evento.
    
- `meta`  
    Información adicional asociada al evento en  formato estructurado (por ejemplo, host, usuario, IP).
    
- `created_at`  
    Fecha de almacenamiento del evento en el sistema.
    

---

### • Rule (Regla)

Representa una **regla de detección** utilizada por el motor de reglas para evaluar los eventos entrantes y determinar si deben generar una alerta.

Atributos principales:

- `id`  
    Identificador único de la regla.
    
- `name`  
    Nombre descriptivo de la regla.
    
- `enabled`  
    Indica si la regla se encuentra activa.
    
- `source`  
    Origen del evento al que aplica la regla (opcional).
    
- `severity_min`  
    Severidad mínima que debe cumplir un evento para ser evaluado.
    
- `contains`  
    Cadena de texto que debe aparecer en el mensaje del evento (opcional).
    
- `meta_match`  
    Condiciones de coincidencia exacta sobre los metadatos del evento.
    
- `throttle_seconds`  
    Intervalo mínimo entre alertas generadas por la misma regla y grupo.
    
- `threshold_count`  
    Número mínimo de eventos requeridos para activar la regla.
    
- `threshold_seconds`  
    Ventana temporal utilizada para el cálculo del umbral.
    
- `created_at`  
    Fecha de creación de la regla.
    

---

### • Alert (Alerta)

Representa una **alerta generada** como resultado de la evaluación de una regla sobre un evento concreto. Es la entidad que se presenta al usuario para su gestión y análisis.

Atributos principales:

- `id`  
    Identificador único de la alerta.
    
- `status`  
    Estado de la alerta (`open`, `ack`, `closed`).
    
- `rule_id`  
    Referencia a la regla que generó la alerta.
    
- `event_id`  
    Referencia al evento que originó la alerta.
    
- `group_key`  
    Clave de agrupación utilizada para mecanismos de _throttling_ y deduplicación (por ejemplo, host).
    
- `created_at`  
    Fecha de generación de la alerta.
    
- `updated_at`  
    Fecha de la última actualización del estado de la alerta.
    

---

## 3. Relaciones y claves

Las relaciones entre las entidades se establecen mediante **claves primarias y foráneas**, garantizando la coherencia de los datos y la trazabilidad del proceso de detección.

- **Event.id → Alert.event_id**  
    Un evento puede generar **cero o varias alertas**, en función de las reglas que se apliquen. Cada alerta queda asociada a un único evento que la origina.
    
- **Rule.id → Alert.rule_id**  
    Cada alerta está vinculada a una única regla, mientras que una regla puede generar múltiples alertas a lo largo del tiempo.
    

Este modelo permite mantener una **trazabilidad completa**, desde el evento recibido por el sistema hasta la alerta final gestionada por el usuario.

---

## 4. Nota sobre la evolución del diseño

Durante la fase inicial de diseño se contempló un modelo con una entidad intermedia (`AlertEvent`) para representar una relación N:M entre alertas y eventos, así como una entidad independiente para las fuentes (`Source`).

[[00_Titulaciones_Oficiales/00_01_CFGS_DAM/00_01_01_Proyecto_Laboratorio-SIEM/00_01_01_99_Borradores/01_ERD_Laboratorio_SIEM_borrador.excalidraw|01_ERD_Laboratorio_SIEM_borrador.excalidraw]]

Tras la implementación del MVP, se decidió **simplificar el modelo**, estableciendo una relación directa entre `Alert` y `Event`, y representando la fuente como un atributo lógico del evento.  
Esta decisión reduce la complejidad del sistema, facilita la trazabilidad y se ajusta al alcance del laboratorio, manteniendo abierta la posibilidad de incorporar correlación avanzada y modelos más complejos en futuras ampliaciones.

---
