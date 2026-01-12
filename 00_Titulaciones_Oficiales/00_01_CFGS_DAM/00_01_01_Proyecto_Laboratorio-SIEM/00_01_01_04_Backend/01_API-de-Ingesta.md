

---

# API de Ingesta de Eventos

## Laboratorio SIEM

---

## 1. Introducción

El Laboratorio SIEM se apoya en un backend encargado de gestionar el ciclo de vida de los eventos generados en el entorno de laboratorio. Este backend constituye el núcleo funcional del sistema y es responsable de garantizar que la información recibida sea coherente, estructurada y persistente.

Dentro de este backend, la **API de ingesta de eventos** actúa como el punto de entrada del sistema, permitiendo que las máquinas virtuales Linux y Windows envíen eventos de forma controlada. Su diseño responde a la necesidad de integrar fuentes heterogéneas en una arquitectura común, manteniendo un alcance ajustado al contexto académico del proyecto.

En este apartado se contextualiza el papel de la API dentro del sistema y se justifica su uso como elemento clave del diseño.

>La API de ingesta del Laboratorio SIEM se implementa como una **API REST desarrollada en Python mediante el framework FastAPI**, ejecutada sobre el servidor ASGI **Uvicorn**. La persistencia de los eventos se realiza en una base de datos **PostgreSQL**, utilizando **SQLAlchemy 2.0** como capa de acceso a datos y **Alembic** para la gestión de migraciones del esquema.

>Las pruebas funcionales de la API se realizan mediante **Postman**, lo que permite simular el envío de eventos desde distintas fuentes sin necesidad de desarrollar clientes específicos.

---

## 2. Rol del backend en el Laboratorio SIEM

En el Laboratorio SIEM, el backend asume la función de **capa lógica central**, coordinando la comunicación entre las fuentes de eventos, la base de datos y los módulos de análisis y visualización.

Sus responsabilidades principales son:

- Recibir eventos procedentes de las máquinas virtuales que actúan como fuentes del laboratorio.
    
- Transformar dichos eventos a un formato común definido por el modelo de datos.
    
- Almacenar la información de forma persistente en la base de datos PostgreSQL.
    
- Proporcionar datos estructurados al motor de reglas y a la interfaz web.
    

Desde el punto de vista arquitectónico, el backend permite separar claramente la generación de eventos del procesamiento y almacenamiento de los mismos, evitando dependencias directas entre componentes y facilitando la evolución del sistema.

---

## 3. Concepto de API en el contexto del proyecto

Una **API** (_Application Programming Interface_) es un mecanismo que permite la comunicación entre distintos sistemas mediante un conjunto de reglas previamente definidas. En lugar de acceder directamente a los recursos internos de una aplicación, los clientes interactúan con ella a través de esta interfaz.

En el contexto concreto del Laboratorio SIEM, la API:

- Define el formato y la estructura de los eventos que pueden ser enviados al sistema.
    
- Establece un punto de entrada único para todas las fuentes del laboratorio.
    
- Controla cómo se aceptan, procesan o rechazan los datos recibidos.
    

Este enfoque permite aislar la lógica interna del sistema de las fuentes externas, mejorando la mantenibilidad y reduciendo el acoplamiento entre componentes.

---

## 4. Necesidad de una API de ingesta en el Laboratorio SIEM

La API de ingesta no es un elemento accesorio, sino una pieza fundamental del diseño del sistema. Su uso responde a necesidades concretas del Laboratorio SIEM:

- **Unificación de fuentes heterogéneas**  
    Los eventos generados por sistemas Linux y Windows presentan formatos y características distintas. La API permite recibirlos de forma homogénea y tratarlos de manera uniforme.
    
- **Control del flujo de datos**  
    Centralizar la ingesta evita accesos directos a la base de datos y permite aplicar validaciones y transformaciones antes de almacenar la información.
    
- **Coherencia con el modelo de datos**  
    La API actúa como garante de que los eventos almacenados cumplen el esquema definido, respetando las relaciones y restricciones del sistema.
    
- **Alineación con el enfoque académico del proyecto**  
    El uso de una API permite aplicar conceptos clave del desarrollo de software, como la definición de interfaces, la validación de datos y la separación de responsabilidades, sin introducir complejidad innecesaria.
    

En consecuencia, la API de ingesta se convierte en el primer componente del flujo de datos del sistema, conectando las fuentes de eventos con la capa de persistencia y preparando la información para su análisis posterior.

---

## 5. Objetivo de la API de ingesta

El objetivo de la API de ingesta del Laboratorio SIEM es actuar como **punto de entrada controlado** para los eventos generados en el entorno de laboratorio, garantizando que dichos eventos se integren de forma coherente con la arquitectura, el modelo de datos y el alcance funcional del proyecto.

En el contexto concreto de este sistema, la API tiene como finalidad:

- Recibir eventos generados por las **máquinas virtuales Linux y Windows** que actúan como fuentes del laboratorio, simulando equipos de una red empresarial básica.
    
