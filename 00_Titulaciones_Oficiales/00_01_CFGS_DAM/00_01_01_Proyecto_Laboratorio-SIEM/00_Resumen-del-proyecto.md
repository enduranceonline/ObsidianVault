## Descripción general

El proyecto **SIEM Lab MVP** consiste en el desarrollo de un laboratorio de ciberseguridad orientado a la monitorización básica de eventos y generación de alertas. El objetivo principal ha sido construir una versión mínima funcional de un sistema SIEM, capaz de recibir eventos simulados, almacenarlos en una base de datos, evaluarlos mediante reglas de detección y generar alertas consultables desde una API y una interfaz web sencilla.

El proyecto se ha planteado como una aplicación propia, no como una simple instalación de herramientas ya existentes. Esta decisión es importante porque permite relacionar el proyecto con el ámbito de la ciberseguridad y el Blue Team, pero manteniendo al mismo tiempo el enfoque propio del ciclo de Desarrollo de Aplicaciones Multiplataforma: análisis, diseño, desarrollo, pruebas, documentación y validación de una aplicación.

El sistema se ha desarrollado con un backend en **FastAPI**, una base de datos **PostgreSQL**, contenedores gestionados mediante **Docker Compose**, una interfaz de consulta con **Adminer** y un frontend básico construido con **HTML, CSS y JavaScript**. Además, se han utilizado **SQLAlchemy** y **Alembic** para la gestión del modelo de datos y migraciones, y **Pytest** para validar parte del comportamiento del sistema.

No se trata de un SIEM real de producción, sino de un **MVP académico y funcional** diseñado para demostrar conceptos fundamentales de monitorización de seguridad, ingesta de eventos, evaluación mediante reglas, generación de alertas y consulta de información relevante.

---

## Flujo principal del sistema

El funcionamiento general del sistema puede resumirse en el siguiente flujo:

