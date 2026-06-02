#python #api #fastapi #PostgreSQL #SQLAlchemy #backend #SIEM

## 1️⃣ Objetivo de la nota

Esta nota explica la relación técnica entre las reglas (`Rule`), la ingesta de eventos (`ingest.py`) y la generación de alertas (`Alert`) dentro del laboratorio SIEM MVP.

A diferencia de las notas anteriores, esta no analiza un único archivo línea por línea. Su función es unir varias piezas ya estudiadas para entender el flujo completo del motor de reglas.

Los archivos implicados son:

```text
backend/app/schemas/rule.py
backend/app/api/routes/rules.py
backend/app/models/rule.py
backend/app/api/routes/ingest.py
backend/app/models/event.py
backend/app/models/alert.py
```

El objetivo principal es entender esta cadena:

```text
RuleCreate
    ↓
Rule
    ↓
POST /ingest
    ↓
Event
    ↓
evaluación de reglas
    ↓
Alert
```

---

## 2️⃣ Archivos relacionados

```text
backend/app/schemas/rule.py
```

Define cómo se validan los datos necesarios para crear una regla.

```text
backend/app/api/routes/rules.py
```

Define los endpoints `POST /rules` y `GET /rules`.

```text
backend/app/models/rule.py
```

Define el modelo ORM `Rule`, que representa la tabla `rules`.

```text
backend/app/api/routes/ingest.py
```

Contiene la lógica que consulta reglas activas y evalúa eventos contra ellas.

```text
backend/app/models/event.py
```

Define el modelo `Event`, que representa los eventos recibidos.

```text
backend/app/models/alert.py
```

Define el modelo `Alert`, que representa las alertas generadas cuando una regla coincide.

---

## 3️⃣ Visión general del flujo

El motor de reglas funciona en dos momentos diferentes:

```text
1. Configuración de reglas
2. Evaluación de reglas durante la ingesta
```

La primera parte ocurre cuando el usuario crea una regla mediante la API.

La segunda ocurre cuando llega un evento nuevo al endpoint `/ingest`.

Flujo completo:

```text
POST /rules
    ↓
se crea una Rule
    ↓
la regla queda guardada en PostgreSQL
    ↓
POST /ingest
    ↓
llega un Event
    ↓
se consultan Rules activas
    ↓
se compara Event contra cada Rule
    ↓
si coincide, se crea una Alert
```

---

## 4️⃣ Fase 1: creación de una regla

La creación de reglas empieza en el endpoint:

```text
POST /rules
```

Este endpoint está definido en:

```text
backend/app/api/routes/rules.py
```

El cliente envía un JSON parecido a este:

```json
{
  "name": "Failed login auth",
  "enabled": true,
  "source": "auth",
  "severity_min": 3,
  "contains": "failed login",
  "throttle_seconds": 300,
  "threshold_count": 5,
  "threshold_seconds": 60,
  "meta_match": {
    "user": "admin"
  }
}
```

Ese JSON se valida con el schema:

```python
RuleCreate
```

definido en:

```text
backend/app/schemas/rule.py
```

---

## 5️⃣ Validación con `RuleCreate`

El schema `RuleCreate` define qué campos puede enviar el usuario al crear una regla.

Campos principales:

```text
name
enabled
source
severity_min
contains
throttle_seconds
threshold_count
threshold_seconds
meta_match
```

Este schema aplica validaciones antes de llegar a la base de datos.

Ejemplos:

```text
name              → mínimo 1 carácter, máximo 120
source            → máximo 64 caracteres
severity_min      → entre 0 y 10
contains          → máximo 200 caracteres
throttle_seconds  → entre 0 y 86400
threshold_count   → entre 1 y 100000
threshold_seconds → entre 1 y 86400
```

Esto evita que entren reglas mal formadas.

La relación es:

```text
JSON recibido
    ↓
RuleCreate
    ↓
datos validados
```

Si el JSON no cumple las restricciones, FastAPI devuelve error de validación y la regla no se crea.

---

## 6️⃣ Conversión de `RuleCreate` a `Rule`

Una vez validado el payload, `rules.py` crea un objeto `Rule`:

```python
rule = Rule(
    name=payload.name,
    enabled=payload.enabled,
    source=payload.source,
    severity_min=payload.severity_min,
    contains=payload.contains,
    meta_match=payload.meta_match,
    throttle_seconds=payload.throttle_seconds,
    threshold_count=payload.threshold_count,
    threshold_seconds=payload.threshold_seconds,
)
```

