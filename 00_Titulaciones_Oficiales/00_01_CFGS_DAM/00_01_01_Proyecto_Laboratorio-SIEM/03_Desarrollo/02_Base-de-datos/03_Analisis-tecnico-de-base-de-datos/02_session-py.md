#PostgreSQL #python 
## 1️⃣ Ubicación del archivo dentro del proyecto

```text
siem-lab/
└── backend/
    └── app/
        └── db/
            └── session.py
````

El archivo `session.py` se encuentra dentro del módulo de base de datos del backend:

```text
backend/app/db/
```

Su función principal es proporcionar sesiones de base de datos a los endpoints de FastAPI mediante una dependencia llamada `get_db`.

Este archivo se apoya directamente en `database.py`, concretamente en la fábrica de sesiones:

```python
SessionLocal
```

La relación entre ambos archivos es:

```text
database.py
   ↓
define SessionLocal
   ↓
session.py
   ↓
define get_db()
   ↓
endpoints FastAPI
```

---

## 2️⃣ Comando utilizado para visualizar el archivo

```bash
cd ~/siem-lab
sed -n '1,220p' backend/app/db/session.py
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
backend/app/db/session.py
```

Es la ruta del archivo que se quiere visualizar.

---

## 3️⃣ Código completo del archivo

```python
from collections.abc import Generator
from .database import SessionLocal

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 4️⃣ Función general del archivo

El archivo `session.py` define la función `get_db`.

Esta función se utiliza como dependencia en FastAPI para proporcionar una sesión de base de datos a los endpoints.

En rutas como `health.py` o `metrics.py`, aparece este patrón:

```python
db: Session = Depends(get_db)
```

Eso significa que FastAPI debe ejecutar `get_db()` para obtener una sesión SQLAlchemy y pasarla al endpoint.

La función `get_db()` realiza tres acciones principales:

```text
1. Crea una sesión de base de datos usando SessionLocal().
2. Entrega esa sesión al endpoint mediante yield.
3. Cierra la sesión al terminar la petición.
```

Este archivo evita repetir manualmente la apertura y cierre de sesiones en cada endpoint.

---

## 5️⃣ Estructura general del archivo

El archivo puede dividirse en tres bloques:

```python
from collections.abc import Generator
```

Importación del tipo `Generator`.

```python
from .database import SessionLocal
```

Importación de la fábrica de sesiones definida en `database.py`.

```python
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Definición de la dependencia que crea, entrega y cierra la sesión de base de datos.

Visualmente:

```text
session.py
├── Importación de Generator
├── Importación de SessionLocal
└── Función get_db()
    ├── Crea sesión
    ├── Entrega sesión
    └── Cierra sesión
```

---

# 6️⃣ Análisis línea por línea

---

## Importación de `Generator`

```python
from collections.abc import Generator
```

Esta línea importa `Generator` desde `collections.abc`.

Desglose:

```python
from collections.abc
```

Indica que se importa desde el módulo `collections.abc`, que contiene clases abstractas relacionadas con colecciones e iteradores.

```python
import Generator
```

Importa el tipo `Generator`.

En este archivo se utiliza como anotación de tipo:

```python
def get_db() -> Generator:
```

Un generador es una función que no devuelve un valor con `return`, sino que produce valores con `yield`.

En este caso, `get_db()` usa:

```python
yield db
```

Por eso se anota como `Generator`.

---

## Importación relativa de `SessionLocal`

```python
from .database import SessionLocal
```

Esta línea importa `SessionLocal` desde el archivo `database.py`.

El punto inicial:

```python
.
```

indica una importación relativa dentro del mismo paquete.

Como `session.py` y `database.py` están en la misma carpeta:

```text
backend/app/db/
```

esta línea significa:

```text
desde el archivo database.py de esta misma carpeta, importa SessionLocal
```

Equivalencia conceptual:

```text
backend/app/db/session.py
        ↓
backend/app/db/database.py
        ↓