- Validar que los eventos recibidos contienen la información mínima necesaria para ser procesados y almacenados, evitando la inserción de datos incompletos o inconsistentes.
    
- Normalizar los eventos a un **formato común**, independientemente de su origen, de manera que todos los registros almacenados sigan una estructura homogénea definida por el esquema de base de datos.
    
- Asignar valores normalizados relevantes para el análisis posterior, como el tipo de evento o su nivel de severidad, siguiendo criterios simples y acordes al alcance académico del proyecto.
    
- Persistir los eventos en la base de datos PostgreSQL respetando las relaciones y restricciones definidas, asegurando la trazabilidad entre eventos y sus fuentes.
    
- Proporcionar una respuesta clara a las fuentes emisoras, indicando si el evento ha sido aceptado y almacenado correctamente o si se ha producido un error durante el proceso.
    

De este modo, la API de ingesta se convierte en el **primer eslabón del flujo de datos del Laboratorio SIEM**, conectando las fuentes de eventos con la capa de persistencia y dejando preparados los datos para su análisis por el motor de reglas y su posterior visualización.

---

## 6. Alcance funcional de la API

La API de ingesta del Laboratorio SIEM se ha diseñado con un **alcance funcional deliberadamente acotado**, coherente con los objetivos formativos del proyecto y con la arquitectura definida para el entorno de laboratorio.

En concreto, la API se encarga de las siguientes funciones:

- **Recepción de eventos individuales** generados por las máquinas virtuales Linux y Windows que actúan como fuentes del laboratorio.
    
- **Validación básica de la estructura de los datos recibidos**, comprobando la presencia de los campos mínimos necesarios para su tratamiento.
    
- **Normalización de los eventos** a un formato común, alineado con el esquema de la base de datos.
    
- **Persistencia de los eventos normalizados** en la base de datos PostgreSQL, respetando las relaciones y restricciones definidas.
    

Este conjunto de funcionalidades permite cubrir el ciclo inicial de vida de un evento dentro del sistema, desde su generación hasta su almacenamiento, sin introducir lógica avanzada que no sea necesaria para el propósito del proyecto.

Quedan explícitamente fuera del alcance de la API de ingesta:

- Mecanismos de **autenticación avanzada** o gestión de identidades.
    
- **Control de acceso complejo** o autorización basada en roles.
    
- Procesamiento de eventos en **tiempo real** o mediante flujos de streaming.
    
- Integración con sistemas externos o plataformas SIEM comerciales.
    

Esta delimitación funcional permite centrar el desarrollo en los conceptos esenciales del backend, evitando una complejidad que no aportaría valor adicional en el contexto académico del Laboratorio SIEM.

---

## 7. Relación con otros componentes del sistema

La API de ingesta se integra con el resto de componentes del Laboratorio SIEM siguiendo el flujo lógico definido en la arquitectura y la topología del sistema.

Su papel dentro del conjunto es el siguiente:

- **Fuentes de eventos**  
    Las máquinas virtuales Linux y Windows envían  los eventos a la API como único punto de entrada al sistema.
    
- **Base de datos**  
    La API es responsable de insertar los eventos validados y normalizados en la base de datos PostgreSQL, garantizando la coherencia del modelo de datos y la trazabilidad de la información.
    
- **Motor de reglas**  
    El motor de reglas accede a los eventos almacenados en la base de datos, que han sido previamente procesados por la API, para realizar el análisis y la detección de patrones.
    
- **Interfaz web**  
    Aunque la interfaz web no interactúa directamente con la API de ingesta, se beneficia indirectamente de su funcionamiento, ya que los eventos y alertas visualizados proceden de datos gestionados por esta.
    

De este modo, la API de ingesta actúa como **componente de enlace** entre las fuentes de eventos y el núcleo del backend, asegurando un flujo de datos controlado y coherente con el diseño global del Laboratorio SIEM.

---

## 8. Diseño de la API de ingesta

La API de ingesta del Laboratorio SIEM se ha diseñado como una **API REST sencilla**, orientada a la recepción de eventos individuales enviados desde las máquinas virtuales que actúan como fuentes del sistema.

Desde el punto de vista arquitectónico, la API constituye la **capa de entrada del backend**, actuando como intermediaria entre las fuentes de eventos y la base de datos. Todas las decisiones de diseño se han tomado para garantizar coherencia con el modelo de datos, facilidad de implementación y claridad conceptual.

En los siguientes subapartados se describen los principios técnicos adoptados, el endpoint definido, el formato de los datos intercambiados, las validaciones aplicadas y el flujo interno de procesamiento.

---

### 8.1 Principios de diseño

El diseño de la API se rige por los siguientes principios técnicos:

- **API REST orientada a recursos**  
    Los eventos se tratan como recursos del sistema, utilizando el método HTTP adecuado (`POST`) para su creación.
    
- **Punto de entrada único**  
    Todas las fuentes envían los eventos a un único endpoint, lo que simplifica el control del flujo de datos y evita lógicas de ingesta dispersas.
    
