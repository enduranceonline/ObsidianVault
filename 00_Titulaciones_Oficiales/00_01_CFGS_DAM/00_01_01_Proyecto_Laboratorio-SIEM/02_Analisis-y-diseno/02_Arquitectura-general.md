## Introducción

La arquitectura del proyecto se ha diseñado para separar responsabilidades entre los distintos componentes del sistema. El objetivo era construir una aplicación sencilla, modular y fácil de reproducir mediante contenedores.

El sistema se organiza alrededor de cuatro elementos principales:

```text
- Frontend
- API FastAPI
- Base de datos PostgreSQL
- Adminer
````

Cada componente cumple una función concreta dentro del flujo general del SIEM Lab MVP.

---

## Visión general de la arquitectura

La arquitectura puede representarse de forma simplificada así:

```text
Usuario
  ↓
Frontend / Swagger / curl
  ↓
API FastAPI
  ↓
PostgreSQL
  ↑
Adminer
```

El usuario puede interactuar con el sistema de varias formas:

```text
- Desde Swagger, para probar endpoints.
- Desde curl, para enviar peticiones manuales.
- Desde el frontend, para consultar alertas.
- Desde Adminer, para revisar la base de datos.
```

La API actúa como núcleo del sistema. Recibe eventos, consulta reglas, genera alertas y expone endpoints para consultar la información.

---

## Componentes principales

### Frontend

El frontend es una interfaz web sencilla desarrollada con HTML, CSS y JavaScript.

Su función es permitir la consulta visual de alertas generadas por el sistema.

Consume principalmente endpoints enriquecidos de la API:

```text
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

No contiene lógica de detección. Su responsabilidad es mostrar la información recibida desde el backend.

---

### API FastAPI

La API es el componente central del proyecto.

Sus responsabilidades principales son:

```text
- Recibir eventos.
- Guardar eventos en base de datos.
- Consultar reglas activas.
- Evaluar eventos mediante el motor de reglas.
- Generar alertas.
- Exponer endpoints de consulta.
- Permitir el cambio de estado de alertas.
- Ofrecer métricas básicas.
```

La API se ha desarrollado con FastAPI y se ejecuta mediante Uvicorn dentro del contenedor `siem-api`.

---

### PostgreSQL

PostgreSQL es la base de datos del sistema.

Almacena la información persistente del proyecto:

```text
- events
- rules
- alerts
- alembic_version
```

La base de datos permite mantener el histórico de eventos recibidos, reglas configuradas y alertas generadas.

---

### Adminer

Adminer es una herramienta auxiliar para consultar PostgreSQL desde navegador.

Se utiliza para validar que la información se guarda correctamente y para revisar las tablas durante el desarrollo.

No forma parte del flujo principal de uso del SIEM, pero resulta útil para pruebas, depuración y demostración.

---

## Arquitectura mediante Docker Compose

Los servicios principales se ejecutan mediante Docker Compose.

Servicios definidos:

```text
siem-api      → backend FastAPI
siem-db       → base de datos PostgreSQL
siem-adminer  → interfaz web para consultar PostgreSQL
```

Esta organización permite levantar el entorno completo con un único comando:

```bash
docker compose up -d --build
```

Docker Compose facilita la comunicación entre servicios mediante nombres internos. Por ejemplo, la API puede conectarse a la base de datos usando el nombre del servicio `db`.

---

## Flujo principal de ejecución

El flujo principal del sistema comienza cuando se envía un evento al endpoint `/ingest`.

```text
1. El usuario envía un evento a la API.
2. FastAPI recibe y valida la petición.
3. El evento se almacena en PostgreSQL.
4. El motor de reglas consulta las reglas activas.
5. El evento se compara con las reglas.
6. Si hay coincidencia, se genera una alerta.
7. La alerta queda guardada en PostgreSQL.
8. El usuario puede consultar la alerta desde API o frontend.
```

Este flujo representa el núcleo funcional del proyecto.

---

## Flujo de consulta

Una vez generadas las alertas, el usuario puede consultarlas mediante diferentes vías.

```text
Swagger/curl → endpoints de la API
Frontend     → endpoints enriquecidos
Adminer      → consulta directa de la base de datos
```

El frontend no accede directamente a PostgreSQL. Todas las consultas pasan por la API, lo que mantiene una separación correcta entre interfaz, lógica de negocio y persistencia.

---

## Separación de responsabilidades

La arquitectura se diseñó separando funciones:

```text
Frontend      → visualización
API           → lógica de aplicación
Motor reglas  → detección
PostgreSQL    → persistencia
Adminer       → inspección auxiliar
Docker Compose → orquestación local
```

Esta separación permite que cada parte del sistema tenga una responsabilidad clara y facilita la explicación del proyecto.

---

## Comunicación entre componentes

La comunicación principal se realiza mediante HTTP y conexión a base de datos.

```text
Frontend → API
Swagger  → API
curl     → API
API      → PostgreSQL
Adminer  → PostgreSQL
```

El usuario nunca modifica directamente la base de datos durante el flujo normal. Las operaciones principales se realizan a través de la API.

Adminer se utiliza únicamente como herramienta de inspección y validación.

---

## Decisiones de diseño relevantes

Durante el diseño de la arquitectura se tomaron varias decisiones importantes:

```text
- Centralizar la lógica en la API.
- Separar la base de datos en un servicio independiente.
- Usar Docker Compose para reproducibilidad.
- Mantener el frontend simple.
- Usar Adminer solo como herramienta auxiliar.
- Evitar depender de un SIEM externo.
```

Estas decisiones permitieron construir una arquitectura suficientemente completa sin aumentar de forma innecesaria la complejidad.

---

## Limitaciones de la arquitectura

La arquitectura actual está pensada para un entorno local de desarrollo y demostración.

Sus principales limitaciones son:

```text
- No está preparada para producción.
- No incluye autenticación.
- No utiliza HTTPS interno.
- No implementa alta disponibilidad.
- No separa entornos de desarrollo, pruebas y producción.
- No incorpora balanceo de carga.
```

Estas limitaciones son asumibles dentro del contexto de un MVP académico.

---

## Posibles mejoras arquitectónicas

En futuras versiones, la arquitectura podría ampliarse con:

```text
- Autenticación y autorización.
- Reverse proxy.
- HTTPS.
- Sistema de usuarios.
- Workers asíncronos.
- Integración con fuentes reales de logs.
- Dashboard más avanzado.
- Servicio de notificaciones.
- Despliegue en servidor externo.
```

Estas mejoras permitirían acercar el sistema a un entorno más realista.

---

## Conclusión

La arquitectura general del SIEM Lab MVP se basa en una separación clara entre interfaz, API, base de datos y herramientas auxiliares.

El diseño permite demostrar el flujo principal del sistema de forma ordenada:

```text
evento → API → base de datos → reglas → alerta → consulta
```

Esta arquitectura cumple el objetivo del proyecto: ser sencilla, funcional, reproducible y adecuada para representar una versión mínima de un sistema de monitorización defensiva.