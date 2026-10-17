---
asignatura: Álgebra
tipo: ejercicios
tema: 1
apartado: "1.1"
sesiones: [1]
---

# Ejercicios — Conjuntos

Ejercicios planteados en [[Algebra-clase01]]. Teoría en [[Algebra-Tema-1.1-Conjuntos]].

Estrategia general: para decidir $A \subseteq B$ se comprueba que **todos** los elementos de $A$ están en $B$. Para decidir $A \not\subseteq B$ basta **un** elemento de $A$ que no esté en $B$ (un contraejemplo).

---

# Ejercicios de clase

## Inclusiones 1
$A = \{x, y, 7, *\}$, $B = \{y, *, x\}$, $C = \{*\}$. Indica todas las inclusiones.

(En los apuntes ponía "xy"; se interpreta como dos elementos $x, y$. Si fuera un único elemento "xy", entonces $B \not\subseteq A$.)

**Resolución.** Se comprueba cada par ordenado:

- $C \subseteq A$: el único elemento de $C$ es $*$, y $* \in A$.
- $C \subseteq B$: $* \in B$.
- $B \subseteq A$: $y \in A$, $* \in A$ y $x \in A$.
- $A \not\subseteq B$: $7 \in A$ pero $7 \notin B$.
- $A \not\subseteq C$: $x \in A$ pero $x \notin C$.
- $B \not\subseteq C$: $x \in B$ pero $x \notin C$.

Se cumple la cadena $C \subseteq B \subseteq A$ (por transitividad, $C \subseteq A$ también se deduce de las otras dos).

Además, todo conjunto está incluido en sí mismo ($A \subseteq A$, $B \subseteq B$, $C \subseteq C$) y $\emptyset$ está incluido en los tres. Ningún par es igual, porque no hay inclusión en ambos sentidos.

**Diagrama de Venn:** $C$ dentro de $B$, y $B$ dentro de $A$. El elemento $7$ queda en $A$ fuera de $B$.

## Inclusiones 2
$P$ = primos, $\mathbb{N}$ = naturales, $\mathbb{Q}$ = racionales, $2\mathbb{Z}$ = enteros pares.

**Resolución.**

- $P \subseteq \mathbb{N}$: todo primo es un número natural. De aquí, $P \subseteq \mathbb{N} \subseteq \mathbb{Q}$ y por transitividad $P \subseteq \mathbb{Q}$.
- $\mathbb{N} \subseteq \mathbb{Q}$: todo natural $n$ es la fracción $n/1$.
- $2\mathbb{Z} \subseteq \mathbb{Q}$: todo entero es racional, en particular los pares.
- $2\mathbb{Z} \not\subseteq \mathbb{N}$: $-2$ es par pero no es natural.
- $\mathbb{N} \not\subseteq 2\mathbb{Z}$: $1$ es natural y no es par. Por la misma razón $\mathbb{Q} \not\subseteq 2\mathbb{Z}$.
- $P \not\subseteq 2\mathbb{Z}$: $3$ es primo y no es par.
- $2\mathbb{Z} \not\subseteq P$: $4$ es par y no es primo.
- $\mathbb{N} \not\subseteq P$: $4$ es natural y no es primo.
- $\mathbb{Q} \not\subseteq \mathbb{N}$: $1/2$ es racional y no es natural.

Los conjuntos $P$ y $2\mathbb{Z}$ **no están incluidos** el uno en el otro, pero tampoco son disjuntos: $P \cap 2\mathbb{Z} = \{2\}$, el único primo par.

**Diagrama de Venn:** $P \subseteq \mathbb{N} \subseteq \mathbb{Q}$ como círculos anidados. $2\mathbb{Z}$ es un círculo dentro de $\mathbb{Q}$ que solo se solapa con $\mathbb{N}$ (en los pares positivos) y toca a $P$ únicamente en el $2$.

## Partes 1
$B = \{a, b, c, d\}$.

