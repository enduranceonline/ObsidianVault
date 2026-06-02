#linux #bash #python #fastapi #docker #backend #frontend #PostgreSQL #SIEM

## 1️⃣ Objetivo de la nota

Esta nota documenta el entorno de desarrollo utilizado para construir y ejecutar el laboratorio SIEM MVP.

El objetivo es entender la estructura general del proyecto, los directorios principales, los archivos de configuración, la separación entre backend, frontend, base de datos, Docker y pruebas.

Esta nota no analiza todavía un archivo concreto línea por línea. Su función es contextualizar el entorno técnico sobre el que se apoya el resto del proyecto.

---

## 2️⃣ Ubicación general del proyecto

El proyecto se encuentra en el directorio:

```bash
~/siem-lab
````

La ruta completa mostrada por la terminal es:

```text
/home/endurance/siem-lab
```

El usuario trabaja desde una máquina Linux con el usuario:

```text
endurance
```

El acceso al proyecto se realiza con:

```bash
cd ~/siem-lab
```

---

## 3️⃣ Comandos utilizados para revisar el entorno

Para analizar el entorno se ejecutaron estos comandos:

```bash
cd ~/siem-lab

tree -a -L 4

cat .env.example

find backend -maxdepth 4 -type f | sort

find frontend -maxdepth 3 -type f | sort

find docker -maxdepth 3 -type f | sort

ls -la
ls -la backend
ls -la backend/app
ls -la frontend
ls -la docker
```

El comando `tree` no estaba instalado, por lo que el sistema mostró este aviso:

```text
Command 'tree' not found
```

Esto no impide analizar el proyecto, porque se usaron comandos alternativos como:

```bash
find
ls -la
```

---

## 4️⃣ Estructura general del proyecto

La raíz del proyecto contiene estos elementos principales:

```text
siem-lab/
├── backend/
├── configs/
├── data/
├── docker/
├── .env
├── .env.example
├── frontend/
├── .git/
├── .github/
├── .gitignore
└── README.md
```

Cada elemento cumple una función distinta dentro del laboratorio.

---

## 5️⃣ Directorio `backend/`

El directorio:

```text
backend/
```

contiene la aplicación backend desarrollada con Python, FastAPI, SQLAlchemy, Alembic y PostgreSQL.

Contenido principal:

```text
backend/
├── alembic/
├── alembic.ini
├── app/
├── Dockerfile
├── .pytest_cache/
├── pytest.ini
├── requirements.txt
├── tests/
└── venv/
```

Este módulo contiene:

```text
- Código principal de FastAPI.
- Modelos SQLAlchemy.
- Schemas Pydantic.
- Rutas de API.
- Migraciones Alembic.
- Tests.
- Entorno virtual local.
- Dockerfile del backend.
```

---

## 6️⃣ Directorio `backend/app/`

Dentro de `backend/app/` se encuentra el núcleo real de la aplicación.

La estructura mostrada es:

```text
backend/app/
├── api/
├── db/
├── __init__.py
├── main.py
├── models/
├── __pycache__/
└── schemas/
```

La separación es clara:

```text
api/
    ↓
rutas HTTP de FastAPI

db/
    ↓
conexión y sesiones de base de datos

models/
    ↓
modelos ORM de SQLAlchemy

schemas/
    ↓
schemas de validación y respuesta con Pydantic

main.py
    ↓
punto de entrada principal de FastAPI
```

Esta organización permite separar responsabilidades.

---

## 7️⃣ Directorio `backend/app/api/`

Dentro de `backend/app/api/routes/` se encuentran las rutas de la API:

```text
backend/app/api/routes/alerts.py
backend/app/api/routes/events.py
backend/app/api/routes/health.py
backend/app/api/routes/info.py
backend/app/api/routes/ingest.py
backend/app/api/routes/metrics.py
backend/app/api/routes/rules.py
```

Cada archivo define un grupo de endpoints:

```text
health.py
    ↓
comprobación de salud del backend y base de datos

info.py
    ↓
información de versión, build y timestamp

events.py
    ↓
creación y consulta de eventos

ingest.py
    ↓
ingesta principal de eventos y generación de alertas

rules.py
    ↓
creación y listado de reglas

