## Introducción

El **SIEM Lab MVP** cumple el objetivo principal de representar un flujo básico de ingesta, evaluación mediante reglas y generación de alertas. Sin embargo, al tratarse de una versión mínima funcional, existen varias limitaciones que deben tenerse en cuenta.

Estas limitaciones no se consideran fallos del proyecto, sino decisiones coherentes con el alcance definido. El sistema no pretende ser un SIEM real de producción, sino una aproximación educativa y funcional a algunos de sus conceptos principales.

---

## Limitación 1. Uso de eventos simulados

La principal limitación del proyecto es que los eventos utilizados son simulados.

Los eventos se envían manualmente mediante el endpoint:

```http
POST /ingest
````

Ejemplo:

```json
{
  "source": "ssh",
  "severity": 7,
  "message": "failed password for invalid user demo",
  "meta": {
    "host": "demo-1779119427"
  }
}
```

Esto permite validar el flujo principal del sistema, pero no representa una integración real con fuentes de logs.

En un entorno real, los eventos podrían proceder de:

```text
- Sistemas Linux.
- Servidores Windows.
- Firewalls.
- Aplicaciones web.
- Servicios de autenticación.
- Bases de datos.
- Dispositivos de red.
- Agentes instalados en endpoints.
```

En esta versión, el objetivo era validar la lógica interna del sistema antes de incorporar fuentes externas.

---

## Limitación 2. Ausencia de autenticación

La API no incluye autenticación de usuarios.

Esto significa que, en el entorno actual, cualquier usuario con acceso a los endpoints podría realizar acciones como:

```text
- Consultar eventos.
- Consultar reglas.
- Enviar eventos.
- Consultar alertas.
- Cambiar el estado de una alerta.
```

En una herramienta real, sería necesario proteger los endpoints mediante un sistema de autenticación.

Posibles soluciones futuras:

```text
- JWT.
- OAuth2.
- Sesiones de usuario.
- API keys.
- Integración con un proveedor de identidad.
```

La autenticación quedó fuera del alcance inicial para mantener el proyecto centrado en la ingesta, reglas y alertas.

---

## Limitación 3. Ausencia de roles y permisos

El sistema tampoco incluye gestión de roles o permisos.

En una herramienta más completa sería necesario diferenciar entre distintos tipos de usuarios, por ejemplo:

```text
Administrador → gestiona reglas, usuarios y configuración.
Analista      → revisa alertas y cambia estados.
Lector        → consulta información sin modificarla.
```

En esta versión no existe esa separación. Todas las operaciones disponibles en la API quedan accesibles si se puede acceder al servicio.

Esta limitación está relacionada con la ausencia de autenticación y sería una mejora lógica en versiones posteriores.

---

## Limitación 4. Motor de reglas básico

El motor de reglas implementado es funcional, pero limitado.

Actualmente permite trabajar con condiciones como:

```text
source
severity_min
contains
meta_match
throttle_seconds
threshold_count
threshold_seconds
```

Esto permite representar una lógica básica de detección, pero no equivale a un sistema de correlación avanzado.

Un motor de reglas más completo podría incluir:

```text
- Operadores AND/OR complejos.
- Expresiones anidadas.
- Correlación entre múltiples fuentes.
- Reglas basadas en secuencias temporales.
- Reglas por comportamiento.
- Priorización dinámica.
- Supresión de falsos positivos.
- Integración con inteligencia de amenazas.
```

En el proyecto se priorizó un motor sencillo, comprensible y validable frente a una lógica más compleja pero difícil de cerrar dentro del MVP.

---

## Limitación 5. Correlación limitada

El sistema incorpora una forma básica de agrupación mediante `group_key`, obtenido a partir de:

```text
meta.host
```

Esto permite relacionar eventos asociados a un mismo host, pero la correlación sigue siendo limitada.

No se implementan correlaciones complejas como:

```text
- Relacionar eventos de distintos sistemas.
- Detectar secuencias de ataque.
- Cruzar IPs, usuarios y hosts.
- Detectar movimiento lateral.
- Unir eventos de autenticación, red y aplicación.
- Identificar patrones distribuidos.
```

La correlación actual es suficiente para demostrar el concepto básico de agrupación, pero no representa la complejidad de un SIEM real.

---

## Limitación 6. Frontend básico

El frontend cumple su función como interfaz visual, pero tiene un alcance limitado.

Permite:

```text
- Visualizar alertas.
- Consultar información enriquecida.
- Aplicar filtros básicos.
- Actualizar datos manualmente.
```

No incluye funcionalidades avanzadas como:

```text
- Dashboard con gráficos.
- Actualización en tiempo real.
- Gestión de reglas desde la interfaz.
- Cambio de estado desde todas las vistas.
- Sistema de usuarios.
- Panel de métricas avanzado.
- Exportación de resultados.
```

El frontend se desarrolló como apoyo visual del backend, no como una aplicación completa de monitorización.

---

## Limitación 7. Sin actualización en tiempo real

El sistema no implementa actualización automática en tiempo real.

Cuando se genera una nueva alerta, el frontend puede requerir una actualización manual para mostrar los datos más recientes.

No se utilizaron mecanismos como:

```text
- WebSockets.
- Server-Sent Events.
- Polling automático.
- Colas de eventos.
```

Esta decisión redujo la complejidad del desarrollo y fue coherente con el enfoque MVP.

---

## Limitación 8. Sin sistema de incidentes

El sistema gestiona alertas, pero no incidentes.

Una alerta representa una condición detectada por una regla. Sin embargo, en herramientas reales, varias alertas podrían agruparse en un caso o incidente.

En esta versión no existen entidades como:

```text
- Incidents.
- Cases.
- Investigations.
- Comments.
- Evidence.
- Assignments.
```

Por tanto, el sistema permite revisar alertas, pero no gestionar investigaciones completas.

---

## Limitación 9. Sin historial de cambios de estado

El sistema permite cambiar el estado de una alerta, pero no almacena un historial detallado de esos cambios.

Actualmente una alerta puede estar en estados como:

```text
open
ack
closed
```

Pero no se guarda una línea temporal completa con información como:

```text
- Quién cambió el estado.
- Cuándo se cambió.
- Estado anterior.
- Estado nuevo.
- Comentario asociado.
```

Esta funcionalidad sería importante en una versión más cercana a un sistema real de operación.

---

## Limitación 10. Sin notificaciones

El sistema no envía notificaciones cuando se genera una alerta.

No se han implementado avisos mediante:

```text
- Correo electrónico.
- Telegram.
- Discord.
- Slack.
- Webhooks.
- Sistemas externos.
```

Las alertas deben consultarse manualmente desde la API o desde el frontend.

Esta limitación es aceptable para el MVP, ya que el objetivo principal era generar y consultar alertas, no automatizar su comunicación externa.

---

## Limitación 11. Despliegue local, no productivo

El proyecto está diseñado para ejecutarse en un entorno local de laboratorio.

Se utiliza:

```text
- Máquina virtual.
- Docker Compose.
- PostgreSQL local.
- Frontend servido con Python HTTP Server.
```

No está preparado para producción.

No incluye:

```text
- HTTPS.
- Reverse proxy.
- Hardening de contenedores.
- Gestión segura de secretos.
- Alta disponibilidad.
- Monitorización del propio sistema.
- Backups automatizados.
- Escalabilidad.
```

El despliegue local es suficiente para validar el funcionamiento del proyecto, pero no debe considerarse un entorno productivo.

---

## Limitación 12. Pruebas automatizadas limitadas

El proyecto incluye pruebas automatizadas con Pytest, pero su alcance es reducido.

Resultado validado:

```text
4 passed in 1.00s
```

Estas pruebas permiten comprobar parte del comportamiento del backend, pero no cubren todas las combinaciones posibles.

Quedan fuera de las pruebas automatizadas actuales:

```text
- Todos los casos del motor de reglas.
- Casos negativos de ingesta.
- Errores de validación complejos.
- Pruebas completas de filtros.
- Pruebas de frontend.
- Pruebas de carga.
- Pruebas de seguridad.
```

Las pruebas automatizadas sirven como apoyo, pero no sustituyen a la validación funcional realizada manualmente.

---

## Limitación 13. Sin normalización avanzada de eventos

Los eventos recibidos tienen una estructura simple:

```text
source
severity
message
meta
```

Esto permite validar el flujo, pero no representa la variedad real de formatos de logs.

En un entorno real, los logs pueden tener formatos diferentes según la fuente:

```text
- Syslog.
- JSON.
- Windows Event Logs.
- Logs de aplicación.
- Logs de firewall.
- Logs de servidor web.
```

Una versión avanzada debería transformar esos formatos en un modelo común antes de aplicar reglas.

---

## Limitación 14. Sin gestión avanzada de falsos positivos

El sistema puede generar alertas cuando se cumple una regla, pero no incluye mecanismos avanzados para gestionar falsos positivos.

Un falso positivo ocurre cuando una alerta parece indicar un problema, pero no representa un incidente real.

En esta versión no se incluyen funciones como:

```text
- Supresión de reglas.
- Listas blancas.
- Comentarios de analistas.
- Aprendizaje de patrones normales.
- Clasificación de alertas.
- Reglas de exclusión.
```

La revisión humana queda representada únicamente mediante el cambio de estado de la alerta.

---

## Justificación de las limitaciones

Las limitaciones anteriores son coherentes con el alcance del proyecto.

El objetivo no era crear una plataforma SIEM completa, sino construir una base funcional que permitiera demostrar:

```text
- Ingesta de eventos.
- Persistencia.
- Evaluación mediante reglas.
- Generación de alertas.
- Consulta desde API y frontend.
```

Incluir funcionalidades avanzadas habría aumentado mucho la complejidad y habría dificultado cerrar una versión validada.

La decisión de mantener el sistema como MVP permitió completar el proyecto y documentar con claridad qué partes funcionan y cuáles quedan como posibles mejoras.

---

## Conclusión

El SIEM Lab MVP tiene limitaciones claras, pero asumidas desde el diseño.

Estas limitaciones no reducen el valor del proyecto, porque el sistema cumple su objetivo principal: representar el flujo básico de un sistema de monitorización defensiva mediante una aplicación propia.

El proyecto queda como una base funcional sobre la que podrían construirse futuras ampliaciones.