SessionLocal
```

`SessionLocal` fue definido en `database.py` con:

```python
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
```

Es decir, `SessionLocal` es una fábrica capaz de crear sesiones SQLAlchemy conectadas a PostgreSQL.

---

## Definición de la función `get_db`

```python
def get_db() -> Generator:
```

Esta línea define la función `get_db`.

Desglose:

```python
def
```

Palabra clave de Python para definir una función.

```python
get_db
```

Nombre de la función.

El nombre indica su finalidad:

```text
get_db → obtener base de datos / obtener sesión de base de datos
```

```python
()
```

La función no recibe parámetros.

```python
-> Generator
```

Anotación de tipo que indica que la función devuelve un generador.

Esto tiene sentido porque dentro de la función se utiliza:

```python
yield db
```

```python
:
```

Marca el inicio del bloque de código de la función.

---

## Creación de la sesión

```python
    db = SessionLocal()
```

Esta línea crea una sesión de base de datos.

Desglose:

```python
db
```

Variable local donde se guarda la sesión.

```python
=
```

Operador de asignación.

```python
SessionLocal()
```

Llama a la fábrica de sesiones importada desde `database.py`.

Aunque `SessionLocal` no es una sesión concreta, al ejecutarla con paréntesis:

```python
SessionLocal()
```

se crea una nueva sesión SQLAlchemy.

La relación sería:

```text
SessionLocal
   ↓
SessionLocal()
   ↓
db
```

A partir de este momento, `db` puede utilizarse para consultar o modificar la base de datos.

Ejemplos de uso en otros endpoints:

```python
db.execute(...)
db.add(...)
db.commit()
db.refresh(...)
db.close()
```

---

## Inicio del bloque `try`

```python
    try:
```

Esta línea inicia un bloque `try`.

El bloque `try` se usa para ejecutar código que debe ir acompañado de una limpieza posterior.

En este caso, la limpieza importante es cerrar la sesión de base de datos.

La estructura completa es:

```python
try:
    yield db
finally:
    db.close()
```

Esto significa:

```text
entrega la sesión al endpoint;
cuando termine, pase lo que pase, cierra la sesión.
```

---

## Entrega de la sesión con `yield`

```python
        yield db
```

Esta línea es la parte central de `get_db`.

`yield` convierte la función en un generador.

A diferencia de `return`, que finaliza una función, `yield` entrega un valor y deja la función suspendida hasta que FastAPI termina de usar ese valor.

En este caso:

```python
yield db
```

entrega la sesión de base de datos al endpoint que la ha solicitado.

Por ejemplo, en `health.py`:

```python
def health(db: Session = Depends(get_db)):
```

FastAPI ejecuta `get_db()`, recibe el valor producido por `yield db` y lo asigna al parámetro `db`.

La relación es:

```text
get_db()
   ↓
crea db = SessionLocal()
   ↓
yield db
   ↓
FastAPI entrega db al endpoint
   ↓
endpoint usa db
```

---

## Bloque `finally`

```python
    finally:
```

Esta línea inicia un bloque `finally`.

En Python, el bloque `finally` se ejecuta siempre después del bloque `try`, tanto si todo ha ido bien como si se ha producido un error.

En este archivo, `finally` garantiza que la sesión se cierre incluso si el endpoint falla.

Esto es importante porque dejar sesiones abiertas puede provocar:

```text
- Fugas de conexiones.
- Consumo innecesario de recursos.
- Bloqueos o saturación del pool de conexiones.
```

---

## Cierre de la sesión

```python
        db.close()
```

Esta línea cierra la sesión de base de datos.

Desglose:

```python
db
```

Variable que contiene la sesión SQLAlchemy.

```python
.close()
```

Método que cierra la sesión.

Cerrar la sesión no significa necesariamente cerrar físicamente toda conexión con PostgreSQL para siempre. SQLAlchemy puede devolver la conexión al pool para reutilizarla.

Lo importante es que el endpoint deja de retener esa sesión.

La relación completa es:

```text
Petición HTTP
   ↓
get_db crea sesión
   ↓
endpoint usa sesión
   ↓
termina petición
   ↓
