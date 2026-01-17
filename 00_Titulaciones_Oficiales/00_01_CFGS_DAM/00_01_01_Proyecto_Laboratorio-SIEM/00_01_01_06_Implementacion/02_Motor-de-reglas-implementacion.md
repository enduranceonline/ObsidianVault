

---

# Motor de Reglas (Implementación)

## Laboratorio SIEM

Referencia de diseño y decisiones previas:  
[[00_Titulaciones_Oficiales/00_01_CFGS_DAM/00_01_01_Proyecto_Laboratorio-SIEM/00_01_01_04_Backend/02_Motor-de-reglas.md|00_01_01_04_Backend/02_Motor-de-reglas.md]]

---

## 1. Objetivo del componente

El motor de reglas implementa la **lógica de detección del Laboratorio SIEM**, evaluando los eventos almacenados en el sistema y determinando si deben generar alertas.

Su objetivo principal es transformar eventos individuales en **alertas significativas**, aplicando un conjunto de reglas configurables y mecanismos básicos de control de ruido, manteniendo un enfoque didáctico y alineado con el alcance del proyecto.

---

## 2. Integración dentro del backend

El motor de reglas **no se implementa como un servicio independiente**, sino que se integra directamente en el backend del sistema, formando parte del flujo de procesamiento iniciado por la API de Ingesta.

El proceso de evaluación de reglas se ejecuta inmediatamente después de persistir un evento, garantizando que:

- El evento siempre existe en base de datos antes de ser analizado.
    
- La generación de alertas es trazable y reproducible.
    
- El sistema mantiene un flujo claro y secuencial.
    

---

## 3. Activación del motor de reglas

El motor se activa como parte del endpoint:

```
POST /ingest
```

El flujo simplificado es el siguiente:

1. Recepción y validación del evento.
    
2. Persistencia del evento en la tabla `events`.
    
3. Recuperación de las reglas activas (`enabled = true`).
    
4. Evaluación secuencial de cada regla.
    
5. Generación de alertas cuando se cumplen las condiciones.
    

Este enfoque evita procesos asíncronos o complejos, priorizando la claridad y el control del comportamiento del sistema.

---

## 4. Criterios de evaluación de reglas

Cada regla se evalúa aplicando de forma secuencial los siguientes criterios, cuando están definidos:

### 4.1 Origen (`source`)

Si la regla define un origen concreto, el evento debe coincidir exactamente con dicho valor.

Esto permite limitar reglas a tipos específicos de eventos (por ejemplo, `ssh`, `syslog`).

---

### 4.2 Severidad mínima (`severity_min`)

El evento debe tener una severidad igual o superior al valor definido en la regla.

Este criterio permite filtrar eventos de baja relevancia.

---

### 4.3 Contenido del mensaje (`contains`)

Si se define, el texto indicado debe aparecer en el mensaje del evento.

La comparación se realiza de forma insensible a mayúsculas/minúsculas.

---

### 4.4 Coincidencia de metadatos (`meta_match`)

Permite definir coincidencias exactas sobre campos concretos de los metadatos del evento.

Este mecanismo facilita reglas dependientes de atributos como el host o el usuario, sin necesidad de normalizar todos los campos.

---

## 5. Agrupación lógica de eventos (`group_key`)

Para determinadas reglas, el motor utiliza una **clave de agrupación** (`group_key`) derivada del evento, normalmente a partir de:

- `meta.host`
    

Esta clave permite tratar eventos procedentes del mismo origen como un conjunto lógico, facilitando mecanismos como:

- control de repetición,
    
- aplicación de umbrales,
    
- reducción de alertas redundantes.
    

Si no se dispone de información suficiente para calcular la clave, el evento se evalúa como individual.

---

## 6. Mecanismos de control de ruido

Con el objetivo de evitar la generación excesiva de alertas, el motor incorpora los siguientes mecanismos:

### 6.1 Throttling temporal

Si una regla define un intervalo de _throttle_, el motor comprueba si existe una alerta activa reciente (estado `open` o `ack`) para la misma regla y grupo.

Si el intervalo no se ha cumplido, no se genera una nueva alerta.

---

### 6.2 Anti-duplicación de alertas

Independientemente del _throttle_, si ya existe una alerta activa para la misma combinación de regla y grupo, no se crea una nueva alerta.

Este mecanismo evita alertas duplicadas cuando un problema persiste en el tiempo.

---

## 7. Reglas con umbral (`threshold`)

El motor permite definir reglas basadas en umbrales temporales, mediante:

- `threshold_count`
    
- `threshold_seconds`
    

En estos casos:

1. Se define una ventana temporal hacia atrás.
    
2. Se cuentan los eventos que cumplen los criterios de la regla.
    
3. Solo se genera una alerta si el número de eventos alcanza el umbral definido.
    

Este mecanismo permite detectar patrones simples, como múltiples intentos fallidos en un corto periodo de tiempo.

---

## 8. Generación de alertas

Cuando una regla se cumple:

- Se crea un registro en la tabla `alerts`.
    
- La alerta queda asociada:
    
    - a la regla que la generó (`rule_id`)
        
    - al evento que provocó la evaluación (`event_id`)
        
- El estado inicial de la alerta es `open`.
    

Cada alerta representa una situación que requiere atención y puede ser gestionada posteriormente por el usuario.

---

## 9. Decisiones de diseño relevantes

Durante la implementación del motor de reglas se tomaron las siguientes decisiones:

- Evaluación secuencial y determinista de reglas.
    
- Persistencia del evento antes de cualquier análisis.
    
- Integración directa en el backend, sin procesos externos.
    
- Control de ruido mediante mecanismos simples y verificables.
    
- Prioridad a la trazabilidad frente a la complejidad.
    

Estas decisiones permiten un comportamiento predecible y fácil de analizar, adecuado para un entorno formativo.

---

## 10. Limitaciones y alcance

El motor de reglas implementado:

- No realiza correlación avanzada entre múltiples tipos de eventos.
    
- No utiliza técnicas heurísticas ni aprendizaje automático.
    
- No ejecuta evaluaciones asíncronas o distribuidas.
    

Estas limitaciones son **deliberadas** y coherentes con el alcance académico del proyecto.

---

## 11. Posibles ampliaciones

El diseño actual permite evolucionar el motor en el futuro mediante:

- Correlación más compleja entre eventos.
    
- Reglas dependientes de múltiples atributos.
    
- Evaluación asíncrona o por lotes.
    
- Integración con fuentes externas de inteligencia.
    

Estas ampliaciones se consideran fuera del alcance del presente proyecto.

---

## Nota sobre la coherencia documental

Esta nota documenta exclusivamente funcionalidades **implementadas y verificadas** en el backend del Laboratorio SIEM. No se describen comportamientos teóricos ni componentes no desarrollados, garantizando coherencia entre documentación y código.

---