Aquí ocurre el paso de schema Pydantic a modelo SQLAlchemy.

Relación campo a campo:

```text
payload.name              → rule.name
payload.enabled           → rule.enabled
payload.source            → rule.source
payload.severity_min      → rule.severity_min
payload.contains          → rule.contains
payload.meta_match        → rule.meta_match
payload.throttle_seconds  → rule.throttle_seconds
payload.threshold_count   → rule.threshold_count
payload.threshold_seconds → rule.threshold_seconds
```

Conceptualmente:

```text
RuleCreate
    ↓
Rule
```

`RuleCreate` valida datos.

`Rule` representa una fila real en la tabla `rules`.

---

## 7️⃣ Persistencia de la regla

Después de crear el objeto `Rule`, el endpoint lo añade a la sesión de base de datos:

```python
db.add(rule)
```

Luego intenta confirmar la transacción:

```python
db.commit()
```

Si todo va bien, la regla queda almacenada en PostgreSQL.

Relación:

```text
Rule
    ↓
db.add(rule)
    ↓
db.commit()
    ↓
tabla rules
```

La tabla afectada es:

```text
rules
```

---

## 8️⃣ Control de reglas duplicadas

El campo `name` de la regla es único.

En el modelo `Rule`, se define como:

```python
name: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
```

Esto significa que no pueden existir dos reglas con el mismo nombre.

Si el usuario intenta crear una regla duplicada, SQLAlchemy puede lanzar:

```python
IntegrityError
```

El endpoint lo captura así:

```python
except IntegrityError:
    db.rollback()
    raise HTTPException(status_code=409, detail="Rule name already exists")
```

Esto devuelve un error HTTP:

```text
409 Conflict
```

Con respuesta:

```json
{
  "detail": "Rule name already exists"
}
```

Este control evita duplicidades y mantiene la tabla `rules` más limpia.

---

## 9️⃣ Fase 2: llegada de un evento a `/ingest`

Una vez existen reglas en la base de datos, el flujo principal ocurre cuando llega un evento al endpoint:

```text
POST /ingest
```

Este endpoint está definido en:

```text
backend/app/api/routes/ingest.py
```

Ejemplo de evento recibido:

```json
{
  "source": "auth",
  "severity": 4,
  "message": "Failed login attempt for user admin",
  "meta": {
    "host": "server-01",
    "user": "admin",
    "ip": "192.168.1.10"
  }
}
```

El evento se valida con:

```python
IngestPayload
```

Después se crea un objeto:

```python
Event
```

y se guarda en la base de datos.

---

## 🔟 Creación del evento

En `ingest.py`, el evento se crea así:

```python
ev = Event(
    ts=now,
    source=payload.source,
    severity=payload.severity,
    message=payload.message,
    meta=payload.meta,
)
```

Este objeto representa una fila de la tabla:

```text
events
```

Después se añade a la sesión:

```python
db.add(ev)
```

Y se ejecuta:

```python
db.flush()
```

El `flush` es importante porque permite obtener:

```python
ev.id
```

antes de hacer `commit`.

Esto es necesario porque, si una regla coincide, la alerta necesitará guardar:

```text
event_id = ev.id
```

---

## 1️⃣1️⃣ Cálculo de `group_key`

Después de crear el evento, `ingest.py` calcula una clave de agrupación:

```python
group_key = _compute_group_key(ev)
```

La función auxiliar es:

```python
def _compute_group_key(ev: Event) -> str | None:
    if not ev.meta:
        return None
    return ev.meta.get("host")
```

Esto significa que el sistema busca:

```text
meta.host
```

Ejemplo:

```json
{
  "meta": {
    "host": "server-01"
  }
}
```

Resultado:

```text
group_key = "server-01"
```

Si no existe `meta` o no existe `host`, el resultado será:

```text
group_key = None
```

El `group_key` es importante porque afecta a:

```text
throttle
anti-duplicado
threshold
agrupación de alertas
```

---

## 1️⃣2️⃣ Consulta de reglas activas

Después de guardar temporalmente el evento, `ingest.py` consulta las reglas activas:

```python
rules = db.execute(
    select(Rule).where(Rule.enabled.is_(True)).order_by(Rule.id.asc())
).scalars().all()
```

Esta consulta obtiene únicamente reglas donde:

```text
enabled = true
```

