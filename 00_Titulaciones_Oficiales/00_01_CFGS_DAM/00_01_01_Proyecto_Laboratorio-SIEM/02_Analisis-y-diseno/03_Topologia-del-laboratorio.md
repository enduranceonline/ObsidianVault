## Introducción

El proyecto se ha desarrollado dentro de un entorno de laboratorio local. La finalidad de esta topología no es simular una infraestructura empresarial completa, sino disponer de un entorno controlado donde ejecutar la aplicación, la base de datos, los servicios auxiliares y las pruebas.

La topología combina tres niveles principales:

```text
Equipo anfitrión
        ↓
Máquina virtual siem-lab
        ↓
Servicios Docker
````

Este diseño permite aislar el proyecto del sistema principal y mantener un entorno reproducible.

---

## Visión general

La topología del laboratorio puede resumirse así:

```text
Equipo anfitrión
  └── VirtualBox
        └── VM siem-lab
              └── Docker Compose
                    ├── siem-api
                    ├── siem-db
                    └── siem-adminer
```

El usuario interactúa con el sistema desde el navegador o la terminal, accediendo a los servicios expuestos por la máquina virtual.

---

## Equipo anfitrión

El equipo anfitrión es el sistema físico desde el que se ejecuta la máquina virtual.

Desde este equipo se realizan tareas como:

```text
- Abrir la máquina virtual.
- Acceder al navegador.
- Consultar Swagger.
- Usar el frontend.
- Revisar Adminer.
- Ejecutar comandos desde terminal.
- Gestionar archivos del proyecto.
```

El equipo anfitrión no ejecuta directamente la base de datos ni la API principal del proyecto. Estos servicios se ejecutan dentro de la máquina virtual.

---

## Máquina virtual siem-lab

La máquina virtual `siem-lab` actúa como entorno principal de desarrollo y ejecución.

Dentro de ella se encuentran:

```text
- Código del proyecto.
- Docker Compose.
- Contenedores del sistema.
- Comandos de validación.
- Entorno de pruebas.
```

La decisión de trabajar dentro de una VM permitió separar el laboratorio del sistema anfitrión y reducir dependencias directas sobre el equipo principal.

Inicialmente se intentó trabajar con VMware, pero aparecieron problemas de estabilidad y compatibilidad. Finalmente se utilizó VirtualBox, que permitió continuar el desarrollo de forma más estable.

---

## Servicios Docker

Dentro de la máquina virtual, los servicios principales se ejecutan mediante Docker Compose.

Los contenedores principales son:

```text
siem-api      → backend FastAPI
siem-db       → base de datos PostgreSQL
siem-adminer  → interfaz web para consultar PostgreSQL
```

Cada servicio tiene una responsabilidad concreta:

```text
- siem-api recibe peticiones HTTP y ejecuta la lógica del sistema.
- siem-db almacena eventos, reglas y alertas.
- siem-adminer permite inspeccionar la base de datos desde navegador.
```

---

## Servicio siem-api

El contenedor `siem-api` ejecuta la aplicación FastAPI.

Sus funciones principales son:

```text
- Exponer los endpoints de la API.
- Recibir eventos mediante /ingest.
- Consultar reglas activas.
- Ejecutar el motor de reglas.
- Generar alertas.
- Consultar datos almacenados.
- Permitir el cambio de estado de alertas.
```

El servicio se expone normalmente en el puerto:

```text
8000
```

Desde este puerto se puede acceder a:

```text
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
http://127.0.0.1:8000/metrics
```

---

## Servicio siem-db

El contenedor `siem-db` ejecuta PostgreSQL.

Su función es almacenar la información persistente del sistema:

```text
- Eventos recibidos.
- Reglas configuradas.
- Alertas generadas.
- Versiones de migración de Alembic.
```

La API se comunica con la base de datos a través de la red interna de Docker Compose.

El usuario no necesita acceder directamente a PostgreSQL durante el flujo normal de uso. Para inspección visual se utiliza Adminer.

---

## Servicio siem-adminer

El contenedor `siem-adminer` ejecuta Adminer.

Adminer permite acceder a PostgreSQL desde navegador para revisar:

```text
- Tablas existentes.
- Registros almacenados.
- Eventos recibidos.
- Reglas creadas.
- Alertas generadas.
```

Se expone normalmente en el puerto:

```text
8080
```

URL habitual:

```text
http://127.0.0.1:8080
```

Adminer es una herramienta auxiliar. No forma parte del flujo principal de detección, pero fue útil para comprobar que la información se guardaba correctamente.

---

## Frontend

El frontend no se ejecuta dentro de Docker en esta versión. Se sirve de forma local mediante el servidor HTTP de Python:

```bash
python3 -m http.server 5173 -d frontend
```

URL habitual:

```text
http://127.0.0.1:5173/index.html
```

El frontend consume los endpoints de la API, principalmente los relacionados con alertas enriquecidas:

```text
GET /alerts/ui
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Esta decisión simplifica el entorno y evita añadir un contenedor adicional solo para servir archivos estáticos.

