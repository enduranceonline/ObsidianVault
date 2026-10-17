---
asignatura: Álgebra
tipo: tema
tema: 2
apartado: "2"
sesiones: []
estado: adelantado
material: "[[Algebra_Ciberseguridad.pdf]]"
---

# Tema 2 · Introducción a la combinatoria

> [!info] Nota adelantada
> Aún no se ha visto en clase. Fuente: Tema 2 de [[Algebra_Ciberseguridad.pdf]]. Se completará con la sesión correspondiente. Conecta con [[Algebra-Tema-1.1-Conjuntos]] (partes de un conjunto) y se usa en [[0_Algebra-Ejercicios-UC1]].
>
> Nota: la hoja de ejercicios UC1 incluye combinatoria junto con los contenidos de 1.1-1.3.

## 2.1 Principios de cardinalidad

### 2.1.1 Principio de la adición
Si $A$ y $B$ son **disjuntos** ($A \cap B = \emptyset$), entonces $|A \cup B| = |A| + |B|$. Se generaliza a $n$ conjuntos disjuntos dos a dos: $|A_1 \cup \cdots \cup A_n| = |A_1| + \cdots + |A_n|$.

> [!warning] Errata del libro
> El libro escribe la condición como $A \cap B \neq \emptyset$; debe ser $A \cap B = \emptyset$ (disjuntos).

- Ejemplo: 34 aprobados y 15 suspensos (nadie puede estar en ambos) $\Rightarrow$ $34 + 15 = 49$ presentados.

### 2.1.2 Principio de Dirichlet (palomar)
Si se reparten $m$ elementos en $n$ cajas y $m > n$, alguna caja contiene **al menos 2** elementos.

- Ejemplo: en una reunión de 8 personas, al menos dos nacieron el mismo día de la semana (7 días).
- Aplicaciones en informática: es imposible un hash sin colisiones, y un compresor sin pérdida que acorte algunos archivos debe alargar otros.

### 2.1.3 Principio de inclusión-exclusión
$$|A \cup B| = |A| + |B| - |A \cap B|.$$
Para tres conjuntos:
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|.$$

- Ejemplo: 15 estudian matemáticas, 10 física y 3 ambas $\Rightarrow$ $15 + 10 - 3 = 22$.

### 2.1.4 Principio de la multiplicación
$$|A \times B| = |A| \cdot |B|, \qquad |A_1 \times \cdots \times A_n| = |A_1| \cdots |A_n|.$$

- Ejemplo: 2 tipos de disco (HDD, SSD) y 3 sistemas operativos $\Rightarrow$ $2 \cdot 3 = 6$ configuraciones.

## 2.2 Permutaciones, combinaciones y variaciones

### Guía para elegir la fórmula
Responde a estas tres preguntas:

1. ¿**Importa el orden**? (¿cambiar el orden da un resultado distinto?)
2. ¿Se **pueden repetir** elementos?
3. ¿Se usan **todos** los elementos del conjunto (solo se reordenan) o se **elige una parte**?

| ¿Orden? | ¿Repetición? | ¿Todos los elementos? | Nombre | Fórmula |
| --- | --- | --- | --- | --- |
| Sí | No | Sí | Permutaciones sin repetición | $P_n = n!$ |
| Sí | Sí (elementos repetidos en el origen) | Sí | Permutaciones con repetición | $P_n^{n_1,\ldots,n_r} = \dfrac{n!}{n_1!\,n_2!\cdots n_r!}$ |
| No | No | No ($k$ de $n$) | Combinaciones sin repetición | $C_{n,k} = \dbinom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$ |
| No | Sí | No ($k$ de $n$) | Combinaciones con repetición | $CR_{n,k} = \dbinom{n+k-1}{k}$ |
| Sí | No | No ($k$ de $n$) | Variaciones sin repetición | $V_{n,k} = \dfrac{n!}{(n-k)!}$ |
| Sí | Sí | No ($k$ de $n$) | Variaciones con repetición | $VR_{n,k} = n^k$ |

