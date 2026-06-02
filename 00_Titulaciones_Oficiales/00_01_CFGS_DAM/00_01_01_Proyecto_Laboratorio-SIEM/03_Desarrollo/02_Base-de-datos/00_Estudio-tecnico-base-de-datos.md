
## 1️⃣ Objetivo de la nota

Esta nota resume el papel de la base de datos dentro del laboratorio SIEM MVP.

El objetivo es entender cómo el backend FastAPI se conecta a PostgreSQL, cómo se crean las sesiones de trabajo con SQLAlchemy y cómo se define la base común de los modelos ORM.

El análisis detallado línea por línea se desarrolla en la carpeta:

```text
03_Analisis-tecnico-de-base-de-datos/
````

---

## 2️⃣ Archivos relacionados

Los archivos principales relacionados con la conexión y estructura base de la base de datos son:

```text
backend/app/db/database.py
backend/app/db/session.py
backend/app/db/base.py
```

También se relacionan directamente con los modelos SQLAlchemy:

```text
backend/app/models/event.py
backend/app/models/rule.py
backend/app/models/alert.py
```

Y con las migraciones de Alembic:

```text
backend/alembic/
backend/alembic/versions/
backend/alembic.ini
```

---

## 3️⃣ Papel de la base de datos dentro del proyecto

La base de datos PostgreSQL es el componente encargado de almacenar la información persistente del laboratorio SIEM.

En el proyecto se almacenan principalmente tres tipos de información:

```text
Eventos  → información recibida por la API de ingesta
Reglas   → condiciones configuradas para detectar comportamientos relevantes
Alertas  → resultados generados cuando un evento cumple una regla
```

El backend FastAPI no trabaja directamente con SQL puro en todos los endpoints. En su lugar, utiliza SQLAlchemy como ORM para representar las tablas mediante clases Python.

La relación general es:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
psycopg
   ↓
PostgreSQL
```

---

## 4️⃣ Relación entre archivos

### `database.py`

Este archivo configura la conexión principal con PostgreSQL.

Sus responsabilidades son:

```text
- Leer la variable de entorno DATABASE_URL.
- Crear el engine de SQLAlchemy.
- Crear la fábrica de sesiones SessionLocal.
- Proporcionar una función simple para probar la conexión.
```

---

### `session.py`

Este archivo define la dependencia `get_db`, utilizada por los endpoints de FastAPI para obtener una sesión de base de datos.

Su función es:

```text
- Crear una sesión.
- Entregarla al endpoint.
- Cerrarla correctamente al terminar la petición.
```

Este archivo es clave porque aparece en rutas como:

```python
db: Session = Depends(get_db)
```

---

### `base.py`

Este archivo define la clase base común de los modelos SQLAlchemy.

Los modelos del proyecto, como `Event`, `Rule` y `Alert`, heredan de esta base para convertirse en modelos ORM.

Su función es proporcionar una clase común desde la que SQLAlchemy puede registrar las tablas del proyecto.

---

## 5️⃣ Flujo técnico de base de datos

El flujo técnico de conexión con la base de datos es el siguiente:

```text
docker/compose.yml
        ↓
define DATABASE_URL
        ↓
contenedor siem-api
        ↓
backend/app/db/database.py
        ↓
create_engine(DATABASE_URL)
        ↓
SessionLocal = sessionmaker(...)
        ↓
backend/app/db/session.py
        ↓
get_db()
        ↓
endpoint FastAPI
        ↓
db.execute(...) / db.add(...) / db.commit(...)
        ↓
PostgreSQL
```

---

## 6️⃣ Relación con los endpoints

Los endpoints que necesitan acceder a PostgreSQL utilizan la dependencia `get_db`.

Ejemplo:

```python
def health(db: Session = Depends(get_db)):
```

Esto significa que FastAPI debe proporcionar una sesión de base de datos al endpoint.

La relación sería:

```text
Endpoint FastAPI
        ↓
Depends(get_db)
        ↓
SessionLocal()
        ↓
Session SQLAlchemy
        ↓
PostgreSQL
```

De esta forma, los endpoints no tienen que crear ni cerrar conexiones manualmente.

---

## 7️⃣ Relación con los modelos

Los modelos SQLAlchemy representan las tablas principales del sistema:

```text
Event → eventos de seguridad
Rule  → reglas de detección
Alert → alertas generadas
```

Estos modelos dependen de la clase `Base` definida en:

```text
backend/app/db/base.py
```

La relación es:

```text
Base
 ├── Event
 ├── Rule
 └── Alert
```

Esto permite que SQLAlchemy conozca la estructura de las tablas y pueda trabajar con ellas como clases Python.

---

## 8️⃣ Relación con Alembic

Alembic se utiliza para gestionar migraciones de base de datos.

Las migraciones permiten crear o modificar tablas de forma controlada.

La relación general es:

```text
Modelos SQLAlchemy
        ↓
Alembic
        ↓
Migraciones
        ↓
PostgreSQL
```

En el proyecto existen migraciones para crear y modificar tablas como:

```text
events
rules
alerts
```

Ejemplos de cambios gestionados por migraciones:

```text
- Crear tabla de eventos.
- Añadir campo meta a eventos.
- Crear reglas y alertas.
- Añadir threshold a reglas.
- Añadir throttle a reglas.
- Añadir group_key a alertas.
- Añadir status y updated_at a alertas.
```

---

## 9️⃣ Relación con el flujo general del SIEM

La base de datos participa en todo el flujo principal del laboratorio:

```text
Evento recibido
        ↓
Validación mediante schema
        ↓
Almacenamiento como Event
        ↓
Consulta de reglas Rule
        ↓
Generación de Alert
        ↓
Consulta desde API, frontend o métricas
```

Sin la base de datos, el sistema no podría conservar eventos, reglas ni alertas entre ejecuciones.

---

## 🔟 Archivos que se analizarán en detalle

El análisis técnico línea por línea se organizará así:

```text
03_Analisis-tecnico-de-base-de-datos/
├── 01_database-py
├── 02_session-py
├── 03_base-py
├── 04_model-event-py
├── 05_model-rule-py
├── 06_model-alert-py
└── 07_migraciones-alembic
```

---

## 1️⃣1️⃣ Resumen técnico

El módulo de base de datos conecta el backend FastAPI con PostgreSQL mediante SQLAlchemy.

El archivo `database.py` crea el motor de conexión y la fábrica de sesiones. El archivo `session.py` proporciona sesiones de base de datos a los endpoints mediante la dependencia `get_db`. El archivo `base.py` define la clase base de la que heredan los modelos ORM.

Gracias a esta estructura, los endpoints pueden trabajar con la base de datos de forma organizada, reutilizable y coherente con la arquitectura del proyecto.
