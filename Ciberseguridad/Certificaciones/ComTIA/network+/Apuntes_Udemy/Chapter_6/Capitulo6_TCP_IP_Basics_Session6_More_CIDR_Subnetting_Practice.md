# Capítulo 6 — TCP/IP Basics  
## Session 6: More **CIDR Subnetting** Practice

> **Idioma:** Español con palabras clave en **inglés** (CIDR, /n, subnet mask) para el examen **CompTIA Network+**.

---

## 1. Refresco rápido de tamaños

| CIDR | Hosts (usable) | Mask (dotted)      |
|------|----------------|--------------------|
| /24  | 254            | 255.255.255.0      |
| /25  | 126            | 255.255.255.128    |
| /26  | 62             | 255.255.255.192    |
| /27  | 30             | 255.255.255.224    |
| /28  | 14             | 255.255.255.240    |
| /29  | 6              | 255.255.255.248    |
| /30  | 2              | 255.255.255.252    |

> Fórmula: **Hosts = 2^(32‑n) − 2**

---

## 2. Escenario 1 – Servidor de juegos (4 hosts)

**Requisitos:** 4 servidores visibles en Internet (IP estáticas)  
**Proveedor:** Comcast Business ofrece bloques /30, /29, /28…

### 2.1 Selección de máscara  
Necesitamos ≥ 4 hosts → /29 provee **6 usable**. (/30 solo ofrece 2)

### 2.2 Asignación de bloque /29  
Supongamos que el ISP entrega **198.51.100.248/29**

| Tipo          | Dirección          |
|---------------|--------------------|
| Network ID    | 198.51.100.248     |
| Usable hosts  | .249 ‑ .254        |
| Broadcast     | 198.51.100.255     |
| Gateway (ISP) | 198.51.100.249     |

Quedan **5 IPs**; usamos .250‑.254 para nuestros 4 servers y 1 spare.

---

## 3. Escenario 2 – Oficina requiere 8 IPs

**Meta:** mínimo 8 direcciones fijas para servicios varios.  
**Bloque asignado por ISP:** 199.44.6.80/28 (ejemplo real en texto)

### 3.1 Desglose /28

```
Mask /28 = 255.255.255.240
Incremento = 16
```

| Subred | Rango usable                | Broadcast |
|--------|-----------------------------|-----------|
| .80/28 | 199.44.6.81‑199.44.6.94     | .95       |

- **ISP Gateway:** 199.44.6.81 (reservado)  
- Usables restantes: **.82‑.94** → 13 direcciones (cumple 8 IPs requeridas).

---

## 4. Procedimiento general de subnetting

1. **Hosts needed → elegir /n** usando tabla.  
2. **Calcular incremento** = 256 − último valor mask.  
3. **Listar subredes**: empezar por Network ID, sumar incremento.  
4. Reservar primera usable para **gateway** si el ISP lo requiere.  
5. Asignar hosts; documentar en hoja Subnet Plan.

---

## 5. Ejercicios propuestos

1. Diseña un bloque para 45 hosts:  
   - ¿Qué /n usarías?  
   - Muestra Network, Broadcast y rango usable.

2. Tu ISP te da **203.0.113.128/27**.  
   - ¿Cuántos hosts puedes usar?  
   - ¿Cuál es la dirección broadcast?

> Soluciones al final del capítulo.

---

## 6. Tips para el examen Network+

1. Memoriza tabla /24‑/30.  
2. Gateway suele ser **primer usable** o **último usable**.  
3. Siempre resta 2 (Network ID y Broadcast).  
4. /30 se usa en enlaces punto‑a‑punto (solo 2 hosts).  
5. Verifica que el bloque no se superponga con otros de tu red.

---

*Fin de la Session 6. Continúa practicando para dominar CIDR y VLSM.*