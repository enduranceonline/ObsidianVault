## Introducción

El backend es el componente central del SIEM Lab MVP. Se ha desarrollado con **FastAPI** y se encarga de recibir peticiones, validar datos, comunicarse con la base de datos, ejecutar la lógica del sistema y devolver respuestas estructuradas.

La API concentra la mayor parte de la funcionalidad del proyecto:

```text
- Ingesta de eventos.
- Gestión de reglas.
- Generación de alertas.
- Consulta de alertas.
- Cambio de estado de alertas.
- Consulta de métricas.
- Comprobación del estado del sistema.
````

---

## Función del backend en el proyecto

El backend actúa como punto de entrada y núcleo lógico del sistema.

Su función principal es coordinar el flujo:

```text
petición HTTP → validación → lógica de negocio → base de datos → respuesta
```

En el caso principal del proyecto, este flujo se concreta así:

```text
POST /ingest
    ↓
validar evento
    ↓
guardar evento
    ↓
consultar reglas activas
    ↓
evaluar evento
    ↓
generar alerta si procede
    ↓
devolver resultado
```

---

## Elección de FastAPI

FastAPI se eligió porque permite desarrollar APIs REST de forma clara y rápida.

Las razones principales fueron:

```text
- Sintaxis sencilla.
- Validación automática de datos.
- Documentación automática con Swagger.
- Buena integración con Python.
- Buen rendimiento.
- Facilidad para organizar endpoints por módulos.
```

La documentación automática fue especialmente útil durante el desarrollo, ya que permitió probar los endpoints desde el navegador mediante:

```text
http://127.0.0.1:8000/docs
```

---

## Organización del backend

El backend se encuentra dentro de la carpeta:

```text
backend/
```

La estructura principal es:

```text
backend/
├── app/
│   ├── api/
│   │   └── routes/
│   ├── db/
│   ├── models/
│   └── schemas/
├── tests/
├── Dockerfile
├── requirements.txt
└── pytest.ini
```

Esta estructura permite separar rutas, modelos, esquemas, configuración de base de datos y pruebas.

---

## Rutas de la API

Las rutas se organizaron por funcionalidad.

Los grupos principales son:

```text
health
info
metrics
events
ingest
rules
alerts
```

Esta división facilita mantener el código más ordenado y permite localizar rápidamente la lógica asociada a cada parte del sistema.

---

## Endpoint de estado: /health

El endpoint `/health` permite comprobar si la API está funcionando y si existe conexión con la base de datos.

```http
GET /health
```

Respuesta esperada:

```json
{
  "status": "ok",
  "db": "ok"
}
```

Este endpoint fue útil para validar el entorno después de levantar los contenedores y para comprobar que la API podía comunicarse correctamente con PostgreSQL.

---

## Endpoint de información: /info

El endpoint `/info` devuelve información básica de la aplicación.

```http
GET /info
```

Su función es ofrecer una respuesta sencilla que permita identificar la API y comprobar que está disponible.

---

## Endpoint de métricas: /metrics

El endpoint `/metrics` devuelve datos resumidos sobre el estado del sistema.

```http
GET /metrics
```

Métricas principales:

```text
- events_total
- rules_total
- rules_enabled
- alerts_total
```

Este endpoint permite comprobar rápidamente si el sistema está almacenando eventos, reglas y alertas.

---

## Endpoints de eventos

Los endpoints de eventos permiten crear y consultar eventos simples.

```http
POST /events
GET /events
```

Estos endpoints permiten trabajar directamente con eventos, aunque el flujo principal del proyecto se realiza mediante `/ingest`.

La diferencia importante es que `/events` se centra en guardar o consultar eventos, mientras que `/ingest` activa también el motor de reglas.

---

## Endpoint de ingesta: /ingest

El endpoint `/ingest` es el más importante del proyecto.

```http
POST /ingest
```

Su función es recibir un evento, guardarlo en la base de datos y activar la evaluación mediante reglas.

Ejemplo de evento:

```json
{
  "source": "ssh",
  "severity": 7,
  "message": "failed password for invalid user demo",
  "meta": {
    "host": "demo-host"
  }
}
```

Este endpoint representa el flujo principal del SIEM Lab MVP.

---

## Endpoints de reglas

Los endpoints de reglas permiten crear y consultar reglas de detección.

```http
POST /rules
GET /rules
```

Una regla define las condiciones que debe cumplir un evento para generar una alerta.

Ejemplo conceptual de regla:

```json
{
  "name": "SSH failed login demo",
  "enabled": true,
  "source": "ssh",
  "severity_min": 5,
  "contains": "failed",
  "meta_match": null,
  "throttle_seconds": 60,
  "threshold_count": null,
  "threshold_seconds": null
}
```

Las reglas activas son utilizadas por el motor de reglas durante la ingesta de eventos.

---

## Endpoints de alertas

Los endpoints de alertas permiten consultar y gestionar las alertas generadas.

Endpoints principales:

```http
GET /alerts
GET /alerts/{alert_id}
PATCH /alerts/{alert_id}
```

También existen endpoints enriquecidos para el frontend:

```http
GET /alerts/ui
GET /alerts/ui/count
GET /alerts/{alert_id}/ui
```

Estos endpoints permiten mostrar información combinada de alertas y eventos asociados.

---

## Cambio de estado de alertas

El backend permite modificar el estado de una alerta mediante:

```http
PATCH /alerts/{alert_id}
```

Estados permitidos:

```text
open
ack
closed
```

Esta funcionalidad permite simular una gestión básica de alertas.

Ejemplo:

```json
{
  "status": "ack"
}
```

---

## Validación de datos

FastAPI permite validar los datos recibidos mediante esquemas.

En el proyecto se utilizan esquemas para definir la estructura esperada de:

```text
- Eventos
- Reglas
- Alertas
- Actualización de estado
```

Esto permite evitar que peticiones mal formadas lleguen a la lógica interna del sistema.

---

## Comunicación con la base de datos

El backend se comunica con PostgreSQL mediante SQLAlchemy.

La API utiliza modelos para representar las tablas principales:

```text
Event
Rule
Alert
```

Esta comunicación permite:

```text
- Insertar eventos.
- Consultar reglas.
- Crear alertas.
- Filtrar alertas.
- Actualizar estados.
- Calcular métricas.
```

---

## Lógica de negocio

La lógica principal del backend no se limita a guardar datos. También aplica reglas y decide si un evento debe generar una alerta.

La lógica más importante se encuentra en el flujo de `/ingest`:

```text
1. Recibir evento.
2. Guardarlo en events.
3. Calcular group_key.
4. Consultar reglas activas.
5. Evaluar condiciones.
6. Crear alerta si corresponde.
7. Guardar alerta en alerts.
```

Esta lógica convierte el backend en el núcleo funcional del proyecto.

---

## Problemas encontrados

Durante el desarrollo del backend aparecieron varios problemas y decisiones importantes.

Uno de ellos fue diferenciar claramente entre `/events` e `/ingest`. El endpoint `/events` permite trabajar con eventos, pero `/ingest` es el que representa el flujo completo del SIEM porque activa el motor de reglas.

También fue necesario crear endpoints específicos para el frontend. Inicialmente podía parecer suficiente consultar `/alerts`, pero el frontend necesitaba información enriquecida procedente del evento asociado. Por ello se añadieron endpoints como `/alerts/ui`.

Otro punto importante fue estabilizar los filtros y la paginación para que la consulta de alertas fuera útil y no devolviera siempre toda la información sin control.

---

## Validación del backend

El backend se validó mediante:

```text
- Swagger.
- curl.
- Frontend.
- Adminer.
- Pytest.
```

Se comprobó que:

```text
- La API respondía correctamente.
- /health confirmaba la conexión con la base de datos.
- /metrics devolvía datos coherentes.
- /rules listaba reglas.
- /ingest generaba alertas.
- /alerts/ui devolvía información enriquecida.
- PATCH /alerts/{id} modificaba estados.
- Los filtros funcionaban correctamente.
```

---

## Limitaciones del backend

El backend actual tiene limitaciones propias del MVP:

```text
- No incluye autenticación.
- No incluye roles ni permisos.
- No implementa autorización por usuario.
- No utiliza procesamiento asíncrono.
- No incorpora cola de eventos.
- No expone notificaciones externas.
- No implementa un sistema completo de gestión de incidentes.
```

Estas limitaciones son aceptadas dentro del alcance del proyecto.

---

## Posibles mejoras

En futuras versiones, el backend podría ampliarse con:

```text
- Autenticación con JWT.
- Gestión de usuarios.
- Roles y permisos.
- Procesamiento asíncrono de eventos.
- Integración con fuentes reales de logs.
- Endpoints de informes.
- Historial de cambios de estado.
- Sistema de comentarios en alertas.
- Notificaciones externas.
```

---

## Conclusión

El backend FastAPI es el núcleo del SIEM Lab MVP. Recibe eventos, gestiona reglas, genera alertas, permite consultar información y ofrece endpoints para el frontend.

La elección de FastAPI facilitó el desarrollo de una API clara, documentada y fácil de probar. Su integración con PostgreSQL, SQLAlchemy y Docker permitió construir un backend funcional y adecuado para el alcance del proyecto.