## Introducción

Tras realizar las pruebas funcionales, las pruebas de ingesta, las pruebas del motor de reglas, las pruebas del frontend y las pruebas automatizadas, se confirmó que el **SIEM Lab MVP** funciona correctamente como versión mínima del sistema.

El flujo principal validado fue:

```text
evento simulado → ingesta → almacenamiento → evaluación → alerta → consulta → gestión
````

El objetivo de esta nota es recoger el estado final del proyecto y resumir qué partes quedaron validadas.

---

## Estado general del sistema

El sistema quedó operativo y permitió demostrar el funcionamiento completo del laboratorio.

Componentes validados:

```text
- Máquina virtual siem-lab.
- Servicios Docker.
- API FastAPI.
- Base de datos PostgreSQL.
- Adminer.
- Swagger.
- API de ingesta.
- Motor de reglas.
- Gestión de alertas.
- Frontend.
- Pruebas automatizadas.
```

Cada componente cumplió una función dentro del flujo general del proyecto.

---

## Servicios validados

Los servicios principales se levantaron mediante Docker Compose.

Servicios validados:

```text
siem-api      → backend FastAPI
siem-db       → base de datos PostgreSQL
siem-adminer  → consulta visual de PostgreSQL
```

Puertos principales utilizados:

```text
8000 → API FastAPI
8080 → Adminer
5173 → Frontend
```

El entorno quedó preparado para ejecutar la aplicación, consultar la base de datos y visualizar las alertas desde navegador.

---

## Resultado de la API

La API respondió correctamente durante las pruebas.

Endpoints principales validados:

```text
GET /health
GET /info
GET /metrics
GET /rules
POST /ingest
GET /alerts
GET /alerts/ui
GET /alerts/ui/count
GET /alerts/{alert_id}/ui
PATCH /alerts/{alert_id}
```

El endpoint `/health` permitió comprobar que la API y la base de datos estaban operativas.

El endpoint `/metrics` permitió consultar contadores generales de eventos, reglas y alertas.

Swagger permitió revisar y probar los endpoints desde el navegador.

---

## Resultado de la base de datos

PostgreSQL almacenó correctamente la información generada por el sistema.

Tablas validadas:

```text
events
rules
alerts
alembic_version
```

La tabla `events` almacenó los eventos recibidos mediante `/ingest`.

La tabla `rules` almacenó las reglas de detección.

La tabla `alerts` almacenó las alertas generadas por el motor de reglas.

La tabla `alembic_version` permitió controlar el estado de las migraciones gestionadas por Alembic.

Adminer permitió comprobar visualmente que las tablas y registros existían en la base de datos.

---

## Resultado de la ingesta

La ingesta de eventos funcionó correctamente.

Se validó el envío de un evento SSH simulado mediante el endpoint:

```http
POST /ingest
```

Evento creado:

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

Este resultado confirmó que `/ingest` recibió el evento, validó la estructura y devolvió el registro creado.

La respuesta de `/ingest` valida la ingesta del evento, pero no debe confundirse con la generación de la alerta. La alerta se comprueba posteriormente mediante `/alerts/ui`.

---

## Resultado del motor de reglas

El motor de reglas generó alertas correctamente cuando el evento coincidió con una regla activa.

Regla utilizada:

```text
test_rule_ssh
```

Condiciones principales:

```text
source = ssh
severity_min = 5
contains = failed
```

Evento evaluado:

```text
event_id: 19
source: ssh
severity: 7
message: failed password for invalid user demo
meta.host: demo-1779119427
```

Alerta generada:

```json
{
    "id": 8,
    "rule_id": 7,
    "event_id": 19,
    "title": "Rule matched: test_rule_ssh",
    "group_key": "demo-1779119427",
    "status": "open",
    "rule_name": "test_rule_ssh",
    "event_source": "ssh",
    "event_severity": 7,
    "event_message": "failed password for invalid user demo"
}
```

Relación validada:

```text
Evento 19 → Regla test_rule_ssh → Alerta 8
```

También se observó una ejecución anterior válida:

```text
Evento 18 → Regla test_rule_ssh → Alerta 7
```

Esto confirma que el comportamiento del motor de reglas se mantiene en distintas ejecuciones.

---

## Resultado de la gestión de alertas

La gestión básica de alertas quedó validada.

Estados contemplados:

```text
open
ack
closed
```

Las alertas nuevas se generan inicialmente en estado:

```text
open
```

Para validar el cambio de estado de forma coordinada con la alerta más reciente, se utiliza la alerta `8`.

Comando de actualización:

```bash
curl -s -X PATCH http://127.0.0.1:8000/alerts/8 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "ack"
  }' | python3 -m json.tool
