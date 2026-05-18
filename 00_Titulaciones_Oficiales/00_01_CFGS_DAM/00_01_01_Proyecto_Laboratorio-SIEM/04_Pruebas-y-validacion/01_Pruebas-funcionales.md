## Introducción

Las pruebas funcionales se realizaron para comprobar que las funcionalidades principales del **SIEM Lab MVP** funcionaban correctamente y que el sistema cumplía el flujo previsto:

```text
evento → ingesta → almacenamiento → evaluación → alerta → consulta
````

El objetivo de estas pruebas no fue medir rendimiento ni carga, sino validar que los componentes principales trabajaban de forma coordinada: API, base de datos, motor de reglas, frontend y servicios Docker.

Las pruebas se realizaron sobre el proyecto ya desplegado en la máquina virtual `siem-lab`, con los servicios levantados mediante Docker Compose.

---

## Criterio general de validación

El sistema se consideró funcional cuando pudo demostrarse el flujo completo:

```text
1. Levantar el entorno.
2. Comprobar que la API responde.
3. Verificar conexión con PostgreSQL.
4. Consultar reglas activas.
5. Enviar un evento mediante /ingest.
6. Generar una alerta automáticamente.
7. Consultar la alerta desde la API.
8. Visualizarla desde el frontend.
9. Cambiar el estado de la alerta.
10. Confirmar los datos desde Adminer.
```

Este criterio permitió validar el comportamiento principal del MVP de extremo a extremo.

---

## Entorno utilizado para las pruebas

Las pruebas se realizaron dentro de la máquina virtual del proyecto.

Servicios principales:

```text
siem-api      → backend FastAPI
siem-db       → base de datos PostgreSQL
siem-adminer  → interfaz web para consultar PostgreSQL
```

El frontend se sirvió de forma independiente mediante el servidor HTTP de Python:

```bash
cd ~/siem-lab
python3 -m http.server 5173 -d frontend
```

URLs utilizadas durante las pruebas:

```text
API / Swagger → http://127.0.0.1:8000/docs
Healthcheck   → http://127.0.0.1:8000/health
Métricas      → http://127.0.0.1:8000/metrics
Adminer       → http://127.0.0.1:8080
Frontend      → http://127.0.0.1:5173/index.html
```

---

## Prueba 1. Comprobación de contenedores Docker

### Objetivo

Verificar que los servicios principales del proyecto estaban levantados correctamente.

### Comando utilizado

```bash
cd ~/siem-lab/docker
docker compose ps
```

### Resultado esperado

Los contenedores principales debían aparecer en ejecución:

```text
siem-db
siem-api
siem-adminer
```

En el caso de PostgreSQL, el servicio debía aparecer como activo o saludable.

### Resultado obtenido

Durante la validación final se comprobó que Docker Compose levantaba correctamente los servicios principales del proyecto.

Servicios validados:

```text
siem-db
siem-api
siem-adminer
```

![[Pasted image 20260518171444.png]]

> salida del comando `docker compose ps` mostrando los tres servicios en ejecución.

### Conclusión

La prueba confirmó que el entorno Docker estaba operativo y que los servicios necesarios para continuar con la validación estaban disponibles.

---

## Prueba 2. Comprobación del endpoint /health

### Objetivo

Comprobar que la API respondía correctamente y que tenía conexión con PostgreSQL.

### Endpoint probado

```http
GET /health
```

### Comando utilizado

```bash
curl http://127.0.0.1:8000/health
```

### Resultado esperado

La API debía devolver una respuesta indicando que tanto el servicio como la base de datos estaban operativos.

Ejemplo esperado:

```json
{
  "status": "ok",
  "db": "ok"
}
```

### Resultado obtenido

El endpoint `/health` respondió correctamente después de resolver el problema de autenticación con PostgreSQL. Esta prueba permitió confirmar que la API y la base de datos estaban comunicándose correctamente.

![[Pasted image 20260518171712.png]]

> terminal mostrando la respuesta de `/health`.

### Problema relacionado

Durante el desarrollo apareció un error de autenticación con PostgreSQL:

```text
FATAL: password authentication failed for user "siem"
```

La causa fue que el volumen persistente de PostgreSQL conservaba una contraseña anterior. Se solucionó actualizando la contraseña del usuario directamente en PostgreSQL y reiniciando la API.

### Conclusión

La prueba confirmó que la API estaba disponible y que la conexión con PostgreSQL funcionaba correctamente.

---

## Prueba 3. Comprobación de Swagger

### Objetivo

Verificar que la documentación interactiva de FastAPI estaba disponible y que los endpoints principales aparecían correctamente.

### URL utilizada

```text
http://127.0.0.1:8000/docs
```

### Resultado esperado

Swagger debía mostrar los módulos principales de la API:

```text
health
info
metrics
events
ingest
rules
alerts
```

### Resultado obtenido

Swagger se mostró correctamente y permitió revisar los endpoints principales del sistema.

![[Pasted image 20260518171858.png]]

>Swagger abierto en `/docs` mostrando los grupos de endpoints.

### Conclusión

La prueba confirmó que FastAPI estaba generando correctamente la documentación interactiva de la API.

---

## Prueba 4. Consulta de métricas

### Objetivo

Comprobar que el sistema podía devolver métricas generales sobre eventos, reglas y alertas.

### Endpoint probado

```http
GET /metrics
```

### Comando utilizado

```bash
curl -s http://127.0.0.1:8000/metrics | python3 -m json.tool
```

### Resultado esperado

El endpoint debía devolver contadores generales del sistema:

```text
events_total
rules_total
rules_enabled
alerts_total
```

### Resultado obtenido

Durante la validación final se utilizaron las métricas para comprobar que el número de eventos y alertas aumentaba tras enviar un evento mediante `/ingest`.

Antes de la prueba de ingesta:

```text
events_total: 16
rules_total: 7
rules_enabled: 2
alerts_total: 4
```

Después de enviar el evento de demo:

```text
events_total: 17
rules_total: 7
rules_enabled: 2
alerts_total: 5
```

![[Pasted image 20260518172032.png]]

> salida de `/metrics` antes y después de enviar el evento de prueba.

### Conclusión

La prueba confirmó que el sistema registraba correctamente nuevos eventos y alertas, y que las métricas reflejaban esos cambios.

---

## Prueba 5. Consulta de reglas

### Objetivo

Verificar que existían reglas configuradas y que el sistema podía consultarlas desde la API.

### Endpoint probado

```http
GET /rules
```

### Comando utilizado

```bash
curl -s http://127.0.0.1:8000/rules | python3 -m json.tool
```

### Resultado esperado

La API debía devolver una lista de reglas disponibles, incluyendo su estado de activación.

### Resultado obtenido

Durante la validación final se comprobó que el sistema tenía reglas existentes y que había reglas activas.

Reglas relevantes validadas:

```text
test_rule_ssh
Auth brute 3 in 60 any-host
```

La regla `test_rule_ssh` permitía detectar eventos de tipo SSH con severidad suficiente y mensaje que contuviera la palabra `failed`.

### Evidencia recomendada para la memoria

![[Pasted image 20260518172407.png]]

```bash
endurance@siem-lab:~/siem-lab/docker$ curl -s http://127.0.0.1:8000/rules | python3 -m json.tool
[
    {
        "id": 7,
        "name": "test_rule_ssh",
        "enabled": true,
        "source": "ssh",
        "severity_min": 5,
        "contains": "failed",
        "throttle_seconds": 60,
        "threshold_count": null,
        "threshold_seconds": null,
        "meta_match": null,
        "created_at": "2026-01-17T07:54:45.503764Z"
    },
    {
        "id": 6,
        "name": "Auth brute 3 in 60 any-host",
        "enabled": true,
        "source": null,
        "severity_min": 7,
        "contains": null,
        "throttle_seconds": 0,
        "threshold_count": 3,
        "threshold_seconds": 60,
        "meta_match": {
            "facility": "auth"
        },
        "created_at": "2026-01-16T10:51:57.093679Z"
    },
    {
        "id": 5,
        "name": "Auth brute 3 in 60 no-throttle",
        "enabled": false,
        "source": null,
        "severity_min": 7,
        "contains": null,
        "throttle_seconds": 0,
        "threshold_count": 3,
        "threshold_seconds": 60,
        "meta_match": {
            "host": "kali",
            "facility": "auth"
        },
        "created_at": "2026-01-16T10:04:32.797663Z"
    },
    {
        "id": 4,
        "name": "Auth brute 3 in 60 A",
        "enabled": false,
        "source": null,
        "severity_min": 7,
        "contains": null,
        "throttle_seconds": 120,
        "threshold_count": 3,
        "threshold_seconds": 60,
        "meta_match": {
            "host": "kali",
            "facility": "auth"
        },
        "created_at": "2026-01-15T19:35:52.259451Z"
    },
    {
        "id": 3,
        "name": "Auth brute 3 in 60 v2",
        "enabled": false,
        "source": null,
        "severity_min": 7,
        "contains": null,
        "throttle_seconds": 120,
        "threshold_count": 3,
        "threshold_seconds": 60,
        "meta_match": {
            "host": "kali",
            "facility": "auth"
        },
        "created_at": "2026-01-15T19:03:11.201935Z"
    },
    {
        "id": 2,
        "name": "Auth brute 3 in 60",
        "enabled": false,
        "source": null,
        "severity_min": 7,
        "contains": null,
        "throttle_seconds": null,
        "threshold_count": null,
        "threshold_seconds": null,
        "meta_match": {
            "host": "kali",
            "facility": "auth"
        },
        "created_at": "2026-01-15T18:58:17.613873Z"
    },
    {
        "id": 1,
        "name": "Auth on kali sev>=7",
        "enabled": false,
        "source": null,
        "severity_min": 7,
        "contains": null,
        "throttle_seconds": null,
        "threshold_count": null,
        "threshold_seconds": null,
        "meta_match": {
            "host": "kali",
            "facility": "auth"
        },
        "created_at": "2026-01-15T16:43:21.529104Z"
    }
]
endurance@siem-lab:~/siem-lab/docker$ 
```

>  respuesta de `/rules` mostrando las reglas existentes y sus campos principales.

### Conclusión

La prueba confirmó que el sistema disponía de reglas activas para evaluar eventos durante la ingesta.

---

## Prueba 6. Ingesta de evento simulado

### Objetivo

Comprobar que el endpoint `/ingest` recibe correctamente un evento simulado, valida su estructura y lo almacena en la base de datos.

Esta prueba permite verificar la primera parte del flujo principal del sistema:

```text
evento simulado → POST /ingest → almacenamiento en PostgreSQL
````

