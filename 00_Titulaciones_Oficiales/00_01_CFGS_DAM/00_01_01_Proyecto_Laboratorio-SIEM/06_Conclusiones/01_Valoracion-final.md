## Introducción

Durante el desarrollo del **SIEM Lab MVP** surgieron incidencias de distinto tipo. Algunas fueron problemas técnicos concretos relacionados con virtualización, Docker, PostgreSQL o pruebas. Otras fueron problemas de diseño, alcance o interpretación del comportamiento del sistema.

Estas incidencias fueron importantes porque obligaron a tomar decisiones y permitieron mejorar el proyecto. En lugar de entenderlas únicamente como errores, se han tratado como parte del proceso real de desarrollo.

El objetivo de esta nota es analizar los problemas que más influyeron en el proyecto, explicar cómo se resolvieron y recoger los aprendizajes obtenidos.

---

## Incidencias de alcance y enfoque

### Problema detectado

Uno de los primeros retos fue definir el alcance real del proyecto. La idea inicial estaba relacionada con los sistemas SIEM, pero un SIEM profesional es una herramienta muy amplia.

Un SIEM real puede incluir:

```text
- Recogida de logs desde múltiples fuentes.
- Agentes instalados en equipos externos.
- Normalización de eventos.
- Correlación avanzada.
- Gestión de usuarios.
- Roles y permisos.
- Dashboards en tiempo real.
- Notificaciones.
- Informes.
- Retención histórica.
- Integración con herramientas externas.
````

Intentar abarcar todas estas funcionalidades habría hecho que el proyecto creciera demasiado. El riesgo era desarrollar muchas partes de forma incompleta y no llegar a validar correctamente el flujo principal.

También existía otro riesgo: basar el proyecto en instalar herramientas existentes como Wazuh, ELK, Splunk o Graylog. Eso habría permitido montar un laboratorio realista, pero habría reducido el peso del desarrollo propio.

---

### Solución aplicada

Se decidió plantear el proyecto como un **MVP**, centrado en el flujo principal:

```text
evento → ingesta → almacenamiento → evaluación → alerta → consulta
```

También se decidió desarrollar una aplicación propia, en lugar de instalar un SIEM existente como núcleo del proyecto.

Componentes desarrollados:

```text
- API de ingesta.
- Modelo de datos propio.
- Motor básico de reglas.
- Gestión de alertas.
- Endpoints de consulta.
- Frontend básico.
```

Esta decisión permitió mantener el equilibrio entre ciberseguridad y desarrollo de aplicaciones.

---

### Aprendizaje

El aprendizaje principal fue que limitar el alcance no significa reducir el valor del proyecto.

En este caso, acotar el sistema permitió construir una versión más clara, funcional y validable. El proyecto no intenta ser un SIEM completo, sino representar correctamente una parte esencial de su funcionamiento.

También se entendió la diferencia entre montar un laboratorio de ciberseguridad y desarrollar una aplicación orientada a ciberseguridad. Para este proyecto, era más importante demostrar diseño, desarrollo, pruebas y documentación de una aplicación propia.

---

## Incidencias relacionadas con el entorno de virtualización

### Problema detectado

El entorno de trabajo fue una de las primeras dificultades importantes. Inicialmente se intentó trabajar con VMware, pero aparecieron problemas de estabilidad y compatibilidad que dificultaban avanzar con normalidad.

Después se migró el entorno a VirtualBox, pero también surgieron incidencias relacionadas con los módulos del sistema en Kali Linux.

Errores detectados:

```text
VERR_VM_DRIVER_NOT_INSTALLED
VERR_VM_DRIVER_VERSION_MISMATCH
```

Estos errores impedían arrancar correctamente la máquina virtual.

También apareció un problema de pantalla negra al iniciar la VM, que impedía acceder correctamente al entorno de trabajo.

---

### Explicación técnica

VirtualBox necesita módulos del kernel para ejecutar máquinas virtuales. En sistemas Linux, estos módulos suelen depender de paquetes como `virtualbox-dkms`.

DKMS permite recompilar módulos cuando cambia el kernel del sistema. Si la versión instalada de VirtualBox, los módulos cargados y el kernel no coinciden correctamente, pueden aparecer errores de carga.

Por tanto, aunque VirtualBox esté instalado, la máquina virtual puede no arrancar si los módulos necesarios no están disponibles o no son compatibles con el kernel actual.

El problema de pantalla negra estaba más relacionado con la configuración gráfica de la máquina virtual: controlador gráfico, aceleración, memoria de vídeo o compatibilidad entre la VM y el sistema anfitrión.

---

### Solución aplicada

Se revisó la instalación de VirtualBox y se sincronizaron los paquetes necesarios:

```text
virtualbox
virtualbox-qt
virtualbox-dkms
```

También se revisó la configuración gráfica de la máquina virtual hasta conseguir que arrancara correctamente.

Finalmente, la VM `siem-lab` quedó operativa y se utilizó como entorno principal de desarrollo.

---

### Aprendizaje

Este problema permitió entender que el entorno de desarrollo también forma parte del proyecto.

No todos los fallos proceden del código. En un entorno con virtualización, contenedores y base de datos, los errores pueden aparecer en distintas capas:

```text
- Sistema anfitrión.
- Virtualización.
- Máquina virtual.
- Docker.
- Base de datos.
- Backend.
- Frontend.
```

Saber ubicar el problema en la capa correcta fue clave para avanzar.

---

## Incidencias con Docker y PostgreSQL

### Problema detectado

Uno de los problemas técnicos más relevantes fue el fallo de autenticación entre la API y PostgreSQL.

Error observado:

```text
FATAL: password authentication failed for user "siem"
```

Aparentemente, la configuración de credenciales era correcta, pero la API no conseguía conectarse a la base de datos.

---

### Explicación técnica

El problema estaba relacionado con los volúmenes persistentes de Docker.

En Docker, un contenedor puede eliminarse y recrearse, pero los datos almacenados en un volumen pueden mantenerse. Esto es especialmente importante en bases de datos como PostgreSQL.

Cuando PostgreSQL se inicializa por primera vez, crea usuarios, contraseñas y bases de datos a partir de las variables de entorno. Sin embargo, si la base de datos ya fue inicializada previamente, cambiar las variables de entorno no modifica automáticamente las credenciales almacenadas en el volumen.

En este caso, el contenedor podía reconstruirse, pero el volumen seguía conservando una contraseña anterior para el usuario `siem`.

---

### Solución aplicada

La solución fue modificar la contraseña directamente dentro de PostgreSQL:

```bash
docker compose exec db psql -U siem -d siem -c "ALTER USER siem WITH PASSWORD 'change_me';"
docker compose restart api
```

Después de aplicar el cambio y reiniciar la API, el endpoint `/health` respondió correctamente:

```json
{
  "status": "ok",
  "db": "ok"
}
```

---

### Aprendizaje

El aprendizaje principal fue entender que:

```text
Recrear un contenedor no implica reiniciar los datos persistidos.
```

También quedó clara la diferencia entre:

```text
Contenedor → servicio en ejecución.
Imagen     → plantilla desde la que se crea el contenedor.
Volumen    → almacenamiento persistente que sobrevive al contenedor.
```

Los volúmenes son útiles porque conservan datos, pero también pueden conservar configuraciones antiguas que generen errores si no se tienen en cuenta.

---

## Incidencias de diseño de API

### Problema detectado

Durante el desarrollo fue necesario diferenciar correctamente entre crear eventos y procesar eventos.

Inicialmente podía parecer suficiente disponer de endpoints como:

```http
POST /events
GET /events
```

Sin embargo, estos endpoints solo permiten trabajar con eventos como registros de base de datos. No representan el comportamiento principal del SIEM Lab MVP.

El flujo importante del proyecto era:

```text
recibir evento → almacenarlo → evaluar reglas → generar alerta
```

Por tanto, hacía falta un endpoint que no solo guardara el evento, sino que activara el procesamiento.

---

### Solución aplicada

Se definió `/ingest` como endpoint principal del sistema:

```http
POST /ingest
```

La diferencia quedó establecida así:

```text
/events → permite crear o consultar eventos.
/ingest → recibe eventos y activa el motor de reglas.
```

Esto permitió que el proyecto tuviera un flujo más claro y más fácil de validar.

---

### Aprendizaje

El diseño de una API no consiste solo en crear rutas que guarden datos. Cada endpoint debe representar una intención clara dentro del sistema.

En este caso:

```text
/events → operación de datos.
/ingest → operación de negocio.
```

La diferencia es importante porque guardar un evento no equivale a procesarlo.

---

## Incidencias entre backend y frontend

### Problema detectado

Al desarrollar el frontend se detectó que el endpoint básico de alertas no era suficiente para mostrar la información necesaria.

Una alerta almacenada en la tabla `alerts` contiene datos como:

```text
id
rule_id
event_id
title
status
group_key
created_at
```

Sin embargo, para que el frontend pudiera mostrar una vista útil, también necesitaba información del evento asociado:

```text
event_source
event_severity
event_message
event_ts
```

El problema era cómo proporcionar esos datos sin duplicarlos innecesariamente dentro de la tabla `alerts`.

---

### Explicación técnica

Duplicar datos del evento dentro de la alerta habría simplificado la lectura desde el frontend, pero habría empeorado el modelo de datos.

Por ejemplo:

```text
events.source  → dato original
alerts.source  → copia duplicada
```

Esto puede provocar inconsistencias y ensuciar el diseño.

La alternativa correcta era mantener las relaciones:

```text
alerts.event_id → events.id
alerts.rule_id  → rules.id
```

Y crear endpoints que devolvieran una respuesta enriquecida combinando datos de varias tablas.

---

### Solución aplicada

Se crearon endpoints específicos para el frontend:

```http
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Estos endpoints devuelven alertas junto con información del evento asociado y de la regla activada.