### 2.2.1 Permutaciones sin repetición
Ordenar $n$ objetos distintos: $n \cdot (n-1) \cdots 2 \cdot 1 = n!$.
- Ejemplo: con $\{a,b,c,d\}$ hay $4! = 24$ ordenaciones.

### 2.2.2 Permutaciones con repetición
$n$ elementos de $r$ tipos, con $n_i$ elementos del tipo $i$: $\dfrac{n!}{n_1!\,n_2!\cdots n_r!}$.
- Ejemplo: los dígitos de $112223$: $n = 6$, con $n_1 = 2$ (unos), $n_2 = 3$ (doses), $n_3 = 1$ (tres): $\dfrac{6!}{2!\,3!\,1!} = 60$.

> [!warning] Errata del libro
> El libro da $120$ como resultado de este ejemplo, pero $\dfrac{720}{2 \cdot 6 \cdot 1} = 60$. El valor correcto es $60$.

### 2.2.3 Combinaciones sin repetición
Elegir $k$ de $n$ distintos, sin repetir, **sin importar el orden**: $\dbinom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$.
- Ejemplo: grupos de 3 letras de $\{a,b,c,d\}$: $\dbinom{4}{3} = 4$ (abc, abd, acd, bcd).
- **Es el número de subconjuntos de $k$ elementos de un conjunto de $n$.** Es el que justifica los $6$ subconjuntos de 2 elementos de la [[Algebra-clase01]]: $\dbinom{4}{2} = 6$.

### 2.2.4 Combinaciones con repetición
Elegir $k$ de $n$ **pudiendo repetir** y sin importar el orden: $\dbinom{n+k-1}{k}$.
- Ejemplo: grupos de 3 de $\{a,b,c,d\}$ permitiendo repetir: $\dbinom{6}{3} = 20$ (aaa, aab, aac, aad, abc, …).

### 2.2.5 Variaciones sin repetición
Elegir $k$ de $n$ **sin repetir e importando el orden**: $\dfrac{n!}{(n-k)!} = n(n-1)\cdots(n-k+1)$.
- Ejemplo: números de 2 cifras distintas con $\{1,2,3,4\}$: $\dfrac{4!}{2!} = 12$.

### 2.2.6 Variaciones con repetición
Elegir $k$ de $n$ **pudiendo repetir e importando el orden**: $n^k$.
- Ejemplo: números de 2 cifras con $\{1,2,3,4\}$ (pueden repetirse): $4^2 = 16$.

## Propiedades útiles del número combinatorio
(No están en el libro, pero se usan en los ejercicios de ampliación.)

- $\dbinom{n}{0} = \dbinom{n}{n} = 1$ y $\dbinom{n}{1} = n$.
- Simetría: $\dbinom{n}{k} = \dbinom{n}{n-k}$.
- **Conexión con las partes de un conjunto**: el número de subconjuntos de $k$ elementos de un $A$ con $|A| = n$ es $\dbinom{n}{k}$. Como $|\mathcal{P}(A)| = 2^n$ es la suma de los subconjuntos de todos los tamaños $k = 0, \ldots, n$, se obtiene
$$\sum_{k=0}^{n} \binom{n}{k} = 2^n.$$
- Ejemplo con $n = 4$: $1 + 4 + 6 + 4 + 1 = 16 = 2^4$ (los cardinales de la [[Algebra-Ejercicios-Conjuntos]]).

## Potencias de 2 y archivos (contexto informático)
- Un byte son 8 bits, y cada bit tiene 2 valores. Un byte distingue $2^8 = 256$ valores, y una cadena de $m$ bytes, $256^m$ valores. Es una variación con repetición: $n^k$ con $n = 256$.

## Enlaces
- [[Algebra-Tema-1.1-Conjuntos]]
- [[Algebra-Tema-1.3-Aplicaciones]]
- [[0_Algebra-Ejercicios-UC1]]
