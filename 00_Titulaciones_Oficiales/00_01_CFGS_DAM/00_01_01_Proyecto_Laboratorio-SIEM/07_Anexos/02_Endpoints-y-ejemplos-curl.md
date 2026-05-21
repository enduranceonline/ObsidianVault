## Introducción

Este anexo recopila los endpoints principales del **SIEM Lab MVP** junto con ejemplos de uso mediante `curl`.

La finalidad de esta nota es servir como referencia rápida para probar la API desde terminal y entender qué función cumple cada endpoint dentro del sistema.

Los endpoints se agrupan por funcionalidad:

```text
- Estado e información del sistema.
- Métricas.
- Eventos.
- Ingesta.
- Reglas.
- Alertas.
- Alertas enriquecidas para frontend.
- Cambio de estado.
````

---

## URL base de la API

Durante el desarrollo y las pruebas, la API se ejecuta en local en el puerto `8000`.

```text
http://127.0.0.1:8000
```

Ejemplo general:

```bash
curl http://127.0.0.1:8000/health
```

---

## Documentación interactiva Swagger

FastAPI genera documentación interactiva automáticamente.

URL:

```text
http://127.0.0.1:8000/docs
```

Swagger permite probar los endpoints desde el navegador sin escribir comandos manuales.

---

# 1. Endpoints de estado e información

## GET /health

### Función

Comprueba que la API está operativa y que existe conexión con PostgreSQL.

### Comando

```bash
curl http://127.0.0.1:8000/health
```

### Respuesta esperada

```json
{
  "status": "ok",
  "db": "ok"
}
```

### Qué valida

```text
- API levantada.
- Conexión correcta con la base de datos.
```

---

## GET /info

### Función

Devuelve información básica de la aplicación.

### Comando

```bash
curl http://127.0.0.1:8000/info
```

### Qué valida

```text
- La API responde.
- El endpoint informativo está disponible.
```

---

# 2. Endpoint de métricas

## GET /metrics

### Función

Devuelve contadores generales del sistema.

### Comando

```bash
curl -s http://127.0.0.1:8000/metrics | python3 -m json.tool
```

### Campos principales

```text
events_total
rules_total
rules_enabled
alerts_total
```

### Uso recomendado

Consultar antes y después de enviar un evento para comprobar si aumentan los contadores.

### Qué valida

```text
- La API consulta correctamente la base de datos.
- Existen eventos, reglas y alertas registradas.
- Los contadores reflejan el estado del sistema.
```

---

# 3. Endpoints de eventos

## POST /events

### Función

Crea un evento directamente en la base de datos.

Este endpoint permite registrar eventos, pero no representa el flujo principal del SIEM Lab MVP porque no activa necesariamente la lógica completa de ingesta y reglas.

### Ejemplo

```bash
curl -s -X POST http://127.0.0.1:8000/events \
  -H "Content-Type: application/json" \
  -d '{
    "source": "manual",
    "severity": 3,
    "message": "manual test event",
    "meta": {
      "host": "test-host"
    }
  }' | python3 -m json.tool
```

### Qué valida

```text
- Creación directa de eventos.
- Persistencia en la tabla events.
```

---

## GET /events

### Función

Consulta eventos almacenados.

### Comando

```bash
curl -s http://127.0.0.1:8000/events | python3 -m json.tool
```

### Qué valida

```text
- Consulta de eventos persistidos.
- Acceso a registros de la tabla events desde la API.
```

---

# 4. Endpoint de ingesta

## POST /ingest

### Función

Recibe un evento, lo almacena y activa el motor de reglas.

Este es el endpoint principal del proyecto.

### Comando recomendado

```bash
HOST="demo-$(date +%s)"

curl -s -X POST http://127.0.0.1:8000/ingest \
  -H "Content-Type: application/json" \
  -d "{
    \"source\": \"ssh\",
    \"severity\": 7,
    \"message\": \"failed password for invalid user demo\",
    \"meta\": {
      \"host\": \"$HOST\"
    }
  }" | python3 -m json.tool
```

### Respuesta validada

```json
{
    "id": 18,
    "ts": "2026-05-18T15:25:09.175179Z",
    "source": "ssh",
    "severity": 7,
    "message": "failed password for invalid user demo",
    "meta": {
        "host": "demo-1779117909"
    },
    "created_at": "2026-05-18T15:25:09.180716Z"
}
```

### Qué valida

```text
- Recepción del evento.
- Validación de estructura.
- Persistencia en PostgreSQL.
- Activación posterior del motor de reglas.
```

### Importante

La respuesta de `/ingest` devuelve el evento creado, no la alerta generada.

Para comprobar la alerta, se debe consultar:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

---

# 5. Endpoints de reglas

## GET /rules

### Función

Consulta las reglas configuradas en el sistema.

### Comando

```bash
curl -s http://127.0.0.1:8000/rules | python3 -m json.tool
```

### Campos relevantes

```text
id
name
enabled
source
severity_min
contains
meta_match
throttle_seconds
threshold_count
threshold_seconds
```

### Qué valida

```text
- Existencia de reglas.
- Identificación de reglas activas.
- Condiciones que usa el motor de reglas.
```

---

## POST /rules

### Función

Crea una nueva regla de detección.

### Ejemplo

```bash
curl -s -X POST http://127.0.0.1:8000/rules \
  -H "Content-Type: application/json" \
  -d '{
    "name": "SSH failed login demo",
    "enabled": true,
    "source": "ssh",
    "severity_min": 5,
    "contains": "failed",
    "meta_match": null,
    "throttle_seconds": 60,
    "threshold_count": null,
    "threshold_seconds": null
  }' | python3 -m json.tool
