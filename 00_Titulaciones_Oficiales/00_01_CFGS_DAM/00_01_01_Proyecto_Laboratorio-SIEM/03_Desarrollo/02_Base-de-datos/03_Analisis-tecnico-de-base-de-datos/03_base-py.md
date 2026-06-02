#PostgreSQL #python 
## 1️⃣ Ubicación del archivo dentro del proyecto

```text
siem-lab/
└── backend/
    └── app/
        └── db/
            └── base.py
````

El archivo `base.py` se encuentra dentro del módulo de base de datos del backend:

```text
backend/app/db/
```

Su función principal es definir la clase base común de los modelos SQLAlchemy del proyecto.

Este archivo es pequeño, pero importante, porque proporciona la clase de la que heredarán los modelos ORM como:

```text
Event
Rule
Alert
```

La relación general es:

```text
base.py
   ↓
Base
   ↓
models/event.py
models/rule.py
models/alert.py
   ↓
tablas de PostgreSQL
```

---

## 2️⃣ Comando utilizado para visualizar el archivo

```bash
cd ~/siem-lab
sed -n '1,220p' backend/app/db/base.py
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
'1,220p'
```

Indica que se impriman las líneas de la 1 a la 220.

```bash
backend/app/db/base.py
```

Es la ruta del archivo que se quiere visualizar.

---

## 3️⃣ Código completo del archivo

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

---

## 4️⃣ Función general del archivo

El archivo `base.py` define una clase llamada `Base`.

Esta clase actúa como clase base para los modelos ORM de SQLAlchemy.

En SQLAlchemy, un modelo ORM es una clase Python que representa una tabla de base de datos.

Por ejemplo:

```text
Clase Python  → Tabla PostgreSQL
Event         → events
Rule          → rules
Alert         → alerts
```

Para que SQLAlchemy pueda reconocer estas clases como modelos de base de datos, deben heredar de una base declarativa.

En este proyecto, esa base declarativa es:

```python
Base
```

La función de este archivo es centralizar esa base común para que todos los modelos compartan la misma estructura de registro interno.

---

## 5️⃣ Estructura general del archivo

El archivo tiene dos bloques:

```python
from sqlalchemy.orm import DeclarativeBase
```

Importa la clase `DeclarativeBase` desde SQLAlchemy.

```python
class Base(DeclarativeBase):
    pass
```

Define la clase `Base`, que hereda de `DeclarativeBase`.

Visualmente:

```text
base.py
├── Importación de DeclarativeBase
└── Definición de clase Base
```

---

# 6️⃣ Análisis línea por línea

---

## Importación de `DeclarativeBase`

```python
from sqlalchemy.orm import DeclarativeBase
```

Esta línea importa `DeclarativeBase` desde el módulo ORM de SQLAlchemy.

Desglose:

```python
from sqlalchemy.orm
```

Indica que la importación se realiza desde la parte ORM de SQLAlchemy.

ORM significa:

```text
Object Relational Mapper
```

Es decir, una herramienta que permite relacionar clases Python con tablas de una base de datos relacional.

```python
import DeclarativeBase
```

Importa la clase `DeclarativeBase`.

`DeclarativeBase` se utiliza en SQLAlchemy 2.x para crear una clase base declarativa moderna.

Esta clase base sirve como punto común para definir modelos ORM.

---

## Definición de la clase `Base`

```python
class Base(DeclarativeBase):
```

Esta línea define una clase llamada `Base`.

Desglose:

```python
class
```

Palabra clave de Python para definir una clase.

```python
Base
```

Nombre de la clase.

Se usa el nombre `Base` por convención. En muchos proyectos con SQLAlchemy, la clase base de los modelos se llama así.

```python
(DeclarativeBase)
```

Indica que `Base` hereda de `DeclarativeBase`.

Esto significa que `Base` recibe el comportamiento necesario para actuar como clase base declarativa de SQLAlchemy.

```python
:
```

Marca el inicio del bloque de código de la clase.

---

## Qué significa heredar de `DeclarativeBase`

Cuando se define:

```python
class Base(DeclarativeBase):
```

se está creando una clase personalizada que SQLAlchemy usará como base para los modelos.

Después, los modelos pueden definirse así:

```python
class Event(Base):
    ...
```

```python
class Rule(Base):
    ...
```

```python
class Alert(Base):
    ...
