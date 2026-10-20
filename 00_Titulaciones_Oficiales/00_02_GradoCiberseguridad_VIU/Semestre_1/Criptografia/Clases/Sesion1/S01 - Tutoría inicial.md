---
asignatura: Criptografía (11GCIB)
sesion: 1
tipo: Tutoría inicial
fecha: 2026-10-15
profesora: Amorina González Armayor
email: agonzalezar@professor.universidadviu.com
tags:
  - criptografia
  - sesion
  - cifrado-clasico
  - analisis-frecuencias
  - atbash
  - cesar
  - rot13
  - transposicion
  - book-cipher
  - ctf
---

# Sesión 1 · Tutoría inicial

> [!info] Material relacionado
> Guía docente: [[Guia_docente.pdf]]
> Write-ups de la sesión: [[WriteUp-MagicCrypto.pdf]] · [[WriteUp-Ruta.pdf]] · [[WriteUp-ElLibroDelQuijote.pdf]] · [[WriteUp-NotaCifrada.pdf]]
> Concepto: [[Cifrar vs hashear vs codificar]]

## 1. Organización de la asignatura

Asignatura práctica, centrada en resolver ejercicios. Históricamente no ha habido suspensos salvo por no cumplir con las entregas.

### Evaluación

| Bloque | Peso | Detalle |
|---|---|---|
| Portafolio | 60 % | 90 % actividades · 10 % autoevaluaciones |
| Examen | 40 % | Tipo test, 1 h, con una hoja de papel |

- **Examen:** sin cálculo matemático, todo es descifrar. Tendremos tablas de apoyo a disposición. **Sin IA**: hay que saber resolverlo a mano.
- **Autoevaluaciones:** mezclan teoría y ejercicios, intentos ilimitados hasta enero (fin de clases). Suman pequeños puntos al portafolio.
- **Actividades:** la suma de todas las que se proponen supera los 10 puntos, así que si se pierden puntos en alguna se pueden "recuperar" con otras. El portafolio tiene un máximo de 10.
- Si el portafolio se aprueba en 1.ª convocatoria, se guarda para la 2.ª.
- Todo se entrega por la plataforma. Casi todas las actividades son autocorregibles y se puede usar IA en ellas.
- Los materiales docentes se irán ampliando sesión a sesión. En la tutoría inicial están los enlaces de teoría y actividades.

## 2. Análisis de frecuencias: *El escarabajo de oro* (Poe, 1843)