```text
Evento o log simulado
        ↓
Ingesta mediante API
        ↓
Almacenamiento en PostgreSQL
        ↓
Evaluación mediante reglas activas
        ↓
Generación automática de alertas
        ↓
Consulta mediante API y frontend
````

El endpoint principal del proyecto es `/ingest`, ya que representa el punto de entrada de los eventos de seguridad. Cuando la API recibe un evento, este se almacena en la base de datos y posteriormente se evalúa contra las reglas activas. Si el evento cumple las condiciones definidas en alguna regla, el sistema genera una alerta asociada.

Este flujo permite representar de forma simplificada el comportamiento de una solución SIEM: recibir información de seguridad, procesarla, aplicar lógica de detección y generar alertas que puedan ser consultadas posteriormente.

---

## Objetivo general del proyecto

El objetivo general del proyecto ha sido desarrollar un laboratorio SIEM básico, funcional y reproducible, que permita simular el ciclo principal de tratamiento de eventos de seguridad:

```text
recepción → almacenamiento → evaluación → alerta → consulta → gestión
```

Con este proyecto se busca demostrar la capacidad de diseñar y construir una aplicación backend con persistencia en base de datos, lógica de negocio propia, endpoints documentados, interfaz de consulta y pruebas funcionales.

---

## Objetivos específicos

Los objetivos específicos del proyecto han sido:

```text
- Crear una API capaz de recibir eventos o logs simulados.
- Almacenar los eventos recibidos en una base de datos relacional.
- Diseñar un modelo de datos para eventos, reglas y alertas.
- Implementar un sistema básico de reglas de detección.
- Generar alertas automáticamente cuando un evento coincide con una regla activa.
- Permitir la consulta de alertas mediante API.
- Permitir el cambio de estado de las alertas.
- Crear endpoints enriquecidos para facilitar la visualización desde frontend.
- Desarrollar una interfaz web sencilla para consultar alertas.
- Contenerizar el entorno mediante Docker Compose.
- Documentar la API mediante Swagger.
- Validar el funcionamiento mediante pruebas manuales y automatizadas.
- Documentar el proyecto para que pueda reproducirse desde cero.
```

---

## Alcance del proyecto

Uno de los aspectos más importantes del desarrollo ha sido delimitar correctamente el alcance. Al tratarse de un proyecto inspirado en un SIEM, existía el riesgo de intentar construir una herramienta demasiado amplia o cercana a una solución profesional real.

Un SIEM completo puede incluir múltiples fuentes de logs, normalización avanzada, correlación compleja, dashboards, autenticación, gestión de usuarios, reporting, almacenamiento histórico, integración con agentes, alertas en tiempo real y despliegues distribuidos.

Sin embargo, para este proyecto se decidió acotar el alcance a un **MVP académico funcional**, centrado en demostrar el flujo esencial de un SIEM:

```text
evento → ingesta → almacenamiento → evaluación → alerta → consulta
```

Esta decisión permitió mantener el proyecto dentro de unos límites asumibles y, al mismo tiempo, conservar su valor técnico. En lugar de intentar abarcar muchas funcionalidades de forma superficial, se priorizó construir un flujo reducido pero completo, coherente y verificable.

---

## Enfoque como MVP

El proyecto se ha desarrollado siguiendo una lógica de **Minimum Viable Product**. Esto significa que se han priorizado las funcionalidades necesarias para demostrar el núcleo del sistema, dejando fuera aquellas que habrían aumentado mucho la complejidad sin ser imprescindibles para la entrega académica.

Funcionalidades incluidas en el MVP:

```text
- Ingesta de eventos mediante API.
- Persistencia en PostgreSQL.
- Gestión básica de reglas.
- Evaluación automática de eventos mediante reglas activas.
- Generación automática de alertas.
- Consulta y filtrado de alertas.
- Cambio de estado de alertas.
- Frontend básico de visualización.
- Métricas y healthcheck.
- Pruebas automatizadas mínimas.
- Documentación técnica del proyecto.
```

Funcionalidades descartadas o aplazadas para futuras mejoras:

```text
- Autenticación de usuarios.
- Roles y permisos.
- Integración con fuentes reales de logs.
- Agentes instalados en máquinas externas.
- Dashboards avanzados.
- Correlación compleja entre múltiples eventos.
- Notificaciones externas.
- Exportación de informes.
- Despliegue en producción.
```

Esta delimitación fue necesaria para evitar que el proyecto creciera de forma descontrolada. El objetivo no era construir un SIEM completo, sino una base funcional que permitiera entender y demostrar sus componentes esenciales.

---

## Tecnologías principales

Las tecnologías utilizadas en el proyecto han sido:

```text
Python 3.12
FastAPI
Uvicorn
PostgreSQL 16
SQLAlchemy
Alembic
Docker Compose
Adminer
HTML
CSS
JavaScript
Pytest
VirtualBox
Git/GitHub
```

La elección de estas herramientas responde a la necesidad de construir un entorno modular, reproducible y fácil de desplegar.

**FastAPI** se eligió por ser un framework moderno, rápido y adecuado para crear APIs REST. Además, genera automáticamente documentación interactiva mediante Swagger, lo que facilita la prueba y validación de endpoints.

**PostgreSQL** se utilizó como sistema gestor de base de datos relacional por su robustez y porque permite modelar correctamente entidades como eventos, reglas y alertas.

**SQLAlchemy** se utilizó para trabajar con modelos de datos desde Python y mantener una separación clara entre la lógica de la aplicación y la base de datos.

**Alembic** se incorporó para gestionar migraciones y mantener el esquema de base de datos de forma controlada.

**Docker Compose** permitió levantar varios servicios relacionados entre sí de forma sencilla: API, base de datos y Adminer.

**Adminer** se utilizó como herramienta ligera para consultar visualmente la base de datos y comprobar la persistencia de los datos.

**HTML, CSS y JavaScript** se utilizaron para construir un frontend básico, suficiente para demostrar la consulta visual de alertas sin introducir frameworks complejos.

**Pytest** se utilizó para ejecutar pruebas automatizadas sobre parte del comportamiento del backend.

**VirtualBox** se utilizó como plataforma de virtualización para ejecutar el entorno de desarrollo dentro de una máquina virtual.

---

## Componentes principales del sistema

El sistema está formado por tres servicios principales ejecutados mediante Docker Compose:

```text
siem-db       → Base de datos PostgreSQL
siem-api      → Backend FastAPI
siem-adminer  → Interfaz web para consultar PostgreSQL
```

Además, el proyecto incluye un frontend independiente servido mediante un servidor HTTP local de Python. Este frontend consume los endpoints de la API para mostrar alertas, aplicar filtros y consultar detalles.

La estructura general permite separar responsabilidades:

```text
- La API recibe eventos, gestiona reglas y expone alertas.
- PostgreSQL almacena eventos, reglas y alertas.
- Adminer permite inspeccionar la base de datos.
- El frontend permite visualizar alertas desde el navegador.
- Docker Compose coordina los servicios necesarios.
```

---

## Modelo funcional del sistema

El modelo funcional del sistema gira alrededor de tres entidades principales:

```text
events
rules
alerts
```

Los **eventos** representan logs o sucesos simulados que entran en el sistema. Cada evento incluye información como origen, severidad, mensaje y metadatos.

Las **reglas** definen condiciones de detección. Una regla puede comprobar, por ejemplo, si un evento procede de una fuente concreta, si alcanza una severidad mínima o si contiene una determinada cadena de texto.

Las **alertas** son el resultado de aplicar las reglas sobre los eventos. Cuando un evento coincide con una regla activa, el sistema genera una alerta asociada tanto al evento como a la regla que la ha provocado.

Esta relación permite saber no solo que se ha generado una alerta, sino también por qué se ha generado y a partir de qué evento.

---

## Funcionamiento del motor de reglas

El motor de reglas es una de las partes centrales del proyecto. Su función es evaluar los eventos recibidos y determinar si deben generar una alerta.

El flujo interno es el siguiente:

```text
1. La API recibe un evento mediante /ingest.
2. El evento se almacena en PostgreSQL.
3. El sistema obtiene un group_key a partir de meta.host.
4. Se consultan las reglas activas.
5. Cada regla se compara con el evento.
6. Si hay coincidencia, se genera una alerta.
7. La alerta queda asociada al evento y a la regla.
```

Las reglas pueden utilizar diferentes condiciones:

```text
source
severity_min
contains
meta_match
throttle_seconds
threshold_count
threshold_seconds
```

También se incorporó lógica relacionada con:

```text
- throttle
- anti-duplicado
- threshold por ventana temporal
- agrupación mediante group_key
```

Durante el desarrollo fue necesario definir con claridad cómo debía comportarse el motor de reglas para evitar resultados ambiguos. Finalmente, se decidió que el `group_key` se obtuviera a partir de `meta.host`.

La decisión final fue:

```text
- El group_key se obtiene a partir de meta.host.
- Si no existe group_key, se permiten alertas unitarias.
- El throttle y el anti-duplicado solo se aplican cuando existe group_key.
- Los thresholds requieren group_key para funcionar correctamente.
```

Esta solución simplifica el comportamiento del sistema y permite documentar sus limitaciones de forma clara.

---

## Endpoints principales

Los endpoints principales del proyecto son:

```text
GET /health
GET /info
GET /metrics

