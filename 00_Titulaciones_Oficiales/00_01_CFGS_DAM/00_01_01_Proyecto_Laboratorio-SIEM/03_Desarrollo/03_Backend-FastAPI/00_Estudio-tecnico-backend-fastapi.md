#python #api #uvicorn
## 1️⃣ Objetivo de la nota

Esta nota resume el papel del backend FastAPI dentro del laboratorio SIEM MVP.

El objetivo es entender cómo se organiza la API, qué archivos intervienen en su arranque, cómo se cargan las rutas y cómo el backend actúa como núcleo de comunicación entre el frontend, la base de datos PostgreSQL y la lógica del laboratorio.

El análisis detallado línea por línea se desarrolla en la carpeta:

```text
04_Analisis-tecnico-del-backend/
````

---

## 2️⃣ Archivos relacionados

Los archivos principales relacionados con el backend FastAPI son:

```text
backend/app/main.py
backend/app/api/routes/health.py
backend/app/api/routes/info.py
backend/app/api/routes/metrics.py
backend/app/api/routes/__init__.py
```

También se relaciona indirectamente con otros módulos del proyecto:

```text
backend/app/api/routes/ingest.py
backend/app/api/routes/events.py
backend/app/api/routes/rules.py
backend/app/api/routes/alerts.py
backend/app/db/
backend/app/models/
backend/app/schemas/
```

---

## 3️⃣ Papel del backend dentro del proyecto

El backend FastAPI es el núcleo del laboratorio SIEM MVP.

Su función principal es exponer una API HTTP que permite interactuar con el sistema. A través de esta API, el laboratorio puede recibir eventos de seguridad, consultar eventos almacenados, gestionar reglas, generar alertas, consultar métricas y proporcionar información básica del estado del sistema.

A nivel funcional, el backend se sitúa entre el usuario o frontend y la base de datos PostgreSQL:

```text
Usuario / Frontend / Swagger / curl
        ↓
Backend FastAPI
        ↓
PostgreSQL
```

FastAPI recibe las peticiones HTTP, valida los datos mediante esquemas Pydantic, utiliza SQLAlchemy para comunicarse con la base de datos y devuelve respuestas en formato JSON.

---

## 4️⃣ Relación con Docker y Uvicorn

El backend no se ejecuta directamente como un script Python normal. Se arranca mediante Uvicorn dentro del contenedor `siem-api`.

En el archivo `docker/compose.yml`, el servicio `api` ejecuta:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Esta instrucción indica que Uvicorn debe buscar la aplicación FastAPI en:

```text
backend/app/main.py
```

Concretamente, interpreta:

```text
app.main:app
```

de la siguiente forma:

```text
app       → carpeta o paquete Python backend/app/
main      → archivo main.py
app       → variable app definida dentro de main.py
```

Por tanto, el archivo `main.py` es el punto de entrada real de la API.

---

## 5️⃣ Flujo de arranque del backend

El arranque del backend sigue este flujo:

```text
1. Docker Compose levanta el servicio api.
2. El contenedor usa la imagen construida desde backend/Dockerfile.
3. Se instalan las dependencias desde backend/requirements.txt.
4. Docker ejecuta Uvicorn.
5. Uvicorn carga backend/app/main.py.
6. FastAPI crea la aplicación principal.
7. Se registran los routers de la API.
8. La documentación Swagger queda disponible en /docs.
9. La API queda escuchando en el puerto 8000.
```

Este flujo conecta la contenerización del proyecto con el código Python real del backend.

---

## 6️⃣ Estructura de rutas del backend

El backend organiza sus endpoints en archivos separados dentro de:

```text
backend/app/api/routes/
```

La estructura principal es:

```text
routes/
├── health.py
├── info.py
├── metrics.py
├── ingest.py
├── events.py
├── rules.py
└── alerts.py
```

Cada archivo agrupa rutas relacionadas con una parte concreta del laboratorio:

```text
health.py  → comprobación de estado de la API
info.py    → información general de versión o entorno
metrics.py → métricas agregadas del sistema
ingest.py  → entrada de eventos de seguridad
events.py  → consulta de eventos almacenados
rules.py   → gestión de reglas de detección
alerts.py  → gestión y consulta de alertas
```

Esta separación evita tener todos los endpoints mezclados en un único archivo y facilita el mantenimiento del proyecto.

---

## 7️⃣ Papel de FastAPI

FastAPI permite crear una API REST usando Python.

En este proyecto, FastAPI se encarga de:

```text
- Crear la aplicación principal.
- Registrar rutas HTTP.
- Generar documentación automática en /docs.
- Validar datos de entrada con Pydantic.
- Devolver respuestas JSON.
- Gestionar dependencias como sesiones de base de datos.
```

Un endpoint típico de FastAPI se define mediante decoradores como:

```python
@app.get("/health")
```

o mediante routers:

```python
router = APIRouter()
```

Después, esos routers se incorporan a la aplicación principal usando una instrucción similar a:

```python
app.include_router(router)
```

---

## 8️⃣ Papel de los routers

Los routers permiten dividir la API en módulos.

En lugar de definir todos los endpoints directamente en `main.py`, cada grupo de rutas se define en su propio archivo.

La idea general es:

```text
main.py
   ↓
