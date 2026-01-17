

---

# Componentes del sistema

## Laboratorio SIEM

---

## Introducción

En este apartado se describen los **componentes lógicos que conforman el Laboratorio SIEM**, detallando su función, responsabilidades y la forma en que se relacionan entre sí dentro del sistema.

A diferencia del capítulo de arquitectura general, este apartado se centra en explicar **qué hace cada componente desde un punto de vista funcional**, sin profundizar todavía en aspectos de implementación técnica ni en tecnologías concretas.

---

## Flujo general de datos

El funcionamiento del sistema se basa en un **flujo de datos principalmente secuencial y desacoplado**, en el que los eventos generados por las fuentes atraviesan distintos módulos hasta ser analizados y visualizados.

Este flujo se representa de forma esquemática en el siguiente diagrama:

[[00_01_01_09_Anexos/Diagramas/02_Flujo_Datos_SIEM.excalidraw.md|02_Flujo_Datos_SIEM]]

De manera general, el flujo es el siguiente:

1. Las fuentes de eventos generan información relevante.
    
2. Los eventos se envían al sistema central a través del módulo de ingesta.
    
3. Los eventos se normalizan dentro del backend.
    
4. La información se almacena de forma persistente.
    
5. Los eventos almacenados se analizan mediante reglas.
    
6. Se generan alertas cuando se detectan condiciones relevantes.
    
7. La interfaz web permite la consulta y gestión de la información.

---

## Descripción de los componentes

### Fuentes de eventos

Las fuentes de eventos son los sistemas encargados de **generar la información** que posteriormente será analizada por el Laboratorio SIEM. Estas fuentes se despliegan en un entorno de laboratorio controlado y no forman parte directa del sistema SIEM.

Responsabilidades:
- Generar eventos de forma natural o simulada.
- Registrar acciones relevantes desde el punto de vista de la seguridad.
- Enviar los eventos al sistema central mediante mecanismos controlados.

Entradas:
- Acciones de usuarios.
- Actividad de servicios.
- Eventos propios del sistema operativo.

Salidas:
- Eventos estructurados enviados al módulo de ingesta.

---

### Módulo de ingesta

El módulo de ingesta actúa como **punto de entrada único** al sistema SIEM. Constituye la frontera entre las fuentes externas y el núcleo del sistema.

Responsabilidades:
- Recibir eventos procedentes de las fuentes del laboratorio.
- Validar la estructura básica de los eventos recibidos.
- Rechazar eventos inválidos o incompletos.
- Transferir los eventos válidos al proceso de normalización.

Entradas:
- Eventos en formato estructurado enviados por las fuentes.

Salidas:
- Eventos validados listos para su normalización.

---

### Módulo de normalización

El módulo de normalización se encarga de **adaptar los eventos recibidos** a un modelo de datos común, independiente del origen del evento.

Responsabilidades:
- Unificar el formato de los eventos.
- Asignar campos estándar comunes.
- Enriquecer los eventos con información básica adicional, cuando procede.

Entradas:
- Eventos validados por el módulo de ingesta.

Salidas:
- Eventos normalizados preparados para su almacenamiento y análisis.

---

### Módulo de almacenamiento

El módulo de almacenamiento gestiona la **persistencia de la información** generada y procesada por el sistema.

Responsabilidades:
- Almacenar eventos normalizados.
- Almacenar alertas generadas por el sistema.
- Garantizar la integridad y disponibilidad de los datos.

Entradas:
- Eventos normalizados.
- Alertas generadas por el módulo de análisis.

Salidas:
- Información persistente accesible para los módulos de análisis y visualización.

---

### Módulo de análisis y reglas

Este módulo implementa la **lógica de detección** del sistema SIEM, evaluando los eventos almacenados en función de un conjunto de reglas predefinidas.

Responsabilidades:
- Analizar eventos según reglas establecidas.
- Detectar patrones simples de interés.
- Generar alertas cuando se cumplen las condiciones definidas.

Entradas:
- Eventos almacenados o en proceso de evaluación.

Salidas:
- Alertas de seguridad generadas.

Las reglas se definen con un alcance limitado y un enfoque didáctico, acorde al contexto académico del proyecto.

---

### Módulo de gestión de alertas

El módulo de gestión de alertas se encarga de la **administración del ciclo de vida de las alertas** generadas por el sistema.

Responsabilidades:
- Registrar las alertas generadas.
- Gestionar el estado de las alertas (abierta, cerrada).
- Facilitar la consulta y actualización de las alertas.

Entradas:
- Alertas generadas por el módulo de análisis.

Salidas:
- Alertas gestionadas y actualizadas.

---

### Interfaz web

La interfaz web proporciona un **punto de acceso visual** al sistema SIEM, permitiendo la interacción del usuario con la información almacenada.

Responsabilidades:
- Mostrar eventos y alertas de forma estructurada.
- Facilitar la navegación por la información.
- Permitir acciones básicas sobre las alertas.

Entradas:
- Datos proporcionados por el backend del sistema.

Salidas:
- Información visualizada y gestionada por el usuario.

---

## Relación entre componentes

Los componentes del sistema interactúan de forma **secuencial y desacoplada**, siguiendo el flujo de datos definido previamente. Esta separación de responsabilidades favorece la claridad del diseño, facilita el mantenimiento del sistema y permite su evolución sin afectar a la estructura base.

Cada componente cumple una función concreta dentro del flujo global, contribuyendo al funcionamiento coherente del Laboratorio SIEM.
