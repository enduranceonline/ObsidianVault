
## 1️⃣ Objetivo de esta nota

Esta nota resume el funcionamiento técnico general del laboratorio SIEM MVP, explicando cómo se conectan los distintos componentes del proyecto y cómo circula la información desde que se recibe un evento hasta que se genera y consulta una alerta.

El objetivo es tener una visión global del sistema antes de estudiar cada bloque por separado: entorno de desarrollo, base de datos, backend, API de ingesta, motor de reglas, gestión de alertas, frontend y contenedores Docker.

---

## 2️⃣ Visión general del sistema

El proyecto funciona como una aplicación web orientada a simular un laboratorio SIEM básico. Su finalidad es recibir eventos de seguridad, almacenarlos, evaluarlos mediante reglas configuradas y generar alertas cuando se cumplen determinadas condiciones.

A nivel técnico, el sistema se divide en varios componentes:

- Backend desarrollado con FastAPI.
- Base de datos PostgreSQL.
- Modelos definidos con SQLAlchemy.
- Esquemas de validación mediante Pydantic.
- API de ingesta para recibir eventos.
- Motor de reglas para evaluar eventos.
- Gestión de alertas.
- Frontend para visualizar la información.
- Contenedores Docker para levantar el entorno de laboratorio.

---

## 3️⃣ Flujo de datos principal

El flujo general del laboratorio puede resumirse de la siguiente manera:

```text
Evento de seguridad
        ↓
API de ingesta
        ↓
Validación de datos
        ↓
Almacenamiento en PostgreSQL
        ↓
Evaluación por el motor de reglas
        ↓
Generación de alerta
        ↓
Consulta desde API o frontend
````

Este flujo representa el comportamiento principal del sistema. Primero entra un evento, después se valida y almacena, posteriormente se compara con las reglas existentes y, si se cumplen las condiciones definidas, se genera una alerta consultable desde la aplicación.

---

## 4️⃣ Componentes principales

### 🔹 Entorno de desarrollo

Define las herramientas utilizadas para programar, ejecutar y probar el proyecto. Incluye el uso de Visual Studio Code, Python, entorno virtual, dependencias, Docker y comandos básicos de ejecución.

### 🔹 Base de datos

La base de datos PostgreSQL almacena la información persistente del laboratorio. Entre los datos principales se encuentran eventos, reglas y alertas.

### 🔹 Backend FastAPI

El backend actúa como núcleo de la aplicación. Expone los endpoints de la API, recibe peticiones, valida datos, consulta la base de datos y devuelve respuestas en formato JSON.

### 🔹 API de ingesta

La API de ingesta permite introducir eventos de seguridad en el sistema. Es uno de los puntos de entrada principales del laboratorio.

### 🔹 Motor de reglas

El motor de reglas evalúa los eventos recibidos comparándolos con reglas configuradas. Su función es decidir si un evento o conjunto de eventos debe generar una alerta.

### 🔹 Gestión de alertas

La gestión de alertas permite almacenar, consultar y filtrar las alertas generadas por el sistema. Esta parte representa la salida principal del laboratorio desde el punto de vista de un analista SOC.

### 🔹 Frontend

El frontend permite visualizar la información de forma más cómoda, evitando depender únicamente de Swagger, curl o consultas directas.

### 🔹 Contenerización con Docker

Docker permite levantar el laboratorio de forma reproducible mediante servicios independientes, como la API, la base de datos y herramientas auxiliares como Adminer.

---

## 5️⃣ Relación entre carpetas de documentación

Dentro de la carpeta `03_Desarrollo`, cada bloque contiene dos tipos de notas:

```text
00_Estudio-tecnico-...
```

Estas notas explican el código y el funcionamiento interno con mayor profundidad.

```text
01_Entorno-de-desarrollo
02_Base-de-datos
03_Backend-FastAPI
...
```

Estas notas recogen una explicación más formal y ordenada, más cercana a la memoria del proyecto.

La idea es que las notas técnicas sirvan para estudiar, mientras que las notas principales sirvan para documentar el proyecto de forma más limpia.

---

## 6️⃣ Estructura real del repositorio

El repositorio del laboratorio SIEM MVP se organiza en varios bloques principales:

```text
siem-lab/
├── backend/
├── frontend/
├── docker/
├── .github/
├── .env
├── .env.example
├── .gitignore
└── README.md
```

El directorio `backend/` contiene la API desarrollada con FastAPI, los modelos de base de datos, los esquemas de validación, las rutas de la API, las migraciones de Alembic y los tests.

El directorio `frontend/` contiene la interfaz web del laboratorio, formada por archivos HTML, JavaScript y CSS.

El directorio `docker/` contiene la configuración de Docker Compose, utilizada para levantar los servicios del laboratorio de forma reproducible.

El directorio `.github/` contiene el workflow de integración continua, utilizado para ejecutar comprobaciones automáticas del proyecto.

Los archivos `.env` y `.env.example` permiten configurar variables de entorno, como credenciales, nombres de servicios o parámetros de conexión.

El archivo `README.md` actúa como documentación principal del repositorio, incluyendo explicación general, comandos de uso y resumen técnico.