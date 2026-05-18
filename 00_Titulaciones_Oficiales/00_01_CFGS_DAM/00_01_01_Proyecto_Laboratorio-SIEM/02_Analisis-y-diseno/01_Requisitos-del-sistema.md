## Introducción

Antes de desarrollar el proyecto fue necesario definir qué debía hacer el sistema y qué condiciones debía cumplir para considerarse funcional.

Los requisitos del SIEM Lab MVP se han dividido en:

```text
- Requisitos funcionales
- Requisitos no funcionales
- Requisitos técnicos
- Requisitos de validación
- Requisitos fuera de alcance
````

Esta separación permite distinguir entre las funcionalidades que el sistema debe ofrecer, las condiciones técnicas que debe cumplir y las limitaciones asumidas por tratarse de un MVP.

---

## Requisitos funcionales

Los requisitos funcionales describen las acciones que el sistema debe permitir realizar.

### RF01. Comprobar el estado del sistema

El sistema debe ofrecer un endpoint que permita comprobar si la API está funcionando y si existe conexión con la base de datos.

Endpoint asociado:

```text
GET /health
```

Este requisito permite validar rápidamente que los componentes principales están operativos.

---

### RF02. Consultar información básica de la aplicación

El sistema debe ofrecer un endpoint informativo con datos básicos de la aplicación.

Endpoint asociado:

```text
GET /info
```

Este requisito permite identificar la aplicación y confirmar que la API responde correctamente.

---

### RF03. Recibir eventos simulados

El sistema debe permitir recibir eventos simulados mediante una petición HTTP.

Endpoint principal:

```text
POST /ingest
```

Cada evento debe incluir información básica como:

```text
- source
- severity
- message
- meta
```

Este requisito representa el punto de entrada principal del sistema.

---

### RF04. Almacenar eventos en base de datos

Cada evento recibido mediante la API debe guardarse en PostgreSQL.

La persistencia permite consultar posteriormente los eventos recibidos y relacionarlos con las alertas generadas.

---

### RF05. Crear reglas de detección

El sistema debe permitir crear reglas que definan condiciones de detección.

Endpoint asociado:

```text
POST /rules
```

Una regla puede incluir condiciones como:

```text
- source
- severity_min
- contains
- meta_match
- throttle_seconds
- threshold_count
- threshold_seconds
```

---

### RF06. Consultar reglas existentes

El sistema debe permitir consultar las reglas disponibles.

Endpoint asociado:

```text
GET /rules
```

Este requisito permite verificar qué reglas existen y cuáles están activas.

---

### RF07. Evaluar eventos mediante reglas activas

Cuando se recibe un evento mediante `/ingest`, el sistema debe evaluar ese evento contra las reglas activas.

Si el evento cumple las condiciones de una regla, debe generarse una alerta.

---

### RF08. Generar alertas automáticamente

El sistema debe crear una alerta cuando un evento coincide con una regla activa.

Cada alerta debe quedar asociada a:

```text
- El evento que la originó.
- La regla que se activó.
- Un estado inicial.
- Un título.
- Un group_key, si corresponde.
```

---

### RF09. Consultar alertas

El sistema debe permitir consultar las alertas generadas.

Endpoints asociados:

```text
GET /alerts
GET /alerts/{alert_id}
```

Este requisito permite revisar las alertas almacenadas en el sistema.

---

### RF10. Consultar alertas enriquecidas para frontend

El sistema debe ofrecer endpoints específicos para que el frontend pueda consultar alertas con información adicional del evento asociado.

Endpoints asociados:

```text
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Estos endpoints evitan duplicar datos en la base de datos y facilitan la visualización.

---

### RF11. Filtrar alertas

El sistema debe permitir aplicar filtros sobre las alertas.

Filtros contemplados:

```text
- Estado
- Severidad mínima
- Texto de búsqueda
- Límite
- Offset
```

Este requisito permite consultar la información de forma más útil y reducir ruido.

---

### RF12. Cambiar el estado de una alerta

El sistema debe permitir modificar el estado de una alerta.

Endpoint asociado:

```text
PATCH /alerts/{alert_id}
```

Estados permitidos:

```text
open
ack
closed
```

Esta funcionalidad permite simular una gestión básica de alertas.

---

### RF13. Consultar métricas básicas

El sistema debe ofrecer métricas generales sobre los datos almacenados.

Endpoint asociado:

```text
GET /metrics
```

Métricas previstas:

```text
- Total de eventos
- Total de reglas
- Reglas activas
- Total de alertas
```

---

### RF14. Visualizar alertas desde frontend

El sistema debe incluir una interfaz web básica que permita visualizar las alertas generadas.

El frontend debe permitir:

```text
- Ver listado de alertas.
- Consultar información relevante.
- Aplicar filtros básicos.
- Actualizar los datos.
- Acceder al detalle de una alerta.
```

---

## Requisitos no funcionales

