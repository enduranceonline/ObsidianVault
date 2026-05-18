## Introducción

Durante el desarrollo del **SIEM Lab MVP** surgieron diferentes incidencias que afectaron tanto a la parte técnica como a la definición del proyecto. Algunas estuvieron relacionadas con errores concretos de entorno, configuración o ejecución; otras fueron problemas de diseño, alcance o interpretación del funcionamiento del sistema.

Estas incidencias fueron importantes porque obligaron a tomar decisiones, ajustar el alcance y comprender mejor cómo se relacionaban los distintos componentes del proyecto.

El objetivo de esta nota no es repetir todos los errores de forma aislada, sino analizar los problemas que realmente condicionaron el desarrollo y explicar qué se aprendió de ellos.

---

## Incidencias de alcance y enfoque

### Problema detectado

Uno de los primeros problemas fue definir hasta dónde debía llegar el proyecto. La temática elegida, un laboratorio inspirado en un SIEM, podía crecer fácilmente hasta convertirse en un proyecto demasiado grande.

Un SIEM real puede incluir muchas funcionalidades:

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
- Integración con otras herramientas de seguridad.
````

Intentar implementar todas estas funciones habría sido poco realista. El riesgo era acabar con muchas partes empezadas, pero ninguna suficientemente cerrada o validada.

También existía otro problema: en ciberseguridad es habitual montar laboratorios instalando herramientas ya existentes, como Wazuh, ELK, Splunk o Graylog. Eso puede ser útil desde el punto de vista práctico, pero en este caso habría reducido mucho el valor como proyecto de desarrollo de aplicaciones.

El proyecto tenía que demostrar desarrollo propio, no solo instalación y configuración de software externo.

---

### Decisión tomada

Se decidió plantear el sistema como un **MVP**, centrado únicamente en el flujo principal:

```text
evento → ingesta → almacenamiento → evaluación → alerta → consulta
```

También se decidió no instalar un SIEM real como núcleo del proyecto. En su lugar, se desarrollaron componentes propios:

```text
- API de ingesta.
- Modelo de datos.
- Motor básico de reglas.
- Gestión de alertas.
- Endpoints de consulta.
- Frontend básico.
```

Esta decisión permitió mantener el proyecto dentro de un alcance razonable y, al mismo tiempo, conservar su relación con la ciberseguridad defensiva.

---

### Aprendizaje

El principal aprendizaje fue que limitar el alcance no significa empobrecer el proyecto. En este caso, limitarlo permitió construir una versión funcional, comprobable y coherente.

Un MVP no consiste en hacer “poco”, sino en seleccionar qué parte del sistema aporta más valor y desarrollarla correctamente.

También se entendió la diferencia entre montar un laboratorio de ciberseguridad y desarrollar una aplicación orientada a ciberseguridad. El proyecto debía estar más cerca de lo segundo.

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

Estos errores indicaban que VirtualBox no podía cargar correctamente los módulos necesarios del kernel.

También apareció un problema de pantalla negra al arrancar la máquina virtual. La VM parecía iniciar, pero no permitía acceder correctamente al entorno gráfico.

---

### Explicación técnica

VirtualBox necesita módulos del kernel para poder ejecutar máquinas virtuales. En sistemas Linux, estos módulos suelen depender de paquetes como `virtualbox-dkms`.

DKMS permite recompilar módulos cuando cambia el kernel del sistema. Si hay una diferencia entre la versión instalada de VirtualBox, los módulos cargados y el kernel en uso, pueden aparecer errores como los anteriores.

Por eso, aunque VirtualBox estuviera instalado, la máquina virtual no podía arrancar correctamente si los módulos no estaban disponibles o no coincidían con la versión esperada.

La pantalla negra, en cambio, estaba más relacionada con la configuración gráfica de la máquina virtual. Este tipo de problema puede deberse a parámetros de aceleración gráfica, controlador de vídeo virtual, memoria de vídeo o compatibilidad entre la VM y el host.

---

### Solución aplicada

Se revisó la instalación de VirtualBox y se sincronizaron los paquetes necesarios:

```text
virtualbox
virtualbox-qt
virtualbox-dkms
```

También se ajustó la configuración gráfica de la máquina virtual hasta conseguir que arrancara correctamente.

Finalmente, la VM `siem-lab` quedó operativa y pudo utilizarse como entorno principal de desarrollo.

---

### Aprendizaje

Este problema ayudó a entender que el entorno de desarrollo también forma parte del proyecto. Si la virtualización falla, el código puede estar bien y aun así el sistema no ser ejecutable.

También permitió diferenciar entre:

```text
- Problemas del código.
- Problemas de Docker.
- Problemas de base de datos.
- Problemas del sistema anfitrión.
- Problemas de virtualización.
```

Este aprendizaje fue importante porque evitó buscar errores en el backend cuando el problema real estaba en capas inferiores del entorno.

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

