

---

# Flujo de interacción del usuario

## Laboratorio SIEM

---

## 1. Introducción

El flujo de interacción del usuario describe la **secuencia de acciones** que un usuario puede realizar dentro de la interfaz web del Laboratorio SIEM. Este flujo define cómo se navega entre las distintas vistas y cómo se consulta la información generada por el sistema.

El objetivo de este apartado es detallar el comportamiento esperado de la interfaz desde el punto de vista del usuario, sin entrar en aspectos de implementación ni diseño visual.

---

## 2. Acceso inicial a la interfaz

Al acceder a la interfaz web del Laboratorio SIEM, el usuario es dirigido a la **vista principal de alertas**, que actúa como punto de entrada al sistema.

Esta decisión responde a que las alertas representan la información más relevante desde el punto de vista funcional y permiten obtener rápidamente una visión general del estado del sistema.

---

## 3. Navegación entre vistas

La navegación entre las distintas vistas sigue un flujo sencillo e intuitivo:

- Desde la **vista de alertas**, el usuario puede:
    
    - consultar alertas abiertas y cerradas,
        
    - seleccionar una alerta concreta para ver su detalle.
        
- Desde la **vista de detalle de alerta**, el usuario puede:
    
    - analizar los eventos asociados,
        
    - cambiar el estado de la alerta,
        
    - volver a la vista general de alertas.
        
- Desde la **vista de eventos**, el usuario puede:
    
    - consultar eventos recientes,
        
    - identificar eventos asociados a alertas,
        
    - regresar a otras vistas principales.
        

Este modelo de navegación facilita la trazabilidad y evita flujos complejos.

---

## 4. Interacción con alertas

La interacción principal del usuario se centra en la gestión de alertas:

- Revisión de alertas abiertas.
    
- Consulta del contexto de una alerta.
    
- Cierre de alertas una vez revisadas.
    

Estas acciones permiten simular el trabajo básico de un analista dentro de un sistema SIEM, manteniendo un alcance adecuado al proyecto.

---

## 5. Comportamiento esperado de la interfaz

Durante la interacción, la interfaz debe:

- Reflejar cambios de estado de forma inmediata.
    
- Mantener la coherencia entre vistas.
    
- Mostrar información actualizada procedente del backend.
    
- Evitar acciones ambiguas o inconsistentes.
    

La interfaz no toma decisiones por sí misma, sino que refleja el estado del sistema gestionado por el backend.

---

## 6. Alcance del flujo de interacción

El flujo de interacción definido cubre únicamente las acciones básicas necesarias para:

- Consultar información.
    
- Navegar entre vistas.
    
- Gestionar el estado de las alertas.
    

Quedan fuera del alcance:

- Personalización del flujo por usuario.
    
- Acciones automatizadas desde la interfaz.
    
- Configuración avanzada del sistema.
    

---