Ejemplo de respuesta enriquecida:

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

---

### Aprendizaje

Este problema permitió diferenciar entre:

```text
Modelo de datos interno → cómo se almacena la información.
Respuesta de API        → cómo se entrega la información al consumidor.
```

No siempre conviene adaptar la base de datos al frontend. En este caso, fue mejor mantener un modelo limpio y crear endpoints específicos para visualización.

---

## Incidencias con el motor de reglas

### Problema detectado

El motor de reglas fue una de las partes más delicadas del proyecto, porque no bastaba con comprobar si un evento coincidía con una regla simple.

También había que decidir cómo se comportaban elementos como:

```text
- group_key
- threshold
- throttle
- control de duplicados
```

El riesgo era que el motor creciera demasiado o tuviera comportamientos ambiguos.

---

### Explicación técnica

El `group_key` sirve para agrupar eventos relacionados. En este proyecto se decidió obtenerlo a partir de:

```text
meta.host
```

Por ejemplo:

```json
{
  "meta": {
    "host": "demo-1779119427"
  }
}
```

Genera:

```text
group_key = demo-1779119427
```

Este valor permite saber que varios eventos pertenecen a una misma máquina o fuente lógica.

El problema aparece al aplicar funciones como `threshold` o `throttle`.

Un `threshold` necesita contar eventos relacionados dentro de una ventana temporal, por ejemplo:

