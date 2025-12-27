

---

# Topología del laboratorio  
## Laboratorio SIEM

---

## Introducción

En este apartado se describe la **topología del laboratorio utilizada para la generación de eventos**, especificando los sistemas implicados y su función dentro del proyecto.

El objetivo de esta topología no es reproducir una infraestructura empresarial completa, sino **proporcionar un entorno controlado y realista** que permita generar eventos representativos para su análisis por parte del Laboratorio SIEM.

---

## Enfoque de la topología

La topología del laboratorio se ha diseñado bajo los siguientes criterios:

- Simplicidad y control del entorno.
- Generación de eventos reales y reproducibles.
- Fácil mantenimiento y comprensión.
- Adecuación al contexto académico.

El laboratorio se compone de un número reducido de sistemas virtualizados, suficientes para simular escenarios básicos de seguridad sin introducir complejidad innecesaria.

---

## Sistemas que componen el laboratorio

### • Sistema Linux

El sistema Linux actúa como una de las principales fuentes de eventos del laboratorio.

Funciones principales:

- Generación de eventos de autenticación.
- Simulación de accesos legítimos y fallidos.
- Registro de acciones administrativas básicas.

Tipos de eventos generados:

- Intentos de acceso por SSH.
- Errores de autenticación.
- Uso de privilegios elevados.

Estos eventos permiten simular escenarios habituales de monitorización en entornos reales.

---

### • Sistema Windows

El sistema Windows se utiliza como segunda fuente de eventos, representando un entorno de estación de trabajo o servidor básico.

Funciones principales:

- Generación de eventos del sistema.
- Simulación de accesos mediante servicios remotos.
- Registro de eventos básicos de seguridad.

Tipos de eventos generados:

- Accesos remotos.
- Errores de autenticación.
- Eventos del sistema operativo.

El uso de un sistema Windows permite diversificar el origen de los eventos y enriquecer el análisis.

---

### • Sistema Laboratorio SIEM

El sistema Laboratorio SIEM constituye el **núcleo del proyecto**, alojando la aplicación desarrollada.

Funciones principales:

- Recepción de eventos desde los sistemas del laboratorio.
- Procesamiento y normalización de los eventos.
- Análisis mediante reglas de detección.
- Generación y gestión de alertas.
- Visualización de la información.

Este sistema se despliega de forma independiente y centraliza toda la lógica del proyecto.

---

## Conectividad y flujo de eventos

La comunicación entre los sistemas sigue un esquema sencillo:

- Los sistemas Linux y Windows generan eventos localmente.
- Los eventos relevantes se envían al Laboratorio SIEM mediante peticiones a la API.
- El Laboratorio SIEM procesa los eventos de forma centralizada.

No se utilizan mecanismos de enrutamiento complejos ni dispositivos de seguridad avanzados, ya que no forman parte del alcance del proyecto.

---

## Escenarios simulados

El laboratorio permite simular, entre otros, los siguientes escenarios:

- Múltiples intentos fallidos de acceso desde un mismo sistema.
- Accesos correctos tras varios fallos consecutivos.
- Acciones administrativas básicas.
- Generación repetida de eventos en intervalos cortos de tiempo.

Estos escenarios son suficientes para validar el funcionamiento del sistema desarrollado.

---

## Limitaciones de la topología

La topología definida presenta las siguientes limitaciones deliberadas:

- Número reducido de sistemas.
- Ausencia de segmentación avanzada de red.
- No integración con infraestructuras empresariales reales.
- Orientación exclusiva a la generación de eventos para el proyecto.

Estas limitaciones garantizan un entorno manejable y alineado con los objetivos académicos.

---

## Rol de la topología en el proyecto

La topología del laboratorio proporciona el **contexto práctico necesario** para validar el funcionamiento del Laboratorio SIEM, sirviendo como fuente de eventos reales y controlados sin ampliar el alcance del proyecto.

---

