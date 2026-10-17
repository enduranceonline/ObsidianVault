---
asignatura: Álgebra
tipo: tema
tema: 1
apartado: "1.2"
sesiones: []
estado: adelantado
material: "[[Algebra_Ciberseguridad.pdf]]"
---

# 1.2 Relaciones

> [!info] Nota adelantada
> Aún no se ha visto en clase. Fuente: apartado 1.2 de [[Algebra_Ciberseguridad.pdf]]. Se completará con la sesión correspondiente. Viene de [[Algebra-Tema-1.1-Conjuntos]]; se usa en [[0_Algebra-Ejercicios-UC1]].

## Par ordenado y producto cartesiano
- **Par ordenado** $(a, b)$: une $a \in A$ (primera componente) y $b \in B$ (segunda componente). **El orden importa**: $(1, 2) \neq (2, 1)$.
- **Producto cartesiano**: $A \times B = \{(a, b) \mid a \in A \wedge b \in B\}$.
- Ejemplo: $A = \{1,2,3\}$, $B = \{c,d\}$:
  $A \times B = \{(1,c), (1,d), (2,c), (2,d), (3,c), (3,d)\}$.
- $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$ es el plano real.
- **Cardinal** (principio de la multiplicación): $|A \times B| = |A| \cdot |B|$.
- En general $A \times B \neq B \times A$ (no es conmutativo).

> [!tip] Cómo listar $A \times B$ sin olvidar ninguno
> Fija cada elemento de $A$ por orden y empareja con **todos** los de $B$, como en el ejemplo. Comprueba al final que el número de pares es $|A| \cdot |B|$.

## 1.2.1 Relaciones
- Una **relación** $\mathcal{R}$ de $A$ en $B$ es un **subconjunto** de $A \times B$:
  $\mathcal{R} = \{(a, b) \in A \times B \mid a \mathrel{\mathcal{R}} b\} \subseteq A \times B$.
- $a \mathrel{\mathcal{R}} b$ significa "$a$ está relacionado con $b$".
- Ejemplo 1: $A = \{1,2,3,4,5\}$, $B = \{-2,0,1,-3\}$, y $a \mathrel{\mathcal{R}} b$ si $a$ es par y $b$ es negativo. Entonces $\mathcal{R} = \{(2,-2), (2,-3), (4,-2), (4,-3)\}$.
- Ejemplo 2: mismos conjuntos, $a \mathrel{\mathcal{R}} b$ si $a + b$ es múltiplo de 3. Entonces $\mathcal{R} = \{(2,-2), (2,1), (3,0), (3,-3), (5,-2), (5,1)\}$.

## 1.2.2 Relaciones de equivalencia
Una relación $\mathcal{R}$ de un conjunto $A$ **sobre sí mismo** es de **equivalencia** si cumple:

1. **Reflexiva**: $\forall a \in A,\ a \mathrel{\mathcal{R}} a$.
2. **Simétrica**: $\forall a, b \in A,\ a \mathrel{\mathcal{R}} b \to b \mathrel{\mathcal{R}} a$.
3. **Transitiva**: $\forall a, b, c \in A,\ a \mathrel{\mathcal{R}} b \wedge b \mathrel{\mathcal{R}} c \to a \mathrel{\mathcal{R}} c$.

### Cómo se demuestra cada propiedad
- Para **probar** una propiedad hay que hacerlo con elementos genéricos y la definición de la relación.
- Para **refutarla** basta **un contraejemplo** concreto.