La generación de alertas se valida en la prueba siguiente, ya que la respuesta de `/ingest` devuelve el evento creado, pero no muestra directamente la alerta generada.

---

### Endpoint probado

```http
POST /ingest
```

---

### Evento utilizado

Se envió un evento simulado de tipo SSH con severidad 7 y un mensaje de intento fallido de autenticación.

Para evitar problemas con duplicados o agrupaciones anteriores, se utilizó un valor dinámico en `meta.host`.

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

### Resultado esperado

El sistema debía recibir el evento, validar los datos enviados y almacenarlo correctamente.

El evento debía conservar los campos principales:

```text
source
severity
message
meta.host
```

Además, la API debía devolver una respuesta con el identificador del evento creado y sus fechas asociadas.

---

### Resultado obtenido

El endpoint `/ingest` respondió correctamente y devolvió el evento creado.

Salida obtenida:

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

Este resultado confirma que:

```text
- El endpoint /ingest estaba operativo.
- El evento fue recibido correctamente.
- El evento fue almacenado con id 18.
- El campo source se guardó como ssh.
- La severidad se guardó con valor 7.
- El mensaje se almacenó correctamente.
- El campo meta.host se recibió con el valor demo-1779117909.
- La API generó los campos temporales ts y created_at.
```

---

### Interpretación del resultado

