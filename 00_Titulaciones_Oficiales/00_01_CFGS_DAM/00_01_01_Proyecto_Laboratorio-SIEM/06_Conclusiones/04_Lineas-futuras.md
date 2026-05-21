## Introducción

El **SIEM Lab MVP** cumple su objetivo como versión mínima funcional, pero deja abiertas varias posibilidades de ampliación.

Las líneas futuras se plantean como mejoras que permitirían acercar el proyecto a un entorno más realista, ampliar sus funcionalidades y reforzar su valor como laboratorio de ciberseguridad defensiva.

Estas mejoras no forman parte del alcance actual, pero podrían desarrollarse a partir de la base ya creada.

---

## Integración con logs reales

La mejora más importante sería sustituir o complementar los eventos simulados por eventos procedentes de fuentes reales.

Actualmente, los eventos se envían manualmente mediante:

```http
POST /ingest
````

En una versión futura, el sistema podría recibir logs desde:

```text
- Sistemas Linux.
- Servicios SSH.
- Servidores web.
- Firewalls.
- Aplicaciones.
- Contenedores Docker.
- Máquinas virtuales del laboratorio.
```

Esta mejora permitiría que el sistema dejara de depender exclusivamente de eventos manuales y se acercara más al comportamiento de una herramienta de monitorización real.

---

## Agente de envío de eventos

Una ampliación relacionada sería desarrollar un pequeño agente encargado de leer logs de una máquina y enviarlos a la API.

El flujo podría ser:

```text
archivo de log → agente → POST /ingest → motor de reglas → alerta
```

El agente podría estar desarrollado en Python y encargarse de:

```text
- Leer archivos de log.
- Extraer líneas nuevas.
- Transformar cada línea en un evento estructurado.
- Enviar el evento a la API.
- Gestionar errores de conexión.
```

Esta mejora permitiría trabajar con una arquitectura más cercana a un sistema real de recogida de eventos.

---

## Normalización de eventos

Actualmente, los eventos tienen una estructura simple:

```text
source
severity
message
meta
```

En una versión futura sería útil añadir una fase de normalización.

La normalización consiste en convertir eventos procedentes de distintas fuentes a un formato común. Esto facilitaría aplicar reglas de forma más coherente aunque los logs originales tuvieran estructuras diferentes.

Ejemplo:

```text
Log SSH original
        ↓
Normalización
        ↓
Evento estructurado
        ↓
Evaluación mediante reglas
```

Campos normalizados posibles:

```text
- timestamp
- source
- host
- user
- ip
- action
- result
- severity
- message
```

Esta mejora sería importante si el sistema empieza a recibir logs reales de distintas fuentes.

---

## Autenticación y autorización

El sistema actual no incluye autenticación. Cualquier usuario con acceso a la API podría consultar alertas o modificar estados.

Una línea futura importante sería añadir autenticación.

Opciones posibles:

```text
- JWT.
- OAuth2.
- API keys.
- Sesiones de usuario.
```

Además de autenticar usuarios, sería necesario implementar autorización mediante roles.

Ejemplo de roles:

```text
Administrador → gestiona reglas, usuarios y configuración.
Analista      → revisa alertas y cambia estados.
Lector        → consulta información sin modificarla.
```

Esta mejora sería necesaria para acercar el proyecto a un entorno más seguro y realista.

---

## Gestión avanzada de alertas

Actualmente, las alertas pueden encontrarse en tres estados:

```text
open
ack
closed
```

Esta gestión es suficiente para el MVP, pero podría ampliarse.

Mejoras posibles:

```text
- Historial de cambios de estado.
- Comentarios en alertas.
- Asignación de alertas a usuarios.
- Prioridad de alertas.
- Clasificación por tipo.
- Agrupación de alertas relacionadas.
- Cierre justificado de alertas.
```

Con estas mejoras, el sistema pasaría de una gestión básica de alertas a una aproximación más cercana a la gestión operativa de seguridad.

---

## Sistema de incidentes o casos

En una versión futura, varias alertas podrían agruparse en un incidente o caso.

Actualmente el sistema trabaja con alertas individuales. Sin embargo, en entornos reales, una investigación puede estar formada por varias alertas relacionadas.

Ejemplo:

```text
Alerta 1 → intento fallido SSH
Alerta 2 → múltiples intentos desde el mismo host
Alerta 3 → acceso correcto posterior
        ↓
