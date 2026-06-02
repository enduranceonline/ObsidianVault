
## 1️⃣ Objetivo de la nota

Esta nota resume el papel de Docker dentro del laboratorio SIEM MVP. Su función es servir como visión técnica general antes de entrar en el análisis detallado de cada archivo.

El análisis línea por línea se desarrolla en la carpeta:

```text
09_Analisis-tecnico-de-docker/
```


---

## 2️⃣ Archivos relacionados

```
docker/compose.ymlbackend/Dockerfilebackend/requirements.txt.env.exampledocker/.env
```

---

## 3️⃣ Papel de Docker en el proyecto

Docker permite levantar el laboratorio de forma reproducible sin instalar manualmente PostgreSQL, Adminer ni las dependencias del backend en el sistema anfitrión.

El entorno queda dividido en servicios independientes:

```
db       → PostgreSQLadminer  → interfaz web para consultar PostgreSQLapi      → backend FastAPI
```

---

## 4️⃣ Relación entre archivos

```
docker/compose.yml        ↓define los servicios del laboratoriobackend/Dockerfile        ↓define cómo se construye la imagen de la APIbackend/requirements.txt        ↓define las dependencias Python del backend.env.example        ↓sirve como plantilla de variables de entorno
```

---

## 5️⃣ Flujo de arranque

```
1. Docker Compose lee docker/compose.yml.2. Se cargan las variables de entorno desde docker/.env.3. Se crea la red interna siem-net.4. Se crea o reutiliza el volumen siem_db.5. Arranca PostgreSQL.6. El healthcheck comprueba que PostgreSQL está listo.7. Arranca Adminer.8. Docker construye la imagen del backend usando backend/Dockerfile.9. Se instalan las dependencias desde requirements.txt.10. Arranca Uvicorn ejecutando app.main:app.11. FastAPI queda disponible en localhost:8000.
```

---

## 6️⃣ Relación con el flujo de datos del SIEM

Docker no procesa eventos directamente, pero prepara el entorno donde ocurre el flujo principal del laboratorio:

```
API FastAPI        ↓recibe eventos        ↓valida datos        ↓guarda información en PostgreSQL        ↓evalúa reglas        ↓genera alertas
```

Sin Docker, habría que configurar manualmente Python, PostgreSQL, dependencias, puertos y variables de entorno.

---

## 7️⃣ Notas detalladas relacionadas

```
09_Analisis-tecnico-de-docker/01_docker-compose-yml09_Analisis-tecnico-de-docker/02_backend-Dockerfile09_Analisis-tecnico-de-docker/03_backend-requirements
```

---

