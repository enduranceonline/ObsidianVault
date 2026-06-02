
## 1️⃣ Objetivo de la nota

Esta nota resume el papel de la API de ingesta dentro del laboratorio SIEM MVP.

El objetivo es entender cómo entra un evento en el sistema, cómo se valida, cómo se almacena en PostgreSQL y cómo puede desencadenar la evaluación de reglas y la generación de alertas.

El análisis detallado línea por línea se desarrolla en la carpeta:

```text
05_Analisis-tecnico-de-ingesta/
````

---

## 2️⃣ Archivos relacionados

Los archivos principales de este módulo son:

```text
backend/app/api/routes/ingest.py
backend/app/api/routes/events.py
backend/app/schemas/ingest.py
backend/app/schemas/event.py
```

También se relacionan directamente con otros archivos ya analizados:

```text
backend/app/models/event.py
backend/app/models/rule.py
backend/app/models/alert.py
backend/app/db/session.py
```

Relación principal:

```text
schemas/
   ↓
validan datos de entrada y salida

routes/
   ↓
definen endpoints HTTP

models/
   ↓
representan tablas SQLAlchemy

db/session.py
   ↓
proporciona sesión de base de datos
```

---

## 3️⃣ Papel de la API de ingesta dentro del proyecto

La API de ingesta es el punto de entrada de eventos al laboratorio SIEM.

Su función es recibir información externa mediante una petición HTTP, validarla y almacenarla como un registro de tipo `Event`.

El flujo principal es:

```text
Cliente / frontend / curl / Swagger
        ↓
POST /ingest
        ↓
IngestPayload
        ↓
Event
        ↓
PostgreSQL
        ↓
Evaluación de reglas
        ↓
Generación opcional de Alert
```

Este módulo es clave porque representa el inicio del flujo real del SIEM.

Sin ingesta, no habría eventos que analizar, reglas que evaluar ni alertas que generar.

---

## 4️⃣ Diferencia entre `/ingest` y `/events`

En este proyecto existen dos rutas relacionadas con eventos:

```text
/ingest
/events
```

Aunque ambas trabajan con eventos, no cumplen exactamente la misma función.

---

### `/ingest`

El endpoint principal de ingesta se encuentra en:

```text
backend/app/api/routes/ingest.py
```

Su función es más completa:

```text
1. Recibe un evento.
2. Lo guarda en la tabla events.
3. Calcula un group_key si existe meta.host.
4. Consulta reglas habilitadas.
5. Evalúa criterios de reglas.
6. Aplica throttle.
7. Aplica anti-duplicado.
8. Aplica threshold si corresponde.
9. Crea alertas si una regla coincide.
10. Confirma la transacción.
```

Por tanto, `/ingest` representa el flujo SIEM completo.

---

### `/events`

El archivo se encuentra en:

```text
backend/app/api/routes/events.py
```

Tiene dos responsabilidades:

```text
POST /events → crear un evento simple
GET /events  → listar eventos con filtros
```

A diferencia de `/ingest`, el endpoint `POST /events` crea un evento básico, pero no ejecuta toda la lógica de reglas y alertas.

Por tanto:

```text
POST /events
        ↓
crea evento

POST /ingest
        ↓
crea evento + evalúa reglas + puede generar alertas
```

La ruta `/events` también sirve para consultar eventos almacenados mediante filtros como:

```text
limit
before_id
source
severity_min
severity_max
q
meta_key
meta_value
```

---

## 5️⃣ Esquemas de validación

Los esquemas se encuentran en:

```text
backend/app/schemas/
```

Los dos archivos principales de este módulo son:

```text
schemas/ingest.py
schemas/event.py
```

---

### `IngestPayload`

Definido en:

```text
backend/app/schemas/ingest.py
```

Representa los datos que debe recibir el endpoint `/ingest`.

Campos:

```text
source   → origen del evento
severity → severidad del evento
message  → mensaje descriptivo
meta     → metadatos opcionales
```

Este schema valida restricciones como:

```text
source   → mínimo 1 carácter, máximo 64
severity → entre 0 y 10
message  → mínimo 1 carácter
meta     → opcional
```

---

### `EventCreate`

Definido en:

```text
backend/app/schemas/event.py
```

Representa los datos necesarios para crear un evento simple desde `/events`.

Campos:

```text
source
severity
message
```

No incluye `meta`, por lo que es más limitado que `IngestPayload`.

---

### `EventOut`

También definido en:

```text
backend/app/schemas/event.py
```

Representa cómo se devuelve un evento desde la API.

Campos:

```text
id
ts
source
severity
message
meta
created_at
```

Este schema permite transformar un objeto SQLAlchemy `Event` en una respuesta JSON.

La configuración:

```python
model_config = {"from_attributes": True}
```

permite a Pydantic construir la respuesta a partir de atributos de un modelo ORM.

---

## 6️⃣ Flujo técnico de `/ingest`

El flujo completo de `POST /ingest` es:

```text
1. El cliente envía un JSON con source, severity, message y meta.
2. FastAPI valida el JSON usando IngestPayload.
3. Se obtiene una sesión de base de datos mediante get_db().
4. Se crea un objeto Event.
5. Se añade el evento a la sesión con db.add(ev).
6. Se ejecuta db.flush() para obtener ev.id antes del commit.
7. Se calcula group_key usando meta.host.
8. Se consultan reglas activas.
9. Cada regla se evalúa contra el evento.
10. Si la regla no coincide, se usa continue.
11. Si la regla coincide, se comprueba throttle.
12. Se comprueba si ya existe una alerta activa.
13. Se comprueba threshold si está configurado.
14. Si todo se cumple, se crea un objeto Alert.
15. Se confirma la transacción con db.commit().
16. Se devuelve el evento creado.
```

Visualmente:

```text
POST /ingest
    ↓