Incidente: posible compromiso de cuenta
```

Entidades futuras posibles:

```text
incidents
cases
comments
case_alerts
```

Esta funcionalidad permitiría trabajar con una lógica más cercana a la investigación de incidentes.

---

## Mejora del motor de reglas

El motor de reglas actual es funcional, pero básico.

Una línea futura sería ampliar su expresividad.

Mejoras posibles:

```text
- Condiciones AND/OR.
- Reglas compuestas.
- Reglas por secuencia temporal.
- Reglas por frecuencia.
- Reglas por combinación de fuentes.
- Reglas con exclusiones.
- Priorización automática.
- Supresión de falsos positivos.
```

También podría incorporarse una sintaxis más flexible para definir reglas sin tener que modificar código.

Ejemplo conceptual:

```text
source = ssh
AND severity >= 7
AND message contains "failed"
AND count(host) >= 3 in 60 seconds
```

Esto acercaría el sistema a un motor de correlación más realista.

---

## Mejoras en threshold y throttle

El proyecto ya incorpora una base para trabajar con conceptos como `threshold`, `throttle` y `group_key`.

En futuras versiones se podría ampliar esta lógica.

Mejoras posibles:

```text
- Ventanas temporales más flexibles.
- Reglas por usuario, IP o host.
- Reglas combinadas por varios campos.
- Control de duplicados más avanzado.
- Supresión temporal de alertas repetidas.
- Métricas sobre eventos agrupados.
```

Esta línea de mejora permitiría reducir ruido y hacer que las alertas generadas fueran más útiles.

---

## Dashboard avanzado

El frontend actual es una interfaz básica de consulta. Una mejora natural sería desarrollar un dashboard más completo.

Funcionalidades posibles:

```text
- Gráficos de alertas por severidad.
- Alertas por estado.
- Alertas por fuente.
- Evolución temporal de eventos.
- Contadores en tiempo real.
- Panel de reglas activas.
- Vista de hosts con más alertas.
```

Esto permitiría visualizar mejor el estado del sistema y convertir el frontend en una herramienta más útil.

---

## Actualización en tiempo real

Actualmente, el frontend puede requerir actualización manual para mostrar las alertas más recientes.

En una versión futura se podría implementar actualización automática.

Opciones posibles:

```text
- Polling periódico.
- WebSockets.
- Server-Sent Events.
```

El polling sería la opción más sencilla. WebSockets o Server-Sent Events permitirían una actualización más dinámica, aunque añadirían más complejidad.

---

## Gestión de reglas desde el frontend

Actualmente, las reglas se gestionan principalmente desde la API.

Una mejora futura sería permitir crear, editar, activar o desactivar reglas desde la interfaz web.

Funcionalidades posibles:

```text
- Listar reglas.
- Crear nuevas reglas.
- Editar reglas existentes.
- Activar o desactivar reglas.
- Ver estadísticas de activación.
- Probar reglas contra eventos de ejemplo.
```

Esto haría que el frontend no solo sirviera para consultar alertas, sino también para administrar parte del sistema.

---

## Notificaciones externas

Otra mejora posible sería añadir notificaciones cuando se genere una alerta.

Canales posibles:

```text
- Correo electrónico.
- Telegram.
- Discord.
- Slack.
- Webhooks.
```

El flujo sería:

```text
evento → regla → alerta → notificación externa
```

Esta funcionalidad permitiría que las alertas no dependieran únicamente de la consulta manual del usuario.

---

## Endurecimiento de seguridad

Para una versión más avanzada sería necesario mejorar la seguridad del propio sistema.

Mejoras posibles:

```text
- Autenticación.
- Control de permisos.
- HTTPS.
- Gestión segura de secretos.
- Validación más estricta de entradas.
- Limitación de peticiones.
- Logs de auditoría.
- Protección de endpoints administrativos.
```

Estas mejoras serían necesarias si el sistema se desplegara fuera de un entorno local de laboratorio.

---

## Despliegue más realista

Actualmente el proyecto se ejecuta en una máquina virtual local mediante Docker Compose.

Una línea futura sería preparar un despliegue más cercano a producción.

Opciones posibles:

```text
- Servidor VPS.
- Reverse proxy con Nginx o Traefik.
- HTTPS con certificados.
- Separación entre entorno de desarrollo y producción.
- Backups automatizados de PostgreSQL.
- Variables de entorno gestionadas de forma segura.
```

También podría contenerizarse el frontend para que todos los componentes se ejecuten mediante Docker Compose.

---

## Ampliación de pruebas automatizadas

Las pruebas automatizadas actuales validan una parte limitada del backend.

En futuras versiones se podrían ampliar para cubrir más escenarios.

Casos recomendados:

```text
- Ingesta válida.
- Ingesta inválida.
- Evento que genera alerta.
- Evento que no genera alerta.
- Cambio de estado correcto.
- Cambio de estado inválido.
- Filtros de alertas.
- Reglas con threshold.
- Reglas con throttle.
- Eventos sin group_key.
```

También sería útil incorporar pruebas de integración que validen el flujo completo:

```text
crear regla → enviar evento → generar alerta → consultar alerta
```

---

## Integración con herramientas Blue Team

En una versión más avanzada, el proyecto podría integrarse con herramientas habituales del ámbito Blue Team.

Posibilidades:

```text
- Wazuh.
- Suricata.
- Zeek.
- Syslog.
- OpenSearch.
- Grafana.
```

El objetivo no sería sustituir el desarrollo propio, sino usar el SIEM Lab MVP como componente educativo dentro de un laboratorio más amplio.

---

## Priorización de mejoras

No todas las mejoras tienen la misma prioridad.

Una posible evolución ordenada sería:

```text
1. Ampliar pruebas automatizadas.
2. Añadir gestión de reglas desde frontend.
3. Mejorar dashboard visual.
4. Incorporar autenticación.
5. Añadir logs reales de Linux.
6. Desarrollar un agente básico.
7. Mejorar motor de reglas.
8. Añadir notificaciones.
9. Preparar despliegue más realista.
```

Esta priorización permite evolucionar el proyecto sin perder el control del alcance.

---

## Conclusión

El SIEM Lab MVP deja una base funcional sobre la que pueden construirse muchas mejoras.

Las líneas futuras más importantes son la integración con logs reales, la ampliación del motor de reglas, la autenticación, la gestión avanzada de alertas y la mejora del frontend.

Estas ampliaciones permitirían acercar el proyecto a un entorno más realista, pero no eran necesarias para validar la versión actual.

El valor de esta primera versión está en haber construido un flujo completo y funcional que puede servir como base para futuras evoluciones.