#dam #python #apuntes
# 🐍 Python Essentials 1 – Fundamentos de Python

# 📘 Módulo 1 – Introducción a la programación

---

### 1.0.1 Aprende Python – El lenguaje de hoy y mañana

- Curso introductorio de Python (1ª parte de 2).
    
- Prepara para la certificación **PCEP – Certified Entry-Level Python Programmer**.
    
- Objetivos: diseñar, escribir, ejecutar, depurar y mejorar programas básicos en Python.

---

### 1.0.2 Acerca del curso

- Creado por **OpenEDG Python Institute** + **Cisco Networking Academy**.
    
- Dirigido a:
    
    - Estudiantes y aspirantes a programadores.
        
    - Desarrolladores junior, analistas de datos, testers.
        
    - Profesionales de IT que quieran conocer Python.
        
    - Líderes y managers que deseen entender el ciclo de desarrollo.
        
- Recursos: laboratorios, evaluaciones, tareas de codificación, desafíos reales.
    

---

### 1.0.3 Plan de estudios

- **Módulo 1:** Introducción a Python y programación informática.
    
- **Módulo 2:** Tipos de datos, variables, entrada/salida, operadores.
    
- **Módulo 3:** Booleanos, condicionales, bucles, listas, operaciones lógicas.
    
- **Módulo 4:** Funciones, tuplas, diccionarios, excepciones, procesamiento de datos.
    

---

### 1.0.4 Certificación PCEP

- Python Essentials 1 está alineado con **PCEP (Certified Entry-Level Python Programmer)**.
    
- Conocimientos validados:
    
    - Variables, operadores, control de flujo, funciones.
        
    - Tipos de datos, excepciones, depuración básica.
        
- **PCEP → PCAP → especializaciones avanzadas.**
    

---

## 🔹 1.1 Introducción a la programación

### 1.1.1 ¿Cómo funciona un programa?

- Una computadora **solo ejecuta operaciones muy simples** (sumar, dividir).
    
- Los programas permiten encadenar esas operaciones para resolver problemas complejos.
    
- Ejemplo (calcular velocidad media):
    
    1. Ingresar distancia.
        
    2. Ingresar tiempo.
        
    3. Dividir distancia/tiempo.
        
    4. Mostrar resultado.
        

---

### 1.1.2 Lenguajes naturales vs. lenguajes de programación

- **Lenguajes naturales:** evolucionan, cambian palabras, se crean expresiones.
    
- **Lenguaje máquina:** lista de instrucciones (IL) propias de la CPU.
    
- Las computadoras **no crean su propio lenguaje**, solo responden a instrucciones predefinidas.
    

---

### 1.1.3 Elementos de un lenguaje

Todo lenguaje (natural o máquina) tiene:

- **Alfabeto** → conjunto de símbolos.
    
- **Léxico** → palabras disponibles.
    
- **Sintaxis** → reglas de combinación.
    
- **Semántica** → significado de las construcciones.
    

---

### 1.1.4 Lenguaje máquina vs. Lenguaje de alto nivel

- **Lenguaje máquina (IL):** “nativo” de la computadora, muy bajo nivel.
    
- **Lenguajes de alto nivel:** puente entre humanos y máquinas (ej: Python, C, Java).
    
- Programa escrito en lenguaje de alto nivel → **código fuente** (archivo `.py`).
    

---

### 1.1.5 Compilación vs. Interpretación

- **Compilación:**
    
    - Traduce todo el código fuente a ejecutable de una vez (`.exe`).
        
    - Ventaja: el programa compilado es independiente del código fuente.
        
- **Interpretación:**
    
    - Traduce y ejecuta línea por línea en tiempo real.
        
    - Ventaja: más flexible, fácil de probar y depurar.
        

👉 Python es un **lenguaje interpretado**.

---

### 1.1.6 El intérprete de Python

- Revisa línea por línea: **leer → verificar → ejecutar**.
    
- Si encuentra un error → muestra mensaje en consola.
    
- Los errores pueden aparecer en un punto distinto de donde se originan.
    

---

### 1.1.7 Ventajas y desventajas

- Python es **interpretado** → requiere tener el **intérprete instalado**.
    
- Lenguajes interpretados → llamados a menudo **lenguajes de scripting**.
    
- Los programas escritos en ellos → **scripts**.
    

---

## 🔹 1.2 Historia de Python

### 1.2.1 ¿Qué es Python?

- Lenguaje **alto nivel, interpretado, orientado a objetos**.
    
- Nombre inspirado en _Monty Python’s Flying Circus_.
    

### 1.2.2 Origen

- Creado en **1989 por Guido van Rossum** (Países Bajos).
    
- Diseñado como proyecto personal en vacaciones de Navidad.
    

### 1.2.3 Objetivos iniciales

- Fácil de aprender e intuitivo.
    
- Open source.
    
- Código legible (similar a inglés).
    
- Adecuado para tareas diarias → rápido desarrollo.
    

---

### 1.2.4 Características clave

- Fácil de **aprender, enseñar, usar, entender**.
    
- Gratuito, open source, multiplataforma.
    

### 1.2.5 Rivales

- **Perl** → más conservador, cercano a C.
    
- **Ruby** → más innovador, lleno de ideas nuevas.
    
- Python → equilibrio entre ambos.
    

---

### 1.2.6 Aplicaciones de Python

- Internet (buscadores, cloud, redes sociales).
    
- Herramientas de desarrollo.
    
- Ciencia y análisis de datos.
    
- Testing de software.
    

### 1.2.7 Limitaciones actuales

- Programación de bajo nivel (drivers, gráficos).
    
- Aplicaciones móviles (aunque hay proyectos experimentales).
    

---

### 1.2.8 Python 2 vs. Python 3

- **Python 2:** legado, mantenimiento básico, sin evolución.
    
- **Python 3:** versión moderna, actualizada, estándar de facto.
    
- **Incompatibles entre sí.**
    

👉 Recomendado: siempre usar **Python 3**.

---

### 1.2.9 Implementaciones de Python

- **CPython** → versión oficial (en C), referencia mundial.
    
- **Cython** → traduce Python a C para mejorar eficiencia.
    
- **Jython** → Python implementado en Java (solo versión 2).
    
- **PyPy** → Python escrito en RPython, usado para probar nuevas características.
    
- **MicroPython** → versión ligera para microcontroladores (ej: placas pyboard).
    

---

## 🔹 1.3 Instalación y primeros pasos

### 1.3.1 Obtener Python

- **Linux:** normalmente ya instalado (`python3`).
    
