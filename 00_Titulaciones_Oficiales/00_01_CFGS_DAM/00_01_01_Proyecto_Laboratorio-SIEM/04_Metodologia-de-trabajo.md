## Enfoque general

El proyecto se ha desarrollado siguiendo un enfoque incremental. En lugar de intentar construir todas las funcionalidades desde el inicio, se ha trabajado por fases, validando cada parte antes de avanzar a la siguiente.

La prioridad ha sido conseguir primero un flujo funcional mínimo y después ampliarlo con mejoras concretas:

```text
API básica → base de datos → reglas → alertas → frontend → pruebas → documentación
````

Este enfoque permitió detectar errores de forma progresiva y evitar que el proyecto creciera sin control.

---

## Organización del trabajo

El desarrollo se dividió en varias fases principales:

```text
1. Definición del alcance del proyecto.
2. Preparación del entorno de desarrollo.
3. Diseño de la arquitectura.
4. Diseño del modelo de datos.
5. Desarrollo del backend.
6. Implementación del motor de reglas.
7. Desarrollo del frontend.
8. Pruebas y validación.
9. Documentación final.
```

Cada fase se fue ajustando en función de los problemas encontrados y de las necesidades reales del MVP.

---

## Fase 1: Definición del alcance

La primera fase consistió en concretar qué debía ser el proyecto y qué debía quedar fuera.

Al tratarse de una temática relacionada con SIEM, existía el riesgo de plantear una herramienta demasiado ambiciosa. Por ello, se decidió limitar el desarrollo a un MVP centrado en el flujo principal:

```text
evento → ingesta → almacenamiento → evaluación → alerta → consulta
```

Esta decisión permitió mantener el proyecto dentro de un alcance asumible y evitar funcionalidades que habrían añadido complejidad sin aportar valor directo a la demostración principal.

---

## Fase 2: Preparación del entorno

El entorno de desarrollo se preparó dentro de una máquina virtual llamada `siem-lab`.

Inicialmente se intentó trabajar con VMware, pero aparecieron problemas de estabilidad y compatibilidad. Finalmente se migró el entorno a VirtualBox, donde el proyecto pudo desarrollarse de forma más estable.

El uso de una máquina virtual permitió aislar el entorno de trabajo y disponer de un laboratorio controlado para ejecutar Docker, la API, la base de datos y las pruebas.

---

## Fase 3: Diseño de la arquitectura

Una vez definido el alcance, se diseñó una arquitectura sencilla basada en servicios separados:

```text
Frontend → API FastAPI → PostgreSQL
                 ↓
              Adminer