Por eso la API intentaba conectarse usando una contraseña, mientras PostgreSQL seguía esperando otra.

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
Contenedor → proceso o servicio en ejecución.
Imagen     → plantilla desde la que se crea el contenedor.
Volumen    → almacenamiento persistente que puede sobrevivir al contenedor.
```

Este problema fue útil porque permitió comprender mejor cómo Docker gestiona el estado de servicios como PostgreSQL. En proyectos con base de datos, los volúmenes son una ventaja porque conservan datos, pero también pueden mantener configuraciones antiguas que provocan errores difíciles de interpretar.

---

## Incidencias de diseño de API

### Problema detectado

Durante el desarrollo apareció una cuestión importante: diferenciar correctamente entre crear eventos y procesar eventos.

Inicialmente podía parecer suficiente disponer de endpoints como:

```http
POST /events
GET /events
```

Sin embargo, estos endpoints solo permitían trabajar con eventos como registros de base de datos. No representaban el comportamiento principal del SIEM Lab MVP.

El flujo importante del proyecto era otro:

```text
recibir evento → almacenarlo → evaluar reglas → generar alerta
```

Por tanto, hacía falta un endpoint que no solo guardara el evento, sino que activara el procesamiento.

---

### Decisión tomada

Se definió `/ingest` como endpoint principal del sistema:

```http
POST /ingest
```

La diferencia quedó establecida así:

```text
/events → permite crear o consultar eventos.
/ingest → recibe eventos y activa el motor de reglas.
```

Esto permitió que el proyecto tuviera un flujo más realista y más fácil de explicar.

---

### Aprendizaje

El aprendizaje fue que el diseño de una API no consiste solo en crear rutas que guarden datos. Cada endpoint debe representar una intención clara dentro del sistema.

En este caso, `/events` representa una operación de datos, mientras que `/ingest` representa una operación de negocio.

La diferencia es importante:

```text
Guardar un evento no equivale a procesarlo.
```

Este matiz permitió separar mejor la lógica del proyecto y evitar confusiones durante las pruebas.

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

La duda era cómo proporcionar esos datos sin duplicarlos innecesariamente dentro de la tabla `alerts`.

---

### Explicación técnica

Duplicar datos del evento dentro de la alerta habría simplificado la lectura desde el frontend, pero habría empeorado el modelo de datos.

Por ejemplo, si la alerta almacenara de nuevo el `source`, la `severity` y el `message`, esos datos estarían repetidos:

```text
events.source  → dato original
alerts.source  → copia duplicada
```

Esto puede provocar inconsistencias si en algún momento se modifica una estructura o se quiere consultar el origen real de la información.

La alternativa era mantener las relaciones correctamente:

```text
alerts.event_id → events.id
alerts.rule_id  → rules.id
```

Y crear endpoints que devuelvan una respuesta enriquecida combinando datos de varias tablas.

---

### Solución aplicada

Se crearon endpoints específicos para el frontend:

```http
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Estos endpoints permiten devolver alertas junto con información del evento asociado y de la regla activada.

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

Este problema permitió entender mejor la diferencia entre:

```text
Modelo de datos interno → cómo se almacena la información.
Respuesta de API        → cómo se entrega la información a quien la consume.
```

No siempre conviene adaptar la base de datos al frontend. A veces es mejor mantener un modelo limpio y crear endpoints específicos para la visualización.

Esto también permitió comprender la utilidad de separar responsabilidades:

```text
Base de datos → persistencia ordenada.
API           → composición y transformación de datos.
Frontend      → presentación visual.
```

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

El riesgo era que el motor creciera demasiado o que tuviera comportamientos ambiguos.

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

Este valor permite saber que varios eventos pertenecen a la misma máquina o fuente lógica.

El problema aparece al aplicar funciones como `threshold` o `throttle`.

Un `threshold` necesita contar eventos relacionados dentro de una ventana temporal. Por ejemplo:

```text
3 eventos en 60 segundos para el mismo host.
```

Pero si no existe `group_key`, el sistema no sabe con claridad qué eventos debe agrupar.

El `throttle` también necesita saber si una alerta es repetida para la misma fuente. Sin `group_key`, el sistema podría bloquear alertas de forma incorrecta o permitir duplicados sin control.

---

### Decisión tomada

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

También se entendió que, en un MVP, es preferible tener reglas más simples pero bien definidas que intentar construir una correlación avanzada difícil de validar.

El criterio fue priorizar un motor:

```text
comprensible → documentado → validable
```

antes que uno más ambicioso pero menos claro.

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

Sin embargo, después el motor de reglas puede generar una alerta diferente, con otro identificador:

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

Ejemplo real validado:

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

Este ajuste hizo que las pruebas fueran más precisas y menos ambiguas.

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

Por tanto, para validar correctamente el backend, lo más coherente era ejecutar las pruebas dentro de ese contenedor.

---

## Incidencias del frontend

### Problema detectado

Durante la validación se observó que el frontend podía no mostrar inmediatamente la última alerta generada.

El backend sí generaba la alerta y `/alerts/ui` la devolvía correctamente, pero la interfaz necesitaba actualizar la vista para mostrar los datos más recientes.

---

### Explicación técnica

El frontend de esta versión es una interfaz sencilla desarrollada con HTML, CSS y JavaScript. No implementa actualización automática en tiempo real.

Esto significa que la interfaz no recibe cambios de forma automática cuando se genera una nueva alerta. Para ver los datos actualizados, debe realizar una nueva petición a la API, normalmente mediante una acción de actualización o recarga.

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

Las incidencias del proyecto permitieron extraer varios aprendizajes técnicos y metodológicos.

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

### Aprendizajes de documentación

```text
- La documentación debe revisarse igual que el código.
- Las pruebas deben tener evidencias separadas.
- No conviene mezclar resultados esperados con resultados obtenidos.
- Es importante indicar qué valida cada comando.
- La redacción técnica debe evitar confundir entidades relacionadas.
```

---

## Impacto de las incidencias en el resultado final

Las incidencias no solo fueron obstáculos. También ayudaron a mejorar el proyecto.

El problema de alcance permitió definir mejor el MVP.

El problema con Docker y PostgreSQL permitió entender la persistencia de volúmenes.

La confusión entre `/events` e `/ingest` ayudó a clarificar el diseño de la API.

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