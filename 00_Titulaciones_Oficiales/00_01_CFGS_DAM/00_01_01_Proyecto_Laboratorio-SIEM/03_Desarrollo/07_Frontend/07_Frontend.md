## Introducción

El frontend del SIEM Lab MVP se desarrolló como una interfaz web sencilla para consultar visualmente las alertas generadas por el sistema.

Su objetivo no es sustituir a Swagger ni convertirse en un dashboard avanzado, sino demostrar que la información procesada por el backend puede mostrarse de forma clara desde un navegador.

El frontend consume datos de la API y permite revisar las alertas generadas por el motor de reglas.

---

## Función del frontend

El frontend cumple una función de apoyo visual dentro del proyecto.

Permite:

```text
- Consultar alertas generadas.
- Visualizar información relevante de cada alerta.
- Aplicar filtros básicos.
- Actualizar los datos mostrados.
- Acceder al detalle de una alerta.
````

Esta interfaz ayuda a demostrar el flujo completo del sistema:

```text
evento → ingesta → regla → alerta → visualización
```

---

## Tecnologías utilizadas

El frontend se desarrolló con tecnologías web básicas:

```text
HTML
CSS
JavaScript
```

No se utilizó ningún framework frontend avanzado. Esta decisión permitió mantener el proyecto simple y evitar que la interfaz aumentara la complejidad del desarrollo.

El objetivo principal del proyecto estaba en el backend, la base de datos y el motor de reglas. Por tanto, el frontend se planteó como una capa ligera de visualización.

---

## Ubicación del frontend

El frontend se encuentra dentro de la carpeta:

```text
frontend/
```

Estructura principal:

```text
frontend/
├── index.html
├── alert.html
└── assets/
```

El archivo `index.html` actúa como pantalla principal de consulta de alertas.

El archivo `alert.html` permite consultar información detallada de una alerta concreta.

La carpeta `assets/` contiene los recursos estáticos necesarios, como archivos CSS o JavaScript.

---

## Ejecución del frontend

En esta versión, el frontend no se ejecuta dentro de Docker.

Se sirve mediante el servidor HTTP incorporado de Python:

```bash
cd ~/siem-lab
python3 -m http.server 5173 -d frontend
```

URL de acceso:

```text
http://127.0.0.1:5173/index.html
```

Esta decisión simplificó el entorno y evitó añadir un contenedor adicional solo para servir archivos estáticos.

---

## Comunicación con la API

El frontend consume información procedente de la API FastAPI.

La comunicación se realiza mediante peticiones HTTP desde JavaScript.

Flujo básico:

```text
Frontend
   ↓
API FastAPI
   ↓
PostgreSQL
   ↓
API FastAPI
   ↓
Frontend
```

El frontend no se conecta directamente a la base de datos. Todas las consultas pasan por la API.

Esta separación permite mantener una arquitectura más ordenada:

```text
Frontend → visualización
API      → lógica y acceso a datos
DB       → persistencia
```

---

## Endpoints utilizados por el frontend

El frontend utiliza principalmente los endpoints enriquecidos de alertas:

```http
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Estos endpoints se crearon porque el frontend necesitaba mostrar información combinada de la alerta y del evento asociado.

Por ejemplo:

```text
- ID de alerta
- Estado
- Título
- group_key
- Source del evento
- Severidad del evento
- Mensaje del evento
- Regla activada
- Fecha de creación
```

En lugar de duplicar todos estos datos en la tabla `alerts`, se decidió que la API generara respuestas enriquecidas para la interfaz.

---

## Listado de alertas

La pantalla principal permite mostrar un listado de alertas generadas.

Cada alerta representa una detección producida por el motor de reglas.

La información mostrada permite revisar de forma rápida:

```text
- Qué alerta se ha generado.
- Cuál es su estado.
- Qué severidad tenía el evento.
- Qué mensaje estaba asociado.
- Qué regla la generó.
```

Esto permite validar visualmente que el backend está procesando eventos y generando resultados consultables.

---

## Filtros disponibles

El frontend permite aplicar filtros para consultar las alertas de forma más precisa.

Filtros principales:

```text
status
severity_min
q
limit
offset
```

Significado:

```text
status       → filtra por estado de alerta
severity_min → filtra por severidad mínima del evento
q            → búsqueda textual
limit        → limita el número de resultados
offset       → permite paginación
```

