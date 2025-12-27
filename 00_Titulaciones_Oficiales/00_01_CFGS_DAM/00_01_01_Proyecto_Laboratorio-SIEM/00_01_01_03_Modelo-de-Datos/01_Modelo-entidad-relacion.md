

---

# Modelo entidad–relación (ER)  
## Laboratorio SIEM

---

## Introducción

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

## Relación entre entidades

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

## Entidad intermedia

### • AlertEvent (Relación Alerta–Evento)

Entidad de unión que permite asociar múltiples eventos a una alerta y mantener trazabilidad.

Rol en el sistema:

- Permite reconstruir qué eventos causaron una alerta.
- Facilita el detalle de alertas en el dashboard.

---

## Diagrama ER (descripción textual)

Relaciones principales (resumen):

- Source (1) —— (N) Event
- Rule (1) —— (N) Alert
- Alert (1) —— (N) AlertEvent —— (N) Event (1)

---

## Consideraciones de diseño

El modelo se ha diseñado con criterios de:

- Normalización y trazabilidad.
- Simplicidad estructural.
- Compatibilidad con consultas típicas del sistema:
- “Eventos recientes por fuente”
- “Alertas abiertas”
- “Detalle de alerta con eventos asociados”
- “Alertas generadas por regla”

---
