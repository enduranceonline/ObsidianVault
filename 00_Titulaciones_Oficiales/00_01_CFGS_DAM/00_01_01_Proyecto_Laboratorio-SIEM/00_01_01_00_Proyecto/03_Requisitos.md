

---

# 📋 Requisitos del Proyecto

## Laboratorio SIEM

---

## 1. Introducción

En este apartado se definen los **requisitos funcionales y no funcionales** del proyecto **Laboratorio SIEM**, con el objetivo de concretar de forma precisa el comportamiento esperado del sistema y los criterios que permitirán validar su correcto funcionamiento.

La definición de estos requisitos facilita:

- La planificación del desarrollo.
    
- La validación del sistema.
    
- La evaluación académica del proyecto.
    

---

## 2. Requisitos funcionales

Los requisitos funcionales describen **qué debe hacer el sistema**.

---

### 🔹 RF-01 – Recepción de eventos

El sistema deberá permitir la **recepción de eventos de seguridad** a través de una API REST, utilizando un formato estructurado (por ejemplo, JSON).

---

### 🔹 RF-02 – Normalización de eventos

El sistema deberá procesar los eventos recibidos y **normalizarlos a un modelo de datos común**, independientemente de su origen.

---

### 🔹 RF-03 – Almacenamiento de eventos

El sistema deberá **almacenar los eventos normalizados** en una base de datos relacional para su posterior análisis y consulta.

---

### 🔹 RF-04 – Análisis de eventos

El sistema deberá analizar los eventos almacenados mediante un **conjunto de reglas de detección simples**, definidas previamente.

---

### 🔹 RF-05 – Generación de alertas

El sistema deberá **generar alertas de seguridad** cuando se cumplan las condiciones establecidas en las reglas de detección.

---

### 🔹 RF-06 – Gestión de alertas

El sistema deberá permitir la **consulta y gestión de alertas**, incluyendo el cambio de estado (por ejemplo, abierta o cerrada).

---

### 🔹 RF-07 – Visualización de información

El sistema deberá proporcionar una **interfaz web** que permita visualizar:

- Eventos recientes.
    
- Alertas activas.
    
- Detalles básicos de cada alerta.
    

---

### 🔹 RF-08 – Entorno de laboratorio

El sistema deberá operar sobre eventos generados en un **entorno de laboratorio controlado**, diseñado para simular escenarios básicos de seguridad.

---

## 3. Requisitos no funcionales

Los requisitos no funcionales describen **cómo debe comportarse el sistema**.

---

### 🔹 RNF-01 – Usabilidad

La interfaz web deberá ser **simple, clara y fácil de utilizar**, permitiendo al usuario comprender rápidamente la información mostrada.

---

### 🔹 RNF-02 – Rendimiento

El sistema deberá ser capaz de procesar eventos en un volumen reducido, adecuado a un entorno académico, sin degradar su funcionamiento.

---

### 🔹 RNF-03 – Modularidad

El sistema deberá diseñarse de forma **modular**, permitiendo la separación entre:

- Ingesta de eventos
    
- Lógica de análisis
    
- Persistencia
    
- Visualización
    

---

### 🔹 RNF-04 – Mantenibilidad

El código deberá estar organizado y documentado, facilitando su **mantenimiento y comprensión**.

---

### 🔹 RNF-05 – Portabilidad

El sistema deberá poder desplegarse en distintos entornos mediante el uso de **contenedores**, sin depender de configuraciones específicas del sistema anfitrión.

---

### 🔹 RNF-06 – Seguridad básica

El sistema implementará **mecanismos básicos de seguridad**, adecuados al contexto académico, como control de acceso simple y validación de datos de entrada.

---

## 4. Requisitos de validación

El cumplimiento de los requisitos se verificará mediante:

- Pruebas funcionales sobre la API.
    
- Generación controlada de eventos en el laboratorio.
    
- Comprobación visual de eventos y alertas en el dashboard.
    
- Documentación de resultados.
    

---