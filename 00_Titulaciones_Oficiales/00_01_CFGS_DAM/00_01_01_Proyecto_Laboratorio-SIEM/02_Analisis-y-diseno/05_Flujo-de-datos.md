## Introducción

El flujo de datos describe cómo circula la información dentro del SIEM Lab MVP, desde que se recibe un evento hasta que se genera una alerta y puede consultarse desde la API o el frontend.

El flujo principal del proyecto es:

```text
evento simulado → ingesta → almacenamiento → evaluación → alerta → consulta
````

Este recorrido permite entender cómo se conectan los componentes principales del sistema.

---

## Flujo general del sistema

El flujo completo puede representarse de forma simplificada así:

```text
Usuario / prueba manual
        ↓
POST /ingest
        ↓
API FastAPI
        ↓
Guardar evento en PostgreSQL
        ↓
Consultar reglas activas
        ↓
Evaluar evento contra reglas
        ↓
Generar alerta si hay coincidencia
        ↓
Guardar alerta en PostgreSQL
        ↓
Consultar alerta desde API o frontend
```

La API actúa como punto central del flujo. Recibe los datos, ejecuta la lógica del sistema y coordina la comunicación con la base de datos.

---

## Entrada de datos

La entrada principal de datos se realiza mediante el endpoint:

```http
POST /ingest
```

Este endpoint recibe eventos simulados en formato JSON.

Ejemplo:

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

Cada evento contiene cuatro campos principales:

```text
source   → origen del evento
severity → nivel de severidad
message  → mensaje descriptivo
meta     → metadatos adicionales
```

Este diseño permite enviar eventos sencillos, pero suficientemente expresivos para ser evaluados por reglas.

---

## Validación inicial del evento

Cuando la API recibe un evento, primero valida que la petición tenga la estructura esperada.

La validación permite comprobar que el evento contiene los datos necesarios para ser procesado correctamente.

Si el evento es válido, continúa el flujo. Si no lo es, la API devuelve un error de validación.

Esta fase es importante porque evita que datos incompletos o mal formados lleguen a la base de datos o al motor de reglas.

---

## Almacenamiento del evento

Una vez validado, el evento se guarda en la tabla:

```text
events
```

El almacenamiento permite conservar el histórico de eventos recibidos.

La información guardada incluye:

```text
- Identificador del evento.
- Fuente.
- Severidad.
- Mensaje.
- Metadatos.
- Fecha de creación.
```

Este paso es importante porque la alerta generada posteriormente queda asociada al evento original.

---

## Cálculo del group_key

Después de almacenar el evento, el sistema obtiene un valor de agrupación llamado `group_key`.

En esta versión del proyecto, el `group_key` se calcula a partir de:

```text
meta.host
```

Ejemplo:

```json
{
  "meta": {
    "host": "server-01"
  }
}
```

Resultado:

```text
group_key = server-01
```

El `group_key` permite agrupar eventos relacionados con una misma máquina o fuente.

Se utiliza especialmente en funciones como:

```text
- Control de duplicados.
- Throttle.
- Threshold.
```

Si el evento no contiene `meta.host`, el sistema puede generar alertas simples, pero algunas funciones de agrupación quedan limitadas.

---

## Consulta de reglas activas

Una vez recibido y almacenado el evento, la API consulta las reglas activas en la tabla:

```text
rules
```

No todas las reglas del sistema se aplican necesariamente. Solo se evalúan aquellas que están habilitadas mediante el campo:

```text
enabled = true
```

Esto permite mantener reglas creadas pero desactivadas, sin que influyan en la generación de alertas.

---

## Evaluación del evento

El motor de reglas compara el evento recibido con cada regla activa.

Las condiciones principales que puede evaluar son:

```text
source
severity_min
contains
meta_match
threshold_count
threshold_seconds
throttle_seconds
```

La evaluación se realiza de forma progresiva. Si el evento no cumple una condición necesaria, esa regla no genera alerta.

Ejemplo de evaluación:

```text
Evento:
source = ssh
severity = 7
message = failed password for invalid user demo

Regla:
source = ssh
severity_min = 5
contains = failed

Resultado:
coincidencia
```

En este caso, el evento cumple todas las condiciones de la regla.

---

## Generación de alerta

Si el evento coincide con una regla activa, el sistema genera una alerta.

La alerta se guarda en la tabla:

```text
alerts
```

La alerta queda asociada a:

```text
- El evento recibido.
- La regla activada.
- Un título.
- Un estado inicial.
- Un group_key, si existe.
- Una fecha de creación.
```

El estado inicial de una alerta es:

```text
open
```

Esto indica que la alerta está pendiente de revisión.

---

## Consulta de alertas

Una vez generada, la alerta puede consultarse mediante la API.

Endpoints principales:

```http
GET /alerts
GET /alerts/{alert_id}
```

Estos endpoints permiten acceder a la información básica de las alertas almacenadas.

También existen endpoints enriquecidos para facilitar la visualización desde el frontend:

```http
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Estos endpoints combinan información de la alerta con datos del evento asociado.

