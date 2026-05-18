## Introducción

En cualquier sistema informático se generan continuamente eventos: accesos de usuarios, errores de autenticación, conexiones de red, cambios de configuración, actividad de servicios, operaciones sobre archivos o mensajes procedentes de aplicaciones.

De forma aislada, muchos de estos eventos pueden parecer poco relevantes. Sin embargo, cuando se analizan en conjunto, pueden ayudar a detectar comportamientos anómalos o posibles incidentes de seguridad.

El problema principal que intenta representar este proyecto es precisamente ese: cómo pasar de tener eventos individuales a generar información útil para la detección y revisión de posibles alertas.

---

## El problema de los eventos dispersos

En una infraestructura real, los eventos pueden proceder de muchas fuentes diferentes:

```text
- Servidores
- Estaciones de trabajo
- Aplicaciones
- Firewalls
- Sistemas de autenticación
- Bases de datos
- Servicios web
- Dispositivos de red
````

Cada fuente puede generar sus propios logs con formatos, niveles de detalle y estructuras diferentes. Esto provoca que la información de seguridad esté dispersa y sea difícil de revisar manualmente.

Un evento concreto puede no ser importante por sí solo, pero varios eventos relacionados pueden indicar un comportamiento sospechoso. Por ejemplo, múltiples intentos fallidos de inicio de sesión desde una misma máquina pueden ser más relevantes que un único fallo aislado.

---

## De almacenar logs a detectar información relevante

Guardar eventos no es suficiente. Una base de datos llena de logs puede contener mucha información, pero si no existe una lógica que permita analizarla, filtrar lo importante y generar señales de alerta, su utilidad es limitada.

El valor de un sistema de monitorización no está únicamente en almacenar datos, sino en transformarlos en información accionable.

En este proyecto, esa transformación se representa mediante reglas de detección. Cada regla define una serie de condiciones que permiten decidir si un evento debe generar una alerta.

Ejemplo simplificado:

```text
Evento recibido:
source = ssh
severity = 7
message = failed password for invalid user demo

Regla activa:
source = ssh
severity_min = 5
contains = failed

Resultado:
se genera una alerta
```

Este ejemplo muestra cómo un evento almacenado pasa a convertirse en una alerta cuando cumple unas condiciones definidas.

---

## Necesidad de centralización

Otro problema habitual en seguridad es la falta de centralización. Si cada sistema mantiene sus propios logs de forma independiente, revisar lo que ocurre en la infraestructura se vuelve lento y poco eficiente.

Centralizar los eventos permite:

```text
- Consultar información desde un único punto.
- Aplicar reglas comunes.
- Detectar patrones repetidos.
- Facilitar la revisión de alertas.
- Mantener un histórico de actividad.
```

El proyecto reproduce esta idea de forma simplificada: todos los eventos simulados entran por una API común y se almacenan en una base de datos PostgreSQL.

---

## Necesidad de reglas de detección

Una vez centralizados los eventos, el siguiente problema es decidir cuáles son relevantes.

Para ello se utilizan reglas. Una regla permite expresar una condición de detección, por ejemplo:

```text
- Eventos de una fuente concreta.
- Eventos con severidad mínima.
- Mensajes que contienen una palabra determinada.
- Eventos asociados a ciertos metadatos.
- Repetición de eventos en una ventana temporal.
```

En el proyecto, las reglas permiten evaluar eventos recibidos mediante `/ingest` y generar alertas cuando se cumplen las condiciones definidas.

Este enfoque permite representar una idea básica de los sistemas SIEM: no todos los logs son alertas, pero algunos logs pueden convertirse en alertas si coinciden con una lógica de detección.

---

## Problema de volumen y priorización

En entornos reales, uno de los mayores retos no es solo recibir eventos, sino priorizarlos.

Un sistema puede generar miles o millones de eventos. Revisarlos manualmente sería inviable. Por eso, las herramientas de monitorización necesitan mecanismos para reducir ruido y destacar lo importante.

Aunque este proyecto trabaja con eventos simulados y un volumen reducido, incorpora algunos conceptos relacionados con esta problemática:

```text
- Severidad del evento.
- Estados de alerta.
- Filtros de consulta.
- Agrupación mediante group_key.
- Control básico de duplicados.
- Throttle.
- Threshold.
```

Estas funciones no convierten el proyecto en un SIEM completo, pero permiten representar problemas reales de monitorización de una forma asumible.

---

## Diferencia entre evento y alerta

Una distinción importante del proyecto es la diferencia entre evento y alerta.

Un **evento** es un dato recibido por el sistema. Representa algo que ha ocurrido.

Una **alerta** es el resultado de aplicar una lógica de detección sobre uno o varios eventos. Representa algo que merece ser revisado.

Esta diferencia es clave porque evita tratar todos los logs como si fueran incidentes. El sistema no genera alertas por cada evento de forma indiscriminada, sino únicamente cuando se cumplen las condiciones de una regla activa.

---

## Problema representado por el proyecto

El proyecto representa una versión simplificada del siguiente problema:

```text
¿Cómo se puede recibir información de seguridad, almacenarla, evaluarla mediante reglas y generar alertas consultables?
```

Para resolverlo, se ha construido un sistema con los siguientes elementos:

```text
- Una API de ingesta.
- Una base de datos.
- Un modelo de eventos.
- Un modelo de reglas.
- Un modelo de alertas.
- Un motor básico de evaluación.
- Endpoints de consulta.
- Un frontend de visualización.
```

Cada componente responde a una parte del problema:

```text
API          → entrada de eventos
PostgreSQL   → almacenamiento
Reglas       → lógica de detección
Alertas      → resultado de la detección
Frontend     → consulta visual
```

---

## Relación con el proyecto desarrollado

El SIEM Lab MVP no intenta cubrir todos los problemas de una infraestructura real. Su objetivo es reproducir el núcleo del proceso de monitorización defensiva en un entorno controlado.

Por este motivo, se utilizan eventos simulados en lugar de logs reales. Esta decisión reduce la complejidad y permite centrarse en el flujo principal del sistema.

El resultado es un laboratorio que permite entender cómo se conectan los conceptos principales:

```text
evento → regla → alerta → revisión
```

---

## Conclusión

El problema de partida del proyecto es la necesidad de convertir eventos dispersos en información útil para la detección de posibles incidentes.

El sistema desarrollado aborda este problema de forma simplificada mediante una API de ingesta, almacenamiento en base de datos, reglas de detección y generación automática de alertas.

Esta aproximación permite comprender la lógica básica de un SIEM sin asumir la complejidad de una herramienta profesional completa.