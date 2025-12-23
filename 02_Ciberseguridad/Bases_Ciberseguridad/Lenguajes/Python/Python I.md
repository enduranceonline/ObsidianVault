# Curso de Introducción a Python
#bases #python #apuntes
## 1. Tipos de Datos Básicos  
- **Enteros** (`int`), **flotantes** (`float`) y **cadenas** (`str`).  
- Literales numéricos vs. literales de cadena:  
  - `4` es entero; `"4"` es cadena.  
- **Operaciones básicas**: `+`, `-`, `*`, `/`, `//`, `%`, `**`  
- Conversión de tipos: `int()`, `str()`  
- **Variables y asignación**: asociación de nombre → valor.  
- **Identificadores**: reglas de nombrado, palabras reservadas.  
- **Control de `print`**: argumentos `sep=`, `end=`.  
- **Formateo de cadenas**: `format()`, f-strings.  
- **Secuencias de escape**: `\n`, `\t`, etc.  
- **Entrada de usuario**: `input()` y conversión con `int()`/`float()`  

## 2. Listas

>Las **listas** en Python son colecciones **ordenadas** y **mutables**, ideales para almacenar secuencias de elementos que pueden cambiar a lo largo del programa.

### 2.1 Creación

- **Literal**  
  ```python
  frutas = ['manzana', 'banana', 'cereza']
```

- **Constructor `list()`**

    ```python
    numeros = list((1, 2, 3, 4))
    ```

- **Comprensión de listas**

    ```python
    cuadrados = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
    ```


### 2.2 Indexado y _slicing_

- **Acceso por índice** (0-based)

    ```python
    frutas = ['manzana', 'banana', 'cereza']
    print(frutas[0])   # 'manzana'
    print(frutas[-1])  # 'cereza'  (último elemento)
    ```

- **Slicing**

    ```python
    nums = [0, 1, 2, 3, 4, 5, 6]
    print(nums[2:5])     # [2, 3, 4]
    print(nums[:3])      # [0, 1, 2]
    print(nums[4:])      # [4, 5, 6]
    print(nums[1:6:2])   # [1, 3, 5]  (paso = 2)
    ```

### 2.3 Métodos comunes

|Método|Descripción|Ejemplo|
|---|---|---|
|`append(x)`|Añade `x` al final de la lista|`lista.append(10)`|
|`insert(i, x)`|Inserta `x` en la posición `i`|`lista.insert(1, 'nuevo')`|
|`pop([i])`|Elimina y devuelve el elemento en `i` (por defecto el último)|`item = lista.pop()`|
|`remove(x)`|Elimina la primera ocurrencia de `x`|`lista.remove('banana')`|
|`sort()`|Ordena **in place**|`lista.sort()`|
|`reverse()`|Invierte el orden **in place**|`lista.reverse()`|
|`copy()`|Devuelve una **copia superficial**|`otra = lista.copy()`|

> **Nota:** Muchos de estos métodos modifican la lista original.

### 2.4 Recorrido

- **Bucle `for`**

    ```python
    for fruta in frutas:
        print(f"Tengo una {fruta.upper()}")
    ```

- **Índice y valor**

    ```python
    for i, fruta in enumerate(frutas, start=1):
        print(f"{i}. {fruta}")
    ```

- **_While_ tradicional**

    ```python
    i = 0
    while i < len(frutas):
        print(frutas[i])
        i += 1
    ```


### 2.5 Ejemplos combinados

```python
# 1) Crear y popular lista
pares = []
for n in range(10):
    if n % 2 == 0:
        pares.append(n)
# pares = [0, 2, 4, 6, 8]

# 2) Insertar en medio
pares.insert(2, 99)         # [0, 2, 99, 4, 6, 8]

# 3) Recorrer y eliminar si > 50
i = 0
while i < len(pares):
    if pares[i] > 50:
        pares.pop(i)
    else:
        i += 1
# pares = [0, 2, 99, 4, 6, 8]

# 4) Ordenar y copiar
pares.sort()                # [0, 2, 4, 6, 8, 99]
copia = pares.copy()
```


