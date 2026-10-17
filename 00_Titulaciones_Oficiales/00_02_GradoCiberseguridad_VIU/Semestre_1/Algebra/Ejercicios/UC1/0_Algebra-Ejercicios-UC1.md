---
asignatura: Álgebra
tipo: ejercicios
tema: 1
apartado: "UC1"
sesiones: [1]
estado: adelantado
material: "[[ejs_tema1.pdf]]"
solucionario: "[[ejs_tema1_sol.pdf]]"
---

# Ejercicios UC1 — Guía y hoja de ruta

Hoja de ejercicios: [[ejs_tema1.pdf]]. Solucionario: [[ejs_tema1_sol.pdf]] (solo resultados, sin desarrollo).

Leyenda:
- ✅ **Se puede hacer ya**: la teoría está en [[Algebra-clase01]] y [[Algebra-Tema-1.1-Conjuntos]].
- 🟡 **Teoría adelantada**: no se ha visto en clase, pero la nota correspondiente permite empezar. Se completará cuando el profesor lo explique.

## Qué cubre la hoja
La hoja UC1 abarca más que la Sesión 1: conjuntos (1.1), relaciones (1.2), aplicaciones (1.3) y combinatoria (Tema 2 del libro). Por tanto, de lo que falta por dar en el Tema 1:

| Bloque | Apartado | Nota | Estado |
| --- | --- | --- | --- |
| Conjuntos, operaciones y partes | 1.1 | [[Algebra-Tema-1.1-Conjuntos]] | ✅ visto en Sesión 1 |
| Producto cartesiano, relaciones, equivalencia | 1.2 | [[Algebra-Tema-1.2-Relaciones]] | 🟡 adelantado |
| Aplicaciones, composición, inversa, numerabilidad | 1.3 | [[Algebra-Tema-1.3-Aplicaciones]] | 🟡 adelantado |
| Principios de cardinalidad y fórmulas de conteo | Tema 2 | [[Algebra-Tema-2-Combinatoria]] | 🟡 adelantado |

## Ejercicios recomendados

- [ ] **1.** $A \cap B$, $A \cup B$, $A \setminus B$, $B \setminus A$ en cinco casos (conjuntos finitos e intervalos) — ✅ [[Algebra-Tema-1.1-Conjuntos]] (secciones 1.1.2 y "Notación de intervalos")
- [ ] **2.** Producto cartesiano $A \times B$ — 🟡 [[Algebra-Tema-1.2-Relaciones]] (producto cartesiano). Es inmediato con la definición.
- [ ] **3.** $\mathcal{P}(A)$ de un conjunto de 4 elementos — ✅ [[Algebra-Tema-1.1-Conjuntos]] (1.1.3) y [[Algebra-Ejercicios-Conjuntos]] (Partes 1)
- [ ] **4.** ¿Es aplicación? ¿Inyectiva, sobreyectiva, biyectiva? ¿Inversa? (cuatro apartados) — 🟡 [[Algebra-Tema-1.3-Aplicaciones]] (1.3.1 y 1.3.3)
- [ ] **5.** Composición $g \circ f$ con conjuntos finitos — 🟡 [[Algebra-Tema-1.3-Aplicaciones]] (1.3.2)
- [ ] **6–11.** Problemas de conteo — 🟡 [[Algebra-Tema-2-Combinatoria]] (2.2, usa la guía de "¿orden? ¿repetición? ¿todos?")

## Ejercicios de ampliación

- [ ] **1.** Demostrar las propiedades asociativa, conmutativa y distributiva (a–f) — ✅ método de doble inclusión o de equivalencias lógicas, en [[Algebra-Tema-1.1-Conjuntos]]
- [ ] **2.** Demostrar las leyes de De Morgan con un conjunto universal $X$ — ✅ igual que el anterior; ver también [[Algebra-Ejercicios-Conjuntos]] (Ampliación 3 y 4)
- [ ] **3.** Operaciones con conjuntos infinitos de enteros: pares/impares y múltiplos de 2 y de 3 — ✅ [[Algebra-Tema-1.1-Conjuntos]] ("Conjuntos de múltiplos"). Recuerda que $\mathbb{N}$ empieza en 1.
- [ ] **4.** ¿Es relación de equivalencia? ¿Qué clases tiene? (cuatro apartados) — 🟡 [[Algebra-Tema-1.2-Relaciones]] (1.2.2)
- [ ] **5.** Aplicaciones con funciones reales: inyectividad, sobreyectividad e inversa — 🟡 [[Algebra-Tema-1.3-Aplicaciones]] (1.3.1 y 1.3.3). Fíjate bien en el dominio y el codominio de cada apartado.
- [ ] **6.** Composición de funciones reales en ambos órdenes y comparación — 🟡 [[Algebra-Tema-1.3-Aplicaciones]] (1.3.2)
- [ ] **7.** Demostrar que tres conjuntos infinitos son numerables — 🟡 [[Algebra-Tema-1.3-Aplicaciones]] (1.3.4)
- [ ] **8–9.** Conteo aplicado a archivos y bytes — 🟡 [[Algebra-Tema-2-Combinatoria]]
- [ ] **10.** Subconjuntos de $k$ elementos de un conjunto de $n$ y suma de los números combinatorios — 🟡 [[Algebra-Tema-2-Combinatoria]] (2.2.3 y propiedades), conectado con $|\mathcal{P}(A)| = 2^n$ de la Sesión 1

## Orden de trabajo sugerido
1. **Ya**: recomendados 1 y 3, y ampliación 1, 2 y 3. Todo se resuelve con lo visto en la Sesión 1 más la nota de intervalos.
2. **Después**: recomendados 2, 4 y 5, y ampliación 4 a 7, leyendo antes 1.2 y 1.3.
3. **Al final**: recomendados 6–11 y ampliación 8–10, con la guía de combinatoria.

## Erratas detectadas
> [!warning] Solucionario
> - **Recomendado 1b:** el solucionario da $A \setminus B = [1, 0[$, que no es un intervalo válido. Con $A = [-1, 1]$ y $B = [0, 2]$ lo correcto empieza en $-1$.
> - **Ampliación 7b:** el solucionario da $f(n) = n - 4$, pero con $\mathbb{N} = \{1, 2, \ldots\}$ eso da $-3$ para $n = 1$, no $5$. La biyección correcta suma, no resta.
>
> En ambos casos, dilo a la tutoría o al profesor si queréis confirmarlo.

> [!warning] Libro
> - **2.1.1 (adición):** el libro escribe $A \cap B \neq \emptyset$; debe ser $A \cap B = \emptyset$.
> - **2.2.2 (permutaciones con repetición):** el ejemplo $112223$ da $60$, no $120$.
> - **1.2.2 (transitiva):** al sumar los dos múltiplos de 3 se obtiene $3m' + 3m$ (el libro escribe $3m' - 3m$).

## Enlaces
- [[Algebra-clase01]]
- [[Algebra-Tema-1.1-Conjuntos]]
- [[Algebra-Tema-1.2-Relaciones]]
- [[Algebra-Tema-1.3-Aplicaciones]]
- [[Algebra-Tema-2-Combinatoria]]
- [[Algebra-Ejercicios-Conjuntos]]