alerts.py
    ↓
consulta y actualización de alertas

metrics.py
    ↓
métricas agregadas del sistema
```

Estos routers se registran en:

```text
backend/app/main.py
```

---

## 8️⃣ Directorio `backend/app/db/`

El directorio:

```text
backend/app/db/
```

contiene los archivos relacionados con la base de datos:

```text
backend/app/db/base.py
backend/app/db/database.py
backend/app/db/session.py
```

Función de cada archivo:

```text
base.py
    ↓
define la clase Base para los modelos ORM

database.py
    ↓
crea engine, SessionLocal y prueba de conexión

session.py
    ↓
define get_db() para inyectar sesiones en FastAPI
```

Este bloque conecta FastAPI con PostgreSQL mediante SQLAlchemy.

---

## 9️⃣ Directorio `backend/app/models/`

El directorio:

```text
backend/app/models/
```

contiene los modelos ORM:

```text
backend/app/models/alert.py
backend/app/models/event.py
backend/app/models/rule.py
```

Cada modelo representa una tabla de PostgreSQL:

```text
Event
    ↓
tabla events

Rule
    ↓
tabla rules

Alert
    ↓
tabla alerts
```

Relación funcional:

```text
Event
    ↓
evento recibido

Rule
    ↓
condición de detección

Alert
    ↓
resultado cuando una regla coincide con un evento
```

---

## 🔟 Directorio `backend/app/schemas/`

El directorio:

```text
backend/app/schemas/
```

contiene los schemas de Pydantic:

```text
backend/app/schemas/alert.py
backend/app/schemas/event.py
backend/app/schemas/ingest.py
backend/app/schemas/rule.py
```

Estos schemas controlan:

```text
- Qué datos acepta la API.
- Qué datos devuelve la API.
- Qué validaciones se aplican.
- Cómo se serializan objetos ORM.
```

Relación típica:

```text
JSON recibido
    ↓
Schema Pydantic
    ↓
Modelo SQLAlchemy
    ↓
PostgreSQL
    ↓
Schema de salida
    ↓
