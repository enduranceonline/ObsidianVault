
#python #api #fastapi #swagger #pydantic #PostgreSQL #SQLAlchemy #backend #SIEM

## 1️⃣ Objetivo de la nota

Esta nota resume el papel del motor de reglas dentro del laboratorio SIEM MVP.

El objetivo es entender cómo se crean reglas de detección, cómo se almacenan en PostgreSQL y cómo son utilizadas posteriormente durante la ingesta de eventos para decidir si debe generarse una alerta.

El análisis detallado línea por línea se desarrolla en la carpeta:

```text
06_Analisis-tecnico-motor-de-reglas/
````

---

## 2️⃣ Archivos relacionados

Los archivos principales relacionados con el motor de reglas son:

```text
backend/app/api/routes/rules.py
backend/app/schemas/rule.py
backend/app/models/rule.py
backend/app/api/routes/ingest.py
backend/app/models/alert.py
```

Cada archivo cumple una función concreta:

```text
schemas/rule.py
        ↓
define cómo se validan y devuelven las reglas

routes/rules.py
        ↓
expone endpoints para crear y listar reglas

models/rule.py
        ↓
define la tabla rules en PostgreSQL

routes/ingest.py
        ↓
consulta reglas activas y evalúa eventos

models/alert.py
        ↓
almacena las alertas generadas por reglas
```

---

## 3️⃣ Papel del motor de reglas dentro del proyecto

El motor de reglas permite que el laboratorio SIEM no se limite a almacenar eventos, sino que pueda analizarlos.

Sin reglas, el sistema solo tendría un registro de eventos.

Con reglas, el sistema puede detectar condiciones relevantes y generar alertas.

La relación general es:

```text
Evento recibido
        ↓
Consulta de reglas activas
        ↓
Evaluación de criterios
        ↓
Coincidencia
        ↓
Generación de alerta
```

El modelo `Rule` define las condiciones que debe cumplir un evento para considerarse relevante.

---

## 4️⃣ Flujo general del motor de reglas

El flujo completo puede dividirse en dos fases:

```text
1. Configuración de reglas
2. Evaluación de reglas durante la ingesta
```

---

### Fase 1: creación de reglas

La creación de reglas se realiza desde:

```text
POST /rules
```

El flujo es:

```text
Cliente / Swagger / curl
        ↓
POST /rules
        ↓
RuleCreate
        ↓
validación Pydantic
        ↓
modelo Rule
        ↓
tabla rules en PostgreSQL
```

El endpoint está definido en:

```text
backend/app/api/routes/rules.py
```

Y el schema de entrada está definido en:

```text
backend/app/schemas/rule.py
```

---

### Fase 2: evaluación durante la ingesta

La evaluación ocurre dentro de:

```text
POST /ingest
```

El flujo es:

```text
Evento recibido
        ↓
se guarda como Event
        ↓
se consultan reglas habilitadas
        ↓
se compara el evento con cada Rule
        ↓
si coincide, se crea Alert
```

La consulta de reglas activas en `ingest.py` es:

```python
rules = db.execute(
    select(Rule).where(Rule.enabled.is_(True)).order_by(Rule.id.asc())
).scalars().all()
```

Esto significa que solo se evalúan reglas con:

```text
enabled = true
```

---

## 5️⃣ Endpoints relacionados con reglas

El archivo:

```text
backend/app/api/routes/rules.py
```

expone dos endpoints principales:

```text
POST /rules
GET /rules
```

---

### `POST /rules`

Permite crear una regla nueva.

Utiliza el schema:

```text
RuleCreate
```

y devuelve:

```text
RuleOut
```

El flujo es:

```text
JSON de entrada
        ↓
RuleCreate
        ↓
Rule(...)
        ↓
db.add(rule)
        ↓
db.commit()
        ↓
db.refresh(rule)
        ↓
RuleOut
```

---

### `GET /rules`

Permite listar reglas almacenadas.

Acepta un parámetro opcional:

```text
limit
```

Por defecto devuelve hasta 100 reglas y permite un máximo de 500.

El flujo es:

```text
GET /rules
        ↓
select(Rule)
        ↓
order_by(Rule.id.desc())
        ↓
limit(limit)
        ↓