```text
3 eventos en 60 segundos para el mismo host.
```

Pero si no existe `group_key`, el sistema no sabe con claridad qué eventos debe agrupar.

El `throttle` también necesita saber si una alerta es repetida para la misma fuente. Sin `group_key`, el sistema podría bloquear alertas de forma incorrecta o permitir duplicados sin control.

---

### Solución aplicada

Se definió el comportamiento del motor así:

```text
- El group_key se obtiene a partir de meta.host.
- Las alertas simples pueden generarse aunque no exista group_key.
- El throttle y el control de duplicados dependen del group_key.
- Los thresholds requieren group_key para funcionar correctamente.
```

Esta decisión permitió mantener el motor de reglas simple, pero con un comportamiento claro.

---

### Aprendizaje

El aprendizaje principal fue que añadir lógica de detección no consiste solo en añadir campos a una regla. Cada campo modifica el comportamiento del sistema y puede generar casos límite.

En un MVP es preferible tener reglas más simples pero bien definidas que intentar construir una correlación avanzada difícil de validar.

El criterio fue priorizar un motor:

```text
comprensible → documentado → validable
```

---

## Incidencias durante la validación

### Problema detectado

Durante las pruebas apareció una confusión entre el identificador del evento y el identificador de la alerta.

En la respuesta de `/ingest`, el sistema devuelve el evento creado:

