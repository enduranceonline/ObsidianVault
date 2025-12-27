

---

# Esquema de base de datos  
## Laboratorio SIEM

---

## Introducción

En este apartado se define el **esquema físico de la base de datos** a partir del modelo entidad–relación. Se describen las tablas, sus campos principales, tipos de datos recomendados y restricciones relevantes.

El objetivo es disponer de un diseño claro y consistente que permita:

- Persistir eventos y alertas con trazabilidad.
- Realizar consultas típicas del sistema (eventos recientes, alertas abiertas, detalle de alerta).
- Mantener un alcance simple y adecuado al proyecto académico.

---

## Tipo de base de datos

Se utilizará una base de datos **relacional**, por su adecuación al modelo definido y por facilitar:

- Integridad referencial mediante claves foráneas.
- Consultas estructuradas y filtrado eficiente.
- Trazabilidad entre entidades.

---

## Tablas del sistema

### • sources

Propósito: almacenar las fuentes lógicas de eventos.

Campos recomendados:

- id (PK) — integer/uuid
- name — varchar (único)
- type — varchar
- description — text (nullable)
- created_at — datetime

Restricciones:

- name único para evitar duplicados.

---

### • events

Propósito: almacenar eventos normalizados.

Campos recomendados:

- id (PK) — integer/uuid
- timestamp — datetime (momento en que ocurrió el evento)
- source_id (FK -> sources.id) — integer/uuid
- event_type — varchar
- severity — smallint o varchar (según enfoque)
- message — text
- metadata — json/text (nullable)
- created_at — datetime (momento de ingestión/almacenado)

Índices recomendados:

- index por timestamp (consultas de “eventos recientes”)
- index por source_id + timestamp (filtros por fuente)
- index por event_type (según volumen)

Restricciones:

- source_id obligatorio (un evento debe tener fuente).

---

### • rules

Propósito: almacenar reglas de detección (referencia y trazabilidad).

Campos recomendados:

- id (PK) — integer/uuid
- name — varchar (único)
- description — text
- condition — text (representación lógica de la regla)
- severity — smallint o varchar
- enabled — boolean
- created_at — datetime

Restricciones:

- name único para identificar reglas de forma estable.

Nota:

- Aunque la lógica pueda estar implementada en código, mantener rules permite trazabilidad y documentación interna del sistema.

---

### • alerts

Propósito: almacenar alertas generadas por reglas.

Campos recomendados:

- id (PK) — integer/uuid
- rule_id (FK -> rules.id) — integer/uuid
- status — varchar (por ejemplo: OPEN/CLOSED)
- severity — smallint o varchar
- description — text
- created_at — datetime
- closed_at — datetime (nullable)

Índices recomendados:

- index por status + created_at (alertas abiertas primero)
- index por rule_id (análisis por regla)

Restricciones:

- rule_id obligatorio (cada alerta debe asociarse a una regla).
- closed_at solo tiene sentido si status = CLOSED (se valida en lógica de aplicación).

---

### • alert_events

Propósito: tabla de unión para la relación N:M entre alertas y eventos.

Campos recomendados:

- id (PK) — integer/uuid
- alert_id (FK -> alerts.id) — integer/uuid
- event_id (FK -> events.id) — integer/uuid
- created_at — datetime

Índices y restricciones recomendadas:

- índice por alert_id (cargar detalle de alerta rápido)
- índice por event_id (ver participación de eventos)
- restricción UNIQUE(alert_id, event_id) para evitar duplicados

---

## Integridad y trazabilidad

El esquema garantiza integridad referencial mediante claves foráneas y permite reconstruir el flujo completo:

source → events → (rules) → alerts → alert_events → events

Esto posibilita:

- Identificar el origen de cada evento.
- Saber qué regla generó cada alerta.
- Consultar qué eventos explican una alerta.

---