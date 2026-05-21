## Introducción

Este anexo recopila las referencias técnicas utilizadas o relacionadas con el desarrollo del **SIEM Lab MVP**.

Las referencias se agrupan por tecnología y por área del proyecto para facilitar su consulta. No todas se han utilizado como guía directa durante el desarrollo, pero sí representan documentación relevante para entender las herramientas empleadas.

---

## Python

Python se utilizó como lenguaje principal del backend.

Referencia principal:

```text
Documentación oficial de Python
https://docs.python.org/3/
````

Uso dentro del proyecto:

```text
- Desarrollo del backend.
- Implementación de lógica de negocio.
- Definición del motor de reglas.
- Ejecución de scripts auxiliares.
- Pruebas automatizadas.
```

---

## FastAPI

FastAPI se utilizó para desarrollar la API REST del sistema.

Referencia principal:

```text
Documentación oficial de FastAPI
https://fastapi.tiangolo.com/
```

Uso dentro del proyecto:

```text
- Creación de endpoints.
- Validación de peticiones.
- Documentación automática con Swagger.
- Gestión de rutas.
- Respuestas JSON.
```

Endpoints relacionados:

```text
GET /health
GET /metrics
POST /ingest
GET /rules
GET /alerts/ui
PATCH /alerts/{alert_id}
```

---

## Uvicorn

Uvicorn se utilizó como servidor ASGI para ejecutar la aplicación FastAPI.

Referencia principal:

```text
Documentación oficial de Uvicorn
https://www.uvicorn.org/
```

Uso dentro del proyecto:

```text
- Ejecución del backend.
- Servicio HTTP de la API.
- Integración con FastAPI.
```

---

## PostgreSQL

PostgreSQL se utilizó como base de datos relacional del proyecto.

Referencia principal:

```text
Documentación oficial de PostgreSQL
https://www.postgresql.org/docs/
```

Uso dentro del proyecto:

```text
- Persistencia de eventos.
- Persistencia de reglas.
- Persistencia de alertas.
- Relación entre entidades.
```

Tablas principales:

```text
events
rules
alerts
alembic_version
```

---

## SQLAlchemy

SQLAlchemy se utilizó para trabajar con la base de datos desde Python mediante modelos.

Referencia principal:

```text
Documentación oficial de SQLAlchemy
https://docs.sqlalchemy.org/
```

Uso dentro del proyecto:

```text
- Definición de modelos.
- Comunicación entre backend y PostgreSQL.
- Consultas desde la API.
- Inserción y actualización de registros.
```

Modelos principales:

```text
Event
Rule
Alert
```

---

## Alembic

Alembic se utilizó para gestionar migraciones de base de datos.

Referencia principal:

```text
Documentación oficial de Alembic
https://alembic.sqlalchemy.org/
```

Uso dentro del proyecto:

```text
- Creación del esquema de base de datos.
- Control de cambios en tablas.
- Aplicación de migraciones.
```

Comando utilizado:

```bash
docker compose exec api alembic upgrade head
```

---

## Docker

Docker se utilizó para ejecutar los servicios principales del proyecto en contenedores.

Referencia principal:

```text
Documentación oficial de Docker
https://docs.docker.com/
```

Uso dentro del proyecto:

```text
- Ejecución de la API.
- Ejecución de PostgreSQL.
- Ejecución de Adminer.
- Aislamiento de servicios.
- Reproducibilidad del entorno.
```

---

## Docker Compose

Docker Compose se utilizó para definir y levantar varios servicios de forma coordinada.

Referencia principal:

```text
Documentación oficial de Docker Compose
https://docs.docker.com/compose/
```

Uso dentro del proyecto:

```text
- Definición de servicios.
- Red interna entre contenedores.
- Variables de entorno.
- Levantamiento del laboratorio.
```

Servicios definidos:

```text
siem-api
siem-db
siem-adminer
```

Comando principal:

```bash
docker compose up -d --build
```

---

## Adminer

Adminer se utilizó como herramienta web para consultar PostgreSQL.

Referencia principal:

```text
Sitio oficial de Adminer
https://www.adminer.org/
```

Uso dentro del proyecto:

```text
- Revisión visual de tablas.
- Comprobación de eventos almacenados.
- Comprobación de reglas.
- Comprobación de alertas.
```

URL local:

```text
http://127.0.0.1:8080
```

---

## Pytest

Pytest se utilizó para ejecutar pruebas automatizadas del backend.

Referencia principal:

```text
Documentación oficial de Pytest
https://docs.pytest.org/
```

Uso dentro del proyecto:

```text
- Ejecución de pruebas automatizadas.
- Validación parcial del backend.
- Comprobación de comportamiento esperado.
```

Comando utilizado:

```bash
docker compose exec api python -m pytest
```

Resultado validado:

```text
4 passed in 1.00s
```

---

## HTML

HTML se utilizó para estructurar la interfaz web del frontend.

Referencia principal:

```text
MDN Web Docs - HTML
https://developer.mozilla.org/en-US/docs/Web/HTML
```

Uso dentro del proyecto:

```text
- Estructura de la página principal.
- Vista de alertas.
- Vista de detalle de alerta.
```

---

## CSS

CSS se utilizó para aplicar estilos visuales al frontend.

Referencia principal:

```text
MDN Web Docs - CSS
https://developer.mozilla.org/en-US/docs/Web/CSS
```

Uso dentro del proyecto:

```text
- Estilos de la interfaz.
- Presentación de alertas.
- Organización visual del frontend.
```

---

## JavaScript

JavaScript se utilizó para consumir la API desde el frontend.

Referencia principal:

```text
MDN Web Docs - JavaScript
https://developer.mozilla.org/en-US/docs/Web/JavaScript
```

Uso dentro del proyecto:

```text
- Peticiones HTTP a la API.
- Consulta de /alerts/ui.
- Actualización de datos en pantalla.
- Gestión básica de interacción.
```

---

## Fetch API

La Fetch API se utiliza en JavaScript para realizar peticiones HTTP desde el navegador.

Referencia principal:

```text
MDN Web Docs - Fetch API
https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
```

Uso dentro del proyecto:

```text
- Obtener alertas desde la API.
- Consultar información enriquecida.
- Mostrar datos en el frontend.
```

---

## Swagger / OpenAPI

FastAPI genera documentación interactiva mediante Swagger UI a partir del esquema OpenAPI.

Referencias principales:

```text
OpenAPI Specification
https://spec.openapis.org/oas/latest.html

