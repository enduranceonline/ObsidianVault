

---

# API de Ingesta 

## Laboratorio SIEM

Referencia de diseño y decisiones previas:  
[[00_Titulaciones_Oficiales/00_01_CFGS_DAM/00_01_01_Proyecto_Laboratorio-SIEM/00_01_01_04_Backend/01_API-de-Ingesta.md|00_01_01_04_Backend/01_API-de-Ingesta.md]]

---
## 1. Estado del componente

En el estado actual del proyecto no se ha desarrollado todavía la lógica funcional de la API de Ingesta.

Esta nota documentará de forma incremental la implementación del componente conforme se vayan incorporando elementos técnicos al backend del laboratorio SIEM.

---

## 2. Preparación del entorno de desarrollo

Se ha preparado el entorno necesario para iniciar la implementación del backend, incluyendo:

- Creación del repositorio del proyecto.
- Inicialización del entorno de desarrollo en máquina virtual Linux.
- Preparación del entorno virtual de Python.
- Instalación de las dependencias principales del backend.

En esta fase no se han definido todavía endpoints, modelos de datos ni conexión a base de datos.

---

## 3. Alcance de esta fase inicial

El alcance de la fase actual se limita a la preparación del entorno y a la planificación de la implementación del componente.

No se incluye todavía:
- Desarrollo de endpoints REST.
- Validación de eventos.
- Persistencia de datos.
- Integración con otros componentes del sistema.

---

## 4. Observaciones iniciales

Se ha optado por comenzar la implementación del backend de forma incremental, priorizando una base sólida antes de introducir lógica funcional.

Las siguientes iteraciones documentarán exclusivamente funcionalidades que hayan sido implementadas y verificadas.
```

---

Esta nota ahora cumple exactamente con lo que debe cumplir:

- Refleja el estado real del proyecto.
    
- No documenta código inexistente.
    
- Es formal y defendible.
    
- Sirve como punto de arranque limpio para crecer.
    

El siguiente paso ya no es documental, es técnico.

Dime qué implementas primero y avanzamos en ese orden:

1. Estructura base del proyecto FastAPI
    
2. Endpoint mínimo `/health`
    
3. Configuración de base de datos
    
4. Inicialización de Alembic