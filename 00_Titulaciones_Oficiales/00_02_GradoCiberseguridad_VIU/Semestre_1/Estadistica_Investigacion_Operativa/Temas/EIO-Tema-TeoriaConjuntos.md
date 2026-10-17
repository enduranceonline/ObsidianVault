---
asignatura: Estadística e investigación operativa
tipo: tema
tema: Teoría de conjuntos
fuentes: "[[03GCIB-sesión_1.pdf]] (diap. 17-25)"
clases: "[[EIO-clase01]]"
estado: sesión 1 cubierta; ampliar con la sesión 2
---

# Teoría de conjuntos

> [!note] Convención de esta nota
> Todo lo que viene de la presentación lleva la referencia (diap. N). Lo marcado como *(añadido)* es ampliación mía que no está en el material del curso.

## 1. Intuición

Un conjunto es una **bolsa sin orden ni duplicados** donde solo importa una cosa: si un objeto está dentro o no. Con eso basta para hablar de "el conjunto de equipos infectados", "los puertos abiertos" o "las claves posibles" *(añadido)*.

Dos preguntas guían todo el tema:
1. ¿Cómo **describo** un conjunto? → extensión o comprensión.
2. ¿Cómo **mido** su tamaño? → cardinal.

## 2. Formalización

> [!definition] Conjunto según Cantor (diap. 17)
> Colección de objetos **definidos y bien diferenciados** (distintos, distinguibles), **concebidos como un todo**. Los objetos se llaman **elementos** y decimos que el conjunto los contiene.

> [!definition] Conjunto y pertenencia (diap. 19)
> Un conjunto es una colección de objetos físicos o abstractos; cada objeto es un **elemento**. Si $A$ es un conjunto:
> - $a\in A$: "$a$ es un elemento de $A$" o "$a$ pertenece a $A$".
> - $a\notin A$: $a$ no pertenece a $A$.
>
> Un conjunto se escribe entre llaves, con los elementos separados por comas.

> [!tip] Concepto primitivo *(añadido)*
> "Conjunto" y "pertenencia" no se definen a partir de otros conceptos, se aceptan como punto de partida. La definición de Cantor es una descripción intuitiva, no una definición formal.

### 2.1 Por extensión y por comprensión (diap. 19-23)

| | Por **extensión** | Por **comprensión** |
|---|---|---|
| Idea | Listar los elementos | Dar la propiedad que los define |
| Forma | $V=\{a,e,i,o,u\}$ | $A=\{x\mid \varphi(x)\}$ |
| Útil cuando | El conjunto es pequeño | El conjunto es grande o infinito |

> [!definition] Comprensión
> $A=\{x\mid\varphi(x)\}$, donde $\mid$ se lee "tal que" y $\varphi(x)$ es la **propiedad** que cumplen los elementos de $A$ **y solo ellos**.
> Es decir: $x\in A \iff \varphi(x)$ es verdadera.

> [!example] Ejemplos de clase (diap. 19-22)
> - $P=\{x\mid x \text{ es un planeta del sistema solar}\}$. Aquí $\varphi(x)$ = "$x$ es un planeta del sistema solar".
> - $V=\{x\mid x \text{ es vocal de nuestro alfabeto}\}=\{a,e,i,o,u\}$.
> - Impares: $I=\{k\in\mathbb{N}\mid k=2n-1,\ n\in\mathbb{N}\}=\{1,3,5,7,\dots\}$.
>
> Comprobar una pertenencia (diap. 22): ¿$4\in I$?
> $4=2n-1\iff 5=2n\iff n=\tfrac52\notin\mathbb{N}$ (numeros naturales), luego $4\notin I$.

> [!tip] Cómo pasar de comprensión a extensión *(añadido)*
> Sustituye $n=1,2,3,\dots$ en la regla. En $I$: $n=1\to1,\ n=2\to3,\ n=3\to5\dots$ Con $\mathbb{N}=\{1,2,3,\dots\}$ el primer impar es 1.

### 2.2 Cardinal (diap. 24)

