#certificacion #network #apuntes
# 📘 CompTIA Network+ — Capítulo 4: Estándares y Escenarios de Ethernet (Edición ampliada)

Este documento unifica las **cuatro sesiones** del Capítulo 4, manteniendo la estructura original y aportando información adicional necesaria para la certificación **CompTIA Network+**.  
> ⚠️ **Palabras clave y nombres de estándares se mantienen en inglés** para coincidir con la terminología del examen.

---

## 📡 Sección 1 — 100BaseT (Fast Ethernet)

### ¿Qué es 100BaseT?
Fast Ethernet representa la evolución de 10 Mbps Ethernet a **100 Mbps**, multiplicando por 10 la velocidad:

- Sustituyó progresivamente los *hubs* por **switches**.
- Introdujo el funcionamiento **Full‑Duplex** de forma generalizada.
- Incorporó variantes en **fibra óptica multimode**.

### Half‑Duplex vs Full‑Duplex

| Half‑Duplex (HDX)                         | Full‑Duplex (FDX)                         |
|-------------------------------------------|-------------------------------------------|
| Solo transmite *o* recibe a la vez.       | Transmisión y recepción simultáneas.      |
| Mayor probabilidad de colisiones.         | Sin colisiones (carriles separados).      |
| Ejemplo: Walkie‑talkie.                   | Ejemplo: Llamada telefónica.              |
| Menor eficiencia de red.                  | Máximo rendimiento del enlace.            |

### Estándares 100Base

| Estándar  | Medio/Cableado | Pares usados | Distancia máx. | Estado |
|-----------|----------------|--------------|----------------|--------|
| 100BaseT4 | Cat3 UTP       | 4 pares      | 100 m          | ⚠️ Obsoleto |
| 100BaseTX | Cat5 UTP       | 2 pares      | 100 m          | ✅ Vigente |
| 100BaseFX | Fibra multimode| 2 fibras     | 2 km           | 💡 Fibra |

> 📝 **Para el examen**: reconocer características y estado (vigente/obsoleto) de cada estándar.

---

## 🚀 Sección 2 — Gigabit Ethernet y 10‑Gigabit Ethernet

### 1. Gigabit Ethernet (1000Base)

| Estándar       | Medio                      | Distancia máx. | Comentario clave                |
|----------------|----------------------------|----------------|---------------------------------|
| 1000Base‑CX    | Twinax (cobre)             | 25 m           | Uso datacenter legacy.          |
| 1000Base‑SX    | Fibra multimode            | ≈ 500 m¹       | “Short eXtended”; campus LAN.   |
| 1000Base‑LX    | Fibra monomode            | 5 km           | “Long”; conexiones MAN.         |
| 1000Base‑T     | Cat5e/Cat6 UTP            | 100 m²        | Estándar dominante en oficinas. |

¹ Depende del tipo de fibra multimode (*OM2 / OM3 / OM4*).  
² 55 m cuando se usa Cat6 sin apantallar.

### 2. 10‑Gigabit Ethernet (10GBase)

#### Cobre UTP

| Estándar  | Cable | Distancia máx. | Observaciones |
|-----------|-------|----------------|---------------|
| 10GBase‑T | Cat6 / Cat6a | 55 m (Cat6) / 100 m (Cat6a) | Autonegociación 1 G/10 G. |

#### Fibra óptica

| Estándar     | Tipo de fibra | λ (nm) | Distancia máx. | Uso típico          |
|--------------|--------------|--------|----------------|---------------------|
| 10GBase‑SR   | Multimode    | 850    | 26‑400 m       | Datacenter intra‑rack |
| 10GBase‑LR   | Monomode     | 1310   | 10 km          | Enlaces metro‑LAN   |
| 10GBase‑ER   | Monomode     | 1550   | 40 km          | Backbones rurales   |

##### Variantes SONET/SDH

- **10GBase‑SW/LW/EW** → mismas especificaciones de SR/LR/ER pero compatibles con infraestructuras **SONET/SDH**.

