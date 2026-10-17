---
asignatura: Álgebra
tipo: tema
tema: 1
apartado: "1.1"
sesiones: [1]
material: "[[Algebra_Ciberseguridad.pdf]]"
---

# 1.1 Conjuntos

Fuente: apartado 1.1 de [[Algebra_Ciberseguridad.pdf]] y diapositivas de [[04GCIB - Sesión 1 - Conjuntos.pdf]]. Visto en [[Algebra-clase01]].

## Definiciones
- Un **conjunto** es una colección de objetos físicos o abstractos, llamados **elementos**.
- $a \in A$: "$a$ es un elemento de $A$" o "$a$ pertenece a $A$".
- Se denota entre llaves con los elementos separados por comas, o por una propiedad: $\{2n - 1 \mid n \in \mathbb{N}\}$.
- El **cardinal** $|A|$ es el número de elementos. Si es infinito, $|A| = \infty$.
  - Ejemplo: continentes de la Tierra, $|A| = 6$.
  - Ejemplo: naturales impares, $|B| = \infty$.

## 1.1.1 Relaciones entre conjuntos
- **Inclusión**: $A \subseteq B$ si $\forall x \in A,\ x \in B$. En caso contrario, $A \not\subseteq B$.
- $\emptyset \subseteq A$ para todo conjunto $A$.
- **Igualdad**: $A = B$ si $A \subseteq B$ y $B \subseteq A$.
- La inclusión propia ($A \subseteq B$ y $A \neq B$) no se usa en la asignatura.
- Ejemplos:
  - $A = \{a,b,c\}$, $B = \{a,b,c,d\}$: $A \subseteq B$ pero $B \not\subseteq A$ (porque $d \in B$ y $d \notin A$).
  - $A = \{1,3,4\}$, $B = \{1,2,4\}$: no hay inclusión en ningún sentido ($3 \in A$, $3 \notin B$; $2 \in B$, $2 \notin A$).
  - $B = \{a,d,e\}$ es subconjunto de $A = \{a,b,c,d,e,f\}$, pero $C = \{a,g\}$ no lo es.

### Ejemplo de igualdad: $\mathbb{Q} = D$
$\mathbb{Q} = \{a/b \mid a,b \in \mathbb{Z},\ b \neq 0\}$ y $D$ = decimales periódicos. Hay que probar las dos inclusiones.

- $D \subseteq \mathbb{Q}$ (un decimal periódico es una fracción):
  1. Correr la coma hasta después del primer periodo.
  2. Correr la coma hasta justo antes del inicio del primer periodo.
  3. Restar ambas, lo que elimina la parte periódica.
  - Con $x = 0{,}7537\ldots$: $10^4 x = 7537{,}37\ldots$, $10^2 x = 75{,}37\ldots$, y $(10^4 - 10^2)\,x = 7462$, luego $x = \frac{7462}{9900}$.
- $\mathbb{Q} \subseteq D$ (una fracción es un decimal periódico): al dividir $a/b$ los restos $r_i$ están entre $0$ y $b-1$ y por tanto, en algún momento, se repiten. Ejemplo: $3/7$, restos entre $0$ y $6$.
- $0{,}5 = 0{,}5000\ldots$ es periódico, con periodo $0$.

## 1.1.2 Operaciones entre conjuntos
- **Unión**: $A \cup B = \{x \mid x \in A \vee x \in B\}$.
- **Intersección**: $A \cap B = \{x \mid x \in A \wedge x \in B\}$. Si $A \cap B = \emptyset$, son **disjuntos**. Si $A \subseteq B$, entonces $A \cap B = A$.
- **Complementario / diferencia**: $B \setminus A = \{x \mid x \in B \wedge x \notin A\}$.
  - No es simétrica. Si $A \subseteq B$, entonces $A \setminus B = \emptyset$.
  - "Complementario" se usa cuando hay un conjunto universal $U$: $A^c = U \setminus A$. En esta asignatura se usan ambos nombres.
  - Ejemplo: el complementario de los pares en $\mathbb{N}$ es el conjunto de los impares.
- Ejemplos: $A \cup B$ con $A = \{a,b,c,e\}$, $B = \{c,e,f\}$ da $\{a,b,c,e,f\}$. Con $A = \{1,3,5\}$, $B = \{2,4,6\}$ da $\{1,2,3,4,5,6\}$.

### Propiedades
Para $A, B, C$ cualesquiera:
1. Asociativa: $(A \cup B) \cup C = A \cup (B \cup C)$ y $(A \cap B) \cap C = A \cap (B \cap C)$.
2. Conmutativa: $A \cup B = B \cup A$ y $A \cap B = B \cap A$.
3. Distributiva: $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ y $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$.
4. De Morgan: $(A \cup B)^c = A^c \cap B^c$ y $(A \cap B)^c = A^c \cup B^c$.

