## Introducción

La API de ingesta es una de las partes principales del SIEM Lab MVP. Su función es recibir eventos simulados, almacenarlos en la base de datos y activar el proceso de evaluación mediante reglas.

El endpoint principal es:

```http
POST /ingest
````

Este endpoint representa el punto de entrada del flujo principal del sistema.

---

## Función de la ingesta

La ingesta permite introducir eventos en el sistema para que puedan ser procesados.

El flujo básico es:

```text
evento recibido → validación → almacenamiento → evaluación → alerta
```

A diferencia de los endpoints `/events`, que permiten trabajar con eventos de forma más directa, `/ingest` activa el comportamiento completo del sistema.

Por este motivo, `/ingest` es el endpoint más representativo del proyecto.

---

## Estructura de un evento

Los eventos se envían en formato JSON.

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

Campos principales:

```text
source   → origen del evento
severity → nivel de severidad
message  → mensaje descriptivo
meta     → metadatos adicionales
```

Esta estructura permite representar eventos simples, pero suficientemente útiles para ser evaluados por reglas.

---

## Campo source

El campo `source` indica el origen del evento.

Ejemplos posibles:

```text
ssh
auth
web
firewall
system
```

Este campo permite que una regla se aplique únicamente a eventos de una fuente concreta.

Ejemplo:

```text
source = ssh
```

---

## Campo severity

El campo `severity` indica la gravedad del evento mediante un valor numérico.

Ejemplo:

```json
{
  "severity": 7
}
```

Las reglas pueden utilizar este valor mediante la condición `severity_min`.

Ejemplo:

```text
severity_min = 5
```

En este caso, la regla solo tendrá en cuenta eventos con severidad igual o superior a 5.

---

## Campo message

El campo `message` contiene la descripción principal del evento.

Ejemplo:

```text
failed password for invalid user demo
```

Las reglas pueden buscar texto dentro del mensaje mediante la condición `contains`.

Ejemplo:

```text
contains = failed
```

Si el mensaje contiene esa palabra, la condición se cumple.

---

## Campo meta

El campo `meta` permite añadir información adicional al evento.

Ejemplo:

```json
{
  "meta": {
    "host": "server-01",
    "ip": "192.168.1.50",
    "user": "demo"
  }
}
```

En esta versión del proyecto, el metadato más importante es:

```text
meta.host
```

A partir de este valor se calcula el `group_key`, utilizado para agrupar eventos relacionados.

---

## Flujo interno de /ingest

Cuando se envía un evento a `/ingest`, el sistema realiza los siguientes pasos:

```text
1. Recibe la petición HTTP.
2. Valida la estructura del evento.
3. Guarda el evento en PostgreSQL.
4. Calcula el group_key a partir de meta.host.
5. Consulta las reglas activas.
6. Evalúa el evento contra cada regla.
7. Genera una alerta si hay coincidencia.
8. Guarda la alerta en PostgreSQL.
9. Devuelve una respuesta al usuario.
```

Este flujo conecta la API, la base de datos y el motor de reglas.

---

## Diferencia entre /events y /ingest

Durante el desarrollo fue importante diferenciar entre los endpoints `/events` y `/ingest`.

Los endpoints de eventos permiten crear o consultar eventos:

```http
POST /events
GET /events
```

Sin embargo, el endpoint `/ingest` representa el flujo completo del SIEM:

```http
POST /ingest
```

Diferencia principal:

```text
/events → trabaja con eventos
/ingest → recibe eventos y activa el motor de reglas
```

Por tanto, para demostrar la generación automática de alertas, el endpoint correcto es `/ingest`.

---

## Evaluación mediante reglas

Después de guardar el evento, el sistema consulta las reglas activas.

Solo se evalúan reglas con:

```text
enabled = true
```

Cada regla puede comprobar condiciones como:

```text
source
severity_min
contains
meta_match
threshold_count
threshold_seconds
throttle_seconds
```

Si el evento cumple las condiciones de una regla, el sistema genera una alerta.

---

## Ejemplo de regla aplicada

Evento recibido:

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

Resultado:

```text
El evento coincide con la regla y se genera una alerta.
```

---

## Respuesta esperada

Tras enviar un evento válido, el sistema debe devolver una respuesta indicando que el evento ha sido procesado.

El resultado esperado es que:

```text
- El evento quede registrado en la tabla events.
- Se evalúen las reglas activas.
- Se genere una alerta si hay coincidencia.
- La alerta quede registrada en la tabla alerts.
```

La comprobación puede hacerse desde:

```text
- Swagger
- curl
- Adminer
- /alerts/ui
- Frontend
```

---

## Prueba de ingesta validada

Durante la validación final se utilizó un evento de prueba de tipo SSH.

Comando utilizado:

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

Este evento generó correctamente una alerta al coincidir con una regla activa.

---

## Consulta posterior de la alerta

Después de enviar el evento, se consultaron las alertas mediante:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

La alerta generada apareció correctamente en la respuesta.

También pudo visualizarse desde el frontend.

---

## Datos validados

Durante la prueba final, las métricas del sistema aumentaron tras la ingesta.

Antes de la prueba existían:

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

Este cambio confirmó que el evento se almacenó y que se generó una nueva alerta.

---

## Problemas y decisiones durante el desarrollo

Uno de los puntos importantes fue definir que `/ingest` debía ser el endpoint principal del proyecto.

Inicialmente podía parecer suficiente crear eventos mediante `/events`, pero eso no representaba el flujo completo del SIEM. Por este motivo, se diferenció claramente entre guardar eventos y procesar eventos.

También fue necesario decidir que el evento debía guardarse antes de evaluar las reglas. Esta decisión permite mantener trazabilidad: si se genera una alerta, queda asociada al evento original.

---

## Limitaciones de la ingesta

La ingesta actual tiene varias limitaciones:

```text
- Los eventos son simulados.
- No se reciben logs reales del sistema.
- No hay agentes externos enviando eventos.
- No existe autenticación en el endpoint.
- No se aplica normalización avanzada.
- No hay cola de procesamiento.
- No existe procesamiento asíncrono.
```

Estas limitaciones son coherentes con el enfoque MVP.

---

## Posibles mejoras

En futuras versiones, la ingesta podría ampliarse con:

```text
- Recepción de logs reales de Linux.
- Integración con syslog.
- Agentes externos.
- Normalización de eventos.
- Autenticación del endpoint.
- Cola de mensajes.
- Procesamiento asíncrono.
- Validación más avanzada de fuentes.
```

Estas mejoras permitirían acercar el proyecto a un entorno de monitorización más realista.

---

## Conclusión

La API de ingesta es el punto de entrada principal del SIEM Lab MVP.

El endpoint `/ingest` permite recibir eventos simulados, almacenarlos, evaluarlos mediante reglas y generar alertas automáticamente.

Su implementación demuestra el flujo central del proyecto y conecta los elementos más importantes del sistema: API, base de datos, motor de reglas y alertas.