```

El sistema se organizó mediante Docker Compose, con tres servicios principales:

```text
siem-api      → backend FastAPI
siem-db       → base de datos PostgreSQL
siem-adminer  → consulta visual de base de datos
```

Esta arquitectura permitió separar responsabilidades y facilitar la reproducción del entorno.

---

## Fase 4: Diseño del modelo de datos

El modelo de datos se diseñó alrededor de tres entidades principales:

```text
events
rules
alerts
```

Los eventos representan los logs simulados que entran en el sistema.
Las reglas definen las condiciones de detección.
Las alertas representan el resultado de aplicar una regla sobre un evento.

La relación entre estas entidades permite saber qué evento generó una alerta y qué regla provocó esa detección.

---

## Fase 5: Desarrollo del backend

El backend se desarrolló con FastAPI. Se implementaron endpoints para gestionar:

```text
- Estado del sistema.
- Eventos.
- Ingesta.
- Reglas.
- Alertas.
- Métricas.
```

Durante esta fase se trabajó también con SQLAlchemy para definir modelos y con Alembic para gestionar migraciones de base de datos.

La API se fue probando desde Swagger y mediante comandos `curl`.

---

## Fase 6: Implementación del motor de reglas

Una vez disponible la ingesta de eventos y la persistencia en base de datos, se implementó el motor de reglas.

El motor evalúa cada evento recibido contra las reglas activas y genera una alerta cuando se cumplen las condiciones definidas.

Durante esta fase se tomaron decisiones importantes sobre:

```text
- Severidad mínima.
- Coincidencia por texto.
- Coincidencia por metadatos.
- Uso de group_key.
- Throttle.
- Threshold.
- Control de duplicados.
```

El objetivo fue mantener una lógica suficientemente representativa, pero sin convertir el motor en un sistema de correlación complejo.

---

## Fase 7: Desarrollo del frontend

El frontend se desarrolló con HTML, CSS y JavaScript.

Su función principal es mostrar las alertas generadas por el sistema y permitir una consulta visual básica.

El frontend consume endpoints específicos de la API, especialmente `/alerts/ui`, que devuelve información enriquecida para facilitar la visualización.

No se planteó como un dashboard avanzado, sino como una interfaz sencilla para demostrar que el sistema puede consultarse desde navegador.

---

## Fase 8: Pruebas y validación

La validación se realizó mediante pruebas manuales y automatizadas.

Las pruebas manuales permitieron comprobar el flujo completo:

```text
1. Crear o disponer de una regla activa.
2. Enviar un evento mediante /ingest.
3. Comprobar que el evento se almacena.
4. Verificar que se genera una alerta.
5. Consultar la alerta desde la API.
6. Visualizarla desde el frontend.
7. Cambiar su estado.
```

También se ejecutaron tests automatizados con Pytest dentro del contenedor de la API:

```bash
docker compose exec api python -m pytest
```

El resultado final fue correcto, con los tests superados.

---

## Fase 9: Documentación

La fase final consistió en consolidar la documentación del proyecto.

Se actualizó el README para incluir:

```text
- Descripción del proyecto.
- Objetivos.
- Stack tecnológico.
- Arquitectura.
- Instalación.
- Reproducción desde cero.
- Endpoints principales.
- Ejemplos de uso.
- Pruebas.
- Limitaciones.
- Futuras mejoras.
```

También se documentaron los problemas encontrados durante el desarrollo, ya que forman parte del proceso real de construcción del proyecto.

---

## Herramientas utilizadas durante el trabajo

Durante el desarrollo se utilizaron distintas herramientas:

```text
Visual Studio Code       → edición de código
Docker Compose           → ejecución de servicios
VirtualBox               → máquina virtual de laboratorio
FastAPI Swagger          → prueba de endpoints
Adminer                  → revisión de base de datos
curl                     → pruebas desde terminal
Pytest                   → pruebas automatizadas
Git/GitHub               → control de versiones
Obsidian                 → organización de notas
Excalidraw               → diagramas del proyecto
```

Cada herramienta se utilizó con una finalidad concreta dentro del proceso de desarrollo.

---

## Gestión de problemas

Los problemas encontrados se trataron como parte del proceso de desarrollo. En lugar de ocultarlos, se documentaron para explicar cómo afectaron al proyecto y qué decisiones se tomaron para resolverlos.

Los problemas más relevantes estuvieron relacionados con:

```text
- Virtualización.
- Configuración del entorno.
- Persistencia de volúmenes Docker.
- Conexión con PostgreSQL.
- Dependencias de pruebas.
- Definición del alcance.
- Diseño del motor de reglas.
- Documentación final.
```

Esta forma de trabajo permitió transformar los errores en aprendizajes técnicos y mejorar la calidad final del proyecto.

---

## Criterio de validación

El proyecto se consideró validado cuando se pudo demostrar el flujo completo de extremo a extremo:

```text
evento simulado → ingesta → base de datos → motor de reglas → alerta → frontend
```

Además, se comprobó que:

```text
- Los contenedores arrancaban correctamente.
- La API respondía.
- La base de datos estaba accesible.
- Swagger documentaba los endpoints.
- Adminer permitía revisar las tablas.
- Las alertas podían filtrarse.
- El estado de una alerta podía modificarse.
- Los tests automatizados se ejecutaban correctamente.
```

Este criterio permitió cerrar el proyecto con una versión funcional y demostrable.

---

## Conclusión

La metodología seguida permitió avanzar de forma ordenada desde una idea inicial hasta un MVP funcional.

El trabajo por fases facilitó la detección de problemas, la toma de decisiones y la validación progresiva del sistema. Además, permitió mantener el alcance bajo control y priorizar las funcionalidades esenciales del proyecto.

