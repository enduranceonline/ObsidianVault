## Introducción

Este anexo recopila los comandos más utilizados durante el desarrollo, validación y ejecución del **SIEM Lab MVP**.

Los comandos están organizados por finalidad:

```text
- Gestión del entorno Docker.
- Comprobación de la API.
- Migraciones de base de datos.
- Pruebas de ingesta.
- Consulta de alertas.
- Cambio de estado de alertas.
- Ejecución del frontend.
- Pruebas automatizadas.
- Git y repositorio.
````

La finalidad de esta nota es disponer de una referencia rápida para levantar, probar y revisar el proyecto.

---

## Acceder al proyecto

Ruta principal del proyecto:

```bash
cd ~/siem-lab
```

Ruta del entorno Docker:

```bash
cd ~/siem-lab/docker
```

---

## Levantar el entorno Docker

Desde la carpeta `docker/`:

```bash
cd ~/siem-lab/docker
docker compose up -d --build
```

Este comando construye y levanta los servicios definidos en Docker Compose.

Servicios principales:

```text
siem-api
siem-db
siem-adminer
```

---

## Comprobar servicios Docker

```bash
docker compose ps
```

Este comando permite comprobar si los contenedores están activos.

Resultado esperado:

```text
siem-api      → en ejecución
siem-db       → en ejecución / healthy
siem-adminer  → en ejecución
```

---

## Parar servicios Docker

```bash
docker compose down
```

Este comando detiene los servicios del proyecto.

---

## Reconstruir servicios

```bash
docker compose up -d --build
```

Se utiliza cuando se han realizado cambios en el código, dependencias o configuración de contenedores.

---

## Ver logs de la API

```bash
docker compose logs -f api
```

Permite revisar la salida del backend FastAPI.

Útil para diagnosticar:

```text
- Errores de conexión.
- Fallos de endpoints.
- Problemas de arranque.
- Trazas de ejecución.
```

---

## Ver logs de PostgreSQL

```bash
docker compose logs -f db
```

Permite revisar la salida del contenedor de base de datos.

Útil para detectar errores como:

```text
- Fallos de autenticación.
- Problemas de inicialización.
- Errores de conexión.
```

---

## Comprobar estado de la API

```bash
curl http://127.0.0.1:8000/health
```

Respuesta esperada:

```json
{
  "status": "ok",
  "db": "ok"
}
```

Este comando valida que:

```text
- La API responde.
- La conexión con PostgreSQL funciona.
```

---

## Consultar información de la API

```bash
curl http://127.0.0.1:8000/info
```

Permite comprobar información básica de la aplicación.

---

## Consultar métricas

```bash
curl -s http://127.0.0.1:8000/metrics | python3 -m json.tool
```

Devuelve métricas generales del sistema:

```text
events_total
rules_total
rules_enabled
alerts_total
```

Este comando es útil antes y después de enviar eventos para comprobar si han aumentado los contadores.

---

## Acceder a Swagger

URL:

```text
http://127.0.0.1:8000/docs
```

Swagger permite probar los endpoints desde navegador.

---

## Ejecutar migraciones

Desde `~/siem-lab/docker`:

```bash
docker compose exec api alembic upgrade head
```

Este comando aplica las migraciones de Alembic y crea o actualiza las tablas de PostgreSQL.

Tablas principales:

```text
events
rules
alerts
alembic_version
```

---

## Acceder a PostgreSQL desde el contenedor

```bash
docker compose exec db psql -U siem -d siem
```

Permite entrar en la consola de PostgreSQL.

Salir de PostgreSQL:

```sql
\q
```

---

## Cambiar contraseña del usuario PostgreSQL

Comando utilizado para corregir el problema de autenticación:

```bash
docker compose exec db psql -U siem -d siem -c "ALTER USER siem WITH PASSWORD 'change_me';"
docker compose restart api
```

Este comando solo debe utilizarse si existe un problema de credenciales entre la API y PostgreSQL.

---

## Acceder a Adminer

URL:

```text
http://127.0.0.1:8080
```

Datos habituales de conexión:

```text
Sistema: PostgreSQL
Servidor: db
Usuario: siem
Base de datos: siem
```

Adminer permite revisar visualmente las tablas y registros de la base de datos.

---

## Consultar reglas

```bash
curl -s http://127.0.0.1:8000/rules | python3 -m json.tool
```

Permite ver las reglas configuradas y comprobar cuáles están activas.

---

## Enviar evento de prueba a /ingest

```bash
HOST="demo-$(date +%s)"