Los requisitos no funcionales describen condiciones de calidad, organización y comportamiento general del sistema.

### RNF01. Reproducibilidad

El proyecto debe poder ejecutarse desde cero en otro entorno siguiendo instrucciones documentadas.

Para ello se utiliza:

```text
- Docker Compose
- .env.example
- README
- Migraciones
- Comandos de validación
```

---

### RNF02. Separación de responsabilidades

El sistema debe separar los componentes principales:

```text
- API
- Base de datos
- Frontend
- Herramienta de inspección
```

Esta separación facilita el mantenimiento y la comprensión del proyecto.

---

### RNF03. Claridad del modelo de datos

El modelo de datos debe diferenciar claramente entre:

```text
- Eventos
- Reglas
- Alertas
```

Esta separación permite explicar el comportamiento del sistema y relacionar cada alerta con su origen.

---

### RNF04. Simplicidad

El sistema debe mantener una complejidad adecuada al contexto académico.

No se busca construir un SIEM completo, sino un MVP funcional que represente el flujo principal.

---

### RNF05. Documentación

El proyecto debe incluir documentación suficiente para explicar:

```text
- Objetivo del sistema
- Tecnologías utilizadas
- Arquitectura
- Puesta en marcha
- Endpoints principales
- Pruebas
- Limitaciones
- Futuras mejoras
```

---

### RNF06. Seguridad básica de configuración

El proyecto no debe subir credenciales reales al repositorio.

Para ello se utilizan:

```text
- Archivos .env locales
- Archivo .env.example
- Reglas en .gitignore
```

---

### RNF07. Validación del funcionamiento

El sistema debe poder validarse mediante pruebas manuales y automatizadas.

La validación debe comprobar que el flujo principal funciona de extremo a extremo.

---

## Requisitos técnicos

Los requisitos técnicos definen las herramientas y condiciones necesarias para ejecutar el proyecto.

### RT01. Entorno de virtualización

El proyecto se ejecuta en una máquina virtual de laboratorio.

Plataforma utilizada finalmente:

```text
VirtualBox
```

La virtualización permite aislar el entorno del sistema anfitrión.

---

### RT02. Contenedores Docker

Los servicios principales deben ejecutarse mediante Docker Compose.

Servicios incluidos:

```text
siem-api
siem-db
siem-adminer
```

---

### RT03. Backend

El backend debe estar desarrollado con:

```text
Python
FastAPI
Uvicorn
SQLAlchemy
Alembic
```

---

### RT04. Base de datos

La base de datos utilizada debe ser:

```text
PostgreSQL
```

Debe almacenar las tablas principales:

```text
events
rules
alerts
alembic_version
```

---

### RT05. Frontend

El frontend debe estar desarrollado con tecnologías web básicas:

```text
HTML
CSS
JavaScript
```

Su función es consumir la API y mostrar alertas.

---

### RT06. Pruebas

Las pruebas automatizadas deben ejecutarse con:

```text
Pytest
```

Preferentemente dentro del contenedor de la API para evitar problemas de dependencias locales.

---

### RT07. Control de versiones

El proyecto debe estar gestionado con:

```text
Git
GitHub
```

Esto permite registrar cambios, mantener una copia remota y preparar la entrega final.

---

## Requisitos de validación

Para considerar el proyecto funcional, deben cumplirse las siguientes comprobaciones:

```text
- La máquina virtual arranca correctamente.
- Docker Compose levanta los servicios.
- PostgreSQL está operativo.
- Adminer permite consultar las tablas.
- FastAPI responde correctamente.
- Swagger está disponible.
- /health devuelve estado correcto.
- /metrics devuelve métricas.
- /rules lista reglas.
- /ingest recibe eventos.
- El motor de reglas genera alertas.
- /alerts/ui devuelve alertas enriquecidas.
- PATCH /alerts/{id} permite cambiar el estado.
- Los filtros funcionan.
- El frontend muestra alertas.
- Los tests automatizados se ejecutan correctamente.
```

---

## Requisitos fuera de alcance

Algunas funcionalidades no forman parte de esta versión del proyecto.

Quedan fuera del alcance:

```text
- Autenticación de usuarios.
- Roles y permisos.
- Integración con logs reales.
- Agentes externos.
- Dashboards avanzados.
- Notificaciones.
- Informes exportables.
- Correlación avanzada.
- Despliegue en producción.
- Alta disponibilidad.
```

Estas funcionalidades se consideran posibles ampliaciones futuras.

---

## Conclusión

Los requisitos definidos permitieron mantener el proyecto dentro de un alcance claro y verificable.

El sistema debía demostrar un flujo completo de ingesta, almacenamiento, evaluación, alerta y consulta, sin asumir la complejidad de un SIEM real.

Esta definición de requisitos sirvió como base para diseñar la arquitectura, implementar el backend, construir el modelo de datos, desarrollar el frontend y validar el resultado final.