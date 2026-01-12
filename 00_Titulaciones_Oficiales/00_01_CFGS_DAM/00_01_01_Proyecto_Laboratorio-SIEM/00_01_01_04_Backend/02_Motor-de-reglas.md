

---

# Motor de reglas

## Laboratorio SIEM

---

## 1. Introducción

En un sistema SIEM, el motor de reglas es el componente encargado de **analizar los eventos almacenados** y detectar situaciones relevantes a partir de condiciones previamente definidas. A diferencia de la API de ingesta, cuyo objetivo es recibir y persistir datos, el motor de reglas introduce **lógica de análisis** sobre la información recopilada.

En el Laboratorio SIEM, el motor de reglas se diseña como un módulo del backend que opera sobre los eventos ya almacenados en la base de datos, permitiendo generar alertas de forma controlada y trazable, acorde al alcance académico del proyecto.

>El motor de reglas del Laboratorio SIEM se implementa como un **módulo interno del backend en Python**, integrado en la misma aplicación FastAPI. Este módulo utiliza **SQLAlchemy 2.0** para consultar eventos y reglas almacenadas en **PostgreSQL**, generar alertas y persistirlas de forma trazable en la base de datos.

>La lógica del motor se ejecuta de forma secuencial y controlada, sin dependencias externas, lo que facilita su comprensión, validación y mantenimiento dentro del alcance del proyecto.

---

## 2. Rol del motor de reglas en el sistema

El motor de reglas es el componente del backend responsable de **interpretar y analizar los eventos almacenados** en la base de datos con el objetivo de identificar situaciones relevantes desde el punto de vista de la seguridad o del funcionamiento del sistema.

Mientras que la API de ingesta se limita a recibir y persistir eventos, el motor de reglas introduce **lógica de decisión**, transformando datos brutos en información procesada mediante la generación de alertas.

Las funciones principales del motor de reglas en el Laboratorio SIEM son las siguientes:

- **Análisis de eventos persistidos**  
    El motor consulta los eventos previamente almacenados en la base de datos, garantizando que el análisis se realice sobre información validada y normalizada.
    
- **Evaluación de condiciones definidas por reglas**  
    Cada regla define una condición lógica que se evalúa sobre uno o varios eventos, permitiendo detectar situaciones específicas previamente definidas.
    
- **Identificación de situaciones relevantes**  
    A partir de la evaluación de las reglas, el motor determina si se ha producido un evento o conjunto de eventos que requiere atención.
    
- **Generación de alertas estructuradas**  
    Cuando una regla se cumple, el motor crea una alerta asociada a dicha regla, asignándole un nivel de severidad y un estado inicial.
    
- **Garantía de trazabilidad**  
    El motor mantiene la relación entre los eventos analizados, la regla aplicada y la alerta generada, permitiendo explicar y auditar cada decisión tomada por el sistema.
    

Desde el punto de vista arquitectónico, el motor de reglas se sitúa **a continuación de la API de ingesta**, utilizando la base de datos como fuente de información, y actúa como paso previo a la gestión y visualización de alertas. Esta posición refuerza la separación entre ingestión de datos, análisis lógico y presentación de resultados.

---

## 3. Concepto de regla en el Laboratorio SIEM

En el Laboratorio SIEM, una **regla** representa una **condición lógica explícita** que define cuándo debe generarse una alerta a partir de los eventos almacenados en el sistema.

Una regla no es un algoritmo complejo, sino una expresión clara y comprensible que permite simular el comportamiento básico de un sistema SIEM real, manteniendo un nivel de complejidad acorde al proyecto.

Cada regla se caracteriza por los siguientes elementos:

- **Nombre identificativo**  
    Permite referenciar la regla de forma clara y estable dentro del sistema.
    
- **Descripción funcional**  
    Explica qué situación pretende detectar la regla y facilita su comprensión.
    
- **Condición lógica**  
    Define el criterio que debe cumplirse para que la regla se active. Esta condición se evalúa sobre los eventos almacenados.
    
- **Nivel de severidad asociado**  
    Indica la importancia o criticidad de la alerta que se generará cuando la regla se cumpla.
    
- **Estado de activación**  
    Permite habilitar o deshabilitar la regla sin  necesidad de eliminarla del sistema.
    

Las reglas se conciben como **expresiones sencillas**, orientadas a detectar situaciones puntuales o patrones básicos, suficientes para demostrar el funcionamiento del motor de reglas dentro de un entorno académico.

---

## 4. Alcance funcional del motor de reglas

El motor de reglas del Laboratorio SIEM se ha diseñado con un alcance funcional **delimitado y controlado**, coherente con los objetivos del proyecto y con el resto de componentes del backend.

>El flujo temporal de procesamiento sigue el orden definido en el diagrama de flujo de datos del laboratorio, siendo la API de ingesta el punto de entrada y el motor de reglas el responsable de la generación de alertas persistentes.

Dentro de su alcance, el motor de reglas incluye:

- La **evaluación de reglas simples** sobre los eventos almacenados en la base de datos.
    
- La **generación de alertas** cuando una condición definida por una regla se cumple.
    
- La **asociación explícita** de cada alerta con los eventos que la han originado.
    
- El **registro persistente** de las alertas y de sus relaciones para su posterior consulta.
    

Quedan explícitamente fuera del alcance del motor de reglas:

- La correlación avanzada entre múltiples fuentes o grandes volúmenes de eventos.
    
- La detección basada en comportamiento, aprendizaje automático o análisis estadístico.
    
- La evaluación de reglas en tiempo real o mediante flujos de eventos continuos.
    