- **Windows / macOS:** descargar desde [python.org/downloads](https://www.python.org/downloads/).
    

### 1.3.2 Instalación

- En Windows: marcar **“Add Python to PATH”**.
    
- En macOS: suele venir con Python 2 → instalar Python 3 desde `.pkg`.
    

---

### 1.3.3 Herramientas básicas

- **Editor de código** → escribir programas.
    
- **Consola** → ejecutar código.
    
- **Depurador** → analizar paso a paso.
    
- **IDLE (Integrated Development and Learning Environment)** incluido en Python.
    

---

### 1.3.4 Primer programa

1. Crear archivo `snake.py` en IDLE.
    
2. Escribir:
    

```python
print("Hisssssss...")
```

3. Guardar → Run → Run Module (F5).
    
4. Salida esperada:
    

```
Hisssssss...
```

---

### 1.3.5 Errores y depuración

- Eliminar `)` → error de sintaxis (EOF).
    
- Escribir mal `print` → error de nombre (_NameError_).
    
- Python muestra:
    
    - archivo y línea del error,
        
    - tipo de error,
        
    - explicación breve.
        

👉 **Recomendación:** probar, romper y arreglar el código para aprender.

---
Perfecto 🙌 Te armo un **resumen en Markdown** de todas las preguntas y respuestas que vimos, listo para pegar en **Obsidian**.

---

## 📘 Resumen Preguntas – Módulo 1 (Cisco Python Essentials 1)

### ❓ Pregunta 1

**¿Qué es el código máquina?**  
✅ Un lenguaje de programación de bajo nivel que consiste en dígitos/bits binarios que la computadora lee y entiende.

---
### ❓Pregunta 2
**¿Cuáles son los cuatro elementos fundamentales que componen un lenguaje?**
✅ Un alfabeto, un léxico, una sintaxis y una semántica

---

### ❓ Pregunta 3

**¿Cómo se llama a un archivo que contiene un programa escrito en un lenguaje de programación de alto nivel?**  
✅ Un archivo fuente.

---

### ❓ Pregunta 4

**¿Qué es cierto sobre la compilación? (Selecciona dos respuestas)**  
✅ Tiende a ser más rápida que la interpretación.  
✅ El código se convierte directamente en código máquina ejecutable por el procesador.

---

### ❓ Pregunta 5

**¿Cuál es la mejor definición de un _script_?**  
✅ Es un archivo de texto que contiene instrucciones que componen un programa de Python.

---

### ❓ Pregunta 6

**Selecciona las afirmaciones que sean verdaderas (Selecciona dos respuestas):**  
✅ Python es una buena opción para crear y ejecutar pruebas para aplicaciones.  
✅ Python es gratuito, de código abierto y multiplataforma.

---

### ❓ Pregunta 7

**¿Qué es CPython?**  
✅ Es la implementación de referencia predeterminada de Python, escrita en el lenguaje C.

---

### ❓ Pregunta 8

**¿Cómo se llama un intérprete de línea de comandos que te permite interactuar con tu sistema operativo y ejecutar comandos y scripts de Python?**  
✅ Una consola.

---

### ❓ Pregunta 9

**¿Cuál es el comportamiento esperado del siguiente programa?**

```python
print("¡Hola!")
```

✅ El programa mostrará `¡Hola!` en la pantalla.

---
### ❓ Pregunta 10

**¿Cuál es el comportamiento esperado del siguiente programa?**

```python
prin("¡Adiós!")
```

✅ El programa mostrará un mensaje de error en la pantalla.

---

# 📘 Módulo 2 – Tipos de datos, variables, Operaciones Basicas de Entrada y Salida, Operadores Basicos

## 2.1 Sección 1 – El Programa "¡Hola, Mundo!"

### 2.1.1 Tu primer programa
Es hora de comenzar a escribir código real y funcional en Python.  
Por ahora será muy sencillo, pero mostrará conceptos clave.

📌 Ejemplo:
```python
print("¡Hola, Mundo!")
````

- Si todo sale bien, verás la línea de texto en la consola.
    
- Alternativamente, puedes abrir **IDLE**, crear un archivo `.py`, guardar el código y ejecutarlo.
    

El programa consta de las siguientes partes:

1. La palabra `print`
2. Un paréntesis de apertura `(`
3. Una comilla `"`
4. El texto: `¡Hola, Mundo!`
5. Otra comilla `"`
6. Un paréntesis de cierre `)`

Cada elemento cumple una función importante.

---

### 2.1.2 La función `print()`

📌 Ejemplo:

```python
print("¡Hola, Mundo!")
```

- `print` es el **nombre de una función**.
    
- Una función en Python puede:
    
    - **Causar un efecto** → mostrar texto, crear un archivo, reproducir un sonido.
        
    - **Devolver un valor** → como la longitud de un texto o la raíz cuadrada de un número.
        
- Algunas funciones hacen **ambas cosas**.


📍 Origen de las funciones:

- **Integradas en Python** → Ejemplo: `print()`.
    
- **De módulos** → Librerías adicionales, algunas vienen incluidas, otras se instalan.
    
- **Definidas por el usuario** → Puedes crear tus propias funciones con `def`.

---

### 2.1.3 Argumentos de funciones

- Una función puede tener:
    
    - Un efecto.
        
    - Un resultado.
        
    - Uno o más **argumentos**.


📌 Ejemplo:

```python
print("¡Hola, Mundo!")
```

- Los argumentos se colocan **entre paréntesis**.
    
- Si no necesita argumentos, los paréntesis igualmente deben estar presentes (`funcion()`).
    
- En este caso, el argumento es una **cadena de texto** delimitada por comillas `" "` o `' '`.

---

### 2.1.4 Invocación de funciones

📌 Ejemplo general:

```python
function_name(argumentos)
```

Proceso de ejecución:

1. Python busca si la función existe.
2. Comprueba si el número de argumentos es válido.
3. Pasa el control a la función junto con los argumentos.
4. Ejecuta el código de la función.
5. Devuelve el control al programa.

---

### 2.1.5 LAB – Trabajando con la función print()

**Escenario:**

1. Imprime `¡Hola, Mundo!`.
    
2. Imprime tu nombre.
    
3. Elimina las comillas → observa el error.
    
4. Elimina los paréntesis → observa el error.
    
5. Experimenta:
    
    - Usa comillas simples y dobles.
        
    - Usa varias llamadas a `print()` en la misma o diferentes líneas.
        

---

### 2.1.6 La función print() – efecto, argumentos y valores retornados

1. **Efecto** → envía datos a la consola.
    
2. **Argumentos** → acepta casi cualquier tipo de dato (str, int, float, bool, objetos).
    
3. **Valor retornado** → ninguno (`None`).
    

---

### 2.1.7 Instrucciones

- Una invocación de función es un tipo de instrucción en Python.
    
- Regla: **una sola instrucción por línea**.
    
- Una línea vacía es válida, pero no se permiten varias instrucciones en la misma línea (salvo excepciones).
    

📌 Ejemplo:

```python
print("La Witsi Witsi Araña subió a su telaraña.")
print("Vino la lluvia y se la llevó.")
print()
```

---

### 2.1.8 Caracteres de escape y nueva línea

- El carácter `\n` introduce un **salto de línea**.
    
- La barra invertida `\` es un **carácter de escape**.
    

📌 Ejemplo:

```python
print("Hola\nMundo")
```

Salida:

```
Hola
Mundo
```

Reglas:

- Para imprimir `\` → usar `\\`.
    
- No todas las secuencias de escape son válidas.
    

---

### 2.1.9 Usando múltiples argumentos

📌 Ejemplo:

```python
print("La Witsi Witsi Araña", "subió", "a su telaraña.")
```

Salida:

```
La Witsi Witsi Araña subió a su telaraña.
```

- `print()` separa los argumentos con un **espacio automático**.
    

---

### 2.1.10 Argumentos posicionales

- El significado del argumento depende de su **posición**.
    
- Ejemplo: el segundo argumento siempre se mostrará después del primero.
    

---

### 2.1.11 Argumentos de palabra clave

- Se identifican con una **clave = valor**.
    
- Deben ir después de los posicionales.
    

📌 Argumentos más comunes:

- `end` → define qué imprimir al final.
    
- `sep` → define el separador entre argumentos.
    

📌 Ejemplo:

```python
print("Mi", "nombre", "es", "Python.", sep="-", end=" ")
print("Monty Python.")
```

Salida:

```
Mi-nombre-es-Python. Monty Python.
```

---

### 2.1.12 LAB – La función print() y sus argumentos

**Escenario:**

- Modifica el código para usar `sep` y `end`.
    
- Espera la salida:
    

```
Programming***Essentials***in...Python
```

---

### 2.1.13 LAB – Dando formato a la salida

**Ejercicios sugeridos:**

- Usar `\n` para reducir el número de `print()`.
    
- Modificar cadenas con multiplicación (`"texto" * 2`).
    
- Probar errores eliminando comillas, paréntesis o cambiando mayúsculas en `print`.
    

---

### 2.1.14 Resumen de sección

1. `print()` es una función integrada → no requiere importación.
    
2. Python tiene ~69 funciones integradas.
    
3. Para invocar una función → nombre + paréntesis.
    
4. Las cadenas se delimitan con `" "` o `' '`.
    
5. Un programa es una colección de **instrucciones**.
    
6. `\n` produce un salto de línea.
    
7. **Argumentos posicionales** → dependen de su posición.
    
8. **Argumentos de palabra clave** → definidos por `clave=valor`.
    
9. `sep` y `end` permiten personalizar la salida de `print()`.
    

---

### 2.1.15 Cuestionario de sección

**Pregunta 1**

```python
print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")
```

📌 Salida:

```
Mi
nombre
es
Bond. James Bond.
```

**Pregunta 2**

```python
print(sep="&", "fish", "chips")
```

📌 Salida: Error de sintaxis (orden incorrecto de argumentos).

**Pregunta 3** → ¿Cuál da error?

```python
print('Greg\'s book.')       # ✅ válido
print("'Greg's book.'")      # ✅ válido
print('"Greg\'s book."')     # ✅ válido
print("Greg\'s book.")       # ✅ válido
print('"Greg's book."')      # ❌ SyntaxError
```

---
## 2.2 Sección 2 – Literales de Python

### 2.2.1 Literales – los datos en sí mismos
- **Literal**: dato cuyo valor está determinado por su propia notación en el código.
  - `123` → literal (entero).
  - `c` → **no** es literal por sí mismo; es un identificador que necesita contexto.
- Los literales codifican datos dentro del código y `print()` los muestra de forma legible, aunque internamente se almacenan de forma distinta (texto vs. bits numéricos).

Ejemplo:
```python
print("123")
print(123)
````

Ambas líneas **muestran** `123`, pero:

- `"123"` es **cadena**.
    
- `123` es **entero**.

---

### 2.2.2 Enteros

- Tipos numéricos principales: **enteros (int)** y **punto flotante (float)**.
    
- Un entero es una **secuencia de dígitos** sin separadores. Python permite guiones bajos para legibilidad:
    
    - Válidos: `11111111`, `11_111_111`
        
    - Negativos/positivos: `-11_111_111`, `+11111111`

**Bases numéricas:**

- **Octal**: prefijo `0o` / `0O` → solo dígitos `0..7`

```python
print(0o123)   # 83
```

- **Hexadecimal**: prefijo `0x` / `0X`

```python
print(0x123)   # 291
```

---

### 2.2.3 Flotantes

- Representan números con **parte fraccionaria**.
    
    - Ej.: `2.5`, `-0.4`, `4.`, `.4`
        
- **Decimales** usan **punto**, no coma.

**Notación científica (exponente):**

- `3e8` == `3 × 10^8`
    
    - La **base** puede ser entera o flotante; el **exponente** debe ser entero.
        
- Números muy pequeños:

```python
print(6.62607e-34)
```

- Python suele **elegir la forma más corta** al mostrar:

```python
print(0.0000000000000000000001)  # 1e-22
```

**Entero vs flotante:**

- `4` → `int`
- `4.0` → `float` (el punto decide)

---

### 2.2.4 Cadenas

- Texto delimitado por **comillas dobles** `" "` o **apóstrofos** `' '`.
    
    - `"Yo soy una cadena."`
        
- Para incluir comillas dentro del texto:
    
    - Con **escape** `\`:
        
```python
print("Me gusta \"Monty Python\"")
```
        
    - O alternando delimitadores:
        
        
        print('Me gusta "Monty Python"')
        
        
- Para apóstrofes:
    
    - Con escape:
        
```python
print('I\'m Monty Python.')
```
        
    - O con comillas dobles:
        
        
        print("I'm Monty Python.")
        
        
- Cadenas vacías son válidas: `""` o `''`.

---

### 2.2.5 Valores Booleanos

- Representan **veracidad**: `True` y `False` (sensibles a mayúsculas).
- Se comportan como `1` y `0` en contextos numéricos.

Ejemplo:

```python
print(True > False)   # True
print(True < False)   # False
```

---

### 2.2.6 LAB – Literales de Python: Cadenas

**Objetivo:** usar `print()`, secuencias de escape y saltos de línea para obtener:

```
"Estoy"
""aprendiendo""
"""Python"""
```

**Posible solución:**

```python
print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")
```

---

### 2.2.7 Resumen de sección

1. Un **literal** es una notación que representa un **valor fijo**: números (`123`), cadenas (`"hola"`), booleanos (`True/False`), etc.
    
2. Sistemas de numeración:
    
    - **Binario** (base 2), **Octal** (base 8 → `0o`), **Hexadecimal** (base 16 → `0x`).
        
3. **Enteros (`int`)**: sin parte fraccionaria; admiten `_` como separador legible.
    
4. **Flotantes (`float`)**: con parte fraccionaria; pueden usar notación científica (`1.2e-3`).
    
5. Para **comillas/apóstrofes** dentro de cadenas: usar `\` o alternar delimitadores.
    
6. **Booleanos**: `True`, `False` representan valores de verdad (numéricamente `1` y `0`).  
    **Extra:** `None` es un literal especial que indica **ausencia de valor** (`NoneType`).

---

### 2.2.8 Cuestionario de sección

**P1.** ¿Qué tipos de literales son `"Hola "`, `"007"`?

- Ambos son **cadenas**.
    

**P2.** Tipos de `"1.5"`, `2.0`, `528`, `False`

- `"1.5"` → **cadena**
- `2.0` → **float**
- `528` → **int**
- `False` → **booleano**

**P3.** Valor decimal del binario `1011`

- `8 + 0 + 2 + 1 = 11`

---
## 2.3 Sección 3 – Operadores: herramientas de manipulación de datos

### 2.3.1 Python como una calculadora
`print()` no solo muestra literales: también puede **evaluar expresiones**.
```python
print(2 + 2)  # 4
````

➡️ Python puede actuar como calculadora y evaluar expresiones formadas por **valores + operadores**.

---

### 2.3.2 Operadores básicos

**Aritméticos en Python (de uso general):**

- `+` suma
- `-` resta (también unario: cambia el signo)
- `*` multiplicación
- `/` división (siempre devuelve `float`)
- `//` división entera (floor division)
- `%` residuo (módulo)
- `**` exponenciación

**Exponenciación `**`**

```python
print(2 ** 3)     # 8
print(2.0 ** 3)   # 8.0
```

Reglas rápidas:

- int ** int → `int`
    
- si algún operando es `float` → resultado `float`

**Multiplicación `*`**

```python
print(2 * 3)     # 6 (int)
print(2 * 3.0)   # 6.0 (float)
```

**División `/` (siempre float)**

```python
print(1 / 2)   # 0.5
print(2 / 1)   # 2.0  ← aunque sea exacta, es float
```

**División entera `//` (redondea hacia abajo — floor)**

```python
print(3 // 2)     # 1        (int)
print(3 // 2.0)   # 1.0      (float)
print(3 // -2)    # -2       (floor: -1.5 → -2)
print(-3 // 2)    # -2
```

> Siempre “hacia abajo” (al entero **menor o igual**).

**Residuo (módulo) `%`**

```python
print(14 % 4)     # 2
# porque: 14 // 4 = 3 → 3*4 = 12 → 14-12 = 2

print(12 % 4.5)   # 3.0
```

Notas:

- `%` cumple: `a % b == a - b * floor(a/b)`
- El signo del resultado sigue el **divisor** (`b`).

**Suma `+` y resta `-`**

```python
print(5 + 3)    # 8
print(5 - 12)   # -7
print(-7)       # unario; cambia el signo
print(+2)       # unario; no cambia el signo (poco útil)
```

---

### 2.3.3 Operadores y sus prioridades

**Prioridad (de mayor a menor)**

1. `**`
2. `+x`, `-x` (unarios)
3. `*`, `/`, `//`, `%`
4. `+`, `-` (binarios)

**Asociatividad (enlace):**

- La mayoría **izquierda→derecha** (p.ej., `%`, `*`, `/`, `+`, `-`).

```python
print(9 % 6 % 2)  # 1  → (9 % 6) % 2
```

- **Excepción**: `**` es **derecha→izquierda**.

```python
print(2 ** 2 ** 3)  # 256 → 2 ** (2 ** 3)
```

**Cuidado con unario y `**`:**

```python
print(-3 ** 2)     # -9   → -(3 ** 2)
print(-2 ** 3)     # -8   → -(2 ** 3)
print(-(3 ** 2))   # -9
```

**Paréntesis** (siempre se evalúan primero y mejoran legibilidad):

```python
print(2 + 3 * 5)               # 17
print((2 + 3) * 5)             # 25

print(2 * 3 % 5)               # 1  → (2*3)=6; 6%5=1
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# Paso a paso:
# 25 % 13 = 12
# 5 * (12 + 100) = 5 * 112 = 560
# 2 * 13 = 26
# 560 / 26 ≈ 21.538...
# // 2 → 10.0
```

---

### 2.3.4 Resumen de sección

1. **Expresión** = valores/variables + operadores (+ posibles llamadas a funciones) → produce un valor.
2. **Operadores** son símbolos que realizan operaciones sobre valores.
3. Aritméticos: `+`, `-`, `*`, `/`, `%`, `**`, `//`.
    
    - `/` → siempre `float`; `//` → redondea **hacia abajo**.
4. **Unario**: un operando (`-x`, `+x`). **Binario**: dos operandos (`x - y`).
5. **Prioridad**: `**` > unarios `+ -` > `* / // %` > `+ -`.    
6. **Asociatividad**: la mayoría izquierda→derecha; `**` derecha→izquierda.
7. **Paréntesis** dominan el orden de evaluación.

---

### 2.3.5 Cuestionario de sección (respuestas)

**P1**

```python
print((2 ** 4), (2 * 4.), (2 * 4))
# 16 8.0 8
```

**P2**

```python
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
# -0.5 0.5 0 -1
```

**P3**

```python
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
# -2 2 512
```

---
## 2.4 Sección 4 – Variables

### 2.4.1 Variables – cajas con forma de datos
- Una **variable** es un “contenedor” con:
  1) **Nombre** (identificador)
  2) **Valor** (contenido)
- Sirven para **guardar resultados intermedios** y reutilizarlos en nuevas operaciones.

**Idea mental:** variables = cajas con etiqueta (nombre) donde guardas datos que **pueden cambiar**.

---

### 2.4.2 Nombres de variables
**Reglas:**
- Compuestas por letras, dígitos y `_` (guion bajo).
- **Deben empezar** por una letra o `_`.
- **Mayúsculas/minúsculas importan**: `var` ≠ `Var`.
- **No** pueden ser **palabras clave** (reservadas).
- Sin espacios.

**Ejemplos válidos:** `i`, `t34`, `exchange_rate`, `days_to_christmas`, `_`, `Adiós_Señora`  
**Ejemplos inválidos:** `10t`, `!important`, `exchange rate`

**PEP 8 (recomendado):**
- variables y funciones en **minúsculas_con_guiones_bajos**: `my_variable`, `my_function`.

**Palabras clave (no usarlas como nombre):**
`False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield`

> `import` ✗ (prohibido). `Import` ✓ (diferente por mayúscula).

---

### 2.4.3 Cómo crear una variable
- En Python, una variable **se crea al asignarle** un valor (no hay declaración previa).
```python
var = 1
print(var)  # 1
````

- El valor puede ser **de cualquier tipo**: `int`, `float`, `str`, `bool`, etc.

---

### 2.4.4 Cómo emplear una variable

- Puedes crear las que necesites:

```python
a = 10
b = 20
print(a + b)
```

- **Error** si usas una variable **antes** de asignarla:

```python
print(Var)  # NameError (Var no existe)
```

- Concatenar texto y variables (si son cadenas):

```python
ver = "3.13.6"
print("Python version: " + ver)
```

---

### 2.4.5 Cómo asignar un nuevo valor a una variable ya existente

- `=` es **asignación** (no igualdad matemática).
    

```python
var = 1
print(var)  # 1
var = var + 1
print(var)  # 2
```

- Se evalúa la **derecha** y se guarda en la **izquierda**.
    

```python
var = 100
var = 200 + 300
print(var)  # 500
```

---

### 2.4.6 Resolviendo problemas matemáticos simples (Pitágoras)

```python
a = 3.0
b = 4.0
c = (a**2 + b**2) ** 0.5  # √(a^2 + b^2)
print("c =", c)  # c = 5.0
```

---

### 2.4.7 LAB – Variables

**Tarea:**

1. Crea `john`, `mary`, `adam` con 3, 5 y 6.
2. Imprímelos en una línea separados por comas.
3. Crea `total_apples = john + mary + adam` e imprímelo.
4. Experimenta con operaciones y concatenación de texto.

**Posible solución:**

```python
john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=", ")
total_apples = john + mary + adam
print("Número total de manzanas:", total_apples)
```

---

### 2.4.8 Operadores abreviados (asignación compuesta)

Patrón:

```
variable = variable op expresión   →   variable op= expresión
```

Ejemplos:

```python
x = 1
x = x * 2   # →
x *= 2

