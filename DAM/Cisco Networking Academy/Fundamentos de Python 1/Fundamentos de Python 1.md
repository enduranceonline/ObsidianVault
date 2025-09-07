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

# 📘 Módulo 2 – Tipos de datos, variables, Operaciones Basicas de Entrada y Salida, Operadores Basicos