## 1.1.3 Partes de un conjunto
- $\mathcal{P}(A) = \{B \mid B \subseteq A\}$.
- Los elementos de un conjunto pueden ser conjuntos: en $A = \{\{a,b\}, c\}$ se tiene $\{a,b\} \in A$, pero $a \notin A$.
- Se lista por cardinal: $\emptyset$ (siempre incluido), los de 1 elemento, los de 2, etc., y al final el propio $A$.
- Ejemplo: $\mathcal{P}(\{1,2,3\}) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}\}$, con $1+3+3+1 = 8$ elementos.
- **Teorema**: si $|A| = n$, entonces $|\mathcal{P}(A)| = 2^n$.

## Complemento adelantado (para la hoja de ejercicios UC1)

> [!info] No visto en clase
> Esta parte no está en el libro con este detalle; es notación y método necesarios para [[0_Algebra-Ejercicios-UC1]].

### Convención sobre $\mathbb{N}$
En el libro, $\mathbb{N} = \{1, 2, 3, \ldots\}$: el $0$ **no** está. Por eso $\{2n \mid n \in \mathbb{N}\} = \{2, 4, 6, \ldots\}$.

### Notación de intervalos de $\mathbb{R}$
- $[a, b] = \{x \in \mathbb{R} \mid a \leq x \leq b\}$ (cerrado: incluye los extremos).
- $]a, b[ = \{x \mid a < x < b\}$ (abierto; también se escribe $(a, b)$).
- $[a, b[ = \{x \mid a \leq x < b\}$ y $]a, b] = \{x \mid a < x \leq b\}$.
- $]a, +\infty[ = \{x \mid x > a\}$ y $]-\infty, b] = \{x \mid x \leq b\}$. El **infinito siempre va abierto**, porque no es un número.
- $]-\infty, +\infty[ = \mathbb{R}$.

> [!tip] Cómo operar con intervalos
> 1. **Dibuja la recta real** y marca cada conjunto (punto relleno si el extremo está incluido, hueco si no).
> 2. La intersección es lo que está marcado en **ambos**; la unión, lo que está marcado en **alguno**; $A \setminus B$, lo de $A$ que no está en $B$.
> 3. **Estudia cada extremo por separado**: ¿pertenece o no al resultado? Ahí se cometen casi todos los errores.
> 4. Si el resultado está formado por dos trozos separados, se deja como **unión de intervalos**, y si no queda nada, es $\emptyset$.
>
> Ejemplo (no es de la hoja): $[0, 3]$ y $]1, 5[$.
> - $[0,3] \cap\, ]1,5[\ = \,]1, 3]$ (el $1$ no está en $]1,5[$ y el $3$ sí está en ambos).
> - $[0,3] \cup\, ]1,5[\ = [0, 5[$.
> - $[0,3] \setminus\, ]1,5[\ = [0, 1]$ (el $1$ sí está en $[0,3]$ y no en $]1,5[$).
> - $]1,5[\ \setminus\, [0,3] = \,]3, 5[$.

### Conjuntos de múltiplos
$a\mathbb{Z} = \{an \mid n \in \mathbb{Z}\}$ es el conjunto de los múltiplos de $a$ (por ejemplo $2\mathbb{Z}$ son los pares). Un entero $z$ está en $a\mathbb{Z} \cap b\mathbb{Z}$ si es múltiplo **de ambos** a la vez.

### Cómo demostrar igualdades de conjuntos (propiedades y De Morgan)
Hay dos métodos:

1. **Doble inclusión**: probar $X \subseteq Y$ y $Y \subseteq X$ con un elemento genérico $x$.
2. **Cadena de equivalencias**: traducir a lógica ($x \in A \cup B \iff x \in A \vee x \in B$, etc.) y usar las leyes de la lógica (asociativa, conmutativa, distributiva y De Morgan de $\wedge, \vee, \neg$).

> [!example] Ejemplo de método: absorción $A \cap (A \cup B) = A$
> - $\subseteq$: si $x \in A \cap (A \cup B)$, en particular $x \in A$.
> - $\supseteq$: si $x \in A$, entonces $x \in A \cup B$, y como también $x \in A$, se tiene $x \in A \cap (A \cup B)$.
>
> Por equivalencias: $x \in A \cap (A \cup B) \iff x \in A \wedge (x \in A \vee x \in B) \iff x \in A$.

## Por ampliar
- Número de subconjuntos de $k$ elementos de un conjunto de $n$: $\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$. Por ejemplo, $\binom{4}{2} = 6$. Se verá en la sesión de combinatoria.

## Enlaces
- [[Algebra-clase01]]
- [[Algebra-Ejercicios-Conjuntos]]