Esta prueba valida la ingesta y persistencia del evento, pero no demuestra por sí sola la generación de una alerta.

Para confirmar que el evento también activó una regla y generó una alerta, es necesario consultar posteriormente los endpoints de métricas o alertas:

```bash
curl -s "http://127.0.0.1:8000/metrics" | python3 -m json.tool
```

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

Por este motivo, la generación de alertas se documenta como una prueba independiente.

---

```bash
endurance@siem-lab:~/siem-lab/docker$ HOST="demo-$(date +%s)"

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
endurance@siem-lab:~/siem-lab/docker$ curl -s "http://127.0.0.1:8000/metrics" | python3 -m json.tool
{
    "events_total": 18,
    "rules_total": 7,
    "rules_enabled": 2,
    "alerts_total": 6,
    "alerts_by_status": {
        "ack": 2,
        "closed": 2,
        "open": 2
    },
    "alerts_by_group_key_top": {
        "kali": 2,
        "demo-1778929393": 1,
        "vm1": 1,
        "win11": 1,
        "demo-1779117909": 1
    }
}
endurance@siem-lab:~/siem-lab/docker$ curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
[
    {
        "id": 7,
        "rule_id": 7,
        "event_id": 18,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1779117909",
        "status": "open",
        "created_at": "2026-05-18T15:25:09.180716Z",
        "updated_at": "2026-05-18T15:25:09.180716Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-18T15:25:09.175179Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    },
    {
        "id": 6,
        "rule_id": 7,
        "event_id": 17,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1778929393",
        "status": "ack",
        "created_at": "2026-05-16T11:03:13.407991Z",
        "updated_at": "2026-05-16T11:05:36.705119Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-16T11:03:13.403746Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    },
    {
        "id": 5,
        "rule_id": 7,
        "event_id": 14,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "vm1",
        "status": "ack",
        "created_at": "2026-01-17T07:55:05.826924Z",
        "updated_at": "2026-01-17T14:04:27.654930Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-01-17T07:55:05.768740Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user"
    },
    {
        "id": 4,
        "rule_id": 6,
        "event_id": 13,
        "title": "Rule matched: Auth brute 3 in 60 any-host",
        "group_key": "kali",
        "status": "closed",
        "created_at": "2026-01-16T16:19:02.756862Z",
        "updated_at": "2026-01-17T14:04:44.320880Z",
        "rule_name": "Auth brute 3 in 60 any-host",
        "event_ts": "2026-01-16T16:19:02.756388Z",
        "event_source": "syslog",
        "event_severity": 7,
        "event_message": "ssh fail rearm 3"
    },
    {
        "id": 2,
        "rule_id": 6,
        "event_id": 6,
        "title": "Rule matched: Auth brute 3 in 60 any-host",
        "group_key": "win11",
        "status": "open",
        "created_at": "2026-01-16T11:35:09.449952Z",
        "updated_at": "2026-01-16T12:06:32.638684Z",
        "rule_name": "Auth brute 3 in 60 any-host",
        "event_ts": "2026-01-16T11:35:09.446991Z",
        "event_source": "syslog",
        "event_severity": 7,
        "event_message": "ssh fail"
    }
]
endurance@siem-lab:~/siem-lab/docker$ 
```

