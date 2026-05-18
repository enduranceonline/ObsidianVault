## Introducción

Para entender el proyecto es necesario definir algunos conceptos básicos relacionados con los sistemas SIEM y la monitorización de eventos de seguridad.

Esta nota no pretende explicar en profundidad el funcionamiento de un SIEM profesional, sino aclarar los términos principales que se utilizan en el proyecto: evento, log, regla, alerta, severidad, metadatos, correlación y estado de una alerta.

---

## SIEM

Un **SIEM** es una solución orientada a recopilar, almacenar, analizar y consultar eventos de seguridad procedentes de diferentes sistemas.

Sus siglas significan:

```text
Security Information and Event Management
````

De forma simplificada, un SIEM permite centralizar eventos y aplicar lógica de detección para identificar comportamientos sospechosos.

En este proyecto se reproduce una versión reducida de ese flujo:

```text
evento → regla → alerta → consulta
```

---

## Evento

Un **evento** representa algo que ha ocurrido en un sistema.

Puede ser, por ejemplo:

```text
- Un inicio de sesión.
- Un error de autenticación.
- Una conexión de red.
- Un cambio de configuración.
- Un fallo de una aplicación.
- Una acción realizada por un usuario.
```

En el proyecto, los eventos son simulados y se envían mediante el endpoint `/ingest`.

Un evento contiene información como:

```text
- source
- severity
- message
- meta
```

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

---

## Log

Un **log** es un registro generado por un sistema, servicio o aplicación. Normalmente contiene información sobre una acción, error o cambio de estado.

En este proyecto, los conceptos de evento y log se utilizan de forma cercana, ya que los eventos simulados representan entradas de log simplificadas.

La diferencia principal es que el log suele ser el registro original generado por un sistema, mientras que el evento es la representación estructurada que el proyecto procesa.

---

## Fuente del evento

La **fuente** indica de dónde procede el evento.

En el proyecto se representa mediante el campo:

```text
source
```

Ejemplos de fuentes posibles:

```text
ssh
firewall
web
system
auth
```

Este campo permite crear reglas que solo se apliquen a eventos procedentes de una fuente concreta.

Ejemplo:

```text
source = ssh
```

---

## Severidad

La **severidad** indica la importancia o gravedad de un evento.

En el proyecto se representa mediante un valor numérico:

```text
severity
```

Una severidad más alta indica que el evento puede ser más relevante desde el punto de vista de seguridad.

Ejemplo:

```json
{
  "severity": 7
}
```

Las reglas pueden usar una severidad mínima para decidir si un evento debe generar una alerta.

Ejemplo:

```text
severity_min = 5
```

Esto significa que solo los eventos con severidad igual o superior a 5 serán considerados por esa regla.

---

## Mensaje

El **mensaje** contiene la descripción principal del evento.

En el proyecto se representa mediante el campo:

```text
message
```

Ejemplo:

```text
failed password for invalid user demo
```

Las reglas pueden buscar texto dentro del mensaje mediante la condición `contains`.

Ejemplo:

```text
contains = failed
```

Si el mensaje del evento contiene esa palabra, la condición se considera cumplida.

---

## Metadatos

Los **metadatos** contienen información adicional del evento.

En el proyecto se representan mediante el campo:

```text
meta
```

Ejemplo:

```json
{
  "meta": {
    "host": "demo-host",
    "ip": "192.168.1.50"
  }
}
```

Los metadatos permiten añadir contexto sin modificar la estructura principal del evento.

En este proyecto, el metadato más importante es:

```text
meta.host
```

A partir de este valor se calcula el `group_key`, utilizado para agrupar eventos relacionados.

---

## Regla

Una **regla** define las condiciones que debe cumplir un evento para generar una alerta.

En el proyecto, una regla puede incluir condiciones como:

```text
- source
- severity_min
- contains
- meta_match
- threshold_count
- threshold_seconds
- throttle_seconds
```

Ejemplo simplificado:

```text
source = ssh
severity_min = 5
contains = failed
```

Esta regla generaría una alerta si llega un evento de tipo `ssh`, con severidad mínima 5 y cuyo mensaje contenga la palabra `failed`.

---

## Alerta

Una **alerta** es el resultado de aplicar una regla sobre un evento.

No todos los eventos generan alertas. Solo se genera una alerta cuando un evento cumple las condiciones de una regla activa.

En el proyecto, cada alerta queda asociada a:

```text
- Un evento.
- Una regla.
- Un estado.
- Un título.
- Un group_key, si existe.
```

Esta relación permite saber qué ocurrió, qué regla se activó y qué alerta se generó.

---

## Estado de una alerta

Las alertas pueden tener diferentes estados según su situación dentro del ciclo de revisión.

En el proyecto se utilizan tres estados:

```text
open
ack
closed
```

Significado:

```text
open   → alerta abierta y pendiente de revisión
ack    → alerta reconocida o aceptada
closed → alerta cerrada
```

Esta funcionalidad permite simular una gestión básica de alertas.

---

## Correlación básica

La **correlación** consiste en analizar eventos para encontrar relaciones entre ellos.

En un SIEM real, la correlación puede ser compleja y tener en cuenta múltiples fuentes, ventanas temporales, usuarios, direcciones IP o patrones de comportamiento.

En este proyecto se implementa una correlación básica mediante:

```text
- Reglas activas.
- Severidad mínima.
- Coincidencia de texto.
- Metadatos.
- group_key.
- Threshold.
- Throttle.
```

El objetivo no es implementar una correlación avanzada, sino representar una versión sencilla y comprensible.

---

## Group key

El `group_key` permite agrupar eventos relacionados.

En este proyecto se obtiene a partir de:

```text
meta.host
```

Esto permite identificar eventos asociados a una misma máquina o fuente.

Ejemplo:

```json
{
  "meta": {
    "host": "server-01"
  }
}
```

En este caso, el `group_key` sería:

```text
server-01
```

El `group_key` es importante para aplicar controles como duplicados, throttle o thresholds.

---

## Threshold

El **threshold** permite generar alertas cuando se alcanza un número determinado de eventos dentro de una ventana temporal.

Ejemplo conceptual:

```text
3 eventos fallidos en 60 segundos
```

Este tipo de lógica permite detectar patrones repetidos, como varios intentos fallidos de autenticación.

En el proyecto, los thresholds requieren `group_key` para evitar agrupaciones ambiguas.

---

## Throttle

El **throttle** sirve para limitar la generación repetida de alertas durante un periodo de tiempo.

Su objetivo es reducir ruido y evitar que el sistema genere muchas alertas iguales en poco tiempo.

Ejemplo conceptual:

```text
No generar otra alerta igual para el mismo host durante 60 segundos.
```

En el proyecto, el throttle depende del `group_key`.

---

## Falso positivo

Un **falso positivo** ocurre cuando el sistema genera una alerta, pero esa alerta no representa un incidente real.

Por ejemplo, un usuario puede fallar varias veces su contraseña sin que exista un ataque.

Aunque el proyecto no implementa una gestión avanzada de falsos positivos, el concepto es importante porque explica por qué las alertas necesitan revisión humana.

---

## Diferencia entre evento, regla y alerta

La diferencia puede resumirse así:

```text
Evento → dato recibido
Regla  → condición de detección
Alerta → resultado generado
```

Ejemplo:

```text
Evento:
Intento fallido de acceso SSH.

Regla:
Detectar eventos SSH con severidad mínima 5 y mensaje que contenga "failed".

Alerta:
Se ha detectado un posible intento fallido relevante.
```

Esta separación es una de las bases del proyecto.

---

## Aplicación de estos conceptos en el proyecto

Los conceptos anteriores se reflejan directamente en el SIEM Lab MVP:

```text
Evento      → tabla events
Regla       → tabla rules
Alerta      → tabla alerts
Fuente      → campo source
Severidad   → campo severity
Mensaje     → campo message
Metadatos   → campo meta
Agrupación  → group_key
Estado      → open / ack / closed
```

Esta correspondencia permite que el proyecto sea sencillo de entender y defender.

---

## Conclusión

El proyecto utiliza una versión simplificada de los conceptos habituales en un sistema SIEM.

La clave está en diferenciar entre los datos que entran al sistema, las reglas que los evalúan y las alertas que se generan como resultado. Esta separación permite construir un flujo claro, mantener el modelo de datos ordenado y representar de forma práctica el funcionamiento básico de una herramienta de monitorización defensiva.