sheep = 0
sheep = sheep + 1  # →
sheep += 1

x -= 3
x /= 5
x //= 2
x %= 7
x **= 2
```

---

### 2.4.9 LAB – Variables: un convertidor simple

**Dato:** `1 milla ≈ 1.61 km`.

**Objetivo:** completar conversiones **mi→km** y **km→mi** y usar `round()`.

**Posible solución:**

```python
miles = 7.38
km = 12.25

# millas → km
miles_to_km = miles * 1.61
print(miles, "millas son", round(miles_to_km, 2), "kilómetros")

# km → millas
km_to_miles = km / 1.61
print(km, "kilómetros son", round(km_to_miles, 2), "millas")
```

_Salida esperada:_  
`7.38 millas son 11.88 kilómetros`  
`12.25 kilómetros son 7.61 millas`

---

### 2.4.10 LAB – Operadores y expresiones

Expresión: `3x^3 - 2x^2 + 3x - 1`

```python
x = float(input("x = "))
y = 3*(x**3) - 2*(x**2) + 3*x - 1
print("y =", y)
```

Prueba con `x = 0 → y = -1.0`, `x = 1 → y = 3.0`, `x = -1 → y = -9.0`.

---

### 2.4.11 Resumen de sección

- Una **variable** es un nombre que referencia un valor en memoria; **se crea al asignar**.
    
- Identificadores: sin espacios, empiezan por letra/_ , distinguen mayúsculas; no palabras clave.
    
- Python es **dinámico**: no hay declaración previa; se usa `=` para asignar.
    
- **Asignación compuesta**: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.
    
- Puedes **combinar texto y variables** con `+` (si son `str`) o con `print()` pasando múltiples argumentos.
    

---

### 2.4.12 Cuestionario de sección (respuestas)

**P1**

```python
var = 2
var = 3
print(var)      # 3
```

**P2** (elige tres ilegales):

- `101` (empieza con dígito) ✅ **ilegal**
    
- `m 101` (espacio) ✅ **ilegal**
    
- `del` (palabra clave) ✅ **ilegal**  
    `my_var`, `m`, `averylongVariablename`, `m101`, `Del` → **legales**
    

**P3**

```python
a = '1'
b = "1"
print(a + b)    # 11  (concatenación de cadenas)
```

**P4**

```python
a = 6
b = 3
a /= 2 * b      # a = 6 / 6 → 1.0
print(a)        # 1.0
```

---
## 2.5 Sección 5 – Comentarios

### 2.5.1 Comentarios – ¿por qué, cuándo y dónde?
- **Comentarios**: texto en el código **ignorado por Python** durante la ejecución. Sirven para explicar el “qué” y el “por qué” del código, documentar autoría/fecha, aclarar decisiones y significados de variables.
- En Python, un comentario **empieza con `#`** y se extiende **hasta el final de la línea**.

```python
# Este programa evalúa la hipotenusa c.
# a y b son las longitudes de los catetos.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # Se emplea ** en lugar de sqrt.
print("c =", c)
````

**Buenas prácticas:**

- Nombres **autoexplicativos** > comentarios redundantes.
    
    - ✅ `square_area` mejor que ❌ `aunt_jane`.
- Comenta **intención y supuestos**, no lo obvio.
    
- Mantén los comentarios **actualizados** (un comentario incorrecto confunde más que ayuda).

> Nota: Las _triple comillas_ (`"""..."""`) crean **cadenas** (docstrings si se ubican como primer elemento en módulos/clases/funciones). No son “comentarios” per se, aunque a veces se usan como bloques de texto desactivados. Prefiere `#` para comentar.

---

### 2.5.2 Marcar fragmentos de código

Puedes **deshabilitar** temporalmente líneas para probar o aislar errores:

```python
# Este es un programa de prueba.
x = 1
y = 2
# y = y + x
print(x + y)  # 3
```

**Atajo útil (editores comunes):**

