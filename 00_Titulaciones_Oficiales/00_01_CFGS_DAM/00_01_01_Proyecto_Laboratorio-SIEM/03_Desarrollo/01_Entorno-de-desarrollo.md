## Introducción

El entorno de desarrollo del proyecto se preparó con el objetivo de trabajar en un laboratorio aislado, reproducible y adecuado para ejecutar los servicios necesarios del SIEM Lab MVP.

El sistema se desarrolló dentro de una máquina virtual Linux llamada `siem-lab`, utilizando Docker Compose para levantar los servicios principales del proyecto.

---

## Entorno principal

El proyecto se ejecuta dentro de la ruta:

```bash
/home/endurance/siem-lab
````

Dentro de esta carpeta se encuentra el código fuente del backend, el frontend, la configuración de Docker, los archivos de entorno, las pruebas y la documentación.

La estructura general del proyecto es:

```text
siem-lab/
├── backend/
├── frontend/
├── docker/
├── .env
├── .env.example
├── .gitignore
└── README.md
```

---

## Máquina virtual

El desarrollo se realizó dentro de una máquina virtual llamada:

```text
siem-lab
```

La máquina virtual permitió aislar el entorno del sistema anfitrión y disponer de un espacio controlado para instalar dependencias, ejecutar Docker y validar el proyecto.

El uso de una VM también permitió simular mejor un entorno de laboratorio, separando el proyecto del sistema principal.

---

## Cambio de VMware a VirtualBox

Inicialmente se intentó trabajar con VMware, pero aparecieron problemas de estabilidad y compatibilidad que dificultaban el avance del proyecto.

Como solución, se decidió migrar el entorno a **VirtualBox**.

Esta decisión permitió recuperar estabilidad y continuar el desarrollo con una máquina virtual funcional. El cambio de plataforma fue uno de los primeros problemas importantes del proyecto, ya que demostró la importancia de tener un entorno base fiable antes de avanzar con el desarrollo de la aplicación.

---

## Problemas con VirtualBox en Kali Linux

Durante el desarrollo también aparecieron errores relacionados con VirtualBox en el sistema anfitrión Kali Linux.

Los errores principales fueron:

```text
VERR_VM_DRIVER_NOT_INSTALLED
VERR_VM_DRIVER_VERSION_MISMATCH
```

Estos errores estaban relacionados con los módulos de VirtualBox y su compatibilidad con el kernel del sistema.

La solución consistió en revisar y sincronizar los paquetes necesarios de VirtualBox, incluyendo:

```text
virtualbox
virtualbox-qt
virtualbox-dkms
```

Este problema permitió entender mejor la dependencia entre VirtualBox, los módulos DKMS y el kernel del sistema operativo.

---

## Problema de pantalla negra en la máquina virtual

En una fase posterior, la máquina virtual arrancaba pero se quedaba en pantalla negra.

Este problema impedía acceder correctamente al entorno de trabajo. Se solucionó revisando la configuración gráfica de VirtualBox y ajustando los parámetros necesarios hasta conseguir que la VM volviera a arrancar correctamente.

Este incidente reforzó la necesidad de saber diagnosticar problemas del entorno y no asumir que todos los errores proceden del código del proyecto.

---

## Uso de Docker Compose

Dentro de la máquina virtual, los servicios principales se ejecutan mediante Docker Compose.

El archivo principal de configuración se encuentra en:

```bash
docker/compose.yml
```

Los servicios definidos son:

```text
siem-api      → backend FastAPI
siem-db       → base de datos PostgreSQL
siem-adminer  → interfaz web para PostgreSQL
```

El entorno se levanta con:

```bash
cd ~/siem-lab/docker
docker compose up -d --build
```

Y se comprueba con:

```bash
docker compose ps
```

---

## Servicios del entorno

### siem-api

Contenedor encargado de ejecutar la aplicación FastAPI mediante Uvicorn.

Expone la API en el puerto:

```text
8000
```

URLs principales:

```text
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/health
http://127.0.0.1:8000/metrics
```

---

### siem-db

Contenedor encargado de ejecutar PostgreSQL.

Almacena las tablas principales del sistema:

```text
events
rules
alerts
alembic_version
```

La API se comunica con PostgreSQL a través de la red interna de Docker Compose.

---

### siem-adminer

Contenedor encargado de ejecutar Adminer.

Se utiliza para revisar la base de datos desde navegador.

URL:

```text
http://127.0.0.1:8080
```

Adminer fue útil para comprobar visualmente que los eventos, reglas y alertas se estaban guardando correctamente.

---

## Frontend local

El frontend se sirve de forma independiente mediante el servidor HTTP de Python.

Comando utilizado:

```bash
cd ~/siem-lab
python3 -m http.server 5173 -d frontend
```

URL:

```text
http://127.0.0.1:5173/index.html
```

En esta versión no se creó un contenedor específico para el frontend porque se trataba de una interfaz sencilla basada en HTML, CSS y JavaScript.

Esta decisión permitió reducir complejidad y mantener el foco en la API y el motor de reglas.

---

## Archivos de configuración

El proyecto utiliza archivos `.env` para la configuración del entorno.

También se incluye un archivo:

```text
.env.example
```

Este archivo sirve como plantilla para reproducir el proyecto sin exponer credenciales reales.

La configuración sensible se excluye del repositorio mediante `.gitignore`.

Fragmento relevante:

```gitignore
# Env/secrets
.env
.env.*
!.env.example
```

Esta decisión evita subir credenciales locales a GitHub y facilita la reproducción del proyecto en otros entornos.

---

## Problema con credenciales de PostgreSQL

Durante el desarrollo apareció un error de autenticación entre la API y PostgreSQL:

```text
FATAL: password authentication failed for user "siem"
```

La causa fue que el volumen persistente de PostgreSQL conservaba una contraseña anterior, aunque la configuración del entorno se hubiera modificado.

La solución fue cambiar la contraseña directamente dentro de PostgreSQL:

```bash
docker compose exec db psql -U siem -d siem -c "ALTER USER siem WITH PASSWORD 'change_me';"
docker compose restart api
```

Después de aplicar esta solución, el endpoint `/health` respondió correctamente.

Este problema fue importante porque permitió comprender que los volúmenes Docker conservan datos aunque se modifiquen variables de entorno.

---

## Herramientas utilizadas

Durante el desarrollo se utilizaron varias herramientas:

```text
Visual Studio Code → edición del código
Docker Compose     → ejecución de servicios
VirtualBox         → virtualización
Swagger            → prueba de endpoints
Adminer            → inspección de PostgreSQL
curl               → pruebas manuales
Pytest             → pruebas automatizadas
Git/GitHub         → control de versiones
Obsidian           → documentación y organización de notas
Excalidraw         → diagramas
```

Cada herramienta tuvo una función concreta dentro del proceso.

---

## Validación del entorno

Para considerar que el entorno estaba correctamente preparado, se comprobaron los siguientes puntos:

```text
- La máquina virtual arrancaba correctamente.
- Docker Compose levantaba los contenedores.
- PostgreSQL estaba operativo.
- La API respondía en el puerto 8000.
- Swagger estaba disponible.
- Adminer permitía acceder a la base de datos.
- El frontend podía servirse en el puerto 5173.
- Los tests podían ejecutarse dentro del contenedor de la API.
```

---

## Comandos principales

Levantar el entorno:

```bash
cd ~/siem-lab/docker
docker compose up -d --build
```

Comprobar contenedores:

```bash
docker compose ps
```

Ver logs de la API:

```bash
docker compose logs -f api
```

Comprobar healthcheck:

```bash
curl http://127.0.0.1:8000/health
```

Ejecutar migraciones:

```bash
docker compose exec api alembic upgrade head
```

Ejecutar tests:

```bash
docker compose exec api python -m pytest
```

Servir frontend:

```bash
cd ~/siem-lab
python3 -m http.server 5173 -d frontend
```

---

## Aprendizajes relacionados con el entorno

La preparación del entorno permitió obtener varios aprendizajes importantes:

```text
- La importancia de trabajar sobre una base estable.
- La diferencia entre errores de entorno y errores de código.
- El papel de Docker Compose en proyectos reproducibles.
- El funcionamiento de los volúmenes persistentes de Docker.
- La utilidad de Adminer para validar datos.
- La conveniencia de separar configuración real y configuración de ejemplo.
- La importancia de documentar comandos de arranque y validación.
```

---

## Conclusión

El entorno de desarrollo fue una parte importante del proyecto, ya que permitió ejecutar y validar todos los componentes del SIEM Lab MVP de forma aislada.

La combinación de VirtualBox, Docker Compose, PostgreSQL, FastAPI y Adminer permitió construir un laboratorio local suficiente para desarrollar, probar y demostrar el funcionamiento del sistema.

Los problemas encontrados durante la preparación del entorno ayudaron a mejorar la comprensión de la virtualización, los contenedores, la persistencia y la configuración del proyecto.