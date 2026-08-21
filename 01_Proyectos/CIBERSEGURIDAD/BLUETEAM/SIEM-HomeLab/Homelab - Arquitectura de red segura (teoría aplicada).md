---
tags: [homelab, redes, arquitectura, seguridad, opnsense, vlan]
proyecto: Homelab — Red doméstica dúplex
fuente_teorica: Kasiu Tech — Dominio 2, Módulo 1 (Arquitecturas de red seguras)
fecha: 2026-08-20
estado: revisión de diseño previa a la mudanza
---

# Arquitectura de red segura — teoría aplicada al proyecto

Revisión del diseño de red del homelab contrastado con el marco teórico de arquitecturas seguras (DMZ, segmentación, Zero Trust, tráfico Este-Oeste, NFV).

**Objetivo de la nota:** validar lo que ya está bien decidido, nombrar correctamente lo que se está haciendo, y detectar los huecos **antes** de cerrar el diseño de VLANs y comprar el material restante.

---

## Resumen: qué cambia en el plan

| Punto | Estado previo | Conclusión |
|---|---|---|
| Topología de firewall | 4 patas en VP2420 | ✅ Correcto. Es *Single Firewall* multi-pata. Punto único de fallo **asumido conscientemente** |
| Puerto 4 libre | "para el futuro" | 🔄 Reservarlo como **DMZ** si algún día se expone un servicio |
| VLANs | En diseño | ✅ Segmentación correcta, pero **incompleta**: solo cubre Norte-Sur |
| Tráfico dentro de cada VLAN | No contemplado | ❗ **Hueco principal.** Requiere Port Isolation + Client Isolation |
| Puerto 3 (laboratorio) | Llamado "aislamiento físico" | ✅ Buena decisión, nombre a matizar: **no es air gap** |
| Suricata | Previsto en modo IPS | ⚠️ **Arrancar en modo IDS.** Riesgo de tumbar la casa por falso positivo |
| Gestión de equipos | SSH directo desde Windows | 🔄 Añadir **bastion host** cuando llegue Proxmox |
| Rendimiento Suricata | No evaluado | ⚠️ Evaluar **antes de contratar** el ancho de banda |

---

## 1. DMZ y topología de filtrado

### Qué dice la teoría

Dos topologías posibles:

- **Single Firewall (tres patas):** un dispositivo con al menos 3 interfaces (WAN, LAN, DMZ). Económico, pero **punto único de fallo total** — si el firewall cae, cae todo.
- **Back-to-Back (dual firewall):** dos firewalls en serie. El exterior gestiona Internet↔DMZ, el interior gestiona DMZ↔LAN.

**Regla de oro:** el tráfico nunca debe fluir directamente desde Internet a la LAN. Debe terminar en la DMZ (proxy inverso, servidor web) y ser **ese** quien haga una petición nueva hacia la LAN.

### Cómo se aplica aquí

El VP2420 es un *Single Firewall* con cuatro patas:

| Puerto | Rol actual | Equivalente teórico |
|---|---|---|
| 1 | WAN (operadora) | Interfaz no confiable |
| 2 | Trunk 802.1Q → switch | LAN segmentada |
| 3 | Laboratorio | Zona aislada físicamente |
| 4 | Libre | **Candidato natural a DMZ** |

**El punto único de fallo es real y está asumido.** Un back-to-back exige dos firewalls y no tiene sentido en un homelab doméstico. Lo importante es que sea una decisión consciente y no un descuido: si el VP2420 cae, la casa se queda sin red.

> **Mitigación práctica del punto único de fallo:** el SAI cubre el corte eléctrico. Para el fallo de hardware, tener a mano la configuración de OPNsense exportada (`System → Configuration → Backups`) y guardada en el NAS **y** fuera de la red. Restaurar sobre hardware nuevo es cuestión de minutos si existe el backup; es imposible si no existe.

### Decisión sobre el puerto 4

