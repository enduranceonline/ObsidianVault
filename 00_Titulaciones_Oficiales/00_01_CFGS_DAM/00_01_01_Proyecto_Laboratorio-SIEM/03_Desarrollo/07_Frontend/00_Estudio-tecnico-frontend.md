#html #css #javascript #frontend #api #fastapi #swagger #SIEM #SOC

## 1️⃣ Objetivo de la nota

Esta nota resume el papel del frontend dentro del laboratorio SIEM MVP.

El objetivo es entender cómo la interfaz web consume la API del backend, cómo muestra las alertas generadas por el sistema, cómo permite aplicar filtros, navegar entre páginas y actualizar el estado de una alerta.

El análisis detallado línea por línea se desarrolla en la carpeta:

```text
08_Analisis-tecnico-frontend/
```

---

## 2️⃣ Archivos relacionados

Los archivos principales del frontend son:

```text
frontend/index.html
frontend/alert.html
frontend/assets/app.js
frontend/assets/alerts.js
frontend/assets/alert_detail.js
frontend/assets/styles.css
```

Cada archivo cumple una función concreta:

```text
index.html
    ↓
estructura de la página principal de alertas

alert.html
    ↓
estructura de la página de detalle de una alerta

app.js
    ↓
funciones comunes reutilizables

alerts.js
    ↓
lógica de listado, filtros y paginación

alert_detail.js
    ↓
lógica de detalle y cambio de estado

styles.css
    ↓
diseño visual de la interfaz
```

---

## 3️⃣ Papel del frontend dentro del proyecto

El frontend permite interactuar con el laboratorio desde una interfaz web sencilla.

Hasta ahora, muchos flujos podían probarse desde:

```text
curl
Swagger
Adminer
psql
```

Pero el frontend permite visualizar y gestionar alertas de forma más cercana a una herramienta SOC.

La relación general es:

```text
Backend FastAPI
        ↓
Endpoints REST
        ↓
JavaScript fetch()
        ↓
HTML dinámico
        ↓
Usuario visualiza y gestiona alertas
```

---

## 4️⃣ Estructura general del frontend

La carpeta frontend tiene esta estructura:

```text
frontend/
├── index.html
├── alert.html
└── assets/
    ├── app.js
    ├── alerts.js
    ├── alert_detail.js
    └── styles.css
```

La separación es clara:

```text
HTML
    ↓
define la estructura de las páginas

CSS
    ↓
define el aspecto visual

JavaScript
    ↓
conecta la página con la API y actualiza el DOM
```

Esta separación ayuda a mantener el proyecto más ordenado.

---

## 5️⃣ Página principal: `index.html`

El archivo:

```text
frontend/index.html
```

define la página principal de alertas.

Su título visible es:

```text
Alertas
```

Y su subtítulo indica:

```text
Vista principal — listado, filtros y paginación
```

Esta página contiene:

```text
- Cabecera superior.
- Botón de actualizar.
- Formulario de filtros.
- Tabla de alertas.
- Botones de paginación.
- Cajas de error e información.
```

La tabla muestra columnas como:

```text
ID
Estado
Severidad
group_key
Título
rule_id
event_id
created_at
acción Ver
```

---

## 6️⃣ Página de detalle: `alert.html`

El archivo:

```text
frontend/alert.html
```

define la página de detalle de una alerta concreta.

Esta página se abre desde la tabla principal mediante enlaces como:

```text
alert.html?id=1
```

Contiene:

```text
- Cabecera de detalle.
- Botón para volver al listado.
- Título de la alerta.
- Subtítulo con estado y group_key.
- Botones ACK, CLOSE y REOPEN.
- Panel con datos clave de la alerta.
- Panel de notas.
```

Esta página permite cambiar el estado de una alerta.

Los estados gestionados son:

```text
open
ack
closed
```

---

## 7️⃣ Archivo común: `app.js`

El archivo:

```text
frontend/assets/app.js
```

contiene funciones comunes usadas por las demás páginas.

Funciones principales:

```text
API_BASE
qs()
show()
hide()
fmtDate()
statusBadgeClass()
apiFetch()
getQueryParam()
setQueryParams()
```

Este archivo actúa como una pequeña librería interna del frontend.

Su función más importante es:

```text
apiFetch()
```

porque centraliza las llamadas HTTP al backend.

La constante:

```javascript
const API_BASE = "http://localhost:8000";
```

indica que el frontend espera encontrar el backend en:

```text
http://localhost:8000
```

---

## 8️⃣ Lógica del listado: `alerts.js`

El archivo:

```text
frontend/assets/alerts.js
```

controla la página principal `index.html`.

Gestiona:

```text
- Estado de filtros.
- Lectura de parámetros desde la URL.
- Sincronización del formulario.
- Actualización de la URL.
- Petición a GET /alerts.
- Renderizado de filas en la tabla.
- Botones Prev y Next.
- Botón Actualizar.
- Botón Limpiar.
```

El estado principal se guarda en el objeto:

```javascript
let state = {
  limit: 50,
  offset: 0,
  status: "",
  group_key: "",
};
```

Este objeto representa los filtros actuales de la página.

---

## 9️⃣ Lógica del detalle: `alert_detail.js`

El archivo:

```text
frontend/assets/alert_detail.js
```

controla la página `alert.html`.

Gestiona:

```text
- Lectura del parámetro id desde la URL.
- Carga de la alerta concreta.
- Renderizado de datos en la página.
- Activación o desactivación de botones según estado.
- Cambio de estado mediante PATCH /alerts/{id}.
```

El flujo principal es:

```text
alert.html?id=1
        ↓
getQueryParam("id")
        ↓
GET /alerts/1
        ↓
renderAlert()
        ↓
botones ACK / CLOSE / REOPEN
        ↓
PATCH /alerts/1
```

---

## 🔟 Estilos visuales: `styles.css`

El archivo:

```text
frontend/assets/styles.css
```

define el diseño visual de la interfaz.

Incluye estilos para:

```text
body
topbar
container
brand
logo
cards
forms
buttons
alerts
tables
badges
grid
panels
responsive design
```

El diseño usa variables CSS en `:root`:

```css
:root {
  --bg: #0b1020;
  --card: #111836;
  --card2: #0f1530;
  --text: #e7ecff;
  --muted: #a7b0d6;
  --border: rgba(255,255,255,0.12);
  --border2: rgba(255,255,255,0.08);
  --shadow: 0 10px 30px rgba(0,0,0,0.35);
  --radius: 14px;
}
```

Esto permite mantener una estética consistente en toda la interfaz.

---

## 1️⃣1️⃣ Relación entre HTML y JavaScript

El frontend funciona porque el HTML define elementos con `id`, y JavaScript los selecciona para leer o modificar contenido.

Ejemplo en `index.html`:

```html
<tbody id="alertsTbody">
```

En `alerts.js` se usa:

```javascript
const tb = qs("alertsTbody");
```

Otro ejemplo:

```html
<button id="btnRefresh" class="btn">Actualizar</button>
```

En JavaScript:

```javascript
qs("btnRefresh").addEventListener("click", () => loadAlerts());
```

La relación es:

```text
HTML id
    ↓
qs(id)
    ↓
JavaScript modifica o escucha eventos
```

---

## 1️⃣2️⃣ Relación entre frontend y backend

El frontend consume el backend mediante llamadas HTTP.

La función central es:

```javascript
apiFetch(path, { method = "GET", query = null, body = null } = {})
```

Esta función construye una URL usando:

```javascript
API_BASE + path
```

Por ejemplo:

```javascript
apiFetch("/alerts")
```

llama a:

```text
http://localhost:8000/alerts
```

Y:

```javascript
apiFetch(`/alerts/${alertId}`, {
  method: "PATCH",
  body: { status: nextStatus }
})
```

llama a:

```text
PATCH http://localhost:8000/alerts/{id}
```

---

## 1️⃣3️⃣ Endpoints usados por el frontend

Según el código mostrado, el frontend utiliza principalmente estos endpoints:

```text
GET /alerts
GET /alerts/{alert_id}
PATCH /alerts/{alert_id}
```

En la versión actual del frontend, el listado principal consulta:

```javascript
apiFetch("/alerts", ...)
```

y no:

```text
GET /alerts/ui
```

Esto explica por qué en `index.html` aparece una nota indicando que la severidad no existe en `AlertOut`.

La tabla deja severidad como:

```text
—
```

para no inventar un dato que no viene en la respuesta básica.

---

## 1️⃣4️⃣ Punto importante: `/alerts` frente a `/alerts/ui`

En backend existen dos tipos de endpoints:

```text
/alerts
    ↓
devuelve AlertOut básico

/alerts/ui
    ↓
devuelve AlertUIOut enriquecido
```

Sin embargo, el frontend actual usa:

```text
GET /alerts
```

Por eso la página principal solo tiene acceso a:

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

No tiene acceso directo a:

```text
rule_name
event_source
event_severity
event_message
```

Esto es una decisión importante del estado actual del proyecto.

Para mostrar severidad real en la tabla, habría que modificar `alerts.js` para consumir:

```text
GET /alerts/ui
```

---

## 1️⃣5️⃣ Listado de alertas

El listado se carga en `alerts.js` mediante:

```javascript
const data = await apiFetch("/alerts", {
  query: {
    limit: state.limit,
    offset: state.offset,
    status: state.status || null,
    group_key: state.group_key || null,
  }
});
```