IngestPayload
    ↓
Event(...)
    ↓
db.add(ev)
    ↓
db.flush()
    ↓
Rule.enabled == True
    ↓
criterios de coincidencia
    ↓
throttle / anti-duplicado / threshold
    ↓
Alert(...)
    ↓
db.commit()
    ↓
EventOut
```

---

## 7️⃣ Flujo técnico de `/events`

El archivo `events.py` define dos operaciones principales.

---

### Crear evento simple

```text
POST /events
```

Flujo:

```text
1. Recibe un EventCreate.
2. Crea un objeto Event.
3. Lo añade a la sesión.
4. Ejecuta commit.
5. Refresca el objeto con db.refresh(ev).
6. Devuelve EventOut.
```

Este endpoint es útil para crear eventos de forma directa, pero no contiene la lógica avanzada de `/ingest`.

---

### Listar eventos

```text
GET /events
```

Permite consultar eventos con filtros.

Filtros disponibles:

```text
limit        → número máximo de eventos
before_id    → paginación por id
source       → filtro por origen
severity_min → severidad mínima
severity_max → severidad máxima
q            → búsqueda en message
meta_key     → búsqueda por clave en meta
meta_value   → búsqueda por valor en meta
```

Flujo:

```text
1. Crea una consulta base select(Event).
2. Añade filtros si el usuario los ha indicado.
3. Ordena por Event.id descendente.
4. Limita el número de resultados.
5. Ejecuta la consulta.
6. Devuelve lista de EventOut.
```

---

## 8️⃣ Relación con los modelos

La API de ingesta se relaciona con los modelos ORM de base de datos:

```text
Event
Rule
Alert
```

---

### Relación con `Event`

`Event` representa el evento recibido.

En `/ingest`, se crea así:

```python
ev = Event(
    ts=now,
    source=payload.source,
    severity=payload.severity,
    message=payload.message,
    meta=payload.meta,
)
```

Esto transforma el payload validado en un registro persistible.

---

### Relación con `Rule`

Después de guardar el evento, se consultan reglas activas:

```python
select(Rule).where(Rule.enabled.is_(True))
```

Cada regla se compara contra el evento.

Los criterios evaluados son:

```text
source
severity_min
contains
meta_match
throttle_seconds
threshold_count
threshold_seconds
```

---

### Relación con `Alert`

Si una regla coincide, se crea una alerta:

```python
alert = Alert(
    rule_id=rule.id,
    event_id=ev.id,
    title=f"Rule matched: {rule.name}",
    group_key=group_key,
)
```

Esto conecta:

```text
Alert.rule_id → Rule.id
Alert.event_id → Event.id
```

---

## 9️⃣ Relación con el flujo general del SIEM

Este módulo representa el núcleo funcional del laboratorio.

La relación completa es:

```text
Entrada HTTP
        ↓
Validación Pydantic
        ↓
Modelo Event
        ↓
Base de datos PostgreSQL
        ↓
Consulta de Rule
        ↓
Evaluación lógica
        ↓
Modelo Alert
        ↓
Consulta desde API/frontend
```

En términos del proyecto:

```text
API de ingesta
        ↓
Base de datos
        ↓
Motor de reglas
        ↓
Gestión de alertas
```

Por eso este módulo conecta varios apartados del desarrollo.

---

## 🔟 Puntos importantes

### `/ingest` es el endpoint principal del flujo SIEM

Aunque `/events` también permite crear eventos, `/ingest` es más representativo del funcionamiento real del laboratorio porque activa la lógica de reglas y alertas.

---

### `db.flush()` permite obtener el `id` antes del commit

En `/ingest`, se usa:

```python
db.flush()
```

Esto permite que `ev.id` esté disponible antes de ejecutar `db.commit()`.

Es necesario porque la alerta necesita guardar:

```text
event_id = ev.id
```

---

### `group_key` depende de `meta.host`

La función `_compute_group_key` extrae:

```text
meta.host
```

Si el evento no tiene `meta` o no tiene clave `host`, el `group_key` será `None`.

Esto afecta a:

```text
throttle
anti-duplicado
threshold
```

---

### El endpoint aplica rollback si falla algo

En `/ingest`, si ocurre una excepción, se ejecuta:

```python
db.rollback()
```

Esto evita dejar datos parcialmente guardados.

---

### `/events` permite consulta flexible

El endpoint `GET /events` sirve para revisar eventos almacenados con distintos filtros.

Esto es útil para depuración, frontend y validación del laboratorio.

---

## 1️⃣1️⃣ Notas detalladas relacionadas

Las notas detalladas del módulo se organizarán así:

```text
05_Analisis-tecnico-de-ingesta/
├── 01_ingest-py
├── 02_events-py
├── 03_schema-ingest-py
└── 04_schema-event-py
```

Orden recomendado:

```text
1. schema-ingest-py
2. schema-event-py
3. ingest-py
4. events-py
```

Aunque en la estructura se puede mantener `01_ingest-py`, para estudiar es útil entender primero los schemas.
