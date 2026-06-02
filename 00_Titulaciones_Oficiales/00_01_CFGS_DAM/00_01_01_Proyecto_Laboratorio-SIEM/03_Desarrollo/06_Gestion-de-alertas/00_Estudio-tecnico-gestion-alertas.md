#python #api #fastapi #swagger #pydantic #PostgreSQL #SQLAlchemy #backend #SIEM #SOC

## 1️⃣ Objetivo de la nota

Esta nota resume el papel del módulo de gestión de alertas dentro del laboratorio SIEM MVP.

El objetivo es entender cómo se consultan las alertas generadas, cómo se enriquecen con información de reglas y eventos, cómo se filtran desde la API y cómo se actualiza su estado dentro de un flujo básico tipo SOC.

El análisis detallado línea por línea se desarrolla en la carpeta:

```text
07_Analisis-tecnico-gestion-alertas/
```

---

## 2️⃣ Archivos relacionados

Los archivos principales de este módulo son:

```text
backend/app/api/routes/alerts.py
backend/app/schemas/alert.py
backend/app/models/alert.py
backend/app/models/rule.py
backend/app/models/event.py
```

También se relacionan con módulos ya estudiados:

```text
backend/app/api/routes/ingest.py
backend/app/api/routes/rules.py
backend/app/api/routes/events.py
```

Relación principal:

```text
ingest.py
    ↓
genera Alert

models/alert.py
    ↓
define la tabla alerts

schemas/alert.py
    ↓
define respuestas y actualizaciones

routes/alerts.py
    ↓
permite consultar y actualizar alertas
```

---

## 3️⃣ Papel de las alertas dentro del proyecto

Las alertas son el resultado principal del laboratorio desde el punto de vista de un analista SOC.

Un evento por sí solo es un dato registrado.

Una regla define una condición de detección.

Una alerta aparece cuando un evento cumple una regla.

La relación general es:

```text
Event
   ↓
se evalúa contra
Rule
   ↓
si coincide
Alert
```

Por tanto, la alerta representa una detección que puede ser revisada posteriormente.

---

## 4️⃣ Flujo general de alertas

El flujo completo puede dividirse en cuatro fases:

```text
1. Creación automática de alertas durante la ingesta.
2. Consulta de alertas.
3. Consulta enriquecida para interfaz.
4. Actualización del estado de la alerta.
```

---

### Fase 1: creación automática

La alerta se crea en:

```text
backend/app/api/routes/ingest.py
```

Cuando una regla coincide con un evento, se crea un objeto `Alert`:

```python
alert = Alert(
    rule_id=rule.id,
    event_id=ev.id,
    title=f"Rule matched: {rule.name}",
    group_key=group_key,
)
```

Esto conecta la alerta con:

```text
rule_id  → regla que generó la alerta
event_id → evento que disparó la alerta
```

---

### Fase 2: consulta de alertas básicas

La consulta básica se realiza con:

```text
GET /alerts
```

Este endpoint devuelve una lista de alertas usando el schema:

```text
AlertOut
```

Permite filtros como:

```text
limit
offset
status
group_key
rule_id
```

---

### Fase 3: consulta enriquecida para UI

La consulta enriquecida se realiza con:

```text
GET /alerts/ui
```

Este endpoint no devuelve solo los datos de la alerta, sino también información útil para mostrar en una interfaz:

```text
rule_name
event_ts
event_source
event_severity
event_message
```

Esto evita que el frontend tenga que hacer varias consultas separadas para reconstruir el contexto de una alerta.

---

### Fase 4: actualización de estado

La actualización se realiza con:

```text
PATCH /alerts/{alert_id}
```

Permite cambiar el estado de una alerta.

Los estados permitidos son:

```text
open
ack
closed
```

Este flujo representa una gestión básica tipo SOC:

```text
open   → alerta nueva
ack    → alerta reconocida
closed → alerta cerrada
```

---

## 5️⃣ Endpoints del módulo de alertas

El archivo:

```text
backend/app/api/routes/alerts.py
```

define varios endpoints:

```text
GET   /alerts
GET   /alerts/ui
GET   /alerts/ui/count
GET   /alerts/{alert_id}
GET   /alerts/{alert_id}/ui
PATCH /alerts/{alert_id}
```

