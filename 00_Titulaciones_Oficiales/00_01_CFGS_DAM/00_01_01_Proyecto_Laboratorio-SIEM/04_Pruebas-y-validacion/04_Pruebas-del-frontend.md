## Introducción

Las pruebas del frontend se realizaron para comprobar que la interfaz web podía consumir correctamente la API y mostrar las alertas generadas por el sistema.

El frontend no genera eventos ni ejecuta reglas. Su función es consultar los datos procesados por el backend y mostrarlos de forma visual.

El flujo validado en esta sección es:

```text
alertas generadas → API /alerts/ui → frontend → visualización
````

---

## Objetivo de la prueba

El objetivo principal fue comprobar que el frontend:

```text
- Carga correctamente desde el navegador.
- Consume los endpoints de la API.
- Muestra alertas generadas por el sistema.
- Presenta información enriquecida de las alertas.
- Permite actualizar los datos mostrados.
- Permite consultar alertas procedentes del motor de reglas.
```

---

## Ejecución del frontend

El frontend se sirvió mediante el servidor HTTP de Python.

Comando utilizado:

```bash
cd ~/siem-lab
python3 -m http.server 5173 -d frontend
```

URL utilizada:

```text
http://127.0.0.1:5173/index.html
```

En esta versión del proyecto, el frontend no se ejecuta dentro de Docker. Se sirve como contenido estático desde la carpeta `frontend/`.

---

## Endpoint utilizado por el frontend

El frontend consume principalmente el endpoint enriquecido de alertas:

```http
GET /alerts/ui
```

Este endpoint devuelve información combinada de la alerta y del evento asociado.

También puede utilizar:

```http
GET /alerts/{alert_id}/ui
GET /alerts/ui/count
```

Estos endpoints permiten mostrar información más útil que la consulta básica de alertas.

---

## Datos que debe mostrar el frontend

El frontend debe poder mostrar información como:

```text
- ID de alerta.
- Estado de la alerta.
- Nombre de la regla activada.
- Source del evento.
- Severidad del evento.
- Mensaje del evento.
- group_key.
- Fecha de creación.
```

Estos datos permiten comprobar visualmente que la alerta procede de un evento real procesado por el backend.

---

## Resultado esperado

Después de generar una alerta mediante `/ingest`, el frontend debía mostrarla en el listado de alertas.

La alerta esperada debía corresponder con la información obtenida desde `/alerts/ui`.

En la prueba actual, la alerta principal validada fue:

```text
alert_id: 8
event_id: 19
rule_name: test_rule_ssh
group_key: demo-1779119427
status: open
event_source: ssh
event_severity: 7
event_message: failed password for invalid user demo
```

---

## Resultado obtenido

El frontend cargó correctamente desde el navegador y mostró las alertas generadas por el sistema.

Durante la validación se comprobó que las alertas disponibles en `/alerts/ui` podían visualizarse desde la interfaz.

La alerta más reciente disponible en la API era:

```text
Alerta 8 → Evento 19 → Regla test_rule_ssh
```

Datos principales:

```text
id: 8
rule_id: 7
event_id: 19
group_key: demo-1779119427
status: open
event_source: ssh
event_severity: 7
event_message: failed password for invalid user demo
```

---

## Actualización de datos

Durante la prueba se observó que, tras generar una nueva alerta, podía ser necesario actualizar la vista del frontend para que aparecieran los datos más recientes.

Este comportamiento es normal en esta versión, ya que el frontend no implementa actualización en tiempo real.

La actualización manual permite volver a consultar la API y mostrar las alertas más recientes.

---

## Evidencia 1. Frontend cargado

![[Pasted image 20260518181955.png]]

> Captura: navegador mostrando el frontend en `http://127.0.0.1:5173/index.html`.

La captura debe mostrar que la interfaz carga correctamente.

---

## Evidencia 2. Listado de alertas

![[Pasted image 20260518182149.png]]

> Captura: frontend mostrando el listado de alertas generadas.

La captura debe mostrar, si es posible, la alerta reciente:

```text
id: 8
event_id: 19
rule_name: test_rule_ssh
status: open
event_source: ssh
event_severity: 7
event_message: failed password for invalid user demo
```

---

## Evidencia 3. Relación con /alerts/ui

![[Pasted image 20260518182247.png]]

> Captura: comparación entre la salida de `/alerts/ui` y la alerta mostrada en el frontend.

La finalidad de esta evidencia es comprobar que el frontend está mostrando datos obtenidos desde la API.

---

## Interpretación del resultado

El resultado confirma que el frontend cumple su función dentro del MVP.

La API genera y expone las alertas, mientras que el frontend las consulta y las muestra visualmente.

El flujo validado es:

```text
API /alerts/ui → frontend → listado visual de alertas
```

---

## Diferencia entre frontend y Swagger

Swagger y el frontend cumplen funciones diferentes.

```text
Swagger  → permite probar endpoints de forma técnica.
Frontend → permite visualizar los resultados de forma más clara.
```

Durante el desarrollo, Swagger fue útil para probar la API. El frontend permitió comprobar que los datos podían presentarse desde una interfaz web.

---

## Problemas o consideraciones detectadas

Durante la validación del frontend se detectaron algunas consideraciones:

```text
- El frontend requiere que la API esté levantada.
- Si no se actualiza la vista, puede no mostrar inmediatamente la última alerta.
- No existe actualización automática en tiempo real.
- El frontend depende de los endpoints enriquecidos /alerts/ui.
```

Estas consideraciones son coherentes con el alcance del proyecto.

---

## Resultado de la prueba

|Elemento comprobado|Resultado|
|---|---|
|Servidor HTTP del frontend|Validado|
|Carga de `index.html`|Validado|
|Consumo de API|Validado|
|Consulta de `/alerts/ui`|Validado|
|Visualización de alertas|Validado|
|Visualización de información enriquecida|Validado|
|Actualización manual de datos|Validado|
|Actualización en tiempo real|No implementado|

---

## Limitaciones observadas

El frontend actual tiene limitaciones propias del MVP:

```text
- No tiene autenticación.
- No actualiza datos en tiempo real.
- No incluye gráficos.
- No permite crear reglas.
- No permite gestionar usuarios.
- No funciona como dashboard completo.
```

Estas limitaciones no impiden validar su función principal: mostrar alertas generadas por el backend.

---

## Conclusión

La prueba confirma que el frontend funciona correctamente como interfaz visual básica del SIEM Lab MVP.

El sistema permite consultar desde el navegador las alertas generadas por el motor de reglas y expuestas por la API.

El flujo validado es:

```text
alerta generada → /alerts/ui → frontend → visualización
```