Ahora mismo no se expone ningún servicio a internet, así que no hace falta DMZ. Pero cuando surja (Nextcloud, Home Assistant remoto, un servidor de juegos), la arquitectura correcta es:

```
Internet → WAN → [DMZ: proxy inverso] → petición nueva → LAN: NAS
```

**Nunca** un port forward directo desde el router hasta el NAS. Eso viola la regla de oro y convierte un fallo del servicio expuesto en acceso a la LAN.

**Acción:** reservar mentalmente el puerto 4 como DMZ y no gastarlo en otra cosa.

---

## 2. Segmentación — y el hueco principal del diseño

### Qué dice la teoría

- **VLANs (802.1Q):** dividen el dominio de broadcast en capa 2. Limitación explícita: *"si un atacante salta a una VLAN, puede atacar a todos los dispositivos de esa misma subred"*.
- **PVLAN (Private VLAN):** técnica de capa 2 para aislar puertos **dentro** de una misma VLAN.
- **Microsegmentación:** políticas a nivel de carga de trabajo individual, no de subred. Se implementa vía SDN o agentes en el host.

### El hueco: tráfico Este-Oeste

Concepto clave del módulo:

| Tipo | Qué es | Quién lo controla |
|---|---|---|
| **Norte-Sur** | Entra o sale de la red (Internet ↔ servidor) | Firewall perimetral |
| **Este-Oeste** | Entre dispositivos **dentro** de la red | ❗ El firewall **no lo ve** |

Y el dato que lo hace urgente: **el 80% del tráfico actual es Este-Oeste.**

**Aplicado a este diseño:** el OPNsense solo ve tráfico que cruza entre VLANs. El tráfico *dentro* de una VLAN lo conmuta el switch en capa 2 y **nunca sube al firewall**.

Consecuencias concretas:

- Una cámara IoT comprometida puede atacar **todas las demás cámaras** sin que el firewall se entere
- Suricata en la interfaz del laboratorio ve tráfico **enrutado**, no el que ocurre entre dos máquinas del propio laboratorio
- Los 3 PCs del estudio, en la misma VLAN, se ven entre sí sin ningún filtro

Las reglas inter-VLAN previstas —correctas y necesarias— **no cubren nada de esto**.

### La solución, con el hardware ya comprado

Sin coste adicional:

**Port Isolation en el SG3218XP-M2** — es la implementación práctica de PVLAN. Puertos que solo pueden hablar con el uplink, nunca entre ellos. Directamente aplicable a la VLAN IoT.

**Client Isolation en los EAP770** — el equivalente inalámbrico, configurable por SSID. Los dispositivos del SSID de invitados solo salen a internet, no se ven entre sí.

### Regla de diseño que se deriva

Al definir cada VLAN, preguntar: **¿sus miembros necesitan hablarse entre ellos?**

| VLAN | ¿Necesitan verse? | Aislamiento |
|---|---|---|
| IoT | No | ✅ Port + Client Isolation |
| Invitados | No | ✅ Client Isolation |
| Hogar | Sí (Chromecast, impresora, NAS) | ❌ Dejar abierta |
| Laboratorio | Sí (es el objetivo del laboratorio) | ❌ Dejar abierta |
| Gestión | No (solo desde bastion) | ✅ Restringir |

---

## 3. Microsegmentación — llega con Proxmox

La teoría la sitúa a nivel de hipervisor o agente. **Proxmox incluye un firewall distribuido a nivel de VM y contenedor**, que es exactamente esa capa.

Permitiría el caso del temario: dos VMs en la misma subred que **no pueden hablarse** salvo regla explícita.

**No es para septiembre.** Pero conviene saberlo al diseñar las VLANs: no hace falta crear diez VLANs hoy intentando compensar una granularidad que llegará por otra vía. Diseñar 5-6 VLANs bien pensadas y dejar el detalle fino para cuando exista el hipervisor.

**Políticas basadas en atributos:** la teoría describe reglas por etiqueta en vez de por IP (*"cualquier servidor con el tag 'Base de Datos' solo recibe tráfico del tag 'App Server' por el puerto 3306"*). Proxmox soporta *security groups* que se acercan a este modelo. Interesante para la fase de laboratorio.