---

### `GET /alerts`

Devuelve alertas básicas.

Usa:

```text
AlertOut
```

Permite filtrar por:

```text
status
group_key
rule_id
```

Es útil para obtener alertas sin información adicional de reglas o eventos.

---

### `GET /alerts/ui`

Devuelve alertas enriquecidas para frontend.

Usa:

```text
AlertUIOut
```

Este endpoint hace joins con:

```text
rules
events
```

para añadir información contextual.

Campos adicionales:

```text
rule_name
event_ts
event_source
event_severity
event_message
```

---

### `GET /alerts/ui/count`

Devuelve el número total de alertas que cumplen los filtros de la UI.

Sirve para paginación o contadores en la interfaz.

Devuelve un entero:

```text
int
```

---

### `GET /alerts/{alert_id}`

Devuelve una alerta concreta por su ID.

Usa:

```text
AlertOut
```

Si la alerta no existe, devuelve:

```text
404 Alert not found
```

---

### `GET /alerts/{alert_id}/ui`

Devuelve una alerta concreta enriquecida con información de regla y evento.

Usa:

```text
AlertUIOut
```

Es útil para una pantalla de detalle de alerta.

---

### `PATCH /alerts/{alert_id}`

Actualiza el estado de una alerta.

Usa como entrada:

```text
AlertUpdate
```

Y devuelve:

```text
AlertOut
```

Permite cambiar el estado a:

```text
open
ack
closed
```

---

## 6️⃣ Schemas de alertas

El archivo:

```text
backend/app/schemas/alert.py
```

define los schemas principales de este módulo:

```text
AlertStatus
AlertOut
AlertUIOut
AlertUpdate
```

---

### `AlertStatus`

Define los estados permitidos de una alerta:

```python
AlertStatus = Literal["open", "ack", "closed"]
```

Esto limita los valores válidos a:

```text
open
ack
closed
```

Así se evita que una alerta tenga estados arbitrarios como:

```text
pending
resolved
invalid
```

---

### `AlertOut`

Define la respuesta básica de una alerta.

Campos:

```text
id
rule_id
event_id
title
group_key
status
created_at
updated_at
```

Este schema representa directamente los datos principales del modelo `Alert`.

---

### `AlertUIOut`

Extiende `AlertOut` y añade campos preparados para interfaz:

```text
rule_name
event_ts
event_source
event_severity
event_message
```

Esto permite que una alerta llegue al frontend con contexto suficiente para ser entendida rápidamente.

---

### `AlertUpdate`

Define qué puede modificarse en una alerta.

En este MVP solo permite cambiar:

```text
status
```

Esto es coherente con un flujo SOC básico, donde el analista cambia el estado de la alerta pero no modifica directamente el evento o la regla original.

---

## 7️⃣ Modelo `Alert`

El modelo `Alert` se encuentra en:

```text
backend/app/models/alert.py
```

Representa la tabla:

```text
alerts
```

Campos principales:

```text
id
rule_id
event_id
title
group_key
status
created_at
updated_at
```

Relaciones:

```text
Alert.rule  → Rule
Alert.event → Event
```

También incluye claves foráneas:

```text
alerts.rule_id  → rules.id
alerts.event_id → events.id
```

Esto garantiza que cada alerta esté vinculada a una regla y a un evento.

---

## 8️⃣ Consulta básica de alertas

El endpoint básico es:

```text
GET /alerts
```

Construye una consulta sobre el modelo `Alert`:

```text
select(Alert)
```

Ordena por fecha de creación descendente:

```text
Alert.created_at.desc()
```

Y aplica:

```text
limit
offset
```

Esto permite obtener alertas recientes y paginar resultados.

Filtros disponibles:

```text
status
group_key
rule_id
```

Ejemplo:

```text
GET /alerts?status=open
```

Devuelve alertas abiertas.

Ejemplo:

```text
GET /alerts?group_key=server-01
```

Devuelve alertas asociadas a un grupo concreto.

---

## 9️⃣ Consulta enriquecida para UI

El endpoint:

```text
GET /alerts/ui
```

es más completo.

No consulta únicamente `Alert`, sino que también une las tablas:

```text
rules
events
```

