

---

# Arquitectura general del sistema

## Laboratorio SIEM

---

## Introducción

En este apartado se describe la **arquitectura general del Laboratorio SIEM**, definiendo los principales componentes del sistema, sus responsabilidades y la forma en que interactúan entre sí dentro de un entorno de laboratorio virtualizado.

El objetivo de este capítulo es proporcionar una **visión global y estructurada del diseño del sistema**, que sirva como referencia para comprender el funcionamiento del laboratorio y como base para los apartados posteriores, donde se detallará cada componente de manera específica a nivel de diseño e implementación.

---

## Enfoque arquitectónico

El sistema se ha diseñado siguiendo una **arquitectura modular**, en la que cada componente del laboratorio cumple una función concreta y bien delimitada. Desde el punto de vista lógico, el sistema presenta una organización distribuida, aunque su despliegue se realiza de forma centralizada dentro de un entorno de laboratorio controlado.

Este enfoque facilita la comprensión del sistema, su mantenimiento y su posible evolución futura, permitiendo añadir o modificar componentes sin alterar la estructura base del laboratorio.

La arquitectura adopta un modelo **cliente–servidor**, donde un backend centralizado actúa como núcleo del sistema SIEM, gestionando la ingesta, el procesamiento y el almacenamiento de eventos, mientras que las fuentes de eventos y la interfaz web interactúan con este núcleo mediante mecanismos controlados.

Desde el punto de vista del despliegue, el laboratorio se apoya en un entorno **virtualizado**, utilizando varias máquinas virtuales con roles diferenciados. Esta separación permite simular un entorno representativo de monitorización de seguridad, adecuado para el contexto académico del proyecto, manteniendo un alto grado de control y aislamiento entre los distintos elementos.

---

## Componentes principales del sistema

### Fuentes de eventos

Las fuentes de eventos representan los sistemas que generan información susceptible de análisis por parte del SIEM. Estas fuentes se despliegan en máquinas virtuales independientes y forman parte de un entorno de laboratorio controlado.

Ejemplos de fuentes de eventos contempladas en el proyecto incluyen:

- Sistemas Linux, que generan eventos relacionados con autenticaciones, accesos y errores del sistema.
    
- Sistemas Windows, que generan eventos básicos del sistema operativo y de seguridad.
    
- Servicios de red simulados, que permiten generar patrones de acceso o intentos fallidos de forma controlada.
    

Las fuentes de eventos **no forman parte directa del sistema SIEM**, ya que no implementan lógica de análisis ni almacenamiento. Su función se limita a la generación y envío de eventos hacia el sistema central.

En la fase actual del proyecto, estas fuentes pueden generar eventos reales o simulados, siendo el objetivo principal validar el flujo de ingesta, análisis y generación de alertas. La incorporación de agentes específicos o mecanismos automáticos de envío de eventos se plantea como una posible evolución futura.

---

### Módulo de ingesta de eventos

El módulo de ingesta constituye el **punto de entrada único** al sistema SIEM. Su función es recibir los eventos generados por las distintas fuentes a través de una **API REST**, actuando como frontera entre el exterior y el núcleo del sistema.

Las responsabilidades principales de este módulo son:

- Recepción de eventos en formato estructurado (JSON).
    
- Validación básica de los datos recibidos para asegurar su coherencia mínima.
    
- Rechazo de eventos inválidos o incompletos.
    
- Encaminamiento de los eventos hacia los procesos internos del sistema.
    

Este diseño evita el acceso directo a la base de datos desde las fuentes de eventos y permite centralizar el control del flujo de información.

---

### Proceso de normalización

El proceso de normalización se integra dentro del backend del sistema y se encarga de **unificar los eventos recibidos** en un modelo de datos común, independientemente de su origen o formato original.

Entre sus funciones principales se encuentran:

- Transformación de eventos heterogéneos a una estructura homogénea.
    
- Asignación de campos comunes, como fecha, origen, mensaje y nivel de severidad.
    
- Preparación del evento para su almacenamiento y posterior análisis.
    

Este proceso garantiza la coherencia de los datos almacenados y permite que el motor de reglas trabaje sobre información homogénea.

---

### Módulo de análisis y reglas

El módulo de análisis implementa la **lógica principal del sistema SIEM**, aplicando un conjunto de reglas sencillas sobre los eventos almacenados.

Sus responsabilidades incluyen:

- Evaluación de eventos en función de reglas predefinidas.
    
- Detección de patrones básicos, como la repetición de eventos dentro de un intervalo temporal.
    
- Identificación de situaciones potencialmente relevantes desde el punto de vista de la seguridad.
    

Las reglas se diseñan con un enfoque didáctico, adaptado al contexto académico del proyecto, y no pretenden replicar sistemas avanzados de correlación industrial.

---

### Gestión de alertas

El módulo de gestión de alertas se encarga de administrar las alertas generadas como resultado del análisis de eventos.

Sus funciones principales son:

- Creación y almacenamiento de alertas.
    
- Gestión del estado de las alertas (abierta, reconocida o cerrada).
    
- Asociación de cada alerta con el evento que la ha originado.
    

Este componente permite simular un flujo básico de tratamiento de incidentes, alineado con el funcionamiento de un SIEM real.

---

### Persistencia de datos

La persistencia de datos garantiza el almacenamiento centralizado de la información generada y procesada por el sistema, incluyendo:

- Eventos normalizados.
    
- Alertas generadas por el motor de reglas.
    
- Información auxiliar necesaria para el funcionamiento del sistema.
    

Para este fin se utiliza una **base de datos relacional**, desplegada como servicio dentro del nodo central del sistema. Esta solución es adecuada tanto para el alcance funcional del proyecto como para su contexto académico.

---

### Interfaz web

La interfaz web actúa como **punto de visualización e interacción** con el sistema SIEM.

A través de esta interfaz, el usuario puede:

- Consultar eventos recientes almacenados en el sistema.
    
- Visualizar las alertas activas.
    
- Acceder al detalle de cada alerta.
    
- Modificar el estado de las alertas.
    

La interfaz se mantiene deliberadamente simple y funcional, priorizando la claridad de la información y la comprensión del flujo de trabajo del sistema frente a la complejidad visual.

---