## Introducción

El proyecto utiliza **Docker Compose** para ejecutar los servicios principales del SIEM Lab MVP de forma coordinada.

La contenerización permite levantar la API, la base de datos y la herramienta de inspección sin instalar todos los componentes directamente en el sistema anfitrión.

El objetivo principal de Docker en este proyecto es facilitar la reproducibilidad del entorno y separar los servicios del sistema.

---

## Función de Docker en el proyecto

Docker permite ejecutar cada componente principal en un contenedor independiente.

En el proyecto se utilizan tres servicios:

```text
siem-api      → Backend FastAPI
siem-db       → Base de datos PostgreSQL
siem-adminer  → Interfaz web para consultar PostgreSQL
````

Esta separación permite que cada servicio tenga una responsabilidad concreta.

---

## Docker Compose

La configuración principal se encuentra en:

```bash
docker/compose.yml
```

Docker Compose permite definir y levantar todos los servicios con un único comando:

```bash
cd ~/siem-lab/docker
docker compose up -d --build
```

Para comprobar el estado de los contenedores:

```bash
docker compose ps
```

---

## Servicio siem-api

El servicio `siem-api` ejecuta el backend desarrollado con FastAPI.

Su función es:

```text
- Recibir peticiones HTTP.
- Exponer los endpoints de la API.
- Comunicarse con PostgreSQL.
- Ejecutar el motor de reglas.
- Generar alertas.
- Devolver respuestas al frontend, Swagger o curl.
```

La API se expone en el puerto:

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

## Servicio siem-db

El servicio `siem-db` ejecuta PostgreSQL.

Su función es almacenar:

```text
- Eventos
- Reglas
- Alertas
- Información de migraciones
```

La API se conecta a esta base de datos mediante la red interna de Docker Compose.

El uso de un contenedor para PostgreSQL evita instalar la base de datos directamente en el sistema anfitrión y facilita la reproducción del entorno.

---

## Servicio siem-adminer

El servicio `siem-adminer` ejecuta Adminer.

Adminer permite consultar la base de datos desde navegador.

URL habitual:

```text
http://127.0.0.1:8080
```

Durante el desarrollo fue útil para comprobar:

```text
- Si las tablas existían.
- Si los eventos se guardaban.
- Si las reglas estaban creadas.
- Si las alertas se generaban correctamente.
```

Adminer no forma parte del flujo principal del SIEM, pero facilita la validación.

---

## Red interna de Docker

Docker Compose crea una red interna que permite que los contenedores se comuniquen entre sí.

La API no necesita conectarse a PostgreSQL usando `localhost`, sino el nombre del servicio de base de datos definido en Docker Compose.

Esto permite que el backend pueda resolver la conexión con PostgreSQL dentro del entorno de contenedores.

---

## Variables de entorno

El proyecto utiliza variables de entorno para configurar la conexión entre servicios.

Los archivos principales son:

```text
.env
.env.example
docker/.env
```

El archivo `.env.example` sirve como plantilla segura para reproducir el proyecto.

Los archivos `.env` reales no se suben al repositorio porque pueden contener credenciales o configuraciones locales.

Fragmento relevante de `.gitignore`:

```gitignore
.env
.env.*
!.env.example
```

Esta configuración permite proteger datos sensibles sin perder la posibilidad de documentar las variables necesarias.

---

## Migraciones dentro del contenedor

Las migraciones de base de datos se ejecutan desde el contenedor de la API.

Comando utilizado:

```bash
docker compose exec api alembic upgrade head
```

Esto aplica el esquema necesario en PostgreSQL y crea las tablas principales del proyecto:

```text
events
rules
alerts
alembic_version
```

Ejecutar las migraciones dentro del contenedor evita depender de instalaciones locales de Alembic o Python fuera del entorno Docker.

---

## Ejecución de pruebas dentro del contenedor

Durante el desarrollo se intentó ejecutar `pytest` desde el entorno local, pero no estaba instalado.

Error detectado:

```text
No module named pytest
```

La solución fue ejecutar las pruebas dentro del contenedor de la API:

```bash
docker compose exec api python -m pytest
```

El resultado fue correcto:

```text
4 passed
```

Este caso demostró una ventaja clara de Docker: las pruebas deben ejecutarse en el entorno donde realmente están instaladas las dependencias del proyecto.

---

## Problema con volúmenes persistentes

Uno de los problemas más importantes estuvo relacionado con PostgreSQL y los volúmenes persistentes.

El error fue:

```text
FATAL: password authentication failed for user "siem"
```

La causa fue que el volumen de PostgreSQL conservaba una contraseña anterior. Aunque se modificaran las variables de entorno, la base de datos ya inicializada mantenía su configuración previa.

La solución fue cambiar la contraseña directamente en PostgreSQL:

```bash
docker compose exec db psql -U siem -d siem -c "ALTER USER siem WITH PASSWORD 'change_me';"
docker compose restart api
```

Este problema permitió entender que reconstruir contenedores no siempre reinicia el estado de los datos si existen volúmenes persistentes.

---

## Comandos principales

Levantar entorno:

```bash
cd ~/siem-lab/docker
docker compose up -d --build
```

Parar servicios:

```bash
docker compose down
```

Ver estado:

```bash
docker compose ps
```

Ver logs de la API:

```bash
docker compose logs -f api
```

Ver logs de PostgreSQL:

```bash
docker compose logs -f db
```

Ejecutar migraciones:

```bash
docker compose exec api alembic upgrade head
```

Ejecutar tests:

```bash
docker compose exec api python -m pytest
```

Entrar en PostgreSQL:

```bash
docker compose exec db psql -U siem -d siem
```

---

## Ventajas obtenidas

El uso de Docker Compose aportó varias ventajas:

```text
- Separación entre servicios.
- Reproducibilidad del entorno.
- Menor dependencia del sistema anfitrión.
- Facilidad para levantar y parar el laboratorio.
- Ejecución controlada de API, base de datos y Adminer.
- Posibilidad de ejecutar pruebas dentro del contenedor correcto.
- Mayor claridad para documentar la puesta en marcha.
```

Estas ventajas fueron importantes para convertir el proyecto en un sistema más fácil de validar y reproducir.

---

## Limitaciones

La contenerización actual tiene algunas limitaciones:

```text
- El frontend no está contenerizado.
- No hay reverse proxy.
- No hay HTTPS.
- No hay separación entre entornos de desarrollo y producción.
- No hay configuración avanzada de redes.
- No se utiliza orquestación más compleja como Kubernetes.
```

Estas limitaciones son aceptables dentro del alcance del MVP.

---

## Posibles mejoras

En futuras versiones podrían añadirse mejoras como:

```text
- Contenerizar también el frontend.
- Añadir un reverse proxy.
- Incorporar HTTPS.
- Separar configuración de desarrollo y producción.
- Añadir healthchecks más completos.
- Automatizar migraciones al arrancar.
- Crear perfiles de Docker Compose.
```

Estas mejoras permitirían acercar el entorno a un despliegue más profesional.

---

## Conclusión

Docker Compose fue una pieza clave del proyecto porque permitió ejecutar la API, PostgreSQL y Adminer de forma coordinada y reproducible.

Además, los problemas encontrados con los volúmenes persistentes y la ejecución de tests ayudaron a comprender mejor cómo funcionan los entornos contenerizados.

La contenerización permitió que el SIEM Lab MVP pudiera ejecutarse como un laboratorio local ordenado, aislado y fácil de documentar.