Esto envía filtros al backend:

```text
limit
offset
status
group_key
```

Ejemplo:

```text
GET /alerts?limit=50&offset=0&status=open&group_key=server-01
```

Después se llama a:

```javascript
renderRows(data);
```

para pintar la tabla.

---

## 1️⃣6️⃣ Renderizado dinámico de la tabla

La función:

```javascript
renderRows(alerts)
```

recibe una lista de alertas y genera filas HTML dinámicamente.

Si no hay resultados, muestra:

```text
Sin resultados
```

Si hay resultados, crea una fila por alerta con:

```text
id
status
severidad placeholder
group_key
title
rule_id
event_id
created_at
link Ver
```

El enlace de detalle se genera así:

```javascript
<a class="btn" href="./alert.html?id=${encodeURIComponent(a.id)}">Ver</a>
```

Esto conecta el listado con la página de detalle.

---

## 1️⃣7️⃣ Prevención básica de inyección HTML

En `alerts.js`, el título de la alerta se pinta usando:

```javascript
escapeHtml(a.title)
```

La función `escapeHtml` reemplaza caracteres especiales como:

```text
&
<
>
"
'
```

Esto evita insertar directamente HTML potencialmente peligroso en la tabla.

Es una buena práctica, especialmente porque `title` viene de datos almacenados y podría contener caracteres especiales.

---

## 1️⃣8️⃣ Paginación

La paginación se basa en dos valores:

```text
limit
offset
```

`limit` indica cuántos resultados se cargan.

`offset` indica desde qué posición empezar.

Botón `Prev`:

```javascript
state.offset = Math.max(0, state.offset - state.limit);
```

Botón `Next`:

```javascript
state.offset = state.offset + state.limit;
```

El backend recibe estos valores y aplica:

```text
limit
offset
```

en la consulta.

---

## 1️⃣9️⃣ Sincronización con la URL

El frontend guarda los filtros en la URL.

Ejemplo:

```text
index.html?limit=50&offset=0&status=open&group_key=server-01
```

Esto se gestiona con:

```javascript
readStateFromUrl()
syncUrl()
setQueryParams()
```

Ventaja:

```text
- Se puede recargar la página sin perder filtros.
- Se puede compartir una URL filtrada.
- El estado visual queda reflejado en la barra de direcciones.
```

---

## 2️⃣0️⃣ Detalle de alerta

La página `alert.html` carga una alerta concreta.

Primero lee el parámetro:

```javascript
alertId = getQueryParam("id");
```

Si no existe, muestra error:

```text
Falta parámetro ?id= en la URL.
```

Si existe, llama a:

```javascript
apiFetch(`/alerts/${alertId}`)
```

Esto consulta:

```text
GET /alerts/{alert_id}
```

Después renderiza los campos con:

```javascript
renderAlert(a)
```

---

## 2️⃣1️⃣ Gestión de botones según estado

La función:

```javascript
setButtonsForStatus(status)
```

activa o desactiva botones según el estado actual.

Reglas:

```text
open
    ↓
puedes ACK o CLOSE

ack
    ↓
puedes CLOSE o REOPEN

closed
    ↓
puedes REOPEN
```

En código:

```javascript
btnAck.disabled = (status !== "open");
btnClose.disabled = (status === "closed");
btnReopen.disabled = (status !== "ack" && status !== "closed");
```

Esto evita acciones incoherentes desde la interfaz.

---

## 2️⃣2️⃣ Actualización de estado

El cambio de estado se realiza con:

```javascript
updateStatus(nextStatus)
```

Esta función llama a:

```javascript
apiFetch(`/alerts/${alertId}`, {
  method: "PATCH",
  body: { status: nextStatus }
});
```

Ejemplos:

```text
ACK    → status = ack
CLOSE  → status = closed
REOPEN → status = open
```

El backend valida que el estado sea uno de:

```text
open
ack
closed
```

---

## 2️⃣3️⃣ Relación con el flujo SOC

El frontend representa visualmente un flujo SOC básico:

```text
Nueva alerta
    ↓
open

Analista la reconoce
    ↓
ack

Analista la cierra
    ↓
closed

Si se quiere reabrir
    ↓
open
```

Este flujo está implementado en:

```text
alert_detail.js
```

y se comunica con:

```text
PATCH /alerts/{alert_id}
```

---

## 2️⃣4️⃣ Relación con las notas anteriores

El frontend depende de todo lo estudiado antes:

```text
Docker
    ↓
levanta backend y base de datos

FastAPI
    ↓
expone endpoints

Base de datos
    ↓
guarda events, rules y alerts

Motor de reglas
    ↓
genera alertas

Gestión de alertas
    ↓
permite consultarlas y actualizarlas

Frontend
    ↓
permite interactuar visualmente con esas alertas
```