Estos filtros ayudan a simular una revisión más realista de alertas, ya que en un entorno de monitorización no siempre interesa mostrar todos los resultados a la vez.

---

## Detalle de alerta

Además del listado general, el frontend incluye una vista de detalle.

Esta vista permite consultar una alerta concreta mediante:

```http
GET /alerts/{alert_id}/ui
```

La finalidad de esta pantalla es mostrar información más específica sobre una alerta seleccionada.

Esto permite comprobar la relación entre:

```text
- La alerta generada.
- El evento original.
- La regla que provocó la detección.
```

---

## Actualización de datos

Durante la validación final se comprobó que el frontend mostraba inicialmente las alertas existentes y que, al pulsar la opción de actualizar, aparecía la alerta generada en la última prueba.

Este comportamiento confirmó que el frontend consumía correctamente los datos de la API.

La actualización manual es suficiente para esta versión del MVP. No se implementó actualización en tiempo real porque habría añadido complejidad adicional y no era necesaria para demostrar el flujo principal.

---

## Relación con Swagger y curl

El frontend no sustituye a Swagger ni a `curl`.

Cada herramienta cumple una función diferente:

```text
Swagger → probar endpoints de forma interactiva
curl    → validar peticiones desde terminal
Frontend → visualizar resultados de forma más amigable
```

Durante el desarrollo, Swagger y `curl` fueron más útiles para probar la API. El frontend se utilizó principalmente para demostrar el resultado final desde una interfaz web.

---

## Decisiones de diseño del frontend

Las decisiones principales fueron:

```text
- Usar HTML, CSS y JavaScript.
- No utilizar frameworks avanzados.
- Servir el frontend con Python HTTP Server.
- Consumir únicamente la API, no la base de datos.
- Usar endpoints enriquecidos para simplificar la visualización.
- Mantener la interfaz como apoyo visual del MVP.
```

Estas decisiones permitieron incorporar una interfaz funcional sin desplazar el foco del proyecto.

---

## Problemas y ajustes durante el desarrollo

Durante el desarrollo apareció la necesidad de adaptar la API para que el frontend pudiera mostrar información más útil.

El endpoint básico `/alerts` no era suficiente, ya que devolvía principalmente información propia de la alerta. Para mostrar datos del evento asociado fue necesario crear endpoints enriquecidos como `/alerts/ui`.

También se detectó durante la validación que el frontend podía no mostrar inmediatamente la última alerta generada hasta actualizar la vista. Al comprobar la actualización manual, la alerta apareció correctamente, por lo que el problema no estaba en la API ni en la base de datos, sino en la necesidad de refrescar los datos mostrados.

---

## Validación del frontend

El frontend se validó comprobando que:

```text
- Cargaba correctamente desde el navegador.
- Consumía la API.
- Mostraba alertas generadas.
- Aplicaba filtros.
- Mostraba información enriquecida.
- Permitía consultar detalles.
- Actualizaba los datos al refrescar la vista.
```

La validación confirmó que el frontend cumplía su función dentro del MVP.

---

## Limitaciones

El frontend actual tiene varias limitaciones:

```text
- No incluye autenticación.
- No permite cambiar estados directamente desde todas las vistas.
- No tiene actualización en tiempo real.
- No incluye gráficos.
- No incluye dashboard avanzado.
- No gestiona usuarios.
- No permite crear reglas desde la interfaz.
- No permite investigación avanzada de alertas.
```

Estas limitaciones son coherentes con el alcance del proyecto.

---

## Posibles mejoras

En futuras versiones, el frontend podría ampliarse con:

```text
- Dashboard con métricas visuales.
- Gráficos de alertas por severidad.
- Gestión de reglas desde interfaz.
- Cambio de estado directamente desde el listado.
- Autenticación de usuarios.
- Vista de detalle más completa.
- Actualización automática.
- Filtros avanzados.
- Exportación de resultados.
```

Estas mejoras permitirían acercar la interfaz a una herramienta de monitorización más completa.

---

## Conclusión

El frontend del SIEM Lab MVP cumple una función clara: mostrar de forma visual las alertas generadas por el backend.

Su desarrollo con HTML, CSS y JavaScript permitió mantener la simplicidad del proyecto y evitar complejidad innecesaria.

Aunque se trata de una interfaz básica, permite demostrar que el sistema no solo procesa eventos y genera alertas, sino que también ofrece una forma visual de consultarlas.