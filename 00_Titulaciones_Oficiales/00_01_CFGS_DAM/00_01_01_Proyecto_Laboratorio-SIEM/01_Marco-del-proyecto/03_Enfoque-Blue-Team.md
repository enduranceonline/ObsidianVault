## Qué es el enfoque Blue Team

Dentro de la ciberseguridad, el enfoque **Blue Team** se centra en la defensa, monitorización, detección y respuesta ante posibles incidentes de seguridad.

Mientras que otros enfoques se orientan a encontrar vulnerabilidades o simular ataques, el Blue Team trabaja desde la perspectiva de proteger sistemas, revisar eventos, analizar alertas y mejorar la capacidad de detección de una organización.

Este proyecto se relaciona con el enfoque Blue Team porque reproduce una parte básica del proceso defensivo:

```text
recibir eventos → aplicar reglas → generar alertas → revisarlas
````

---

## Relación con un entorno SOC

Un **SOC** o _Security Operations Center_ es un equipo encargado de monitorizar la seguridad de una organización. Una de sus tareas principales es revisar alertas generadas por herramientas de seguridad, analizar si son relevantes y decidir si requieren actuación.

De forma simplificada, el trabajo puede representarse así:

```text
1. Los sistemas generan eventos.
2. Las herramientas de monitorización los recopilan.
3. Se aplican reglas de detección.
4. Se generan alertas.
5. Un analista revisa las alertas.
6. Se clasifican, investigan o cierran.
```

El proyecto no implementa un SOC real, pero sí reproduce los elementos básicos sobre los que se apoya este tipo de trabajo: eventos, reglas, alertas y estados.

---

## Papel de los eventos

Los eventos son la materia prima de la monitorización. Sin eventos no hay información que analizar.

En un entorno defensivo, los eventos pueden proceder de diferentes fuentes:

```text
- Sistemas operativos
- Servicios de autenticación
- Aplicaciones web
- Firewalls
- Bases de datos
- Dispositivos de red
```

En este proyecto, los eventos son simulados y se envían mediante la API. Aunque no proceden de sistemas reales, permiten representar la lógica principal de ingesta y análisis.

---

## Papel de las reglas

Las reglas permiten transformar eventos en alertas. Una regla define qué condiciones deben cumplirse para considerar que un evento merece atención.

Por ejemplo, una regla puede detectar:

```text
- Intentos fallidos de autenticación.
- Eventos con severidad elevada.
- Mensajes que contienen palabras concretas.
- Actividad repetida desde un mismo host.
```

En el proyecto, las reglas son una parte central porque permiten introducir lógica de detección propia, sin depender de herramientas externas.

---

## Papel de las alertas

Una alerta representa un evento o conjunto de eventos que cumplen una condición de detección.

Desde el punto de vista Blue Team, una alerta no significa necesariamente que exista un incidente real. Significa que hay algo que debe revisarse.

Por eso el proyecto incluye estados básicos de alerta:

```text
open   → alerta abierta
ack    → alerta reconocida
closed → alerta cerrada
```

Estos estados permiten representar de forma sencilla el ciclo de revisión de una alerta.

---

## Priorización y reducción de ruido

Uno de los problemas habituales en monitorización es el exceso de información. Si un sistema genera demasiadas alertas poco relevantes, el analista puede perder tiempo revisando ruido.

Por este motivo, en seguridad defensiva son importantes conceptos como:

```text
- Severidad
- Filtrado
- Agrupación
- Control de duplicados
- Umbrales
- Throttle
```

El proyecto incorpora una versión básica de estos conceptos para evitar que la generación de alertas sea completamente indiscriminada.

---

## Qué parte del enfoque Blue Team reproduce el proyecto

El proyecto reproduce una parte concreta del flujo defensivo:

```text
Evento recibido
        ↓
Evaluación mediante regla
        ↓
Generación de alerta
        ↓
Consulta y cambio de estado
```

Esto permite trabajar una visión práctica de cómo una herramienta defensiva puede convertir datos técnicos en información revisable.

No se implementan fases posteriores como investigación completa, respuesta ante incidentes, contención, erradicación o análisis forense. Esas fases quedan fuera del alcance del MVP.

---

## Valor formativo del enfoque

El enfoque Blue Team aporta valor al proyecto porque permite trabajar con un caso de uso técnico realista.

A nivel de desarrollo, obliga a diseñar una aplicación con entrada de datos, lógica de negocio, persistencia, consultas y visualización.

A nivel de ciberseguridad, permite entender la importancia de registrar eventos, aplicar reglas y revisar alertas de forma ordenada.

El proyecto sirve como primera aproximación a conceptos que aparecen en herramientas reales de monitorización, aunque adaptados a una escala reducida.

---

## Conclusión

El enfoque Blue Team del proyecto se centra en la detección y gestión básica de alertas.

El sistema desarrollado no pretende cubrir todas las tareas de un SOC, pero sí representa el núcleo inicial de la monitorización defensiva: recibir eventos, evaluarlos mediante reglas y generar alertas que puedan ser revisadas.