lista de RuleOut
```

---

## 6️⃣ Schemas relacionados con reglas

El archivo:

```text
backend/app/schemas/rule.py
```

define dos schemas:

```text
RuleCreate
RuleOut
```

---

### `RuleCreate`

`RuleCreate` define los datos que el usuario puede enviar para crear una regla.

Campos principales:

```text
name              → nombre de la regla
enabled           → indica si la regla está activa
source            → filtro por origen del evento
severity_min      → severidad mínima
contains          → texto que debe contener el mensaje
throttle_seconds  → control de frecuencia de alertas
threshold_count   → número de eventos requeridos
threshold_seconds → ventana temporal
meta_match        → coincidencia exacta sobre metadatos
```

Este schema valida restricciones como:

```text
name              → entre 1 y 120 caracteres
source            → máximo 64 caracteres
severity_min      → entre 0 y 10
contains          → máximo 200 caracteres
throttle_seconds  → entre 0 y 86400
threshold_count   → entre 1 y 100000
threshold_seconds → entre 1 y 86400
```

---

### `RuleOut`

`RuleOut` define cómo se devuelve una regla desde la API.

Incluye todos los campos principales de la regla y añade:

```text
id
created_at
```

Estos campos no los envía el usuario al crear la regla, sino que proceden de la base de datos.

La configuración:

```python
model_config = {"from_attributes": True}
```

permite convertir objetos SQLAlchemy `Rule` en respuestas JSON mediante Pydantic.

---

## 7️⃣ Modelo `Rule`

El modelo `Rule` se encuentra en:

```text
backend/app/models/rule.py
```

Este modelo representa la tabla:

```text
rules
```

La tabla almacena las condiciones que después se evalúan contra eventos.

Campos principales:

```text
id
name
enabled
source
severity_min
contains
throttle_seconds
threshold_count
threshold_seconds
meta_match
created_at
```

La relación entre schema, modelo y tabla es:

```text
RuleCreate
        ↓
Rule
        ↓
rules
        ↓
RuleOut
```

---

## 8️⃣ Criterios de coincidencia

Durante la ingesta, cada evento se compara con las reglas activas.

Los criterios principales son:

```text
source
severity_min
contains
meta_match
```

---

### Criterio `source`

Permite limitar una regla a eventos de un origen concreto.

Ejemplo:

```text
source = "auth"
```

La regla solo coincidirá con eventos cuyo origen sea `auth`.

---

### Criterio `severity_min`

Permite definir una severidad mínima.

Ejemplo:

```text
severity_min = 4
```

La regla solo coincidirá con eventos cuya severidad sea igual o superior a 4.

---

### Criterio `contains`

Permite buscar texto dentro del mensaje del evento.

Ejemplo:

```text
contains = "failed login"
```

La regla puede coincidir con mensajes como:

```text
Failed login attempt for user admin
```

La comparación se realiza sin distinguir mayúsculas y minúsculas.

---

### Criterio `meta_match`

Permite comparar campos dentro del JSON `meta`.

Ejemplo:

```json
{
  "user": "admin",
  "action": "login_failed"
}
```

La regla solo coincidirá si el evento contiene esos mismos valores dentro de `meta`.

---

## 9️⃣ Throttle

El campo:

```text
throttle_seconds
```

permite limitar la frecuencia con la que una regla genera alertas.

Ejemplo:

```text
throttle_seconds = 300
```

Esto significa que, para la misma regla y grupo, no debería generarse otra alerta hasta que pasen 300 segundos.

En `ingest.py`, el throttle solo se aplica si existe:

```text
group_key
```

El código toma esta decisión:

```text
si group_key es None, no se aplica throttle
```

Esto evita aplicar control de frecuencia sin una agrupación fiable.

---

## 🔟 Threshold

El threshold permite crear reglas que se activan solo cuando se alcanza un número determinado de eventos en una ventana temporal.

Los campos relacionados son:

```text
threshold_count
threshold_seconds
```

Ejemplo:

```text
threshold_count = 5
threshold_seconds = 60
```

Esto significa:

```text
5 eventos en 60 segundos
```

Durante la ingesta, el sistema cuenta eventos recientes que coinciden con la regla dentro de esa ventana temporal.

Si el número de eventos encontrados es menor que `threshold_count`, no genera alerta.

Si es igual o superior, la regla puede generar una alerta.

---

## 1️⃣1️⃣ Relación con `group_key`

El `group_key` se calcula en `ingest.py` a partir de:

```text
meta.host
```

La función encargada es:

```python
def _compute_group_key(ev: Event) -> str | None:
    if not ev.meta:
        return None
    return ev.meta.get("host")
