## Introducción

Una vez finalizado y validado el **SIEM Lab MVP**, se puede comprobar que los objetivos principales definidos al inicio del proyecto se han cumplido.

El sistema desarrollado permite representar el flujo básico de un SIEM educativo:

```text
evento simulado → ingesta → almacenamiento → evaluación → alerta → consulta
````

Esta nota recoge los objetivos que se han alcanzado y explica cómo se han materializado dentro del proyecto.

---

## Objetivo general cumplido

El objetivo general era desarrollar un laboratorio SIEM básico en formato MVP, capaz de recibir eventos simulados, almacenarlos, evaluarlos mediante reglas y generar alertas consultables.

Este objetivo se ha cumplido porque el sistema permite:

```text
- Recibir eventos mediante /ingest.
- Guardar eventos en PostgreSQL.
- Consultar reglas activas.
- Evaluar eventos mediante un motor propio.
- Generar alertas automáticamente.
- Consultar alertas desde la API.
- Visualizar alertas desde el frontend.
- Cambiar el estado de una alerta.
```

El resultado final es una aplicación funcional, no únicamente una maqueta o una configuración de herramientas externas.

---

## Desarrollo de una API REST funcional

Se ha desarrollado una API REST con **FastAPI**.

La API expone endpoints para:

```text
- Comprobar el estado del sistema.
- Consultar información general.
- Consultar métricas.
- Gestionar eventos.
- Ingestar eventos.
- Gestionar reglas.
- Consultar alertas.
- Cambiar estados de alertas.
```

Endpoints principales validados:

```text
GET /health
GET /info
GET /metrics
POST /ingest
GET /rules
GET /alerts
GET /alerts/ui
PATCH /alerts/{alert_id}
```

Este objetivo se considera cumplido porque la API responde correctamente y actúa como núcleo lógico del proyecto.

---

## Implementación de la ingesta de eventos

Se ha implementado el endpoint principal de ingesta:

```http
POST /ingest
```

Este endpoint permite recibir eventos simulados con la siguiente estructura:

```text
source
severity
message
meta
```

Ejemplo validado:

```json
{
    "id": 18,
    "source": "ssh",
    "severity": 7,
    "message": "failed password for invalid user demo",
    "meta": {
        "host": "demo-1779117909"
    }
}
```

Este objetivo se considera cumplido porque el sistema recibe el evento, lo procesa y lo almacena correctamente.

---

## Diseño de una base de datos relacional

Se ha diseñado una base de datos PostgreSQL con las entidades principales del sistema:

```text
events
rules
alerts
alembic_version
```

El modelo permite diferenciar correctamente entre:

```text
Evento → dato recibido
Regla  → condición de detección
Alerta → resultado generado
```

La relación principal queda representada así:

```text
events 1 ─── N alerts N ─── 1 rules
```

Este objetivo se considera cumplido porque el sistema mantiene trazabilidad entre eventos recibidos, reglas activadas y alertas generadas.

---

## Implementación del motor básico de reglas

Se ha desarrollado un motor de reglas propio.

El motor evalúa eventos recibidos mediante `/ingest` contra reglas activas.

Condiciones soportadas:

```text
source
severity_min
contains
meta_match
throttle_seconds
threshold_count
threshold_seconds
```

La regla `test_rule_ssh` permitió validar el comportamiento principal:

```text
source = ssh
severity_min = 5
contains = failed
```

Evento validado:

```text
event_id: 19
source: ssh
severity: 7
message: failed password for invalid user demo
```

Resultado:

```text
Evento 19 → Regla test_rule_ssh → Alerta 8
```

Este objetivo se considera cumplido porque el sistema no solo almacena eventos, sino que aplica lógica de detección y genera alertas.

---

## Generación automática de alertas

El sistema genera alertas automáticamente cuando un evento coincide con una regla activa.

Ejemplo de alerta generada:

```json
{
    "id": 8,
    "rule_id": 7,
    "event_id": 19,
    "title": "Rule matched: test_rule_ssh",
    "group_key": "demo-1779119427",
    "status": "open",
    "rule_name": "test_rule_ssh",
    "event_source": "ssh",
    "event_severity": 7,
    "event_message": "failed password for invalid user demo"
}
```

Este objetivo se considera cumplido porque la alerta queda almacenada en PostgreSQL y puede consultarse desde la API.

---

## Gestión básica de estados de alertas

Se ha implementado una gestión básica del estado de las alertas.

Estados contemplados:

```text
open
ack
closed
```

El cambio de estado se realiza mediante:

```http
PATCH /alerts/{alert_id}
```

Esto permite representar una gestión inicial del ciclo de vida de una alerta:

```text
alerta generada → alerta reconocida → alerta cerrada
```

Este objetivo se considera cumplido porque las alertas pueden cambiar de estado desde la API.

---

## Consulta y filtrado de alertas

El sistema permite consultar alertas mediante endpoints básicos y enriquecidos.

Endpoints principales:

```text
GET /alerts
GET /alerts/{alert_id}
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Filtros validados:

```text
status
severity_min
q
limit
offset
```

Estos filtros permiten consultar alertas de forma más precisa.

Ejemplos:

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?status=ack" | python3 -m json.tool
```

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?severity_min=7" | python3 -m json.tool
```

Este objetivo se considera cumplido porque la API permite revisar alertas sin limitarse a devolver todos los registros sin control.

---

## Desarrollo de un frontend básico

Se ha desarrollado un frontend sencillo con:

```text
HTML
CSS
JavaScript
```

El frontend permite visualizar alertas generadas por el backend.

URL utilizada:

```text
http://127.0.0.1:5173/index.html
```

El frontend consume principalmente:

```http
GET /alerts/ui
```

Este objetivo se considera cumplido porque permite consultar visualmente las alertas desde navegador.

---

## Contenerización del entorno

Se ha utilizado **Docker Compose** para levantar los servicios principales del proyecto.

Servicios definidos:

```text
siem-api      → backend FastAPI
siem-db       → base de datos PostgreSQL
siem-adminer  → interfaz de consulta de PostgreSQL
```

Comando principal:

```bash
cd ~/siem-lab/docker
docker compose up -d --build
```

Este objetivo se considera cumplido porque el entorno puede levantarse de forma coordinada y reproducible.

---

## Validación mediante pruebas

El proyecto se ha validado mediante pruebas manuales y automatizadas.

Pruebas manuales realizadas:

```text
- Comprobación de Docker Compose.
- Comprobación de /health.
- Consulta de /metrics.
- Consulta de /rules.
- Ingesta mediante /ingest.
- Consulta de alertas mediante /alerts/ui.
- Filtros de alertas.
- Cambio de estado de alerta.
- Visualización desde frontend.
- Revisión de datos en Adminer.
```

Pruebas automatizadas:

```bash
docker compose exec api python -m pytest
```

Resultado:

```text
4 passed in 1.00s
```

Este objetivo se considera cumplido porque el sistema ha sido validado de extremo a extremo.

---

## Documentación del proyecto

El proyecto se ha documentado mediante:

```text
- README del repositorio.
- Notas en Obsidian.
- Diagramas del sistema.
- Comandos de validación.
- Explicación de problemas y soluciones.
```

La documentación permite explicar:

```text
- Qué hace el proyecto.
- Qué tecnologías utiliza.
- Cómo se levanta el entorno.
- Cómo se prueba la API.
- Cómo funciona el motor de reglas.
- Qué limitaciones tiene.
- Qué mejoras podrían incorporarse.
```

Este objetivo se considera cumplido porque el proyecto no solo funciona, sino que también puede explicarse y reproducirse.

---

## Relación con los objetivos académicos

El proyecto ha permitido aplicar competencias propias del ciclo de Desarrollo de Aplicaciones Multiplataforma:

```text
- Desarrollo backend.
- Diseño de base de datos.
- Creación de API REST.
- Desarrollo frontend básico.
- Uso de contenedores.
- Control de versiones.
- Pruebas.
- Documentación técnica.
- Resolución de problemas.
```

Aunque la temática está orientada a ciberseguridad, el núcleo del proyecto sigue siendo el desarrollo de una aplicación funcional.

---

## Resumen de objetivos cumplidos

|Objetivo|Estado|
|---|---|
|Desarrollar API REST|Cumplido|
|Implementar ingesta de eventos|Cumplido|
|Diseñar base de datos relacional|Cumplido|
|Implementar motor de reglas|Cumplido|
|Generar alertas automáticamente|Cumplido|
|Gestionar estados de alertas|Cumplido|
|Consultar y filtrar alertas|Cumplido|
|Crear frontend básico|Cumplido|
|Contenerizar entorno|Cumplido|
|Validar funcionamiento|Cumplido|
|Documentar proyecto|Cumplido|

---

## Conclusión

Los objetivos principales del SIEM Lab MVP se han cumplido.

El sistema permite recibir eventos, almacenarlos, evaluarlos mediante reglas, generar alertas, consultarlas, filtrarlas y visualizarlas desde una interfaz web básica.

El resultado final es un MVP funcional y validado, adecuado para demostrar competencias de desarrollo aplicadas a un contexto de ciberseguridad defensiva.