JSON de respuesta
```

---

## 1️⃣1️⃣ Directorio `backend/alembic/`

El directorio:

```text
backend/alembic/
```

contiene la configuración y las migraciones de base de datos.

Archivos y carpetas principales:

```text
backend/alembic/env.py
backend/alembic/README
backend/alembic/script.py.mako
backend/alembic/versions/
```

Dentro de `versions/` aparecen varias migraciones:

```text
c031417b68f1_init.py
b8f4b712e6b5_create_events_table.py
be0f61d66ed2_add_meta_to_events.py
d841bcb4d197_add_rules_and_alerts.py
41bf261af532_add_group_key_to_alerts.py
3099c4ee7f79_add_throttle_to_rules.py
cbd8e2a0c1fe_add_throttle_seconds_to_rules.py
b1b85630457f_add_threshold_to_rules.py
2e15d222277a_add_status_and_updated_at_to_alerts.py
d7f85cce3934_fix_group_key_default.py
```

Esto demuestra que la base de datos se ha ido construyendo de forma incremental.

Las migraciones reflejan la evolución del MVP:

```text
1. Creación inicial.
2. Tabla de eventos.
3. Campo meta en eventos.
4. Reglas y alertas.
5. group_key en alertas.
6. throttle en reglas.
7. threshold en reglas.
8. status y updated_at en alertas.
9. ajustes posteriores.
```

---

## 1️⃣2️⃣ Directorio `backend/tests/`

El proyecto sí contiene tests automatizados.

Aparecen estos archivos:

```text
backend/tests/test_alerts_ui.py
backend/tests/test_health.py
```

También existe configuración de pytest:

```text
backend/pytest.ini
```

Esto significa que el proyecto no depende únicamente de validación manual.

Hay al menos pruebas automatizadas para:

```text
- Healthcheck.
- Endpoints de alertas UI.
```

Este punto será importante cuando lleguemos al módulo:

```text
04_Pruebas-y-validacion
```

o al apartado equivalente dentro de tu estructura.

---

## 1️⃣3️⃣ Directorio `backend/venv/`

El directorio:

```text
backend/venv/
```

contiene un entorno virtual de Python.

Archivos visibles:

```text
backend/venv/bin/activate
backend/venv/bin/pip
backend/venv/bin/python
backend/venv/bin/uvicorn
backend/venv/pyvenv.cfg
```

Este entorno sirve para ejecutar el backend en local sin depender del Python global del sistema.

Sin embargo, para la entrega del proyecto, este directorio no debe incluirse en el `.zip`.

Motivo:

```text
- Es pesado.
- Es recreable.
- Depende de la máquina.
- No forma parte del código fuente.
```

En una entrega limpia se conserva:

```text
requirements.txt
```

y se excluye:

```text
venv/
```

---

## 1️⃣4️⃣ Archivos `__pycache__`, `.pyc` y `.pytest_cache`

En la salida aparecen varios archivos generados automáticamente:

```text
__pycache__/
*.pyc
.pytest_cache/
```

Ejemplos:

```text
backend/app/__pycache__/main.cpython-312.pyc
backend/app/models/__pycache__/alert.cpython-312.pyc
backend/.pytest_cache/
backend/tests/__pycache__/
```

Estos archivos no forman parte del código fuente.

Son generados por:

```text
Python
pytest
ejecución de tests
importación de módulos
```

Para la entrega, deben excluirse.

Son “basura técnica” en el buen sentido: el sistema los genera para acelerar o recordar ejecuciones, pero no hay que entregarlos.

---

## 1️⃣5️⃣ Archivo `requirements.txt`

El archivo:

```text
backend/requirements.txt
```

contiene las dependencias Python del backend.

Aunque en esta salida no se ha impreso su contenido, por el proyecto sabemos que centraliza paquetes necesarios como FastAPI, SQLAlchemy, psycopg, Alembic, Uvicorn y pytest si procede.

Su función es permitir reconstruir el entorno:

```bash
pip install -r requirements.txt
```

Este archivo sí debe entregarse.

Es la forma correcta de que otra persona pueda instalar dependencias sin recibir el `venv`.

---

## 1️⃣6️⃣ Archivo `backend/Dockerfile`

El archivo:

```text
backend/Dockerfile
```

define cómo construir la imagen Docker del backend.

Este archivo es clave para la contenerización.

Relación:

```text
Dockerfile
    ↓
imagen del backend
    ↓
servicio api en docker/compose.yml
```

Este archivo sí forma parte del proyecto y debe incluirse en la entrega.

---

## 1️⃣7️⃣ Directorio `frontend/`

El directorio:

```text
frontend/
```

contiene la interfaz web del laboratorio.

Estructura mostrada:

```text
frontend/
├── alert.html
├── assets/
└── index.html
```

Contenido principal:

```text
frontend/index.html
frontend/alert.html
frontend/assets/app.js
frontend/assets/alerts.js
frontend/assets/alert_detail.js
frontend/assets/styles.css
```

El frontend está construido con:

```text
HTML
CSS
JavaScript puro
```

No utiliza frameworks como React, Angular, Vue o Vite.

Esto simplifica la ejecución y la entrega.

---

## 1️⃣8️⃣ Directorio `frontend/assets/`

El directorio:

```text
frontend/assets/
```

contiene los recursos JavaScript y CSS:

```text
frontend/assets/app.js
frontend/assets/alerts.js
frontend/assets/alert_detail.js
frontend/assets/styles.css
```

Función de cada archivo:

```text
app.js
    ↓
funciones comunes y llamadas a API

alerts.js
    ↓
lógica de listado de alertas

alert_detail.js
    ↓
lógica de detalle y actualización de estado

styles.css
    ↓
estilos visuales
```

---

## 1️⃣9️⃣ Directorio `docker/`

El directorio:

```text
docker/
```

contiene la configuración de Docker Compose:

```text
docker/compose.yml
docker/.env
```

El archivo:

```text
docker/compose.yml
```

define los servicios necesarios para ejecutar el laboratorio.

El archivo:

```text
docker/.env
```

contiene variables reales para Docker.

En una entrega limpia, normalmente se incluye:

```text
docker/compose.yml
```

pero se excluye:

```text
docker/.env
```

porque es un archivo de entorno real.

En su lugar se entrega:

```text
.env.example
```

---

## 2️⃣0️⃣ Archivos `.env` y `.env.example`

En la raíz existen:

```text
.env
.env.example
```

También existe:

```text
docker/.env
```

El archivo `.env.example` contiene:

```env
POSTGRES_DB=siem
POSTGRES_USER=siem
POSTGRES_PASSWORD=change_me
DATABASE_URL=postgresql+psycopg://siem:change_me@db:5432/siem