curl -s -X POST http://127.0.0.1:8000/ingest \
  -H "Content-Type: application/json" \
  -d "{
    \"source\": \"ssh\",
    \"severity\": 7,
    \"message\": \"failed password for invalid user demo\",
    \"meta\": {
      \"host\": \"$HOST\"
    }
  }" | python3 -m json.tool
```

Este comando envía un evento SSH simulado.

El uso de `HOST="demo-$(date +%s)"` genera un valor dinámico para evitar duplicados y facilitar la identificación de la alerta generada.

---

## Consultar alertas enriquecidas

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

Este comando devuelve las alertas junto con información del evento asociado.

Campos relevantes:

```text
id
rule_id
event_id
title
group_key
status
rule_name
event_source
event_severity
event_message
```

---

## Filtrar alertas por estado

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?status=ack" | python3 -m json.tool
```

Estados posibles:

```text
open
ack
closed
```

---

## Filtrar alertas por severidad mínima

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?severity_min=7" | python3 -m json.tool
```

Devuelve alertas cuyo evento asociado tiene severidad igual o superior a la indicada.

---

## Buscar alertas por texto

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?q=failed" | python3 -m json.tool
```

Permite buscar alertas relacionadas con una cadena de texto.

---

## Consultar una alerta enriquecida concreta

```bash
curl -s "http://127.0.0.1:8000/alerts/8/ui" | python3 -m json.tool
```

Devuelve información detallada de una alerta concreta.

---

## Cambiar estado de una alerta

Ejemplo con la alerta `8`:

```bash
curl -s -X PATCH http://127.0.0.1:8000/alerts/8 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "ack"
  }' | python3 -m json.tool
```

Este comando cambia el estado de la alerta a `ack`.

Estados permitidos:

```text
open
ack
closed
```

---

## Servir frontend

Desde la raíz del proyecto:

```bash
cd ~/siem-lab
python3 -m http.server 5173 -d frontend
```

URL:

```text
http://127.0.0.1:5173/index.html
```

El frontend consume la API y muestra las alertas generadas.

---

## Ejecutar pruebas automatizadas

Desde `~/siem-lab/docker`:

```bash
docker compose exec api python -m pytest
```

Resultado validado:

```text
4 passed in 1.00s
```

Las pruebas deben ejecutarse dentro del contenedor `api`, ya que representa el entorno correcto del backend.

---

## Comprobar estructura del proyecto

Desde la raíz del proyecto:

```bash
find . -maxdepth 2 -type d | sort
```

Permite revisar las carpetas principales.

---

## Ver estado de Git

```bash
git status
```

Muestra archivos modificados, añadidos o pendientes de commit.

---

## Ver diferencias antes de confirmar cambios

```bash
git diff
```

Para un archivo concreto:

```bash
git diff README.md
```

---

## Añadir cambios a Git

```bash
git add .
```

O un archivo concreto:

```bash
git add README.md
```

---

## Crear commit

```bash
git commit -m "Update project documentation"
```

---

## Subir cambios a GitHub

```bash
git push
```

---

## Comandos de validación rápida

Secuencia mínima para comprobar el sistema:

```bash
cd ~/siem-lab/docker

docker compose ps

curl http://127.0.0.1:8000/health

curl -s http://127.0.0.1:8000/metrics | python3 -m json.tool

curl -s http://127.0.0.1:8000/rules | python3 -m json.tool

curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

---

## Secuencia completa de prueba

```bash
cd ~/siem-lab/docker

docker compose up -d --build

docker compose exec api alembic upgrade head

curl http://127.0.0.1:8000/health

curl -s http://127.0.0.1:8000/metrics | python3 -m json.tool

HOST="demo-$(date +%s)"

curl -s -X POST http://127.0.0.1:8000/ingest \
  -H "Content-Type: application/json" \
  -d "{
    \"source\": \"ssh\",
    \"severity\": 7,
    \"message\": \"failed password for invalid user demo\",
    \"meta\": {
      \"host\": \"$HOST\"
    }
  }" | python3 -m json.tool

curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool

docker compose exec api python -m pytest
```

---

## URLs principales

```text
API Healthcheck:
http://127.0.0.1:8000/health

Swagger:
http://127.0.0.1:8000/docs

Adminer:
http://127.0.0.1:8080

Frontend:
http://127.0.0.1:5173/index.html
```

---

## Conclusión

Estos comandos permiten levantar, probar, validar y revisar el SIEM Lab MVP.

La combinación de Docker Compose, curl, Swagger, Adminer, Pytest y frontend permite comprobar el funcionamiento completo del sistema desde distintos puntos de vista.