POST /events
GET /events

POST /ingest

POST /rules
GET /rules

GET /alerts
GET /alerts/{alert_id}
PATCH /alerts/{alert_id}

GET /alerts/ui
GET /alerts/ui/count
GET /alerts/{alert_id}/ui
```

El endpoint `/health` permite comprobar el estado de la API y la conexión con la base de datos.

El endpoint `/metrics` devuelve métricas básicas del sistema, como el número total de eventos, reglas y alertas.

El endpoint `/ingest` es el punto principal de entrada de eventos y activa el proceso de evaluación mediante reglas.

Los endpoints de `/rules` permiten crear y consultar reglas.

Los endpoints de `/alerts` permiten consultar alertas, aplicar filtros y modificar su estado.

Los endpoints `/alerts/ui` se crearon para facilitar al frontend la consulta de alertas enriquecidas con información adicional procedente del evento asociado.

---

## Gestión de alertas

Las alertas generadas por el sistema pueden encontrarse en diferentes estados:

```text
open
ack
closed
```

El estado `open` representa una alerta abierta pendiente de revisión.

El estado `ack` representa una alerta reconocida o aceptada por el usuario.

El estado `closed` representa una alerta cerrada.

La API permite modificar el estado de una alerta mediante el endpoint:

```http
PATCH /alerts/{alert_id}
```

Esta funcionalidad permite simular una parte básica del ciclo de gestión de alertas habitual en herramientas de monitorización y seguridad.

---

## Frontend

El frontend del proyecto se ha desarrollado con HTML, CSS y JavaScript. Su objetivo no es ser una interfaz avanzada, sino proporcionar una forma visual de consultar las alertas generadas por el sistema.

El frontend permite:

```text
- Visualizar alertas.
- Aplicar filtros.
- Consultar información enriquecida.
- Ver el estado de las alertas.
- Actualizar la información mostrada.
- Acceder al detalle de una alerta.
```

Durante la validación final se comprobó que el frontend cargaba correctamente y mostraba las alertas generadas por el backend.

---

## Pruebas y validación

El proyecto ha sido validado mediante pruebas manuales y automatizadas.

Se comprobaron los siguientes puntos:

```text
- La máquina virtual arranca correctamente.
- Docker Compose levanta los servicios necesarios.
- PostgreSQL funciona correctamente.
- Adminer permite consultar la base de datos.
- La API FastAPI responde correctamente.
- Swagger está disponible en /docs.
- /health responde correctamente.
- /metrics devuelve información del sistema.
- /rules lista reglas existentes.
- /ingest permite enviar eventos simulados.
- El motor de reglas genera alertas automáticamente.
- /alerts/ui muestra alertas enriquecidas.
- PATCH /alerts/{id} permite cambiar el estado de una alerta.
- Los filtros por estado, severidad y texto funcionan.
- El frontend carga correctamente y muestra las alertas.
- Los tests automatizados se ejecutan correctamente.
```

Durante una prueba final se envió un evento de tipo SSH con severidad suficiente y mensaje coincidente con una regla activa. El sistema almacenó el evento, evaluó las reglas y generó una alerta asociada.

La alerta pudo consultarse posteriormente desde la API, visualizarse desde el frontend y modificarse de estado de `open` a `ack`.

Este resultado confirma que el flujo principal del proyecto funciona de extremo a extremo.

---

## Problemas relevantes durante el desarrollo

Durante el desarrollo del proyecto aparecieron varios problemas técnicos, de planificación y de diseño. Estos problemas fueron importantes porque condicionaron la evolución del proyecto y ayudaron a tomar decisiones más realistas.

No todos los problemas estuvieron relacionados con errores de código o configuración. También hubo dificultades vinculadas al alcance del proyecto, las normas de la entrega, la necesidad de justificar el desarrollo propio y la delimitación de lo que debía incluir el MVP.

---

### Problemas de alcance

Uno de los principales retos fue definir hasta dónde debía llegar el proyecto. Al trabajar sobre una temática relacionada con SIEM, era fácil ampliar demasiado el alcance e intentar incluir funcionalidades propias de soluciones profesionales.

Durante el planteamiento del proyecto se valoraron funcionalidades como dashboards más avanzados, integración con fuentes reales de logs, agentes externos, normalización de eventos, autenticación, informes o correlación más compleja.

Finalmente, se decidió limitar el proyecto a un MVP centrado en el flujo principal:

```text
evento → ingesta → almacenamiento → evaluación → alerta → consulta
```

Esta decisión permitió mantener el proyecto dentro de un alcance razonable y evitar que la complejidad técnica impidiera terminar una versión funcional.

---

### Problema de enfoque académico

Otro problema importante fue evitar que el proyecto se convirtiera únicamente en un laboratorio basado en herramientas existentes. Instalar y configurar herramientas de ciberseguridad puede ser útil desde el punto de vista práctico, pero no era suficiente para justificar un proyecto de desarrollo de aplicaciones.

Por este motivo, se decidió desarrollar una aplicación propia:

```text
- API propia.
- Modelo de datos propio.
- Motor de reglas propio.
- Endpoints personalizados.
- Frontend básico propio.
- Documentación propia.
- Pruebas propias.
```

Esta decisión permitió mantener el equilibrio entre la temática de ciberseguridad y los objetivos académicos del ciclo de DAM.

---

### Problemas con la definición del MVP

Durante el desarrollo fue necesario ajustar varias veces la definición del MVP. Algunas funcionalidades inicialmente atractivas fueron descartadas porque aumentaban la complejidad sin ser imprescindibles para demostrar el funcionamiento principal del sistema.

El criterio utilizado fue priorizar las funcionalidades que aportaban valor directo al flujo principal. Por ese motivo, se mantuvieron la ingesta, la persistencia, las reglas, las alertas, los filtros, el frontend básico y las pruebas.

En cambio, se dejaron para futuras mejoras las funcionalidades más avanzadas, como autenticación, integración con logs reales, dashboards completos o correlación avanzada.

Este proceso permitió entender que un MVP no consiste en hacer una versión pobre de una herramienta grande, sino en construir una versión pequeña pero coherente, funcional y demostrable.

---

### Problemas relacionados con el motor de reglas

El motor de reglas fue una de las partes que requirió más decisiones de diseño. No bastaba con comprobar si un evento coincidía con una regla; también había que definir cómo se comportaban los umbrales, los duplicados y la agrupación de eventos.

Uno de los puntos más importantes fue el uso de `group_key`. Se decidió obtenerlo a partir de `meta.host`, ya que el host permite agrupar eventos relacionados con una misma máquina o fuente.

También fue necesario decidir qué ocurría si un evento no tenía `group_key`. Para evitar comportamientos ambiguos, se definió que las alertas unitarias podían generarse igualmente, pero que la lógica de throttle, anti-duplicado y threshold dependía de la existencia de un `group_key`.

Esta decisión permitió simplificar el motor y mantener un comportamiento más previsible.

---

### Problemas relacionados con el modelo de datos

Durante el desarrollo también fue necesario ajustar la relación entre eventos, reglas y alertas.

El modelo final se organizó alrededor de tres tablas principales:

```text
events
rules
alerts
```

Cada alerta queda asociada a un evento y a una regla. Esta decisión es importante porque permite reconstruir el origen de una alerta y entender qué regla la generó.

También apareció la necesidad de mostrar en el frontend información que no pertenecía directamente a la alerta, sino al evento relacionado. Para resolverlo, se optó por crear endpoints enriquecidos como `/alerts/ui`, en lugar de duplicar innecesariamente datos dentro de la tabla de alertas.

Esta decisión permitió mantener un modelo de datos más limpio y ofrecer al frontend la información necesaria.

---

### Problemas relacionados con la API

A medida que el backend crecía, fue necesario estabilizar el contrato de la API. El sistema necesitaba endpoints coherentes para consultar alertas, aplicar filtros, contar resultados y modificar estados.

Se definieron operaciones específicas para:

```text
- Consultar alertas.
- Consultar una alerta concreta.
- Consultar alertas enriquecidas para frontend.
- Contar alertas filtradas.
- Cambiar el estado de una alerta.
```

También se definieron estados controlados para las alertas:

```text
open
ack
closed
```

Esto permitió que la API tuviera un comportamiento más claro y que el frontend pudiera consumirla de forma estable.

---

### Problemas de configuración y seguridad

Durante el desarrollo se detectó la necesidad de separar la configuración real del proyecto de la configuración de ejemplo. Era importante evitar subir credenciales reales o valores sensibles al repositorio.

Para solucionarlo se utilizaron archivos `.env` y `.env.example`. El archivo `.env.example` permite documentar las variables necesarias sin exponer credenciales reales, mientras que `.gitignore` evita subir archivos de configuración sensibles.

Esta decisión mejoró la seguridad básica del proyecto y facilitó su reproducción desde cero en otro entorno.

---

### Problemas de virtualización

Inicialmente se intentó trabajar con VMware, pero aparecieron problemas de estabilidad y compatibilidad. Esto dificultaba avanzar con normalidad en el desarrollo.

La solución fue migrar el entorno a VirtualBox. Esta decisión permitió trabajar de forma más estable con la máquina virtual `siem-lab`.

También aparecieron problemas con VirtualBox en Kali Linux, concretamente errores relacionados con los módulos del sistema:

```text
VERR_VM_DRIVER_NOT_INSTALLED
VERR_VM_DRIVER_VERSION_MISMATCH
```

Estos errores se resolvieron reinstalando y sincronizando los paquetes necesarios de VirtualBox y DKMS.

Este problema permitió comprender mejor la relación entre el software de virtualización, los módulos del kernel y el sistema anfitrión.

---

### Problema de pantalla negra en la máquina virtual

Durante una fase del desarrollo, la máquina virtual arrancaba pero se quedaba en pantalla negra. Este problema impedía acceder correctamente al entorno de trabajo.

La solución consistió en revisar y ajustar la configuración gráfica de VirtualBox hasta conseguir que la VM arrancara correctamente.

Este incidente reforzó la importancia de saber diagnosticar problemas de entorno, especialmente cuando el desarrollo depende de una máquina virtual.

---

### Problema de autenticación con PostgreSQL

Uno de los problemas técnicos más relevantes fue el fallo de autenticación entre la API y PostgreSQL.

El error era:

```text
FATAL: password authentication failed for user "siem"
```

La causa estaba relacionada con la persistencia de volúmenes Docker. Aunque se habían actualizado las credenciales en la configuración, el volumen antiguo de PostgreSQL conservaba una contraseña anterior.

La solución fue modificar la contraseña del usuario directamente en PostgreSQL:

```bash
docker compose exec db psql -U siem -d siem -c "ALTER USER siem WITH PASSWORD 'change_me';"
docker compose restart api
```

Después de aplicar la solución, el endpoint `/health` respondió correctamente indicando que tanto la API como la base de datos estaban operativas.

Este problema permitió entender mejor cómo funcionan los volúmenes persistentes de Docker y por qué los cambios en variables de entorno no siempre modifican una base de datos ya inicializada.

---

### Problema con las pruebas automatizadas

Durante la validación se intentó ejecutar `pytest` desde el entorno virtual local, pero no estaba instalado:

```text
No module named pytest
```

Como el proyecto estaba preparado para funcionar dentro de Docker, se decidió ejecutar las pruebas dentro del contenedor de la API:

```bash
docker compose exec api python -m pytest
```

El resultado fue correcto:

```text
4 passed
```

Esta solución permitió validar el proyecto sin depender del entorno local del sistema anfitrión. También reforzó la utilidad de Docker como herramienta para mantener entornos reproducibles.

---

## Estado final del proyecto

El proyecto ha quedado funcionalmente validado.

Se ha comprobado que funcionan correctamente:

```text
- VirtualBox y la máquina virtual siem-lab.
- Docker Compose.
- PostgreSQL.
- Adminer.
- FastAPI.
- Swagger.
- Healthcheck.
- Métricas.
- Gestión de reglas.
- Ingesta de eventos.
- Motor de reglas.
- Generación automática de alertas.
- Consulta de alertas enriquecidas.
- Cambio de estado de alertas.
- Filtros por estado, severidad y texto.
- Frontend.
- Tests automatizados.
- README actualizado.
- Repositorio en GitHub.
```

Durante la validación final, el sistema fue capaz de recibir un evento de demo, almacenarlo, evaluarlo mediante una regla activa y generar una alerta. Posteriormente, dicha alerta pudo consultarse, visualizarse desde el frontend y cambiarse de estado.

Este comportamiento confirma que el flujo principal del SIEM Lab MVP funciona correctamente de extremo a extremo.

---

## Resultado obtenido

El resultado final es un laboratorio SIEM básico, funcional y reproducible, capaz de demostrar de forma práctica el ciclo completo de tratamiento de eventos de seguridad.

El proyecto cumple su objetivo principal: crear una base técnica realista sobre la que entender cómo se organizan algunos componentes habituales en herramientas de monitorización y detección de seguridad.

Aunque el sistema tiene limitaciones propias de un MVP, proporciona una base clara para futuras ampliaciones. Entre las posibles mejoras se encuentran la integración con fuentes reales de logs, autenticación de usuarios, dashboards más avanzados, normalización de eventos, notificaciones externas o despliegue en un entorno más cercano a producción.

En conclusión, el proyecto no solo demuestra el funcionamiento de una aplicación desarrollada con backend, base de datos, frontend y contenedores, sino que también refleja un proceso completo de análisis, toma de decisiones, resolución de problemas, validación y documentación.