---

## Flujo hacia el frontend

El frontend no accede directamente a PostgreSQL. Toda la información que muestra procede de la API.

Flujo de consulta desde frontend:

```text
Frontend
   ↓
GET /alerts/ui
   ↓
API FastAPI
   ↓
Consulta PostgreSQL
   ↓
Respuesta enriquecida
   ↓
Visualización en navegador
```

Este diseño mantiene la separación entre interfaz, lógica de aplicación y persistencia.

---

## Cambio de estado de una alerta

El flujo de datos no termina necesariamente con la consulta de una alerta. El sistema permite modificar su estado mediante:

```http
PATCH /alerts/{alert_id}
```

Estados permitidos:

```text
open
ack
closed
```

Flujo de actualización:

```text
Usuario
   ↓
PATCH /alerts/{alert_id}
   ↓
API FastAPI
   ↓
Actualizar alerta en PostgreSQL
   ↓
Devolver alerta actualizada
```

Esta operación permite representar una gestión básica del ciclo de vida de las alertas.

---

## Flujo de métricas

El sistema también permite consultar métricas generales mediante:

```http
GET /metrics
```

Este endpoint consulta la base de datos y devuelve información resumida:

```text
- Total de eventos.
- Total de reglas.
- Reglas activas.
- Total de alertas.
```

El flujo es:

```text
Usuario / Swagger / curl
        ↓
GET /metrics
        ↓
API
        ↓
Consulta PostgreSQL
        ↓
Respuesta con métricas
```

Estas métricas permiten comprobar rápidamente el estado general del sistema.

---

## Flujo de validación con Adminer

Adminer permite revisar directamente los datos almacenados en PostgreSQL.

Flujo de inspección:

```text
Usuario
   ↓
Adminer
   ↓
PostgreSQL
   ↓
Tablas events, rules, alerts
```

Adminer no forma parte del flujo funcional principal, pero fue útil para validar que los datos se estaban guardando correctamente.

---

## Ejemplo completo del flujo

Ejemplo de evento enviado:

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

Regla activa:

```text
source = ssh
severity_min = 5
contains = failed
```

Resultado del flujo:

```text
1. El evento se recibe en /ingest.
2. Se almacena en la tabla events.
3. Se obtiene group_key = demo-host.
4. Se consultan las reglas activas.
5. El evento coincide con la regla SSH.
6. Se genera una alerta.
7. La alerta se guarda en la tabla alerts.
8. La alerta puede consultarse desde /alerts/ui.
9. El frontend la muestra al usuario.
10. El estado puede cambiarse de open a ack.
```

---

## Decisiones relevantes del flujo

Durante el diseño del flujo se tomaron varias decisiones:

```text
- Centralizar la entrada de eventos en /ingest.
- Guardar el evento antes de evaluar reglas.
- Asociar cada alerta al evento original.
- Asociar cada alerta a la regla activada.
- Usar group_key para agrupación básica.
- Crear endpoints enriquecidos para el frontend.
- Mantener Adminer como herramienta auxiliar, no como parte del flujo principal.
```

Estas decisiones permiten que el flujo sea claro, trazable y fácil de explicar.

---

## Limitaciones del flujo actual

El flujo actual es suficiente para el MVP, pero tiene algunas limitaciones:

```text
- Los eventos son simulados.
- No existe ingesta automática desde sistemas reales.
- No hay autenticación en los endpoints.
- No existe procesamiento asíncrono.
- No hay cola de eventos.
- No se implementa normalización avanzada.
- No existe correlación compleja entre múltiples fuentes.
```

Estas limitaciones son coherentes con el alcance del proyecto y pueden abordarse en futuras versiones.

---

## Posibles mejoras

El flujo de datos podría ampliarse con:

```text
- Agentes externos que envíen logs reales.
- Cola de mensajes para procesar eventos.
- Normalización previa de eventos.
- Workers asíncronos.
- Integración con syslog.
- Integración con logs de Linux.
- Sistema de notificaciones.
- Dashboard en tiempo real.
```

Estas mejoras acercarían el sistema a una arquitectura más realista, pero no eran necesarias para validar el MVP.

---

## Conclusión

El flujo de datos del SIEM Lab MVP permite representar de forma clara el proceso principal de un sistema de monitorización defensiva.

El sistema recibe eventos, los almacena, los evalúa mediante reglas, genera alertas y permite consultarlas desde API o frontend.

Este flujo demuestra el funcionamiento esencial del proyecto y conecta los principales componentes desarrollados: API, base de datos, motor de reglas y frontend.