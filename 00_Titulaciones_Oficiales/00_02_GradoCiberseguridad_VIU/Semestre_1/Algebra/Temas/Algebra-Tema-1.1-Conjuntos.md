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

Una operación toma dos conjuntos y construye un conjunto nuevo. Antes de verlas, el glosario con todo el lenguaje que hace falta para leer sus fórmulas y las propiedades.

### Glosario de simbología

| Símbolo | Se lee | Significa | Ejemplo |
| --- | --- | --- | --- |
| $x \in A$ | "$x$ pertenece a $A$" | $x$ es un elemento de $A$ | $3 \in \{1,3,5\}$ |
| $x \notin A$ | "$x$ no pertenece a $A$" | $x$ **no** es un elemento de $A$ | $2 \notin \{1,3,5\}$ |
| $\{ \ldots \}$ | "el conjunto formado por…" | Las llaves agrupan los elementos | $\{1,3,5\}$ |
| $\mid$ (dentro de llaves) | "tal que" | Separa el nombre de la variable de su condición | $\{x \mid x \in A \wedge x \in B\}$ |
| $\emptyset$ | "conjunto vacío" | Conjunto sin ningún elemento | $\{1,2\} \cap \{3,4\} = \emptyset$ |
| $A \subseteq B$ | "$A$ incluido en $B$" | Todo elemento de $A$ está en $B$ | $\{1,3\} \subseteq \{1,2,3\}$ |
| $\wedge$ | "y" | Se cumplen **las dos** condiciones a la vez | $x \in A \wedge x \in B$ |
| $\vee$ | "o" | Se cumple **al menos una** (puede ser ambas) | $x \in A \vee x \in B$ |
| $\neg$ | "no" | Niega una condición | $\neg(x \in A)$ es lo mismo que $x \notin A$ |
| $\cap$ | "intersección" | Elementos comunes a los dos conjuntos | $\{1,2,3\} \cap \{2,3,4\} = \{2,3\}$ |
| $\cup$ | "unión" | Elementos de uno u otro (o de ambos) | $\{1,2\} \cup \{2,3\} = \{1,2,3\}$ |
| $B \setminus A$ | "$B$ menos $A$" | Elementos de $B$ que **no** están en $A$ | $\{1,2,3\} \setminus \{2\} = \{1,3\}$ |
| $U$ | "universo" (conjunto total) | Conjunto que contiene a todos los demás con los que se trabaja | $U = \{1,\ldots,8\}$ |
| $A^c$ | "complementario de $A$" | Todo lo de $U$ que no está en $A$: $A^c = U \setminus A$ | Con $U = \{1,\ldots,8\}$, $\{1,2\}^c = \{3,\ldots,8\}$ |
| $\forall$ | "para todo" | La afirmación vale para cada elemento | $\forall x \in A, x \in B$ |
| $\to$ | "implica" | Si se cumple lo de la izquierda, se cumple lo de la derecha | $x \in A \to x \in B$ |
| $\iff$ | "si y solo si" | Las dos afirmaciones son equivalentes | $A = B \iff A \subseteq B \wedge B \subseteq A$ |
| $A \cap B = \emptyset$ | "$A$ y $B$ son disjuntos" | No tienen ningún elemento en común | $\{1,3\}$ y $\{2,4\}$ |
| $\lvert A \rvert$ | "cardinal de $A$" | Número de elementos | $\lvert\{a,b,c\}\rvert = 3$ |

> [!warning] El "o" matemático es inclusivo
> $x \in A \vee x \in B$ **incluye** el caso en que $x$ está en los dos. En castellano a veces "o" significa uno u otro pero no ambos; aquí no.

### Conjuntos de ejemplo
Para ver todas las operaciones con los mismos datos:
$$U = \{1,2,3,4,5,6,7,8\}, \quad A = \{1,2,3,4\}, \quad B = \{3,4,5,6\}$$

### Intersección $A \cap B$
$$A \cap B = \{x \mid x \in A \wedge x \in B\}$$
- **Qué dice la fórmula:** "el conjunto de los $x$ tales que $x$ está en $A$ **y** además en $B$"; es decir, lo que $A$ y $B$ tienen en común.
- **Venn:** se sombrea solo la zona donde se solapan los dos círculos.
- **Ejemplo:** $A \cap B = \{3, 4\}$.
- Si no se solapan, $A \cap B = \emptyset$ y los conjuntos son **disjuntos**. Si $A \subseteq B$, entonces $A \cap B = A$ (el de dentro).

![[Venn-interseccion.png | center]]

### Unión $A \cup B$
$$A \cup B = \{x \mid x \in A \vee x \in B\}$$
- **Qué dice la fórmula:** "el conjunto de los $x$ tales que $x$ está en $A$ **o** en $B$ (o en los dos)"; se juntan todos los elementos, **sin repetir** los comunes.
- **Venn:** se sombrean los dos círculos enteros.
- **Ejemplo:** $A \cup B = \{1, 2, 3, 4, 5, 6\}$. El $3$ y el $4$ están en los dos y aparecen una sola vez.
- Si $A \subseteq B$, entonces $A \cup B = B$ (el de fuera).
![[Venn-union.png | center | 450]]

