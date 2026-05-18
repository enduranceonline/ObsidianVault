## Objetivo general

El objetivo general del proyecto es desarrollar un **laboratorio SIEM básico en formato MVP**, capaz de recibir eventos simulados, almacenarlos, evaluarlos mediante reglas de detección y generar alertas consultables desde una API y una interfaz web.

El proyecto busca demostrar el funcionamiento esencial de un sistema de monitorización de seguridad, manteniendo un alcance realista y adecuado al contexto académico del ciclo de Desarrollo de Aplicaciones Multiplataforma.

---

## Objetivos técnicos

### Desarrollar una API REST funcional

Crear un backend con **FastAPI** que permita gestionar los elementos principales del sistema:

```text
- Eventos
- Reglas
- Alertas
- Métricas
- Estado del sistema
````

La API debe permitir recibir información, procesarla y devolver respuestas estructuradas para su consulta desde Swagger, terminal o frontend.

---

### Implementar una ingesta de eventos

Desarrollar un endpoint principal de ingesta capaz de recibir eventos simulados con información básica:

```text
- Origen del evento
- Severidad
- Mensaje
- Metadatos adicionales
```

Este endpoint debe representar el punto de entrada del sistema y activar el flujo principal del proyecto.

---

### Diseñar una base de datos relacional

Crear un modelo de datos en **PostgreSQL** que permita almacenar de forma persistente:

```text
- Eventos recibidos
- Reglas de detección
- Alertas generadas
```

El diseño debe permitir relacionar cada alerta con el evento que la originó y con la regla que provocó su generación.

---

### Implementar un motor básico de reglas

Desarrollar una lógica de detección propia que evalúe los eventos recibidos contra reglas activas.

Las reglas deben poder trabajar con condiciones como:

```text
- Source
- Severidad mínima
- Contenido del mensaje
- Metadatos
- Umbrales
- Control de duplicados
```

El objetivo no es crear un motor de correlación avanzado, sino una lógica básica, comprensible y funcional.

---

### Generar alertas automáticamente

Permitir que el sistema genere alertas cuando un evento cumpla las condiciones definidas en una regla activa.

Cada alerta debe quedar registrada en base de datos y contener la información necesaria para ser consultada posteriormente.

---

### Gestionar estados de alertas

Implementar una gestión básica del ciclo de vida de una alerta mediante estados controlados:

```text
open
ack
closed
```

Esta funcionalidad permite simular una parte básica del trabajo habitual de revisión y seguimiento de alertas en un entorno de monitorización.

---

### Crear una interfaz web básica

Desarrollar un frontend sencillo con **HTML, CSS y JavaScript** que permita consultar las alertas generadas por el sistema.

La interfaz debe permitir:

```text
- Ver alertas
- Aplicar filtros
- Consultar información relevante
- Actualizar los datos mostrados
```

El frontend no busca ser un dashboard avanzado, sino una prueba visual del funcionamiento del sistema.

---

### Contenerizar el entorno

Utilizar **Docker Compose** para levantar los servicios principales del proyecto:

```text
- API FastAPI
- Base de datos PostgreSQL
- Adminer
```

Este objetivo permite mejorar la reproducibilidad del entorno y facilitar la puesta en marcha del proyecto desde cero.

---

### Validar el funcionamiento del sistema

Comprobar que el sistema funciona correctamente mediante pruebas manuales y automatizadas.

La validación debe incluir:

```text
- Comprobación de la API
- Comprobación de la base de datos
- Pruebas de ingesta
- Pruebas de generación de alertas
- Pruebas de filtros
- Pruebas de cambio de estado
- Pruebas del frontend
- Ejecución de tests automatizados
```

---

### Documentar el proyecto

Elaborar documentación técnica suficiente para explicar:

```text
- Qué hace el proyecto
- Cómo está construido
- Qué tecnologías utiliza
- Cómo se despliega
- Cómo se prueba
- Qué problemas surgieron
- Qué limitaciones tiene
- Qué mejoras podrían añadirse
```

La documentación debe servir tanto para la memoria del proyecto como para facilitar la reproducción del sistema desde el repositorio.

---

## Objetivos académicos

Además de los objetivos técnicos, el proyecto tiene una finalidad académica. Por ello, se han definido los siguientes objetivos:

```text
- Aplicar conocimientos de programación backend.
- Trabajar con bases de datos relacionales.
- Diseñar una API REST documentada.
- Separar responsabilidades entre componentes.
- Usar control de versiones.
- Desplegar servicios mediante contenedores.
- Validar funcionalidades mediante pruebas.
- Documentar decisiones técnicas.
- Resolver problemas reales surgidos durante el desarrollo.
```

Estos objetivos permiten justificar el proyecto dentro del ciclo de Desarrollo de Aplicaciones Multiplataforma, aunque la temática esté orientada a ciberseguridad.

---

## Objetivos relacionados con ciberseguridad

El proyecto también persigue objetivos formativos vinculados al ámbito Blue Team:

```text
- Comprender el flujo básico de un SIEM.
- Simular la recepción de eventos de seguridad.
- Aplicar reglas de detección sobre eventos.
- Generar alertas a partir de condiciones definidas.
- Consultar y filtrar alertas.
- Entender la relación entre eventos, reglas y alertas.
- Introducir conceptos básicos de monitorización defensiva.
```

Estos objetivos permiten conectar el desarrollo de software con un caso de uso realista dentro de la ciberseguridad defensiva.

---

## Objetivos de alcance

Para evitar que el proyecto creciera de forma excesiva, se definieron también objetivos de alcance:

```text
- Mantener el proyecto como un MVP funcional.
- Priorizar el flujo principal antes que funcionalidades secundarias.
- Evitar convertir el proyecto en una simple instalación de herramientas.
- Desarrollar componentes propios.
- Dejar las funcionalidades avanzadas como futuras mejoras.
```

Esta delimitación fue necesaria porque un SIEM real incluye muchas más capacidades que las asumibles en este proyecto.

---

## Objetivos cumplidos

Al finalizar el desarrollo, se han cumplido los objetivos principales previstos:

```text
- La API funciona correctamente.
- La base de datos almacena eventos, reglas y alertas.
- El endpoint de ingesta recibe eventos simulados.
- El motor de reglas evalúa eventos.
- Las alertas se generan automáticamente.
- Las alertas pueden consultarse y filtrarse.
- El estado de una alerta puede modificarse.
- El frontend muestra la información del sistema.
- Docker Compose levanta los servicios principales.
- Adminer permite revisar la base de datos.
- Swagger documenta la API.
- Los tests automatizados se ejecutan correctamente.
- El proyecto está documentado y subido a GitHub.
```

El resultado final cumple el objetivo de construir una versión mínima, funcional y demostrable de un laboratorio SIEM.

---

## Objetivos no incluidos en esta versión

Algunas funcionalidades quedaron fuera del alcance inicial para mantener el proyecto dentro de unos límites realistas:

```text
- Autenticación de usuarios.
- Roles y permisos.
- Integración con logs reales.
- Instalación de agentes externos.
- Dashboards avanzados.
- Correlación compleja.
- Notificaciones automáticas.
- Informes exportables.
- Despliegue en producción.
```

Estas funcionalidades se consideran posibles líneas futuras de mejora, pero no eran necesarias para demostrar el objetivo principal del proyecto.

---

## Conclusión

Los objetivos del proyecto se han centrado en construir una aplicación funcional, reproducible y orientada a la monitorización básica de eventos de seguridad.

La prioridad ha sido desarrollar un flujo completo y verificable antes que añadir funcionalidades avanzadas. Gracias a esta delimitación, el proyecto ha podido completarse como un MVP coherente, adecuado al contexto académico y útil como introducción práctica a conceptos de ciberseguridad defensiva.