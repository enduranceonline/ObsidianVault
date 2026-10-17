---
asignatura: Álgebra
tipo: tema
tema: 1
apartado: "1.3"
sesiones: []
estado: adelantado
material: "[[Algebra_Ciberseguridad.pdf]]"
---

# 1.3 Aplicaciones

> [!info] Nota adelantada
> Aún no se ha visto en clase. Fuente: apartado 1.3 de [[Algebra_Ciberseguridad.pdf]]. Se completará con la sesión correspondiente. Viene de [[Algebra-Tema-1.2-Relaciones]]; se usa en [[0_Algebra-Ejercicios-UC1]].
>
> Convención del libro: $\mathbb{N} = \{1, 2, 3, \ldots\}$ (el $0$ no está en $\mathbb{N}$).

## Aplicación (o función)
Una relación $f$ de $A$ en $B$ es una **aplicación** si
$$\forall a \in A,\ \exists!\, b \in B \text{ tal que } a \mathrel{f} b,$$
es decir, **cada** elemento de $A$ tiene **exactamente un** elemento de $B$ asociado. Se escribe $f : A \to B$ y $f(a) = b$.

- **Dominio**: $\mathrm{Dom}(f) = A$.
- **Imagen** (o recorrido): $\mathrm{Im}(f) = f(A) = \{f(a) \mid a \in A\} \subseteq B$. No tiene por qué ser igual a $B$.
- $B$ es el **codominio** (conjunto de llegada).

> [!warning] Dos formas de que NO sea aplicación
> 1. Un elemento de $A$ con **dos** imágenes (por ejemplo $f(1) = 1$ y $f(1) = 3$).
> 2. Un elemento de $A$ **sin** imagen.
>
> Que un elemento de $B$ no reciba flechas no impide ser aplicación; solo impide ser sobreyectiva.

> [!tip] Comprobación rápida con diagramas de flechas
> Dibuja $A$ a la izquierda y $B$ a la derecha. Es aplicación si **de cada punto de $A$ sale exactamente una flecha**. A cada punto de $B$ pueden llegar 0, 1 o varias.

## 1.3.1 Inyectiva, sobreyectiva y biyectiva

### Inyectiva
$f$ es **inyectiva** si $\forall a, b \in A,\ f(a) = f(b) \to a = b$. Es decir, **no hay dos elementos distintos con la misma imagen**.

- Propiedad (finitos): si $f$ es inyectiva, $|A| = |f(A)|$ y por tanto $|A| \leq |B|$.
- **Para probarla**: supón $f(a) = f(b)$ y deduce $a = b$.
- **Para refutarla**: da dos elementos **distintos** con la misma imagen.

### Sobreyectiva (o suprayectiva)
$f$ es **sobreyectiva** si $f(A) = B$, es decir, $\forall b \in B\ \exists a \in A$ con $f(a) = b$. **Todo elemento de $B$ recibe al menos una flecha.**

- Propiedad (finitos): si $f$ es sobreyectiva, $|A| \geq |B|$.
- **Para probarla**: dado $b \in B$ cualquiera, despeja $a$ en $f(a) = b$ y **comprueba que ese $a$ está en $A$**.
- **Para refutarla**: encuentra un $b \in B$ sin ningún $a$ que cumpla $f(a) = b$.

### Biyectiva
$f$ es **biyectiva** si es inyectiva **y** sobreyectiva: $\forall b \in B\ \exists!\, a \in A$ con $f(a) = b$. Es una correspondencia 1 a 1.

- Propiedad (finitos): si $f$ es biyectiva, $|A| = |B|$.

> [!tip] Atajo con cardinales (solo conjuntos finitos)
> - Si $|A| > |B|$, **no puede ser inyectiva**.
> - Si $|A| < |B|$, **no puede ser sobreyectiva**.
> - Si $|A| \neq |B|$, **no puede ser biyectiva**.
>
> Si $|A| = |B|$ hay que comprobarlo: o es biyectiva o no es ni inyectiva ni sobreyectiva (en finitos, una cosa lleva a la otra).

> [!warning] La sobreyectividad depende del codominio escrito
> $f(x) = 2x$ con $f : \mathbb{Z} \to \mathbb{Z}$ **no** es sobreyectiva (el $1$ no recibe flecha), pero con $f : \mathbb{Z} \to 2\mathbb{Z}$ **sí** lo es. Lee siempre bien el conjunto de llegada y el de salida.

> [!example] Ejemplos de método (no son de la hoja de ejercicios)
> **$h : \mathbb{Z} \to \mathbb{Z}$, $h(n) = 2n$.**
> - Inyectiva: si $2n = 2m$, entonces $n = m$.
> - No sobreyectiva: no existe $n \in \mathbb{Z}$ con $2n = 1$.
>
> **$k : \mathbb{Z} \to \mathbb{Z}$, $k(n) = n + 5$.**
> - Inyectiva: si $n + 5 = m + 5$, entonces $n = m$.
> - Sobreyectiva: dado $y \in \mathbb{Z}$, tomando $n = y - 5 \in \mathbb{Z}$ se tiene $k(n) = y$.
> - Es biyectiva.