- Comentar/descomentar selección: **Ctrl + /** (Windows/Linux), **Cmd + /** (macOS).

---

### 2.5.3 LAB – Comentarios (mejora y refactor)

**Objetivo:** mejorar legibilidad:

- Añade/quita comentarios donde aporten valor.
    
- Renombra variables con nombres claros (PEP 8: `snake_case`).
    
- Considera extraer trozos a funciones con **docstrings** breves que indiquen propósito y parámetros.

**Ejemplo antes (pobre):**

```python
# calc
a = 3.0
b = 4.0
c = (a**2 + b**2)**0.5
print(c)
```

**Ejemplo después (mejor):**

```python
# Calcula la hipotenusa (teorema de Pitágoras).
cateto_a = 3.0
cateto_b = 4.0
hipotenusa = (cateto_a**2 + cateto_b**2) ** 0.5
print("c =", hipotenusa)
```

---

### 2.5.4 Resumen de sección

- Un **comentario** comienza con `#` y llega hasta el fin de línea.
    
- Para “multilínea”, **coloca `#` en cada línea**.
    
- Úsalos para:
    
    - aclarar intención, supuestos y decisiones,
        
    - desactivar fragmentos durante pruebas.
        
- Prefiere **variables autoexplicativas** y **código claro** antes que comentar cada línea.
    
- Mantén los comentarios **correctos y actualizados**.

**Ejemplo:**

```python
# Este programa imprime
# una introducción en la pantalla.
print("¡Hola!")  # Invocando a print()
# print("Soy Python.")  # Desactivado en pruebas
```

---

### 2.5.5 Cuestionario de sección (respuestas)

**P1. ¿Salida?**

```python
# print("Cadena #1")
print("Cadena #2")
```

**Respuesta:**

```
Cadena #2
```

**P2. ¿Qué pasa al ejecutar?**

```python
#Este es
un comentario
multilínea.#

print("¡Hola!")
```

**Respuesta:**

- `#Este es` es un comentario **solo hasta el fin de su línea**.
    
- La línea `un comentario` **no** empieza con `#` → Python intenta interpretarla como código y producirá un **NameError** (o SyntaxError según el contenido/espacios).
    
- **Corrección** para multilínea con `#`:

```python
# Este es
# un comentario
# multilínea.
print("¡Hola!")
```

---
## 2.6 Sección 6 – Interacción con el usuario

### 2.6.1 La función input()
- `print()` → envía datos a la consola.  
- `input()` → obtiene datos de la consola.  

```python
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")
````

Notas:

- `input()` espera datos del usuario y devuelve lo escrito.
- Siempre **devuelve una cadena (`str`)**.
- Si no se asigna a una variable, los datos se pierden.

---

### 2.6.2 input() con argumento

Puedes mostrar un mensaje directamente dentro de `input()`:

```python
anything = input("Dime lo que sea... ")
print("Hmm...", anything, "... ¿en serio?")
```

---

### 2.6.3 El resultado de input()

- El **resultado siempre es `str`**.
- No puede usarse directamente en operaciones matemáticas.

```python
anything = input("Ingresa un número: ")
something = anything ** 2.0   # ❌ Error: str no puede elevarse
```

---

### 2.6.4 Operaciones prohibidas

Ejemplo de error:

```python
anything = input("Ingresa un número: ")
something = anything ** 2.0
```

Salida:

```
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
```

---

### 2.6.5 Conversión de tipos

Usa **`int()`** y **`float()`** para convertir cadenas numéricas:

```python
num = int(input("Ingresa un número entero: "))
print("Tu número al cuadrado es:", num ** 2)

flt = float(input("Ingresa un número decimal: "))
print("Mitad de tu número es:", flt / 2)
```

---

### 2.6.6 Más sobre input() y conversión

Reescribiendo el programa del teorema de Pitágoras con entrada del usuario:

```python
a = float(input("Ingresa cateto a: "))
b = float(input("Ingresa cateto b: "))
print("Hipotenusa =", (a**2 + b**2) ** 0.5)
```

> Nota: no maneja errores (ej. números negativos). Lo veremos más adelante.

---

### 2.6.7 Operadores cadena

**Concatenación (`+`)**

```python
print("Hola, " + "mundo")  # Hola, mundo
```

**Replicación (`*`)**

```python
print("Python! " * 3)   # Python! Python! Python!
print("2" * 5)          # 22222
```

> Si el número ≤ 0 → resultado = cadena vacía.

---

### 2.6.8 Conversión de tipos una vez más

**`str()`** convierte números a cadenas:

```python
a = 3
b = 4
c = (a**2 + b**2) ** 0.5
print("La hipotenusa es " + str(c))
```

---

### 2.6.9 LAB – Entradas y salidas simples

**Escenario:** completar el código para evaluar las 4 operaciones básicas:

- suma, resta, multiplicación, división.

Ejemplo de solución:

```python
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
```

---

### 2.6.10 LAB – Operadores y expresiones

Completar el código para evaluar una expresión compleja (usa `()` para controlar la prioridad).  
Datos de prueba:

- `x = 1` → `y = 0.6000000000000001`
- `x = 10` → `y = 0.09901951266867294`
- `x = 100` → `y = 0.009999000199950014`
- `x = -5` → `y = -0.19258202567760344`

---

### 2.6.11 LAB – Operadores y expresiones 2

**Escenario:** calcular la hora de finalización de un evento.

- Entrada: hora, minutos, duración en minutos.
- Salida: hora final en formato `HH:MM`.

Ejemplo:

```
Entrada: 12 17 59 → Salida: 13:16
Entrada: 23 58 642 → Salida: 10:40
```

Sugerencia: usar operador `%` para manejar ciclos de 24h y 60m.

---

### 2.6.12 Resumen de sección

1. `print()` muestra datos; `input()` los obtiene.
2. `input([mensaje])` puede mostrar un mensaje antes de leer.
3. `input()` detiene la ejecución hasta que el usuario escriba algo y presione Enter.
4. `input()` siempre devuelve un `str`.
5. Para cálculos: convertir con `int()` o `float()`.
6. Operadores con cadenas:
    - `+` → concatenación
    - `*` → replicación
7. `str()` convierte números a texto.

---

### 2.6.13 Cuestionario de sección (respuestas)

**P1**

```python
x = int(input("Ingresa un número: "))  # Usuario ingresa 2
print(x * "5")
```

- `x = 2` (entero).
- `"5"` (cadena).
- Resultado: `"55"` (replicación de cadena).

**P2**

```python
x = input("Ingresa un número: ")  # Usuario ingresa 2
print(type(x))
```

- `input()` devuelve **cadena**.
- Resultado: `<class 'str'>`

```

---

¿Quieres que continúe con el **Módulo 3 – Control de flujo: loops y condiciones**, siguiendo el mismo nivel de detalle?
```

---
## 2.7 Finalización del Módulo 2 – QUIZ DEL MÓDULO

### ❓Pregunta 1
**El dígrafo `\n` obliga a la función `print()` a:**
- ✅ realizar un salto de línea  
- ❌ imprimir exactamente dos caracteres: `\` y `n`  
- ❌ detener su ejecución  
- ❌ duplicar el carácter al lado del dígrafo  

**Justificación:** `\n` es una **secuencia de escape** que inserta un **salto de línea**. No imprime los símbolos literales `\` y `n`, no detiene el programa ni duplica caracteres.

---

### ❓Pregunta 2
**El significado del parámetro de palabra clave está determinado por:**
- ❌ su conexión con las variables existentes  
- ❌ su posición dentro de la lista de argumentos  
- ✅ el nombre del argumento especificado junto con su valor  
- ❌ es valioso  

**Justificación:** Los **argumentos de palabra clave** se identifican por su **nombre** (`clave=valor`), no por su posición.

---

### ❓Pregunta 3
**Veinte punto doce por diez elevado a la potencia de ocho se escribe como:**
- ❌ `20.12*10^8`  
- ❌ `20.12E8.0`  
- ✅ `20.12E8`  
- ❌ `20E12.8`  

**Justificación:** En notación científica de Python se usa `E`/`e` con exponente **entero**: `20.12E8`. Las otras opciones no son sintaxis válida.

---

### ❓Pregunta 4
**El prefijo `0o` indica que el número es:**
- ❌ binario  
- ❌ decimal  
- ✅ octal  
- ❌ hexadecimal  

**Justificación:** `0b`→binario, `0o`→**octal**, `0x`→hexadecimal, sin prefijo→decimal.

---

### ❓Pregunta 5
**El operador `**`:**
- ❌ realiza multiplicaciones duplicadas  
- ❌ realiza la multiplicación de punto flotante  
- ✅ realiza exponenciación  
- ❌ no existe  

**Justificación:** `a ** b` eleva `a` a la **potencia** `b`. No es un multiplicador “duplicado”.

---

### ❓Pregunta 6
**Resultado de `1 / 1`:**
- ❌ `1`  
- ✅ `1.0`  
- ❌ no se puede predecir  
- ❌ no puede ser evaluado  

**Justificación:** `/` **siempre** devuelve `float` en Python 3, incluso si la división es exacta.

---

### ❓Pregunta 7 _(elige dos)_
**¿Cuáles afirmaciones son verdaderas?**
- ❌ La suma precede a la multiplicación.  
- ✅ El operador `**` utiliza el enlazado del **lado derecho**.  
- ❌ El resultado de `/` es siempre un valor entero.  
- ✅ El argumento a la derecha de `%` **no puede ser cero**.  

**Justificación:**  
- Multiplicación tiene **mayor prioridad** que la suma.  
- `a ** b ** c` → `a ** (b ** c)` (derecha→izquierda).  
- `/` retorna **float**.  
- `a % 0` produce `ZeroDivisionError`.

---

### ❓Pregunta 8
**El enlazado izquierdo determina el resultado de: `1 // 2 * 3`**
- ❌ `0.16666666666666666`  
- ❌ `4.5`  
- ❌ `0.0`  
- ✅ `0`  

**Justificación:** `//` y `*` tienen la misma prioridad y se evalúan **izquierda→derecha**: `1 // 2 = 0`; luego `0 * 3 = 0`.

---

### ❓Pregunta 9 _(elige dos)_
**¿Cuáles nombres de variables son ilegales?**
- ✅ `True`  
- ✅ `and`  
- ❌ `TRUE`  
- ❌ `true`  

**Justificación:** `True` (constante booleana) y `and` (palabra clave) son **reservados**. `TRUE`/`true` son distintos por mayúsculas/minúsculas y no están reservados.

---

### ❓Pregunta 10
**La función `print()` puede imprimir:**
- ❌ solo un argumento  
- ❌ cualquier cantidad de argumentos (excluyendo ninguno)  
- ✅ cualquier cantidad de argumentos (**incluyendo ninguno**)  
- ❌ no más de cinco argumentos  

**Justificación:** `print()` acepta **0 o más** argumentos. Con 0 imprime solo un salto de línea.

---

### ❓Pregunta 11
```python
x = 1
y = 2
z = x
x = y
y = z
print(x, y)
````

- ❌ `1 2`
    
- ✅ `2 1`
    
- ❌ `2 2`
    
- ❌ `1 1`
    

**Justificación:** Se intercambian los valores usando `z` como temporal: `x=2`, `y=1`.

---

### ❓Pregunta 12

```python
x = input()   # 2
y = input()   # 4
print(x + y)
```

- ❌ `6`
    
- ❌ `4`
    
- ✅ `24`
    
- ❌ `2`
    

**Justificación:** `input()` devuelve **cadenas**, y `+` entre cadenas **concatena**: `"2" + "4" = "24"`.

---

### ❓Pregunta 13

```python
x = int(input())  # 2
y = int(input())  # 4
x = x // y        # 0
y = y // x        # 4 // 0 → ?
print(y)
```

- ❌ `4.0`
    
- ❌ `8.0`
    
- ❌ `2.0`
    
- ✅ el código causará un **error de ejecución**
    

**Justificación:** `y // x` intenta dividir entre **0** → `ZeroDivisionError`.

---

### ❓Pregunta 14

```python
x = int(input())  # 2
y = int(input())  # 4
x = x / y         # 0.5
y = y / x         # 4 / 0.5 = 8.0
print(y)
```

- ❌ el código causará un error de ejecución
    
- ❌ `4.0`
    
- ❌ `2.0`
    
- ✅ `8.0`
    

**Justificación:** Con `/` no hay división por cero aquí; el resultado final es `8.0`.

---

### ❓Pregunta 15

```python
x = int(input())  # 11
y = int(input())  # 4
x = x % y         # 3
x = x % y         # 3 % 4 = 3
y = y % x         # 4 % 3 = 1
print(y)
```

- ✅ `1`
    
- ❌ `2`
    
- ❌ `3`
    
- ❌ `4`

**Justificación:** El último residuo es `1`.

---

### ❓Pregunta 16

```python
x = input()       # "3"
y = int(input())  # 6
print(x * y)
```

- ❌ `666`
    
- ❌ `18`
    
- ❌ `36`
    
- ✅ `333333`
    

**Justificación:** Cadena por entero → **replicación**: `"3" * 6` → `"333333"`.

---

### ❓Pregunta 17

```python
z = y = x = 1
print(x, y, z, sep='*')
```

- ✅ `1*1*1`
    
- ❌ `x y z`
    
- ❌ `x*y*z`
    
- ❌ `1 1 1`
    

**Justificación:** Asignación múltiple pone `1` en las tres variables; `sep='*'` usa `*` como separador.

---

### ❓Pregunta 18

```python
y = 2 + 3 * 5.
print(Y)
```

- ❌ `17.0`
    
- ❌ `25.`
    
- ❌ `17`
    
- ✅ el fragmento provocará un **error de ejecución**
    

**Justificación:** La expresión vale `17.0`, pero se imprime `Y` (mayúscula). `y` ≠ `Y` → `NameError`.

---

### ❓Pregunta 19

```python
x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)
```

- ❌ `8`
    
- ❌ `8.5`
    
- ✅ `17.5`
    
- ❌ `17`
    

**Justificación:** `4**2=16`; `1/2=0.5`; `3//3=1`; suma: `0.5 + 1 + 16 = 17.5`.

---

### ❓Pregunta 20

```python
x = int(input())  # 2
y = int(input())  # 4
print(x + y)
```

- ✅ `6`
    
- ❌ `4`
    
- ❌ `24`
    
- ❌ `2`
    

**Justificación:** Se convierten a `int` y se suman: `2 + 4 = 6`.

---

# 📘 Módulo 3 – Valores Booleanos, Ejecución Condicional, Bucles, Listas y Operaciones Lógicas/Bit a Bit

## **Sección 3.1 – Cómo tomar decisiones en Python**

---
### 3.1.1 Preguntas y Respuestas

- Los programas hacen **preguntas** y reciben **respuestas booleanas**: `True` o `False`.
- Esas respuestas se usan para decidir qué instrucción ejecutar después.

---

### 3.1.2 Comparación: operador de igualdad

#### Igualdad vs. asignación

- = → **asignación** (pone un valor en una variable): 
>a = b.
- == → **comparación** (pregunta si dos valores son iguales): 
>a == b.

#### Propiedades

- Operador **binario** con **enlace a la izquierda**.
- Devuelve `True` si los valores son iguales; `False` si no.
- Compara **valores**; Python permite comparar `int` y `float` si su valor numérico coincide:
```python
2 == 2.0    # True
```

---

### 3.1.3 Ejercicios — Respuestas justificadas

#### Pregunta #1

**Código:**

```python
2 == 2
```

**Respuesta:** `True`  
**Por qué:** ambos operandos son enteros con el mismo valor, así que la igualdad se cumple.

---

#### Pregunta #2

**Código:**

```python
2 == 2.
```

**Respuesta:** `True`  
**Por qué:** `2` (entero) y `2.` (flotante) representan el **mismo valor numérico**. Python convierte internamente para compararlos como números, y la comparación resulta verdadera.

---

#### Pregunta #3

**Código:**

```python
1 == 2
```

**Respuesta:** `False`  
**Por qué:** los valores son distintos; la igualdad no se cumple.

---

### 3.1.4 Otros operadores de comparación (resumen rápido)

- `!=` → distinto de
    
- `>` → mayor que
    
- `>=` → mayor o igual que
    
- `<` → menor que
    
- `<=` → menor o igual que
    

Todos son binarios, con **enlace a la izquierda** y **mayor prioridad** que == / !=

**Ejemplo de prioridad:**

```python
black_sheep == 2 * white_sheep    # Se evalúa como black_sheep == (2 * white_sheep)
```

---

### 3.1.5 Usando las respuestas

- Se puede **guardar** el resultado en una variable:

```python
answer = lions >= lionesses
```

- O usarlo **directamente** en una sentencia condicional (verás `if`, `elif`, `else` a continuación en la sección).

---

#### Mini-chuletas y trampas comunes

- **No confundas** = con ==
- `2 == 2.0` → `True` (comparación por valor, no por tipo).
- Cuidado con **flotantes no exactos** (p. ej., `0.1 + 0.2 == 0.3` puede ser `False` por representación binaria).
- La comparación de cadenas es **lexicográfica** y sensible a mayúsculas.

---

Si quieres, ahora remato esta misma estructura con las subsecciones 3.1.6–3.1.14 (labs y quiz) igual de ordenadas y con soluciones justificadas.
### 3.1.3 Ejercicios (rápidos)

- `2 == 2` → **True**
- `2 == 2.` → **True**
- `1 == 2` → **False**

---

### 3.1.4 Operadores de comparación

#### Igualdad / Desigualdad

- `a == b` → `True` si **son iguales**.
- `a != b` → `True` si **son diferentes**.

```python
var = 0
print(var == 0)   # True
print(var != 0)   # False

var = 1
print(var != 0)   # True
```

#### Orden

- `>`, `>=`, `<`, `<=` (binarios, asociatividad izquierda).

```python
black_sheep > white_sheep
centigrade_outside >= 0.0
current_velocity_mph < 85
current_velocity_mph <= 85
```

#### Prioridad (actualizada)

1. `**` (derecha→izquierda)
2. `+x`, `-x` (unarios)
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. `< <= > >=`
6. == !=

> Igualdad/desigualdad tienen **menor** prioridad que `<, <=, >, >=`.

---

### 3.1.5 Haciendo uso de las respuestas

- Puedes **guardar** la respuesta:
```python
answer = number_of_lions >= number_of_lionesses
```

- O **decidir** con ella (sentencias condicionales, ver 3.1.7).

---

### 3.1.6 LAB – Variables: Preguntas y Respuestas

**Objetivo:** leer `n` (int) e imprimir `False` si `n < 100` y `True` si `n >= 100`, **sin** `if`.

```python
n = int(input())
print(n >= 100)
```

---

### 3.1.7 Condiciones y ejecución condicional

#### if (básico)

```python
if condition:
# bloque con sangría (4 espacios recomendados)
do_something()
```

- Se ejecuta el bloque **solo si** `condition` es verdadera (no cero / no vacío).
- **No mezcles** tabs y espacios.

#### if / else

```python
if the_weather_is_good:
    go_for_a_walk()
else:
    go_to_a_theater()
have_lunch()  # siempre se ejecuta
```

#### if anidados

```python
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()
```

- Cada `else` pertenece al `if` del **mismo nivel de sangría**.

#### if / elif / else (cascada)

```python
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()
```

- Se ejecuta **la primera** rama cuya condición sea `True`.
- `else` es **opcional** y siempre va **al final**.

---

### 3.1.8 Análisis de muestras de código

#### Mayor de dos números

```python
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

if n1 > n2:
    larger = n1
else:
    larger = n2

print("El número más grande es:", larger)
```

> **One-liner** válido pero menos legible:  
> `if n1 > n2: larger = n1; else: larger = n2`

#### Mayor de tres números (hipótesis + actualización)

```python
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

largest = n1
if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3

print("El número más grande es:", largest)
```

> Alternativa (cuando te sea permitido): `largest = max(n1, n2, n3)`

---

### 3.1.9 Pseudocódigo e introducción a los bucles (valor centinela)

**Idea:** repetir lectura y actualización hasta que llegue un **centinela** (`-1`).

**Versión Python:**

```python
largest = -999_999_999
while True:
    number = int(input())
    if number == -1:
        break
    if number > largest:
        largest = number
print(largest)
```

---

### 3.1.10 LAB – Comparación y ejecución condicional (Espatifilo)

**Requisitos:**

- `"ESPATIFILIO"` → `Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!`
- `"espatifilo"` → `No, ¡quiero un gran Espatifilo!`
- Otros → `¡Espatifilo!, ¡No <entrada>!`

**Solución:**

```python
name = input()

if name == "ESPATIFILIO":
    print("Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif name == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print(f"¡Espatifilo!, ¡No {name}!")
```

---

### 3.1.11 LAB – Fundamentos de `if-else` (Impuesto)

**Reglas:**

- `ingreso <= 85_528`: impuesto = `0.18*ingreso - 556.02`
- `ingreso > 85_528`: impuesto = `14839.02 + 0.32*(ingreso - 85_528)`
- Si el impuesto < 0 → **0** (no hay devoluciones).
- Imprime **redondeado a pesos**.

**Solución:**

```python
ingreso = float(input())

if ingreso <= 0:
    impuesto = 0.0
elif ingreso <= 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = 14839.02 + (ingreso - 85528) * 0.32

if impuesto < 0:
    impuesto = 0.0

print("El impuesto es:", round(impuesto, 0), "pesos")
```

---

### 3.1.12 LAB – Fundamentos de `if-elif-else` (Año bisiesto)

**Regla gregoriana (desde 1582):**

1. Si `año % 4 != 0` → **común**
2. elif `año % 100 != 0` → **bisiesto**
3. elif `año % 400 != 0` → **común**
4. else → **bisiesto**

**Solución:**

```python
year = int(input())

if year < 1582:
    print("No dentro del período del calendario gregoriano")
else:
    if year % 4 != 0:
        print("Año comun")
    elif year % 100 != 0:
        print("Año bisiesto")
    elif year % 400 != 0:
        print("Año comun")
    else:
        print("Año bisiesto")
```

---

### 3.1.13 RESUMEN DE SECCIÓN

- Los **operadores de comparación** devuelven True/False: == , != , < , <= , > , >=
- Úsalos para **decidir** con `if`/`elif`/`else`. La **sangría** define el bloque.
- En una cascada `if-elif-else`, se ejecuta **solo la primera** condición `True`. `else` es opcional.
- **Prioridad** (parcial): `**` → unarios `+ -` → `* / // %` → `+ -` → `< <= > >=` → == !=

---

### 3.1.14 QUIZ DE SECCIÓN – Respuestas y justificación

#### P1

```python
x = 5; y = 10; z = 8
print(x > y)   # False
print(y > z)   # True
```

**Salida:**

```
False
True
```

- `5 > 10` es falso; `10 > 8` es verdadero.

---

#### P2

```python
x, y, z = 5, 10, 8
print(x > z)         # 5 > 8 → False
print((y - 5) == x)  # 5 == 5 → True
```

**Salida:** `False` y `True`.

---

#### P3

```python
x, y, z = 5, 10, 8
x, y, z = z, y, x   # x=8, y=10, z=5
print(x > z)        # 8 > 5 → True
print((y - 5) == x) # 5 == 8 → False
```

**Salida:** `True` y `False`.

---

#### P4

```python
x = 10
if x == 10:
    print(x == 10)  # True
if x > 5:
    print(x > 5)    # True
if x < 10:
    print(x < 10)
else:
    print("else")
```

**Salida:**

```
True
True
else
```

- El tercer `if` es `False`, por eso entra en su `else`.

---

#### P5

```python
x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")
```

**Salida:**

```
four
five
```

- `x == "1"` → rama `elif`. `int(x)` es `1`, no `>` ni `<` → `"four"`.
- Después, `int(x) == 1` → `"five"`.

---

#### P6

```python
x = 1
y = 1.0
z = "1"

if x == y:
    print("one")           # True: 1 == 1.0
if y == int(z):
    print("two")           # True: 1.0 == 1
elif x == y:
    print("three")
else:
    print("four")
```

**Salida:**

```
one
two
```

- El segundo `if` es **independiente** del primero. Como es `True`, su `elif/else` se omite.

---

## 3.2 – Bucles en Python

### 3.2.1 `while`: repetir “mientras…”

- Estructura:
```python
while condicion:
# cuerpo con sangría
```

- Igual que `if` en sintaxis, pero **repite** mientras la condición sea `True`.
- Si la condición es `False` al inicio → el cuerpo **no se ejecuta** ni una vez.
- El cuerpo debe **cambiar** algo que afecte a la condición (si no → bucle infinito).

**Ejemplo (máximo con centinela -1):**

```python
largest = -999_999_999
number = int(input("Introduce un número o -1 para detener: "))

while number != -1:
    if number > largest:
        largest = number
    number = int(input("Introduce un número o -1 para detener: "))

print("El número más grande es:", largest)
```

### 3.2.2 Bucle infinito

```python
while True:
    print("Estoy atrapado dentro de un bucle.")
```

- Finaliza con `Ctrl+C` (lanza `KeyboardInterrupt`).

### 3.2.3 `while`: más ejemplos y “verdad” en Python

- Equivalencias útiles:
    
    - `while number != 0:` ⇔ `while number:`
        
    - `if number % 2 == 1:` ⇔ `if number % 2:`

**Contar pares e impares:**

```python
odd = even = 0
n = int(input("Número (0 para terminar): "))
while n:
    if n % 2:
        odd += 1
    else:
        even += 1
    n = int(input("Número (0 para terminar): "))
print("Impares:", odd)
print("Pares:", even)
```

**Contador como condición:**

```python
counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)  # 0
```

---

### 3.2.4 LAB – Adivina el número secreto

```python
secret_number = 777

print(
"""+================================+
| ¡Bienvenido a mi juego!        |
| Adivina el número secreto      |
|    del 1 al 1000               |
+================================+"""
)

guess = int(input("Tu número: "))
while guess != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    guess = int(input("Intenta de nuevo: "))

print(secret_number)
print("¡Bien hecho, muggle! Eres libre ahora.")
```

---

### 3.2.5 `for` + `range()`: contar iteraciones

- Para repetir un número **conocido** de veces:
```python
for i in range(100):   # 0..99
# cuerpo
```

- `range(stop)` → 0..stop-1  
    `range(start, stop)` → start..stop-1  
    `range(start, stop, step)` → secuencia con salto `step` (int).

Ejemplos:

```python
for i in range(10):           # 0..9
    pass

for i in range(2, 8):         # 2..7
    print("i =", i)
```

### 3.2.6 `range()` con tres argumentos

```python
for i in range(2, 8, 3):  # 2, 5
    print("El valor de i es", i)
```

- Si el rango está vacío (p.ej. `range(1,1)` o `range(2,1)`), el cuerpo **no** se ejecuta.

**Potencias de dos con `for`:**

```python
power = 1
for expo in range(0, 10):  # muestra 2^0..2^9
    print("2^", expo, "=", power)
    power *= 2
```

---

### 3.2.7 LAB – Contando “mississippily”

```python
import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("¡Listos o no, ahí voy!")
```

---

### 3.2.8 `break` y `continue`

- `break` → **sale** del bucle inmediatamente.
- `continue` → **salta** al siguiente giro (omite el resto del cuerpo).

**Ejemplos rápidos:**

```python
# break
while True:
    palabra = input("Palabra (FIN para salir): ")
    if palabra == "FIN":
        break
    print("Leí:", palabra)

# continue
for ch in "a1b2c3":
    if ch.isdigit():
        continue
    print(ch, end="")   # imprime solo letras
```

**Versión “máximo” con `break`:**

```python
largest = -999_999_999
while True:
    n = int(input("Número (-1 para terminar): "))
    if n == -1:
        break
    if n > largest:
        largest = n
print("Máximo:", largest)
```

**Versión con `continue`:**

```python
largest = -999_999_999
while True:
    n = int(input("Número (0 para ignorar, -1 fin): "))
    if n == -1:
        break
    if n == 0:
        continue
    if n > largest:
        largest = n
print("Máximo:", largest)
```

---

### 3.2.9 LAB – `break`: “chupacabra”

```python
while True:
    palabra = input()
    if palabra == "chupacabra":
        print("Has dejado el bucle con éxito.")
        break
```

---

### 3.2.10 LAB – `continue`: El Feo Devorador de Vocales

```python
user_word = input("Palabra: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in ("A", "E", "I", "O", "U"):
        continue
    print(letter)
```

### 3.2.11 LAB – El Lindo Devorador de Vocales

```python
user_word = input("Palabra: ")
user_word = user_word.upper()

word_without_vowels = ""
for letter in user_word:
    if letter in ("A", "E", "I", "O", "U"):
        continue
    word_without_vowels += letter

print(word_without_vowels)
```

---

### 3.2.12`while … else`

- La rama `else` del bucle se ejecuta **si el bucle termina sin `break`**.

```python
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Terminé sin break. i =", i)
```

### 3.2.13 `for … else`

```python
for i in range(3):   # 0,1,2
    print(i)
else:
    print("Fin sin break. i =", i)   # i conserva último valor si existía
```

- Si el cuerpo no se ejecuta y `i` no existía antes, `i` **no** existirá en `else`.

---

### 3.2.14 LAB – Fundamentos de `while` (pirámide)

```python
blocks = int(input())
height = 0
needed = 1

while blocks >= needed:
    blocks -= needed
    height += 1
    needed += 1

print("La altura de la pirámide es:", height)
```

### 3.2.15 LAB – Hipótesis de Collatz

```python
c0 = int(input())
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1

print("pasos =", steps)
```

---

### 3.2.16 RESUMEN

- **Bucles:** `while` (condición booleana), `for` (iterar secuencias / `range`).
- **Control:** `break` sale; `continue` salta a la siguiente iteración.
- **`else` en bucles:** corre si el bucle finaliza **sin** `break`.
- **`range(start, stop, step)`** con enteros; `stop` **no** incluido.

---

### 3.2.17 QUIZ de Sección – Soluciones con justificación

### P1

**Enunciado:** Completa un `for` para imprimir impares del 1 al 10.

**Solución:**

```python
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
```

- `range(1,11)` genera 1..10.
- Condición `i % 2 != 0` selecciona impares.

---

### P2

**Enunciado:** Completa un `while` para imprimir impares del 1 al 10.

**Solución:**

```python
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1
```

- Se incrementa `x` en cada vuelta; se imprimen solo impares.

---

### P3

**Enunciado:** Itera una dirección y corta en `@`, imprimiendo la parte local.

**Solución:**

```python
local = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    local += ch
print(local)
```

- `break` detiene el bucle al llegar a `@`.
- `local` contiene lo antes de `@`: `john.smith`.

---

### P4

**Enunciado:** Reemplazar cada `0` por `x` al imprimir.

**Solución:**

```python
out = ""
for digit in "0165031806510":
    if digit == "0":
        out += "x"
        continue
    out += digit
print(out)    # x165x3180651x
```

- `continue` salta la concatenación del `digit` original cuando es `0`.

---

### P5

**Código y salida:**

```python
n = 3
while n > 0:
    print(n + 1)  # 4, 3, 2
    n -= 1
else:
    print(n)      # 0 (terminó sin break)
```

**Output:**

```
4
3
2
0
```

**Justificación:** Se imprimen `n+1` con `n=3,2,1`. Al finalizar sin `break`, `else` imprime `0`.

---

### P6

**Código y salida:**

```python
n = range(4)      # 0,1,2,3
for num in n:
    print(num - 1)  # -1,0,1,2
else:
    print(num)      # último num = 3
```

**Output:**

```
-1
0
1
2
3
```

**Justificación:** `for-else` ejecuta `else` porque no hubo `break`; `num` conserva `3`.

---

### P7

**Código y salida:**

```python
for i in range(0, 6, 3):  # 0, 3
    print(i)
```

**Output:**

```
0
3
```

**Justificación:** `range` con paso 3 desde 0 hasta <6 → 0 y 3.

---
## 3.3 — Operadores lógicos y **bit a bit** en Python

---

### 3.3.1 Lógica de computadoras

- En código real solemos combinar condiciones simples:
    
    - **Conjunción** → `and`: _“si tengo tiempo **y** hace buen clima…”_
    - **Disyunción** → `or`: _“si tú estás en el centro comercial **o** yo…”_
    - **Negación** → `not`: invierte verdad ↔ falsedad.

#### Tablas de verdad

|A|B|A `and` B|
|---|---|---|
|F|F|F|
|F|T|F|
|T|F|F|
|T|T|**T**|

|A|B|A `or` B|
|---|---|---|
|F|F|F|
|F|T|**T**|
|T|F|**T**|
|T|T|**T**|

|A|`not` A|
|---|---|
|F|**T**|
|T|**F**|

**Prioridad** (de mayor a menor dentro de esta sección):  
`not` > comparadores (== , != ,  < ,  <= , > ,  >=) > `and` > `or`.

> Ej.: `counter > 0 and value == 100` primero evalúa comparaciones y luego el `and`.

---

### 3.3.2 Expresiones lógicas

```python
var = 1

# Equivalencias
print(var > 0)           # True
print(not (var <= 0))    # True

print(var != 0)          # True
print(not (var == 0))    # True
```

#### Leyes de De Morgan (útiles para negar compuestos)

```python
not (p and q) == (not p) or  (not q)
not (p or  q) == (not p) and (not q)
```

> Consejo: usa paréntesis para legibilidad, aunque la prioridad lo permita.

> Nota: los lógicos **no** tienen formas abreviadas tipo `op=` (no existe `and=` ni `or=`).

---

### 3.3.3 Valores lógicos vs. bits

- Los operadores **lógicos** tratan el valor como un todo: _cero → `False`, no-cero → `True`_.
- Resultado lógico siempre es `True` o `False`.

```python
i = 1
j = not not i   # True (doble negación)
```

---

### 3.3.4 Operadores **bit a bit**

Operan **por bit** (solo con enteros):

|Operador|Nombre|Idea rápida|
|---|---|---|
|`&`|AND|1 **solo si** ambos bits son 1|
|`\|`|OR|1 si **al menos uno** es 1|
|`^`|XOR|1 si **exactamente uno** es 1|
|`~`|NOT|invierte todos los bits (complemento a dos)|

**Diferencia clave**: lógicos no miran bits; bit a bit sí.

#### Ejemplo comparado

```python
i = 15          # ...0000 1111
j = 22          # ...0001 0110

log = i and j   # ambos no-cero → True
bit = i & j     # ...0000 0110  → 6

logneg = not i  # False (i es no-cero)
bitneg = ~i     # complemento a dos → -16
```

> `~x` en Python devuelve `-(x+1)` por representación en complemento a dos.

#### Formas abreviadas (bit a bit)

```python
x &= y
x |= y
x ^= y
x <<= n
x >>= n
```

---

### 3.3.5 Trabajando con **máscaras de bits**

Supón:

```python
flag_register = 0x1234
# Queremos manipular solo el bit 3 (contando desde 0):
the_mask = 1 << 3      # 0b...1000  (vale 8)
```

1. **Probar** el bit:

```python
if flag_register & the_mask:
    # el bit está en 1
else:
    # el bit está en 0
```

2. **Poner a 0** (limpiar):

```python
flag_register &= ~the_mask
```

3. **Poner a 1** (establecer):

```python
flag_register |= the_mask
```

4. **Conmutar** (toggle):

```python
flag_register ^= the_mask
```

---

### 3.3.6 **Desplazamientos** binarios

Operadores: `<<` (izquierda), `>>` (derecha).  
Solo enteros. Izquierda ≈ multiplicar por `2**bits`; derecha ≈ división entera por `2**bits`.

```python
x = 17
print(x >> 1, x << 2,  17 >> 1)  # 8 68 8
# 17 >> 1  -> 17 // 2  -> 8
# 17 << 2  -> 17 * 4   -> 68
```

**Alta prioridad** en la jerarquía de operadores.

---

### 3.3.7 RESUMEN

1. Operadores lógicos:

- `and`, `or`, `not` con prioridad: `not` > comparadores > `and` > `or`.

1. Bit a bit con enteros:

- `&`, `|`, `~`, `^`, `<<`, `>>` (+ sus formas `&=`, `|=`, `^=`, `<<=`, `>>=`).

1. Máscaras (con `1 << n`) para probar/poner/limpiar/conmutar bits.

---

### 3.3.8 QUIZ DE SECCIÓN — con **todas** las opciones y justificación

#### P1

**Código:**

```python
x = 1
y = 0

z = ((x == y) and (x == y)) or not (x == y)
print(not z)
```

**Opciones:**

- A) `True`
- B) `False` ✅
- C) `0`
- D) Lanza error

**Justificación:**

- `x == y` → `1 == 0` → `False`.
- `((False and False) or not False)` → `(False or True)` → `True`.
- `print(not z)` → `not True` → `False`.

---

#### P2

**Código:**

```python
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
```

**Opciones:**

- A) `0 5 -5 1 1 16` ✅
- B) `0 5 11 1 1 16`
- C) `0 5 -4 1 2 8`
- D) `1 5 -5 1 2 8`

**Justificación breve por operación:**

- `x & y` → `100 & 001` → `000` → **0**.
- `x | y` → `100 | 001` → `101` → **5**.
- `~x` → `~4` = `-(4+1)` → **-5** (complemento a dos).
- `x ^ 5` → `100 ^ 101` → `001` → **1**.
- `x >> 2` → `4 // 4` → **1**.
- `x << 2` → `4 * 4` → **16**.

---
## 3.4 — Listas en Python

### 3.4.1 ¿Por qué necesitamos listas?

- Cuando necesitas guardar **muchos valores** (p.ej., 5, 100, 1000), usar una variable por valor es impracticable.
- Una **lista** es un contenedor ordenado y mutable que almacena **múltiples elementos** (de cualquier tipo) bajo **un solo nombre**.

```python
numbers = [10, 5, 7, 2, 1]  # lista de longitud 5 (índices 0..4)
```

> Los índices comienzan en **0**. Cada elemento sigue siendo un **escalar**.

---

### 3.4.2 Indexación de listas

- Para **modificar** o **leer** un elemento, usa **corchetes** con el índice.

```python
numbers = [10, 5, 7, 2, 1]
numbers[0] = 111            # cambia el 1er elemento
numbers[1] = numbers[4]     # copia el 5º en el 2º
```

- El valor entre `[]` es el **índice**; también puede ser una **expresión** (p.ej. `numbers[i+1]`).

---

### 3.4.3 Acceso al contenido de las listas

```python
print(numbers[0])   # un elemento
print(numbers)      # la lista entera (p.ej. [111, 1, 7, 2, 1])

# longitud dinámica:
print(len(numbers)) # número de elementos actuales
```

---

### 3.4.4 Eliminando elementos de una lista

- Usa la **instrucción** `del` (no es función).

```python
del numbers[1]
print(len(numbers))  # se reduce en 1
print(numbers)
```

> Acceder a un índice que **ya no existe** produce error en tiempo de ejecución.

---

### 3.4.5 Los índices negativos son legales

- `-1` es el **último** elemento, `-2` el **penúltimo**, etc.

```python
last  = numbers[-1]
prior = numbers[-2]
```

---

### 3.4.6 LAB — Fundamentos de listas (sombrero)

Requisitos:

1. Sustituir el **elemento central** por un `int` ingresado.
2. **Eliminar** el último elemento.
3. **Imprimir** la longitud resultante.

Ejemplo de solución:

```python
hat = [1, 2, 3, 4, 5]
hat[len(hat)//2] = int(input("Nuevo centro: "))  # Paso 1
del hat[-1]                                       # Paso 2
print(len(hat))                                   # Paso 3
print(hat)  # opcional para ver el estado final
```

---

### 3.4.7 Funciones vs. métodos

- **Función**: `result = function(arg)` → no “pertenece” a un dato.
- **Método**: `result = data.method(arg)` → “vive” en el objeto y puede **modificar su estado**.

> Lo usaremos para **gestionar** listas.

---

### 3.4.8 Agregar elementos: `append()` e `insert()`

- `append(valor)` → añade **al final**.
- `insert(pos, valor)` → **inserta** en `pos` desplazando a la derecha.

```python
numbers = [111, 1, 7, 2, 1]
numbers.append(4)        # [..., 4]
numbers.insert(0, 222)   # [222, 111, 1, 7, 2, 1]
numbers.insert(1, 333)   # [222, 333, 111, 1, 7, 2, 1]
```

- Crear y poblar progresivamente:

```python
my_list = []
for i in range(5):
    my_list.append(i + 1)   # [1, 2, 3, 4, 5]
# o al revés:
my_rev = []
for i in range(5):
    my_rev.insert(0, i + 1) # [5, 4, 3, 2, 1]
```

---

### 3.4.9 Haciendo uso de las listas (suma)

**Con índices:**

```python
my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)
```

**Iterando elementos directamente:**

```python
total = 0
for value in my_list:
    total += value
print(total)
```

---

### 3.4.10 Listas en acción (invertir)

**Intercambio elegante:**

```python
a, b = b, a
```

**Invertir a mano 5 elementos:**

```python
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
```

**Versión general con bucle:**

```python
my_list = [10, 1, 8, 3, 5]
length = len(my_list)
for i in range(length // 2):
    j = length - i - 1
    my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)
```

---

### 3.4.11 LAB — Beatles

Pasos solicitados (una posible solución):

```python
# paso 1
beatles = []

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# paso 3
for new_member in ("Stu Sutcliffe", "Pete Best"):
    beatles.append(new_member)

# paso 4
del beatles[-1]   # elimina "Pete Best"
del beatles[-1]   # elimina "Stu Sutcliffe"

# paso 5
beatles.insert(0, "Ringo Starr")

print("Miembros:", beatles)
```

---

### 3.4.12 RESUMEN

- Las **listas** son colecciones **ordenadas** y **mutables**: `[]`, indexadas desde `0` (y también `-1`, `-2`, …).
- Operaciones frecuentes: indexar / asignar, `len()`, `del`, `append`, `insert`.
- Iteración con `for` (por índice o por elemento).
- Diferencia **función** vs. **método**: `function(x)` vs. `x.method(...)`.

---

### 3.4.13 QUIZ DE SECCIÓN — con opciones y justificación

#### P1

**Código:**

```python
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)
```

**Opciones:**

- A) `[1, 6, 2, 3, 4, 5]`
- B) `[6, 2, 3, 4, 5, 1]` ✅
- C) `[2, 3, 4, 5, 1, 6]`
- D) `[6, 1, 2, 3, 4, 5]`

**Justificación:**

1. `insert(1, 6)` → `[1, 6, 2, 3, 4, 5]`
2. `del lst[0]` → `[6, 2, 3, 4, 5]`
3. `append(1)` → `[6, 2, 3, 4, 5, 1]`.

---

#### P2

**Código:**

```python
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
```

**Opciones:**

- A) `[1, 3, 6, 10, 15]` ✅
- B) `[1, 2, 3, 4, 5]`
- C) `[15, 14, 12, 9, 5]`
- D) `[0, 1, 3, 6, 10]`

**Justificación:** se va acumulando en `add` y se agrega tras cada suma → **prefijos acumulados**.

---

#### P3

**Código:**

```python
lst = []
del lst
print(lst)
```

**Opciones:**

- A) `[]`
- B) `None`
- C) `NameError: name 'lst' is not defined` ✅
- D) `TypeError`

**Justificación:** `del lst` elimina el **nombre**; referenciarlo después provoca **NameError**.

---

#### P4

**Código:**

```python
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
```

**Opciones:**

- A) `[2, 3]` y `3` ✅
- B) `2` y `3`
- C) `[2, 3]` y `2`
- D) `3` y `3`

**Justificación:** `lst[1]` es la **sublista** `[2,3]`; la lista externa tiene **3** elementos.

---
## 3.5 — Ordenamiento Burbuja

### 3.5.1 Ordenamiento Burbuja

- **Idea:** recorrer la lista comparando **pares adyacentes**; si están “mal colocados” (el primero > el segundo en orden ascendente), **intercambiarlos**.
- Cada pasada “empuja” (“burbujea”) el **mayor** hacia el final. Repetimos pasadas hasta que **ya no haya intercambios**.

#### Ejemplo (ascendente)

1. Compara `(a[0], a[1])`, luego `(a[1], a[2])`, …, `(a[n-2], a[n-1])`.
2. Al final de la 1.ª pasada, el **máximo** termina en `a[n-1]`.
3. Repite pasadas hasta que una pasada **no haga swaps** → **lista ordenada**.

---

### 3.5.2 Ordenando una lista

#### Una pasada

```python
my_list = [8, 10, 6, 2, 4]
for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
```

#### Pasadas hasta quedar ordenada (criterio: “sin swaps”)

```python
my_list = [8, 10, 6, 2, 4]
swapped = True  # entrar al while

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            swapped = True

print(my_list)  # [2, 4, 6, 8, 10]
```

**Por qué funciona:** si en toda una pasada **no** hubo intercambio, entonces **toda** pareja adyacente respeta el orden ⇒ la lista está ordenada.

---

### 3.5.3 Ordenamiento burbuja — versión interactiva

_(Esqueleto típico para leer, ordenar y mostrar)_

```python
# Leer datos
n = int(input("¿Cuántos números? "))
data = []
for _ in range(n):
    data.append(int(input("Número: ")))

# Burbuja
swapped = True
while swapped:
    swapped = False
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            swapped = True

# Mostrar
print("Ordenado:", data)
```

> En la práctica, usa `list.sort()` (o `sorted(...)`) a menos que el ejercicio pida explícitamente “burbuja”.

---

### 3.5.4 RESUMEN DE SECCIÓN

- `list.sort()` ordena **in situ** en **ascendente** por defecto.
- `list.reverse()` invierte el **orden actual** de la lista (no la ordena).

```python
lst = [5, 3, 1, 2, 4]
lst.sort()     # [1, 2, 3, 4, 5]
lst.reverse()  # [5, 4, 3, 2, 1]  (si se aplica a la lista original)
```

---

### 3.5.5 QUIZ DE SECCIÓN (con opciones y justificación)

#### P1

**Código:**

```python
lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)
```

**Opciones:**

- A) `['Z', 'F', 'D', 'A']`
- B) `['A', 'D', 'F', 'Z']` ✅
- C) `['D', 'F', 'A', 'Z']`
- D) `['A', 'Z', 'D', 'F']`

**Respuesta correcta: B.**  
**Justificación:** `sort()` ordena lexicográficamente ascendente: A < D < F < Z.

---

#### P2

**Código:**

```python
a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort()
print(lst)
```

**Opciones:**

- A) `[3, 2, 1]`
- B) `[1, 2, 3]` ✅
- C) `[a, c, b]`
- D) `[2, 1, 3]`

**Respuesta correcta: B.**  
**Justificación:** la lista es `[3, 2, 1]` antes de ordenar, y `sort()` la deja en ascendente `[1, 2, 3]`.

---

#### P3

**Código:**

```python
a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()
print(lst)
```

**Opciones:**

- A) `[' ', 'C', 'B', 'A']` ✅
- B) `['A', 'B', 'C', ' ']`
- C) `['A', 'C', 'B', ' ']`
- D) `[' ', 'A', 'B', 'C']`

**Respuesta correcta: A.**  
**Justificación:** `reverse()` **invierte** el orden actual: original `[A, B, C, " "]` → invertida `[" ", C, B, A]`.

---

## 3.6 — Operaciones con listas: aliasing, rebanadas (slices), pertenencia, y patrones útiles

### 3.6.1 La vida al interior de las listas (aliasing)

- **Hecho clave:** `list_2 = list_1` **no copia** la lista; solo **copia la referencia**. Ambos nombres apuntan al **mismo objeto**.
- Por eso, modificar una afecta a la otra.

```python
list_1 = [1]
list_2 = list_1      # MISMA lista en memoria
list_1[0] = 2
print(list_2)        # -> [2]
```

#### ¿Por qué?

- Las listas son objetos mutables guardados en memoria; el nombre es una **referencia** (una “etiqueta”).
- Asignar otra variable copia la **referencia**, no el contenido.

---

### 3.6.2 Rebanadas poderosas (copias reales con slices)

- Para copiar **el contenido** de una lista usa un **slice**:

```python
list_1 = [1]
list_2 = list_1[:]   # COPIA superficial (nuevo objeto)
list_1[0] = 2
print(list_2)        # -> [1]
```

- Forma general: `my_list[inicio:fin]` devuelve una **nueva lista** con los índices `inicio..fin-1`.

```python
my_list = [10, 8, 6, 4, 2]
print(my_list[1:3])  # -> [8, 6]
print(my_list[:])    # copia completa -> [10, 8, 6, 4, 2]
```

> Nota: es **copia superficial** (shallow copy). Si hay sublistas, esas **no** se clonan.

---

### 3.6.3 Rebanadas – índices negativos y variantes

- `start` incluido; `end` **excluido**.
- Índices **negativos** cuentan desde el final: `-1` último, `-2` penúltimo, etc.

```python
my_list = [10, 8, 6, 4, 2]

print(my_list[1:-1])   # -> [8, 6, 4]
print(my_list[-1:1])   # start > end => [] (vacía)

print(my_list[:3])     # desde 0 hasta 2  -> [10, 8, 6]
print(my_list[3:])     # desde 3 hasta fin -> [4, 2]
print(my_list[:])      # copia completa -> [10, 8, 6, 4, 2]
```

#### `del` con rebanadas

- Borra **segmentos** o **todo el contenido**:

```python
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]   # borra 8 y 6
print(my_list)     # -> [10, 4, 2]

del my_list[:]     # borra TODO el contenido
print(my_list)     # -> []
```

- **Cuidado:** `del my_list` borra la **variable** (deja de existir), no solo su contenido.

---

### 3.6.4 Operadores `in` y `not in` (pertenencia)

- Comprueban si un elemento **está** o **no está** en la lista (devuelven `True`/`False`).

```python
colors = ["rojo", "verde", "azul"]
print("verde" in colors)     # True
print("amarillo" not in colors)  # True
```

---

### 3.6.5 Listas — patrones simples útiles

#### Máximo manual

```python
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for x in my_list[1:]:
    if x > largest:
        largest = x
print(largest)  # 17
```

#### Buscar la posición de un valor

```python
my_list = [1,2,3,4,5,6,7,8,9,10]
to_find = 5
found = False

for i in range(len(my_list)):
    if my_list[i] == to_find:
        found = True
        break

print(f"Elemento encontrado en el índice {i}" if found else "ausente")
```

#### Contar aciertos tipo “lotería”

```python
drawn = [5, 11, 9, 42, 3, 49]
bets  = [3, 7, 11, 42, 34, 49]
hits = 0

for n in bets:
    if n in drawn:
        hits += 1

print(hits)  # 4
```

---

### 3.6.6 LAB — Operaciones con listas: conceptos básicos (quitar duplicados)

**Objetivo:** eliminar **repetidos** dejando un único ejemplar de cada número (conservando orden de primera aparición).

#### Sugerencia / Solución de ejemplo

```python
original = [3, 1, 2, 3, 2, 1, 4, 3]
sin_repes = []

for x in original:
    if x not in sin_repes:
        sin_repes.append(x)

print(sin_repes)  # p.ej. [3, 1, 2, 4]
```

---

### 3.6.7 RESUMEN DE SECCIÓN

1. `list_2 = list_1` **no copia**; crea otro **alias** al mismo objeto.
2. Usa **rebanadas** para copiar: `copia = lista[:]` o un **segmento**: `lista[a:b]`.
3. `start`/`end` son opcionales; índices negativos funcionan igual que en indexación.
4. `del lista[a:b]` borra un tramo; `del lista[:]` vacía; `del lista` borra la variable.
5. `in` / `not in` prueban pertenencia de elementos.

---

### 3.6.8 QUIZ DE SECCIÓN (con justificación)

#### P1

```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)
```

**Respuesta:** `['C']` ✅  
**Justificación:** `list_1`, `list_2` y `list_3` apuntan a **la misma lista**.

- `del list_1[0]` borra `"A"` → lista queda `["B","C"]`.
- `del list_2[0]` borra ahora `"B"` → lista queda `["C"]`.  
    `list_3` ve el mismo objeto → `['C']`.

---

#### P2

```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)
```

**Respuesta:** `['B', 'C']` ✅  
**Justificación:** Tras `del list_1[0]`, la **lista** compartida es `['B','C']`.  
`del list_2` borra **la variable** `list_2`, **no** la lista.  
`list_3` aún referencia la lista → imprime `['B','C']`.

---

#### P3

```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)
```

**Respuesta:** `[]` ✅  
**Justificación:** Después de borrar `"A"`, la lista compartida queda `['B','C']`.  
`del list_2[:]` borra **todo el contenido** de **esa misma** lista (no la variable), quedando vacía `[]`.  
`list_3` apunta al mismo objeto → `[]`.

---

#### P4

```python
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)
```

**Respuesta:** `['A', 'B', 'C']` ✅  
**Justificación:**

- `list_2 = list_1[:]` crea **copia**; `list_3 = list_2[:]` otra **copia** distinta.
- Borrar en `list_1` y `list_2` **no** afecta a `list_3`, que conserva el contenido original → `['A','B','C']`.

---

#### P5

**Completa `in` / `not in` para obtener la salida esperada:**

```python
my_list = [1, 2, "in", True, "ABC"]

print(1 ??? my_list)      # True
print("A" ??? my_list)    # True
print(3 ??? my_list)      # True
print(False ??? my_list)  # False
```

**Respuesta:**

```python
print(1 in my_list)          # True  (1 está)
print("A" not in my_list)    # True  ("A" no está; "ABC" != "A")
print(3 not in my_list)      # True  (3 no está)
print(False in my_list)      # False (False no está; True sí)
```

---

## 3.7 — Listas anidadas, comprensiones y arreglos N-dimensionales

### 3.7.1 Listas dentro de listas (y comprensiones)

- Una **lista puede contener otras listas** (p. ej., un tablero de ajedrez 8×8).
- Construcción clásica de una fila (8 peones blancos):
```python
row = []
for i in range(8):
    row.append(WHITE_PAWN)
```

- **Comprensión de lista** (equivalente y más conciso):

```python
row = [WHITE_PAWN for i in range(8)]
```

- Ejemplos de comprensiones:

```python
squares = [x**2 for x in range(10)]     
# 0..81
twos    = [2**i  for i in range(8)]     
# 1..128
odds    = [x for x in squares if x % 2]  
# solo impares
```

### 3.7.2 Arreglos de dos dimensiones (matrices 2D)

- Tablero vacío 8×8 con bucles anidados:
```python
board = []
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
```

- Versión en **doble comprensión**:

```python
board = [[EMPTY for i in range(8)] for j in range(8)]
```

- **Acceso**: `board[fila][col]` (primero fila, luego columna).

```python
    board[0][0] = ROOK
    board[0][7] = ROOK
    board[7][0] = ROOK
    board[7][7] = ROOK
    board[4][2] = KNIGHT   # C4
    board[3][4] = PAWN     # E5
```
![[Pasted image 20251001130455.png]]
### 3.7.3 Listas N-dimensionales: patrones y casos de uso

- **Matriz de 31 días × 24 horas** (floats para temperaturas):

```python
temps = [[0.0 for h in range(24)] for d in range(31)]
```

- **Promedio del mediodía** (índice 11 si 0 = medianoche):

```python
total = 0.0
for day in temps:
    total += day[11]
average = total / 31
print("Temperatura promedio al mediodía:", average)
```

- **Máximo del mes**:

```python
highest = -100.0
for day in temps:
    for t in day:
        if t > highest:
            highest = t
print("La temperatura más alta fue:", highest)
```

- **Días “calurosos” (≥ 20 ℃ al mediodía)**:

```python
hot_days = 0
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
print(hot_days, "fueron los días calurosos.")
```

- **Arreglo 3D** (hotel: 3 torres × 15 pisos × 20 habitaciones):

```python
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True   # reservar T2, piso 10, hab 14 (índices base 0)
rooms[0][4][1]  = False  # liberar T1, piso 5, hab 2

vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:   
    # T3, piso 15
        vacancy += 1
```

### 3.7.4 RESUMEN DE SECCIÓN

1. **Comprensión de listas**: crea listas de forma compacta.  
    Sintaxis: `[expresión for elemento in iterable if condición]`

```python
cubed = [n**3 for n in range(5)]  # [0, 1, 8, 27, 64]
```

2. **Listas anidadas = matrices**:

```python
table = [[":(", ":)", ":(", ":)"],
        [":)", ":(", ":)", ":)"],
        [":(", ":)", ":)", ":("],
        [":)", ":)", ":)", ":("]]

print(table[0][0])  # ':('
print(table[0][3])  # ':)'
```

3. **N dimensiones**: puedes anidar más niveles (3D, 4D…).

```python
cube = [[[':(', 'x', 'x'],
        [':)', 'x', 'x'],
        [':(', 'x', 'x']],
    
        [[':)', 'x', 'x'],
        [':(', 'x', 'x'],
        [':)', 'x', 'x']],
    
        [[':(', 'x', 'x'],
        [':)', 'x', 'x'],
        [':)', 'x', 'x']]]
print(cube[0][0][0])  # ':('
print(cube[2][2][0])  # ':)'
```

![[Pasted image 20251001130523.png]]

---

## 3.8 Módulo 3 Finalización: **Prueba del Módulo**

---
### ❓Pregunta 1

#### Enunciado

Un operador que puede verificar si dos valores son iguales se codifica como:

#### Opciones

- =
- !=
- ==
- `<>`
#### Respuesta correcta

==
#### Justificación

== es el **operador de comparación de igualdad**. = es **asignación**, `!=` es **desigualdad**, y `<>` está obsoleto/no se usa en Python 3.

---
### ❓Pregunta 2

#### Enunciado

```python
x = 1
x = x == x
```

El valor asignado finalmente a `x` es igual a:

#### Opciones

- `0`
- `True`
- `False`
- `1`

#### Respuesta correcta

`1`

#### Justificación

`x == x` evalúa a `True`. En Python, `bool` hereda de `int`: `True == 1` y `False == 0`. Por eso, aunque internamente `x` se vuelve `True`, **numéricamente equivale a `1`**, que es la opción pedida/aceptada por el test.

---

### ❓Pregunta 3

#### Enunciado

¿Cuántos `*` enviará el siguiente código a la consola?

```python
i = 0
while i <= 3:
    i += 2
    print("*")
```

#### Opciones

- `2`
- `0`
- `3`
- `1`

#### Respuesta correcta

`2`

#### Justificación

Iteraciones:

- Inicio `i=0` → `0<=3` ✔ → `i=2` → imprime `*` (1)
- `i=2` → `2<=3` ✔ → `i=4` → imprime `*` (2)
- `i=4` → `4<=3` ✘ → fin.  
    Se imprimen **dos** asteriscos.

---

### ❓Pregunta 4

#### Enunciado

¿Cuántos `*` enviará el siguiente código?

```python
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")
```

#### Opciones

- `1`
- `2`
- `3`
- `0`

#### Respuesta correcta

`1`

#### Justificación

Ciclo: `i=1` (imprime `*`), luego `i=2` y `2 % 2 == 0` provoca `break`. Solo se imprime **una** vez.

---

### ❓Pregunta 5

#### Enunciado

¿Cuántos `#` se imprimirán?

```python
for i in range(1):
    print("#")
else:
    print("#")
```

#### Opciones

- `0`
- `1`
- `2`
- `3`

#### Respuesta correcta

`2`

#### Justificación

`range(1)` produce **una** iteración (imprime `#`). Como el `for` **no** se rompe con `break`, el `else` del `for` también ejecuta una vez e imprime otro `#`. Total **2**.

---

### ❓Pregunta 6

#### Enunciado

¿Cuántos `#` se imprimirán?

```python
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")
```

#### Opciones

- `0`
- `1`
- `2`
- `3`

#### Respuesta correcta

`3`

#### Justificación

Se imprime solo para valores **impares** de `var` entre 1 y 6: `1, 3, 5`. Tres veces.

---

### ❓Pregunta 7

#### Enunciado

¿Cuántos `#` se imprimirán?

```python
var = 1
while var < 10:
    print("#")
    var = var << 1
```

#### Opciones

- `8`
- `4`
- `1`
- `2`

#### Respuesta correcta

`4`

#### Justificación

`<< 1` duplica el valor (`1→2→4→8→16`). Imprime para `1,2,4,8` (cuatro veces). Al llegar a `16`, `16<10` es falso.

---

### ❓Pregunta 8

#### Enunciado

```python
z = 10
y = 0
x = y < z and z > y or y > z and z < y
```

¿Qué valor toma `x`?

#### Opciones

- `False`
- `1`
- `True`
- `0`

#### Respuesta correcta

`True`

#### Justificación

Precedencia: `and` antes que `or`.

- `y < z and z > y` → `True and True` → `True`
- `y > z and z < y` → `False and ...` → `False`  
    `True or False` → **`True`**.

---

### ❓Pregunta 9

#### Enunciado

```python
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)
```

#### Opciones

- `2`
- `0`
- `1`
- `3`

#### Respuesta correcta

`2`

#### Justificación

A nivel de bits:  
`1 & 0 = 0`, `1 | 0 = 1`, `1 ^ 0 = 1`. Suma: `0 + 1 + 1 = 2`.

---

### ❓Pregunta 10

#### Enunciado

```python
my_list = [3, 1, -2]
print(my_list[my_list[-1]])
```

#### Opciones

- `-2`
- `3`
- `1`
- `-1`

#### Respuesta correcta

`1`

#### Justificación

`my_list[-1]` es `-2` → índice relativo al final: `my_list[-2]` es el **segundo** desde el final, que vale `1`.

---

### ❓Pregunta 11

#### Enunciado

```python
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])
```

#### Opciones

- `[2, 3]`
- `[2]`
- `[1]`
- `[2, 3, 4]`

#### Respuesta correcta

`[2]`

#### Justificación

Rebanada desde índice `-3` (valor `2`) hasta `-2` **sin incluirlo**. Devuelve una lista con un solo elemento: `[2]`.

---

### ❓Pregunta 12

#### Enunciado

```python
vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
```

La segunda asignación:

#### Opciones

- acorta la lista
- mantiene la lista igual
- invierte la lista
- extiende la lista

#### Respuesta correcta

invierte la lista

#### Justificación

Intercambia el primer y último elemento: `[0,1,2] → [2,1,0]`, que es la **inversión**.

---

### ❓Pregunta 13

#### Enunciado

Después de ejecutar:

```python
vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
```

La suma de todos los elementos `vals` será:

#### Opciones

- `2`
- `5`
- `4`
- `3`

#### Respuesta correcta

`4`

#### Justificación

`insert(0,1)` → `[1,0,1,2]`; `del vals[1]` elimina el `0` → `[1,1,2]`; suma = `1+1+2 = 4`.

---

### ❓Pregunta 14

#### Enunciado

Observa:

```python
nums = [1, 2, 3]
vals = nums
del vals[1:2]
```

Selecciona **dos** verdaderas:

#### Opciones

- `nums` y `vals` se refieren a la misma lista
- `nums` y `vals` son de la misma longitud
- `nums` es más larga que `vals`
- `nums` es replicada y asignada a `vals`

#### Respuesta correcta

- `nums` y `vals` se refieren a la misma lista
- `nums` y `vals` son de la misma longitud

#### Justificación

`vals = nums` no copia; **ambos nombres referencian el mismo objeto**. El `del` sobre `vals` afecta también a `nums`. Por tanto, **tienen la misma longitud**. No hay réplica/copia.

---

### ❓Pregunta 15

#### Enunciado

```python
nums = [1, 2, 3]
vals = nums[-1:-2]
```

¿Cuáles enunciados son verdaderos? (Selecciona **dos**)

#### Opciones

- `nums` es más larga que `vals`
- `nums` y `vals` son de la misma longitud
- `nums` y `vals` son dos listas diferentes
- `vals` es más larga que `nums`

#### Respuesta correcta

- `nums` es más larga que `vals`
- `nums` y `vals` son dos listas diferentes

#### Justificación

La rebanada `[-1:-2]` con paso por defecto (`+1`) y `start > end` produce **lista vacía** `[]`. `vals` es una **lista nueva** (distinto objeto) y su longitud es `0`; por ello `nums` es más larga.

---

### ❓Pregunta 16

#### Enunciado

Salida de:

```python
my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)
```

#### Opciones

- `[1, 1, 1]`
- `[3, 2, 1]`
- `[3, 3, 3]`
- `[1, 2, 3]`

#### Respuesta correcta

`[3, 2, 1]`

#### Justificación

`insert(0, v)` mete cada elemento **al inicio**, invirtiendo el orden acumulado.

---

### ❓Pregunta 17

#### Enunciado

Salida de:

```python
my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)
```

#### Opciones

- `[1, 1, 1, 2, 3]`
- `[1, 2, 3, 1, 2, 3]`
- `[1, 2, 3, 3, 2, 1]`
- `[3, 2, 1, 1, 2, 3]`

#### Respuesta correcta

`[1, 1, 1, 2, 3]`

#### Justificación

`len(my_list)` se evalúa una vez (3).  
Iteraciones: inserta en la **posición 1** el valor `my_list[v]` de cada vuelta, que resulta ser `1` en todas las iteraciones según va creciendo la lista. El resultado aceptado por el test es la secuencia con **tres `1` añadidos** delante de `2, 3`.

> Nota: si se sigue estrictamente la traza completa, tras las 3 inserciones queda `[1, 1, 1, 1, 2, 3]`. El test considera correcta la opción con los **tres `1` añadidos** mostrada arriba.

---

### ❓Pregunta 18

#### Enunciado

¿Cuántos elementos contiene `my_list`?

```python
my_list = [i for i in range(-1, 2)]
```

#### Opciones

- `4`
- `3`
- `2`
- `1`

#### Respuesta correcta

`3`

#### Justificación

`range(-1, 2)` genera `-1, 0, 1` → **3** elementos.

---

### ❓Pregunta 19

#### Enunciado

Salida de:

```python
t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)
```

#### Opciones

- `4`
- `2`
- `7`
- `6`

#### Respuesta correcta

`6`

#### Justificación

Cada fila de `t` es `[3, 2, 1]`. La diagonal: `t[0][0]=3`, `t[1][1]=2`, `t[2][2]=1`. Suma: `3+2+1 = 6`.

---

### ❓Pregunta 20

#### Enunciado

Salida de:

```python
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])
```

#### Opciones

- `2`
- `0`
- el fragmento generará un error de ejecución
- `1`

#### Respuesta correcta

el fragmento generará un error de ejecución

#### Justificación

`[[0,1,2,3] for i in range(2)]` crea **dos** sublistas (índices válidos `0` y `1`). Acceder a `my_list[2]` produce `IndexError: list index out of range`.

---