API_PORT=8000
ADMINER_PORT=8080

APP_VERSION=0.1.0
GIT_SHA=unknown
BUILD_TIME=unknown
```

Función de estas variables:

```text
POSTGRES_DB
    ↓
nombre de la base de datos

POSTGRES_USER
    ↓
usuario de PostgreSQL

POSTGRES_PASSWORD
    ↓
contraseña de ejemplo

DATABASE_URL
    ↓
cadena de conexión usada por SQLAlchemy

API_PORT
    ↓
puerto publicado para FastAPI

ADMINER_PORT
    ↓
puerto publicado para Adminer

APP_VERSION
    ↓
versión de la aplicación

GIT_SHA
    ↓
referencia del commit/build

BUILD_TIME
    ↓
fecha o momento de construcción
```

Punto importante:

```text
.env.example sí se entrega.
.env real no se entrega.
docker/.env real no se entrega.
```

---

## 2️⃣1️⃣ Directorios `configs/` y `data/`

En la raíz aparecen:

```text
configs/
data/
```

Según la salida del proyecto, estos directorios existen pero no muestran archivos dentro en esta revisión.

Posible función:

```text
configs/
    ↓
configuraciones futuras o auxiliares

data/
    ↓
datos de prueba, entrada o persistencia auxiliar
```

Aunque actualmente estén vacíos, pueden mantenerse si forman parte de la estructura prevista del laboratorio.

---

## 2️⃣2️⃣ Directorio `.git/` y `.github/`

Aparecen:

```text
.git/
.github/
```

`.git/` contiene el historial interno del repositorio Git.

No debe incluirse en el `.zip` de entrega.

`.github/` puede contener configuración de GitHub, como workflows o plantillas.

Este directorio sí puede formar parte del código si contiene configuración relevante.

Diferencia:

```text
.git/
    ↓
metadatos internos del repositorio
    ↓
no entregar

.github/
    ↓
configuración del proyecto en GitHub
    ↓
puede entregarse si es relevante
```

---

## 2️⃣3️⃣ Archivo `.gitignore`

El archivo:

```text
.gitignore
```

define qué archivos o carpetas debe ignorar Git.

En este proyecto es importante para excluir:

```text
.env
docker/.env
venv/
__pycache__/
.pytest_cache/
*.pyc
```

Este archivo sí debe entregarse, porque documenta qué elementos no forman parte del código fuente.

---

## 2️⃣4️⃣ Archivo `README.md`

El archivo:

```text
README.md
```

contiene la documentación principal del proyecto.

En la raíz se observa:

```text
-rw-rw-r--  1 endurance endurance 11087 May 26 15:31 README.md
```

Esto indica que fue actualizado para la entrega.

El README debe incluir información como:

```text
- Descripción del proyecto.
- Requisitos.
- Estructura.
- Variables de entorno.
- Ejecución con Docker.
- Endpoints principales.
- Notas sobre la entrega.
```

Es uno de los archivos más importantes para que el evaluador entienda cómo ejecutar el laboratorio.

---

## 2️⃣5️⃣ Archivos que forman parte del código fuente

Sí forman parte del proyecto:

```text
backend/app/
backend/alembic/
backend/alembic.ini
backend/Dockerfile
backend/requirements.txt
backend/pytest.ini
backend/tests/
frontend/
docker/compose.yml
.env.example
.gitignore
README.md
.github/ si contiene configuración relevante
configs/ si forma parte de la estructura
data/ si forma parte de la estructura
```

---

## 2️⃣6️⃣ Archivos que no deberían entregarse

No deberían incluirse en el `.zip` final:

```text
.env
docker/.env
.git/
backend/venv/
__pycache__/
*.pyc
.pytest_cache/
```

Motivo:

```text
.env y docker/.env
    ↓
pueden contener configuración real o sensible