```json
{
    "id": 18,
    "source": "ssh",
    "severity": 7,
    "message": "failed password for invalid user demo"
}
```

Ese `id` corresponde al evento, no a la alerta.

Después, el motor de reglas puede generar una alerta diferente, con otro identificador:

```text
Evento 18 → Alerta 7
Evento 19 → Alerta 8
```

---

### Explicación técnica

En el modelo de datos existen entidades distintas:

```text
events.id  → identificador del evento
alerts.id  → identificador de la alerta
```

Aunque estén relacionadas, no tienen por qué compartir el mismo número.

La relación se establece mediante:

```text
alerts.event_id → events.id
```

Por eso, una alerta con `id = 8` puede estar asociada al evento con `id = 19`.

Ejemplo validado:

```json
{
    "id": 8,
    "rule_id": 7,
    "event_id": 19,
    "title": "Rule matched: test_rule_ssh",
    "group_key": "demo-1779119427",
    "status": "open"
}
```

---

### Solución aplicada

Se separaron las pruebas en dos partes:

```text
Pruebas de ingesta:
validan que el evento se recibe y se almacena.

Pruebas del motor de reglas:
validan que el evento genera una alerta.
```

También se ajustó la documentación para que cada prueba tuviera su propia evidencia:

```text
/ingest    → evidencia del evento creado.
/alerts/ui → evidencia de la alerta generada.
/metrics   → evidencia de contadores.
```

---

### Aprendizaje

El aprendizaje fue que, en sistemas con varias entidades relacionadas, la validación debe hacerse siguiendo las relaciones reales del modelo.

No basta con ver que `/ingest` responde correctamente. Esa respuesta demuestra que el evento se ha creado, pero no demuestra por sí sola que se haya generado una alerta.

Para validar la alerta hay que consultar `/alerts/ui` o comprobar el incremento de `alerts_total`.

---

## Incidencias con las pruebas automatizadas

### Problema detectado

Durante la validación se intentó ejecutar Pytest desde el entorno local, pero apareció el error:

```text
No module named pytest
```

Esto indicaba que `pytest` no estaba instalado en el entorno Python local.

---

### Explicación técnica

El proyecto estaba preparado para ejecutarse mediante Docker. Por tanto, las dependencias principales estaban disponibles dentro del contenedor de la API, no necesariamente en el entorno local del sistema.

Esto es habitual en proyectos contenerizados. El entorno local puede no tener instaladas las mismas versiones o librerías que el contenedor.

Ejecutar las pruebas fuera del contenedor podía provocar errores que no tenían relación con el código, sino con el entorno desde el que se lanzaban.

---

### Solución aplicada

Se ejecutaron las pruebas dentro del contenedor `siem-api`:

```bash
docker compose exec api python -m pytest
```

Resultado obtenido:

```text
4 passed in 1.00s
```

---

### Aprendizaje

El aprendizaje fue que las pruebas deben ejecutarse en el entorno adecuado.

En este proyecto, el entorno adecuado era el contenedor de la API, porque contiene las dependencias reales del backend.

Esto refuerza una idea importante de Docker:

```text
El contenedor define el entorno de ejecución del proyecto.
```

---

## Incidencias del frontend

### Problema detectado

Durante la validación se observó que el frontend podía no mostrar inmediatamente la última alerta generada.