---

## Comunicación entre servicios

La comunicación entre componentes se organiza de la siguiente forma:

```text
Navegador / curl / Swagger
        ↓
siem-api
        ↓
siem-db
```

Adminer se comunica directamente con PostgreSQL:

```text
Navegador
   ↓
siem-adminer
   ↓
siem-db
```

El frontend no accede directamente a la base de datos. Todas las consultas funcionales pasan por la API.

---

## Puertos utilizados

Los puertos principales del laboratorio son:

```text
8000 → API FastAPI
8080 → Adminer
5173 → Frontend local
```

Cada puerto tiene una finalidad concreta:

```text
8000 → probar y consumir la API
8080 → inspeccionar PostgreSQL
5173 → visualizar el frontend
```

---

## Ventajas de esta topología

La topología elegida ofrece varias ventajas:

```text
- Aísla el proyecto dentro de una máquina virtual.
- Permite ejecutar servicios separados mediante Docker.
- Facilita reproducir el entorno.
- Permite inspeccionar la base de datos con Adminer.
- Mantiene el frontend simple.
- Evita instalar PostgreSQL directamente en el sistema anfitrión.
- Facilita la validación mediante comandos y navegador.
```

Para un MVP académico, esta topología resulta suficiente y fácil de defender.

---

## Problemas encontrados

Durante la preparación del laboratorio aparecieron varios problemas técnicos.

El primero fue la elección de la plataforma de virtualización. Inicialmente se intentó trabajar con VMware, pero surgieron problemas que dificultaban el avance. La solución fue migrar a VirtualBox.

También aparecieron errores relacionados con los módulos de VirtualBox en Kali Linux:

```text
VERR_VM_DRIVER_NOT_INSTALLED
VERR_VM_DRIVER_VERSION_MISMATCH
```

Estos problemas se resolvieron revisando la instalación y sincronización de los paquetes necesarios de VirtualBox y DKMS.

Otro problema fue una pantalla negra al arrancar la máquina virtual. Este incidente se solucionó ajustando la configuración gráfica de VirtualBox.

Estos problemas reforzaron la importancia de disponer de un entorno de laboratorio estable antes de avanzar con el desarrollo de la aplicación.

---

## Limitaciones de la topología

La topología actual está pensada para desarrollo y demostración local.

Sus principales limitaciones son:

```text
- No representa una red empresarial real.
- No incluye máquinas generadoras de logs reales.
- No incorpora agentes externos.
- No está preparada para producción.
- No incluye segmentación de red avanzada.
- No utiliza HTTPS ni reverse proxy.
```

Estas limitaciones son coherentes con el alcance del MVP. El objetivo era disponer de un entorno controlado para validar la aplicación, no construir una infraestructura real completa.

---

## Posibles mejoras

En una versión futura, la topología podría ampliarse con:

```text
- Una máquina Linux generadora de logs reales.
- Un agente que envíe eventos a la API.
- Un reverse proxy.
- HTTPS.
- Autenticación.
- Despliegue en un servidor externo.
- Contenerización también del frontend.
- Red de laboratorio con varias máquinas simuladas.
```

Estas mejoras permitirían acercar el laboratorio a un entorno más realista.

---

## Conclusión

La topología del laboratorio se diseñó para ser sencilla, reproducible y suficiente para validar el funcionamiento del SIEM Lab MVP.

El uso de una máquina virtual permitió aislar el entorno. Docker Compose permitió ejecutar la API, la base de datos y Adminer de forma ordenada. El frontend se mantuvo como un servicio local sencillo para evitar complejidad innecesaria.

Esta topología permitió completar y validar el flujo principal del proyecto:

```text
evento → API → PostgreSQL → regla → alerta → consulta
```