## 3. Duplas (Tuplas)

Las **tuplas** (o “duplas”) en Python son colecciones **ordenadas** e **inmutables**, útiles cuando necesites agrupar datos que no deben cambiar.

### 3.1 Creación

- **Literal con paréntesis**  
  ```python
  punto = (10, 20)
  coordenadas = ('x', 'y', 'z')
```

- **Sin paréntesis (packing implícito)**

    ```python
    colores = 'rojo', 'verde', 'azul'
    ```

- **Constructor `tuple()`**

    ```python
    t = tuple([1, 2, 3, 4])
    ```


### 3.2 Indexado y _slicing_

- **Acceso por índice** (0‐based)

    ```python
    nums = (0, 1, 2, 3, 4)
    print(nums[2])    # 2
    print(nums[-1])   # 4
    ```

- **Slicing** (devuelve una tupla)

    ```python
    print(nums[1:4])    # (1, 2, 3)
    print(nums[:3])     # (0, 1, 2)
    print(nums[::2])    # (0, 2, 4)
    ```


### 3.3 Unpacking y packing

- **Unpacking**: asigna simultáneamente

    ```python
    a, b = punto             # a=10, b=20
    x, y, z = coordenadas    # x='x', y='y', z='z'
    ```

- **“_” para ignorar valores**

    ```python
    nombre, edad, _ = ('Ana', 30, 'España')
    ```

- **Packing** (empaquetar varios en uno)

    ```python
    datos = a, b, x, y
    ```


### 3.4 Métodos útiles

|Método|Descripción|Ejemplo|
|---|---|---|
|`count(x)`|Cuenta cuántas veces aparece `x`|`(1,2,2,3).count(2) # 2`|
|`index(x)`|Devuelve el índice de la primera aparición de `x`|`( 'a','b','a').index('a') # 0`|

> **Nota:** Al ser inmutables, no tienen métodos que modifiquen la tupla original.

### 3.5 Usos comunes

- **Retorno múltiple de funciones**

    ```python
    def min_max(lista):
        return min(lista), max(lista)
    lo, hi = min_max([3,1,4,1,5])
    ```

- **Llave de diccionario**

    ```python
    posiciones = {('A',1): 'Inicio', ('B',2): 'Meta'}
    ```

- **Como registros estáticos**

    ```python
    Persona = ('edad', 'nombre', 'email')
    ```


---

> Las tuplas resultan ideales cuando quieras asegurar que una secuencia de valores no sea alterada, además de facilitar el **empaquetado/desempaquetado** en tu código.```

---
## 4. Diccionarios

Los **diccionarios** son mapas **clave→valor** mutables y desordenados, ideales para buscar valores por una clave única.

### 4.1 Creación  
- **Literal**  
  ```python
  alumno = {'nombre': 'Ana', 'edad': 22, 'carrera': 'Física'}