La consulta selecciona:

```text
Alert
Rule.name
Event.ts
Event.source
Event.severity
Event.message
```

Esto permite construir una respuesta enriquecida.

La relación es:

```text
alerts
   ↓ join rule_id
rules
   ↓ join event_id
events
```

Resultado conceptual:

```text
Alert
├── datos propios
├── nombre de la regla
└── datos principales del evento
```

---

## 🔟 Filtros de UI

El archivo define una función auxiliar:

```text
_apply_ui_filters
```

Esta función centraliza los filtros usados por:

```text
GET /alerts/ui
GET /alerts/ui/count
```

Filtros soportados:

```text
status
group_key
rule_id
severity_min
severity_max
source
q
```

Esto evita duplicar la misma lógica de filtros en varios endpoints.

---

### Filtro por `status`

Permite consultar alertas por estado:

```text
open
ack
closed
```

Ejemplo:

```text
GET /alerts/ui?status=open
```

---

### Filtro por `group_key`

Permite consultar alertas de un grupo concreto.

Ejemplo:

```text
GET /alerts/ui?group_key=server-01
```

---

### Filtro por `rule_id`

Permite consultar alertas generadas por una regla concreta.

Ejemplo:

```text
GET /alerts/ui?rule_id=3
```

---

### Filtro por severidad

Permite filtrar según la severidad del evento asociado:

```text
severity_min
severity_max
```

Ejemplo:

```text
GET /alerts/ui?severity_min=4
```

Este filtro no pertenece directamente a la alerta, sino al evento relacionado.

Por eso requiere join con `Event`.

---

### Filtro por `source`

Permite filtrar por origen del evento.

El código usa comparación case-insensitive:

```text
func.lower(Event.source) == source.lower()
```

Esto permite que `AUTH` y `auth` se traten igual.

---

### Filtro por `q`

Permite buscar texto en:

```text
Alert.title
Event.message
```

Esto es útil para búsquedas generales desde la UI.

---

## 1️⃣1️⃣ Conteo para UI

El endpoint:

```text
GET /alerts/ui/count
```

devuelve cuántas alertas cumplen los filtros.

Es importante porque permite implementar paginación en frontend.

Por ejemplo:

```text
GET /alerts/ui?limit=50&offset=0
GET /alerts/ui/count
```

La primera llamada obtiene la página de datos.

La segunda obtiene el total filtrado.

Esto permite mostrar algo como:

```text
Mostrando 50 de 237 alertas
```

---

## 1️⃣2️⃣ Consulta de una alerta concreta

El endpoint básico:

```text
GET /alerts/{alert_id}
```

usa:

```text
db.get(Alert, alert_id)
```

Esto busca una alerta por clave primaria.

Si existe, la devuelve como `AlertOut`.

Si no existe, devuelve:

```text
404 Alert not found
```

---

## 1️⃣3️⃣ Consulta enriquecida de una alerta concreta

El endpoint:

```text
GET /alerts/{alert_id}/ui
```

devuelve una alerta concreta con contexto adicional.

Hace join con:

```text
Rule
Event
```

y devuelve:

```text
AlertUIOut
```

Esto es útil para una pantalla de detalle donde se quiere ver:

```text
- título de la alerta
- estado
- regla asociada
- origen del evento
- severidad del evento
- mensaje del evento
```

---

## 1️⃣4️⃣ Actualización de estado

El endpoint:

```text
PATCH /alerts/{alert_id}
```

permite cambiar el estado de una alerta.

Flujo:

```text
1. Busca la alerta por ID.
2. Si no existe, devuelve 404.
3. Asigna alert.status = payload.status.
4. Añade el objeto a la sesión.
5. Ejecuta commit.
6. Refresca la alerta.
7. Devuelve AlertOut.
```

Esto permite gestionar el ciclo de vida de la alerta.

---

## 1️⃣5️⃣ Ciclo de vida SOC

Los estados definidos son:

```text
open
ack
closed
```

Interpretación:

```text
open
    ↓
alerta nueva pendiente de revisar

ack
    ↓
alerta reconocida o en análisis

closed
    ↓
alerta cerrada, resuelta o descartada
```

Flujo conceptual:

```text
open → ack → closed
```