El backend sí generaba la alerta y `/alerts/ui` la devolvía correctamente, pero la interfaz necesitaba actualizar la vista para mostrar los datos más recientes.

---

### Explicación técnica

El frontend de esta versión es una interfaz sencilla desarrollada con HTML, CSS y JavaScript. No implementa actualización automática en tiempo real.

Esto significa que la interfaz no recibe cambios de forma automática cuando se genera una nueva alerta. Para ver los datos actualizados, debe realizar una nueva petición a la API mediante una acción de actualización o recarga.

Tecnologías como WebSockets, polling automático o Server-Sent Events podrían resolver este comportamiento, pero habrían añadido complejidad innecesaria para el alcance del MVP.

---

### Solución aplicada

Se comprobó que, al actualizar manualmente la vista, la nueva alerta aparecía correctamente.

No se implementó actualización automática porque no era necesaria para validar el flujo principal.

---

### Aprendizaje

La incidencia permitió diferenciar entre un error funcional y una limitación conocida.

El frontend no estaba fallando: simplemente no tenía actualización en tiempo real.

La función principal del frontend era mostrar alertas consultando la API, y esa función quedó validada.

---

## Síntesis de aprendizajes

### Aprendizajes técnicos

```text
- Docker Compose facilita reproducir entornos, pero los volúmenes pueden conservar estados antiguos.
- PostgreSQL mantiene credenciales y datos si el volumen ya fue inicializado.
- FastAPI permite construir una API clara, pero es importante separar bien la intención de cada endpoint.
- El modelo de datos debe distinguir claramente entre eventos, reglas y alertas.
- Los endpoints para frontend pueden necesitar respuestas enriquecidas sin modificar el modelo interno.
- El entorno de pruebas debe coincidir con el entorno real de ejecución.
- La virtualización depende de capas inferiores como módulos del kernel y configuración gráfica.
```

### Aprendizajes de diseño

```text
- Es mejor un MVP completo que un proyecto demasiado amplio e incompleto.
- No todas las funcionalidades interesantes deben implementarse en la primera versión.
- La lógica de reglas debe ser previsible antes que compleja.
- La trazabilidad entre entidades es fundamental para explicar el sistema.
- Separar ingesta, evaluación y consulta mejora la claridad del proyecto.
```

### Aprendizajes de validación

```text
- La respuesta de /ingest valida el evento, no la alerta.
- event_id y alert_id son identificadores distintos.
- Las evidencias deben separarse según lo que validan.
- /alerts/ui permite comprobar la alerta generada.
- /metrics permite comprobar incrementos globales de eventos y alertas.
```

---

## Impacto de las incidencias en el resultado final

Las incidencias no solo fueron obstáculos. También ayudaron a mejorar el proyecto.

El problema de alcance permitió definir mejor el MVP.

El problema con Docker y PostgreSQL permitió entender la persistencia de volúmenes.

La diferencia entre `/events` e `/ingest` ayudó a clarificar el diseño de la API.

La necesidad de `/alerts/ui` mejoró la relación entre backend y frontend.

La confusión entre `event_id` y `alert_id` hizo que las pruebas quedaran mejor separadas.

El problema con Pytest reforzó la importancia de ejecutar pruebas dentro del entorno correcto.

En conjunto, las incidencias ayudaron a convertir el SIEM Lab MVP en un sistema más claro, mejor documentado y más fácil de defender técnicamente.

---

## Conclusión

Los problemas encontrados durante el desarrollo formaron parte del proceso real de construcción del proyecto.

Algunos fueron errores técnicos concretos, como los problemas de VirtualBox, PostgreSQL o Pytest. Otros fueron decisiones de diseño, como delimitar el alcance, diferenciar `/events` de `/ingest` o separar eventos y alertas.

La resolución de estas incidencias permitió mejorar la arquitectura, la documentación y la validación del sistema.

El resultado final no es solo una aplicación funcional, sino también un proyecto cuyo proceso de desarrollo permite explicar decisiones técnicas, problemas encontrados y aprendizajes obtenidos.