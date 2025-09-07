#certificacion #network #apuntes
# Capítulo 6 — TCP/IP Basics  
## Session 1: Introduction to IP Addressing and Binary

> **Idioma:** Español con palabras clave (**IP address, octet, binary, dotted‑decimal**) en **inglés** según el examen **CompTIA Network+**.

---

## 1. ¿Qué es una IP address?

Una **IP address** versión 4 se muestra normalmente como **dotted‑decimal notation**:

```
192.168.10.25
```

- Consta de **4 octets** (octetos) separados por puntos.  
- Cada octet representa **8 bits**, para un total de **32 bits**.  
- Los puntos son solo *separadores* para humanos; dentro del equipo la dirección es una cadena continua de **1 y 0**.

> Ejemplo binario:  
> `11000000 10101000 00001010 00011001` → 192.168.10.25

---

## 2. Estructura interna: 32 bits en 4 octets

| Octet | Bits (posición) | Rango decimal (0‑255) |
|-------|-----------------|-----------------------|
| 1     | 31‑24           | 0‑255                |
| 2     | 23‑16           | 0‑255                |
| 3     | 15‑8            | 0‑255                |
| 4     | 7‑0             | 0‑255                |

Dividir los 32 bits en grupos de 8 facilita la conversión entre **binary** y **decimal**.

---

## 3. Conversión Binary → Decimal (octet)

### Tabla de potencias de 2

| Bit | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|-----|-----|----|----|----|---|---|---|---|

### Pasos

1. Escribe los **8 bits** debajo de la tabla.  
2. Suma los valores donde haya **1**.  
3. Resultado = valor decimal del octet.

#### Ejemplo  
`11000101`

```
1 1 0 0 0 1 0 1
128+64+4+1 = 197
```

---

## 4. Conversión Decimal → Binary

1. Coloca el valor decimal bajo la columna 128.  
2. Si el número ≥ potencia, escribe **1** y réstala; si no, **0**.  
3. Continúa hasta la columna 1.

#### Ejemplo  
Decimal = **171**

```
128 ✔ → resto 43
64  ✘
32  ✔ → resto 11
16  ✘
8   ✔ → resto 3
4   ✘
2   ✔ → resto 1
1   ✔ → resto 0
```
Resultado: **10101011**

---

## 5. Valores binarios “rápidos” a memorizar

| Binario            | Decimal |
|--------------------|---------|
| 00000000           | 0       |
| 11111111           | 255     |
| 10000000           | 128     |
| 00000001           | 1       |

Conocer estos atajos agiliza subnetting y troubleshooting en el examen.

---

## 6. Herramientas prácticas

- **Calculadora de Windows** (modo Programmer) convierte binario ↔ decimal.  
- Apps móviles para IPv4/IPv6 calc.  
- En la prueba **Network+**, debes dominar la lógica manual aunque uses calculadoras en el trabajo real.

---

## 7. Resumen para el examen

1. Una IPv4 tiene **32 bits** distribuidos en **4 octets**.  
2. **Dotted‑decimal** es solo formato humano; internamente es binario puro.  
3. Recuerda tabla `128 64 32 16 8 4 2 1` para convertir.  
4. Conviértete en experto: práctica de binario ↔ decimal agiliza subnetting en sesiones futuras.

---

*Fin de la Session 1. Próximamente: clases de IP address y subnet masks.*