```

### Qué valida

```text
- Creación de reglas desde la API.
- Persistencia en la tabla rules.
- Disponibilidad de reglas para el motor de detección.
```

---

# 6. Endpoints de alertas

## GET /alerts

### Función

Consulta alertas almacenadas en el sistema.

### Comando

```bash
curl -s http://127.0.0.1:8000/alerts | python3 -m json.tool
```

### Qué valida

```text
- Consulta básica de alertas.
- Acceso a la tabla alerts desde la API.
```

---

## GET /alerts/{alert_id}

### Función

Consulta una alerta concreta por su identificador.

### Ejemplo

```bash
curl -s http://127.0.0.1:8000/alerts/8 | python3 -m json.tool
```

### Qué valida

```text
- Consulta individual de alertas.
- Recuperación de una alerta concreta.
```

---

# 7. Endpoints enriquecidos para frontend

## GET /alerts/ui

### Función

Consulta alertas con información enriquecida del evento asociado y la regla activada.

Este endpoint fue creado para facilitar la visualización desde el frontend.

### Comando

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

### Respuesta validada

```json
[
    {
        "id": 8,
        "rule_id": 7,
        "event_id": 19,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1779119427",
        "status": "open",
        "created_at": "2026-05-18T15:50:27.313718Z",
        "updated_at": "2026-05-18T15:50:27.313718Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-18T15:50:27.312118Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    }
]
```

### Qué valida

```text
- Generación de alertas.
- Asociación alerta-evento.
- Asociación alerta-regla.
- Respuesta enriquecida para frontend.
```

---

## GET /alerts/{alert_id}/ui

### Función

Consulta una alerta concreta con información enriquecida.

### Ejemplo

```bash
curl -s "http://127.0.0.1:8000/alerts/8/ui" | python3 -m json.tool
```

### Qué valida

```text
- Consulta detallada de una alerta.
- Información combinada de alerta, evento y regla.
```

---

## GET /alerts/ui/count

### Función

Devuelve el número de alertas que cumplen los filtros aplicados.

### Ejemplo

```bash
curl -s "http://127.0.0.1:8000/alerts/ui/count" | python3 -m json.tool
```

### Qué valida

```text
- Conteo de alertas.
- Apoyo a paginación o indicadores del frontend.
```

---

# 8. Filtros de alertas

## Filtro por estado

### Comando

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?status=ack" | python3 -m json.tool
```

### Estados disponibles

```text
open
ack
closed
```

### Qué valida

```text
- Filtrado por estado.
- Consulta de alertas reconocidas, abiertas o cerradas.
```

---

## Filtro por severidad mínima

### Comando

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?severity_min=7" | python3 -m json.tool
```

### Qué valida

```text
- Filtrado por severidad del evento asociado.
```

---

## Filtro por texto

### Comando

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?q=failed" | python3 -m json.tool
```

### Qué valida

```text
- Búsqueda textual.
- Localización de alertas por contenido del mensaje.
```

---

## Paginación básica

### Ejemplo con limit

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

### Ejemplo con limit y offset

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5&offset=5" | python3 -m json.tool
```

### Qué valida

```text
- Limitación de resultados.
- Consulta por bloques.
```

---

# 9. Cambio de estado de alertas

## PATCH /alerts/{alert_id}

### Función

Modifica el estado de una alerta.

### Ejemplo con alerta 8

```bash
curl -s -X PATCH http://127.0.0.1:8000/alerts/8 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "ack"
  }' | python3 -m json.tool
```

### Estados permitidos

```text
open
ack
closed
```

### Qué valida

```text
- Actualización de alertas.
- Gestión básica del ciclo de vida.
- Cambio de estado desde la API.
```

### Secuencia validada

```text
Alerta 8 → open → ack
```

---

# 10. Secuencia recomendada de prueba completa

## Paso 1. Comprobar API

```bash
curl http://127.0.0.1:8000/health
```

---

## Paso 2. Consultar métricas iniciales

```bash
curl -s http://127.0.0.1:8000/metrics | python3 -m json.tool
```

---

## Paso 3. Consultar reglas

```bash
curl -s http://127.0.0.1:8000/rules | python3 -m json.tool
```

---

## Paso 4. Enviar evento a /ingest

```bash
HOST="demo-$(date +%s)"

curl -s -X POST http://127.0.0.1:8000/ingest \
  -H "Content-Type: application/json" \
  -d "{
    \"source\": \"ssh\",
    \"severity\": 7,
    \"message\": \"failed password for invalid user demo\",
    \"meta\": {
      \"host\": \"$HOST\"
    }
  }" | python3 -m json.tool
```

---

## Paso 5. Consultar alertas generadas

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

---

## Paso 6. Cambiar estado de la alerta

```bash
curl -s -X PATCH http://127.0.0.1:8000/alerts/8 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "ack"
  }' | python3 -m json.tool
```

---

## Paso 7. Ejecutar pruebas automatizadas

```bash
docker compose exec api python -m pytest
```

---

## Conclusión

Los endpoints principales permiten probar el flujo completo del SIEM Lab MVP desde terminal.

La secuencia principal es:

```text
/health → /metrics → /rules → /ingest → /alerts/ui → PATCH /alerts/{id}
```

Estos comandos permiten comprobar que el sistema recibe eventos, los almacena, los evalúa mediante reglas, genera alertas y permite gestionarlas.