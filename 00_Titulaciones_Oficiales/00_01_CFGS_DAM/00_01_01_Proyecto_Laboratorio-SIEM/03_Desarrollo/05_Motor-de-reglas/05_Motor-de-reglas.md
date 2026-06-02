## Introducción

El motor de reglas es el componente encargado de evaluar los eventos recibidos y decidir si deben generar una alerta.

Dentro del SIEM Lab MVP, esta parte representa la lógica principal de detección. El sistema no se limita a almacenar eventos, sino que los compara con reglas activas para identificar aquellos que cumplen determinadas condiciones.

El motor se ejecuta durante el flujo de ingesta:

```text
POST /ingest → guardar evento → evaluar reglas → generar alerta
````

---

## Función del motor de reglas

La función del motor de reglas es transformar eventos en alertas cuando se cumplen unas condiciones definidas.

El flujo básico es:

```text
evento recibido
      ↓
consulta de reglas activas
      ↓
evaluación de condiciones
      ↓
generación de alerta si hay coincidencia
```

Este comportamiento permite representar de forma simplificada cómo una herramienta SIEM puede detectar eventos relevantes entre todos los logs recibidos.

---

## Reglas activas

No todas las reglas almacenadas en la base de datos se aplican necesariamente. El motor solo evalúa las reglas que están habilitadas.

Campo utilizado:

```text
enabled = true
```

Esto permite mantener reglas creadas pero desactivadas, sin que afecten a la generación de alertas.

---

## Estructura básica de una regla

Una regla puede contener diferentes condiciones de detección.

Campos principales:

```text
name               → nombre de la regla
enabled            → indica si la regla está activa
source             → fuente del evento
severity_min       → severidad mínima requerida
contains           → texto que debe aparecer en el mensaje
meta_match         → coincidencia en metadatos
throttle_seconds   → control de alertas repetidas
threshold_count    → número de eventos requeridos
threshold_seconds  → ventana temporal del threshold
```

Ejemplo conceptual:

```text
name = test_rule_ssh
enabled = true
source = ssh
severity_min = 5
contains = failed
```

Esta regla detecta eventos procedentes de `ssh`, con severidad igual o superior a 5 y cuyo mensaje contiene la palabra `failed`.

---

## Condición source

La condición `source` permite aplicar una regla solo a eventos procedentes de una fuente concreta.

Ejemplo:

```text
source = ssh
```

Evento coincidente:

```json
{
  "source": "ssh",
  "severity": 7,
  "message": "failed password for invalid user demo"
}
```

Si el evento procede de otra fuente, la regla no genera alerta.

---

## Condición severity_min

La condición `severity_min` permite filtrar eventos según su nivel de severidad.

Ejemplo:

```text
severity_min = 5
```

Esto significa que la regla solo se aplica a eventos con severidad igual o superior a 5.

Ejemplo:

```text
severity = 7 → coincide
severity = 3 → no coincide
```

Esta condición permite priorizar eventos más relevantes.

---

## Condición contains

La condición `contains` permite buscar una cadena de texto dentro del mensaje del evento.

Ejemplo:

```text
contains = failed
```

Evento coincidente:

```json
{
  "message": "failed password for invalid user demo"
}
```

Esta condición resulta útil para detectar patrones sencillos en mensajes de log.

---

## Condición meta_match

La condición `meta_match` permite comprobar valores dentro de los metadatos del evento.

Los metadatos se almacenan en el campo:

```text
meta
```

Ejemplo de evento:

```json
{
  "source": "ssh",
  "severity": 7,
  "message": "failed password",
  "meta": {
    "host": "server-01",
    "user": "demo"
  }
}
```

Esta condición permite añadir más contexto a la detección sin modificar la estructura principal del evento.

---

## Uso de group_key

El `group_key` permite agrupar eventos relacionados.

En esta versión del proyecto se calcula a partir de:

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

El `group_key` permite aplicar lógica relacionada con duplicados, throttle y thresholds sobre eventos de una misma fuente o máquina.

---

## Control de duplicados

El control de duplicados evita generar alertas repetidas de forma innecesaria para el mismo grupo de eventos.

Esta lógica depende del `group_key`, ya que es necesario identificar si varios eventos pertenecen al mismo origen.

Ejemplo conceptual:

```text
Mismo host
Misma regla
Ventana temporal cercana
        ↓
