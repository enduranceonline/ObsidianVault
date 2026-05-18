## Introducción

Durante el diseño del SIEM Lab MVP se aplicaron varios criterios para mantener el sistema claro, funcional y fácil de validar.

Estos criterios sirvieron como guía para tomar decisiones técnicas durante el desarrollo del backend, la base de datos, el motor de reglas y el frontend.

El objetivo principal fue construir una aplicación sencilla, pero con una estructura suficientemente ordenada para poder explicar su funcionamiento y ampliarla en el futuro.

---

## Separación de responsabilidades

Uno de los criterios principales fue separar las responsabilidades entre componentes.

El sistema se dividió en partes diferenciadas:

```text
Frontend      → visualización de alertas
API FastAPI   → lógica principal del sistema
PostgreSQL    → persistencia de datos
Adminer       → inspección auxiliar de base de datos
Docker Compose → ejecución coordinada de servicios
````

Esta separación permite que cada componente tenga una función concreta y evita mezclar lógica de presentación, lógica de negocio y almacenamiento.

---

## API como núcleo del sistema

La API se diseñó como el componente central del proyecto.

Todas las operaciones importantes pasan por FastAPI:

```text
- Recibir eventos.
- Guardar eventos.
- Consultar reglas.
- Ejecutar el motor de reglas.
- Generar alertas.
- Consultar alertas.
- Cambiar estados.
- Devolver métricas.
```

El frontend y las pruebas no acceden directamente a la base de datos. La API actúa como punto de entrada controlado y mantiene la lógica principal centralizada.

---

## Modelo de datos simple y trazable

El modelo de datos se diseñó con tres entidades principales:

```text
events
rules
alerts
```

El criterio seguido fue mantener una estructura simple, pero trazable.

Cada alerta se relaciona con:

```text
- El evento que la originó.
- La regla que se activó.
```

Esta relación permite explicar el origen de cada alerta y comprobar el comportamiento del sistema durante las pruebas.

---

## Evitar duplicación innecesaria de datos

Durante el diseño se evitó duplicar todos los datos del evento dentro de la alerta.

La alerta almacena la relación con el evento y la regla, mientras que la información detallada puede recuperarse mediante consultas.

Para facilitar el consumo desde el frontend se crearon endpoints enriquecidos:

```text
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

De esta forma, el modelo de datos se mantiene más limpio y el frontend recibe la información que necesita.

---

## Flujo principal antes que funcionalidades secundarias

El diseño priorizó el flujo principal del sistema:

```text
evento → ingesta → almacenamiento → evaluación → alerta → consulta
```

Cada componente se diseñó pensando en reforzar este flujo.

Antes de añadir funcionalidades avanzadas, se validó que el sistema pudiera:

```text
- Recibir un evento.
- Guardarlo en base de datos.
- Evaluarlo con reglas.
- Generar una alerta.
- Consultarla desde API.
- Mostrarla desde frontend.
```

Este criterio permitió mantener el proyecto enfocado.

---

## Motor de reglas previsible

El motor de reglas se diseñó para ser simple y fácil de entender.

Las condiciones principales son:

```text
source
severity_min
contains
meta_match
threshold_count
threshold_seconds
throttle_seconds
```

Durante el desarrollo se decidió que el comportamiento del motor debía ser previsible antes que complejo.

Por eso se definieron reglas claras para `group_key`, `threshold` y `throttle`:

```text
- El group_key se obtiene de meta.host.
- Las alertas simples pueden generarse sin group_key.
- El throttle y el anti-duplicado dependen del group_key.
- Los thresholds requieren group_key.
```

Esta decisión redujo ambigüedades y facilitó la validación.

---

## Frontend como apoyo visual

El frontend se diseñó como una interfaz de apoyo, no como el centro del proyecto.

Su función principal es mostrar que las alertas generadas por el backend pueden consultarse visualmente desde navegador.

Por este motivo se utilizaron tecnologías básicas:

```text
HTML
CSS
JavaScript
```

No se incorporó un framework frontend avanzado porque habría aumentado la complejidad sin aportar valor directo al objetivo principal del MVP.

---

## Reproducibilidad del entorno

Otro criterio importante fue que el proyecto pudiera reproducirse desde cero.

Para ello se utilizó Docker Compose y se documentaron los pasos principales:

```text
- Crear archivos .env desde .env.example.
- Levantar servicios con Docker Compose.
- Ejecutar migraciones.
- Probar endpoints principales.
- Enviar eventos de ejemplo.
- Consultar alertas.
- Ejecutar tests.
```

Este criterio permitió reducir la dependencia del entorno local y facilitar la entrega del proyecto.

---

## Configuración separada del código

La configuración del sistema se separó del código mediante archivos `.env`.

El repositorio incluye un archivo `.env.example` para indicar las variables necesarias sin exponer credenciales reales.

Este criterio permite:

```text
- Evitar subir secretos al repositorio.
- Facilitar la configuración en otro entorno.
- Mantener el proyecto más limpio.
- Documentar las variables necesarias.
```

---

## Validación progresiva

El sistema se diseñó para poder validarse por partes.

Durante el desarrollo se comprobaron progresivamente:

```text
- Estado de la API.
- Conexión con PostgreSQL.
- Creación de reglas.
- Ingesta de eventos.
- Generación de alertas.
- Consulta de alertas.
- Filtros.
- Cambio de estado.
- Funcionamiento del frontend.
- Ejecución de tests.
```

Esta validación incremental permitió detectar problemas de forma más controlada.

---

## Uso de herramientas auxiliares

Se incorporaron herramientas auxiliares para facilitar el desarrollo y la validación.

Las principales fueron:

```text
Swagger → prueba y documentación de endpoints
Adminer → inspección visual de PostgreSQL
curl    → pruebas manuales desde terminal
Pytest  → pruebas automatizadas
GitHub  → control de versiones y entrega
```

Estas herramientas no sustituyen al sistema desarrollado, pero ayudaron a comprobar su funcionamiento.

---

## Control de complejidad

Un criterio constante fue evitar añadir complejidad innecesaria.

Se descartaron funcionalidades como:

```text
- Autenticación.
- Roles.
- Logs reales.
- Dashboard avanzado.
- Notificaciones.
- Informes.
- Despliegue en producción.
```

Estas funciones podrían ser útiles en una versión futura, pero no eran necesarias para validar el núcleo del sistema.

---

## Conclusión

Los criterios de diseño permitieron construir un sistema ordenado, comprensible y ajustado al alcance del proyecto.

La separación de responsabilidades, el modelo de datos simple, el motor de reglas previsible, el frontend ligero y la reproducibilidad mediante Docker fueron decisiones clave para completar el MVP.

El resultado es una arquitectura sencilla, pero suficiente para demostrar el flujo principal de un laboratorio SIEM básico.