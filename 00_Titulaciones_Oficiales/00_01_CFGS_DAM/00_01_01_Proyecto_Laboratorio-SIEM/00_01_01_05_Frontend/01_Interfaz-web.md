

---

# Interfaz web

## Laboratorio SIEM

---

## 1. Introducción

La interfaz web del Laboratorio SIEM constituye la **capa de presentación del sistema**, encargada de mostrar de forma clara y estructurada la información procesada por el backend. Su función principal es permitir la **visualización, consulta y comprensión** de los eventos y alertas generados durante el funcionamiento del laboratorio.

A diferencia del backend, que se centra en la ingestión, análisis y persistencia de datos, el frontend no introduce lógica de decisión ni procesamiento complejo. Su objetivo es ofrecer una representación accesible de la información ya analizada, facilitando la interpretación del estado del sistema.

En esta nota se describe el papel del frontend dentro del Laboratorio SIEM, su alcance funcional y las decisiones de diseño adoptadas.

---

## 2. Rol del frontend en el Laboratorio SIEM

El frontend actúa como **consumidor de datos** generados y gestionados por el backend, proporcionando una interfaz visual que permite interactuar con la información almacenada.

Sus responsabilidades principales son:

- Mostrar los eventos almacenados en el sistema de forma ordenada.
    
- Visualizar las alertas generadas por el motor de reglas.
    
- Permitir la consulta del detalle de una alerta concreta.
    
- Facilitar una visión general del estado del sistema.
    

Desde el punto de vista arquitectónico, el frontend se sitúa **en el extremo del sistema**, accediendo a los datos a través de interfaces definidas por el backend, sin acceso directo a la base de datos ni a la lógica interna.

---

## 3. Objetivo de la interfaz web

El objetivo principal de la interfaz web del Laboratorio SIEM es **proporcionar una visualización clara y comprensible** de la información de seguridad generada en el entorno de laboratorio.

De forma más concreta, la interfaz web persigue:

- Facilitar la identificación de alertas relevantes.
    
- Permitir analizar el contexto de una alerta a partir de los eventos asociados.
    
- Ofrecer una visión global del funcionamiento del sistema.
    
- Servir como apoyo didáctico para comprender el flujo completo de un sistema SIEM.
    

La interfaz no pretende replicar funcionalidades avanzadas de plataformas SIEM profesionales, sino ilustrar los conceptos fundamentales de visualización y consulta de datos en un entorno académico.

---

## 4. Alcance funcional del frontend

El frontend del Laboratorio SIEM se diseña con un alcance funcional **delimitado y coherente** con el resto del sistema.

Incluye las siguientes funcionalidades:

- Visualización de eventos almacenados.
    
- Visualización de alertas abiertas y cerradas.
    
- Consulta del detalle de una alerta y sus eventos asociados.
    
- Actualización del estado de una alerta (por ejemplo, cierre).
    

Quedan fuera del alcance del frontend:

- Configuración de reglas de detección.
    
- Gestión de usuarios o autenticación.
    
- Análisis avanzado o correlación manual.
    
- Personalización compleja de dashboards.
    

Este alcance permite centrar el desarrollo en la presentación de la información sin introducir complejidad innecesaria.

---

## 5. Relación con el backend

La interfaz web se comunica exclusivamente con el backend del Laboratorio SIEM para obtener y actualizar información.

Desde el punto de vista funcional:

- El frontend consulta eventos y alertas mediante interfaces proporcionadas por el backend.
    
- No existe acceso directo a la base de datos desde la interfaz web.
    
- Las acciones realizadas en la interfaz (por ejemplo, cerrar una alerta) se traducen en solicitudes al backend.
    

Este modelo refuerza la separación entre presentación y lógica de negocio, y garantiza que todas las modificaciones relevantes pasen por los mecanismos de control definidos en el backend.

---

## 6. Consideraciones de diseño de la interfaz

El diseño de la interfaz web se rige por los siguientes criterios:

- **Claridad visual**  
    La información se presenta de forma ordenada y legible.
    
- **Simplicidad funcional**  
    Se prioriza un número reducido de vistas claramente diferenciadas.
    
- **Coherencia con el modelo de datos**  
    La estructura de la interfaz refleja las entidades principales del sistema (eventos, alertas).
    
- **Orientación didáctica**  
    La interfaz está pensada para facilitar la comprensión del funcionamiento interno del SIEM.
    

Estas consideraciones permiten una interfaz comprensible, mantenible y adecuada al contexto del proyecto.

---

## 7. Limitaciones del frontend

La interfaz web presenta una serie de limitaciones asumidas conscientemente:

- No incluye autenticación ni control de acceso.
    
- No incorpora visualizaciones avanzadas ni gráficos complejos.
    
- No permite la configuración dinámica del sistema.
    
- No está orientada a uso concurrente intensivo.
    

Estas limitaciones son coherentes con el carácter académico del Laboratorio SIEM y permiten centrar el desarrollo en los conceptos esenciales.

---