Por tanto, una regla deshabilitada sigue existiendo en la tabla `rules`, pero no se evalúa.

La relación es:

```text
tabla rules
    ↓
solo enabled = true
    ↓
lista de reglas activas
```

Ordena por:

```text
Rule.id ascendente
```

Esto hace que las reglas se evalúen según el orden en que fueron creadas.

---

## 1️⃣3️⃣ Evaluación de cada regla

Una vez obtenidas las reglas activas, el sistema las recorre:

```python
for rule in rules:
```

Por cada regla, se comprueban varios criterios.

Si un criterio no se cumple, se ejecuta:

```python
continue
```

Esto significa:

```text
esta regla no aplica;
pasa a la siguiente regla
```

El flujo es:

```text
rule 1
    ↓
¿coincide?
    ↓
sí/no

rule 2
    ↓
¿coincide?
    ↓
sí/no

rule 3
    ↓
¿coincide?
    ↓
sí/no
```

Una misma ingesta puede generar cero, una o varias alertas, dependiendo de cuántas reglas coincidan.

---

## 1️⃣4️⃣ Criterio `source`

El primer criterio es el origen:

```python
if rule.source and ev.source != rule.source:
    continue
```

Si la regla tiene definido `source`, el evento debe tener el mismo origen.

Ejemplo:

```text
rule.source = "auth"
ev.source   = "auth"
```

Coincide.

Ejemplo contrario:

```text
rule.source = "auth"
ev.source   = "firewall"
```

No coincide.

Si `rule.source` es `None`, este criterio no se aplica.

---

## 1️⃣5️⃣ Criterio `severity_min`

El segundo criterio es la severidad mínima:

```python
if rule.severity_min is not None and ev.severity < rule.severity_min:
    continue
```

Ejemplo:

```text
rule.severity_min = 5
ev.severity       = 3
```

Como `3 < 5`, la regla no aplica.

Ejemplo válido:

```text
rule.severity_min = 5
ev.severity       = 7
```

Como `7 >= 5`, la regla supera este criterio.

Si `severity_min` es `None`, no se filtra por severidad.

---

## 1️⃣6️⃣ Criterio `contains`

El tercer criterio es la búsqueda de texto dentro del mensaje:

```python
if rule.contains and rule.contains.lower() not in (ev.message or "").lower():
    continue
```

Ejemplo:

```text
rule.contains = "failed login"
ev.message    = "Failed login attempt for user admin"
```

Coincide.

La comparación usa `.lower()` en ambos textos, por lo que no distingue mayúsculas y minúsculas.

Esto evita que fallen coincidencias por diferencias como:

```text
Failed Login
failed login
FAILED LOGIN
```

---

## 1️⃣7️⃣ Criterio `meta_match`

El cuarto criterio es la coincidencia exacta sobre metadatos:

```python
if rule.meta_match:
    if not ev.meta:
        continue
    if any(ev.meta.get(k) != v for k, v in rule.meta_match.items()):
        continue
```

Si la regla tiene `meta_match`, el evento debe tener `meta`.

Después, cada clave y valor de `meta_match` debe coincidir con el `meta` del evento.

Ejemplo de regla:

```json
{
  "meta_match": {
    "user": "admin",
    "facility": "auth"
  }
}
```

Evento válido:

```json
{
  "meta": {
    "user": "admin",
    "facility": "auth",
    "host": "server-01"
  }
}
```

Evento no válido:

```json
{
  "meta": {
    "user": "guest",
    "facility": "auth"
  }
}
```

No coincide porque:

```text
user != admin
```

---

## 1️⃣8️⃣ Resultado de los criterios básicos

Si el evento supera:

```text
source
severity_min
contains
meta_match
```

entonces la regla se considera candidata para generar alerta.

Pero antes de crearla, el sistema puede aplicar controles adicionales:

```text
throttle
anti-duplicado
threshold
```

Estos controles reducen ruido y evitan alertas repetidas o prematuras.

---

## 1️⃣9️⃣ Throttle

El throttle limita la frecuencia con la que una regla puede generar alertas para el mismo grupo.

El código solo lo aplica si:

```python
group_key is not None
and rule.throttle_seconds is not None
and rule.throttle_seconds > 0
```

Esto significa:

```text
debe existir group_key
debe existir throttle_seconds
throttle_seconds debe ser mayor que 0
```

Si `group_key` es `None`, el throttle no se aplica.