![[Pasted image 20260518173423.png]]

> terminal mostrando el comando `POST /ingest` y la respuesta JSON con el evento creado.

---

### Conclusión

La prueba confirmó que la API de ingesta funcionaba correctamente. El sistema fue capaz de recibir un evento simulado, procesarlo y devolver el registro creado con sus datos principales.

Esta validación demuestra que la primera parte del flujo del SIEM Lab MVP funciona correctamente. La comprobación de la alerta generada se realiza en la prueba posterior.
## Prueba 7. Generación y consulta de alerta

### Objetivo

Comprobar que la alerta generada por el evento podía consultarse desde la API.

### Endpoint probado

```http
GET /alerts/ui
```

### Comando utilizado

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

### Resultado esperado

La respuesta debía mostrar la alerta generada, incluyendo datos de la alerta y del evento asociado.

### Resultado obtenido

La alerta generada apareció correctamente en la consulta enriquecida de `/alerts/ui`.

La alerta mostraba información relacionada con:

```text
- ID de alerta.
- Regla activada.
- Evento asociado.
- Estado.
- Source del evento.
- Severidad.
- Mensaje.
- group_key.
```

```bash
endurance@siem-lab:~/siem-lab/docker$ curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
[
    {
        "id": 7,
        "rule_id": 7,
        "event_id": 18,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1779117909",
        "status": "open",
        "created_at": "2026-05-18T15:25:09.180716Z",
        "updated_at": "2026-05-18T15:25:09.180716Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-18T15:25:09.175179Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    },
    {
        "id": 6,
        "rule_id": 7,
        "event_id": 17,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1778929393",
        "status": "ack",
        "created_at": "2026-05-16T11:03:13.407991Z",
        "updated_at": "2026-05-16T11:05:36.705119Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-16T11:03:13.403746Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    },
    {
        "id": 5,
        "rule_id": 7,
        "event_id": 14,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "vm1",
        "status": "ack",
        "created_at": "2026-01-17T07:55:05.826924Z",
        "updated_at": "2026-01-17T14:04:27.654930Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-01-17T07:55:05.768740Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user"
    },
    {
        "id": 4,
        "rule_id": 6,
        "event_id": 13,
        "title": "Rule matched: Auth brute 3 in 60 any-host",
        "group_key": "kali",
        "status": "closed",
        "created_at": "2026-01-16T16:19:02.756862Z",
        "updated_at": "2026-01-17T14:04:44.320880Z",
        "rule_name": "Auth brute 3 in 60 any-host",
        "event_ts": "2026-01-16T16:19:02.756388Z",
        "event_source": "syslog",
        "event_severity": 7,
        "event_message": "ssh fail rearm 3"
    },
    {
        "id": 2,
        "rule_id": 6,
        "event_id": 6,
        "title": "Rule matched: Auth brute 3 in 60 any-host",
        "group_key": "win11",
        "status": "open",
        "created_at": "2026-01-16T11:35:09.449952Z",
        "updated_at": "2026-01-16T12:06:32.638684Z",
        "rule_name": "Auth brute 3 in 60 any-host",
        "event_ts": "2026-01-16T11:35:09.446991Z",
        "event_source": "syslog",
        "event_severity": 7,
        "event_message": "ssh fail"
    }
]
endurance@siem-lab:~/siem-lab/docker$ 
```