```

- **Constructor `dict()`**

    ```python
    datos = dict(ciudad='Madrid', país='España', población=3_200_000)
    ```


### 4.2 Acceso y modificación

- **Obtener valor**

    ```python
    print(alumno['nombre'])       # 'Ana'
    print(alumno.get('edad'))     # 22
    print(alumno.get('altura', 1.70))  # 1.70 (valor por defecto)
    ```

- **Asignar o actualizar**

    ```python
    alumno['edad'] = 23
    alumno['email'] = 'ana@mail.com'
    ```


### 4.3 Métodos comunes

|Método|Descripción|Ejemplo|
|---|---|---|
|`keys()`|Devuelve vistas de claves|`alumno.keys()`|
|`values()`|Devuelve vistas de valores|`alumno.values()`|
|`items()`|Devuelve vistas de (clave, valor)|`alumno.items()`|
|`get(k[, d])`|Obtiene valor de `k`, o `d` si no existe|`alumno.get('tel', 'N/D')`|
|`pop(k[, d])`|Elimina y devuelve valor de `k`, o `d`|`alumno.pop('carrera')`|
|`update(other)`|Añade/actualiza pares de otro dict|`alumno.update({'edad': 24})`|

### 4.4 Recorrido

```python
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")
```

---

## 5. Conjuntos

Los **conjuntos** (`set`) son colecciones **no ordenadas** de elementos **únicos**, excelentes para operaciones de teoría de conjuntos.

### 5.1 Creación

- **Literal**

    ```python
    pares = {0, 2, 4, 6, 8}
    ```

- **Constructor `set()`**

    ```python
    letras = set('abracadabra')  # {'a','b','r','c','d'}
    ```


### 5.2 Operaciones de conjunto

|Operación|Símbolo|Ejemplo|
|---|---|---|
|Unión|`|`|
|Intersección|`&`|`A & B`|
|Diferencia|`-`|`A - B`|
|Diferencia simétrica|`^`|`A ^ B`|

```python
A = {1,2,3,4}
B = {3,4,5,6}
print(A | B)   # {1,2,3,4,5,6}
print(A & B)   # {3,4}
print(A - B)   # {1,2}
print(A ^ B)   # {1,2,5,6}
```

### 5.3 Métodos útiles

- `add(x)`, `remove(x)`, `discard(x)`, `pop()`, `clear()`


---

## 6. Operadores

Python ofrece varios tipos de operadores; véamos cada categoría con ejemplos.

### 6.1 Aritméticos

| Operador | Descripción      | Ejemplo       |
| -------- | ---------------- | ------------- |
| `+`      | Suma             | `3 + 4 # 7`   |
| `-`      | Resta            | `7 - 2 # 5`   |
| `*`      | Multiplicación   | `5 * 6 # 30`  |
| `/`      | División (float) | `7 / 2 # 3.5` |
| `//`     | División entera  | `7 // 2 # 3`  |
| `%`      | Módulo           | `7 % 2 # 1`   |
| `**`     | Potencia         | `2 ** 3 # 8`  |

### 6.2 Comparación

|Operador|Descripción|Ejemplo|
|---|---|---|
|`==`|Igualdad|`3 == 3 # True`|
|`!=`|Desigualdad|`3 != 4 # True`|
|`<, >`|Menor/Mayor|`2 < 5 # True`|
|`<=, >=`|Menor o igual / ≥|`4 >= 4 # True`|

### 6.3 Lógicos

- `and`, `or`, `not`

```python
(5 > 2) and (3 < 4)   # True
 not (5 == 2)          # True
```

### 6.4 Mixtos y coerción

- Mezclar `int` y `float` produce `float`

```python
 3 + 2.0  # 5.0
```

---

## 7. Precedencia de Operadores

La precedencia define el orden de evaluación. De mayor a menor:

1. `**`
    
2. `*`, `/`, `//`, `%`
    
3. `+`, `-`
    
4. Comparaciones (`<`, `>`, == , etc.)
    
5. `not`
    
6. `and`
    
7. `or`
    

> Usa **paréntesis** para forzar otra orden:

> 2 + 3 * 4     # 14
> (2 + 3) * 4   # 20


---

## 8. If

Estructura de decisión que ejecuta bloques según condiciones.

### 8.1 Sintaxis básica

```python
if condición:
    # bloque 1
elif otra_condición:
    # bloque 2
else:
    # bloque 3
```

### 8.2 Ejemplo

```python
x = 10
if x < 0:
    print("Negativo")
elif x == 0:
    print("Cero")
else:
    print("Positivo")
```

### 8.3 Expresión condicional

```python
estado = "mayor" if x >= 18 else "menor"
```

---

## 9. While / For

### 9.1 `while` (bucle indeterminado)

```python
n = 5
while n > 0:
    print(n)
    n -= 1
```

### 9.2 `for` (bucle definido)

```python
for i in range(3):
    print(i)      # 0, 1, 2
```

