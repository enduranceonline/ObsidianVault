## Introducción

El modelo de datos del proyecto se ha diseñado para representar de forma clara los tres elementos principales del sistema:

```text
events
rules
alerts
````

La finalidad del modelo es almacenar los eventos recibidos, las reglas de detección configuradas y las alertas generadas por el motor de reglas.

La estructura se mantiene deliberadamente sencilla para ajustarse al enfoque MVP del proyecto.

---

## Entidades principales

El sistema se basa en tres entidades:

```text
Evento → dato recibido por la API
Regla  → condición que evalúa un evento
Alerta → resultado generado cuando una regla coincide
```

La relación principal es:

```text
events 1 ─── N alerts N ─── 1 rules
```

Esto significa que:

```text
- Un evento puede generar una o varias alertas.
- Una regla puede generar muchas alertas.
- Cada alerta está asociada a un evento y a una regla.
```

---

## Tabla events

La tabla `events` almacena los eventos recibidos por el sistema.

Un evento representa un log o suceso simulado enviado mediante la API, normalmente a través del endpoint `/ingest`.

Campos principales:

```text
id          → identificador único del evento
source      → origen del evento
severity    → nivel de severidad
message     → mensaje descriptivo
meta        → metadatos adicionales
created_at  → fecha de creación
```

Ejemplo de evento:

```json
{
  "source": "ssh",
  "severity": 7,
  "message": "failed password for invalid user demo",
  "meta": {
    "host": "demo-host"
  }
}
```

Esta tabla permite conservar el histórico de eventos recibidos y relacionarlos posteriormente con las alertas generadas.

---

## Tabla rules

La tabla `rules` almacena las reglas de detección configuradas en el sistema.

Una regla define las condiciones que debe cumplir un evento para generar una alerta.

Campos principales:

```text
id                 → identificador único de la regla
name               → nombre de la regla
enabled            → indica si la regla está activa
source             → fuente del evento a evaluar
severity_min       → severidad mínima requerida
contains           → texto que debe aparecer en el mensaje
meta_match         → coincidencia esperada en metadatos
throttle_seconds   → tiempo de espera para evitar alertas repetidas
threshold_count    → número de eventos necesarios para activar umbral
threshold_seconds  → ventana temporal del umbral
created_at         → fecha de creación
```

Ejemplo conceptual de regla:

```text
name = test_rule_ssh
enabled = true
source = ssh
severity_min = 5
contains = failed
```

Esta regla detecta eventos procedentes de `ssh`, con severidad igual o superior a 5 y cuyo mensaje contenga la palabra `failed`.

---

## Tabla alerts

La tabla `alerts` almacena las alertas generadas por el motor de reglas.

Una alerta se crea cuando un evento recibido cumple las condiciones de una regla activa.

Campos principales:

```text
id          → identificador único de la alerta
rule_id     → regla que ha generado la alerta
event_id    → evento que ha originado la alerta
title       → título descriptivo
status      → estado de la alerta
group_key   → clave de agrupación
created_at  → fecha de creación
```

Estados posibles:

```text
open
ack
closed
```

La alerta permite representar que un evento ha sido considerado relevante según una regla de detección.

---

## Relación entre eventos, reglas y alertas

La relación entre entidades permite reconstruir el origen de cada alerta.

Cuando se genera una alerta, el sistema conserva:

```text
- Qué evento la ha originado.
- Qué regla se ha activado.
- En qué estado se encuentra.
- A qué grupo pertenece, si existe group_key.
```

Ejemplo:

```text
Evento:
source = ssh
severity = 7
message = failed password for invalid user demo

Regla:
source = ssh
severity_min = 5
contains = failed

Alerta:
title = Rule matched: test_rule_ssh
status = open
```

Esta separación evita mezclar conceptos distintos y facilita la consulta de información.

---

## Uso de meta

El campo `meta` permite guardar información adicional del evento.

Se utiliza para datos que pueden variar según el tipo de evento, por ejemplo:

```json
{
  "host": "server-01",
  "ip": "192.168.1.50",
  "user": "demo"
}
```

En el proyecto, el metadato más importante es:

```text
meta.host
```

Este valor se utiliza para calcular el `group_key`.

---

## Uso de group_key

El `group_key` permite agrupar alertas o eventos relacionados.

En esta versión del proyecto, se obtiene a partir de:

```text
meta.host
```

Ejemplo:

```json
{
  "meta": {
    "host": "demo-host"
  }
}
```

Resultado:

```text
group_key = demo-host
```

El `group_key` es importante para aplicar lógica como:

```text
- Control de duplicados.
- Throttle.
- Threshold.
- Agrupación por host.
```

Si un evento no contiene `meta.host`, el sistema puede generar alertas simples, pero algunas funciones de agrupación quedan limitadas.

---

## Tabla alembic_version

Además de las tablas funcionales, existe la tabla:

```text
alembic_version
```

Esta tabla es gestionada por Alembic y permite controlar la versión actual del esquema de base de datos.

No forma parte de la lógica SIEM, pero es necesaria para gestionar migraciones.

---

## Decisiones de diseño del modelo

El modelo de datos se diseñó con varias decisiones importantes:

```text
- Separar eventos, reglas y alertas.
- Asociar cada alerta a un evento y a una regla.
- Usar meta para información flexible.
- Usar group_key para agrupar eventos relacionados.
- Evitar duplicar datos del evento dentro de la alerta.
- Crear endpoints enriquecidos para mostrar datos combinados en frontend.
```

La decisión de no duplicar todos los datos del evento dentro de la tabla `alerts` mantiene el modelo más limpio.

Cuando el frontend necesita mostrar información combinada, se utilizan endpoints como:

```text
GET /alerts/ui
GET /alerts/{alert_id}/ui
```

---

## Limitaciones del modelo

El modelo actual es suficiente para el MVP, pero tiene limitaciones:

```text
- No incluye usuarios.
- No incluye roles ni permisos.
- No almacena investigación de incidentes.
- No incluye comentarios sobre alertas.
- No contempla asignación de alertas a analistas.
- No almacena fuentes reales de logs.
- No incluye normalización avanzada de eventos.
```

Estas limitaciones son coherentes con el alcance del proyecto.

---

## Posibles mejoras

En una versión futura, el modelo podría ampliarse con nuevas entidades:

```text
users          → usuarios del sistema
roles          → permisos y perfiles
cases          → casos o incidentes
comments       → comentarios sobre alertas
assets         → activos monitorizados
log_sources    → fuentes de logs reales
notifications  → avisos generados
```

Estas ampliaciones permitirían acercar el sistema a una herramienta de monitorización más completa.

---

## Conclusión

El modelo de datos del SIEM Lab MVP se basa en una estructura simple y clara.

La separación entre `events`, `rules` y `alerts` permite representar el flujo principal del sistema sin añadir complejidad innecesaria.

Este modelo permite recibir eventos, evaluarlos mediante reglas, generar alertas y conservar la relación entre los datos que originan cada detección.