Este ciclo de vida es simple, pero suficiente para un MVP orientado a lógica SOC.

---

## 1️⃣6️⃣ Relación con el anti-duplicado

El estado de la alerta no solo sirve para la UI.

También afecta al motor de reglas.

En `ingest.py`, el anti-duplicado busca alertas con estado:

```text
open
ack
```

Si ya existe una alerta abierta o reconocida para la misma regla y grupo, no se crea otra.

Por tanto:

```text
open / ack
    ↓
bloquean duplicados

closed
    ↓
permite generar nuevas alertas
```

Esto significa que cerrar una alerta puede permitir que el sistema vuelva a generar otra alerta si vuelve a ocurrir el patrón.

---

## 1️⃣7️⃣ Relación con métricas

El módulo de métricas usa la tabla `alerts` para devolver información agregada:

```text
alerts_total
alerts_by_status
alerts_by_group_key_top
```

Por tanto, el estado de las alertas impacta directamente en las métricas del sistema.

Ejemplo:

```text
open: 5
ack: 2
closed: 10
```

Esto permite tener una visión general del estado operativo del laboratorio.

---

## 1️⃣8️⃣ Relación con frontend

Aunque esta nota analiza el backend, el módulo de alertas está claramente preparado para frontend.

Esto se observa en endpoints como:

```text
GET /alerts/ui
GET /alerts/ui/count
GET /alerts/{alert_id}/ui
```

Estos endpoints no son estrictamente necesarios para una API mínima, pero facilitan mucho la construcción de una interfaz.

La idea es que el frontend reciba ya los datos preparados:

```text
alerta + regla + evento
```

sin tener que hacer múltiples llamadas.

---

## 1️⃣9️⃣ Relación con el flujo general del SIEM

La gestión de alertas se sitúa al final del flujo principal:

```text
POST /rules
    ↓
crea reglas

POST /ingest
    ↓
recibe eventos

Rule + Event
    ↓
genera Alert

GET /alerts
    ↓
consulta alertas

PATCH /alerts/{alert_id}
    ↓
actualiza estado
```

La alerta es el punto donde el sistema deja de ser solo almacenamiento de eventos y empieza a parecerse a una herramienta de monitorización.

---

## 2️⃣0️⃣ Puntos importantes

### Las alertas no se crean desde `alerts.py`

El archivo `alerts.py` no crea alertas nuevas.

Las alertas se crean en:

```text
ingest.py
```

cuando una regla coincide con un evento.

`alerts.py` se encarga de consultarlas y actualizarlas.

---

### `AlertOut` es la salida básica

Sirve para respuestas simples basadas solo en la tabla `alerts`.

---

### `AlertUIOut` es la salida enriquecida

Sirve para frontend porque incluye información adicional de `rules` y `events`.

---

### `AlertUpdate` solo permite cambiar estado

En este MVP, no se permite modificar título, regla, evento o `group_key` desde la API de actualización.

Solo se modifica:

```text
status
```

---

### Los filtros de UI dependen de joins

Filtros como `severity_min`, `severity_max`, `source` o `q` necesitan acceder al evento relacionado.

Por eso los endpoints UI hacen join con `Event`.

---

### La validación de severidad evita rangos incoherentes

El código comprueba:

```text
severity_min cannot be greater than severity_max
```

Si `severity_min` es mayor que `severity_max`, devuelve error 422.

---

### `updated_at` se actualiza al modificar estado

El modelo `Alert` tiene:

```text
onupdate=func.now()
```

Por tanto, cuando se actualiza el estado de una alerta, `updated_at` debería reflejar la última modificación.

---

## 2️⃣1️⃣ Notas detalladas relacionadas

Las notas detalladas del módulo se organizarán así:

```text
07_Analisis-tecnico-gestion-alertas/
├── 01_schema-alert-py
├── 02_alerts-py
└── 03_relacion-alertas-frontend-flujo-soc
```

Orden recomendado:

```text
1. 01_schema-alert-py
2. 02_alerts-py
3. 03_relacion-alertas-frontend-flujo-soc
```

La primera nota permite entender los modelos de entrada y salida.

La segunda analiza los endpoints de consulta y actualización.

La tercera une la gestión de alertas con frontend y flujo SOC.