### Diferencia (complementario) $B \setminus A$
$$B \setminus A = \{x \mid x \in B \wedge x \notin A\}$$
- **Qué dice la fórmula:** "los $x$ que están en $B$ **y no** están en $A$"; a $B$ se le **quita** lo que tiene en común con $A$.
- **Venn:** se sombrea el círculo de $B$ **menos** la zona de solapamiento.
- **Ejemplo:** $A \setminus B = \{1, 2\}$ y $B \setminus A = \{5, 6\}$. **No son iguales**: la diferencia no es simétrica.
- Si $A \subseteq B$, entonces $A \setminus B = \emptyset$ (a $A$ no le queda nada).
- **Complementario:** cuando hay un universo $U$, $A^c = U \setminus A$. Con el ejemplo, $A^c = \{5,6,7,8\}$ y $B^c = \{1,2,7,8\}$. En $\mathbb{N}$, el complementario de los pares son los impares.

![[Venn-diferencia-BA.png.png | center]]

### Propiedades
Para $A, B, C$ cualesquiera. Se comprueban con los conjuntos de ejemplo, añadiendo $C = \{4, 6, 7\}$.

#### 1. Asociativa
$$(A \cup B) \cup C = A \cup (B \cup C) \qquad (A \cap B) \cap C = A \cap (B \cap C)$$
- **En palabras:** si encadenas solo uniones, o solo intersecciones, **da igual dónde pongas los paréntesis**; por eso se puede escribir $A \cup B \cup C$ sin ambigüedad.
- **Comprobación:**
  - $(A \cup B) \cup C = \{1,\ldots,6\} \cup \{4,6,7\} = \{1,\ldots,7\}$ y $A \cup (B \cup C) = \{1,2,3,4\} \cup \{3,\ldots,7\} = \{1,\ldots,7\}$.
  - $(A \cap B) \cap C = \{3,4\} \cap \{4,6,7\} = \{4\}$ y $A \cap (B \cap C) = A \cap \{4,6\} = \{4\}$.

#### 2. Conmutativa
$$A \cup B = B \cup A \qquad A \cap B = B \cap A$$
- **En palabras:** **el orden no importa** en la unión ni en la intersección.
- **Contraste:** la diferencia **no** es conmutativa ($A \setminus B \neq B \setminus A$).

#### 3. Distributiva
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \qquad A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$
- **En palabras:** una operación se **reparte** sobre la otra, como $a(b + c) = ab + ac$. Aquí se reparten **las dos** (con los números solo se reparte el producto sobre la suma).
- **Comprobación:**
  - $B \cup C = \{3,4,5,6,7\}$, así que $A \cap (B \cup C) = \{3,4\}$. Y $(A \cap B) \cup (A \cap C) = \{3,4\} \cup \{4\} = \{3,4\}$.
  - $B \cap C = \{4,6\}$, así que $A \cup (B \cap C) = \{1,2,3,4,6\}$. Y $(A \cup B) \cap (A \cup C) = \{1,\ldots,6\} \cap \{1,2,3,4,6,7\} = \{1,2,3,4,6\}$.

#### 4. Leyes de De Morgan
$$(A \cup B)^c = A^c \cap B^c \qquad (A \cap B)^c = A^c \cup B^c$$
- **En palabras:** al pasar al complementario, **la unión se convierte en intersección y la intersección en unión**. "No estar en ($A$ o $B$)" equivale a "no estar en $A$ **y** no estar en $B$".
- **Por qué:** es la negación lógica, $x \in (A \cup B)^c \iff \neg(x \in A \vee x \in B) \iff x \notin A \wedge x \notin B$.
- **Comprobación** (con $U$ del ejemplo):
  - $(A \cup B)^c = \{1,\ldots,6\}^c = \{7,8\}$ y $A^c \cap B^c = \{5,6,7,8\} \cap \{1,2,7,8\} = \{7,8\}$.
  - $(A \cap B)^c = \{3,4\}^c = \{1,2,5,6,7,8\}$ y $A^c \cup B^c = \{5,6,7,8\} \cup \{1,2,7,8\} = \{1,2,5,6,7,8\}$.


## 1.1.3 Partes de un conjunto
- $\mathcal{P}(A) = \{B \mid B \subseteq A\}$.
- Los elementos de un conjunto pueden ser conjuntos: en $A = \{\{a,b\}, c\}$ se tiene $\{a,b\} \in A$, pero $a \notin A$.
- Se lista por cardinal: $\emptyset$ (siempre incluido), los de 1 elemento, los de 2, etc., y al final el propio $A$.
- Ejemplo: $\mathcal{P}(\{1,2,3\}) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}\}$, con $1+3+3+1 = 8$ elementos.
- **Teorema**: si $|A| = n$, entonces $|\mathcal{P}(A)| = 2^n$.

## Complemento adelantado (para la hoja de ejercicios UC1)

> [!info] No visto en clase
> Esta parte no está en el libro con este detalle; es notación y método necesarios para [[Algebra-Ejercicios-UC1]].

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