.git/
    ↓
historial interno, no necesario para ejecutar

venv/
    ↓
entorno local recreable

__pycache__ y .pyc
    ↓
caché generada por Python

.pytest_cache
    ↓
caché generada por pytest
```

---

## 2️⃣7️⃣ Relación entre entorno local y Docker

El proyecto permite dos formas de ejecución:

```text
1. Ejecución local con Python/venv.
2. Ejecución contenerizada con Docker Compose.
```

### Ejecución local

Se apoya en:

```text
backend/venv/
backend/requirements.txt
DATABASE_URL
uvicorn
```

Flujo conceptual:

```text
activar venv
    ↓
instalar requirements
    ↓
levantar PostgreSQL o usar una base accesible
    ↓
ejecutar uvicorn
```

### Ejecución con Docker

Se apoya en:

```text
docker/compose.yml
backend/Dockerfile
.env.example / .env
```

Flujo conceptual:

```text
docker compose
    ↓
servicio db
    ↓
servicio api
    ↓
servicio adminer
```

Para una entrega académica, Docker es más reproducible.

---

## 2️⃣8️⃣ Relación con el flujo completo del laboratorio

El entorno de desarrollo sostiene todo el flujo técnico:

```text
docker/compose.yml
    ↓
levanta servicios

PostgreSQL
    ↓
almacena events, rules, alerts

backend/app/main.py
    ↓
expone FastAPI

backend/app/api/routes/
    ↓
define endpoints

frontend/
    ↓
consume endpoints

tests/
    ↓
valida partes del sistema
```

Flujo completo:

```text
Entorno Linux
    ↓
Proyecto siem-lab
    ↓
Docker / Python
    ↓
FastAPI + PostgreSQL
    ↓
API REST
    ↓
Frontend HTML/CSS/JS
    ↓
Usuario consulta y gestiona alertas
```

---

## 2️⃣9️⃣ Punto importante sobre `tree`

El comando:

```bash
tree -a -L 4
```

no estaba instalado.

El sistema sugirió:

```bash
sudo apt install tree
```

o:

```bash
sudo snap install tree
```

Esto no afecta al proyecto.

`tree` solo es una herramienta de visualización.

Se puede sustituir por:

```bash
find . -maxdepth 4 -type f | sort
find . -maxdepth 4 -type d | sort
```

Por tanto, no es una dependencia real del laboratorio.

---

## 3️⃣0️⃣ Comandos útiles del entorno

Entrar al proyecto:

```bash
cd ~/siem-lab
```

Listar raíz:

```bash
ls -la
```

Listar backend:

```bash
ls -la backend
```

Listar app backend:

```bash
ls -la backend/app
```

Listar frontend:

```bash
ls -la frontend
```

Listar Docker:

```bash
ls -la docker
```

Ver variables de ejemplo:

```bash
cat .env.example
```

Buscar archivos del backend:

```bash
find backend -maxdepth 4 -type f | sort
```

Buscar archivos del frontend:

```bash
find frontend -maxdepth 3 -type f | sort
```

Buscar archivos Docker:

```bash
find docker -maxdepth 3 -type f | sort
```

Buscar archivos que no deberían entregarse:

```bash
find . -type d \( -name ".git" -o -name "venv" -o -name "__pycache__" -o -name ".pytest_cache" \) -print
find . -type f -name "*.pyc" -print
```

---

## 3️⃣1️⃣ Resumen técnico

El entorno de desarrollo del laboratorio SIEM MVP está organizado en una estructura clara:

```text
backend/
    ↓
API FastAPI, modelos, schemas, rutas, migraciones y tests

frontend/
    ↓
interfaz HTML, CSS y JavaScript

docker/
    ↓
orquestación con Docker Compose

.env.example
    ↓
plantilla de configuración

README.md
    ↓
documentación de ejecución y entrega
```

La aplicación combina:

```text
Linux
Python
FastAPI
SQLAlchemy
Alembic
PostgreSQL
Docker
HTML
CSS
JavaScript
pytest
```

La estructura permite ejecutar, probar y entregar el proyecto de forma ordenada.

Con esta nota queda contextualizado el entorno antes de analizar archivos concretos del módulo `01_Entorno-de-desarrollo`.
