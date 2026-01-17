

---

# API de Ingesta (Implementación)

## Laboratorio SIEM

Referencia de diseño y decisiones previas:  
[[00_Titulaciones_Oficiales/00_01_CFGS_DAM/00_01_01_Proyecto_Laboratorio-SIEM/00_01_01_04_Backend/01_API-de-Ingesta.md|00_01_01_04_Backend/01_API-de-Ingesta.md]]

---

## 1. Objetivo del componente

La API de Ingesta constituye el **punto de entrada único** del Laboratorio SIEM. Su finalidad es recibir eventos en formato estructurado (JSON), realizar una validación básica y activar el flujo interno del sistema:

1. Persistencia del evento en base de datos.
    
2. Evaluación de reglas activas.
    
3. Generación de alertas cuando se cumplen condiciones.
    

Este enfoque centraliza el control de entrada, evita accesos directos a base de datos y proporciona una interfaz clara para futuras fuentes (Linux/Windows) o simulaciones.

---

## 2. Endpoints implementados

### 2.1 `POST /ingest`

**Propósito:**  
Recibe un evento normalizado, lo persiste y desencadena la evaluación de reglas.

**Entrada (JSON):** `IngestPayload`

- `source` (string, obligatorio)
    
- `severity` (int 0–10, obligatorio)
    
- `message` (string, obligatorio)
    
- `meta` (objeto JSON, opcional)
    

**Salida:** `EventOut` (evento persistido)

**Comportamiento principal:**

- Se asigna timestamp en servidor (UTC).
    
- Se inserta el evento en `events`.
    
- Se consultan las reglas activas (`rules.enabled = true`).
    
- Se evalúan criterios:
    
    - `source` (igualdad)
        
    - `severity_min` (mínimo)
        
    - `contains` (subcadena)
        
    - `meta_match` (coincidencia exacta por claves)
        
- Se aplican mecanismos para evitar ruido:
    
    - _throttle_ por ventana temporal (si corresponde)
        
    - anti-duplicado: no generar alertas adicionales si existe una alerta activa (`open/ack`) para la misma regla y grupo
        
- Se crean alertas en `alerts` cuando procede.
    

---

### 2.2 `GET /health`

**Propósito:**  
Verifica que el servicio FastAPI está operativo.

**Salida:**  
`{ "status": "ok" }`

---

### 2.3 `GET /db-check`

**Propósito:**  
Verifica conectividad básica con la base de datos ejecutando una consulta trivial.

**Salida:**  
`{ "db": "ok" }`

---

## 3. Validación de datos (Pydantic)

La validación de entrada se implementa con Pydantic mediante el esquema `IngestPayload`, garantizando coherencia mínima antes de persistir:

- `source`: longitud mínima 1, máxima 64
    
- `severity`: rango 0–10
    
- `message`: longitud mínima 1
    
- `meta`: opcional, JSON arbitrario
    

Esto reduce errores y permite detectar entradas inválidas en fase temprana.

---

## 4. Persistencia y modelo de datos

En la implementación actual:

- Los eventos se almacenan en `events`, incluyendo `meta` como `JSONB`.
    
- Las alertas se almacenan en `alerts`, asociadas a:
    
    - `rule_id`
        
    - `event_id`
        
- Se incluye `group_key` (p.ej. host) para soportar:
    
    - agrupación por origen
        
    - _throttle_ y deduplicación
        

---

## 5. Agrupación por `group_key`

Para aplicar reglas dependientes de agrupación (por ejemplo, por host), se define un `group_key` derivado del evento, tomando como referencia:

- `meta.host` (si existe)
    

Esto permite que el motor trate eventos del mismo host como un conjunto lógico, mejorando la trazabilidad y el control del ruido.

---

## 6. Pruebas manuales realizadas

Se validó el funcionamiento del endpoint mediante pruebas controladas:

- Inserción de reglas en PostgreSQL (`rules`)
    
- Envío de eventos con `curl` hacia `POST /ingest`
    
- Verificación posterior en base de datos:
    
    - inserción en `events`
        
    - generación de registros en `alerts`
        
- Verificación de actualización de estado mediante `PATCH /alerts/{id}` (gestión posterior)
    

Estas pruebas permitieron confirmar el flujo completo:  

**evento → persistencia → evaluación de reglas → alerta**.

---

## 7. Decisiones relevantes y evolución

Durante la implementación se priorizó:

- Mantener el endpoint simple y verificable.
    
- Implementar validación mínima en la entrada.
    
- Asegurar persistencia antes de generar alertas.
    
- Incluir mecanismos básicos de control de ruido (throttle/deduplicación).
    
- Mantener el diseño alineado con el alcance académico del proyecto.
    

---

## 8. Posibles ampliaciones

Este componente permite ampliar el laboratorio sin modificar el núcleo:

- incorporación de fuentes reales (VM Linux / Windows)
    
- envío automático desde agentes o scripts
    
- enriquecimiento de eventos (IP, usuario, proceso)
    
- normalización más avanzada por tipo de fuente
    

Estas ampliaciones se consideran fuera del alcance actual.

---

## Nota sobre el histórico de implementación

La versión anterior de esta nota describía una fase inicial de preparación sin endpoints ni lógica funcional. Dado que el componente ya se encuentra implementado y verificado, ese contenido debe conservarse únicamente como borrador o histórico de planificación, para evitar contradicciones con el estado real del proyecto.

---

Si quieres, hago lo mismo con:

- `02_Motor-de-reglas-implementacion`
    
- `03_Gestion-de-alertas-implementacion`
    

y te lo dejo todo coherente con los comandos que ya ejecutaste (`curl`, `psql`, etc.), sin inventar nada.