1. Escribe 3 subconjuntos con $|X| = 2$.
2. ¿Cuántos subconjuntos con cardinal 2 hay?
3. ¿Cuántos conjuntos hay en $\mathcal{P}(B)$, es decir, cuánto es $|\mathcal{P}(B)|$?

**Resolución.**

1. Por ejemplo $\{a,b\}$, $\{a,c\}$, $\{b,d\}$.
2. Se listan de forma sistemática para no olvidar ninguno: primero los que contienen $a$, luego los que contienen $b$ pero no $a$, y así:
   - con $a$: $\{a,b\}$, $\{a,c\}$, $\{a,d\}$
   - con $b$ (sin $a$): $\{b,c\}$, $\{b,d\}$
   - con $c$ (sin $a$ ni $b$): $\{c,d\}$

   Hay $3 + 2 + 1 = 6$. La combinatoria explicará esto como $\binom{4}{2} = \frac{4!}{2!\,2!} = 6$.
3. $\mathcal{P}(B)$ se escribe por cardinales:
   - cardinal 0: $\emptyset$ (1 conjunto)
   - cardinal 1: $\{a\}, \{b\}, \{c\}, \{d\}$ (4 conjuntos)
   - cardinal 2: los 6 anteriores (6 conjuntos)
   - cardinal 3: $\{a,b,c\}, \{a,b,d\}, \{a,c,d\}, \{b,c,d\}$ (4 conjuntos)
   - cardinal 4: $\{a,b,c,d\}$ (1 conjunto)

   Total: $1 + 4 + 6 + 4 + 1 = 16 = 2^4$, que coincide con el teorema $|\mathcal{P}(A)| = 2^n$.

**Por qué $2^n$.** Para formar un subconjunto hay que decidir, para cada elemento, si entra o no. Con 4 elementos hay $2 \cdot 2 \cdot 2 \cdot 2 = 2^4$ decisiones distintas, y cada una da un subconjunto diferente.

## Partes 2
Dame un conjunto $X$ con $|\mathcal{P}(X)| = 4096$.

**Resolución.** Hay que encontrar $n$ con $2^n = 4096$. Como $2^{10} = 1024$ y $4096 = 4 \cdot 1024 = 2^2 \cdot 2^{10}$, se tiene $4096 = 2^{12}$, luego $|X| = 12$.

Cualquier conjunto de 12 elementos sirve, por ejemplo $X = \{1, 2, \ldots, 12\}$ o los meses del año. **Comprobación:** $|\mathcal{P}(X)| = 2^{12} = 4096$.

---

# Ejercicios de ampliación

## Ampliación 1 — Pertenencia e inclusión
Sea $A = \{a, \{a\}, \{a, b\}\}$. Decide si es verdadero o falso:

1. $a \in A$
2. $\{a\} \in A$
3. $\{a\} \subseteq A$
4. $\{a, b\} \in A$
5. $\{a, b\} \subseteq A$
6. $\emptyset \in A$
7. $\emptyset \subseteq A$
8. $\{\{a\}\} \subseteq A$

Calcula también $|A|$.

> [!solution]- Solución
> Clave: $\in$ relaciona un elemento con un conjunto, y $\subseteq$ relaciona dos conjuntos. $A$ tiene exactamente tres elementos: $a$, $\{a\}$ y $\{a,b\}$.
>
> 1. Verdadero: $a$ es uno de los tres elementos.
> 2. Verdadero: $\{a\}$ es el segundo elemento.
> 3. Verdadero: la inclusión exige que todo elemento de $\{a\}$ esté en $A$, y $a \in A$.
> 4. Verdadero: es el tercer elemento.
> 5. Falso: habría que tener $a \in A$ y $b \in A$, pero $b \notin A$.
> 6. Falso: $\emptyset$ no es ninguno de los tres elementos.
> 7. Verdadero: el vacío está incluido en cualquier conjunto.
> 8. Verdadero: el único elemento de $\{\{a\}\}$ es $\{a\}$, y $\{a\} \in A$.
>
> $|A| = 3$.

