

---

# Entorno de despliegue del laboratorio  
## Laboratorio SIEM

---

## Introducción

En este apartado se describe la **disposición del entorno de despliegue** sobre el que se ejecuta el Laboratorio SIEM, detallando la organización de las máquinas virtuales, su rol dentro del sistema y los criterios técnicos básicos de su configuración.

Este apartado forma parte de la **fase de diseño** del proyecto y tiene como objetivo dejar claramente definido el entorno de trabajo antes de abordar la implementación, sin entrar todavía en configuraciones específicas ni parámetros concretos.

---

## Enfoque del entorno de despliegue

El laboratorio se ejecuta sobre un entorno de **virtualización local**, que permite desplegar y gestionar múltiples máquinas virtuales de forma aislada sobre un único equipo anfitrión.

Este enfoque permite simular un entorno realista de seguridad, separando el núcleo del sistema SIEM de las fuentes de eventos, al tiempo que se mantiene un entorno controlado, reproducible y adecuado al contexto académico del proyecto.

La topología del laboratorio se ha diseñado para:
- Minimizar la complejidad innecesaria.
- Mantener una separación clara de responsabilidades.
- Facilitar la comprensión del flujo de eventos.
- Permitir una futura ampliación sin rediseñar la estructura base.

---
## Máquinas virtuales del laboratorio

El entorno de despliegue del laboratorio se compone de **tres máquinas virtuales**, desplegadas sobre un único equipo anfitrión y conectadas mediante una red interna común. Cada máquina virtual cumple un rol específico dentro del laboratorio y ha sido configurada siguiendo criterios de simplicidad, aislamiento y control.

---

### VM 1 — Nodo central del SIEM

Esta máquina virtual aloja el **núcleo funcional del Laboratorio SIEM** y concentra los servicios desarrollados como parte del proyecto.

Datos de interés:
>nombre: `siem-lab` 
>usuario: `endurance` 
>contraseña: `siemlab123`
>Interfaces:
>	- `ens33 → 192.168.52.x` → **vmnet8 (NAT)** → Internet OK
>	- `ens36 → 172.16.136.x` → **vmnet1 (Host-Only)** → red interna
>Gateway: `no externo`

Características de despliegue:
- Sistema operativo Linux de propósito general.
- Nodo único que centraliza la lógica del sistema.
- Servicios ejecutados de forma local o aislada cuando resulta conveniente.

Criterios de configuración:
- Capacidad suficiente para ejecutar los servicios backend y la base de datos del laboratorio.
- Acceso exclusivo desde la red interna del laboratorio.
- Exposición controlada de servicios únicamente a las fuentes de eventos y a la interfaz web.

Este nodo actúa como punto central de recepción, procesamiento y almacenamiento de la información, evitando dependencias externas y simplificando la gestión del entorno.

---

### VM 2 — Fuente de eventos (Linux)

Esta máquina virtual representa un sistema Linux configurado como **fuente de eventos** dentro del laboratorio.

Características de despliegue:
- Sistema operativo Linux orientado a la generación de eventos.
- Configuración mínima, sin servicios innecesarios.
- Rol exclusivo de generación y envío de eventos.

Criterios de configuración:
- Conectividad limitada a la red interna del laboratorio.
- Capacidad para generar eventos de forma controlada y reproducible.
- Comunicación unidireccional hacia el nodo central del SIEM.

Esta VM no almacena información de forma persistente ni ejecuta componentes del sistema SIEM, lo que permite aislar claramente su función dentro del laboratorio.

---

### VM 3 — Fuente de eventos (Windows)

Esta máquina virtual representa un sistema Windows que actúa como **segunda fuente de eventos** del laboratorio.

Características de despliegue:
- Sistema operativo Windows configurado para la generación de eventos.
- Entorno representativo de una estación de trabajo o sistema básico.
- Rol exclusivo de generación y envío de eventos.

Criterios de configuración:
- Conectividad restringida a la red interna del laboratorio.
- Generación de eventos propios del sistema operativo Windows.
- Envío de eventos al nodo central sin acceso a otros componentes del sistema.

La inclusión de esta máquina virtual permite diversificar el origen de los eventos y validar el funcionamiento del sistema ante fuentes heterogéneas.

---

## Red del laboratorio y comunicación entre nodos

Las máquinas virtuales del laboratorio se interconectan mediante una **red interna proporcionada por la plataforma de virtualización**, diseñada para facilitar la comunicación entre los nodos manteniendo el aislamiento del entorno.

Características técnicas de la red:
- Red virtual privada, no accesible directamente desde el exterior.
- Conectividad directa entre las máquinas virtuales del laboratorio.
- Dirección del tráfico orientada principalmente hacia el nodo central del SIEM.

Criterios de comunicación:
- Las fuentes de eventos establecen comunicación únicamente con el nodo central.
- No existe comunicación directa entre las fuentes de eventos.
- No se permite acceso directo a la base de datos desde las fuentes externas.

La comunicación se realiza exclusivamente a través de la **API de ingesta**, que actúa como punto de control y validación del flujo de información. Este diseño refuerza la trazabilidad de los eventos y evita accesos no controlados a los componentes internos del sistema.

No se incorporan mecanismos avanzados de segmentación ni dispositivos de red adicionales, ya que el objetivo del laboratorio es mantener un entorno comprensible y alineado con el alcance académico del proyecto.

---

## Justificación del diseño del entorno

La configuración del entorno de despliegue responde a los siguientes criterios:

- Separación clara de responsabilidades entre sistemas.
- Aislamiento entre el núcleo del SIEM y las fuentes de eventos.
- Facilidad de mantenimiento y depuración.
- Reproducibilidad del entorno de laboratorio.
- Adecuación al alcance y objetivos académicos del proyecto.

Este diseño permite validar el funcionamiento del Laboratorio SIEM en un entorno controlado, manteniendo una arquitectura coherente y preparada para futuras ampliaciones sin comprometer la estructura base del sistema.