Por tanto, este módulo es la capa visible del laboratorio.

---

## 2️⃣5️⃣ Limitaciones actuales del frontend

El frontend actual es funcional, pero tiene varias limitaciones normales para un MVP.

### No usa `/alerts/ui`

El listado principal usa:

```text
GET /alerts
```

Por eso no muestra datos enriquecidos como severidad real, nombre de regla o mensaje del evento.

### No muestra detalle del evento asociado

En `alert.html`, las notas indican que los eventos asociados no están en `AlertOut`.

Esto podría mejorarse usando:

```text
GET /alerts/{alert_id}/ui
```

### No hay dashboard de métricas

Aunque existe el endpoint:

```text
GET /metrics
```

el frontend actual no lo consume.

### No hay gestión visual de reglas

Aunque existe:

```text
POST /rules
GET /rules
```

el frontend actual está centrado en alertas.

### No hay vista de eventos

Aunque existe:

```text
GET /events
```

el frontend actual no incluye una tabla específica de eventos.

Estas limitaciones son normales y no invalidan el proyecto. De hecho, dejan claro que el MVP se centra en el flujo principal de alertas.

---

## 2️⃣6️⃣ Posibles mejoras futuras

Mejoras razonables para una evolución posterior:

```text
- Cambiar el listado para consumir /alerts/ui.
- Mostrar severidad real del evento.
- Mostrar nombre de la regla en la tabla.
- Mostrar mensaje del evento en el detalle.
- Añadir dashboard con /metrics.
- Añadir vista de eventos.
- Añadir vista de reglas.
- Añadir formulario visual para crear reglas.
- Añadir filtros por source, severity_min y q usando /alerts/ui.
```

Estas mejoras no son necesarias para entender el MVP actual, pero son una evolución lógica.

---

## 2️⃣7️⃣ Decisiones técnicas importantes

### Frontend sin framework

El frontend usa HTML, CSS y JavaScript puro.

No usa:

```text
React
Vue
Angular
Vite
Webpack
```

Esto simplifica mucho la entrega y la ejecución.

---

### API centralizada en `app.js`

Todas las llamadas HTTP pasan por:

```javascript
apiFetch()
```

Esto evita repetir lógica de fetch, headers, JSON y errores.

---

### Estado simple en objeto JavaScript

El listado usa:

```javascript
let state = {...}
```

Esto es suficiente para un MVP.

No hace falta una librería de estado.

---

### Renderizado manual del DOM

El frontend modifica el DOM directamente usando:

```javascript
document.getElementById()
innerHTML
appendChild()
textContent
```

Es una implementación sencilla y transparente.

---

### CSS centralizado

Todo el estilo está en:

```text
styles.css
```

Esto mantiene el diseño separado de la lógica JavaScript.

---

## 2️⃣8️⃣ Flujo técnico completo del frontend

```text
Usuario abre index.html
        ↓
alerts.js ejecuta init()
        ↓
lee filtros de la URL
        ↓
llama a GET /alerts
        ↓
renderiza filas
        ↓
usuario pulsa Ver
        ↓
abre alert.html?id=X
        ↓
alert_detail.js ejecuta init()
        ↓
llama a GET /alerts/X
        ↓
renderiza detalle
        ↓
usuario pulsa ACK/CLOSE/REOPEN
        ↓
PATCH /alerts/X
        ↓
actualiza la vista
```

---

## 2️⃣9️⃣ Comandos útiles relacionados

Servir el frontend con Python desde la carpeta `frontend`:

```bash
cd ~/siem-lab/frontend
python3 -m http.server 5173
```

Abrir la página principal:

```text
http://localhost:5173/index.html
```

Abrir detalle de alerta:

```text
http://localhost:5173/alert.html?id=1
```

Probar backend directamente:

```bash
curl http://localhost:8000/alerts
```

Probar actualización de estado:

```bash
curl -X PATCH http://localhost:8000/alerts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "ack"
  }'
```

Ver Swagger:

```text
http://localhost:8000/docs
```

---

## 3️⃣0️⃣ Notas detalladas relacionadas

Las notas detalladas del módulo se organizarán así:

```text
08_Analisis-tecnico-frontend/
├── 01_index-html
├── 02_alert-html
├── 03_app-js
├── 04_alerts-js
├── 05_alert-detail-js
└── 06_styles-css
```

Orden recomendado:

```text
1. 01_index-html
2. 02_alert-html
3. 03_app-js
4. 04_alerts-js
5. 05_alert-detail-js
6. 06_styles-css
```

Primero se entiende la estructura HTML.

Después se estudian las funciones comunes.

Luego se analiza la lógica específica de listado y detalle.

Finalmente se revisa el estilo visual.