```

Al heredar de `Base`, esos modelos quedan registrados dentro del sistema declarativo de SQLAlchemy.

Esto permite que SQLAlchemy conozca:

```text
- Qué clases representan tablas.
- Qué columnas tiene cada tabla.
- Qué nombres de tabla se han definido.
- Qué metadatos forman parte del esquema.
```

---

## Cuerpo de la clase

```python
    pass
```

La palabra `pass` indica que la clase no añade ningún comportamiento adicional.

En Python, una clase no puede quedar vacía. Si no se quiere definir nada dentro de ella, se usa `pass`.

Desglose:

```python
pass
```

Instrucción nula de Python.

No ejecuta ninguna acción, pero permite que la clase sea sintácticamente válida.

En este caso significa:

```text
La clase Base hereda todo el comportamiento de DeclarativeBase y no añade nada más.
```

Esto es suficiente para que los modelos del proyecto puedan heredar de `Base`.

---

## Resultado final del archivo

Después de cargar este archivo, queda disponible la clase:

```python
Base
```

Esta clase puede ser importada por los modelos del proyecto.

Ejemplo conceptual:

```python
from app.db.base import Base

class Event(Base):
    ...
```

La relación es:

```text
DeclarativeBase
      ↓
Base
      ↓
Event / Rule / Alert
```

---

# 7️⃣ Relación con el flujo técnico del laboratorio

`base.py` no conecta directamente con PostgreSQL ni ejecuta consultas.

Su función es estructural: permite definir modelos ORM reutilizables.

La relación técnica sería:

```text
base.py
   ↓
Base
   ↓
modelos SQLAlchemy
   ↓
Event / Rule / Alert
   ↓
SQLAlchemy metadata
   ↓
Alembic / PostgreSQL
```

Dentro del flujo general del SIEM, participa de forma indirecta:

```text
Evento recibido
        ↓
Endpoint crea objeto Event
        ↓
Event hereda de Base
        ↓
SQLAlchemy sabe mapear Event a una tabla
        ↓
El evento se guarda en PostgreSQL
```

Sin `Base`, los modelos no tendrían una clase declarativa común y SQLAlchemy no podría gestionarlos correctamente como tablas ORM.

---

# 8️⃣ Errores típicos o puntos importantes

### La clase `Base` debe importarse en los modelos

Los modelos deben heredar de `Base`.

Ejemplo conceptual:

```python
class Event(Base):
    ...
```

Si un modelo no hereda de `Base`, SQLAlchemy no lo tratará como modelo ORM declarativo.

---

### `Base` no representa una tabla

La clase `Base` no es una tabla de la base de datos.

Es una clase base para definir otras clases que sí representarán tablas.

Es decir:

```text
Base  → estructura común
Event → tabla real
Rule  → tabla real
Alert → tabla real
```

---

### `pass` no significa que el archivo no sirva

Aunque el archivo parezca demasiado simple, cumple una función importante.

La lógica está heredada de `DeclarativeBase`.

Por eso no hace falta añadir métodos o atributos dentro de `Base`.

---

### Relación con Alembic

Alembic necesita conocer los metadatos de los modelos para generar o comparar migraciones.

Estos metadatos se construyen a partir de las clases que heredan de `Base`.

Por tanto, `Base` también participa indirectamente en la gestión de migraciones.

---

### SQLAlchemy 2.x

El uso de:

```python
DeclarativeBase
```

corresponde al estilo moderno de SQLAlchemy 2.x.

En versiones anteriores era más habitual encontrar:

```python
declarative_base()
```

Ejemplo antiguo:

```python
Base = declarative_base()
```

En este proyecto se usa la forma moderna:

```python
class Base(DeclarativeBase):
    pass
```

---

# 9️⃣ Comandos útiles relacionados

Probar que `Base` puede importarse:

```bash
docker exec -it siem-api python -c "from app.db.base import Base; print(Base)"
```

Comprobar modelos que heredan de `Base`:

```bash
docker exec -it siem-api python -c "from app.models.event import Event; from app.models.rule import Rule; from app.models.alert import Alert; print(Event, Rule, Alert)"
```

Comprobar las tablas registradas en los metadatos de SQLAlchemy:

```bash
docker exec -it siem-api python -c "from app.db.base import Base; import app.models.event, app.models.rule, app.models.alert; print(Base.metadata.tables.keys())"
```

Comprobar tablas existentes en PostgreSQL:

```bash
docker exec -it siem-db psql -U siem -d siem -c "\dt"
```

Ver migraciones de Alembic:

```bash
ls backend/alembic/versions
```

Comprobar versión actual de migración:

```bash
docker exec -it siem-api alembic current
```