La razón es que no hay una agrupación fiable.

---

## 2️⃣0️⃣ Consulta de última alerta para throttle

Para aplicar throttle, el sistema busca la última alerta activa de la misma regla y grupo:

```python
select(Alert.created_at)
.where(
    Alert.rule_id == rule.id,
    Alert.group_key == group_key,
    Alert.status.in_(("open", "ack")),
)
.order_by(Alert.created_at.desc())
.limit(1)
```

Esta consulta busca alertas:

```text
de la misma regla
del mismo group_key
con estado open o ack
```

No considera alertas cerradas.

Esto tiene sentido porque una alerta cerrada ya no debería bloquear indefinidamente nuevas alertas.

---

## 2️⃣1️⃣ Comparación temporal del throttle

Si existe una alerta anterior, se calcula la diferencia:

```python
delta = (now - last_alert_ts).total_seconds()
```

Después se compara con el throttle:

```python
if delta < rule.throttle_seconds:
    continue
```

Ejemplo:

```text
rule.throttle_seconds = 300
última alerta hace 100 segundos
```

Resultado:

```text
100 < 300
    ↓
no se crea alerta
```

Si han pasado más de 300 segundos, el flujo continúa.

---

## 2️⃣2️⃣ Anti-duplicado

Después del throttle, el sistema aplica una comprobación anti-duplicado.

El objetivo es evitar crear otra alerta si ya existe una alerta activa para la misma regla y grupo.

Consulta:

```python
select(Alert.id)
.where(
    Alert.rule_id == rule.id,
    Alert.group_key == group_key,
    Alert.status.in_(("open", "ack")),
)
.order_by(Alert.created_at.desc())
.limit(1)
```

Si devuelve un ID, significa que ya existe una alerta activa.

Entonces se ejecuta:

```python
continue
```

y no se crea otra alerta.

---

## 2️⃣3️⃣ Diferencia entre throttle y anti-duplicado

Throttle y anti-duplicado se parecen, pero no son lo mismo.

```text
Throttle
    ↓
evita alertas demasiado frecuentes durante un tiempo definido

Anti-duplicado
    ↓
evita crear otra alerta si ya hay una abierta o reconocida
```

Ejemplo:

```text
throttle_seconds = 300
```

Puede bloquear nuevas alertas durante 5 minutos.

El anti-duplicado puede bloquearlas mientras exista una alerta `open` o `ack`, aunque hayan pasado más de 5 minutos.

En este proyecto, ambos mecanismos reducen ruido.

El anti-duplicado es más fuerte porque depende del estado de la alerta.

---

## 2️⃣4️⃣ Threshold

El threshold permite generar alerta solo si hay varios eventos coincidentes dentro de una ventana temporal.

Se aplica si existen ambos campos:

```python
rule.threshold_count is not None
and rule.threshold_seconds is not None
```

Ejemplo de regla:

```json
{
  "threshold_count": 5,
  "threshold_seconds": 60
}
```

Significa:

```text
5 eventos en 60 segundos
```

---

## 2️⃣5️⃣ Threshold requiere `group_key`

El código exige:

```python
if group_key is None:
    continue
```

Por tanto, si no existe `meta.host`, no se aplica threshold.

Esto es importante.

Para que una regla con threshold funcione correctamente, los eventos deben incluir:

```json
{
  "meta": {
    "host": "server-01"
  }
}
```

Así el sistema puede contar eventos agrupados por host.

---

## 2️⃣6️⃣ Ventana temporal del threshold

El inicio de la ventana se calcula así:

```python
window_start = now - timedelta(seconds=rule.threshold_seconds)
```

Ejemplo:

```text
now = 12:00:00
threshold_seconds = 60
window_start = 11:59:00
```

Después se cuentan eventos desde ese momento:

```python
stmt = select(func.count(Event.id)).where(Event.ts >= window_start)
```

Esto permite responder a la pregunta:

```text
¿Cuántos eventos coincidentes han ocurrido en los últimos X segundos?
```

---

## 2️⃣7️⃣ Filtros usados en threshold

La consulta del threshold reutiliza los criterios de la regla:

```text
source
severity_min
contains
meta_match
host/group_key
```

Filtros aplicados:

```python
if rule.source:
    stmt = stmt.where(Event.source == rule.source)
```

```python
if rule.severity_min is not None:
    stmt = stmt.where(Event.severity >= rule.severity_min)
```

