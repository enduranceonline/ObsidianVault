## Introducción

La gestión de alertas es la parte del sistema que permite consultar, filtrar y modificar las alertas generadas por el motor de reglas.

Dentro del SIEM Lab MVP, una alerta representa el resultado de aplicar una regla de detección sobre un evento recibido. No todos los eventos generan alertas; solo lo hacen aquellos que cumplen las condiciones de una regla activa.

---

## Función de las alertas

Las alertas permiten destacar eventos que pueden ser relevantes desde el punto de vista de seguridad.

El flujo básico es:

```text
evento recibido → regla coincidente → alerta generada → revisión
````

Cada alerta queda almacenada en PostgreSQL y asociada a:

```text
- El evento que la originó.
- La regla que se activó.
- Un estado.
- Un título.
- Un group_key, si existe.
```

Esta relación permite mantener trazabilidad entre el evento original, la regla aplicada y la alerta resultante.

---

## Tabla alerts

Las alertas se almacenan en la tabla:

```text
alerts
```

Campos principales:

```text
id          → identificador único de la alerta
rule_id     → regla que generó la alerta
event_id    → evento que originó la alerta
title       → título de la alerta
status      → estado actual
group_key   → clave de agrupación
created_at  → fecha de creación
```

Esta tabla permite consultar las alertas generadas y relacionarlas con el resto de entidades del sistema.

---

## Estados de alerta

Para simular una gestión básica de alertas, se definieron tres estados:

```text
open
ack
closed
```

Su significado es:

```text
open   → alerta abierta y pendiente de revisión
ack    → alerta reconocida o aceptada
closed → alerta cerrada
```

Esta gestión de estados permite representar de forma sencilla el ciclo de vida de una alerta.

---

## Generación de alertas

Las alertas se generan durante el flujo de ingesta.

Cuando se envía un evento a:

```http
POST /ingest
```

el sistema realiza los siguientes pasos:

```text
1. Guarda el evento en la base de datos.
2. Consulta las reglas activas.
3. Evalúa el evento contra cada regla.
4. Si hay coincidencia, genera una alerta.
5. Guarda la alerta en PostgreSQL.
```

El estado inicial de una alerta generada es:

```text
open
```

---

## Consulta de alertas

La API permite consultar alertas mediante endpoints específicos.

Endpoints principales:

```http
GET /alerts
GET /alerts/{alert_id}
```

Estos endpoints permiten recuperar alertas almacenadas en la base de datos.

También existen endpoints orientados al frontend:

```http
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Estos endpoints devuelven información enriquecida, combinando datos de la alerta con información del evento asociado.

---

## Alertas enriquecidas

Durante el desarrollo se detectó que el frontend necesitaba mostrar más información que la almacenada directamente en la tabla `alerts`.

Por ejemplo, era útil mostrar datos como:

```text
- source del evento
- severity del evento
- message del evento
- fecha de creación
- estado de la alerta
- regla activada
```

Para evitar duplicar datos dentro de la tabla `alerts`, se crearon endpoints enriquecidos.

Esta decisión mantiene el modelo de datos más limpio y permite adaptar la respuesta de la API a las necesidades de visualización.

---

## Filtros de alertas

El sistema permite filtrar alertas para facilitar su consulta.

Filtros principales:

```text
status
severity_min
q
limit
offset
```

Uso de cada filtro:

```text
status       → filtra por estado de alerta
severity_min → filtra por severidad mínima del evento asociado
q            → búsqueda textual
limit        → limita el número de resultados
offset       → permite paginación
```

Estos filtros ayudan a reducir ruido y permiten consultar la información de forma más precisa.

---

## Ejemplos de consulta

Consultar alertas reconocidas:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?status=ack" | python3 -m json.tool
```

Consultar alertas con severidad mínima:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?severity_min=7" | python3 -m json.tool
```