> [!definition] Cardinal
> El **cardinal** de un conjunto $A$ es su número de elementos, y se denota $|A|$.
> $\mathbb{N}_0:=\{0,1,2,\dots\}$ es el conjunto de los cardinales finitos, y $\mathbb{N}:=\{1,2,3,\dots\}$.
> Si $A$ tiene infinitos elementos, se escribe $|A|\notin\mathbb{N}_0$.

> [!warning] Notación del curso
> Aquí $\mathbb{N}$ **no incluye el 0**; $\mathbb{N}_0$ sí. En otras asignaturas (Álgebra, Lógica y matemática discreta) puede variar. Sigue siempre la de esta asignatura.

> [!example] Ejemplos (diap. 24)
> - $A$ = planetas del sistema solar: $|A|=9$ (la lista de la diapositiva incluye Plutón).
> - $B$ = naturales impares: $|B|\notin\mathbb{N}_0$.
> - *(añadido)* $|\{a,b,c,d\}|=4$.

### 2.3 Sin repeticiones y conjunto vacío (diap. 25)

> [!warning] Sin repetidos
> Los elementos de un conjunto son todos distintos por definición. $\{a,b,c,c,d,a\}$ está mal escrito; lo correcto es $\{a,b,c,d\}$.

> [!definition] Conjunto vacío
> Conjunto sin elementos, denotado $\varnothing$. Ej.: $A$ = satélites de Venus, $A=\varnothing$, ya que Venus no tiene satélites.
> *(añadido)* $|\varnothing|=0$.

> [!warning] *(añadido)* $\varnothing\neq\{\varnothing\}$
> $\{\varnothing\}$ tiene un elemento (el conjunto vacío), así que $|\{\varnothing\}|=1$, mientras que $|\varnothing|=0$.

## 3. Aplicación a ciberseguridad *(añadido)*

- Un log con 10 000 peticiones desde 40 IP distintas: el **conjunto** de IP tiene cardinal 40, no 10 000. Al contar elementos de un conjunto se cuentan los distintos.
- Si no hay equipos infectados, el conjunto de equipos infectados es $\varnothing$.
- Un espacio de claves es un conjunto finito y su cardinal da el coste de la fuerza bruta (conexión con Criptografía).

```python
# Comprobación rápida con Python
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3", "10.0.0.2"]
S = set(ips)                  # elimina repetidos, igual que un conjunto
print(S, len(S))              # |S| = 3

I = {2*n - 1 for n in range(1, 8)}   # comprensión: {1,3,5,...,13}
print(sorted(I), 4 in I)             # 4 no pertenece a I
print(len(set()))                    # conjunto vacío: 0
```

## 4. Conexiones

- **Estadística:** población = conjunto, muestra = subconjunto (ver [[EIO-Tema-IntroduccionEstadistica]]). *(El símbolo de subconjunto $\subseteq$ se verá formalmente más adelante.)*
- **Álgebra y Lógica y matemática discreta:** mismas definiciones, distinta notación según la asignatura.
- **Siguiente en esta asignatura:** combinatoria y probabilidades (ver [[EIO-clase02]]).

## 5. Pendiente de ampliar

- [ ] Subconjuntos, igualdad de conjuntos y operaciones (según se vea en la sesión 2).
- [ ] Cardinal de la unión e intersección (según se vea en la sesión 2).
- [ ] Recordatorio de tipos de números ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$) fuera de clase.
- [ ] Ejercicios cuando el profesor suba colecciones: [[EIO-Ejercicios-Conjuntos]].

## Glosario

| Símbolo                     | Se lee              | Significado                          |
| --------------------------- | ------------------- | ------------------------------------ |
| $\in$                       | pertenece a         | $a\in A$: $a$ es elemento de $A$     |
| $\notin$                    | no pertenece a      | $a\notin A$                          |
| $\mid$                      | tal que             | separa variable y propiedad          |
| $\varphi(x)$                | fi de $x$           | propiedad que cumplen los elementos  |
| $\{\ \}$                    | llaves              | delimitan los elementos del conjunto |
| $\varnothing$               | vacío               | conjunto sin elementos               |
| $\lvert A\rvert$            | cardinal de $A$     | número de elementos                  |
| $\mathbb{N},\ \mathbb{N}_0$ | naturales sin/con 0 | $\{1,2,\dots\}$ y $\{0,1,2,\dots\}$  |
