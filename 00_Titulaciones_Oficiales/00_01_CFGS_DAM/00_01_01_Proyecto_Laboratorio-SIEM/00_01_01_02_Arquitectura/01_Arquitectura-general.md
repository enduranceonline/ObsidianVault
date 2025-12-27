

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

## Flujo general del sistema

El funcionamiento del sistema sigue el siguiente flujo:

1. Generación de eventos en el entorno de laboratorio.
2. Recepción de eventos por el módulo de ingesta.
3. Normalización de los eventos.
4. Almacenamiento en la base de datos.
5. Análisis mediante reglas.
6. Generación de alertas.
7. Visualización a través de la interfaz web.

Este flujo refleja el comportamiento esencial de un sistema SIEM a pequeña escala.

---

## Consideraciones de diseño

El diseño del sistema ha tenido en cuenta los siguientes aspectos:

- Simplicidad y claridad arquitectónica.
- Separación de responsabilidades.
- Facilidad de mantenimiento.
- Adecuación al contexto académico del ciclo DAM.

---