### 9.3 Anidamiento

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(f"{i=} {j=}")
```

---

## 10. Break y Continue

Controlan el flujo dentro de bucles.

- **`break`**: sale completamente del bucle.
    
    ```python
    for n in range(10):
        if n == 5:
            break
        print(n)  # 0–4
    ```

- **`continue`**: salta a la siguiente iteración.

    ```python
    for n in range(5):
        if n % 2 == 0:
            continue
        print(n)  # 1, 3
    ```


---

## 11. Funciones (argumentos determinados)

Definen bloques reutilizables con parámetros fijos.

### 11.1 Definición

```python
def saludar(nombre, edad):
    """
    Saluda a una persona indicando su nombre y edad.
    """
    return f"Hola {nombre}, tienes {edad} años."
```

### 11.2 Uso

```python
msg = saludar("Luis", 28)
print(msg)  # "Hola Luis, tienes 28 años."
```

---

## 12. Funciones (argumentos indeterminados)

### 12.1 `*args` (tupla de valores)

```python
def sumar_todos(*args):
    return sum(args)

print(sumar_todos(1, 2, 3, 4))  # 10
```

### 12.2 `**kwargs` (dict de valores nombrados)

```python
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

imprimir_info(nombre="Ana", edad=30)
# nombre = Ana
# edad = 30
```

### 12.3 Combinación

```python
def combo(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

combo(1, 2, 3, 4, x=10, y=20)
# 1 2 (3, 4) {'x': 10, 'y': 20}
```

---

## 13. Clases y Atributos (POO básica)

Agrupan datos y comportamientos en objetos.

### 13.1 Definición de clase

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre    # atributo de instancia
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
```

### 13.2 Uso

```python
p = Persona("María", 25)
p.saludar()  # "Hola, soy María y tengo 25 años."
```

---

## 14. Herencia en POO

Permite extender clases preexistentes.

### 14.1 Herencia simple

```python
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def info(self):
        print(f"{self.nombre}, {self.edad} años, estudia {self.carrera}.")
```

### 14.2 Herencia múltiple y MRO

```python
class A: pass
class B: pass
class C(A, B): pass
# C.__mro__ muestra el orden de resolución de métodos
```

---

## 15. Ejercicio: Parking

Diseña un programa que:

1. Modele las clases básicas:
    
    - `Coche` (matrícula, modelo)
        
    - `Plaza` (número, ocupada)
        
    - `Parking` (colección de plazas)
        
2. Implemente métodos en `Parking`:
    
    - `aparcar(coche)` → asigna primera plaza libre
        
    - `salir(matrícula)` → libera la plaza correspondiente
        
    - `estado()` → muestra plazas libres y ocupadas
        
3. Proporcione una **interfaz de consola** que:
    
    - Pregunte “¿Aparcar (A), Salir (S) o Estado (E)?”
        
    - Llame al método adecuado y muestre resultados.

> **Sugerencia:** Usa un `dict` en `Parking` para mapear matrículas → plazas y una `list` o `set` para gestionar plazas libres.

```python
class Coche:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo

class Plaza:
    def __init__(self, numero):
        self.numero = numero
        self.ocupada = False

class Parking:
    def __init__(self, total_plazas):
        self.plazas = [Plaza(i) for i in range(1, total_plazas+1)]
        self.ocupados = {}  # matricula -> Plaza

    def aparcar(self, coche):
        for p in self.plazas:
            if not p.ocupada:
                p.ocupada = True
                self.ocupados[coche.matricula] = p
                return p.numero
        return None

    def salir(self, matricula):
        p = self.ocupados.pop(matricula, None)
        if p:
            p.ocupada = False
            return p.numero
        return None
```

```python
# Ejemplo de uso en consola
park = Parking(5)
while True:
    op = input("¿Aparcar (A), Salir (S), Estado (E), Salir programa (Q)? ").upper()
    if op == 'A':
        mat = input("Matrícula: ")
        num = park.aparcar(Coche(mat, '-----'))
        print(f"Aparcado en plaza {num}" if num else "Parking lleno")
    elif op == 'S':
        mat = input("Matrícula: ")
        num = park.salir(mat)
        print(f"Salida de plaza {num}" if num else "Matrícula no encontrada")
    elif op == 'E':
        libres = [p.numero for p in park.plazas if not p.ocupada]
        print("Libres:", libres)
    elif op == 'Q':
        break
```