finally ejecuta db.close()
```

---

## Resultado final del archivo

Después de cargar este archivo, queda disponible la función:

```python
get_db()
```

Esta función puede ser utilizada por cualquier endpoint que necesite acceder a PostgreSQL.

Ejemplo:

```python
def endpoint(db: Session = Depends(get_db)):
    ...
```

El comportamiento será:

```text
1. FastAPI recibe una petición.
2. Detecta Depends(get_db).
3. Ejecuta get_db().
4. Se crea una sesión con SessionLocal().
5. La sesión se entrega al endpoint mediante yield.
6. El endpoint usa la sesión.
7. Al terminar la petición, se ejecuta finally.
8. La sesión se cierra con db.close().
```

---

# 7️⃣ Relación con el flujo técnico del laboratorio

`session.py` conecta los endpoints de FastAPI con la infraestructura de base de datos definida en `database.py`.

La relación técnica es:

```text
database.py
   ↓
SessionLocal
   ↓
session.py
   ↓
get_db()
   ↓
Depends(get_db)
   ↓
endpoint FastAPI
   ↓
PostgreSQL
```

Dentro del flujo general del SIEM:

```text
Evento entra por API
        ↓
Endpoint necesita base de datos
        ↓
FastAPI ejecuta get_db()
        ↓
SessionLocal crea sesión
        ↓
Endpoint guarda o consulta datos
        ↓
db.close() cierra la sesión al terminar
```

Este archivo es pequeño, pero muy importante porque evita gestionar sesiones de base de datos manualmente en cada ruta.

---

# 8️⃣ Errores típicos o puntos importantes

### No cerrar la sesión

La función utiliza:

```python
finally:
    db.close()
```

Esto garantiza que la sesión se cierre siempre.

Si no se cerraran las sesiones, con el tiempo podrían acumularse conexiones abiertas.

---

### Confundir `yield` con `return`

En este archivo se usa:

```python
yield db
```

No se usa:

```python
return db
```

Esto es importante porque FastAPI permite usar dependencias con `yield` para ejecutar código de limpieza después de que termine la petición.

Si se usara `return`, sería más difícil garantizar el cierre automático de la sesión en este patrón.

---

### `SessionLocal()` crea una sesión nueva por petición

Cada vez que un endpoint usa:

```python
Depends(get_db)
```

se crea una nueva sesión para esa petición.

Esto evita compartir la misma sesión entre peticiones diferentes.

---

### La sesión depende de `database.py`

Si `SessionLocal` está mal configurado en `database.py`, entonces `get_db()` también fallará.

Por tanto, errores en `DATABASE_URL`, `engine` o `sessionmaker` pueden afectar a todos los endpoints que usen `get_db`.

---

### Anotación genérica `Generator`

La función está anotada como:

```python
def get_db() -> Generator:
```

Esto indica que devuelve un generador, pero no especifica el tipo exacto que genera.

Una anotación más específica podría ser:

```python
def get_db() -> Generator[Session, None, None]:
```

Pero para este proyecto, la versión actual es suficiente y más simple.

---

# 9️⃣ Comandos útiles relacionados

Probar que `get_db` puede importarse:

```bash
docker exec -it siem-api python -c "from app.db.session import get_db; print(get_db)"
```

Probar que `SessionLocal` puede crear una sesión:

```bash
docker exec -it siem-api python -c "from app.db.database import SessionLocal; db = SessionLocal(); print(db); db.close()"
```

Probar una consulta usando una sesión:

```bash
docker exec -it siem-api python -c "from app.db.database import SessionLocal; from sqlalchemy import text; db = SessionLocal(); print(db.execute(text('SELECT 1')).scalar_one()); db.close()"
```

Probar el endpoint `/health`, que usa `get_db`:

```bash
curl http://localhost:8000/health
```

Ver logs de la API:

```bash
docker logs siem-api
```

Ver logs en tiempo real:

```bash
docker logs -f siem-api
```

Reiniciar la API:

```bash
docker compose --env-file docker/.env -f docker/compose.yml restart api
```