## 1.3.2 Composición de aplicaciones
Si $f : A \to B$ y $g : B \to C$, la composición $g \circ f : A \to C$ es
$$(g \circ f)(a) = g(f(a)).$$

- Se **lee de derecha a izquierda**: primero actúa $f$, luego $g$.
- Para que tenga sentido, la imagen de $f$ debe estar dentro del dominio de $g$.
- **Propiedades**:
  1. $f$ y $g$ inyectivas $\Rightarrow$ $g \circ f$ inyectiva.
  2. $f$ y $g$ sobreyectivas $\Rightarrow$ $g \circ f$ sobreyectiva.
  3. $f$ y $g$ biyectivas $\Rightarrow$ $g \circ f$ biyectiva.
- **No es conmutativa** en general: $g \circ f \neq f \circ g$.

> [!example] Ejemplo de método (distinto al de la hoja)
> $f, g : \mathbb{R} \to \mathbb{R}$ con $f(x) = 2x$ y $g(x) = x + 3$.
> - $(g \circ f)(x) = g(2x) = 2x + 3$.
> - $(f \circ g)(x) = f(x + 3) = 2x + 6$.
> - Son distintas: por ejemplo en $x = 0$ valen $3$ y $6$.

> [!tip] Composición con conjuntos finitos
> Calcula la imagen **de cada elemento del dominio** por separado, como hace el libro: $(g \circ f)(a) = g(f(a))$ para cada $a$.

## 1.3.3 Aplicación inversa
- **Identidad**: $\mathrm{Id}_A : A \to A$, $\mathrm{Id}_A(a) = a$.
- **Teorema.** $f : A \to B$ es biyectiva si y solo si existe una **única** $g : B \to A$ con $g \circ f = \mathrm{Id}_A$ y $f \circ g = \mathrm{Id}_B$. Esa $g$ es la **inversa**, $f^{-1}$.
- **Solo existe si $f$ es biyectiva.**

> [!tip] Cómo calcular la inversa
> - **Conjuntos finitos**: invierte las flechas. Si $f(a) = \beta$, entonces $f^{-1}(\beta) = a$.
> - **Con fórmula**: escribe $y = f(x)$, despeja $x$ en función de $y$ y cambia los papeles. **El dominio de $f^{-1}$ es el codominio de $f$.**
> - Ejemplo: $k(n) = n + 5$ da $k^{-1}(y) = y - 5$.

## 1.3.4 Numerabilidad
Una biyección entre conjuntos finitos obliga a igualdad de cardinal. Para infinitos se usa $\mathbb{N}$ como referencia.

- **Definición.** Un conjunto **infinito** $A$ es **numerable** si existe $f : \mathbb{N} \to A$ biyectiva (se pueden "listar" todos sus elementos, sin repetir ni dejar ninguno).
- **Numerables**: $\mathbb{N}$, los pares $2\mathbb{N}$, $\mathbb{Z}$ y $\mathbb{Q}$.
- **No numerable**: $\mathbb{R}$ (argumento de la diagonal de Cantor, 1891).

> [!tip] Cómo demostrar que un conjunto $A$ es numerable
> 1. **Propón** una fórmula $f : \mathbb{N} \to A$ que recorra $A$ en orden. Comprueba con $n = 1, 2, 3, \ldots$ que sale la lista de $A$.
> 2. **Inyectiva**: $f(n) = f(m) \Rightarrow n = m$.
> 3. **Sobreyectiva**: dado $a \in A$, encuentra $n \in \mathbb{N}$ con $f(n) = a$ (y comprueba que $n \geq 1$).
> 4. Concluye: $f$ es biyectiva, luego $A$ es numerable.

> [!example] Ejemplos
> - **Pares** $2\mathbb{N}$ (libro): $f(n) = 2n$. Inyectiva: $2n = 2n' \Rightarrow n = n'$. Sobreyectiva: si $m$ es par, $m = 2n$ para algún $n \in \mathbb{N}$.
> - **$\mathbb{Z}$** (libro): $f(n) = \dfrac{n}{2}$ si $n$ es par y $f(n) = -\dfrac{n-1}{2}$ si $n$ es impar, que para $n = 1, 2, 3, 4, 5, \ldots$ da $0, 1, -1, 2, -2, \ldots$ (alterna no positivos y positivos).
> - **Otro ejemplo** (no es de la hoja): $\{3, 5, 7, 9, \ldots\}$ con $f(n) = 2n + 1$. Da $3, 5, 7, \ldots$ para $n = 1, 2, 3, \ldots$

## Enlaces
- [[Algebra-Tema-1.2-Relaciones]]
- [[Algebra-Tema-2-Combinatoria]]
- [[0_Algebra-Ejercicios-UC1]]
