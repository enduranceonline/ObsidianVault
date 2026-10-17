---
asignatura: Álgebra
tipo: clase
sesion: 1
fecha: 2026-10-15
profesor: David Zorío Ventura
material: "[[04GCIB - Sesión 1 - Conjuntos.pdf]]"
---

# Clase 01 — Teoría de conjuntos

## Qué se vio
- Presentación de la asignatura: 4 temas.
  - T1 (S1-S4): marco matemático (conjuntos, relaciones y aplicaciones).
  - T2 (S5-S6): matemática discreta, con el objetivo de poder explicar el sistema criptográfico RSA.
  - T3 (S7-S9): sistemas de ecuaciones lineales (álgebra lineal, explicada de la forma más general posible).
  - T4 (S10-S12): espacios vectoriales, aplicaciones lineales y diagonalización de matrices.
- Teoría de conjuntos: mismas definiciones que en EIO → [[Algebra-Tema-1.1-Conjuntos]]
  - **Inclusión** $A \subseteq B$: todo elemento $x$ de $A$ es también elemento de $B$. El conjunto vacío está incluido en cualquier conjunto. Ejemplos 1 y 2 representados en diagramas de Venn.
  - Pregunta al profesor: la **inclusión propia** ($A \subseteq B$ y $A \neq B$) existe, pero no se usará en la asignatura.
  - **Igualdad**: $A = B$ si $A \subseteq B$ y $B \subseteq A$.
  - Ejemplo de igualdad: $\mathbb{Q} = D$ (racionales = decimales periódicos). Hay que probar las dos inclusiones.
    - $D \subseteq \mathbb{Q}$: se corre la coma hasta después del primer periodo y hasta justo antes de él, y se restan. Con $x = 0{,}7537\ldots$ sale $(10^4 - 10^2)\,x = 7462$, luego $x = \frac{7462}{9900}$.
    - $\mathbb{Q} \subseteq D$: al dividir $a/b$ los restos $r_i$ están entre $0$ y $b-1$, así que alguno se repite y las cifras se repiten. Ejemplo: $3/7$, con restos entre $0$ y $6$.
  - **Operaciones**: intersección, unión y complementario o diferencia, cada una con su fórmula y su diagrama de Venn.
    - Si $A \cap B = \emptyset$ son **disjuntos**. Si $A \subseteq B$, entonces $A \cap B = A$.
    - Complementario o diferencia: $A \setminus B = \{x \mid x \in A \wedge x \notin B\}$. No es simétrica. Si $A \subseteq B$, entonces $A \setminus B = \emptyset$.
    - "Complementario" se usa cuando hay un conjunto universal $U$: $A^c = U \setminus A$. En esta asignatura se usan ambos nombres.
  - **Partes de un conjunto** $\mathcal{P}(A)$: se lista $\emptyset$, luego los de 1 elemento, los de 2, etc., y al final el propio $A$. Si $|A| = n$, entonces $|\mathcal{P}(A)| = 2^n$. Esto introduce la combinatoria.
- Ejercicios de clase (inclusiones y partes) → [[Algebra-Ejercicios-Conjuntos]]
- Dudas resueltas:
  - ¿Por qué $0{,}5$ se considera decimal periódico? Porque es racional: $0{,}5 = 0{,}5000\ldots$ y el periodo es el $0$ que se repite.
  - ¿Complementario o diferencia? Ver la nota del tema.

## Avisos
- **Portafolio**: 4 resoluciones de problemas, cada una vale un 10% (40% en total), más las actividades tipo test (Actividad 1, Actividad 2…, todas de C1).
- Los tests no tienen límite de tiempo y se puede salir y volver a entrar. Se pueden ir haciendo según avanza la asignatura y entregar todos hasta el día antes del cierre del portafolio.
- El profesor considera que las actividades corresponden a los contenidos descritos.
- **Examen**: 7 preguntas tipo test, 2 horas. Se permite papel y lápiz para resolver los ejercicios y no hace falta subirlo.

## Por ampliar (en Temas y Ejercicios)
- Combinatoria que explica el $6$ de "subconjuntos de 2 elementos de un conjunto de 4" (ejercicio 1, punto 2 del PDF del profesor). Se verá dentro de dos sesiones.
- Relaciones y aplicaciones (apartados 1.2 y 1.3 del plan de estudios).

## Enlaces
- [[Algebra-Tema-1.1-Conjuntos]]
- [[Algebra-Ejercicios-Conjuntos]]
- [[04GCIB - Sesión 1 - Conjuntos.pdf]]
- [[Algebra_Ciberseguridad.pdf]]
