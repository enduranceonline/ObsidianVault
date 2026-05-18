## Introducción

Las pruebas de ingesta se realizaron para comprobar que el sistema era capaz de recibir eventos simulados mediante el endpoint `/ingest`, validar su estructura y almacenarlos correctamente.

La ingesta representa la entrada principal de información al SIEM Lab MVP. Por este motivo, era necesario validar que el sistema aceptaba eventos con la estructura esperada y generaba un registro persistente en la base de datos.

El flujo validado en esta sección es:

```text
evento simulado → POST /ingest → validación → almacenamiento
````

La generación de alertas se valida en una prueba independiente, ya que corresponde al comportamiento del motor de reglas.

---

## Objetivo de las pruebas

El objetivo principal fue comprobar que el endpoint `/ingest` funcionaba correctamente como punto de entrada del sistema.

Las pruebas debían validar que:

```text
- La API aceptaba peticiones POST en /ingest.
- El evento enviado tenía la estructura esperada.
- El evento se almacenaba correctamente.
- La respuesta incluía el evento creado.
- Los campos principales se conservaban.
- El campo meta.host se recibía correctamente.
- El evento quedaba disponible para ser evaluado por el motor de reglas.
```

---

## Endpoint probado

```http
POST /ingest
```

Este endpoint recibe eventos en formato JSON y activa el flujo principal del sistema.

Aunque `/ingest` también ejecuta el motor de reglas, en esta prueba se valida específicamente la parte de recepción y almacenamiento del evento.

---

## Estructura del evento de prueba

El evento utilizado representa un intento fallido de autenticación SSH.

```json
{
  "source": "ssh",
  "severity": 7,
  "message": "failed password for invalid user demo",
  "meta": {
    "host": "demo-1779117909"
  }
}
```

Campos utilizados:

```text
source   → indica el origen del evento
severity → indica la severidad del evento
message  → contiene el mensaje principal
meta     → contiene metadatos adicionales
```

En este caso, `meta.host` se utilizó para generar un identificador de host dinámico y evitar interferencias con pruebas anteriores.

---

## Comando ejecutado

Para realizar la prueba se utilizó `curl` desde la terminal.

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

El uso de `HOST="demo-$(date +%s)"` permite generar un valor único para cada prueba.

---

## Resultado esperado

El sistema debía devolver el evento creado con sus campos principales y un identificador asignado por la base de datos.

Se esperaba comprobar:

```text
- Creación de un nuevo evento.
- Asignación de un id.
- Conservación del campo source.
- Conservación del campo severity.
- Conservación del campo message.
- Conservación del campo meta.host.
- Generación de campos temporales.
```

---

## Resultado obtenido

La API respondió correctamente y devolvió el evento creado.

```json
{
    "id": 19,
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

El resultado confirma que el evento fue aceptado y registrado por el sistema.

---

## Interpretación del resultado

La respuesta obtenida permite validar que:

```text
- El endpoint /ingest estaba disponible.
- La petición POST fue procesada correctamente.
- El evento se creó con id 18.
- El origen del evento se guardó como ssh.
- La severidad se guardó con valor 7.
- El mensaje se almacenó correctamente.
- El metadato host se recibió como demo-1779117909.
- Se generaron los campos ts y created_at.
```

Esta prueba valida la primera parte del flujo principal: la entrada del evento en el sistema.

---

## Evidencia 1. Ingesta del evento

![[Pasted image 20260518175210.png]]

> Captura: terminal mostrando el comando `POST /ingest` y la respuesta JSON con el evento creado.

La captura debe mostrar especialmente:

```text
- Comando curl ejecutado.
- Endpoint /ingest.
- id del evento creado.
- source = ssh.
- severity = 7.
- message = failed password for invalid user demo.
- meta.host con valor dinámico.
```

---

## Comprobación posterior recomendada

Después de validar la respuesta de `/ingest`, conviene comprobar que el evento queda reflejado en las métricas generales del sistema.

Comando:

```bash
curl -s "http://127.0.0.1:8000/metrics" | python3 -m json.tool
```

Esta comprobación permite confirmar que el contador de eventos ha aumentado.

---

## Evidencia 2. Métricas después de la ingesta

![[Pasted image 20260518175301.png]]

> Captura: salida de `/metrics` después de enviar el evento.

La captura debe mostrar el valor actualizado de:

```text
events_total
alerts_total
rules_total
rules_enabled
```

En la validación realizada, el evento de prueba incrementó el contador de eventos.

---

## Relación con el motor de reglas

Aunque la respuesta de `/ingest` muestra únicamente el evento creado, este endpoint también activa la evaluación mediante reglas.

Por tanto, después de comprobar la ingesta, se debe consultar `/alerts/ui` o `/metrics` para verificar si el evento ha generado una alerta.

Comando recomendado:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

Esta comprobación pertenece a la prueba de generación de alertas.

---

## Diferencia entre ingesta y alerta

Es importante separar ambas validaciones:

```text
Ingesta:
comprueba que el evento entra y se almacena.

Generación de alerta:
comprueba que el evento activa una regla y crea una alerta.
```

La salida obtenida en esta prueba demuestra la ingesta. Para demostrar la alerta, se necesita la consulta posterior de alertas.

---

## Problemas o consideraciones detectadas

Durante las pruebas fue importante utilizar un valor dinámico en `meta.host`.

Motivo:

```text
- Evitar duplicados.
- Evitar interferencias con throttle.
- Evitar coincidencias con pruebas anteriores.
- Generar un group_key nuevo para cada prueba.
```

El uso de un host dinámico permitió realizar pruebas más limpias y controlar mejor el resultado.

---

## Resultado de la prueba

| Elemento comprobado             | Resultado |
| ------------------------------- | --------- |
| Endpoint `/ingest` disponible   | Validado  |
| Evento aceptado por la API      | Validado  |
| Creación de ID del evento       | Validado  |
| Conservación de `source`        | Validado  |
| Conservación de `severity`      | Validado  |
| Conservación de `message`       | Validado  |
| Conservación de `meta.host`     | Validado  |
| Generación de campos temporales | Validado  |

---

## Conclusión

La prueba confirmó que el endpoint `/ingest` funciona correctamente como punto de entrada de eventos.

El sistema fue capaz de recibir un evento simulado de tipo SSH, procesarlo y devolver el registro creado con sus datos principales.

Esta validación confirma que la primera parte del flujo del SIEM Lab MVP funciona correctamente:

```text
evento simulado → API de ingesta → evento almacenado
```