---

## 4. Zero Trust — dónde está realmente este proyecto

### Los tres componentes (NIST SP 800-207)

| Componente | Función | En este setup |
|---|---|---|
| **PE** (Policy Engine) | Decide según puntuación de riesgo | ❌ No existe |
| **PA** (Policy Administrator) | Ejecuta la decisión, genera tokens | ❌ No existe |
| **PEP** (Policy Enforcement Point) | Donde se corta o permite el paso | ✅ OPNsense y puertos del switch |

**Hay músculo, no cerebro. Y está bien.** Un ZTA completo no es realista ni proporcionado en un homelab. Lo importante es no fingir que sí lo es.

### Lo que sí se está aplicando de la mentalidad

**Default Deny** desde la VLAN de laboratorio hacia el resto. Esto es el principio central del dominio aplicado literalmente:

> *"Si no hay una regla específica que diga que ese tráfico está permitido, el sistema debe destruirlo. Es mejor que alguien te llame porque algo no funciona a que te llamen porque te han robado los datos."*

### Un paso realista hacia Identidad + Dispositivo + Contexto

El Omada soporta **802.1X** en los puertos del switch. Convierte el acceso de *"estás enchufado, luego confío"* a *"demuestra quién eres"*. Requiere un servidor RADIUS (viable en el NAS o en Proxmox).

Es la diferencia entre seguridad de perímetro y seguridad de identidad, y es probablemente el proyecto de aprendizaje más rentable de toda la fase 2.

> ⚠️ **El filtrado por MAC no cuenta** como control de identidad. Una MAC se falsifica en un comando. Es capa cosmética, no control.

---

## 5. Aislamiento avanzado

### El puerto 3 no es air gap

La teoría define **air gapping** como aislamiento físico total: la red no tiene conexión física con el exterior (centrales nucleares, sistemas militares).

El puerto 3 **sí enruta** a través del firewall. Lo correcto es llamarlo **segmentación física**: más fuerte que solo VLAN, pero no aislamiento total.

**El motivo original de la decisión era correcto:** separar el laboratorio en una interfaz física elimina la clase entera de ataques de **VLAN hopping** (doble etiquetado 802.1Q, switch spoofing), porque no hay trunk que atacar. Buena decisión de diseño; solo conviene el nombre preciso.

### Bastion host — la pieza que falta

La teoría lo define como un servidor endurecido que es **el único punto de entrada** para administrar el resto. Se accede por SSH/RDP y desde ahí se salta a los equipos críticos.

**Situación actual:** administración por SSH directo desde el PC Windows a cada equipo. Eso es exactamente lo que un bastion evita — el PC de uso diario (navegación, correo, descargas) tiene acceso administrativo a la infraestructura.

**Diseño objetivo:**

```
PC de trabajo → [Bastion: VM endurecida] → OPNsense / Switch / APs / NAS
                       ↑
              único origen permitido
              en la VLAN de gestión
```

La VLAN de gestión acepta conexiones **solo** desde ese host. Con Proxmox puede ser una VM mínima con SSH por clave y sin contraseña.

Beneficio doble: reduce superficie de ataque y centraliza el registro de quién administró qué y cuándo.

### Honeypot

Opcional. Un contenedor en la VLAN de laboratorio que parezca vulnerable genera tráfico real de ataque para practicar análisis, sin riesgo para el resto. Fase posterior, valor didáctico alto.

---

## 6. NFV — ya está implementado

La teoría: sustituir hardware dedicado (firewalls físicos, IPS físicos) por software.

**Suricata dentro de OPNsense es exactamente eso.** No es una limitación presupuestaria ni un apaño: es el modelo que el propio módulo describe como el estándar moderno. Un IPS físico dedicado sería, hoy, la opción anticuada.

Con Proxmox se abre además el **service chaining**: encadenar funciones de seguridad de forma lógica sin tocar un cable.