carga routers
   ↓
routes/health.py
routes/info.py
routes/ingest.py
routes/events.py
routes/rules.py
routes/alerts.py
routes/metrics.py
```

Esto mejora la organización del backend porque cada archivo tiene una responsabilidad clara.

Por ejemplo:

```text
routes/ingest.py
```

se centra en la entrada de eventos, mientras que:

```text
routes/alerts.py
```

se centra en la consulta y actualización de alertas.

---

## 9️⃣ Relación con el flujo general del SIEM

El backend FastAPI participa directamente en el flujo principal del laboratorio:

```text
Evento de seguridad
        ↓
Endpoint de ingesta
        ↓
Validación mediante schemas
        ↓
Persistencia mediante SQLAlchemy
        ↓
Evaluación de reglas
        ↓
Generación de alerta
        ↓
Consulta desde API o frontend
```

Sin el backend, el frontend no tendría forma de consultar datos, la base de datos no recibiría eventos desde la API y el motor de reglas no podría ejecutarse dentro del flujo del laboratorio.

---

## 🔟 Relación con otros módulos

El backend FastAPI se relaciona con los demás módulos de desarrollo de la siguiente forma:

```text
01_Entorno-de-desarrollo
        ↓
define herramientas y dependencias necesarias

02_Base-de-datos
        ↓
proporciona conexión, sesiones y modelos SQLAlchemy

04_API-de-ingesta
        ↓
define los endpoints de entrada y consulta de eventos

05_Motor-de-reglas
        ↓
define la lógica de reglas y condiciones

06_Gestion-de-alertas
        ↓
gestiona la creación, consulta y actualización de alertas

07_Frontend
        ↓
consume la API desde JavaScript

08_Contenerizacion-con-Docker
        ↓
levanta el backend dentro del contenedor siem-api
```

---

## 1️⃣1️⃣ Notas detalladas relacionadas

Las notas detalladas del módulo backend se ubicarán en:

```text
04_Analisis-tecnico-del-backend/
```

Notas previstas:

```text
01_main-py
02_health-py
03_info-py
04_metrics-py
```

El archivo más importante para comenzar es:

```text
backend/app/main.py
```

porque es el punto de entrada de la API y conecta directamente con el comando de arranque definido en Docker Compose.

---

## 1️⃣2️⃣ Resumen técnico

El backend FastAPI es el componente encargado de exponer la lógica del laboratorio mediante una API HTTP.

Su punto de entrada es `backend/app/main.py`, archivo que es cargado por Uvicorn mediante la referencia `app.main:app`. Desde ahí se crea la aplicación FastAPI y se incorporan los distintos routers que separan las funcionalidades del sistema.

La API actúa como intermediaria entre el frontend, la base de datos PostgreSQL y la lógica de eventos, reglas, alertas y métricas. Gracias a FastAPI, el proyecto dispone además de documentación interactiva en `/docs`, lo que facilita la prueba y validación de los endpoints.