- La gestión compleja de ventanas temporales o umbrales dinámicos.
    

Esta delimitación permite centrar el desarrollo en los principios fundamentales del análisis basado en reglas, evitando una complejidad que no aportaría valor adicional en el contexto del Laboratorio SIEM.

---

## 5. Relación con el modelo de datos

El motor de reglas se apoya directamente en el modelo de datos definido para el sistema, utilizando las tablas relacionales como soporte para el análisis y la persistencia de resultados.

En concreto, el motor interactúa con las siguientes tablas:

- **`events`**  
    Proporciona los eventos sobre los que se aplican las reglas.
    
- **`rules`**  
    Almacena la definición de las reglas que el motor debe evaluar.
    
- **`alerts`**  
    Registra las alertas generadas cuando una regla se cumple.
    
- **`alert_events`**  
    Mantiene la relación entre cada alerta y los eventos que han provocado su activación.
    

Esta integración garantiza que cada alerta generada por el motor pueda ser trazada de forma completa, permitiendo identificar tanto la regla aplicada como los eventos concretos que justifican su existencia. De este modo, el sistema mantiene coherencia, explicabilidad y capacidad de auditoría, aspectos fundamentales en cualquier solución SIEM.

---

## 6. Flujo general de funcionamiento del motor de reglas

El motor de reglas opera siguiendo un **ciclo de evaluación secuencial**, basado en la información persistida en la base de datos. Este enfoque garantiza que el análisis se realice siempre sobre datos coherentes y previamente normalizados.

El flujo general de funcionamiento es el siguiente:

1. **Carga de reglas activas**  
    El motor recupera del sistema únicamente aquellas reglas marcadas como activas. Esta selección permite controlar dinámicamente qué condiciones se evalúan sin modificar la lógica del motor.
    
2. **Obtención del conjunto de eventos a analizar**  
    Para cada regla, el motor consulta la base de datos y obtiene los eventos relevantes según el criterio definido por la propia regla (tipo de evento, severidad, intervalo temporal u otros atributos).
    
3. **Evaluación de condiciones lógicas**  
    El motor evalúa la condición asociada a cada  regla sobre el conjunto de eventos seleccionado. Esta evaluación se realiza de forma determinista, produciendo un resultado binario: la condición se cumple o no se cumple.
    
4. **Creación de la alerta**  
    Cuando una condición se cumple, el motor genera una nueva alerta asociada a la regla evaluada, asignándole un estado inicial y un nivel de severidad previamente definido.
    
5. **Vinculación entre alertas y eventos**  
    La alerta generada se asocia explícitamente con los eventos que han provocado su activación, garantizando que la relación quede registrada y pueda ser consultada posteriormente.
    
6. **Persistencia de resultados**  
    Tanto la alerta como sus relaciones con los eventos se almacenan de forma persistente en la base de datos, cerrando el ciclo de evaluación.
    

Este flujo asegura que el comportamiento del motor de reglas sea **predecible, repetible y alineado con el modelo de datos**, evitando decisiones implícitas o no trazables.

---

## 7. Consideraciones de diseño del motor de reglas

El diseño del motor de reglas se apoya en una serie de consideraciones técnicas que condicionan su funcionamiento y su integración con el resto del sistema.

- **Evaluación basada en estado persistente**  
    El motor trabaja exclusivamente sobre eventos almacenados en la base de datos, evitando el análisis de datos transitorios y garantizando consistencia entre ejecuciones.
    
- **Separación clara entre datos y lógica**  
    Las reglas definen _qué_ se debe detectar, mientras que el motor implementa _cómo_ se evalúan dichas reglas. Esta separación facilita el mantenimiento y la extensibilidad del sistema.
    
- **Trazabilidad completa de decisiones**  
    Cada alerta generada puede explicarse a partir de:
    
    - la regla evaluada,
        
    - los eventos implicados,
        
    - y el momento en que se produjo la evaluación.
        
- **Persistencia como principio central**  
    Todas las decisiones relevantes del motor  quedan registradas en la base de datos, evitando estados implícitos en memoria y permitiendo auditoría posterior.
    
- **Control del ciclo de ejecución**  
    El motor no se ejecuta de forma continua ni reactiva, sino como un proceso controlado, lo que simplifica su comportamiento y reduce la complejidad del sistema.
    

Estas consideraciones permiten un diseño robusto y comprensible, alineado con los objetivos formativos del proyecto.

---

## 8. Limitaciones técnicas del motor de reglas

El motor de reglas presenta una serie de limitaciones técnicas asumidas de forma consciente, derivadas tanto del alcance académico del proyecto como de las decisiones de diseño adoptadas.

Entre estas limitaciones se incluyen:

- **Ausencia de evaluación en tiempo real**  
    El motor no procesa eventos conforme llegan, sino que analiza eventos ya persistidos.
    
- **Reglas sin correlación avanzada**  
    No se implementan correlaciones complejas entre múltiples fuentes, ni análisis de comportamiento prolongado.
    
- **Motor de reglas propio y simplificado**  
    No se utilizan motores de reglas externos ni lenguajes especializados, priorizando la claridad frente a la potencia expresiva.
    
- **Escalabilidad limitada**  
    El diseño no está orientado a gestionar grandes volúmenes de eventos concurrentes ni cargas elevadas.
    

Estas limitaciones no se consideran deficiencias, sino **decisiones de alcance**, que permiten centrar el proyecto en los fundamentos del análisis basado en reglas y dejar abiertas posibles líneas de evolución futura.

---