---

## Avisos técnicos sobre el plan de IDS/IPS

### 1. Arrancar Suricata en modo IDS, no IPS

Es literalmente una pregunta del examen del dominio: la principal desventaja de un IPS *in-line* es que **si falla o genera un falso positivo crítico, tumba el servicio**.

Traducido a esta casa: internet caído entero por un falso positivo, a las once de la noche, sin nadie que sepa por qué.

**Plan recomendado:**

1. Suricata en **modo IDS** (solo alerta) durante 2-4 semanas
2. Revisar qué alertas genera y cuáles son ruido
3. Ajustar el conjunto de reglas
4. Solo entonces pasar a **IPS** (bloqueo), con reglas ya validadas

### 2. El J6412 no va a inspeccionar a 2.5 Gbps

Suricata es intensivo en CPU. Un Celeron J6412 de 4 núcleos con inspección profunda activa rinde **bastante por debajo del gigabit**, dependiendo del conjunto de reglas.

**Implicación directa en una decisión pendiente:** si se contrata fibra de 1 Gbps o menos, no hay conflicto. Si se contrata simétrica de varios gigas, habrá que elegir entre velocidad máxima e inspección de tráfico.

**Conviene evaluarlo antes de firmar el contrato de la operadora**, no después.

### 3. Sobre dónde aplicar la inspección

El plan actual (WAN + VLAN de laboratorio) es razonable, con un matiz: en la interfaz de laboratorio Suricata verá **solo tráfico enrutado hacia otras VLANs**, no el movimiento lateral dentro del propio laboratorio. Para eso hace falta la capa de aislamiento del punto 2, o capturar tráfico con un puerto SPAN del switch.

---

## Acciones concretas

### Antes de cerrar el diseño de VLANs

- [ ] Definir para cada VLAN si sus miembros necesitan verse entre sí
- [ ] Planificar **Port Isolation** en los puertos de la VLAN IoT
- [ ] Planificar **Client Isolation** en los SSID de IoT e invitados
- [ ] Reservar el puerto 4 del VP2420 como futura DMZ
- [ ] Definir una VLAN de gestión separada de la VLAN de hogar

### Antes de contratar operadora

- [ ] Evaluar el rendimiento realista de Suricata frente al ancho de banda contratado

### En el despliegue inicial

- [ ] Suricata en modo **IDS**, no IPS
- [ ] Exportar la configuración de OPNsense al NAS **y** a una copia externa
- [ ] Documentar el esquema de VLANs y las reglas antes de aplicarlas

### Fase posterior (con Proxmox)

- [ ] Bastion host para administración de infraestructura
- [ ] Evaluar firewall distribuido de Proxmox (microsegmentación)
- [ ] Evaluar 802.1X con RADIUS en los puertos del switch
- [ ] Suricata a modo IPS con reglas ya validadas

---

## Terminología correcta para el proyecto

Para usar los términos con precisión en documentación y conversaciones con instaladores:

| Se estaba diciendo | Término correcto | Por qué |
|---|---|---|
| "Aislamiento físico" (puerto 3) | **Segmentación física** | Sigue enrutando por el firewall; no es air gap |
| "IPS/IDS" como capa | **NFV** (función virtualizada) | No es hardware dedicado |
| "Reglas inter-VLAN" | Control **Norte-Sur** | Falta explicitar el Este-Oeste |
| "VLAN de laboratorio aislada" | VLAN con **Default Deny** | El aislamiento lo da la política, no la VLAN |

---

## Pendientes actualizados del proyecto

Sustituye el punto 3 de la lista original ("diseño completo de VLANs y reglas de firewall inter-VLAN"), que mezclaba dos problemas distintos:

**3a. Control Norte-Sur** — reglas de OPNsense entre VLANs y hacia internet. Ya estaba previsto.

**3b. Control Este-Oeste** — Port Isolation en el switch y Client Isolation en los AP. **No estaba en la lista** y cubre, según la teoría, el 80% del tráfico.