Buscar alertas que contengan un texto:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?q=failed" | python3 -m json.tool
```

---

## Cambio de estado

El sistema permite cambiar el estado de una alerta mediante:

```http
PATCH /alerts/{alert_id}
```

Ejemplo de cuerpo de petición:

```json
{
  "status": "ack"
}
```

Este endpoint permite actualizar el estado de una alerta existente.

Ejemplo validado durante el proyecto:

```bash
curl -s -X PATCH http://127.0.0.1:8000/alerts/6 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "ack"
  }' | python3 -m json.tool
```

La alerta pasó correctamente de `open` a `ack`.

---

## Ciclo básico de una alerta

El ciclo básico representado en el proyecto es:

```text
1. Se recibe un evento.
2. El evento coincide con una regla.
3. Se genera una alerta en estado open.
4. El usuario revisa la alerta.
5. El usuario puede marcarla como ack.
6. La alerta puede cerrarse como closed.
```

Este flujo es una simplificación de la gestión de alertas en herramientas defensivas.

---

## Diferencia entre alerta e incidente

En el proyecto se trabaja con alertas, no con incidentes.

Una alerta indica que un evento cumple una condición de detección. Sin embargo, no significa necesariamente que exista un incidente real.

Por ejemplo, varios intentos fallidos de autenticación pueden deberse a un error legítimo de un usuario o a un intento de ataque.

Por este motivo, las alertas requieren revisión. El proyecto representa esta revisión de forma básica mediante el cambio de estado.

---

## Validación de la gestión de alertas

La gestión de alertas se validó comprobando:

```text
- Generación automática de alertas desde /ingest.
- Consulta de alertas desde /alerts.
- Consulta enriquecida desde /alerts/ui.
- Filtros por estado.
- Filtros por severidad.
- Búsqueda textual.
- Cambio de estado mediante PATCH.
- Visualización desde frontend.
```

Durante la validación final, una alerta generada por un evento SSH pudo consultarse, visualizarse y cambiarse de estado correctamente.

---

## Problemas y decisiones durante el desarrollo

Durante el desarrollo fue necesario tomar varias decisiones sobre las alertas.

La primera fue separar claramente los eventos de las alertas. Un evento es un dato recibido; una alerta es el resultado de una detección.

La segunda decisión fue no duplicar todos los datos del evento dentro de la tabla `alerts`. En su lugar, se mantuvo la relación con el evento original y se crearon endpoints enriquecidos para el frontend.

La tercera decisión fue limitar los estados a `open`, `ack` y `closed`. Esta estructura es simple, pero suficiente para representar una gestión básica.

También fue necesario añadir filtros para que la consulta de alertas fuera útil y no se limitara a devolver todos los registros sin control.

---

## Limitaciones

La gestión de alertas actual tiene varias limitaciones:

```text
- No existe asignación de alertas a usuarios.
- No hay comentarios sobre alertas.
- No se almacena historial de cambios de estado.
- No se gestionan incidentes o casos.
- No hay sistema de prioridades avanzado.
- No hay notificaciones externas.
- No hay cierre automático de alertas.
```

Estas limitaciones son coherentes con el alcance del MVP.

---

## Posibles mejoras

En futuras versiones, la gestión de alertas podría ampliarse con:

```text
- Historial de cambios de estado.
- Comentarios de analistas.
- Asignación de alertas.
- Gestión de incidentes.
- Priorización automática.
- Notificaciones.
- Agrupación avanzada.
- Dashboard de alertas.
- Exportación de informes.
```

Estas mejoras permitirían acercar el sistema a una herramienta de monitorización más realista.

---

## Conclusión

La gestión de alertas permite cerrar el flujo principal del SIEM Lab MVP.

El sistema no solo recibe eventos y genera alertas, sino que también permite consultarlas, filtrarlas y modificar su estado.

Aunque se trata de una gestión básica, es suficiente para representar el ciclo inicial de revisión de alertas en un entorno Blue Team.