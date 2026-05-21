## Introducción

Este anexo recoge los pasos necesarios para levantar el **SIEM Lab MVP** desde cero en un entorno local.

La finalidad es disponer de una guía ordenada para preparar el proyecto, arrancar los servicios, aplicar migraciones, comprobar la API, enviar un evento de prueba y validar que se genera una alerta.

El flujo general de reproducción es:

```text
clonar proyecto → configurar entorno → levantar Docker → aplicar migraciones → validar API → probar ingesta → consultar alertas
````

---

## Requisitos previos

Antes de ejecutar el proyecto, el entorno debe disponer de:

```text
- Docker instalado.
- Docker Compose disponible.
- Git instalado.
- Python 3 disponible para servir el frontend.
- Navegador web para Swagger, Adminer y frontend.
```

El proyecto puede reproducirse en distintos entornos:

```text
- Linux nativo.
- Máquina virtual Linux.
- Windows con Docker Desktop y WSL2.
```

Durante el desarrollo se utilizó una máquina virtual Linux llamada `siem-lab`. Esta fue la opción elegida para aislar el entorno y trabajar de forma controlada, pero no es obligatorio que el sistema anfitrión sea Linux.

En Windows sería recomendable utilizar **Docker Desktop con WSL2**, ya que permite trabajar con una experiencia más parecida a Linux y reduce posibles problemas de rutas, permisos o ejecución de comandos.

En ese caso, el esquema sería:

```text
Windows
  ↓
WSL2 / Docker Desktop
  ↓
Docker Compose
  ↓
siem-api + siem-db + siem-adminer
```

El frontend también podría servirse desde WSL2 con:

```bash
python3 -m http.server 5173 -d frontend
```

o mediante otro servidor local equivalente.

---

## 1. Obtener el proyecto

Si el proyecto se descarga desde GitHub, primero se debe clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd siem-lab
```

Durante el desarrollo, la ruta utilizada fue:

```bash
cd ~/siem-lab
```

La estructura esperada del proyecto es similar a:

```text
siem-lab/
├── backend/
├── frontend/
├── docker/
├── .env.example
├── README.md
└── ...
```

---

## 2. Revisar archivos de entorno

El proyecto utiliza variables de entorno para configurar servicios como PostgreSQL y la conexión de la API con la base de datos.

Debe existir un archivo de ejemplo:

```text
.env.example
```

A partir de este archivo se puede crear el archivo real:

```bash
cp .env.example .env
```

Si también existe configuración específica dentro de la carpeta `docker/`, se debe revisar si es necesario crear allí otro archivo `.env` a partir de su plantilla correspondiente.

---

## 3. Revisar que los archivos sensibles no se suben al repositorio

El archivo `.gitignore` debe excluir archivos de entorno reales:

```gitignore
.env
.env.*
!.env.example
```

Esto permite mantener una plantilla pública sin subir credenciales o configuraciones locales.

---

## 4. Levantar los servicios Docker

Acceder a la carpeta de Docker:

```bash
cd ~/siem-lab/docker
```

Levantar los servicios:

```bash
docker compose up -d --build
```

Este comando construye y arranca los servicios principales:

```text
siem-api      → API FastAPI
siem-db       → PostgreSQL
siem-adminer  → Adminer
```

---

## 5. Comprobar el estado de los contenedores

```bash
docker compose ps
```

Resultado esperado:

```text
siem-api       Up
siem-db        Up / healthy
siem-adminer   Up
```

Si algún contenedor no aparece en ejecución, se pueden revisar los logs.

Logs de la API:

```bash
docker compose logs -f api
```

Logs de PostgreSQL:

```bash
docker compose logs -f db
```

---

## 6. Aplicar migraciones de base de datos

Una vez levantados los servicios, se aplican las migraciones con Alembic:

```bash
docker compose exec api alembic upgrade head
```

Este comando crea o actualiza las tablas principales:

```text
events
rules
alerts
alembic_version
```

---

## 7. Comprobar el estado de la API

Ejecutar:

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

Esta comprobación valida que:

```text
- La API está levantada.
- La API puede conectarse a PostgreSQL.
```

---

## 8. Acceder a Swagger

Abrir en navegador:

```text
http://127.0.0.1:8000/docs
```

Swagger permite revisar y probar los endpoints principales de la API.

Endpoints importantes:

```text
GET /health
GET /metrics
GET /rules
POST /ingest
GET /alerts/ui
PATCH /alerts/{alert_id}
```

---

## 9. Acceder a Adminer

Abrir en navegador:

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

Adminer permite comprobar visualmente las tablas y registros de PostgreSQL.

---

## 10. Consultar métricas iniciales

```bash
curl -s http://127.0.0.1:8000/metrics | python3 -m json.tool
```

Campos esperados:

```text
events_total
rules_total
rules_enabled
alerts_total
```

Las métricas permiten comprobar el estado general del sistema antes y después de enviar eventos.

---

## 11. Consultar reglas existentes

```bash
curl -s http://127.0.0.1:8000/rules | python3 -m json.tool
```