![[Pasted image 20260518173556.png]]

> salida de `/alerts/ui?limit=5` mostrando la alerta generada.

### Conclusión

La prueba confirmó que las alertas generadas podían consultarse correctamente mediante los endpoints de la API.

---

## Prueba 8. Filtros de alertas

### Objetivo

Comprobar que el sistema permitía filtrar alertas para facilitar su consulta.

### Endpoints probados

```http
GET /alerts/ui?status=ack
GET /alerts/ui?severity_min=7
GET /alerts/ui?q=failed
```

### Comandos utilizados

Filtro por estado:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?status=ack" | python3 -m json.tool
```

Filtro por severidad mínima:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?severity_min=7" | python3 -m json.tool
```

Filtro por búsqueda textual:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?q=failed" | python3 -m json.tool
```

### Resultado esperado

Cada filtro debía devolver únicamente las alertas que cumplieran la condición indicada.

### Resultado obtenido

Durante la validación se comprobó que los filtros por estado, severidad y texto funcionaban correctamente.

```bash
endurance@siem-lab:~/siem-lab/docker$ curl -s "http://127.0.0.1:8000/alerts/ui?status=ack" | python3 -m json.tool
[
    {
        "id": 6,
        "rule_id": 7,
        "event_id": 17,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1778929393",
        "status": "ack",
        "created_at": "2026-05-16T11:03:13.407991Z",
        "updated_at": "2026-05-16T11:05:36.705119Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-16T11:03:13.403746Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    },
    {
        "id": 5,
        "rule_id": 7,
        "event_id": 14,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "vm1",
        "status": "ack",
        "created_at": "2026-01-17T07:55:05.826924Z",
        "updated_at": "2026-01-17T14:04:27.654930Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-01-17T07:55:05.768740Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user"
    }
]
endurance@siem-lab:~/siem-lab/docker$ curl -s "http://127.0.0.1:8000/alerts/ui?severity_min=7" | python3 -m json.tool
[
    {
        "id": 7,
        "rule_id": 7,
        "event_id": 18,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1779117909",
        "status": "open",
        "created_at": "2026-05-18T15:25:09.180716Z",
        "updated_at": "2026-05-18T15:25:09.180716Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-18T15:25:09.175179Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    },
    {
        "id": 6,
        "rule_id": 7,
        "event_id": 17,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1778929393",
        "status": "ack",
        "created_at": "2026-05-16T11:03:13.407991Z",
        "updated_at": "2026-05-16T11:05:36.705119Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-16T11:03:13.403746Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    },
    {
        "id": 5,
        "rule_id": 7,
        "event_id": 14,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "vm1",
        "status": "ack",
        "created_at": "2026-01-17T07:55:05.826924Z",
        "updated_at": "2026-01-17T14:04:27.654930Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-01-17T07:55:05.768740Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user"
    },
    {
        "id": 4,
        "rule_id": 6,
        "event_id": 13,
        "title": "Rule matched: Auth brute 3 in 60 any-host",
        "group_key": "kali",
        "status": "closed",
        "created_at": "2026-01-16T16:19:02.756862Z",
        "updated_at": "2026-01-17T14:04:44.320880Z",
        "rule_name": "Auth brute 3 in 60 any-host",
        "event_ts": "2026-01-16T16:19:02.756388Z",
        "event_source": "syslog",
        "event_severity": 7,
        "event_message": "ssh fail rearm 3"
    },
    {
        "id": 2,
        "rule_id": 6,
        "event_id": 6,
        "title": "Rule matched: Auth brute 3 in 60 any-host",
        "group_key": "win11",
        "status": "open",
        "created_at": "2026-01-16T11:35:09.449952Z",
        "updated_at": "2026-01-16T12:06:32.638684Z",
        "rule_name": "Auth brute 3 in 60 any-host",
        "event_ts": "2026-01-16T11:35:09.446991Z",
        "event_source": "syslog",
        "event_severity": 7,
        "event_message": "ssh fail"
    },
    {
        "id": 1,
        "rule_id": 6,
        "event_id": 3,
        "title": "Rule matched: Auth brute 3 in 60 any-host",
        "group_key": "kali",
        "status": "closed",
        "created_at": "2026-01-16T11:35:09.350069Z",
        "updated_at": "2026-01-16T14:43:52.681078Z",
        "rule_name": "Auth brute 3 in 60 any-host",
        "event_ts": "2026-01-16T11:35:09.345742Z",
        "event_source": "syslog",
        "event_severity": 7,
        "event_message": "ssh fail"
    }
]
endurance@siem-lab:~/siem-lab/docker$ curl -s "http://127.0.0.1:8000/alerts/ui?q=failed" | python3 -m json.tool
[
    {
        "id": 7,
        "rule_id": 7,
        "event_id": 18,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1779117909",
        "status": "open",
        "created_at": "2026-05-18T15:25:09.180716Z",
        "updated_at": "2026-05-18T15:25:09.180716Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-18T15:25:09.175179Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    },
    {
        "id": 6,
        "rule_id": 7,
        "event_id": 17,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "demo-1778929393",
        "status": "ack",
        "created_at": "2026-05-16T11:03:13.407991Z",
        "updated_at": "2026-05-16T11:05:36.705119Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-05-16T11:03:13.403746Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user demo"
    },
    {
        "id": 5,
        "rule_id": 7,
        "event_id": 14,
        "title": "Rule matched: test_rule_ssh",
        "group_key": "vm1",
        "status": "ack",
        "created_at": "2026-01-17T07:55:05.826924Z",
        "updated_at": "2026-01-17T14:04:27.654930Z",
        "rule_name": "test_rule_ssh",
        "event_ts": "2026-01-17T07:55:05.768740Z",
        "event_source": "ssh",
        "event_severity": 7,
        "event_message": "failed password for invalid user"
    }
]
endurance@siem-lab:~/siem-lab/docker$ 
```


![[Pasted image 20260518173841.png]]

> salidas de terminal mostrando filtros aplicados sobre `/alerts/ui`.

### Conclusión

La prueba confirmó que la API permitía consultar alertas de forma más precisa y no únicamente como listado completo.

---

## Prueba 9. Cambio de estado de una alerta

### Objetivo

Comprobar que una alerta podía cambiar de estado mediante la API.

### Endpoint probado

```http
PATCH /alerts/{alert_id}
```

### Comando utilizado

```bash
curl -s -X PATCH http://127.0.0.1:8000/alerts/6 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "ack"
  }' | python3 -m json.tool
```

### Resultado esperado

La alerta debía cambiar su estado de `open` a `ack`.

### Resultado obtenido

La alerta con ID `6` cambió correctamente su estado a:

```text
ack
```

![[Pasted image 20260518174000.png]]

> salida del comando `PATCH /alerts/6` mostrando `status: ack`.

### Conclusión

La prueba confirmó que el sistema permitía modificar el estado de una alerta y representar una gestión básica de alertas.

---

## Prueba 10. Visualización desde frontend

### Objetivo

Comprobar que el frontend podía mostrar las alertas generadas por el backend.

### Comando para servir el frontend

```bash
cd ~/siem-lab
python3 -m http.server 5173 -d frontend
```

### URL utilizada

```text
http://127.0.0.1:5173/index.html
```

### Resultado esperado

El frontend debía cargar correctamente y mostrar las alertas obtenidas desde la API.

### Resultado obtenido

El frontend cargó correctamente y mostró las alertas.

Durante la validación final, inicialmente parecía mostrar solo las alertas anteriores, pero al pulsar la opción de actualizar apareció la alerta nueva. Esto confirmó que el frontend consumía correctamente la API y que la alerta generada estaba disponible.

![[Pasted image 20260518174149.png]]

![[Pasted image 20260518174354.png]]

> frontend mostrando el listado de alertas, incluyendo la alerta generada durante la prueba.

### Conclusión

La prueba confirmó que el frontend cumplía su función como interfaz visual básica para consultar alertas.

---

## Prueba 11. Validación desde Adminer

### Objetivo

Comprobar visualmente que los datos estaban almacenados en PostgreSQL.

### URL utilizada

```text
http://127.0.0.1:8080
```

### Tablas revisadas

```text
events
rules
alerts
alembic_version
```

### Resultado esperado

Adminer debía permitir acceder a la base de datos y visualizar las tablas principales.

### Resultado obtenido

Adminer permitió revisar las tablas principales del sistema y comprobar la existencia de eventos, reglas y alertas.

![[Pasted image 20260518174523.png]]

![[Pasted image 20260518174606.png]]

> Adminer mostrando las tablas `events`, `rules`, `alerts` y `alembic_version`.

### Conclusión

La prueba confirmó que los datos persistían correctamente en PostgreSQL y podían inspeccionarse desde Adminer.

---

## Resumen de resultados

|Prueba|Resultado|
|---|---|
|Contenedores Docker|Validado|
|`/health`|Validado|
|Swagger `/docs`|Validado|
|`/metrics`|Validado|
|`/rules`|Validado|
|`/ingest`|Validado|
|Generación de alertas|Validado|
|Consulta `/alerts/ui`|Validado|
|Filtros de alertas|Validado|
|Cambio de estado|Validado|
|Frontend|Validado|
|Adminer|Validado|

---

## Problemas detectados durante las pruebas

Durante las pruebas se detectaron varios puntos relevantes:

```text
- Error de autenticación entre API y PostgreSQL.
- Persistencia de credenciales antiguas en el volumen Docker.
- Necesidad de diferenciar entre /events y /ingest.
- Necesidad de usar un host dinámico para evitar duplicados en pruebas.
- El frontend necesitaba actualizar la vista para mostrar la última alerta.
- Las pruebas automatizadas debían ejecutarse dentro del contenedor API.
```

Estos problemas fueron resueltos o documentados, y permitieron mejorar la comprensión del funcionamiento interno del sistema.

---

## Conclusión

Las pruebas funcionales confirmaron que el SIEM Lab MVP funciona correctamente como versión mínima del sistema.

El proyecto fue capaz de recibir eventos simulados, almacenarlos, evaluarlos mediante reglas, generar alertas, consultarlas, filtrarlas, modificar su estado y mostrarlas desde una interfaz web.

Por tanto, el flujo principal del sistema quedó validado de extremo a extremo.
