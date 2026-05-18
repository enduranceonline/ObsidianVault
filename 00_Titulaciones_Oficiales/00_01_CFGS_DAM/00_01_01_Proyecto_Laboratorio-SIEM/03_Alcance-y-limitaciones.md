## Alcance del proyecto

El proyecto **SIEM Lab MVP** se ha definido como una versión mínima funcional de un laboratorio SIEM. Su finalidad es representar el flujo básico de tratamiento de eventos de seguridad, desde la ingesta inicial hasta la generación y consulta de alertas.

El alcance se ha centrado en construir una aplicación propia, funcional y demostrable, evitando que el proyecto se convierta en una simple instalación de herramientas existentes o en un intento de desarrollar un SIEM completo.

El flujo principal incluido en el alcance es:

```text
evento simulado → ingesta → almacenamiento → evaluación → alerta → consulta
````

A partir de este flujo, el sistema permite recibir eventos, almacenarlos en base de datos, compararlos con reglas activas y generar alertas cuando se cumplen determinadas condiciones.

---

## Funcionalidades incluidas

El alcance funcional del proyecto incluye las siguientes capacidades:

```text
- Ingesta de eventos simulados mediante API.
- Almacenamiento persistente en PostgreSQL.
- Gestión básica de reglas de detección.
- Evaluación automática de eventos mediante reglas activas.
- Generación automática de alertas.
- Consulta de eventos, reglas y alertas.
- Consulta enriquecida de alertas para el frontend.
- Filtrado de alertas por estado, severidad y texto.
- Cambio de estado de alertas.
- Visualización básica mediante frontend.
- Consulta de métricas generales del sistema.
- Comprobación del estado de la API y la base de datos.
- Documentación automática mediante Swagger.
- Consulta visual de la base de datos mediante Adminer.
- Ejecución del entorno mediante Docker Compose.
- Pruebas automatizadas básicas.
```

Estas funcionalidades permiten demostrar el ciclo principal del sistema sin añadir una complejidad excesiva.

---

## Funcionalidades excluidas

Para mantener el proyecto dentro de un alcance realista, se dejaron fuera varias funcionalidades propias de soluciones SIEM más avanzadas.

No forman parte de esta versión:

```text
- Autenticación de usuarios.
- Gestión de roles y permisos.
- Integración con logs reales del sistema.
- Agentes instalados en equipos externos.
- Normalización avanzada de eventos.
- Correlación compleja entre múltiples fuentes.
- Dashboards avanzados en tiempo real.
- Notificaciones por correo, Telegram u otros canales.
- Informes exportables.
- Retención histórica avanzada.
- Sistema multiusuario.
- Despliegue en producción.
- Alta disponibilidad.
- Cifrado avanzado de comunicaciones internas.
```

Estas funcionalidades se consideran posibles mejoras futuras, pero no eran necesarias para demostrar el objetivo principal del proyecto.

---

## Alcance técnico

A nivel técnico, el proyecto incluye los siguientes componentes:

```text
- Backend desarrollado con FastAPI.
- Base de datos PostgreSQL.
- Modelos gestionados con SQLAlchemy.
- Migraciones mediante Alembic.
- Servicios definidos con Docker Compose.
- Adminer para inspección de base de datos.
- Frontend básico con HTML, CSS y JavaScript.
- Pruebas con Pytest.
- Documentación en README.
- Control de versiones con Git y GitHub.
```

El sistema se ejecuta dentro de una máquina virtual de laboratorio y los servicios principales se levantan mediante contenedores Docker.

La arquitectura se ha diseñado para separar responsabilidades:

```text
FastAPI       → lógica de aplicación y API
PostgreSQL    → persistencia de datos
Adminer       → inspección de base de datos
Frontend      → visualización básica de alertas
Docker Compose → orquestación local de servicios
```

---

## Alcance del motor de reglas

El motor de reglas se ha planteado como una lógica de detección básica, no como un sistema de correlación avanzado.

Las reglas permiten evaluar condiciones como:

```text
- Fuente del evento.
- Severidad mínima.
- Texto contenido en el mensaje.
- Coincidencias en metadatos.
- Umbrales simples.
- Control básico de duplicados.
- Throttle por ventana temporal.
```

El sistema utiliza `meta.host` como base para calcular el `group_key`, lo que permite agrupar eventos relacionados con una misma máquina o fuente.

El comportamiento definido para esta versión es:

```text
- Las alertas simples pueden generarse aunque no exista group_key.
- El throttle y el anti-duplicado dependen del group_key.
- Los thresholds requieren group_key para evitar agrupaciones ambiguas.
```

Esta decisión reduce la complejidad del motor y permite mantener un comportamiento más previsible.

---

## Alcance del frontend

El frontend tiene un alcance limitado. Su función principal es demostrar visualmente que las alertas generadas por el backend pueden consultarse desde una interfaz web.

Incluye:

```text
- Listado de alertas.
- Visualización de información relevante.
- Filtros básicos.
- Actualización de datos.
- Acceso al detalle de alertas.
```

No se ha buscado crear un dashboard profesional. El frontend actúa como apoyo visual para la demostración del proyecto.

---

## Alcance de las pruebas

Las pruebas del proyecto se han centrado en validar el funcionamiento principal del sistema.

Se han realizado pruebas sobre:

```text
- Arranque de contenedores.
- Conexión entre API y base de datos.
- Funcionamiento de /health.
- Funcionamiento de /metrics.
- Creación y consulta de reglas.
- Ingesta de eventos.
- Generación automática de alertas.
- Consulta de alertas.
- Filtros de alertas.
- Cambio de estado de alertas.
- Visualización desde frontend.
- Ejecución de tests automatizados.
```

Las pruebas permiten comprobar que el flujo principal funciona de extremo a extremo.

---

## Limitaciones del proyecto

El proyecto presenta limitaciones propias de un MVP académico.

La primera limitación es que los eventos son simulados. El sistema no recibe logs reales de servidores, firewalls, sistemas operativos u otras fuentes externas. Esto simplifica el desarrollo y permite centrarse en la lógica principal, pero reduce el realismo del entorno.

La segunda limitación es que no existe autenticación. Cualquier usuario con acceso a la API podría consultar o modificar información. En una versión real sería necesario incorporar autenticación, autorización y gestión de permisos.

La tercera limitación está en el motor de reglas. Aunque permite condiciones básicas, no implementa una correlación avanzada como la que tendría un SIEM profesional. No analiza secuencias complejas, múltiples fuentes ni patrones distribuidos.

La cuarta limitación es el frontend. La interfaz permite consultar alertas, pero no ofrece gráficos avanzados, paneles dinámicos ni experiencia de usuario propia de una plataforma completa.

La quinta limitación es el entorno de despliegue. El proyecto está preparado para ejecutarse en local mediante Docker Compose, pero no está diseñado para producción.

---

## Decisiones tomadas para controlar el alcance

Durante el desarrollo fue necesario tomar decisiones para evitar que el proyecto creciera demasiado.

Las decisiones principales fueron:

```text
- Mantener el proyecto como MVP.
- Priorizar el backend y la lógica de detección.
- Usar eventos simulados en lugar de logs reales.
- Crear un frontend sencillo.
- No implementar autenticación en esta versión.
- No añadir dashboards avanzados.
- No integrar herramientas SIEM externas.
- Desarrollar componentes propios.
- Documentar las limitaciones como parte del proyecto.
```

Estas decisiones permitieron finalizar una versión funcional y coherente.

---

## Justificación de las limitaciones

Las limitaciones no se consideran fallos del proyecto, sino decisiones necesarias para mantenerlo dentro de un contexto realista.

Desarrollar un SIEM completo habría requerido un alcance muy superior al de este trabajo. Por este motivo, se ha priorizado la construcción de una base funcional que permita demostrar los conceptos principales sin dispersar el desarrollo.

El valor del proyecto está en haber construido un flujo completo y verificable, aunque sea reducido:

```text
ingesta → persistencia → reglas → alertas → consulta
```

Este enfoque permite que el sistema sea comprensible, demostrable y ampliable.

---

## Posibles ampliaciones futuras

A partir de la versión actual, el proyecto podría ampliarse con:

```text
- Autenticación con JWT.
- Gestión de usuarios y roles.
- Integración con logs reales de Linux.
- Recepción de eventos desde agentes externos.
- Normalización de eventos.
- Dashboard con gráficos.
- Notificaciones automáticas.
- Sistema de severidad más avanzado.
- Exportación de informes.
- Integración con herramientas Blue Team.
- Despliegue en servidor o VPS.
- Endurecimiento de seguridad.
```

Estas mejoras permitirían acercar el proyecto a un entorno más realista, manteniendo como base la arquitectura ya desarrollada.

---

## Conclusión

El alcance del proyecto se ha limitado de forma intencionada para construir una versión mínima, funcional y defendible.

El sistema no pretende sustituir a un SIEM real, sino representar sus componentes esenciales mediante una aplicación propia. Esta delimitación ha permitido completar el desarrollo, validar el funcionamiento principal y documentar una base sólida para futuras mejoras.