Para que `/ingest` genere alertas, debe existir al menos una regla activa compatible con el evento enviado.

Ejemplo de regla usada durante la validación:

```text
test_rule_ssh
```

Condiciones:

```text
source = ssh
severity_min = 5
contains = failed
```

---

## 12. Enviar evento de prueba

Ejecutar:

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

El uso de `HOST="demo-$(date +%s)"` genera un host diferente en cada ejecución, evitando interferencias con pruebas anteriores.

---

## 13. Interpretar la respuesta de /ingest

La respuesta de `/ingest` devuelve el evento creado.

Ejemplo:

```json
{
    "id": 18,
    "ts": "2026-05-18T15:25:09.175179Z",
    "source": "ssh",
    "severity": 7,
    "message": "failed password for invalid user demo",
    "meta": {
        "host": "demo-1779117909"
    },
    "created_at": "2026-05-18T15:25:09.180716Z"
}
```

Esta respuesta valida:

```text
- Recepción del evento.
- Creación del registro.
- Persistencia del evento.
```

No valida por sí sola la alerta generada. Para comprobar la alerta hay que consultar `/alerts/ui`.

---

## 14. Consultar alertas generadas

```bash
curl -s "http://127.0.0.1:8000/alerts/ui?limit=5" | python3 -m json.tool
```

Ejemplo de alerta validada:

```json
{
    "id": 8,
    "rule_id": 7,
    "event_id": 19,
    "title": "Rule matched: test_rule_ssh",
    "group_key": "demo-1779119427",
    "status": "open",
    "rule_name": "test_rule_ssh",
    "event_source": "ssh",
    "event_severity": 7,
    "event_message": "failed password for invalid user demo"
}
```

Relación validada:

```text
Evento 19 → Regla test_rule_ssh → Alerta 8
```

---

## 15. Cambiar el estado de una alerta

Ejemplo con la alerta `8`:

```bash
curl -s -X PATCH http://127.0.0.1:8000/alerts/8 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "ack"
  }' | python3 -m json.tool
```

Estados disponibles:

```text
open
ack
closed
```

Este comando valida la gestión básica de alertas.

---

## 16. Servir el frontend

Desde la raíz del proyecto:

```bash
cd ~/siem-lab
python3 -m http.server 5173 -d frontend
```

Abrir en navegador:

```text
http://127.0.0.1:5173/index.html
```

El frontend consulta la API y muestra las alertas generadas.

En Windows con WSL2, este comando puede ejecutarse desde la terminal de WSL dentro de la carpeta del proyecto. Si se trabaja directamente desde Windows, también puede utilizarse otro servidor local equivalente para servir los archivos estáticos del frontend.

---

## 17. Ejecutar pruebas automatizadas

Desde la carpeta `docker/`:

```bash
cd ~/siem-lab/docker
docker compose exec api python -m pytest
```

Resultado validado:

```text
4 passed in 1.00s
```

Las pruebas deben ejecutarse dentro del contenedor `api`, ya que es el entorno donde están instaladas las dependencias del backend.

---

## 18. Parar el entorno

Desde `~/siem-lab/docker`:

```bash
docker compose down
```

Este comando detiene los servicios.

Los datos de PostgreSQL pueden persistir si se utilizan volúmenes Docker.

---

## Problema posible: credenciales de PostgreSQL

Si aparece un error como:

```text
FATAL: password authentication failed for user "siem"
```

puede deberse a que PostgreSQL conserva credenciales antiguas en un volumen persistente.

Solución aplicada durante el desarrollo:

```bash
docker compose exec db psql -U siem -d siem -c "ALTER USER siem WITH PASSWORD 'change_me';"
docker compose restart api
```

Después, comprobar de nuevo:

```bash
curl http://127.0.0.1:8000/health
```

---

## Secuencia rápida completa

```bash
cd ~/siem-lab/docker

docker compose up -d --build

docker compose exec api alembic upgrade head

curl http://127.0.0.1:8000/health

curl -s http://127.0.0.1:8000/metrics | python3 -m json.tool

curl -s http://127.0.0.1:8000/rules | python3 -m json.tool

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

## Resultado esperado del proceso

Al finalizar la reproducción, el sistema debe permitir comprobar que:

```text
- Docker levanta los servicios principales.
- La API responde en el puerto 8000.
- PostgreSQL está conectado.
- Swagger está disponible.
- Adminer permite consultar la base de datos.
- /ingest recibe eventos.
- El motor de reglas genera alertas.
- /alerts/ui permite consultar alertas enriquecidas.
- El frontend muestra alertas.
- Pytest ejecuta las pruebas automatizadas.
```

---

## Conclusión

La reproducción desde cero confirma que el proyecto no depende únicamente del entorno donde fue desarrollado.

Con Docker Compose, migraciones, comandos de validación y pruebas automatizadas, el SIEM Lab MVP puede levantarse y comprobarse de forma ordenada.

Esta guía permite reconstruir el flujo completo del sistema:

```text
entorno → API → base de datos → ingesta → reglas → alertas → frontend → pruebas
```