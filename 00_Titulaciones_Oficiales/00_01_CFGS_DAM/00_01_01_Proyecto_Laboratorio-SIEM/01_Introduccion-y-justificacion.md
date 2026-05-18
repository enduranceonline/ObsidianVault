## Introducción

El proyecto **SIEM Lab MVP** nace con el objetivo de desarrollar una aplicación orientada a la monitorización básica de eventos de seguridad y la generación automática de alertas. La idea principal consiste en construir una versión mínima funcional de un sistema inspirado en un SIEM, adaptada al contexto académico del ciclo de Desarrollo de Aplicaciones Multiplataforma.

Un SIEM, por sus siglas en inglés *Security Information and Event Management*, es una solución utilizada en ciberseguridad para recopilar, almacenar, analizar y correlacionar eventos procedentes de diferentes sistemas. Su finalidad es facilitar la detección de comportamientos sospechosos, incidentes de seguridad o actividades anómalas dentro de una infraestructura tecnológica.

En este proyecto no se pretende desarrollar un SIEM profesional completo, ya que ese tipo de herramientas requieren una arquitectura mucho más compleja, múltiples fuentes de datos, mecanismos avanzados de correlación, normalización de logs, gestión de usuarios, dashboards avanzados, integración con agentes y capacidades de respuesta ante incidentes.

El objetivo es más concreto: desarrollar un **laboratorio SIEM básico**, funcional y reproducible, que permita comprender y demostrar el flujo esencial de este tipo de sistemas:

```text
Evento o log simulado
        ↓
Ingesta mediante API
        ↓
Almacenamiento en base de datos
        ↓
Evaluación mediante reglas
        ↓
Generación de alertas
        ↓
Consulta y gestión básica
````

Este planteamiento permite unir dos áreas de interés: el desarrollo de aplicaciones y la ciberseguridad defensiva. Por un lado, el proyecto requiere diseñar y desarrollar una aplicación backend con una API REST, modelos de datos, persistencia, pruebas y documentación. Por otro lado, permite trabajar conceptos propios del ámbito Blue Team, como la ingesta de eventos, la detección mediante reglas y la gestión de alertas.

---

## Contexto del proyecto

El proyecto se sitúa dentro del ámbito del desarrollo de aplicaciones, pero está orientado a un caso de uso relacionado con la ciberseguridad. Esta decisión permite que el trabajo tenga una aplicación práctica y conecte con un entorno técnico realista.

En lugar de crear una aplicación genérica, se ha optado por desarrollar una herramienta que simula parte del comportamiento de un sistema utilizado en entornos SOC y Blue Team. Esto permite que el proyecto tenga una finalidad técnica clara y que las decisiones de diseño estén relacionadas con un flujo real de tratamiento de información de seguridad.

El sistema desarrollado permite recibir eventos simulados, almacenarlos, evaluarlos mediante reglas activas y generar alertas cuando se detectan coincidencias. Estas alertas pueden consultarse desde la API y desde un frontend básico.

De esta forma, el proyecto no se limita a mostrar datos estáticos, sino que implementa un flujo completo de procesamiento:

```text
entrada de datos → procesamiento → persistencia → lógica de detección → salida consultable
```

---

## Justificación de la temática elegida

La elección de un laboratorio SIEM se justifica por varios motivos.

En primer lugar, la ciberseguridad es un ámbito en crecimiento y cada vez más relacionado con el desarrollo de software. Muchas herramientas de seguridad modernas se apoyan en APIs, bases de datos, servicios distribuidos, automatización, dashboards y procesamiento de eventos. Por este motivo, desarrollar una aplicación inspirada en un SIEM permite trabajar competencias propias del desarrollo de aplicaciones dentro de un contexto técnico actual.

En segundo lugar, el proyecto permite introducir conceptos del ámbito Blue Team de una forma práctica. Un perfil defensivo en ciberseguridad necesita comprender cómo se reciben los eventos, cómo se analizan, cómo se generan alertas y cómo se prioriza la información relevante. Aunque este proyecto sea una versión simplificada, reproduce el flujo básico de trabajo sobre el que se apoyan muchas herramientas reales.

En tercer lugar, la temática permite construir una aplicación propia y no depender únicamente de herramientas externas. Este punto es especialmente importante porque el objetivo académico no es instalar un producto ya existente, sino desarrollar una solución software. Por ello, se ha decidido implementar una API propia, un modelo de datos propio, un motor de reglas propio y una interfaz de consulta básica.

Finalmente, la elección de esta temática permite crear un proyecto ampliable. Aunque el resultado final sea un MVP, su estructura puede servir como base para futuras mejoras, como integración con fuentes reales de logs, autenticación, dashboards más completos, normalización de eventos o despliegue en un entorno más realista.

---

## Relación con el ciclo de Desarrollo de Aplicaciones Multiplataforma

Aunque el proyecto está orientado a la ciberseguridad, su desarrollo está directamente relacionado con los contenidos y competencias del ciclo de Desarrollo de Aplicaciones Multiplataforma.

El proyecto incluye elementos propios del desarrollo de software:

```text
- Análisis de requisitos.
- Diseño de arquitectura.
- Diseño de modelo de datos.
- Desarrollo de backend.
- Creación de una API REST.
- Persistencia en base de datos.
- Validación de datos.
- Separación de responsabilidades.
- Desarrollo de frontend básico.
- Pruebas funcionales.
- Pruebas automatizadas.
- Documentación técnica.
- Uso de control de versiones.
- Despliegue mediante contenedores.
```

El uso de **FastAPI** permite trabajar el desarrollo backend mediante Python y crear endpoints documentados. **PostgreSQL** permite aplicar conceptos de bases de datos relacionales. **SQLAlchemy** permite trabajar con modelos desde código. **Docker Compose** permite reproducir el entorno de ejecución. **HTML, CSS y JavaScript** permiten desarrollar una interfaz básica para consumir la API.

Por tanto, aunque la temática sea de ciberseguridad, el núcleo del proyecto sigue siendo el desarrollo de una aplicación funcional.

---

## Necesidad de delimitar el alcance

Uno de los puntos más importantes del proyecto fue definir correctamente su alcance. El concepto de SIEM puede abarcar muchas funcionalidades, y si no se establecen límites claros, el proyecto puede crecer demasiado.

Un SIEM real puede incluir:

```text
- Recopilación de logs desde múltiples fuentes.
- Agentes instalados en sistemas externos.
- Normalización de eventos.
- Correlación avanzada.
- Dashboards en tiempo real.
- Gestión de usuarios y permisos.
- Sistemas de notificación.
- Integración con herramientas externas.
- Retención histórica de eventos.
- Informes automáticos.
- Respuesta ante incidentes.
```

Incluir todas estas funcionalidades habría sido poco realista para el alcance académico del proyecto. Por ello, se decidió limitar el desarrollo a un MVP centrado en el flujo esencial:

```text
evento → ingesta → almacenamiento → evaluación → alerta → consulta
```

Esta decisión permitió mantener el proyecto dentro de unos límites asumibles y evitar que la complejidad impidiera finalizar una versión funcional. En lugar de intentar desarrollar muchas funcionalidades de forma superficial, se priorizó construir una base reducida pero coherente y verificable.

---

## Justificación del enfoque MVP

El enfoque MVP fue una decisión clave para el desarrollo del proyecto. El objetivo no era crear una herramienta completa, sino una primera versión funcional que demostrara los conceptos principales.

El proyecto se centró en las siguientes funcionalidades:

```text
- Recibir eventos simulados mediante API.
- Guardar los eventos en PostgreSQL.
- Crear y consultar reglas de detección.
- Evaluar eventos mediante reglas activas.
- Generar alertas automáticamente.
- Consultar alertas desde la API.
- Mostrar alertas desde un frontend básico.
- Cambiar el estado de una alerta.
- Consultar métricas básicas del sistema.
- Validar el sistema mediante pruebas.
```

Este enfoque permitió obtener un resultado cerrado y demostrable. Además, facilitó la toma de decisiones durante el desarrollo, ya que cada funcionalidad se valoró en función de si aportaba valor directo al flujo principal del sistema.

Las funcionalidades que no eran imprescindibles se dejaron como futuras mejoras. Esto incluye autenticación, dashboards avanzados, integración con fuentes reales de logs, notificaciones, roles de usuario o correlación avanzada.

---

## Justificación de desarrollar una aplicación propia

Durante el planteamiento del proyecto existía el riesgo de convertir el trabajo en una simple instalación de herramientas de ciberseguridad. Aunque herramientas como SIEMs reales, gestores de logs o plataformas de monitorización pueden ser útiles para aprender, basar el proyecto únicamente en ellas habría reducido la parte de desarrollo propio.

Por este motivo, se tomó la decisión de construir una aplicación desde cero, manteniendo la inspiración en el funcionamiento de un SIEM, pero desarrollando los componentes principales de forma propia:

```text
- API de ingesta.
- Modelos de eventos, reglas y alertas.
- Motor de reglas.
- Endpoints de consulta.
- Gestión básica de estados.
- Frontend de visualización.
- Documentación de uso.
- Pruebas de validación.
```

Esta decisión permitió que el proyecto tuviera mayor valor académico, ya que demuestra capacidad para analizar un problema, diseñar una solución, implementarla, probarla y documentarla.

---

## Justificación de las herramientas utilizadas

La elección de herramientas se realizó buscando un equilibrio entre aprendizaje, funcionalidad y reproducibilidad.

**Python** se utilizó como lenguaje principal por su claridad, su amplia adopción y su presencia en ámbitos de automatización, backend y ciberseguridad.

**FastAPI** se eligió para desarrollar la API REST porque permite crear endpoints de forma rápida, clara y con documentación automática mediante Swagger.

**PostgreSQL** se utilizó como base de datos relacional porque permite almacenar de forma estructurada eventos, reglas y alertas, manteniendo relaciones entre entidades.

**SQLAlchemy** permitió trabajar con modelos de datos desde Python y separar la lógica de la aplicación de las consultas directas a la base de datos.

**Alembic** se incorporó para gestionar migraciones y mantener controlado el esquema de la base de datos.

**Docker Compose** permitió ejecutar la API, la base de datos y Adminer en servicios separados, facilitando la reproducción del entorno.

**Adminer** se utilizó como herramienta ligera para visualizar la base de datos y comprobar que los datos se almacenaban correctamente.

**HTML, CSS y JavaScript** se utilizaron para construir un frontend básico sin añadir complejidad innecesaria con frameworks más avanzados.

**Pytest** se utilizó para validar parte del comportamiento del backend mediante pruebas automatizadas.

**Git y GitHub** se utilizaron para llevar control de versiones, documentar el avance y disponer de un repositorio final del proyecto.

---

## Problemas iniciales que justificaron ajustes en el proyecto

Durante el desarrollo aparecieron varios problemas que obligaron a ajustar decisiones iniciales.

Uno de los primeros problemas fue el entorno de virtualización. Inicialmente se planteó trabajar con VMware, pero surgieron problemas de estabilidad y compatibilidad. Esto llevó a migrar el entorno a VirtualBox, donde finalmente se pudo trabajar de forma más estable.

También aparecieron problemas con los módulos de VirtualBox en Kali Linux, así como una incidencia de pantalla negra al arrancar la máquina virtual. Estos problemas obligaron a revisar la configuración del entorno y reforzaron la importancia de contar con una base estable antes de avanzar con el desarrollo de la aplicación.

Otro problema importante fue la definición del alcance. En distintos momentos surgieron ideas que podían ampliar demasiado el proyecto, como añadir más funcionalidades de detección, dashboards avanzados o integraciones externas. Para evitar que el proyecto perdiera foco, se decidió mantener una versión MVP.

También fue necesario ajustar el comportamiento del motor de reglas, especialmente en lo relacionado con `group_key`, `threshold`, `throttle` y anti-duplicado. Estas decisiones permitieron simplificar el sistema y hacerlo más previsible.

Estos problemas no se consideran fallos aislados, sino parte del proceso de desarrollo. Cada uno de ellos ayudó a tomar decisiones más realistas y a mejorar la calidad del resultado final.

---

## Valor del proyecto

El valor principal del proyecto está en que permite demostrar un flujo completo de una aplicación orientada a seguridad:

```text
recibir datos → almacenarlos → procesarlos → generar resultados → consultarlos
```

Aunque el sistema sea limitado, incluye los elementos esenciales de una aplicación real:

```text
- Backend.
- Base de datos.
- API REST.
- Lógica de negocio.
- Frontend.
- Contenedores.
- Documentación.
- Pruebas.
```

Además, el proyecto tiene valor formativo porque obliga a trabajar con problemas habituales en desarrollo: configuración de entorno, persistencia, diseño de modelos, validación de endpoints, documentación, pruebas y control del alcance.

Desde el punto de vista de la ciberseguridad, permite introducir conceptos propios de monitorización y detección de eventos, sirviendo como base para futuros aprendizajes relacionados con SOC, Blue Team, SIEMs reales o automatización de seguridad.

---

## Conclusión de la justificación

El desarrollo de **SIEM Lab MVP** está justificado por su valor técnico, académico y formativo.

Desde el punto de vista académico, permite demostrar competencias propias del desarrollo de aplicaciones: diseño, programación, base de datos, API, frontend, pruebas y documentación.

Desde el punto de vista técnico, permite construir una aplicación modular, reproducible y ampliable.

Desde el punto de vista de la ciberseguridad, permite comprender de forma práctica el funcionamiento básico de un sistema de ingesta, detección y generación de alertas.

La decisión de limitar el proyecto a un MVP ha sido fundamental para obtener un resultado realista y funcional. Gracias a esta delimitación, el proyecto no intenta competir con un SIEM real, sino representar de forma clara sus componentes esenciales mediante una aplicación propia y defendible.