```python
if rule.contains:
    stmt = stmt.where(Event.message.ilike(f"%{rule.contains}%"))
```

```python
if rule.meta_match:
    stmt = stmt.where(Event.meta.contains(rule.meta_match))
```

```python
stmt = stmt.where(Event.meta.contains({"host": group_key}))
```

Esto hace que el conteo no sea genérico, sino ajustado a la regla actual.

---

## 2️⃣8️⃣ Comparación con `threshold_count`

El número de eventos encontrados se guarda en:

```python
matched_count = db.execute(stmt).scalar_one()
```

Luego se compara:

```python
if matched_count < rule.threshold_count:
    continue
```

Ejemplo:

```text
threshold_count = 5
matched_count = 4
```

No se genera alerta.

Ejemplo:

```text
threshold_count = 5
matched_count = 5
```

Sí puede generarse alerta.

---

## 2️⃣9️⃣ Creación de la alerta

Si el evento supera todos los criterios, se crea una alerta:

```python
alert = Alert(
    rule_id=rule.id,
    event_id=ev.id,
    title=f"Rule matched: {rule.name}",
    group_key=group_key,
)
```

Relación:

```text
rule.id → alert.rule_id
ev.id   → alert.event_id
```

Esto conecta la alerta con:

```text
la regla que coincidió
el evento que la disparó
```

Después se añade a la sesión:

```python
db.add(alert)
```

La alerta se confirmará cuando se ejecute:

```python
db.commit()
```

---

## 3️⃣0️⃣ Transacción completa

En `ingest.py`, el evento y las alertas se guardan dentro de la misma transacción.

Flujo:

```text
db.add(ev)
db.flush()
db.add(alert)
db.commit()
```

Esto significa que la ingesta intenta guardar todo junto.

Si algo falla, se ejecuta:

```python
db.rollback()
```

y se revierte la operación.

Esto evita estados intermedios incorrectos.

---

## 3️⃣1️⃣ Flujo completo resumido

```text
1. Se crea una regla con POST /rules.
2. La regla se valida con RuleCreate.
3. La regla se guarda como Rule en PostgreSQL.
4. Llega un evento a POST /ingest.
5. El evento se valida con IngestPayload.
6. Se crea un objeto Event.
7. Se guarda temporalmente con db.flush().
8. Se calcula group_key desde meta.host.
9. Se consultan reglas activas.
10. Cada Rule se compara con el Event.
11. Si no coincide, se salta con continue.
12. Si coincide, se aplican throttle, anti-duplicado y threshold.
13. Si todo se cumple, se crea Alert.
14. Se ejecuta db.commit().
15. La alerta queda disponible para consulta.
```

---

## 3️⃣2️⃣ Diagrama técnico global

```text
POST /rules
    ↓
RuleCreate
    ↓
Rule
    ↓
rules table
    ↓
POST /ingest
    ↓
IngestPayload
    ↓
Event
    ↓
events table
    ↓
select active Rule
    ↓
match source/severity/contains/meta
    ↓
throttle / anti-duplicado / threshold
    ↓
Alert
    ↓
alerts table
```

---

## 3️⃣3️⃣ Relación con endpoints del laboratorio

La relación entre endpoints es:

```text
POST /rules
    ↓
crea reglas

GET /rules
    ↓
permite revisar reglas creadas

POST /ingest
    ↓
usa reglas activas para evaluar eventos

GET /events
    ↓
permite revisar eventos recibidos

GET /alerts
    ↓
permite revisar alertas generadas

GET /metrics
    ↓
resume eventos, reglas y alertas
```

El motor de reglas no es una ruta aislada. Es una lógica transversal que conecta varias partes del backend.

---

## 3️⃣4️⃣ Ejemplo práctico completo

### 1. Crear regla

```bash
curl -X POST http://localhost:8000/rules \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Failed login auth",
    "enabled": true,
    "source": "auth",
    "severity_min": 3,
    "contains": "failed login",
    "meta_match": {
      "user": "admin"
    }
  }'
```

Esta regla significa:

```text
Detectar eventos de origen auth,
con severidad mínima 3,
cuyo mensaje contenga failed login,
y cuyo meta.user sea admin.
```

---

### 2. Enviar evento coincidente

```bash
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "source": "auth",
    "severity": 4,
    "message": "Failed login attempt for user admin",
    "meta": {
      "host": "server-01",
      "user": "admin"
    }
  }'
```

