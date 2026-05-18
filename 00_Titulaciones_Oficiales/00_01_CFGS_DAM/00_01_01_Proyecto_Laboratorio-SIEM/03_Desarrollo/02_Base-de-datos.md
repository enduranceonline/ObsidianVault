## Introducción

La base de datos del proyecto se ha implementado con **PostgreSQL**. Su función es almacenar de forma persistente los datos principales del SIEM Lab MVP: eventos, reglas y alertas.

La elección de una base de datos relacional permite mantener una estructura clara y relacionar cada alerta con el evento que la originó y con la regla que se activó.

---

## Función de la base de datos en el proyecto

La base de datos actúa como sistema de persistencia del laboratorio.

Almacena:

```text
- Eventos recibidos por la API.
- Reglas de detección configuradas.
- Alertas generadas por el motor de reglas.
- Información de migraciones gestionada por Alembic.
````

Sin base de datos, el sistema solo podría procesar eventos de forma temporal. PostgreSQL permite conservar la información y consultarla posteriormente desde la API, el frontend o Adminer.

---

## Servicio PostgreSQL

PostgreSQL se ejecuta dentro del contenedor:

```text
siem-db
```

Este servicio forma parte del entorno definido con Docker Compose.

La API se comunica con PostgreSQL mediante la red interna de Docker. Esto permite que el backend pueda acceder a la base de datos sin depender de una instalación directa en el sistema anfitrión.

---

## Tablas principales

La base de datos contiene cuatro tablas relevantes:

```text
events
rules
alerts
alembic_version
```

Las tres primeras pertenecen a la lógica funcional del proyecto. La tabla `alembic_version` pertenece al sistema de migraciones.

---

## Tabla events

La tabla `events` almacena los eventos recibidos por el sistema.

Un evento representa un log o suceso simulado enviado a la API, normalmente mediante el endpoint:

```http
POST /ingest
```

Campos principales:

```text
id          → identificador único
source      → origen del evento
severity    → severidad del evento
message     → mensaje descriptivo
meta        → metadatos adicionales
created_at  → fecha de creación
```

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

Esta tabla permite conservar el histórico de eventos que han entrado al sistema.

---

## Tabla rules

La tabla `rules` almacena las reglas de detección configuradas.

Una regla define las condiciones que debe cumplir un evento para generar una alerta.

Campos principales:

```text
id                 → identificador único
name               → nombre de la regla
enabled            → indica si la regla está activa
source             → fuente esperada del evento
severity_min       → severidad mínima
contains           → texto que debe aparecer en el mensaje
meta_match         → coincidencia de metadatos
throttle_seconds   → tiempo de espera para evitar alertas repetidas
threshold_count    → número de eventos necesarios para umbral
threshold_seconds  → ventana temporal del umbral
created_at         → fecha de creación
```

Ejemplo conceptual:

```text
name = test_rule_ssh
enabled = true
source = ssh
severity_min = 5
contains = failed
```

Esta regla detecta eventos procedentes de `ssh`, con severidad igual o superior a 5 y cuyo mensaje contiene la palabra `failed`.

---

## Tabla alerts

La tabla `alerts` almacena las alertas generadas por el motor de reglas.

Una alerta se crea cuando un evento cumple las condiciones de una regla activa.

Campos principales:

```text
id          → identificador único
rule_id     → regla que ha generado la alerta
event_id    → evento que ha originado la alerta
title       → título descriptivo
status      → estado de la alerta
group_key   → clave de agrupación
created_at  → fecha de creación
```

Estados posibles:

```text
open
ack
closed
```

La relación con `events` y `rules` permite saber por qué se ha generado una alerta determinada.

---

## Tabla alembic_version

La tabla `alembic_version` es gestionada automáticamente por Alembic.

Su función es registrar la versión actual del esquema de la base de datos. No forma parte de la lógica funcional del SIEM, pero permite controlar las migraciones aplicadas.

---

## Relaciones entre tablas

El modelo principal puede resumirse así:

```text
events 1 ─── N alerts N ─── 1 rules
```

Esto significa que:

```text
- Un evento puede generar una o varias alertas.
- Una regla puede generar muchas alertas.
- Cada alerta pertenece a un evento y a una regla.
```

Esta relación permite mantener trazabilidad entre los datos recibidos y las alertas generadas.

---

## Uso de SQLAlchemy

El proyecto utiliza **SQLAlchemy** para trabajar con la base de datos desde Python.

SQLAlchemy permite definir modelos en código para representar las tablas de la base de datos.

Modelos principales:

```text
Event
Rule
Alert
```

Esta capa evita trabajar únicamente con SQL manual y permite integrar mejor la base de datos con la lógica del backend.

---

## Uso de Alembic

**Alembic** se utiliza para gestionar migraciones de base de datos.

Las migraciones permiten crear o modificar el esquema de forma controlada.

Comando utilizado para aplicar migraciones:

```bash
docker compose exec api alembic upgrade head
```

El uso de Alembic facilita reproducir la estructura de la base de datos en otro entorno.

---

## Consulta visual con Adminer

Para inspeccionar la base de datos se utilizó Adminer.

URL habitual:

```text
http://127.0.0.1:8080
```

Adminer permitió revisar:

```text
- Tablas existentes.
- Eventos almacenados.
- Reglas configuradas.
- Alertas generadas.
- Relación entre registros.
```

Fue especialmente útil durante la validación del proyecto, ya que permitía comprobar visualmente que los datos se estaban guardando correctamente.

---

## Problema de autenticación con PostgreSQL

Durante el desarrollo apareció un problema de conexión entre la API y PostgreSQL.

Error detectado:

```text
FATAL: password authentication failed for user "siem"
```

La causa fue que el volumen persistente de PostgreSQL conservaba una contraseña anterior. Aunque se modificaran las variables de entorno, la base de datos ya inicializada mantenía la configuración previa.

La solución fue modificar la contraseña directamente desde PostgreSQL:

```bash
docker compose exec db psql -U siem -d siem -c "ALTER USER siem WITH PASSWORD 'change_me';"
docker compose restart api
```

Después de aplicar esta solución, el endpoint `/health` volvió a responder correctamente.

---

## Aprendizaje del problema

Este problema permitió entender una característica importante de Docker y PostgreSQL: los volúmenes persistentes conservan los datos incluso aunque se reconstruyan los contenedores.

Por tanto, cambiar variables de entorno no siempre modifica una base de datos ya creada.

Aprendizaje principal:

```text
Los contenedores pueden recrearse, pero los volúmenes mantienen el estado anterior.
```

Este aprendizaje fue importante para diagnosticar el fallo correctamente y evitar buscar el error únicamente en el código de la API.

---

## Validación de la base de datos

La base de datos se validó comprobando:

```text
- Conexión correcta desde la API.
- Respuesta correcta de /health.
- Existencia de las tablas principales.
- Inserción de eventos mediante /ingest.
- Persistencia de reglas.
- Generación de alertas.
- Consulta visual desde Adminer.
- Consulta de métricas desde /metrics.
```

También se comprobó que las métricas reflejaban correctamente los datos almacenados.

Ejemplo de métricas validadas:

```text
events_total
rules_total
rules_enabled
alerts_total
```

---

## Decisiones de diseño

Las principales decisiones relacionadas con la base de datos fueron:

```text
- Usar PostgreSQL como sistema relacional.
- Separar eventos, reglas y alertas en tablas distintas.
- Relacionar cada alerta con su evento y su regla.
- Usar meta para almacenar información flexible del evento.
- Usar group_key para agrupación básica.
- No duplicar todos los datos del evento dentro de la alerta.
- Usar endpoints enriquecidos para mostrar datos combinados en el frontend.
```

Estas decisiones permitieron mantener un modelo claro, suficiente para el MVP y fácil de explicar.

---

## Limitaciones

La base de datos actual tiene algunas limitaciones:

```text
- No incluye usuarios.
- No incluye roles.
- No almacena comentarios sobre alertas.
- No gestiona casos o incidentes.
- No almacena fuentes reales de logs.
- No incluye histórico avanzado de cambios de estado.
- No implementa particionado ni optimizaciones para grandes volúmenes.
```

Estas limitaciones son coherentes con el alcance del MVP.

---

## Posibles mejoras

En futuras versiones, la base de datos podría ampliarse con:

```text
- Tabla de usuarios.
- Tabla de roles y permisos.
- Tabla de casos o incidentes.
- Historial de cambios de estado.
- Comentarios sobre alertas.
- Tabla de activos monitorizados.
- Tabla de fuentes de logs.
- Índices adicionales para mejorar consultas.
- Estrategias de retención de eventos.
```

Estas mejoras permitirían acercar el sistema a una plataforma más completa.

---

## Conclusión

La base de datos es uno de los componentes centrales del SIEM Lab MVP.

PostgreSQL permite almacenar eventos, reglas y alertas de forma persistente, manteniendo relaciones claras entre los datos. SQLAlchemy facilita trabajar con estos datos desde el backend y Alembic permite controlar el esquema mediante migraciones.

El problema de autenticación encontrado durante el desarrollo sirvió para comprender mejor el funcionamiento de los volúmenes persistentes de Docker y reforzó la importancia de validar la configuración del entorno.