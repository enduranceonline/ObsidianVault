

---

# Decisiones tecnológicas

## Laboratorio SIEM

---

## 1. Introducción

En este apartado se recogen las decisiones tecnológicas adoptadas para el desarrollo del backend del Laboratorio SIEM. El objetivo es justificar las tecnologías y enfoques seleccionados en función del alcance académico del proyecto, la arquitectura definida y los objetivos funcionales del sistema.

No se detallan aspectos de implementación concreta ni código, que se abordarán en el bloque correspondiente.

---

## 2. Enfoque general del backend

El backend del Laboratorio SIEM se ha diseñado como un **sistema modular**, compuesto por varios componentes claramente diferenciados:

- API de ingesta de eventos.
    
- Motor de reglas.
    
- Gestión de alertas.
    
- Acceso a la base de datos.
    

Este enfoque permite separar responsabilidades, facilitar la comprensión del sistema y mantener una arquitectura coherente con los principios del desarrollo backend.

---

## 3. Tecnologías seleccionadas

El backend del Laboratorio SIEM se implementará con las siguientes tecnologías:

- Lenguaje: **Python 3.12**
    
- Framework API REST: **FastAPI**
    
- Servidor ASGI: **Uvicorn**
    
- Base de datos: **PostgreSQL**
    
- ORM (acceso a datos): **SQLAlchemy 2.0**
    
- Migraciones de esquema: **Alembic**
    
- Entorno de desarrollo (IDE): **Visual Studio Code**
    
- Control de versiones: **Git + GitHub**
    
- Pruebas de API: **Postman**
    
- Cliente de base de datos: **DBeaver**
    
- Testing: **pytest**
    
- Estilo/quality: **Ruff**
    
- Formato de intercambio: **JSON**
    

---

## 4. Asignación tecnológica por módulos del backend

El backend se implementa como una **aplicación única (monolito modular)**: un solo servicio desplegable, con módulos internos separados por responsabilidad.

### 4.1 API de ingesta de eventos

- Implementación: **FastAPI** (endpoint `POST /api/events`)
    
- Responsabilidad: recibir eventos, validar estructura mínima, normalizar campos, persistir en BD.
    
- Persistencia: **SQLAlchemy** → tablas `sources`, `events`.
    

### 4.2 Motor de reglas

- Implementación: módulo interno (servicio) en **Python**
    
- Responsabilidad: cargar reglas activas (`rules`), consultar eventos relevantes (`events`), evaluar condiciones, generar alertas.
    
- Persistencia: **SQLAlchemy** → tablas `alerts`, `alert_events`.
    

### 4.3 Gestión de alertas (consulta y cambios de estado)

- Implementación: **FastAPI** (endpoints para listar alertas, detalle y cierre)
    
- Responsabilidad: exponer alertas al frontend y permitir transición `OPEN → CLOSED`.
    
- Persistencia: **SQLAlchemy** sobre `alerts` y relaciones con `alert_events`.
    

### 4.4 Acceso a datos y migraciones

- ORM: **SQLAlchemy 2.0** como capa única de persistencia
    
- Versionado del esquema: **Alembic** para mantener trazabilidad de cambios en tablas/índices.
    

---

## 5. Herramientas de trabajo y ejecución

- Desarrollo: **Visual Studio Code**
    
- Ejecución local: **Uvicorn** (servidor ASGI)
    
- Gestión de BD: **DBeaver**
    
- Pruebas manuales de endpoints: **Postman**
    
- Control de versiones: **Git + GitHub**
    
- Calidad y estilo: **Ruff**
    
- Pruebas automatizadas: **pytest**
    

---

## 6. Justificación de las decisiones tecnológicas

### 6.1 Python + FastAPI

Se selecciona **Python** por su idoneidad en proyectos de ciberseguridad y análisis, y por su rapidez para construir servicios backend claros y mantenibles. **FastAPI** aporta:

- API REST de alto rendimiento con tipado y validación estructurada.
    
- Documentación automática (OpenAPI), útil para pruebas y defensa del proyecto.
    
- Desarrollo ágil con estructura limpia por módulos.
    

### 6.2 PostgreSQL

Se utiliza **PostgreSQL** por ser un estándar robusto en entornos profesionales y encajar con el modelo relacional definido:

- Integridad referencial y trazabilidad (claves foráneas).
    
- Buen soporte de índices para consultas típicas (eventos recientes, alertas abiertas).
    
- Soporte de tipos útiles como **UUID** y **JSONB** (metadatos).
    

### 6.3 SQLAlchemy + Alembic

Se usa **SQLAlchemy 2.0** para mantener una capa de persistencia consistente y desacoplada del resto del sistema. **Alembic** permite:

- Versionar cambios del esquema de BD.
    
- Reproducir la instalación del proyecto de forma controlada.
    
- Mantener coherencia entre documentación, esquema y despliegue.
    

### 6.4 Toolchain (VS Code, Ruff, pytest)

- **VS Code**: entorno ligero y ampliamente utilizado.
    
- **Ruff**: unifica linting/estándares en una sola herramienta, mejorando consistencia.
    
- **pytest**: pruebas automatizadas simples y defendibles (validaciones, endpoints, reglas básicas).
    

---

## 7. Tecnologías y enfoques descartados

De forma consciente se descartan:

- Microservicios: complejidad innecesaria para el alcance del laboratorio.
    
- Streaming/colas (Kafka/RabbitMQ): no aporta valor al objetivo académico (procesamiento no tiempo real).
    
- Motores SIEM completos (Splunk/Elastic/Wazuh) como núcleo: el objetivo es **desarrollar** un SIEM académico, no solo desplegar uno.
    
- Alta disponibilidad/replicación: fuera de alcance del proyecto.
    

---

## 8. Conclusión

El stack seleccionado (Python + FastAPI + PostgreSQL + SQLAlchemy/Alembic) permite implementar un backend SIEM académico **claro, trazable y defendible**, priorizando modularidad, coherencia con el modelo de datos y facilidad de validación y pruebas, sin introducir complejidad propia de entornos de producción.

---