```

Esto significa que, si un evento llega con:

```json
{
  "meta": {
    "host": "server-01"
  }
}
```

entonces:

```text
group_key = "server-01"
```

El `group_key` se usa para:

```text
- throttle
- anti-duplicado
- threshold
- agrupación de alertas
```

---

## 1️⃣2️⃣ Relación con alertas

Cuando una regla coincide con un evento, el sistema crea una alerta.

En `ingest.py`, la alerta se crea así:

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
Alert.rule_id  → Rule.id
Alert.event_id → Event.id
```

Por tanto, una alerta siempre queda relacionada con:

```text
- la regla que la generó
- el evento que la disparó
```

La relación global es:

```text
Rule
   ↓
coincide con
Event
   ↓
genera
Alert
```

---

## 1️⃣3️⃣ Control de duplicados

Además del throttle, el sistema aplica una comprobación anti-duplicado.

Antes de crear una alerta nueva, busca si ya existe una alerta activa para la misma regla y grupo.

Estados considerados activos:

```text
open
ack
```

Si ya existe una alerta con estado `open` o `ack`, el sistema no crea otra alerta duplicada.

Esto reduce ruido y evita llenar el sistema con alertas repetidas.

Las alertas con estado:

```text
closed
```

no bloquean nuevas alertas.

---

## 1️⃣4️⃣ Relación con el flujo general del SIEM

El motor de reglas conecta el almacenamiento de eventos con la generación de alertas.

La relación general es:

```text
POST /rules
        ↓
crea reglas de detección

POST /ingest
        ↓
recibe eventos

Event
        ↓
se evalúa contra

Rule
        ↓
si coincide

Alert
        ↓
se consulta desde /alerts o frontend
```

Dentro del laboratorio, este módulo representa la lógica de detección.

---

## 1️⃣5️⃣ Puntos importantes

### Las reglas deben estar habilitadas

Solo se evalúan reglas con:

```text
enabled = true
```

Las reglas deshabilitadas permanecen en la base de datos, pero no participan en la detección.

---

### `name` debe ser único

El modelo `Rule` tiene una restricción de unicidad sobre `name`.

Si se intenta crear una regla con un nombre repetido, el endpoint devuelve:

```text
409 Conflict
```

con el mensaje:

```text
Rule name already exists
```

---

### Las reglas pueden ser simples o avanzadas

Una regla simple puede usar solo:

```text
source
severity_min
contains
```

Una regla más avanzada puede usar:

```text
meta_match
throttle_seconds
threshold_count
threshold_seconds
```

---

### Threshold y throttle no son lo mismo

```text
throttle
        ↓
limita la frecuencia de alertas

threshold
        ↓
exige varios eventos en una ventana temporal
```

Ambos reducen ruido, pero tienen funciones distintas.

---

### El motor de reglas está distribuido

La creación y listado de reglas está en:

```text
rules.py
```

Pero la evaluación real ocurre en:

```text
ingest.py
```

Por eso el motor de reglas no es un único archivo, sino una interacción entre rutas, schemas, modelos y lógica de ingesta.

---

## 1️⃣6️⃣ Notas detalladas relacionadas

Las notas detalladas del módulo se organizarán así:

```text
06_Analisis-tecnico-motor-de-reglas/
├── 01_schema-rule-py
├── 02_rules-py
└── 03_relacion-rules-ingest-alerts
```

Orden recomendado de estudio:

```text
1. 01_schema-rule-py
2. 02_rules-py
3. 03_relacion-rules-ingest-alerts
```

La primera nota permite entender qué datos acepta una regla.

La segunda permite entender cómo se crean y listan reglas desde la API.

La tercera une el modelo `Rule` con la lógica de `ingest.py` y la generación de `Alert`.