> 🧠 **Recordatorio Network+**: asociar cada sufijo (SR, LR, ER, T, W) con medio y alcance.

---

## 🔌 Sesión 3 — Transceivers

### Motivación de los transceivers MSA
Los grandes fabricantes acordaron el estándar **MSA (Multi‑Source Agreement)** para crear módulos intercambiables que:

- Permiten adoptar distintos *form factors* (ST, SC, LC, MT‑RJ) sin cambiar el switch.
- Simplifican upgrades de velocidad (ej. de 1 G a 10 G) solo sustituyendo el módulo.

### Tipos de transceivers

| Tipo   | Velocidad típica | Conectores | Notas de examen |
|--------|-----------------|------------|-----------------|
| **GBIC**  | 1 Gbps        | ST / SC    | Primer formato, voluminoso. |
| **SFP**   | 1 Gbps        | LC         | Small Form; prevalente. |
| **SFP+**  | 10 Gbps       | LC         | Igual tamaño que SFP. |
| **QSFP**  | 40 Gbps (QSFP+) / 100 Gbps (QSFP28) | MPO | Alta densidad, data center. |

#### Conexiones Dúplex vs BiDi
- **Dúplex**: 2 fibras (Tx/Rx).
- **BiDi**: 1 fibra; usa láseres de distintos colores en cada dirección.  
  - Reduce fibra requerida.
  - Siempre se compra en **pares complementarios**.

> 📌 **Clave Network+**: diferenciar GBIC, SFP, SFP+, QSFP y entender dúplex vs BiDi.

---

## 🖧 Sesión 4 — Escenarios de Conexión Ethernet

### 1. Bridge Loops
- **Problema**: bucle físico genera *broadcast storm*.  
- **Mitigación**: **Spanning Tree Protocol (STP)** → bloquea puertos redundantes.

### 2. MAC Flooding / L2 DoS
- **Ataque**: sobrecarga tabla CAM.  
- **Defensa**: **Port Security / Storm Control** → limita MACs por puerto, apaga puerto malicioso.

### 3. Speed Mismatch
- Ocurre si un dispositivo no soporta **auto‑negotiation**.  
- Síntomas: sin LED de enlace, velocidades distintas.  
- **Solución**: usar equipo intermedio o reemplazar hardware legacy.

### 4. Trunks Gigabit
- Siempre enlazar switches a su **máxima velocidad común**.  
- Crear *trunk* usando puertos 1 G (o 10 G) antes que 100 Mbps.

### 5. Cable cruzado y puertos Uplink
- Sin **auto‑MDI/MDIX**, se necesita:
  - Puerto uplink + cable directo **o**
  - Puerto normal + cable cruzado.

### 6. Duplex Mismatch en enlaces directos
- Sucede entre dos hosts con cable cruzado.  
- **Solución**: forzar ambos adaptadores a **Half‑Duplex** o habilitar negociación.

#### Tabla resumen

| Escenario          | Protocolo / Función         | Acción recomendada |
|--------------------|-----------------------------|--------------------|
| Bridge Loop        | STP                         | Habilitar STP      |
| MAC Flooding       | Port Security               | Limitar MAC / Shutdown |
| Speed Mismatch     | Auto‑negotiation            | Verificar compat.  |
| Trunk ineficiente  | 802.1Q Trunk / LACP         | Usar puertos G/10G |
| No enlace switches | Auto‑MDI/MDIX               | Uplink o crossover |
| Duplex Mismatch    | Manual Duplex Config.       | Igualar modo       |

---

## 🎯 Conclusión y Consejos de Estudio

- **Memoriza** los sufijos de estándares Ethernet y sus alcances.
- Practica identificar ataques L2 y su mitigación.
- Familiarízate con la **interfaz de configuración** de switches para STP, Port Security y Speed/Duplex.
- Utiliza laboratorios virtuales (GNS3, EVE‑NG) para experimentar con transceivers y topologías con bucles.

---

*Documento elaborado para reforzar tu preparación al examen **CompTIA Network+ (N10‑009)**, centrado exclusivamente en Ethernet según el temario oficial.*