## Ampliación 2 — Partes anidadas
Calcula $\mathcal{P}(\emptyset)$, $\mathcal{P}(\mathcal{P}(\emptyset))$ y los cardinales de cada uno. ¿Cuánto vale $|\mathcal{P}(\mathcal{P}(\mathcal{P}(\emptyset)))|$?

> [!solution]- Solución
> - $\mathcal{P}(\emptyset) = \{\emptyset\}$: el único subconjunto del vacío es el propio vacío. Cardinal $1 = 2^0$.
> - $\mathcal{P}(\{\emptyset\}) = \{\emptyset, \{\emptyset\}\}$. Cardinal $2 = 2^1$.
> - $|\mathcal{P}(\mathcal{P}(\mathcal{P}(\emptyset)))| = 2^2 = 4$, porque el conjunto anterior tiene 2 elementos.
>
> Obsérvese que $\{\emptyset\} \neq \emptyset$: el primero tiene un elemento y el segundo ninguno.

## Ampliación 3 — Operaciones con un conjunto universal
Sea $U = \{1, 2, \ldots, 10\}$, $A = \{1,2,3,4,5,6\}$, $B = \{4,5,6,7,8\}$, $C = \{2,4,6,8,10\}$. Calcula:

1. $A \cap B$, $A \cup B$, $A \setminus B$, $B \setminus A$.
2. $A^c$, $B^c$, $(A \cup B)^c$ y $A^c \cap B^c$. ¿Qué observas?
3. $A \cap (B \cup C)$ y $(A \cap B) \cup (A \cap C)$. ¿Qué observas?

> [!solution]- Solución
> 1. $A \cap B = \{4,5,6\}$. $A \cup B = \{1,2,3,4,5,6,7,8\}$. $A \setminus B = \{1,2,3\}$. $B \setminus A = \{7,8\}$ (y se ve que la diferencia no es simétrica).
> 2. $A^c = \{7,8,9,10\}$. $B^c = \{1,2,3,9,10\}$. $(A \cup B)^c = \{9,10\}$. $A^c \cap B^c = \{9,10\}$. Coinciden: es la ley de De Morgan $(A \cup B)^c = A^c \cap B^c$.
> 3. $B \cup C = \{2,4,5,6,7,8,10\}$, así que $A \cap (B \cup C) = \{2,4,5,6\}$. Por otro lado $A \cap B = \{4,5,6\}$, $A \cap C = \{2,4,6\}$ y su unión es $\{2,4,5,6\}$. Coinciden: propiedad distributiva.

## Ampliación 4 — Demostración por doble inclusión
Demuestra que si $A \subseteq B$, entonces $A \cap B = A$ y $A \cup B = B$.

> [!solution]- Solución
> **$A \cap B = A$.** Se prueban las dos inclusiones.
> - $A \cap B \subseteq A$: si $x \in A \cap B$, entonces $x \in A$ y $x \in B$; en particular $x \in A$.
> - $A \subseteq A \cap B$: sea $x \in A$. Como $A \subseteq B$, también $x \in B$. Luego $x \in A \cap B$.
>
> **$A \cup B = B$.**
> - $A \cup B \subseteq B$: si $x \in A \cup B$, o $x \in B$ (ya está), o $x \in A$ y entonces $x \in B$ por la hipótesis.
> - $B \subseteq A \cup B$: si $x \in B$, entonces $x \in A \cup B$ por definición de unión.
>
> Esto justifica lo dicho en clase: si un conjunto está dentro del otro, la intersección es el de dentro y la unión es el de fuera.

## Ampliación 5 — La diferencia no es simétrica
Demuestra que $A \setminus B = B \setminus A$ solo ocurre si $A = B$, y en ese caso ambos son vacíos.

