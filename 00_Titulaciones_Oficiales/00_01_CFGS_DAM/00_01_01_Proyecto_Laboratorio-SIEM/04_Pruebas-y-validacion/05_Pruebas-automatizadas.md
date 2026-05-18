## Introducción

Las pruebas automatizadas se realizaron para comprobar parte del comportamiento del backend de forma repetible.

A diferencia de las pruebas manuales, que validan el sistema mediante comandos, navegador y frontend, las pruebas automatizadas permiten ejecutar comprobaciones desde código y verificar que determinadas funcionalidades siguen funcionando correctamente.

En este proyecto se utilizó **Pytest** como herramienta de pruebas.

---

## Objetivo de las pruebas automatizadas

El objetivo principal fue validar que el backend mantenía un comportamiento correcto en funcionalidades concretas.

Las pruebas automatizadas permiten:

```text
- Comprobar endpoints del backend.
- Detectar errores después de cambios en el código.
- Validar respuestas esperadas.
- Ejecutar pruebas de forma repetible.
- Reducir la dependencia de comprobaciones manuales.
````

En el contexto del SIEM Lab MVP, estas pruebas sirven como apoyo a las pruebas funcionales realizadas manualmente.

---

## Herramienta utilizada

La herramienta utilizada fue:

```text
Pytest
```

Pytest permite ejecutar pruebas escritas en Python y obtener un resultado resumido indicando cuántas pruebas han pasado o fallado.

Los archivos de pruebas se encuentran dentro de la carpeta:

```text
backend/tests/
```

El proyecto también incluye el archivo:

```text
backend/pytest.ini
```

Este archivo permite configurar el comportamiento de Pytest dentro del backend.

---

## Problema detectado al ejecutar pruebas localmente

Durante la validación se intentó ejecutar Pytest desde el entorno local, pero apareció un error indicando que el módulo no estaba disponible:

```text
No module named pytest
```

Este problema indicaba que `pytest` no estaba instalado en el entorno Python local desde el que se estaba intentando lanzar la prueba.

---

## Solución aplicada

Como el proyecto se ejecuta mediante Docker, se decidió ejecutar las pruebas dentro del contenedor de la API.

Esta decisión es más coherente con la arquitectura del proyecto, ya que el contenedor `siem-api` contiene las dependencias necesarias para ejecutar el backend.

Comando utilizado:

```bash
cd ~/siem-lab/docker
docker compose exec api python -m pytest
```

---

## Resultado esperado

Pytest debía ejecutar las pruebas disponibles y mostrar un resultado final indicando que las pruebas habían sido superadas.

El resultado esperado era que no aparecieran errores ni fallos.

---

## Resultado obtenido

Las pruebas automatizadas se ejecutaron correctamente dentro del contenedor de la API.

Resultado obtenido:

```text
4 passed in 1.00s
```

Este resultado confirma que las pruebas definidas en el proyecto se superaron correctamente.

---

## Evidencia 1. Ejecución de Pytest

![[Pasted image 20260518182535.png]]

> Captura: terminal mostrando la ejecución del comando `docker compose exec api python -m pytest` y el resultado `4 passed`.

La captura debe mostrar:

```text
- Comando ejecutado.
- Ejecución dentro del contenedor api.
- Resultado final de Pytest.
- Número de pruebas superadas.
```

---

## Interpretación del resultado

El resultado `4 passed` indica que las cuatro pruebas automatizadas disponibles fueron ejecutadas y superadas.

Esto confirma que las funcionalidades cubiertas por esas pruebas se comportaban correctamente en el momento de la validación.

También confirma que el contenedor de la API disponía de las dependencias necesarias para ejecutar los tests.

---

## Importancia de ejecutar las pruebas dentro del contenedor

La ejecución dentro del contenedor fue importante porque el proyecto está preparado para funcionar mediante Docker Compose.

Ejecutar las pruebas dentro del contenedor evita problemas derivados del entorno local, como:

```text
- Dependencias no instaladas.
- Versiones diferentes de Python.
- Configuración distinta.
- Rutas o variables de entorno no coincidentes.
```

En este caso, el error local `No module named pytest` se resolvió ejecutando las pruebas en el entorno correcto.

---

## Relación con Docker Compose

Docker Compose permitió disponer de un entorno controlado para ejecutar las pruebas.

El servicio utilizado fue:

```text
siem-api
```

El comando:

```bash
docker compose exec api python -m pytest
```

ejecuta Pytest dentro del contenedor ya levantado, usando las dependencias instaladas en la imagen del backend.

---

## Resultado de la prueba

|Elemento comprobado|Resultado|
|---|---|
|Pytest disponible dentro del contenedor API|Validado|
|Ejecución de pruebas automatizadas|Validado|
|Resultado sin fallos|Validado|
|4 pruebas superadas|Validado|
|Error local identificado|Validado|
|Solución mediante Docker|Validado|

---

## Problemas o consideraciones detectadas

Durante esta validación se detectó una diferencia entre el entorno local y el entorno del contenedor.

El entorno local no tenía `pytest` instalado, por lo que no era adecuado para ejecutar las pruebas directamente.

La solución fue utilizar el contenedor `siem-api`, que representa mejor el entorno real de ejecución del proyecto.

Esta situación refuerza la importancia de usar entornos reproducibles y documentar claramente dónde deben ejecutarse los comandos de validación.

---

## Limitaciones de las pruebas automatizadas

Las pruebas automatizadas actuales tienen un alcance limitado.

No cubren todo el sistema ni sustituyen a las pruebas funcionales manuales.

Limitaciones principales:

```text
- Solo existen cuatro pruebas automatizadas.
- No cubren todas las combinaciones posibles del motor de reglas.
- No sustituyen la validación manual de frontend.
- No prueban escenarios de carga.
- No validan seguridad ni autenticación.
- No cubren todas las rutas posibles de error.
```

Estas limitaciones son coherentes con el enfoque MVP del proyecto.

---

## Posibles mejoras

En futuras versiones, las pruebas automatizadas podrían ampliarse para cubrir:

```text
- Creación de eventos.
- Creación de reglas.
- Ingesta con generación de alerta.
- Ingesta sin generación de alerta.
- Filtros de alertas.
- Cambio de estado de alertas.
- Validaciones de errores.
- Casos de threshold.
- Casos de throttle.
- Casos sin group_key.
```

También podrían añadirse pruebas de integración más completas que validaran el flujo completo:

```text
crear regla → enviar evento → generar alerta → consultar alerta
```

---

## Conclusión

Las pruebas automatizadas permitieron validar parte del backend de forma repetible.

El problema inicial al ejecutar Pytest localmente se resolvió ejecutando las pruebas dentro del contenedor de la API, que era el entorno adecuado del proyecto.

El resultado `4 passed` confirma que las pruebas disponibles fueron superadas correctamente y que el backend mantenía un comportamiento estable en los casos cubiertos.