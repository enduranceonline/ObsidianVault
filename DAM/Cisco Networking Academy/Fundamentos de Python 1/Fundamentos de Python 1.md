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