```

Resultado esperado:

```text
alert_id: 8
status: ack
```

Comprobación posterior:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

Esta prueba permite cerrar la secuencia de validación de forma limpia:

```text
Evento 19 → Alerta 8 → Estado open → Estado ack
```

---

## Resultado de los filtros

Los filtros de alertas funcionaron correctamente.

Filtros validados:

```text
status
severity_min
q
limit
offset
```

Ejemplos de consultas utilizadas:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?status=ack" | python3 -m json.tool
```

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?severity_min=7" | python3 -m json.tool
```

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?q=failed" | python3 -m json.tool
```

Estos filtros permitieron consultar alertas de forma más precisa y comprobar que la API no se limitaba a devolver un listado completo sin control.

---

## Resultado del frontend

El frontend cargó correctamente desde el navegador.

URL utilizada:

```text
http://127.0.0.1:5173/index.html
```

El frontend consumió datos procedentes de:

```http
GET /alerts/ui
```

y permitió visualizar alertas generadas por el sistema.

Durante la validación se comprobó que podía ser necesario actualizar manualmente la vista para mostrar la alerta más reciente. Este comportamiento es coherente con el alcance del MVP, ya que no se implementó actualización en tiempo real.

Flujo validado:

```text
alerta generada → /alerts/ui → frontend → visualización
```

---

## Resultado de Adminer

Adminer permitió consultar visualmente la base de datos.

URL utilizada:

```text
http://127.0.0.1:8080
```

Desde Adminer se pudieron revisar las tablas principales:

```text
events
rules
alerts
alembic_version
```

Esta herramienta permitió confirmar que los eventos, reglas y alertas estaban persistidos en PostgreSQL.

---

## Resultado de las pruebas automatizadas

Las pruebas automatizadas se ejecutaron dentro del contenedor de la API.

Comando utilizado:

```bash
cd ~/siem-lab/docker
docker compose exec api python -m pytest
```

Resultado obtenido:

```text
4 passed in 1.00s
```

Este resultado confirmó que las pruebas automatizadas disponibles se superaron correctamente.

El uso del contenedor `siem-api` fue importante porque el entorno local no tenía `pytest` instalado. Ejecutar las pruebas dentro del contenedor permitió utilizar el entorno real del backend.

---

## Resumen de validación

|Componente o funcionalidad|Resultado|
|---|---|
|Máquina virtual `siem-lab`|Validado|
|Docker Compose|Validado|
|Servicio `siem-api`|Validado|
|Servicio `siem-db`|Validado|
|Servicio `siem-adminer`|Validado|
|API FastAPI|Validado|
|PostgreSQL|Validado|
|Adminer|Validado|
|Swagger `/docs`|Validado|
|`/health`|Validado|
|`/metrics`|Validado|
|`/rules`|Validado|
|`/ingest`|Validado|
|Motor de reglas|Validado|
|Generación de alertas|Validado|
|Consulta `/alerts/ui`|Validado|
|Filtros de alertas|Validado|
|Cambio de estado de alerta|Validado|
|Frontend|Validado|
|Pytest|Validado|

---

## Problemas detectados durante la validación

Durante la validación final se identificaron varios puntos importantes:

```text
- La respuesta de /ingest valida la creación del evento, pero no muestra directamente la alerta generada.
- La alerta debe comprobarse mediante /alerts/ui o mediante el incremento de alerts_total en /metrics.
- Es importante no confundir event_id con alert_id.
- El uso de meta.host dinámico ayuda a evitar problemas con duplicados o throttle.
- El frontend puede requerir actualización manual para mostrar la alerta más reciente.
- Las pruebas automatizadas deben ejecutarse dentro del contenedor api.
- Los volúmenes persistentes de Docker pueden conservar configuraciones anteriores de PostgreSQL.
```

Estos puntos permitieron ajustar la documentación y evitar interpretaciones incorrectas de los resultados.

---

## Resultado final del flujo principal

El flujo principal quedó validado correctamente:

```text
1. Se envía un evento SSH simulado mediante /ingest.
2. La API recibe el evento.
3. El evento se almacena en PostgreSQL.
4. El motor de reglas consulta reglas activas.
5. La regla test_rule_ssh coincide con el evento.
6. El sistema genera una alerta.
7. La alerta queda asociada al evento y a la regla.
8. La alerta puede consultarse desde /alerts/ui.
9. El frontend puede mostrarla.
10. La alerta puede cambiar de estado.
```

Secuencia principal documentada:

```text
Evento 19 → Regla test_rule_ssh → Alerta 8 → Estado open → Estado ack
```

---

## Conclusión

Los resultados finales confirman que el SIEM Lab MVP funciona correctamente como versión mínima del sistema.

El proyecto cumple su objetivo principal: recibir eventos simulados, almacenarlos, evaluarlos mediante reglas, generar alertas y permitir su consulta desde API y frontend.

Aunque existen limitaciones propias de un MVP, el flujo principal quedó validado de extremo a extremo y el sistema puede considerarse funcional.