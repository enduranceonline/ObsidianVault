

---

# Arquitectura general del sistema  
## Laboratorio SIEM

---

## Introducción

En este apartado se describe la **arquitectura general del Laboratorio SIEM**, definiendo los principales componentes del sistema, sus responsabilidades y la forma en que interactúan entre sí.

El objetivo de este capítulo es ofrecer una **visión global del diseño del sistema**, sirviendo como base para los apartados posteriores donde se detallará cada componente de manera específica.

---

## Enfoque arquitectónico

El sistema se ha diseñado siguiendo una **arquitectura modular**, separando claramente las responsabilidades de cada componente. Este enfoque facilita la comprensión del sistema, su mantenimiento y su posible evolución futura.

La arquitectura se basa en un modelo **cliente–servidor**, donde un backend central gestiona la lógica del sistema y una interfaz web permite la interacción con el usuario.

---

## Componentes principales del sistema

### • Fuentes de eventos

Las fuentes de eventos representan los sistemas que generan información susceptible de análisis. En el contexto del proyecto, estas fuentes pertenecen a un entorno de laboratorio controlado.

Ejemplos de fuentes de eventos:
- Sistemas Linux (eventos de autenticación, accesos, errores).
- Sistemas Windows (eventos básicos del sistema).
- Servicios de red simulados (accesos repetidos, intentos fallidos).

Estas fuentes no forman parte directa del sistema desarrollado, pero son esenciales para proporcionar datos reales al Laboratorio SIEM.

---

### • Módulo de ingesta de eventos

El módulo de ingesta es el punto de entrada del sistema. Su función es **recibir eventos de seguridad** procedentes de las distintas fuentes mediante una API REST.

Responsabilidades principales:
- Recepción de eventos en formato estructurado.
- Validación básica de los datos recibidos.
- Envío de los eventos al proceso de normalización.

---

### • Módulo de normalización

El módulo de normalización se encarga de **unificar los eventos recibidos** en un modelo de datos común, independientemente de su origen.

Funciones principales:
- Transformación de formatos heterogéneos.
- Asignación de campos estándar (fecha, origen, tipo, severidad).
- Preparación del evento para su almacenamiento y análisis.

Este componente es clave para garantizar la coherencia del sistema.

---

### • Módulo de análisis y reglas

Este módulo implementa la **lógica de análisis del sistema**, aplicando un conjunto de reglas simples sobre los eventos almacenados.

Responsabilidades:
- Evaluación de eventos según reglas predefinidas.
- Detección de patrones básicos (por ejemplo, repetición de eventos).
- Generación de alertas cuando se cumplen las condiciones establecidas.

Las reglas se diseñan con fines didácticos y no pretenden replicar mecanismos avanzados de correlación.

---

### • Gestión de alertas

El módulo de gestión de alertas se encarga de administrar las alertas generadas por el sistema.

Funciones principales:
- Almacenamiento de alertas.
- Gestión de estados (abierta, cerrada).
- Asociación opcional de alertas a eventos relacionados.

Este componente permite simular un flujo básico de tratamiento de incidentes.

---

### • Persistencia de datos

La persistencia de datos garantiza el almacenamiento de:
- Eventos normalizados.
- Alertas generadas.
- Información auxiliar del sistema.

Se utiliza una base de datos relacional, adecuada al alcance del proyecto y al contexto académico.

---

### • Interfaz web

La interfaz web actúa como **punto de visualización e interacción** con el sistema.

Permite al usuario:
- Consultar eventos recientes.
- Visualizar alertas activas.
- Acceder al detalle de cada alerta.
- Modificar el estado de las alertas.

La interfaz se mantiene simple y funcional, priorizando la claridad de la información.

---

Perfecto, aquí tienes una **reescritura completa**, más clara, menos telegráfica y **alineada explícitamente con el diagrama**, sin repetir lo ya evidente y con un tono académico sólido.  
Puedes **sustituir directamente** el bloque que has pegado por este.

---

## Flujo general del sistema

El Laboratorio SIEM se estructura en torno a un **flujo de datos secuencial y modular**, cuyo objetivo es transformar eventos generados en el entorno de laboratorio en información útil para su análisis y visualización. Este flujo se representa de forma esquemática en la **Figura 2**.

### Figura 2. Flujo de datos del Laboratorio SIEM

[[00_Titulaciones_Oficiales/00_01_CFGS_DAM/00_01_01_Proyecto_Laboratorio-SIEM/00_01_01_09_Anexos/Diagramas/02_Flujo_Datos_SIEM.excalidraw.md|02_Flujo_Datos_SIEM.excalidraw]]

El funcionamiento general del sistema es el siguiente:

1. **Generación de eventos**  
    Los sistemas del entorno de laboratorio (máquinas Linux y Windows) generan eventos relacionados con la actividad del sistema, como autenticaciones o eventos del propio sistema operativo.
    
2. **Ingesta de eventos**  
    Los eventos son recibidos por la **API de ingesta**, que actúa como punto de entrada único al sistema. En esta fase se realiza una validación básica para asegurar que los datos cumplen un formato mínimo esperado.
    
3. **Normalización**  
    Los eventos recibidos se transforman a un formato común mediante el módulo de normalización. Este proceso permite unificar estructuras heterogéneas y asignar niveles de severidad, facilitando su posterior análisis.
    
4. **Persistencia de datos**  
    Los eventos normalizados se almacenan en la **base de datos**, que constituye el núcleo del sistema. En ella se mantienen de forma centralizada los eventos, las reglas definidas y las alertas generadas.
    
5. **Análisis mediante reglas**  
    El **motor de reglas** consulta los eventos almacenados y evalúa si se cumplen las condiciones definidas. Este análisis permite detectar patrones relevantes o comportamientos anómalos dentro del conjunto de eventos.
    
6. **Generación y gestión de alertas**  
    Cuando una regla se activa, se generan alertas que son gestionadas por el módulo correspondiente. Este módulo se encarga de crear las alertas y mantener su estado (por ejemplo, abierta o cerrada), almacenando la información resultante en la base de datos.
    
7. **Visualización**  
    La **interfaz web (dashboard)** accede a la base de datos para mostrar al usuario los eventos y alertas de forma estructurada, permitiendo una visualización clara del estado del sistema y una gestión básica de la información.
    

Este flujo representa el comportamiento esencial de un sistema SIEM a pequeña escala, manteniendo un equilibrio entre realismo funcional y simplicidad acorde al alcance académico del proyecto.

---

## Consideraciones de diseño

El diseño del sistema se ha planteado teniendo en cuenta los siguientes criterios:

- **Simplicidad y claridad arquitectónica**, priorizando un flujo comprensible y fácil de seguir.
    
- **Separación de responsabilidades**, asignando a cada módulo una función concreta dentro del sistema.
    
- **Facilidad de mantenimiento y ampliación**, permitiendo introducir mejoras o nuevas funcionalidades sin alterar la estructura base.
    
- **Adecuación al contexto académico del ciclo DAM**, evitando una complejidad innecesaria y centrándose en los conceptos fundamentales.
    

Estas consideraciones garantizan que el sistema sea coherente, didáctico y alineado con los objetivos formativos del proyecto.

---