> [!example] Ejemplo del libro (se prueba): en $\mathbb{Z}$, $a \mathrel{\mathcal{R}} b$ si $b - a = 3m$ con $m \in \mathbb{Z}$
> - Reflexiva: $a - a = 0 = 3 \cdot 0$.
> - Simétrica: si $b - a = 3m$, entonces $a - b = 3(-m)$.
> - Transitiva: si $b - a = 3m$ y $c - b = 3m'$, entonces $c - a = 3(m + m')$.
>
> (Errata del libro: escribe $3m' - 3m$ al sumar; lo correcto es $c - a = (c-b) + (b-a) = 3m' + 3m = 3(m+m')$.)

> [!example] Ejemplo (se refuta): en $\mathbb{Z}$, $a \mathrel{\mathcal{R}} b$ si $a - b$ es impar
> - No es reflexiva: $a - a = 0$ es par, así que $a \not\mathrel{\mathcal{R}} a$.
> - Basta ese hecho para que no sea de equivalencia. (Tampoco es transitiva: $1 \mathrel{\mathcal{R}} 2$ y $2 \mathrel{\mathcal{R}} 3$, pero $1 \not\mathrel{\mathcal{R}} 3$ porque $1 - 3 = -2$ es par.)

> [!example] Ejemplo (simétrica y reflexiva pero no transitiva): en $\mathbb{Z}$, $a \mathrel{\mathcal{R}} b$ si $|a - b| \leq 1$
> - Reflexiva y simétrica: se ve directamente.
> - No transitiva: $0 \mathrel{\mathcal{R}} 1$ y $1 \mathrel{\mathcal{R}} 2$, pero $0 \not\mathrel{\mathcal{R}} 2$.

> [!warning] Errores típicos
> - Para **probar** la simetría no basta un ejemplo: hay que partir de $a \mathrel{\mathcal{R}} b$ para $a, b$ cualesquiera.
> - Para **refutar** sí basta un único contraejemplo.
> - Comprueba **las tres** propiedades con la definición, no por intuición: una relación puede cumplir dos y fallar la tercera.

## Clases de equivalencia
- **Clase** de $a$: $[a]_{\mathcal{R}} = \{b \in A \mid a \mathrel{\mathcal{R}} b\}$. El elemento $a$ se llama **representante** de la clase.
- Nunca es vacía: $a \in [a]_{\mathcal{R}}$ por la reflexividad.
- **Teorema.** Para $a, b \in A$ son equivalentes:
  1. $a \mathrel{\mathcal{R}} b$.
  2. $[a]_{\mathcal{R}} = [b]_{\mathcal{R}}$.
  3. $[a]_{\mathcal{R}} \cap [b]_{\mathcal{R}} \neq \emptyset$.
- Consecuencia: dos clases son **iguales o disjuntas**. Las clases reparten el conjunto en grupos sin solapes (una **partición**), y cualquier elemento de una clase sirve de representante.

> [!example] Ejemplos del libro
> - Igualdad ($a \mathrel{\mathcal{R}} b$ si $a = b$): cada clase es $[a] = \{a\}$, hay tantas clases como elementos.
> - Múltiplo de 3 en $\mathbb{Z}$: hay **3 clases**, determinadas por el resto al dividir entre 3.
>   - $[0] = \{\ldots, -6, -3, 0, 3, 6, \ldots\}$
>   - $[1] = \{\ldots, -5, -2, 1, 4, 7, \ldots\}$
>   - $[2] = \{\ldots, -4, -1, 2, 5, 8, \ldots\}$
>   - Además $[0] = [3]$, $[1] = [-5]$, $[2] = [11]$.

> [!tip] Cómo calcular las clases
> 1. Toma un elemento genérico $x$ y escribe $[x] = \{y \mid x \mathrel{\mathcal{R}} y\}$.
> 2. Traduce la condición $x \mathrel{\mathcal{R}} y$ a una descripción explícita de $y$ en función de $x$.
> 3. Comprueba para qué valores de $x$ las clases son distintas y cuáles se repiten, para quedarte con **un representante por clase**.

## Enlaces
- [[Algebra-Tema-1.1-Conjuntos]]
- [[Algebra-Tema-1.3-Aplicaciones]]
- [[0_Algebra-Ejercicios-UC1]]
