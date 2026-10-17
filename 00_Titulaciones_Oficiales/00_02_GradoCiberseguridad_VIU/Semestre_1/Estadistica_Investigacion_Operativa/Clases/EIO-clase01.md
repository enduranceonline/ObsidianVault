---
asignatura: Estadística e investigación operativa
tipo: clase
sesion: 1
fecha: 2026-10-14
profesor: Amílcar J. Pérez A.
material: "[[03GCIB-sesión_1.pdf]]"
---

# Clase 01 — Introducción y teoría de conjuntos

## Qué se vio
- Tutoría inicial y presentación del profesor. El profesor fue leyendo la presentación de la sesión (introducción a la asignatura).
- Estadística en ciberseguridad: convertir datos en información útil para detectar, analizar, predecir y responder a amenazas. → [[EIO-Tema-IntroduccionEstadistica]]
- Investigación operativa: optimizar un proceso (costes, tiempos, recursos). Eficacia = lograr el objetivo; eficiencia = lograrlo con el mínimo de recursos.
- Qué es la estadística. Estadística descriptiva vs. inferencial. Población (conjunto) y muestra (subconjunto). Figura 1.2: relación entre probabilidad y estadística inferencial.
- Ejemplos prácticos en ciberseguridad: anomalías de tráfico (promedio diario, desviación estándar, modelo estadístico), fuerza bruta, exfiltración de datos, fraude bancario.
- Idea recurrente del profesor: las conclusiones salen de comparar lo observado con el comportamiento normal (la media) y valorar la probabilidad de esa desviación. Insistió en **entender bien el promedio**; el resto de conceptos se explicarán más adelante.
- Teoría de conjuntos → [[EIO-Tema-TeoriaConjuntos]]
  - Conjunto según Cantor; concepto primitivo en matemáticas.
  - Por **extensión** (diap. 20): listar los elementos. Ej.: $V=\{a,e,i,o,u\}$.
  - Por **comprensión** (diap. 20-21, 23): $A=\{x \mid \varphi(x)\}$, donde $\mid$ = "tal que" y $\varphi(x)$ = propiedad que cumplen los elementos de $A$ **y solo ellos**. Regla mnemotécnica del profesor: comprensión, de *comprender* la propiedad.
    - $P=\{x \mid x \text{ es un planeta del sistema solar}\}$, con $\varphi(x)$ = "$x$ es un planeta del sistema solar".
    - $V=\{x \mid x \text{ es vocal de nuestro alfabeto}\}$.
    - Impares: $I=\{k\in\mathbb{N} \mid k=2n-1,\ n\in\mathbb{N}\}$ (aquí queda confirmada la "I mayúscula").
  - Comprobar la pertenencia (diap. 22): $4\notin I$, porque $4=2n-1 \iff 5=2n \iff n=\tfrac52\notin\mathbb{N}$.
  - Pertenencia y glosario de símbolos: $\in$ (épsilon griega modificada), $\notin$, $\mid$, $\varphi$.
  - Cardinal $|A|$ y cardinales finitos ($\mathbb{N}_0$).
- La clase llegó hasta el cardinal (diap. 24). Faltan por ver en la presentación el conjunto vacío y los elementos sin repetición (diap. 25), que están en las diapositivas.

## Avisos
- Los tests de portafolio serán sobre todo **prácticos** o teoría aplicada a la práctica.
- Test 1 (Conjuntos y Probabilidades): entrega recomendada sáb 07/11/2026; fecha límite 25/01/2027. Examen: 01/02/2027, 18:00. Hay que sacar ≥ 5 en portafolio y en examen por separado.
- Uso de IA en actividades: declararlo y detallarlo (Guía Docente, §4).
- El profesor **aún no ha subido colecciones de ejercicios**.

## Por ampliar (en Temas y Ejercicios)
Anotado como pendiente, sin desarrollar aquí.

**→ [[EIO-Tema-IntroduccionEstadistica]]**
- [ ] Estadística descriptiva vs. inferencial, con ejemplos aplicados.
- [ ] Conceptos citados en los ejemplos: promedio diario, desviación estándar, modelo estadístico (prioridad: promedio).
- [ ] Figura 1.2: probabilidad ↔ inferencia ↔ población/muestra.
- [ ] Explicar mejor los ejemplos de ciberseguridad (diap. 10-13).

**→ [[EIO-Tema-TeoriaConjuntos]]**
- [ ] Definición de Cantor y concepto primitivo.
- [ ] Glosario de símbolos: $\in$, $\notin$, $\mid$, $\varphi$, $|A|$, $\mathbb{N}$, $\mathbb{N}_0$ (el profesor dijo que está descrito arriba; consolidarlo en el tema).
- [ ] Cardinal y cardinales finitos: fórmulas y ejemplos.
- [ ] Recordatorio de tipos de números (no se hizo en clase).
- [ ] Conjunto vacío y elementos sin repetición (de las diapositivas).

## Enlaces
- Presentación: [[03GCIB-sesión_1.pdf]]
- Siguiente: [[EIO-clase02]] (mié 21/10/2026, 18:00-20:00: conjuntos y combinatoria / probabilidades)
- Conexiones: Álgebra y Lógica y matemática discreta (conjuntos, cardinal, $\mathbb{N}$); Criptografía (espacio de claves como conjunto finito).