- **Procesamiento síncrono**  
    Cada petición se procesa de forma síncrona: el evento se valida, normaliza y almacena antes de devolver una respuesta. No se utilizan colas ni mecanismos asíncronos.
    
- **Validación previa a persistencia**  
    Ningún evento se almacena en la base de datos sin haber superado previamente las validaciones mínimas definidas por la API.
    
- **Independencia del origen**  
    La API no depende de si el evento procede de Linux o Windows; ambos se tratan de forma uniforme una vez recibidos.
    
- **Ajuste al contexto académico**  
    No se incluyen mecanismos avanzados como autenticación JWT, versionado de endpoints o balanceo de carga, ya que no son necesarios para cumplir los objetivos del proyecto.
    

---

### 8.2 Endpoint de ingesta

La API expone un único endpoint responsable de la recepción de eventos:

```
POST /api/events
```

Desde el punto de vista técnico:

- El método `POST` indica la creación de un nuevo recurso en el sistema.
    
- La ruta `/api/events` representa la colección de eventos gestionados por el backend.
    
- Cada petición corresponde a **un único evento**, lo que simplifica la validación y la trazabilidad.
    

El endpoint espera recibir los datos del evento en el cuerpo de la petición HTTP y devuelve una respuesta estructurada indicando el resultado de la operación, incluyendo códigos de estado HTTP adecuados (por ejemplo, éxito o error de validación).

---

### 8.3 Estructura de los datos recibidos

Los eventos se envían a la API en formato **JSON**, que actúa como contrato de comunicación entre las fuentes y el backend.

A nivel técnico, la estructura de los datos recibidos se diseña para:

- Representar la información mínima necesaria para un evento.
    
- Ser fácilmente mapeable a los campos de la tabla `events`.
    
- Permitir extensiones futuras sin romper el formato base.
    

Un evento incluye conceptualmente:

- Un identificador o nombre de la fuente.
    
- Un tipo de evento que permita su clasificación.
    
- Una marca temporal que indique cuándo ocurrió el suceso.
    
- Un mensaje descriptivo.
    
- Información adicional opcional, almacenada como metadatos.
    

Este diseño garantiza una correspondencia directa entre la API y el esquema físico de la base de datos, evitando transformaciones complejas.

---

### 8.4 Validaciones básicas

La API aplica validaciones técnicas antes de persistir cualquier evento, actuando como **primer nivel de control de calidad** de los datos.

Las validaciones incluyen:

- **Validación estructural**  
    Comprobación de que el cuerpo de la petición es un JSON válido y contiene los campos obligatorios.
    
- **Validación de tipos**  
    Verificación de que los campos recibidos tienen el tipo de dato esperado (texto, fecha, valores numéricos).
    
- **Validación referencial**  
    Comprobación de que la fuente indicada existe previamente en la tabla `sources`.
    
- **Normalización de valores**  
    Asignación de valores por defecto cuando ciertos campos no se especifican (por ejemplo, severidad).
    

Si una validación falla, la API devuelve un error y **no se realiza ninguna operación de escritura en la base de datos**, garantizando la coherencia del sistema.

---

### 8.5 Flujo interno de procesamiento

El procesamiento interno de un evento dentro de la API sigue una secuencia técnica bien definida:

1. Recepción de la petición HTTP en el endpoint `/api/events`.
    
2. Verificación de que el cuerpo de la petición es válido y parseable.
    
3. Aplicación de las validaciones estructurales y referenciales.
    
4. Normalización de los datos al formato interno del sistema.
    
5. Inserción del evento en la base de datos PostgreSQL.
    
6. Generación de la respuesta HTTP correspondiente.
    

Este flujo asegura que todos los eventos almacenados cumplen el esquema definido y están preparados para ser utilizados por el motor de reglas sin procesamiento adicional.

---

## 9. Consideraciones de implementación

La implementación de la API de ingesta se realiza dentro de la máquina virtual asignada al backend SIEM y se apoya directamente en el esquema de base de datos definido previamente.

Desde un punto de vista técnico:

- La API encapsula la lógica de validación y persistencia.
    
- El acceso a la base de datos se realiza mediante una capa de persistencia claramente separada.
    
- El diseño favorece la legibilidad del código frente a la optimización prematura.
    
- La estructura del backend permite añadir nuevas validaciones o campos sin modificar el contrato básico de la API.
    

Estas decisiones facilitan el desarrollo progresivo y la comprensión del sistema.

---

## 10. Limitaciones del diseño

El diseño de la API asume conscientemente una serie de limitaciones técnicas:

- No se implementan mecanismos de autenticación ni autorización.
    
- No se gestiona alta concurrencia ni grandes volúmenes de eventos.
    
- No se utilizan colas, streaming ni procesamiento en tiempo real.
    
- No se implementa versionado de la API.
    
- No se contemplan mecanismos de alta disponibilidad.
    

Estas limitaciones son coherentes con el alcance académico del proyecto y permiten centrar el desarrollo en los fundamentos del backend y del funcionamiento básico de un sistema SIEM, dejando abiertas posibles ampliaciones futuras.

---
