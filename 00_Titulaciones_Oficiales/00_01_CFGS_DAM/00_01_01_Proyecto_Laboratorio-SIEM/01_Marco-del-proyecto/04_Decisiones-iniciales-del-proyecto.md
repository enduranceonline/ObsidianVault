## Introducción

Durante la planificación y el desarrollo del proyecto fue necesario tomar varias decisiones para mantener el trabajo dentro de un alcance realista y coherente con los objetivos académicos.

La idea inicial partía de un ámbito amplio: los sistemas SIEM y la monitorización de eventos de seguridad. Sin embargo, un SIEM real incluye muchas funcionalidades avanzadas que quedaban fuera del alcance del proyecto. Por este motivo, se decidió construir una versión mínima funcional centrada en el flujo principal:

```text
evento → ingesta → almacenamiento → evaluación → alerta → consulta
````

Esta nota recoge las decisiones más importantes que condicionaron el diseño del sistema.

---

## Desarrollar una aplicación propia y no instalar un SIEM real

Una de las primeras decisiones fue no basar el proyecto en la instalación de una herramienta SIEM ya existente.

Existen soluciones como Wazuh, ELK, Splunk, Graylog u otras plataformas que permiten crear laboratorios de monitorización más completos. Sin embargo, utilizarlas como núcleo del proyecto habría reducido la parte de desarrollo propio.

Como el proyecto pertenece al ciclo de Desarrollo de Aplicaciones Multiplataforma, se decidió crear una aplicación propia con:

```text
- API de ingesta.
- Modelo de datos propio.
- Gestión de eventos.
- Gestión de reglas.
- Motor básico de detección.
- Generación de alertas.
- Endpoints de consulta.
- Frontend básico.
```

Esta decisión permitió mantener el equilibrio entre la temática de ciberseguridad y el objetivo académico de desarrollar una solución software.

---

## Trabajar con eventos simulados

Otra decisión importante fue utilizar eventos simulados en lugar de integrar logs reales del sistema.

La integración de logs reales habría añadido complejidad adicional:

```text
- Configuración de fuentes externas.
- Adaptación de formatos.
- Normalización de eventos.
- Permisos de lectura.
- Instalación de agentes.
- Gestión de diferentes estructuras de log.
```

Para esta versión se priorizó representar el flujo principal del sistema de forma controlada. Por ello, los eventos se envían manualmente mediante la API y contienen campos simples como `source`, `severity`, `message` y `meta`.

Esta decisión reduce el realismo del laboratorio, pero permite centrar el desarrollo en la lógica esencial: recibir eventos, almacenarlos, evaluarlos y generar alertas.

---

## Separar eventos, reglas y alertas

El modelo de datos se diseñó separando tres entidades principales:

```text
events
rules
alerts
```

Esta separación permite representar de forma clara el funcionamiento del sistema:

```text
Evento → dato recibido
Regla  → condición de detección
Alerta → resultado generado
```

Cada alerta queda asociada al evento que la originó y a la regla que se activó. De esta forma, el sistema no solo muestra que existe una alerta, sino que también permite entender por qué se ha generado.

Esta decisión facilita la consulta, la validación y la explicación del comportamiento del proyecto.

---

## Implementar un motor de reglas básico

El proyecto necesitaba una lógica propia capaz de convertir eventos en alertas. Para ello se desarrolló un motor de reglas básico.

El motor permite evaluar condiciones como:

```text
- Fuente del evento.
- Severidad mínima.
- Texto contenido en el mensaje.
- Coincidencia de metadatos.
- Umbrales simples.
- Control básico de duplicados.
- Throttle.
```

No se buscó implementar una correlación avanzada como la de un SIEM profesional. El objetivo era construir una lógica sencilla, comprensible y suficiente para demostrar el funcionamiento principal del sistema.

---

## Limitar el comportamiento de group_key, threshold y throttle

Durante el desarrollo fue necesario definir cómo debían comportarse algunas funciones del motor de reglas.

Uno de los puntos más importantes fue el uso de `group_key`, utilizado para agrupar eventos relacionados. En esta versión se decidió obtenerlo a partir de:

```text
meta.host
```

También se definió el comportamiento de `threshold` y `throttle` para evitar resultados ambiguos:

```text
- Las alertas simples pueden generarse aunque no exista group_key.
- El throttle y el control de duplicados dependen del group_key.
- Los thresholds requieren group_key para funcionar correctamente.
```

Esta decisión simplificó el motor de reglas y permitió que su comportamiento fuera más previsible.

---

## Usar endpoints enriquecidos para el frontend

Durante el desarrollo apareció una necesidad práctica: el frontend necesitaba mostrar información de la alerta junto con datos del evento asociado.

Una opción habría sido duplicar información dentro de la tabla de alertas. Sin embargo, se decidió mantener el modelo de datos más limpio y crear endpoints específicos para la interfaz, como:

```text
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Estos endpoints devuelven información enriquecida sin alterar innecesariamente la estructura principal de la base de datos.

Esta decisión permitió separar mejor la lógica interna del sistema de las necesidades concretas de visualización.

---

## Separar configuración real y configuración de ejemplo

Para evitar subir credenciales o valores sensibles al repositorio, se decidió utilizar archivos `.env` para la configuración real y `.env.example` como plantilla.

El archivo `.env.example` permite documentar las variables necesarias para ejecutar el proyecto, mientras que `.gitignore` evita que los archivos `.env` reales se suban a GitHub.

Esta decisión mejora la seguridad básica del proyecto y facilita su reproducción desde cero en otros entornos.

---

## Dejar funcionalidades avanzadas como futuras mejoras

Para mantener el proyecto dentro de un alcance asumible, se descartaron varias funcionalidades avanzadas:

```text
- Autenticación de usuarios.
- Roles y permisos.
- Integración con logs reales.
- Agentes externos.
- Dashboards avanzados.
- Notificaciones automáticas.
- Informes exportables.
- Correlación compleja.
- Despliegue en producción.
```

Estas funcionalidades podrían aportar valor en una versión futura, pero no eran necesarias para demostrar el flujo principal del MVP.

El criterio seguido fue priorizar una versión pequeña, funcional y validada antes que una versión más ambiciosa pero incompleta.

---

## Problemas que influyeron en estas decisiones

Algunas decisiones no surgieron únicamente de la planificación inicial, sino también de problemas encontrados durante el desarrollo.

Entre los más relevantes destacan:

```text
- Riesgo de que el proyecto creciera demasiado.
- Riesgo de convertirlo en una simple instalación de herramientas.
- Necesidad de justificar desarrollo propio.
- Dificultades para definir el comportamiento del motor de reglas.
- Necesidad de mantener un modelo de datos claro.
- Necesidad de ofrecer al frontend datos enriquecidos sin duplicar información.
- Necesidad de proteger la configuración sensible del proyecto.
```

Estos problemas ayudaron a ajustar el diseño y a convertir el proyecto en una solución más coherente.

---

## Conclusión

Las decisiones de diseño y alcance permitieron transformar una idea amplia en un proyecto concreto, funcional y defendible.

El sistema no intenta ser un SIEM completo, sino una representación simplificada de su flujo principal. La decisión de desarrollar componentes propios, usar eventos simulados, separar eventos/reglas/alertas y limitar el motor de detección permitió mantener el proyecto dentro de un alcance realista.

Gracias a estas decisiones, el resultado final es un MVP funcional, reproducible y adecuado para demostrar competencias de desarrollo de aplicaciones aplicadas a un contexto de ciberseguridad defensiva.