> [!solution]- Solución
> Supón que $A \setminus B = B \setminus A$ y que existe $x \in A \setminus B$. Entonces $x \in A$ y $x \notin B$. Como $A \setminus B = B \setminus A$, también $x \in B \setminus A$, es decir, $x \in B$. Esto contradice $x \notin B$. Por tanto $A \setminus B = \emptyset$, y por igualdad $B \setminus A = \emptyset$.
>
> $A \setminus B = \emptyset$ significa $A \subseteq B$, y $B \setminus A = \emptyset$ significa $B \subseteq A$. Por la doble inclusión, $A = B$.
>
> Recíprocamente, si $A = B$ ambas diferencias son $\emptyset$.

## Ampliación 6 — De decimal periódico a fracción
Escribe como fracción:

1. $0{,}\overline{36}$
2. $2{,}4\overline{15}$ (es decir, $2{,}4151515\ldots$)
3. $0{,}\overline{9}$

> [!solution]- Solución
> **1.** $x = 0{,}3636\ldots$. El periodo tiene 2 cifras, así que $100x = 36{,}3636\ldots$. Restando, $99x = 36$, luego $x = \frac{36}{99} = \frac{4}{11}$.
>
> **2.** $x = 2{,}41515\ldots$. Se usan dos potencias: una que corre la coma hasta justo antes del periodo y otra hasta después del primer periodo.
> - $10x = 24{,}1515\ldots$
> - $1000x = 2415{,}1515\ldots$
> - Restando: $990x = 2415 - 24 = 2391$, luego $x = \frac{2391}{990} = \frac{797}{330}$.
>
> **3.** $x = 0{,}999\ldots$, $10x = 9{,}999\ldots$ y restando, $9x = 9$, luego $x = 1$. Así, $1 = 0{,}\overline{9}$: un mismo número racional puede tener dos escrituras decimales.

## Ampliación 7 — De fracción a decimal periódico
Obtén el desarrollo decimal de $\frac{5}{12}$ y de $\frac{3}{7}$ siguiendo los restos de la división. ¿Cuántos restos distintos puede haber al dividir entre 7?

> [!solution]- Solución
> **$5/12$.** Se multiplica el resto por 10 y se divide entre 12:
> - $50 = 4 \cdot 12 + 2$ (cifra 4, resto 2)
> - $20 = 1 \cdot 12 + 8$ (cifra 1, resto 8)
> - $80 = 6 \cdot 12 + 8$ (cifra 6, resto 8)
>
> El resto $8$ se repite, así que la cifra $6$ se repite siempre: $\frac{5}{12} = 0{,}41\overline{6}$.
>
> **$3/7$.** Restos sucesivos: $3 \to 2 \to 6 \to 4 \to 5 \to 1 \to 3$, con cifras $4, 2, 8, 5, 7, 1$. Al reaparecer el resto $3$ empieza otro ciclo: $\frac{3}{7} = 0{,}\overline{428571}$.
>
> Al dividir entre $7$ los restos están entre $0$ y $6$. Si aparece el $0$ el decimal termina, y si no hay a lo sumo 6 restos distintos, así que el periodo tiene como máximo 6 cifras. Este argumento es el que prueba $\mathbb{Q} \subseteq D$.

## Ampliación 8 — Contar subconjuntos con una condición
Sea $X$ un conjunto de 5 elementos y $a \in X$.

1. ¿Cuántos subconjuntos de $X$ contienen a $a$?
2. ¿Cuántos no lo contienen?
3. Si $|\mathcal{P}(Y)| = 64$, ¿cuántos elementos tiene $Y$?

> [!solution]- Solución
> 1. Para formar un subconjunto que contenga a $a$, ese elemento queda fijado y solo se decide para los otros 4: $2^4 = 16$.
> 2. Para los que no contienen a $a$, también $2^4 = 16$.
> 3. $64 = 2^6$, así que $|Y| = 6$.
>
> Comprobación de los apartados 1 y 2: $16 + 16 = 32 = 2^5 = |\mathcal{P}(X)|$.

---

## Enlaces
- [[Algebra-clase01]]
- [[Algebra-Tema-1.1-Conjuntos]]