Este evento coincide porque:

```text
source = auth              → coincide
severity = 4 >= 3          → coincide
message contiene failed login → coincide
meta.user = admin          → coincide
```

Resultado esperado:

```text
se crea Event
se evalúa Rule
se crea Alert
```

---

### 3. Consultar alertas

```bash
curl http://localhost:8000/alerts
```

Debería aparecer una alerta relacionada con la regla creada.

---

## 3️⃣5️⃣ Puntos importantes

### Las reglas se configuran antes de ingestar eventos

Si no hay reglas creadas, `/ingest` guardará eventos, pero no generará alertas.

---

### Solo se evalúan reglas activas

Una regla con:

```text
enabled = false
```

no participa en la evaluación.

---

### Una regla puede coincidir con muchos eventos

Cada vez que llega un evento, se vuelve a evaluar contra las reglas activas.

---

### Un evento puede activar varias reglas

Si varias reglas coinciden con el mismo evento, pueden generarse varias alertas.

---

### `group_key` es clave para lógica avanzada

Sin `group_key`, no se aplican correctamente:

```text
throttle
anti-duplicado
threshold
```

Por eso es importante enviar eventos con:

```json
{
  "meta": {
    "host": "..."
  }
}
```

---

### Threshold requiere eventos acumulados

Una regla con threshold no tiene por qué generar alerta con el primer evento.

Necesita alcanzar el número configurado dentro de la ventana temporal.

---

### El anti-duplicado depende del estado de la alerta

Si ya hay una alerta:

```text
open
```

o:

```text
ack
```

para la misma regla y grupo, no se crea otra.

Si la alerta está:

```text
closed
```

sí puede generarse una nueva.

---

## 3️⃣6️⃣ Comandos útiles relacionados

Listar reglas:

```bash
curl http://localhost:8000/rules
```

Crear regla simple:

```bash
curl -X POST http://localhost:8000/rules \
  -H "Content-Type: application/json" \
  -d '{
    "name": "High severity events",
    "enabled": true,
    "severity_min": 5
  }'
```

Enviar evento de prueba:

```bash
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "source": "auth",
    "severity": 5,
    "message": "High severity authentication event",
    "meta": {
      "host": "server-01"
    }
  }'
```

Consultar eventos:

```bash
curl http://localhost:8000/events
```

Consultar alertas:

```bash
curl http://localhost:8000/alerts
```

Consultar métricas:

```bash
curl http://localhost:8000/metrics
```

Consultar reglas en PostgreSQL:

```bash
docker exec -it siem-db psql -U siem -d siem -c "SELECT id, name, enabled, source, severity_min, contains, throttle_seconds, threshold_count, threshold_seconds, meta_match FROM rules ORDER BY id DESC;"
```

Consultar eventos recientes:

```bash
docker exec -it siem-db psql -U siem -d siem -c "SELECT id, source, severity, message, meta, created_at FROM events ORDER BY id DESC LIMIT 10;"
```

Consultar alertas recientes:

```bash
docker exec -it siem-db psql -U siem -d siem -c "SELECT id, rule_id, event_id, title, group_key, status, created_at FROM alerts ORDER BY id DESC LIMIT 10;"
```

Consultar alertas con JOIN:

```bash
docker exec -it siem-db psql -U siem -d siem -c "SELECT a.id, a.title, a.status, r.name AS rule_name, e.source, e.severity, e.message FROM alerts a JOIN rules r ON a.rule_id = r.id JOIN events e ON a.event_id = e.id ORDER BY a.id DESC LIMIT 10;"
```

---

## 3️⃣7️⃣ Resumen técnico

El motor de reglas permite transformar eventos almacenados en alertas operativas.

La creación de reglas se realiza mediante `POST /rules`, donde el payload se valida con `RuleCreate` y se guarda como modelo `Rule` en PostgreSQL.

Durante la ingesta, `POST /ingest` crea un evento `Event`, consulta las reglas activas y evalúa criterios como `source`, `severity_min`, `contains` y `meta_match`.

Si la regla coincide, el sistema aplica controles adicionales como throttle, anti-duplicado y threshold. Si todos los criterios se cumplen, se crea una alerta `Alert` vinculada al evento y a la regla.

La relación final es:

```text
Rule + Event → Alert
```

Esta es una de las partes más importantes del laboratorio, porque convierte el proyecto de un simple almacén de eventos en un sistema básico de detección.