

---

# Gestión de Alertas (Implementación)

## Laboratorio SIEM

Referencia de diseño y decisiones previas:  
[[00_Titulaciones_Oficiales/00_01_CFGS_DAM/00_01_01_Proyecto_Laboratorio-SIEM/00_01_01_04_Backend/03_Gestion-de-alertas.md|00_01_01_04_Backend/03_Gestion-de-alertas.md]]

---

## 1. Objetivo del componente

El módulo de gestión de alertas permite **administrar el ciclo de vida de las alertas** generadas por el motor de reglas del Laboratorio SIEM. Su función principal es ofrecer mecanismos para:

- consultar alertas generadas,
    
- filtrar y ordenar resultados,
    
- modificar el estado de una alerta,
    
- facilitar el análisis y la trazabilidad.
    

Este componente constituye el **principal punto de interacción del usuario** con el sistema, tanto desde la API como desde la futura interfaz web.

---

## 2. Integración dentro del backend

La gestión de alertas se implementa como un **conjunto de endpoints REST** dentro del backend FastAPI, accediendo directamente a la tabla `alerts` y manteniendo coherencia con el modelo de datos definido.

No se utilizan procesos asíncronos ni colas externas; las operaciones sobre alertas se realizan de forma síncrona y controlada, priorizando la claridad y la verificabilidad del comportamiento.

---

## 3. Modelo de estado de las alertas

Cada alerta dispone de un **estado** que define su situación dentro del sistema:

- `open`: alerta recién generada y pendiente de revisión.
    
- `ack`: alerta reconocida por el usuario.
    
- `closed`: alerta cerrada tras su análisis.
    

Este modelo simple permite simular un flujo básico de tratamiento de incidentes, habitual en sistemas SIEM reales, sin introducir complejidad innecesaria.

El estado se almacena en el campo `status` de la tabla `alerts` y se actualiza mediante la API.

---

## 4. Endpoints implementados

### 4.1 `GET /alerts`

**Propósito:**  
Permite consultar las alertas almacenadas en el sistema, aplicando filtros y paginación.

**Parámetros de consulta:**

- `limit`: número máximo de resultados devueltos.
    
- `offset`: desplazamiento para paginación.
    
- `status`: filtrar por estado (`open`, `ack`, `closed`).
    
- `group_key`: filtrar por clave de agrupación.
    
- `rule_id`: filtrar por regla.
    

**Comportamiento:**

- Devuelve las alertas ordenadas por fecha de creación descendente.
    
- Permite construir vistas de alertas activas o históricas.
    
- Facilita su consumo por la interfaz web.
    

---

### 4.2 `GET /alerts/{id}`

**Propósito:**  
Recupera el detalle completo de una alerta concreta.

**Comportamiento:**

- Verifica la existencia de la alerta.
    
- Devuelve todos los campos relevantes (`status`, `rule_id`, `event_id`, `group_key`, timestamps).
    

Este endpoint permite acceder al contexto de una alerta desde vistas de detalle.

---

### 4.3 `PATCH /alerts/{id}`

**Propósito:**  
Permite modificar el estado de una alerta existente.

**Entrada (JSON):**

- `status`: nuevo estado (`open`, `ack`, `closed`).
    

**Comportamiento:**

- Valida el estado recibido mediante esquema Pydantic.
    
- Actualiza el campo `status`.
    
- Actualiza automáticamente `updated_at`.
    

Este endpoint permite simular acciones habituales en la gestión de alertas, como el reconocimiento o cierre de incidentes.

---

## 5. Validación y consistencia de datos

La modificación de alertas se valida mediante esquemas Pydantic (`AlertUpdate`), asegurando que:

- Solo se permiten estados válidos.
    
- No se aceptan cambios arbitrarios de campos críticos.
    
- El backend mantiene el control de la lógica de negocio.
    

Este enfoque evita inconsistencias y refuerza la integridad del sistema.

---

## 6. Relación con eventos y reglas

Cada alerta mantiene una relación directa con:

- el evento que originó su generación (`event_id`),
    
- la regla responsable (`rule_id`).
    

Esta relación garantiza la **trazabilidad completa**, permitiendo:

- identificar qué evento provocó la alerta,
    
- conocer la lógica de detección aplicada,
    
- analizar el contexto del incidente.
    

---

## 7. Pruebas manuales realizadas

El funcionamiento del módulo se validó mediante pruebas manuales controladas:

- Consulta de alertas con filtros (`GET /alerts`).
    
- Recuperación de alertas individuales (`GET /alerts/{id}`).
    
- Actualización del estado de alertas (`PATCH /alerts/{id}`).
    
- Verificación de cambios en base de datos mediante consultas SQL.
    

Estas pruebas confirmaron el correcto funcionamiento del ciclo de vida de las alertas.

---

## 8. Decisiones de diseño relevantes

Durante la implementación del módulo se priorizaron las siguientes decisiones:

- Modelo de estados simple y claro.
    
- Endpoints REST coherentes y fácilmente consumibles.
    
- Validación estricta de entradas.
    
- Persistencia inmediata de los cambios.
    
- Enfoque didáctico y trazable.
    

Estas decisiones garantizan un comportamiento predecible y alineado con los objetivos del proyecto.

---

## 9. Limitaciones y alcance

El módulo de gestión de alertas implementado:

- No incluye asignación de alertas a usuarios.
    
- No incorpora comentarios ni histórico de acciones.
    
- No gestiona escalados ni priorización avanzada.
    
- No implementa notificaciones externas.
    

Estas limitaciones son deliberadas y coherentes con el alcance académico del Laboratorio SIEM.

---

## 10. Posibles ampliaciones

El diseño actual permite ampliar la gestión de alertas mediante:

- historial de acciones sobre alertas,
    
- asignación a usuarios o roles,
    
- integración con sistemas de notificación,
    
- enriquecimiento visual en la interfaz web.
    

Estas ampliaciones quedan fuera del alcance del presente proyecto.

---

## Nota sobre coherencia documental

Esta nota documenta exclusivamente funcionalidades **implementadas y verificadas** en el backend del Laboratorio SIEM, manteniendo coherencia total entre documentación y código.

---