Swagger
https://swagger.io/
```

Uso dentro del proyecto:

```text
- Documentación automática de endpoints.
- Pruebas manuales desde navegador.
- Revisión de rutas disponibles.
```

URL local:

```text
http://127.0.0.1:8000/docs
```

---

## Git

Git se utilizó como sistema de control de versiones.

Referencia principal:

```text
Documentación oficial de Git
https://git-scm.com/doc
```

Uso dentro del proyecto:

```text
- Control de cambios.
- Registro de evolución del código.
- Preparación de entrega.
```

---

## GitHub

GitHub se utilizó como repositorio remoto del proyecto.

Referencia principal:

```text
Documentación de GitHub
https://docs.github.com/
```

Uso dentro del proyecto:

```text
- Almacenamiento remoto del repositorio.
- Consulta del código final.
- Revisión del README.
- Entrega del proyecto.
```

---

## Obsidian

Obsidian se utilizó para organizar las notas técnicas del proyecto.

Referencia principal:

```text
Ayuda oficial de Obsidian
https://help.obsidian.md/
```

Uso dentro del proyecto:

```text
- Organización de la memoria.
- Redacción de notas.
- Relación entre apartados.
- Preparación de contenido para la documentación final.
```

---

## Excalidraw

Excalidraw se utilizó para crear diagramas del proyecto.

Referencia principal:

```text
Sitio oficial de Excalidraw
https://excalidraw.com/
```

Uso dentro del proyecto:

```text
- Diagrama ERD.
- Diagrama de flujo de datos.
- Diagrama de topología del laboratorio.
```

Diagramas previstos:

```text
01_ERD_Laboratorio_SIEM.excalidraw
02_Flujo_Datos_SIEM.excalidraw
03_Topologia_Lab.excalidraw
```

---

## Conceptos SIEM

El proyecto se inspira en conceptos propios de sistemas SIEM.

Conceptos utilizados:

```text
- Ingesta de eventos.
- Logs.
- Reglas de detección.
- Alertas.
- Severidad.
- Correlación básica.
- Reducción de ruido.
- Gestión de estados.
```

El objetivo no ha sido replicar una herramienta SIEM real, sino representar de forma simplificada su flujo principal.

---

## Conceptos Blue Team

El enfoque Blue Team se relaciona con la defensa, monitorización y detección de posibles incidentes.

Conceptos aplicados en el proyecto:

```text
- Monitorización defensiva.
- Revisión de alertas.
- Detección mediante reglas.
- Priorización por severidad.
- Consulta y filtrado de alertas.
```

El proyecto utiliza estos conceptos como contexto funcional, aunque su núcleo sigue siendo el desarrollo de una aplicación.

---

## Conclusión

Las referencias anteriores cubren las tecnologías y conceptos principales utilizados en el SIEM Lab MVP.

El proyecto combina desarrollo backend, base de datos, contenerización, frontend básico, pruebas y conceptos de ciberseguridad defensiva.

Estas referencias sirven como apoyo técnico para comprender las herramientas empleadas y justificar las decisiones tomadas durante el desarrollo.