Evitar alerta duplicada
```

Esto ayuda a reducir ruido en el sistema.

---

## Throttle

El `throttle` limita la generación repetida de alertas durante un periodo de tiempo.

Campo utilizado:

```text
throttle_seconds
```

Ejemplo:

```text
throttle_seconds = 60
```

Esto significa que, para una misma regla y un mismo `group_key`, el sistema evita generar alertas repetidas durante 60 segundos.

El objetivo es impedir que un mismo patrón produzca muchas alertas iguales en poco tiempo.

---

## Threshold

El `threshold` permite generar alertas cuando se alcanza un número determinado de eventos dentro de una ventana temporal.

Campos utilizados:

```text
threshold_count
threshold_seconds
```

Ejemplo conceptual:

```text
threshold_count = 3
threshold_seconds = 60
```

Esto representa una condición como:

```text
3 eventos relacionados en 60 segundos
```

Este tipo de lógica permite detectar comportamientos repetidos, como varios intentos fallidos de autenticación.

---

## Decisión sobre group_key, throttle y threshold

Durante el desarrollo fue necesario definir claramente cómo debía comportarse el motor en relación con `group_key`, `throttle` y `threshold`.

La decisión final fue:

```text
- El group_key se obtiene a partir de meta.host.
- Las alertas simples pueden generarse aunque no exista group_key.
- El throttle y el control de duplicados dependen del group_key.
- Los thresholds requieren group_key para funcionar correctamente.
```

Esta decisión redujo ambigüedades y permitió mantener un comportamiento más fácil de validar.

---

## Flujo interno del motor

Cuando llega un evento mediante `/ingest`, el motor sigue este proceso:

```text
1. Recibir evento ya validado.
2. Guardar evento en la tabla events.
3. Obtener group_key desde meta.host.
4. Consultar reglas activas.
5. Evaluar cada condición de la regla.
6. Comprobar throttle, duplicados o threshold si corresponde.
7. Generar alerta si se cumplen las condiciones.
8. Guardar alerta en la tabla alerts.
```

Este flujo conecta la ingesta, el modelo de datos y la generación de alertas.

---

## Ejemplo de detección simple

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

Evaluación:

```text
source coincide
severity 7 >= 5
message contiene "failed"
```

Resultado:

```text
Se genera una alerta.
```

---

## Alerta generada

Cuando el evento coincide con la regla, el sistema crea una alerta.

Información principal:

```text
rule_id   → regla activada
event_id  → evento que originó la alerta
title     → título descriptivo
status    → open
group_key → valor obtenido de meta.host
```

El estado inicial de la alerta es:

```text
open
```

Posteriormente puede modificarse a:

```text
ack
closed
```

---

## Problemas durante el desarrollo

El motor de reglas fue una de las partes que requirió más decisiones de diseño.

Los principales problemas fueron:

```text
- Definir qué condiciones debía soportar una regla.
- Evitar que el motor creciera demasiado.
- Decidir cómo calcular el group_key.
- Definir qué ocurre si un evento no tiene meta.host.
- Controlar duplicados sin complicar demasiado el sistema.
- Aplicar throttle y threshold de forma previsible.
```

La solución fue mantener una lógica básica, documentar claramente sus límites y priorizar que el comportamiento fuera comprensible.

---

## Validación del motor de reglas

El motor se validó enviando eventos de prueba mediante `/ingest`.

Prueba principal:

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

Después se consultaron las alertas:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

El resultado confirmó que el evento generaba una alerta correctamente.

---

## Resultado validado

Durante la prueba final se comprobó que el sistema incrementaba correctamente el número de eventos y alertas.

Antes de la prueba:

```text
events_total: 16
rules_total: 7
rules_enabled: 2
alerts_total: 4
```

Después de enviar el evento:

```text
events_total: 17
rules_total: 7
rules_enabled: 2
alerts_total: 5
```

Esto confirmó que el motor procesó el evento y generó una nueva alerta.

---

## Limitaciones del motor de reglas

El motor actual tiene limitaciones propias de un MVP:

```text
- No implementa correlación avanzada.
- No analiza múltiples fuentes reales.
- No incluye lenguaje de reglas complejo.
- No permite expresiones lógicas avanzadas.
- No incluye prioridades dinámicas.
- No calcula riesgo acumulado.
- No integra inteligencia de amenazas.
```

Estas limitaciones son coherentes con el objetivo del proyecto: representar una lógica básica de detección.

---

## Posibles mejoras

En futuras versiones, el motor podría ampliarse con:

```text
- Reglas más expresivas.
- Condiciones AND/OR más avanzadas.
- Integración con logs reales.
- Normalización de eventos.
- Correlación entre múltiples fuentes.
- Priorización automática.
- Sistema de supresión de falsos positivos.
- Clasificación de alertas por tipo.
```

Estas mejoras permitirían acercar el motor a una herramienta de detección más realista.

---

## Conclusión

El motor de reglas es el componente que convierte el proyecto en algo más que una API de almacenamiento.

Gracias a este motor, el sistema puede recibir eventos, evaluarlos y generar alertas de forma automática.

Aunque su lógica es sencilla, permite representar el funcionamiento básico de una herramienta de monitorización defensiva y cumple con el objetivo principal del SIEM Lab MVP.