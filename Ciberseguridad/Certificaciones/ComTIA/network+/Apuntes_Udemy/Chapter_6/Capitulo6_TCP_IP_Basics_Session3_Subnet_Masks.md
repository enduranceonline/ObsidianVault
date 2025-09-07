# Capítulo 5 — Installing Physical Network  
## Session 9: Troubleshooting Cabling – PART 3 (Signal Integrity & Cable Selection)

> **Idioma:** Español con palabras clave en **inglés** tal como los exige el examen **CompTIA Network+**.

---

## 1. Importancia del cableado en el rendimiento de red

La fiabilidad de una red Ethernet cableada depende tanto del **hardware/software** como de la pericia del técnico para **diagnosticar** y **solucionar** problemas de cableado.  
Escoger el **cable wrong** o ignorar el mantenimiento provoca:

- Pérdida de rendimiento (Throughput).  
- Costes adicionales de reemplazo.  
- Paradas de servicio críticas.

---

## 2. Selección correcta de cables

### 2.1 Fiber‑optic

| Tipo             | Distancia máx. | Velocidad típica | Categorías | Uso recomendado |
|------------------|----------------|------------------|------------|-----------------|
| **Single‑mode**  | 10–200 km      | 1–10 Gbps        | **OS1** (indoor) / **OS2** (outdoor) | Backbone WAN, enlaces campus |
| **Multi‑mode**   | 100–260 m      | 10–100 Gbps      | **OM1–OM5** | LAN, data center interconnect |

> ⚠️ Elegir el tipo incorrecto (ej. OM1 para 40 Gb) limita alcance y velocidad.

### 2.2 Copper (Twisted Pair)

| Categoría | Velocidad máx. | Shielding option | Nota |
|-----------|---------------|------------------|------|
| **Cat5e** | 1 Gbps        | UTP / STP        | Obsoleto para 10 Gb |
| **Cat6**  | 10 Gbps (≤ 55 m) | UTP / STP    | Mejor para LAN 10 G |
| **Cat6a** | 10 Gbps (100 m) | F/UTP          | Recomendado entornos EMI |

**Shielded Twisted Pair** (STP) es esencial en ambientes con alta **EMI**: data centers, equipos médicos, líneas de alta tensión.

---

## 3. Signal Degradation

### 3.1 Crosstalk

| Tipo de diafonía | Descripción | Herramienta de prueba |
|------------------|-------------|-----------------------|
| **NEXT** (Near‑End) | Interferencia captada en el mismo extremo transmisor. | Cable certifier (NEXT dB) |
| **FEXT** (Far‑End)  | Interferencia detectada en el extremo receptor.       | Certifier (FEXT dB) |
| **Alien Crosstalk (AXT)** | Interferencia entre hilos de **cables distintos**. | Certifier multi‑cable |

**Mitigación**: mantener twists, usar separadores y STP, seguir radio de curvatura.

### 3.2 Attenuation

- **Definición:** Pérdida gradual de potencia de señal a lo largo del cable.  
- **Causa:** Resistencia, fricción de electrones (cobre) o dispersión modal (fibra).  
- **Reglas:** ≤ 100 m para **UTP**; obedecer tablas OS/OM para fibra.

---

## 4. Herramientas de diagnóstico avanzado

| Herramienta            | Función                                  |
|------------------------|------------------------------------------|
| **Cable tester básico**| Wiremap & Continuity.                    |
| **Cable certifier**    | NEXT, RL, PSNEXT, Delay‑Skew.           |
| **TDR / OTDR**         | Distancia a la falla, opens/shorts.     |
| **Spectrum analyzer**  | Visualiza frecuencias y EMI.            |

---

## 5. Fallos de terminación

| Error común             | Impacto                      | Solución                            |
|-------------------------|------------------------------|-------------------------------------|
| Wires TX/RX invertidos  | Sin enlace o duplex mismatch | Re‑terminar con pin‑out correcto.   |
| Untwist > 13 mm         | Aumenta NEXT, baja SNR       | Mantener twist cerca del IDC.       |
| Conector inadecuado     | Intermitencias, alta RL      | Usar jack/plug Cat apropiado.       |

---

## 6. Procedimiento de troubleshooting integral

1. **Identify**: revisar síntomas, velocidad y alcance requeridos.  
2. **Isolate**: usar Cable tester para Wiremap → Continuity.  
3. **Measure**: ejecutar **TDR** para longitud/cortes; certifier para NEXT/RL.  
4. **Rectify**: reemplazar cable wrong o re‑terminar punchdowns.  
5. **Verify**: re‑certificar y documentar en sistema **TIA‑606**.

---

## 7. Tips para el examen Network+

1. **Single‑mode** ≈ largas distancias; **Multi‑mode** ≈ corto alcance alta velocidad.  
2. **OM3/OM4/OM5** soportan 40/100 Gbps; **OM1/OM2** limitados.  
3. **Attenuation** aumenta con distancia → respeta 100 m para UTP.  
4. **NEXT vs FEXT vs AXT**: conoce ubicación y causa.  
5. Shielding (STP) se implementa en ambientes **EMI** intensos.  

---

*Fin de la Session 9 – PART 3. Ahora posees una visión completa de diagnóstico, selección y mantenimiento de cables para CompTIA Network+.*
