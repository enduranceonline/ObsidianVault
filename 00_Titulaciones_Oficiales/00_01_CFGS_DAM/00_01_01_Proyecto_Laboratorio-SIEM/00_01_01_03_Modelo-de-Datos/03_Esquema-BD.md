#PostgreSQL

---

# Esquema de base de datos

## Laboratorio SIEM

---

## 1. Introducción

En este apartado se define el **esquema físico de la base de datos** del Laboratorio SIEM, derivado directamente del **modelo entidad–relación final** presentado en el apartado anterior.

Se detallan las tablas que componen el sistema, sus campos, tipos de datos recomendados, índices y restricciones, con el objetivo de disponer de un diseño **implementable**, **coherente** y **alineado con el alcance académico del proyecto**.

El esquema ha sido diseñado para:

- Persistir eventos y alertas de forma estructurada.
    
- Mantener trazabilidad completa entre eventos, reglas y alertas.
    
- Permitir consultas habituales del sistema de forma eficiente.
    
- Servir como base para el desarrollo del backend y la interfaz web.
    

---

## 2. Gestor de base de datos

Se utiliza un **sistema gestor de bases de datos relacional (RDBMS)**, concretamente:

**PostgreSQL**

### Justificación de la elección

PostgreSQL se ha seleccionado por los siguientes motivos:

- Soporte sólido de **integridad referencial** y restricciones.
    
- Disponibilidad de tipos de datos avanzados como `JSONB`, adecuados para metadatos de eventos.
    
- Buen rendimiento en consultas estructuradas y temporales.
    
- Amplia adopción en entornos reales y educativos.
    
- Adecuación tanto para desarrollo local como para despliegues más complejos.
    

No se emplean bases de datos NoSQL, ya que el modelo del sistema es claramente relacional y prioriza la **trazabilidad entre entidades**.

---

## 3. Criterios generales de diseño

El esquema de base de datos se ha definido siguiendo los siguientes criterios:

- Todas las tablas disponen de una **clave primaria (PK)**.
    
- Las relaciones se implementan mediante **claves foráneas (FK)**.
    
- Se incluyen **campos temporales** para auditoría y análisis histórico.
    
- Los índices se definen según las consultas más habituales del sistema.
    
- La lógica compleja se implementa en el backend, no en la base de datos.
    

---

## 4. Convenciones y notación

Los campos se describen con la siguiente estructura:

```
nombre_del_campo (tipo_de_clave) — tipo_de_dato
```

Los nombres de campos y tablas siguen convención **snake_case**, en inglés, y en minúsculas, por coherencia con PostgreSQL y el backend.

---

## 5. Tipos de datos utilizados

- **UUID**: identificadores únicos.
    
- **VARCHAR / TEXT**: campos descriptivos.
    
- **SMALLINT**: severidades.
    
- **BOOLEAN**: estados lógicos.
    
- **TIMESTAMP**: fechas y horas.
    
- **JSONB**: metadatos estructurados y flexibles.
    

---

## 6. Tablas del sistema

### • events

**Propósito:**  
Almacena los **eventos normalizados** recibidos por el sistema. Constituye la base del proceso de detección.

**Campos:**

- `id` (PK) — `UUID`
    
- `ts` — `TIMESTAMP`
    
- `source` — `VARCHAR`
    
- `severity` — `SMALLINT`
    
- `message` — `TEXT`
    
- `meta` — `JSONB` (nullable)
    
- `created_at` — `TIMESTAMP`
    

**Índices recomendados:**

- Índice por `ts`.
    
- Índice por `source`.
    
- Índice por `severity`.
    

---

### • rules

**Propósito:**  
Define las **reglas de detección** evaluadas por el motor de reglas.

**Campos:**

- `id` (PK) — `UUID`
    
- `name` — `VARCHAR`
    
- `enabled` — `BOOLEAN`
    
- `source` — `VARCHAR` (nullable)
    
- `severity_min` — `SMALLINT` (nullable)
    
- `contains` — `VARCHAR` (nullable)
    
- `meta_match` — `JSONB` (nullable)
    
- `throttle_seconds` — `INTEGER` (nullable)
    
- `threshold_count` — `INTEGER` (nullable)
    
- `threshold_seconds` — `INTEGER` (nullable)
    
- `created_at` — `TIMESTAMP`
    

**Restricciones:**

- `UNIQUE(name)`
    

---

### • alerts

**Propósito:**  
Almacena las **alertas generadas** como resultado de evaluar una regla sobre un evento concreto.

**Campos:**

- `id` (PK) — `UUID`
    
- `status` — `VARCHAR`
    
- `rule_id` (FK → rules.id) — `UUID`
    
- `event_id` (FK → events.id) — `UUID`
    
- `group_key` — `VARCHAR` (nullable)
    
- `created_at` — `TIMESTAMP`
    
- `updated_at` — `TIMESTAMP`
    

**Índices recomendados:**

- Índice por `(status, created_at)`
    
- Índice por `rule_id`
    
- Índice por `group_key`
    

---

## 7. Relaciones y trazabilidad

El esquema implementa las siguientes relaciones:

- **events.id → alerts.event_id**  
    Un evento puede generar **cero o varias alertas**.
    
- **rules.id → alerts.rule_id**  
    Cada alerta está asociada a una única regla, mientras que una regla puede generar múltiples alertas.
    

Este diseño permite reconstruir el flujo completo del sistema:

```
Event → Rule → Alert
```

garantizando la **trazabilidad completa** del proceso de detección.

---

## 8. Nota sobre la evolución del diseño

En fases iniciales del proyecto se contempló un modelo con entidades adicionales (`sources`, `alert_events`) para representar relaciones más complejas.

Tras la implementación del sistema se optó por un **modelo simplificado**, eliminando tablas intermedias y representando la fuente como un atributo lógico del evento. Esta decisión reduce la complejidad del esquema, facilita las consultas y se ajusta al alcance del laboratorio, manteniendo la posibilidad de evolución futura.

---

## 9. Alcance del esquema

El esquema presentado cubre las necesidades funcionales del Laboratorio SIEM desarrollado. No se incluyen mecanismos avanzados como particionado, replicación o alta disponibilidad, ya que quedan fuera del alcance académico del proyecto.

---