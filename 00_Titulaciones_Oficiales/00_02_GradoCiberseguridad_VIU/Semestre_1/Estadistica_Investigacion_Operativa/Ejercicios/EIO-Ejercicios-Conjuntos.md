---
asignatura: Estadística e investigación operativa
tipo: ejercicios
tema: "[[EIO-Tema-TeoriaConjuntos]]"
origen: práctica propia (el profesor aún no ha subido colección de ejercicios)
clase: "[[EIO-clase01]]"
pdf: "[[EIO-Ejercicios-Conjuntos.pdf]]"
estado: 1-5 resueltos y corregidos; 6-7 pendientes
---

# Ejercicios — Teoría de conjuntos

> [!note] Origen
> Los ejercicios 1-5 salen de la comprobación del tema; el 6 y el 7 son extras. No son una colección oficial. Cuando el profesor suba una, se creará una nota nueva y esta quedará como práctica.

## Mi resolución

![[EIO-Ejercicios-Conjuntos.pdf]]


---

## Ejercicios

Cada uno indica la teoría que usa. Las resoluciones están plegadas: intenta primero por tu cuenta.

### 1. Elementos repetidos
Explica por qué $\{a,b,c,c,d,a\}$ y $\{a,b,c,d\}$ son el mismo conjunto y calcula su cardinal.
Teoría: [[EIO-Tema-TeoriaConjuntos#2.3 Sin repeticiones y conjunto vacío (diap. 25)]]

> [!tip]- Resolución
> Un conjunto no tiene elementos repetidos por definición (diap. 25), así que repetir $c$ o $a$ no añade elementos. Ambos son $\{a,b,c,d\}$ y $|A|=4$.

### 2. Pares por comprensión
Escribe por comprensión los naturales pares y di si su cardinal está en $\mathbb{N}_0$.
Teoría: [[EIO-Tema-TeoriaConjuntos#2.1 Por extensión y por comprensión (diap. 19-23)]] y [[EIO-Tema-TeoriaConjuntos#2.2 Cardinal (diap. 24)]]

> [!tip]- Resolución
> $P=\{k\in\mathbb{N}\mid k=2n,\ n\in\mathbb{N}\}=\{2,4,6,\dots\}$ (con $\mathbb{N}$ sin el 0, el primer par es 2).
> $P$ es infinito, así que $|P|\notin\mathbb{N}_0$ (diap. 24). Recuerda que $\mathbb{N}_0$ solo contiene cardinales **finitos**.

### 3. Pertenencia a $I$
Con $I=\{k\in\mathbb{N}\mid k=2n-1,\ n\in\mathbb{N}\}$, comprueba si $9\in I$.
Teoría: [[EIO-Tema-TeoriaConjuntos#2.1 Por extensión y por comprensión (diap. 19-23)]] (ejemplo de la diap. 22)

> [!tip]- Resolución
> $9=2n-1\iff 10=2n\iff n=5$. Como $5\in\mathbb{N}$, entonces $9\in I$. Comprobación: $2\cdot5-1=9$ ✓.

### 4. Log de IP
Un log tiene 5 000 peticiones desde 120 IP distintas. Si $S$ es el conjunto de las IP, ¿cuánto vale $|S|$?
Teoría: [[EIO-Tema-TeoriaConjuntos#3. Aplicación a ciberseguridad (añadido)]]

> [!tip]- Resolución
> $|S|=120$. Las peticiones repetidas desde una misma IP no añaden elementos al conjunto.

### 5. Vacío frente a $\{\varnothing\}$
Calcula $|\varnothing|$ y $|\{\varnothing\}|$ y explica la diferencia.
Teoría: [[EIO-Tema-TeoriaConjuntos#2.3 Sin repeticiones y conjunto vacío (diap. 25)]]

> [!tip]- Resolución
> $|\varnothing|=0$ y $|\{\varnothing\}|=1$. $\varnothing$ no tiene elementos; $\{\varnothing\}$ tiene uno, que es $\varnothing$ (una caja vacía frente a una caja que contiene otra caja vacía).

### 6. Extra: cardinales finitos
Calcula el cardinal de $\{x\in\mathbb{N}\mid x<4\}$ y el de $\{x\in\mathbb{N}_0\mid x<4\}$.

> [!tip]- Pista 1
> Pasa cada conjunto a extensión. ¿Con qué número empieza cada $\mathbb{N}$?
> [!tip]- Pista 2
> Cuenta los elementos de cada lista y compara: la diferencia viene de si entra el 0.

### 7. Extra: ¿$|\mathbb{N}|\in\mathbb{N}_0$?
Justifícalo con la definición de la diap. 24.

> [!tip]- Pista 1
> ¿Es $\mathbb{N}$ finito o infinito? Mira qué cardinales contiene $\mathbb{N}_0$.
> [!tip]- Pista 2
> Recuerda cómo se escribe el cardinal de un conjunto infinito en el curso.

---

## Errores frecuentes (de lo trabajado)

> [!warning] Cardinal de un conjunto infinito
> $\mathbb{N}\subset\mathbb{N}_0$, y $\mathbb{N}_0$ solo contiene cardinales finitos. Un conjunto infinito tiene $|A|\notin\mathbb{N}_0$.

> [!warning] Conclusión de una pertenencia
> Tras despejar $n$, hay que responder a la pregunta original: $n\in\mathbb{N}$ implica que el elemento pertenece a $I$; $n\notin\mathbb{N}$ implica que no.

> [!warning] $\varnothing$ no es $\{\varnothing\}$
> $|\varnothing|=0$ pero $|\{\varnothing\}|=1$.

> [!warning] Sintaxis de comprensión
> Se separa con "tal que" ($\mid$) y la condición adicional con coma: $\{k\in\mathbb{N}\mid k=2n,\ n\in\mathbb{N}\}$.

## Enlaces
- Tema: [[EIO-Tema-TeoriaConjuntos]]
- Clase: [[EIO-clase01]]
