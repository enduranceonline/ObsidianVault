## Introducción

La elección de tecnologías se realizó buscando un equilibrio entre funcionalidad, aprendizaje, simplicidad y reproducibilidad.

El proyecto necesitaba cubrir varios aspectos:

```text
- Desarrollo de una API.
- Persistencia en base de datos.
- Gestión de modelos y migraciones.
- Ejecución de servicios en contenedores.
- Consulta visual de la base de datos.
- Interfaz web sencilla.
- Pruebas automatizadas.
- Control de versiones.
- Documentación.
````

Por este motivo se eligió un stack basado en **Python, FastAPI, PostgreSQL, Docker Compose, Adminer, HTML, CSS, JavaScript, Pytest y GitHub**.

---

## Python

Se eligió **Python** como lenguaje principal del backend por varios motivos:

```text
- Sintaxis clara.
- Buena integración con frameworks web.
- Amplio uso en automatización y ciberseguridad.
- Ecosistema maduro de librerías.
- Facilidad para desarrollar prototipos funcionales.
```

Python encaja bien con un proyecto de laboratorio, ya que permite implementar lógica de negocio de forma rápida sin añadir una complejidad excesiva.

En este proyecto se ha utilizado para desarrollar la API, definir modelos, implementar el motor de reglas y ejecutar pruebas.

---

## FastAPI

Se eligió **FastAPI** como framework para desarrollar la API REST.

Las razones principales fueron:

```text
- Permite crear endpoints de forma clara.
- Genera documentación automática con Swagger.
- Facilita la validación de datos.
- Tiene buen rendimiento.
- Se integra correctamente con SQLAlchemy.
- Es adecuado para aplicaciones backend modernas.
```

Swagger fue especialmente útil durante el desarrollo, ya que permitió probar los endpoints directamente desde el navegador sin depender desde el inicio del frontend.

FastAPI se utilizó para exponer endpoints como:

```text
GET /health
GET /metrics
POST /ingest
GET /rules
GET /alerts
PATCH /alerts/{alert_id}
GET /alerts/ui
```

---

## Uvicorn

**Uvicorn** se utilizó como servidor ASGI para ejecutar la aplicación FastAPI.

Su función principal es levantar el backend y permitir que la API reciba peticiones HTTP.

Dentro del proyecto, Uvicorn se ejecuta en el contenedor `siem-api`, sirviendo la aplicación definida en FastAPI.

---

## PostgreSQL

Se eligió **PostgreSQL** como sistema gestor de base de datos.

El proyecto necesitaba almacenar información estructurada y relacionada:

```text
- Eventos recibidos.
- Reglas de detección.
- Alertas generadas.
```

PostgreSQL era una opción adecuada porque permite trabajar con tablas, relaciones y consultas de forma robusta.

La elección de una base de datos relacional encaja con el modelo principal del proyecto:

```text
events → alerts ← rules
```

Cada alerta puede relacionarse con el evento que la originó y con la regla que se activó.

---

## SQLAlchemy

Se utilizó **SQLAlchemy** para trabajar con la base de datos desde Python.

Su uso permitió definir modelos de datos en código y evitar trabajar únicamente con SQL manual.

En el proyecto, SQLAlchemy se utilizó para representar entidades como:

```text
- Event
- Rule
- Alert
```

Esto facilita mantener una separación entre la lógica de la aplicación y la estructura de la base de datos.

---

## Alembic

Se incorporó **Alembic** para gestionar migraciones de base de datos.

Su función es mantener controlados los cambios en el esquema de la base de datos a medida que evoluciona el proyecto.

Esto resulta útil cuando se añaden o modifican tablas, columnas o relaciones.

En el proyecto, Alembic permitió preparar la estructura necesaria para trabajar con las tablas principales:

```text
events
rules
alerts
```

---

## Docker Compose

Se eligió **Docker Compose** para ejecutar los servicios principales del proyecto de forma coordinada.

El entorno se organiza en tres contenedores:

```text
siem-api      → Backend FastAPI
siem-db       → Base de datos PostgreSQL
siem-adminer  → Interfaz de consulta para PostgreSQL
```

Docker Compose permitió:

```text
- Levantar varios servicios con un solo comando.
- Separar la API de la base de datos.
- Mantener un entorno reproducible.
- Reducir dependencias del sistema anfitrión.
- Ejecutar pruebas dentro del contenedor adecuado.
```

Esta decisión fue especialmente importante para evitar diferencias entre entornos locales y facilitar la reproducción del proyecto.

---

## Adminer

Se utilizó **Adminer** como herramienta auxiliar para consultar la base de datos desde el navegador.

Adminer permitió comprobar visualmente:

```text
- Las tablas creadas.
- Los eventos almacenados.
- Las reglas existentes.
- Las alertas generadas.
- El contenido real de PostgreSQL.
```

Aunque no forma parte del flujo principal del SIEM, fue útil para validar la persistencia y diagnosticar problemas durante el desarrollo.

---

## HTML, CSS y JavaScript

El frontend se desarrolló con **HTML, CSS y JavaScript** sin frameworks adicionales.

La decisión se tomó para mantener la interfaz sencilla y evitar que el frontend añadiera una complejidad innecesaria.

El objetivo del frontend era demostrar visualmente que las alertas generadas por el backend podían consultarse desde navegador.

Sus funciones principales son:

```text
- Mostrar alertas.
- Aplicar filtros básicos.
- Actualizar datos.
- Consultar información enriquecida.
- Acceder al detalle de una alerta.
```

El frontend consume principalmente los endpoints `/alerts/ui` y `/alerts/{alert_id}/ui`.

---

## Pytest

Se utilizó **Pytest** para ejecutar pruebas automatizadas.

Las pruebas permitieron validar parte del comportamiento del backend y comprobar que determinadas funcionalidades seguían funcionando correctamente.

Durante el desarrollo surgió un problema al intentar ejecutar `pytest` desde el entorno local, ya que no estaba instalado. La solución fue ejecutar las pruebas dentro del contenedor de la API:

```bash
docker compose exec api python -m pytest
```

Esto confirmó la utilidad de Docker como entorno reproducible de pruebas.

---

## VirtualBox

El proyecto se desarrolló dentro de una máquina virtual gestionada con **VirtualBox**.

Inicialmente se intentó trabajar con VMware, pero aparecieron problemas de estabilidad y compatibilidad. Por este motivo, se migró el entorno a VirtualBox.

VirtualBox permitió disponer de un entorno aislado para ejecutar:

```text
- Sistema Linux de laboratorio.
- Docker.
- API.
- Base de datos.
- Herramientas de prueba.
```

Esta decisión ayudó a separar el entorno del proyecto del sistema principal.

---

## Git y GitHub

Se utilizó **Git** para el control de versiones y **GitHub** como repositorio remoto.

Esto permitió:

```text
- Registrar la evolución del proyecto.
- Guardar cambios de forma controlada.
- Documentar el estado final.
- Mantener una copia remota del código.
- Facilitar la entrega del proyecto.
```

El README del repositorio se actualizó al final del desarrollo para incluir instrucciones de instalación, reproducción, endpoints, pruebas, limitaciones y futuras mejoras.

---

## Obsidian y Excalidraw

Para la organización de la memoria y la documentación se utilizó **Obsidian**.

Obsidian permitió estructurar las notas del proyecto de forma modular, separando apartados como:

```text
- Resumen.
- Objetivos.
- Alcance.
- Arquitectura.
- Desarrollo.
- Pruebas.
- Problemas encontrados.
- Conclusiones.
```

También se utilizó **Excalidraw** para crear diagramas relacionados con la arquitectura, el flujo de datos y el modelo de datos.

Estos diagramas sirven como apoyo visual para explicar el funcionamiento del sistema.

---

## Criterios de elección

Las tecnologías se eligieron siguiendo estos criterios:

```text
- Que permitieran desarrollar una aplicación propia.
- Que fueran adecuadas para un MVP.
- Que facilitaran la reproducción del entorno.
- Que no añadieran complejidad innecesaria.
- Que permitieran validar el sistema con pruebas.
- Que fueran coherentes con el contexto académico.
- Que tuvieran relación con entornos reales de desarrollo.
```

El stack final permitió cubrir las necesidades del proyecto sin depender de herramientas demasiado complejas.

---

## Relación entre tecnologías y componentes

La relación entre tecnologías y partes del sistema puede resumirse así:

```text
FastAPI        → API y lógica principal
Uvicorn        → Servidor de la aplicación
PostgreSQL     → Persistencia de datos
SQLAlchemy     → Modelos y acceso a base de datos
Alembic        → Migraciones
Docker Compose → Ejecución de servicios
Adminer        → Consulta visual de PostgreSQL
HTML/CSS/JS    → Frontend
Pytest         → Pruebas automatizadas
VirtualBox     → Entorno de laboratorio
Git/GitHub     → Control de versiones y repositorio
Obsidian       → Organización de documentación
Excalidraw     → Diagramas
```

---

## Conclusión

El conjunto de tecnologías elegido permitió desarrollar un proyecto funcional, modular y reproducible.

La elección de FastAPI, PostgreSQL y Docker Compose fue clave para construir el núcleo del sistema. Adminer, Swagger y Pytest facilitaron la validación. HTML, CSS y JavaScript permitieron crear una interfaz sencilla sin desviar el foco del backend.

En conjunto, el stack utilizado permitió cumplir los objetivos del MVP y mantener el proyecto dentro de un alcance realista.