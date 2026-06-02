#PostgreSQL #python 
## 1️⃣ Ubicación del archivo dentro del proyecto

```text
siem-lab/
└── backend/
    └── app/
        └── models/
            └── event.py
````

El archivo `event.py` se encuentra dentro de la carpeta de modelos del backend:

```text
backend/app/models/
```

Este archivo define el modelo SQLAlchemy `Event`, que representa la tabla de eventos del laboratorio SIEM MVP.

Un evento es una unidad de información recibida por el sistema. En el contexto del laboratorio, puede representar una acción, registro o actividad relevante desde el punto de vista de seguridad.

Este modelo es una de las piezas centrales del flujo de datos:

```text
API de ingesta
        ↓
Validación del evento
        ↓
Modelo Event
        ↓
Tabla events en PostgreSQL
```

---

## 2️⃣ Comando utilizado para visualizar el archivo

```bash
cd ~/siem-lab
sed -n '1,260p' backend/app/models/event.py
```

Desglose del comando:

```bash
cd ~/siem-lab
```

Sitúa la terminal en la raíz del proyecto.

```bash
sed
```

Ejecuta el programa `sed`, utilizado para leer o transformar texto.

```bash
-n
```

Evita que `sed` imprima todo el archivo automáticamente.

```bash
'1,260p'
```

Indica que se impriman las líneas de la 1 a la 260.

```bash
backend/app/models/event.py
```

Es la ruta del archivo que se quiere visualizar.

---

## 3️⃣ Código completo del archivo

```python
from typing import Any, Optional
from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    ts: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    source: Mapped[str] = mapped_column(String(64), nullable=False)
    severity: Mapped[int] = mapped_column(Integer, nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    meta: Mapped[Optional[dict[str, Any]]] = mapped_column(JSONB, nullable=True)
```

---

## 4️⃣ Función general del archivo

El archivo `event.py` define la estructura de los eventos dentro de la base de datos.

La clase principal es:

```python
class Event(Base):
```

Esta clase hereda de `Base`, la clase declarativa definida en:

```text
backend/app/db/base.py
```

Gracias a esta herencia, SQLAlchemy interpreta `Event` como un modelo ORM, es decir, como una clase Python que representa una tabla de PostgreSQL.

La tabla asociada se llama:

```python
__tablename__ = "events"
```

Por tanto, la relación es:

```text
Clase Python Event
        ↓
Tabla PostgreSQL events
```

El modelo define los siguientes campos:

```text
id         → identificador único del evento
ts         → timestamp del evento
source     → origen del evento
severity   → severidad numérica
message    → mensaje descriptivo
created_at → fecha de creación del registro
meta       → información adicional en formato JSONB
```

---

## 5️⃣ Estructura general del archivo

El archivo puede dividirse en cuatro bloques:

```python
from typing import Any, Optional
from sqlalchemy.dialects.postgresql import JSONB
```

Importaciones relacionadas con tipos y JSONB.

```python
from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
```

Importaciones principales de SQLAlchemy.

```python
from app.db.base import Base
```

Importación de la clase base declarativa.

```python
class Event(Base):
    ...
```

Definición del modelo `Event`.

Visualmente:

```text
event.py
├── Importaciones de typing
├── Importación de JSONB
├── Importaciones SQLAlchemy
├── Importación de Base
└── Modelo Event
    ├── __tablename__
    ├── id
    ├── ts
    ├── source
    ├── severity
    ├── message
    ├── created_at
    └── meta
```

---

# 6️⃣ Análisis línea por línea

---

## Importación de `Any` y `Optional`

```python
from typing import Any, Optional
```

Esta línea importa dos tipos desde el módulo estándar `typing`.

```python
Any
```

Representa cualquier tipo de dato.

En este archivo se usa para indicar que el diccionario `meta` puede contener valores de cualquier tipo:

```python
dict[str, Any]
```

Esto significa:

```text
diccionario cuyas claves son strings y cuyos valores pueden ser de cualquier tipo
```

---

```python
Optional
```

Indica que un valor puede ser de un tipo concreto o `None`.

En este archivo se usa aquí:

```python
Optional[dict[str, Any]]
```

Esto significa:

```text
puede ser un diccionario o puede ser None
```

Tiene sentido porque el campo `meta` es opcional.

---

## Importación de `JSONB`

```python
from sqlalchemy.dialects.postgresql import JSONB
```

Esta línea importa el tipo `JSONB` específico de PostgreSQL.

`JSONB` permite almacenar datos JSON de forma binaria y eficiente en PostgreSQL.

En este archivo se usa para el campo:

```python
meta
```

La ventaja de `JSONB` es que permite guardar información flexible sin tener que crear una columna específica para cada dato adicional.

Ejemplo de `meta`:

```json
{
  "ip": "192.168.1.10",
  "user": "admin",
  "action": "login_failed"
}
```

En un laboratorio SIEM esto es útil porque no todos los eventos tienen exactamente los mismos campos.

---

## Importaciones principales de SQLAlchemy

```python
from sqlalchemy import DateTime, Integer, String, Text, func
```

Esta línea importa varios tipos y funciones de SQLAlchemy.

---

### `DateTime`

```python
DateTime
```

Representa una columna de fecha y hora.

En este archivo se usa en:

```python
ts
created_at
```

---

### `Integer`

```python
Integer
```

Representa una columna numérica entera.

En este archivo se usa en:

```python
severity
```

---

### `String`

```python
String
```

Representa una cadena de texto con longitud limitada.

En este archivo se usa en:

```python
source
```

con una longitud máxima de 64 caracteres.

---

### `Text`

```python
Text
```

Representa una cadena de texto larga.

En este archivo se usa en:

```python
message
```

Tiene sentido porque el mensaje del evento puede ser más largo que un campo `String` corto.

---

### `func`

```python
func
```

Permite usar funciones SQL desde SQLAlchemy.

En este archivo se usa:

```python
func.now()
```

Esto representa la función SQL `NOW()`, utilizada para generar fechas automáticamente desde la base de datos.

---

## Importación de `Mapped` y `mapped_column`

```python
from sqlalchemy.orm import Mapped, mapped_column
```

Esta línea importa dos elementos del ORM moderno de SQLAlchemy.

---

### `Mapped`

```python
Mapped
```

Se utiliza para anotar los atributos del modelo.

Ejemplo:

```python
id: Mapped[int]
```

Esto indica que `id` es una columna mapeada por SQLAlchemy y que su tipo Python esperado es `int`.

---

### `mapped_column`

```python
mapped_column
```

Se utiliza para definir una columna de base de datos dentro de un modelo ORM.

Ejemplo:

```python
id: Mapped[int] = mapped_column(primary_key=True)
```

Esto define una columna `id` como clave primaria.

---

## Importación de `Base`

```python
from app.db.base import Base
```

Esta línea importa la clase `Base` definida en:

```text
backend/app/db/base.py
```

`Base` es la clase declarativa común de los modelos SQLAlchemy.

La clase `Event` hereda de ella:

```python
class Event(Base):
```

Esto permite que SQLAlchemy registre `Event` como modelo ORM.

---

## Definición de la clase `Event`

```python
class Event(Base):
```

Esta línea define la clase `Event`.

Desglose:

```python
class
```

Palabra clave de Python para definir una clase.

```python
Event
```

Nombre de la clase.

Representa un evento de seguridad dentro del laboratorio.

```python
(Base)
```

Indica que `Event` hereda de `Base`.

Esto convierte la clase en un modelo ORM declarativo de SQLAlchemy.

---

## Nombre de la tabla

```python
    __tablename__ = "events"
```

Esta línea indica el nombre de la tabla en la base de datos.

Desglose:

```python
__tablename__
```

Atributo especial usado por SQLAlchemy para saber qué tabla representa esta clase.

```python
"events"
```

Nombre real de la tabla PostgreSQL.

Por tanto:

```text
Event → events
```

---

## Campo `id`

```python
    id: Mapped[int] = mapped_column(primary_key=True)
```

Esta línea define la columna `id`.

Desglose:

```python
id
```

Nombre del atributo en Python y de la columna en la tabla.

```python
: Mapped[int]
```

Indica que es una columna mapeada y que su tipo esperado es `int`.

```python
= mapped_column(...)
```

Define la columna usando SQLAlchemy.

```python
primary_key=True
```

Indica que esta columna es la clave primaria de la tabla.

La clave primaria identifica de forma única cada registro.

Conceptualmente:

```text
id → identificador único del evento
```

---

## Campo `ts`

```python
    ts: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
```

Esta línea define la columna `ts`.

`ts` significa normalmente `timestamp`.

Representa la fecha y hora asociada al evento.

Desglose:

```python
ts
```

Nombre del atributo y de la columna.

```python
Mapped[object]
```

Indica que es una columna mapeada. Se usa `object` como tipo genérico para el valor de fecha/hora.

```python
mapped_column(...)
```

Define la columna.

---

### Tipo `DateTime(timezone=True)`

```python
DateTime(timezone=True)
```

Indica que la columna almacena fecha y hora con información de zona horaria.

Esto es importante en sistemas de eventos, porque los logs pueden proceder de distintos sistemas o momentos.

---

### Valor por defecto `server_default=func.now()`

```python
server_default=func.now()
```

Indica que si no se proporciona un valor para `ts`, la base de datos asignará automáticamente la hora actual.

La parte `server_default` significa que el valor por defecto lo aplica el servidor de base de datos, no Python.

```python
func.now()
```

Representa la función SQL `NOW()`.

---

### Restricción `nullable=False`

```python
nullable=False
```

Indica que la columna no puede ser nula.

Todo evento debe tener un timestamp.

---

## Campo `source`

```python
    source: Mapped[str] = mapped_column(String(64), nullable=False)
```

Esta línea define la columna `source`.

Representa el origen del evento.

Ejemplos posibles:

```text
firewall
auth
linux
windows
web
ids
```

Desglose:

```python
source
```

Nombre del atributo y de la columna.

```python
Mapped[str]
```

Indica que el tipo Python esperado es `str`.

```python
String(64)
```

Define una cadena de texto con máximo 64 caracteres.

```python
nullable=False
```

Indica que el campo es obligatorio.

Todo evento debe tener un origen.

---

## Campo `severity`

```python
    severity: Mapped[int] = mapped_column(Integer, nullable=False)
```

Esta línea define la columna `severity`.

Representa la severidad del evento.

Desglose:

```python
severity
```

Nombre del atributo y de la columna.

```python
Mapped[int]
```

Tipo Python esperado: entero.

```python
Integer
```

Tipo de columna SQL: número entero.

```python
nullable=False
```

Campo obligatorio.

La severidad permite clasificar la importancia del evento.

Ejemplo conceptual:

```text
1 → baja
2 → media
3 → alta
4 → crítica
```

La escala exacta depende de cómo se haya diseñado el sistema.

---

## Campo `message`

```python
    message: Mapped[str] = mapped_column(Text, nullable=False)
```

Esta línea define la columna `message`.

Representa el mensaje descriptivo del evento.

Desglose:

```python
message
```

Nombre del atributo y de la columna.

```python
Mapped[str]
```

Tipo Python esperado: string.

```python
Text
```

Tipo SQL para texto largo.

```python
nullable=False
```

Campo obligatorio.

Este campo puede contener una descripción del evento, por ejemplo:

```text
Failed login attempt for user admin
Connection blocked from suspicious IP
Multiple authentication failures detected
```

---

## Campo `created_at`

```python
    created_at: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
```

Esta línea define la columna `created_at`.

Representa la fecha y hora en la que el evento fue creado dentro de la base de datos.

Aunque se parece a `ts`, no significa necesariamente lo mismo.

Diferencia conceptual:

```text
ts         → momento asociado al evento
created_at → momento en que el registro se crea en la base de datos
```

En muchos casos pueden coincidir, pero no siempre.

Por ejemplo, un evento podría haber ocurrido a las 10:00, pero ser recibido e insertado en el SIEM a las 10:05.

---

### Tipo `DateTime(timezone=True)`

```python
DateTime(timezone=True)
```

Fecha y hora con zona horaria.

---

### Valor por defecto

```python
server_default=func.now()
```

Si no se proporciona `created_at`, PostgreSQL asigna la hora actual.

---

### Restricción

```python
nullable=False
```

El campo no puede ser nulo.

---

## Campo `meta`

```python
    meta: Mapped[Optional[dict[str, Any]]] = mapped_column(JSONB, nullable=True)
```

Esta línea define la columna `meta`.

Es uno de los campos más flexibles del modelo.

Permite almacenar información adicional del evento en formato JSONB.

Desglose:

```python
meta
```

Nombre del atributo y columna.

```python
Mapped[Optional[dict[str, Any]]]
```

Indica que el valor puede ser:

```text
- Un diccionario con claves string y valores de cualquier tipo.
- None.
```

```python
mapped_column(JSONB, nullable=True)
```

Define una columna PostgreSQL de tipo JSONB y permite valores nulos.

---

### Por qué usar `JSONB`

En un laboratorio SIEM, no todos los eventos tienen los mismos campos.

Un evento de autenticación puede tener:

```json
{
  "user": "admin",
  "ip": "192.168.1.10"
}
```

Un evento de firewall puede tener:

```json
{
  "src_ip": "10.0.0.5",
  "dst_port": 443,
  "action": "blocked"
}
```

Usar `meta` permite guardar esos datos adicionales sin modificar la estructura principal de la tabla.

---

## Resultado final del archivo

Después de cargar este archivo, SQLAlchemy dispone del modelo:

```python
Event
```

Este modelo representa la tabla:

```text
events
```

con los campos:

```text
id
ts
source
severity
message
created_at
meta
```

---

# 7️⃣ Relación con el flujo técnico del laboratorio

El modelo `Event` participa directamente en el flujo principal del SIEM.

La relación técnica sería:

```text
POST /ingest
        ↓
datos recibidos por FastAPI
        ↓
validación mediante schema
        ↓
creación de objeto Event
        ↓
SQLAlchemy guarda Event
        ↓
registro insertado en tabla events
```

Después, esos eventos pueden ser consultados por otros endpoints:

```text
GET /events
GET /metrics
```

También pueden ser evaluados por el motor de reglas para generar alertas.

Relación general:

```text
Event
   ↓
representa evento recibido
   ↓
se almacena en PostgreSQL
   ↓
puede activar Rule
   ↓
puede generar Alert
```

---

# 8️⃣ Errores típicos o puntos importantes

### Diferencia entre `ts` y `created_at`

Aunque ambos son campos de fecha, no tienen por qué significar lo mismo.

```text
ts         → momento del evento
created_at → momento de inserción en la base de datos
```

En este proyecto ambos tienen valor por defecto `func.now()`, pero conceptualmente conviene diferenciarlos.

---

### `meta` puede ser nulo

El campo `meta` está definido como:

```python
nullable=True
```

Esto significa que un evento puede no tener metadatos adicionales.

---

### `source`, `severity` y `message` son obligatorios

Estos campos tienen:

```python
nullable=False
```

Por tanto, no pueden insertarse eventos sin esos valores.

---

### `JSONB` es específico de PostgreSQL

El tipo:

```python
JSONB
```

pertenece al dialecto PostgreSQL.

Esto significa que el modelo está diseñado específicamente para PostgreSQL, no para cualquier base de datos genérica.

---

### Longitud máxima de `source`

El campo `source` usa:

```python
String(64)
```

Por tanto, el origen del evento no debería superar los 64 caracteres.

---

### `Mapped` y `mapped_column` pertenecen al estilo moderno de SQLAlchemy

Este modelo usa sintaxis moderna de SQLAlchemy 2.x:

```python
id: Mapped[int] = mapped_column(...)
```

Esta forma combina tipado Python con definición ORM.

---

# 9️⃣ Comandos útiles relacionados

Comprobar que el modelo se puede importar:

```bash
docker exec -it siem-api python -c "from app.models.event import Event; print(Event)"
```

Comprobar el nombre de la tabla:

```bash
docker exec -it siem-api python -c "from app.models.event import Event; print(Event.__tablename__)"
```

Comprobar columnas del modelo:

```bash
docker exec -it siem-api python -c "from app.models.event import Event; print(Event.__table__.columns.keys())"
```

Comprobar tablas en PostgreSQL:

```bash
docker exec -it siem-db psql -U siem -d siem -c "\dt"
```

Consultar estructura de la tabla `events`:

```bash
docker exec -it siem-db psql -U siem -d siem -c "\d events"
```

Consultar eventos almacenados:

```bash
docker exec -it siem-db psql -U siem -d siem -c "SELECT id, ts, source, severity, message, created_at, meta FROM events LIMIT 10;"
```

Contar eventos:

```bash
docker exec -it siem-db psql -U siem -d siem -c "SELECT COUNT(*) FROM events;"
```

Consultar eventos por severidad:

```bash
docker exec -it siem-db psql -U siem -d siem -c "SELECT severity, COUNT(*) FROM events GROUP BY severity ORDER BY severity;"
```

Consultar eventos con metadatos:

```bash
docker exec -it siem-db psql -U siem -d siem -c "SELECT id, meta FROM events WHERE meta IS NOT NULL LIMIT 10;"
```