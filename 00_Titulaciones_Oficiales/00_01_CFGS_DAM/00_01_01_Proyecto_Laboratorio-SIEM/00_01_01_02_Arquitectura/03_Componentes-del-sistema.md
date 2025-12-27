

---

# Componentes del sistema  
## Laboratorio SIEM

---

## Introducción

En este apartado se detallan los **componentes lógicos que conforman el Laboratorio SIEM**, describiendo su función, responsabilidades y relación con el resto del sistema.

A diferencia de la arquitectura general, en este capítulo se profundiza en **qué hace exactamente cada componente**, sin entrar aún en aspectos de implementación técnica o tecnologías concretas.

---

## Descripción de los componentes

### • Fuentes de eventos

Las fuentes de eventos son los sistemas encargados de **generar la información** que posteriormente será analizada por el Laboratorio SIEM.

Responsabilidades:

- Generar eventos de forma natural o simulada.
- Registrar acciones relevantes para el análisis de seguridad.
- Enviar los eventos al sistema central.

Entradas:

- Acciones de usuarios.
- Actividad de servicios.
- Eventos del sistema operativo.

Salidas:

- Eventos estructurados enviados al módulo de ingesta.

---

### • Módulo de ingesta

El módulo de ingesta es el **punto de entrada** del sistema desarrollado.

Responsabilidades:

- Recibir eventos procedentes de las fuentes del laboratorio.
- Validar la estructura básica de los eventos.
- Rechazar eventos inválidos o incompletos.
- Transferir los eventos válidos al proceso de normalización.

Entradas:

- Eventos en formato estructurado.

Salidas:

- Eventos validados para su normalización.

---

### • Módulo de normalización

Este componente se encarga de **adaptar los eventos recibidos** a un modelo de datos común.

Responsabilidades:

- Unificar el formato de los eventos.
- Asignar campos estándar.
- Enriquecer eventos con información adicional básica, si procede.

Entradas:

- Eventos validados por el módulo de ingesta.

Salidas:

- Eventos normalizados listos para su almacenamiento y análisis.

---

### • Módulo de almacenamiento

El módulo de almacenamiento gestiona la **persistencia de la información** del sistema.

Responsabilidades:

- Almacenar eventos normalizados.
- Almacenar alertas generadas.
- Mantener la integridad de los datos.

Entradas:

- Eventos normalizados.
- Alertas generadas.

Salidas:

- Información persistente accesible para análisis y visualización.

---

### • Módulo de análisis y reglas

Este módulo implementa la **lógica de detección** del sistema.

Responsabilidades:

- Evaluar eventos según reglas predefinidas.
- Detectar patrones simples.
- Generar alertas cuando se cumplen las condiciones establecidas.

Entradas:

- Eventos almacenados o en tiempo de procesamiento.

Salidas:

- Alertas de seguridad.

Las reglas se definen de forma estática y con un alcance limitado, acorde al contexto académico.

---

### • Módulo de gestión de alertas

Este componente se encarga de la **administración del ciclo de vida de las alertas**.

Responsabilidades:

- Registrar alertas generadas.
- Gestionar el estado de las alertas.
- Permitir la consulta y cierre de alertas.

Entradas:

- Alertas generadas por el módulo de análisis.

Salidas:

- Alertas gestionadas y actualizadas.

---

### • Interfaz web

La interfaz web proporciona un **punto de acceso visual** al sistema.

Responsabilidades:

- Mostrar eventos y alertas.
- Facilitar la navegación por la información.
- Permitir acciones básicas sobre las alertas.

Entradas:

- Datos proporcionados por el backend.

Salidas:

- Información visualizada al usuario.

---

## Relación entre componentes

Los componentes interactúan de forma secuencial y desacoplada:

1. Las fuentes generan eventos.
2. El módulo de ingesta recibe los eventos.
3. Los eventos se normalizan.
4. Se almacenan en la base de datos.
5. Se analizan mediante reglas.
6. Se generan y gestionan alertas.
7. La interfaz web presenta la información.

Esta separación de responsabilidades favorece la claridad y el mantenimiento del sistema.

---