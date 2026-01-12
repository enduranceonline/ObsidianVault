

---

# Vistas del frontend

## Laboratorio SIEM

---

## 1. Introducción

Las vistas del frontend del Laboratorio SIEM representan las distintas **pantallas o secciones funcionales** de la interfaz web a través de las cuales el usuario puede consultar la información generada por el sistema.

Cada vista se diseña para cumplir un objetivo concreto y está directamente relacionada con las entidades principales del modelo de datos, principalmente eventos y alertas. El diseño prioriza la claridad y la coherencia, evitando una fragmentación excesiva de la interfaz.

En esta nota se describen las vistas definidas, su finalidad y la información que presentan.

---

## 2. Vista de alertas

### 2.1 Objetivo

La vista de alertas constituye el **punto central de la interfaz web**, ya que muestra las situaciones relevantes detectadas por el sistema.

Su objetivo principal es:

- Proporcionar una visión general del estado del sistema.
    
- Facilitar la identificación de alertas pendientes de revisión.
    
- Permitir acceder al detalle de cada alerta.
    

---

### 2.2 Información mostrada

En esta vista se muestra un listado de alertas, incluyendo como mínimo:

- Identificador de la alerta.
    
- Regla que la ha generado.
    
- Nivel de severidad.
    
- Estado de la alerta (`OPEN` / `CLOSED`).
    
- Fecha y hora de creación.
    

La información se presenta de forma tabular u organizada, facilitando su lectura y comparación.

---

### 2.3 Funcionalidades asociadas

La vista de alertas permite:

- Filtrar alertas por estado (abiertas o cerradas).
    
- Ordenar alertas por fecha o severidad.
    
- Acceder al detalle de una alerta concreta.
    
- Cambiar el estado de una alerta (por ejemplo, cerrarla).
    

---

## 3. Vista de detalle de alerta

### 3.1 Objetivo

La vista de detalle de alerta permite analizar una alerta de forma individual, proporcionando el **contexto necesario para entender su origen**.

Su objetivo es facilitar la trazabilidad entre alertas, reglas y eventos.

---

### 3.2 Información mostrada

En esta vista se muestra:

- Información general de la alerta:
    
    - Identificador.
        
    - Regla asociada.
        
    - Severidad.
        
    - Estado actual.
        
    - Fechas de creación y cierre (si procede).
        
- Listado de eventos asociados a la alerta:
    
    - Fuente del evento.
        
    - Tipo de evento.
        
    - Fecha y hora.
        
    - Mensaje descriptivo.
        

Esta información permite reconstruir de forma clara por qué se ha generado la alerta.

---

### 3.3 Funcionalidades asociadas

Desde esta vista se permite:

- Consultar el contexto completo de la alerta.
    
- Cambiar el estado de la alerta.
    
- Volver a la vista general de alertas.
    

No se incluyen funcionalidades de modificación de reglas ni edición avanzada.

---

## 4. Vista de eventos

### 4.1 Objetivo

La vista de eventos permite consultar los **eventos almacenados** en el sistema, independientemente de si han generado alertas o no.

Su objetivo es ofrecer una visión detallada de la actividad registrada en el entorno de laboratorio.

---

### 4.2 Información mostrada

En esta vista se presenta un listado de eventos con información como:

- Fecha y hora del evento.
    
- Fuente del evento.
    
- Tipo de evento.
    
- Nivel de severidad.
    
- Mensaje descriptivo.
    

La información se muestra de forma estructurada para facilitar su exploración.

---

### 4.3 Funcionalidades asociadas

La vista de eventos permite:

- Filtrar eventos por fuente, tipo o severidad.
    
- Ordenar eventos por fecha.
    
- Consultar eventos recientes.
    
- Identificar eventos asociados a alertas.
    

---

## 5. Navegación entre vistas

La interfaz web permite una navegación sencilla entre las distintas vistas:

- Desde la vista de alertas se accede al detalle de una alerta.
    
- Desde el detalle de una alerta se accede a los eventos asociados.
    
- Desde la vista de eventos se puede identificar si un evento está vinculado a alguna alerta.
    

Este modelo de navegación refuerza la trazabilidad y facilita la comprensión del flujo de información dentro del sistema.

---

## 6. Relación con el backend

Cada vista del frontend obtiene su información a través de consultas al backend:

- La vista de alertas consulta el estado actual de las alertas.
    
- La vista de detalle accede a la información de una alerta y sus eventos asociados.
    
- La vista de eventos consulta los eventos almacenados.
    

El frontend no implementa lógica de análisis ni toma de decisiones, limitándose a presentar la información proporcionada por el backend.

---

## 7. Consideraciones de diseño de las vistas

El diseño de las vistas se basa en los siguientes criterios:

- **Correspondencia directa con el modelo de datos**  
    Cada vista refleja entidades y relaciones definidas previamente.
    
- **Simplicidad visual**  
    Se evita la sobrecarga de información en una misma pantalla.
    
- **Orientación a la comprensión**  
    Las vistas están pensadas para ayudar a entender cómo funciona el sistema.
    
- **Coherencia funcional**  
    Las acciones disponibles son consistentes entre vistas.
    

Estas consideraciones permiten una interfaz clara y fácil de utilizar.

---

## 8. Limitaciones de las vistas del frontend

Las vistas del frontend presentan limitaciones acordes al alcance del proyecto:

- No se permite la edición de reglas.
    
- No se incluyen dashboards avanzados.
    
- No se gestionan múltiples usuarios.
    
- No se incorpora análisis visual complejo.
    

Estas limitaciones son coherentes con el objetivo didáctico del Laboratorio SIEM.

---