Fuente: [The Gold-Bug — Public Domain Review](https://publicdomainreview.org/collection/edgar-allan-poes-the-gold-bug-1843/)

![[S01-goldbug-criptograma.png]]

Uno de los personajes descifra el mensaje **contando cuántas veces aparece cada carácter**:

![[S01-goldbug-frecuencias.png]]

**¿Por qué cuenta los caracteres?** Porque en cada idioma unas letras aparecen mucho más que otras. Si el cifrado es una **sustitución monoalfabética** (cada letra siempre se cambia por el mismo símbolo), el símbolo más frecuente del criptograma probablemente corresponde a la letra más frecuente del idioma.

Razonamiento de Poe (en inglés):
1. `8` es el más frecuente (33 veces) → **e**.
2. La palabra más común en inglés es *the*. El trigrama `;48` se repite mucho y acaba en `8` → `;` = **t**, `4` = **h**.
3. A partir de ahí se van completando palabras parciales.

> [!tip] Primer reto: identificar el idioma
> Antes de aplicar frecuencias hay que saber en qué idioma está el texto original. El libro está en inglés, pero a priori no podemos dar por hecho el idioma del mensaje.

> [!example]- Clave completa y texto descifrado
> | Cifrado | 5 | 2 | — | † | 8 | 1 | 3 | 4 | 6 | 0 | 9 | * | ‡ | . | ( | ) | ; | ? | ¶ | : |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
> | Claro | a | b | c | d | e | f | g | h | i | l | m | n | o | p | r | s | t | u | v | y |
>
> *A good glass in the bishop's hostel in the devil's seat forty-one degrees and thirteen minutes northeast and by north main branch seventh limb east side shoot from the left eye of the death's-head a bee-line from the tree through the shot fifty feet out.*
>
> Curiosidad: la tabla del libro no incluye `(`, que aparece 10 veces (es la **r**).

Herramienta: [dCode – Gold-Bug Poe](https://www.dcode.fr/gold-bug-poe). De casi todos los cifrados clásicos hay webs para cifrar y descifrar.

### Las frecuencias no siempre bastan: Wordle

[Wordle (NYT)](https://www.nytimes.com/games/wordle/index.html): adivinar una palabra de 5 letras. **Verde** = letra correcta en su posición · **Amarillo** = está en la palabra, pero en otra posición · **Gris** = no está.

![[S01-wordle.png]]

Con las pistas de la captura: E en 5.ª posición, U en 2.ª, la N está pero no en 1.ª ni 2.ª, y quedan descartadas T, H, R, A, P, Y, I, S. El patrón es `_UN_E` y encajan palabras como *lunge*, *dunce* u *ounce*. La profesora buscó en [Merriam-Webster – 5 letter words containing N, E, U](https://www.merriam-webster.com/wordfinder/classic/contains/all/5/neu/1).

Tabla de frecuencias relativas en inglés: [Emory – English Letter Frequencies](https://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/)

> [!warning] No tomar las frecuencias a rajatabla
> Dependen del tipo de texto con que se calcularon. Un texto de redes sociales (abreviaturas, faltas de ortografía) da estadísticas distintas a un texto literario o periodístico.

## 3. Idiomas por bloques: el caso del coreano

En coreano, chino o japonés los caracteres se forman por bloques. En el hangul cada bloque silábico combina consonantes y vocales, así que las técnicas basadas en letras sueltas no se trasladan directamente.

Vídeo: *Korean Cipher with OpenAI o1*. Los coreanos usan un "cifrado" informal: alteran consonantes y vocales de cada bloque (añadiendo o cambiando la consonante final, duplicando, etc.). Un hablante nativo lo lee sin problema, pero los traductores automáticos no.

![[S01-coreano-gpt4o.png]]
GPT-4o lo interpreta como texto corrupto y no traduce.

![[S01-coreano-o1preview.png]]
o1-preview "razona" en varios pasos (identifica palabras distorsionadas, las reconstruye, traduce) antes de dar la respuesta.

> [!example]- Qué dice el texto
> Normalizado: *지구상 어떤 번역기도 읽을 수 없지만 한국인들은 쉽게 알아볼 수 있는 한글의 암호화 방법이 있다. 모음과 자음의 다양한 변환으로 의미는 유지하면서 표면적으로 다르게 보이게 만드는 방식이다. 인공지능 모델들도 헷갈리게 만들 수 있다.*
>
> Traducción aproximada: «Hay un método de cifrado del hangul que ningún traductor del mundo puede leer pero que los coreanos entienden fácilmente. Mediante transformaciones de vocales y consonantes mantiene el significado pero cambia la apariencia. Puede confundir incluso a los modelos de IA.»

Relación con la IA: en textos traducidos/generados con IA también aparecen incoherencias detectables (por ejemplo, en coreano bloques con vocales donde no tocan; en español, abundancia de guiones). El mismo tipo de incoherencias puede aparecer en textos cifrados.

Vídeo complementario: *How to Build Korean Syllable Blocks | Hangul for Beginners EP.03*.

### ¿Por qué trabajar con varios idiomas?

Hay muchas webs que descifran muchos tipos de cifrado, pero no es fácil hacer algo que descifre **cualquier** mensaje, porque:

1. Hay que conocer todas las técnicas.
2. Hace falta un modelo que reconozca cada idioma.
3. Dentro de un mismo idioma hay variantes: no escribe igual alguien de Argentina, de Cádiz o de Cataluña, ni un texto coloquial que uno de un noticiario.

Recursos:
- Técnicas de análisis de texto (coreano, librerías, carga de PDFs…): [r4ks.com/text](https://r4ks.com/text.html). Haremos cosas en Python, no necesariamente en coreano.
- Comparativa de frecuencias de letras por idioma: [gist de Clifford Anderson](https://gist.github.com/CliffordAnderson/b9b204a6d55b06bedd511326afd3e8b9). Habría que saber con qué tipo de texto se calculó.

Un programa para descifrar textos tiene que tener en cuenta las variables de cada idioma, lo que implica más trabajo.

### Manuscrito Voynich

Vídeo: *The world's most mysterious book – Stephen Bax*. Aquí la dificultad principal es **averiguar el idioma** del texto descifrado.

## 4. Seguridad y organismos de referencia

- Separar el **PC de empresa** del **PC personal**.
- [AEPD – Cómo crear contraseñas robustas](https://www.aepd.es/prensa-y-comunicacion/blog/asi-puedes-crear-contrasenas-robustas-para-proteger-tu-privacidad)
- [NCSC (Reino Unido) – Three random words](https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/three-random-words)
- [NCSC – Guías sobre contraseñas](https://www.ncsc.gov.uk/section/advice-guidance/all-topics?topics=passwords&sort=date%2Bdesc): material que veremos en clase y guías de todo tipo.
- [CCN – Centro Criptológico Nacional](https://www.ccn.cni.es/es/) · [CCN-CERT](https://www.ccn-cert.cni.es/es/)
- [INCIBE](https://www.incibe.es/): noticias, formación y retos. Ruta de los ejercicios: *Inicio › España Digital 2026 › Talento Hacker › Academia Hacker › Retos descargables › Nivel iniciación*.

## 5. Retos resueltos (Academia Hacker INCIBE)

### MagicCrypto · Sustitución espejo (Atbash)
📄 [[WriteUp-MagicCrypto.pdf]]

- **Enunciado:** descifrar el mensaje oculto en `MagicCrypto.jpg` (aparece un espejo y la cadena `GSVUOZTRHHZBWVZIVXIZAB`).
- **Técnica:** Atbash: la 1.ª letra se cambia por la última, la 2.ª por la penúltima… (A↔Z, B↔Y, C↔X). Es su propia inversa: cifrar y descifrar es lo mismo. Fácil de programar y fácil de romper con la técnica adecuada.
- Origen hebreo (álef↔tav, bet↔shin). En español con Ñ el alfabeto tiene 27 letras y la N queda fija.

![[S01-atbash-magiccrypto.png]]

`GSVUOZTRHHZBWVZIVXIZAB` → `THEFLAGISSAYWEARECRAZY` → **Flag: `SAYWEARECRAZY`**

### Ruta · Transposición por ruta en espiral
📄 [[WriteUp-Ruta.pdf]]

- **Enunciado:** la contraseña de un zip está escondida en una imagen de la Ruta 66.
- **Técnica:** transposición. Las letras no cambian, cambian de **posición**. Se escribe el mensaje en una figura geométrica y se lee siguiendo una ruta.
- 49 caracteres y un cartel de 7×7 → cuadrado 7×7. Se escribe de izquierda a derecha por filas y se lee en espiral empezando hacia abajo.
- Cadena: `HNIEUFOICSIGATCR$ODLOIEMSAFMMIAREENOBLETHESLARUTA`
- Descifrado: `HICIMOSLARUTAENMOTOFUEINCREIBLETHEFLAGIS$MAREADOS` → **Flag: `$MAREADOS`**

### El libro del Quijote · Book cipher
📄 [[WriteUp-ElLibroDelQuijote.pdf]]

- **Técnica:** cifrado de libro. Cada coordenada es `página:línea:posición de palabra` en una edición concreta del libro.
- Coordenadas y solución:

| Coordenada | Palabra |
|---|---|
| 10:8:2 | querer |
| 23:10:1 | saber |
| 30:8:2 | noticia |
| 30:26:7 | sobre |
| 35:1:7 | conocer |
| 151:19:10 | misterio |
| 151:11:8 | quien |
| 152:11:5 | hizo |

**Flag: `flag{querer_saber_noticia_sobre_conocer_misterio_quien_hizo}`**

> [!important] Dificultades
> - Hace falta **la misma edición en papel**: las versiones online no tienen número de página. La clave está en un formato (libro físico) y el reto en otro (digital).
> - Si una palabra está partida entre dos líneas, puede contarse en la de arriba o en la de abajo, y eso cambia las posiciones.

Vídeo: *Reto 01 – El libro del Quijote | Academia Hacker INCIBE*.

### Nota cifrada · César / ROT13
📄 [[WriteUp-NotaCifrada.pdf]]

- **Técnica:** cifrado César: cada letra se desplaza un número fijo de posiciones en el alfabeto. **ROT13** es el caso de desplazamiento 13: con 26 letras, aplicarlo dos veces devuelve el original, así que cifrar = descifrar.
- Pista visual: las palabras conservan su longitud y la última línea `synt{…}` tiene forma de flag (`s-13=f, y-13=l, n-13=a, t-13=g` → `flag`).

![[S01-rot13-cryptii.png]]

Texto descifrado: *La siguiente información es confidencial. Te ayudará a proseguir en la investigación. No te confíes, no todas las informaciones de las que disponemos son tan fáciles como esta rotación de caracteres. Firmado: un amigo.*

**Flag: `flag{estamos_empezando_a_conocer_algo_de_historia}`**

Ventajas e inconvenientes del César:
- ✅ Muy sencillo de aplicar a mano (incluso con ruedas o discos de cifrado).
- ❌ Solo hay tantas claves como letras del alfabeto: se rompe probando todas (fuerza bruta) o por frecuencias.
- Se puede **ampliar el alfabeto** (minúsculas, números, símbolos) para aumentar algo la complejidad.

Vídeo: [08 Cifrado César, variante ROT13 básico (Parte 01) | Creación y ruptura de cifrados en Python](https://www.youtube.com/watch?v=1ynyZ1y7pd0&t=3s)

## 6. Herramientas

- [TAMU ITSEC Toolbox](https://toolbox.itsec.tamu.edu/)
- [Cryptii – Caesar cipher](https://cryptii.com/pipes/caesar-cipher/)
- [CyberChef](https://gchq.github.io/CyberChef/) (usado en los write-ups para ROT13 y Atbash)
- [dCode](https://www.dcode.fr/)

En estas herramientas aparecen otros cifrados que veremos más adelante.

## 7. Resumen de conceptos

| Tipo | Qué hace | Ejemplo de la sesión | Cómo se ataca |
|---|---|---|---|
| Sustitución monoalfabética | Cambia cada letra por otro símbolo fijo | Gold-Bug | Análisis de frecuencias |
| Sustitución espejo (Atbash) | A↔Z, B↔Y… | MagicCrypto | Tabla inversa |
| Desplazamiento (César/ROT13) | Mueve cada letra *n* posiciones | Nota cifrada | Fuerza bruta (≤ 26 claves) o frecuencias |
| Transposición por ruta | Reordena las letras según un recorrido | Ruta | Deducir la figura y la ruta |
| Cifrado de libro | Coordenadas a un texto de referencia | El Quijote | Tener el mismo libro/edición |
