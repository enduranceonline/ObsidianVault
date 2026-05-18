## Introducción

Las pruebas del motor de reglas se realizaron para comprobar que el sistema era capaz de evaluar eventos recibidos mediante `/ingest` y generar alertas cuando un evento coincidía con una regla activa.

Esta prueba valida la segunda parte del flujo principal del SIEM Lab MVP:

```text
evento almacenado → evaluación mediante reglas → generación de alerta → consulta
````

La ingesta del evento valida que el evento entra en el sistema. Esta prueba valida que, una vez recibido, el evento es evaluado correctamente y se transforma en una alerta.

---

## Objetivo de la prueba

El objetivo de esta prueba fue comprobar que el motor de reglas:

```text
- Consulta reglas activas.
- Evalúa las condiciones definidas en la regla.
- Compara dichas condiciones con el evento recibido.
- Genera una alerta si existe coincidencia.
- Asocia la alerta al evento correspondiente.
- Asocia la alerta a la regla activada.
- Guarda la alerta en PostgreSQL.
- Permite consultar la alerta desde /alerts/ui.
```

---

## Regla utilizada

La prueba se realizó con la regla activa:

```text
test_rule_ssh
```

Esta regla está orientada a detectar eventos SSH relacionados con fallos de autenticación.

Condiciones principales de la regla:

```text
source = ssh
severity_min = 5
contains = failed
```

Por tanto, la regla debe generar una alerta cuando recibe un evento que cumple estas condiciones:

```text
- Procede de ssh.
- Tiene una severidad igual o superior a 5.
- Contiene la palabra failed en el mensaje.
```

---

## Evento evaluado

El evento evaluado por el motor de reglas fue generado previamente mediante `/ingest`.

Datos relevantes del evento:

```text
event_id: 19
source: ssh
severity: 7
message: failed password for invalid user demo
meta.host: demo-1779119427
```

Este evento cumple las condiciones necesarias para activar la regla `test_rule_ssh`.

Comparación entre evento y regla:

```text
source = ssh                    → coincide
severity = 7                    → cumple severity_min = 5
message contiene "failed"       → coincide
meta.host = demo-1779119427     → permite generar group_key
```

---

## Comando utilizado

Para comprobar si el evento había generado una alerta, se consultó el endpoint enriquecido de alertas:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

Este endpoint devuelve las alertas junto con información del evento asociado, lo que permite comprobar si la alerta se ha generado correctamente y a qué evento pertenece.

---

## Resultado esperado

El sistema debía mostrar una alerta asociada al evento `19`, generada por la regla `test_rule_ssh`.

La alerta esperada debía incluir:

```text
- ID de alerta.
- ID de regla.
- ID de evento asociado.
- Nombre de la regla activada.
- Estado de la alerta.
- group_key.
- Source del evento.
- Severidad del evento.
- Mensaje del evento.
```

---

## Resultado obtenido

La consulta a `/alerts/ui` mostró correctamente una alerta generada por el motor de reglas.

La alerta más reciente corresponde al evento `19` y fue generada por la regla `test_rule_ssh`.

Salida relevante obtenida:

```json
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
```

Este resultado confirma que el motor de reglas evaluó correctamente el evento `19` y generó la alerta `8`.

---

## Asociación entre evento, regla y alerta

La alerta generada quedó asociada correctamente al evento recibido y a la regla activada.

Relación principal validada:

```text
Evento 19 → Regla test_rule_ssh → Alerta 8
```

Datos principales:

```text
alert_id: 8
rule_id: 7
event_id: 19
rule_name: test_rule_ssh
group_key: demo-1779119427
status: open
```

Esta relación demuestra que el sistema mantiene trazabilidad entre el evento recibido, la regla que se activa y la alerta generada.

---

## Interpretación del resultado

El comportamiento obtenido es correcto porque el evento cumple todas las condiciones de la regla activa.

Regla:

```text
source = ssh
severity_min = 5
contains = failed
```

Evento:

```text
source = ssh
severity = 7
message = failed password for invalid user demo
```

Evaluación:

```text
source = ssh                  → coincide
severity = 7 >= 5             → cumple la severidad mínima
message contiene "failed"     → coincide
```

Por tanto, el resultado esperado era la generación de una alerta. La aparición de la alerta `8` en `/alerts/ui` confirma que el motor de reglas funcionó correctamente.

---

## Comprobación del group_key

El evento enviado incluía el siguiente metadato:

```json
{
  "meta": {
    "host": "demo-1779119427"
  }
}
```

A partir de este valor, el sistema generó el siguiente `group_key`:

```text
demo-1779119427
```

Este valor aparece correctamente en la alerta generada:

```text
group_key: demo-1779119427
```

El `group_key` es importante porque permite agrupar eventos relacionados y aplicar lógica como control de duplicados, throttle o threshold.

---

## Evidencia 1. Consulta de alertas

![[Pasted image 20260518180618.png]]

> Captura: salida de `/alerts/ui?limit=5` mostrando la alerta `id: 8` asociada al evento `id: 19`.

La captura muestra:

```text
id: 8
rule_id: 7
event_id: 19
title: Rule matched: test_rule_ssh
group_key: demo-1779119427
status: open
rule_name: test_rule_ssh
event_source: ssh
event_severity: 7
event_message: failed password for invalid user demo
```

En la misma salida también aparece una alerta anterior generada por la misma regla:

```text
id: 7
rule_id: 7
event_id: 18
title: Rule matched: test_rule_ssh
group_key: demo-1779117909
status: open
rule_name: test_rule_ssh
event_source: ssh
event_severity: 7
event_message: failed password for invalid user demo
```

Esto confirma que el comportamiento del motor de reglas se repite correctamente en distintas ejecuciones.

---

## Relación con una prueba anterior

La salida de `/alerts/ui` también muestra una validación anterior del mismo flujo:

```text
Evento 18 → Regla test_rule_ssh → Alerta 7
```

Datos de esa alerta:

```text
alert_id: 7
event_id: 18
group_key: demo-1779117909
status: open
```

Esto permite comprobar que el sistema generó alertas correctamente en más de una ejecución de la prueba.

---

## Diferencia entre ingesta y motor de reglas

Es importante separar la validación de ingesta de la validación del motor de reglas.

La respuesta de `/ingest` confirma que el evento se recibe y se almacena.

La consulta de `/alerts/ui` confirma que el evento ha sido evaluado por el motor de reglas y ha generado una alerta.

Resumen:

```text
/ingest    → valida recepción y almacenamiento del evento
/alerts/ui → valida generación y consulta de la alerta
/metrics   → permite comprobar incrementos de eventos y alertas
```

Esta separación evita confundir el identificador del evento con el identificador de la alerta.

---

## Uso de host dinámico

Durante las pruebas se utilizó un host dinámico:

```bash
HOST="demo-$(date +%s)"
```

Esta decisión permitió generar un valor diferente en cada ejecución.

Ventajas:

```text
- Evita interferencias con alertas anteriores.
- Reduce problemas con duplicados.
- Evita que el throttle bloquee nuevas alertas.
- Facilita identificar la alerta generada por una prueba concreta.
```

En esta prueba, el valor generado fue:

```text
demo-1779119427
```

---

## Resultado de la prueba

|Elemento comprobado|Resultado|
|---|---|
|Regla activa disponible|Validado|
|Evento compatible con la regla|Validado|
|Evaluación de `source`|Validado|
|Evaluación de `severity_min`|Validado|
|Evaluación de `contains`|Validado|
|Generación de alerta|Validado|
|Asociación alerta-evento|Validado|
|Asociación alerta-regla|Validado|
|Uso de `group_key`|Validado|
|Consulta desde `/alerts/ui`|Validado|
|Repetición del comportamiento con otro evento|Validado|

---

## Problemas o consideraciones detectadas

Durante la validación fue necesario aclarar la diferencia entre el identificador del evento y el identificador de la alerta.

La correspondencia correcta observada en la salida fue:

```text
Evento 19 → Alerta 8
Evento 18 → Alerta 7
Evento 17 → Alerta 6
```

También se comprobó que la alerta `6`, perteneciente a una prueba anterior, ya aparecía en estado `ack`, mientras que las alertas `7` y `8` estaban en estado `open`.

Esta diferencia es correcta, ya que cada alerta pertenece a una ejecución distinta de la prueba y puede encontrarse en un estado diferente.

---

## Conclusión

La prueba confirma que el motor de reglas funciona correctamente.

El evento `19`, recibido mediante `/ingest`, fue evaluado contra la regla activa `test_rule_ssh`. Al cumplir las condiciones de fuente, severidad y contenido del mensaje, el sistema generó la alerta `8`.

El flujo validado es:

```text
evento SSH → regla test_rule_ssh → alerta generada → consulta desde /alerts/ui
```

Además, la salida muestra una ejecución anterior en la que el evento `18` generó la alerta `7`, confirmando que el comportamiento del motor se mantiene en distintas pruebas.