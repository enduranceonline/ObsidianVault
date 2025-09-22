# Bash Scripting – Apuntes

#bases #bash #apuntes

> **Autor:** _[endurance]_  
> **Última actualización: **

---

## Tabla de contenidos

- [Lección 1 – Introducción a Bash]
- [Lección 2 – Mi primer script]
- [Lección 3 – Variables]
- [Lección 4 – Variables lectura teclado]
- [Lección 5 – Variables especiales]
- [Lección 6 – Variables de entorno]
- [Lección 7 – Operaciones aritméticas]
- [Lección 8 – Operadores de comparación]
- [Lección 9 – Operadores subcadenas]
- [Lección 10 – Operadores lógicos]
- [Lección 11 – Operadores existencia]
- [Lección 12 – If, elif, else]
- [Lección 13 – If control args]
- [Lección 14 – Case y menú]
- [Lección 15 – For]
- [Lección 16 – While]
- [Lección 17 – Funciones]
- [Lección 18 – Funciones importar]
- [Lección 19 – Post Explotación Automatizada]
- [Lección 20 – Escáner automático]

---

# Lección 1 – Introducción a Bash

- **¿Qué es Bash?**  
    Bash (Bourne‑Again SHell) es el intérprete de comandos por defecto en la mayoría de las distribuciones GNU/Linux.
- **Diferencia entre shell y terminal**  
    El _shell_ es el programa que interpreta comandos; el _terminal_ es la interfaz.
- **Shebang**
```bash
#!/usr/bin/env bash
 ```

Indica al sistema qué intérprete usar al ejecutar el script.

---
# Lección 2 – Mi primer script

1. Crear archivo `hola.sh`.

2. Añadir shebang y comandos:

```bash
#!/usr/bin/env bash
echo "¡Hola, mundo!"
```

3. Dar permisos: `chmod +x hola.sh`

4. Ejecutar: `./hola.sh`

---
# Lección 3 – Variables

- Declaración literal: `variable="valor"` (sin espacios)

- Uso: `echo "$variable"`

- `readonly var`: variable constante

- Alcance: global dentro del proceso; en funciones usar `local nombre=valor`

#### Asignación vs. sustitución de comandos

| Forma     | Ejemplo                 | ¿Qué hace?                                                                               | Cuándo usarlo                                                 |
| --------- | ----------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Literal   | `saludo="Hola"`         | Guarda texto tal cual en la variable.                                                    | Para valores estáticos o cadenas definidas manualmente.       |
| Backticks | `` hora=`date +"%T"` `` | Ejecuta el comando y asigna su salida (stdout). Sintaxis histórica.                      | Compatible con shells POSIX antiguos, pero difícil de anidar. |
| `$()`     | `hora=$(date +"%T")`    | Igual que backticks pero más legible y fácil de anidar: `files=$(ls $(dirname "$ruta"))` | Forma recomendada en Bash moderno.                            |

##### Ventajas de `$()` sobre backticks

1. Soporta anidación sin necesidad de escapes complicados.

2. Facilita la lectura y el mantenimiento.

3. Los editores resaltan los paréntesis haciendo más claro el bloque sustituido.


```
# Ejemplos prácticos
usuario=$(whoami)            # => nombre de usuario actual
kernel=$(uname -r)           # => versión del kernel
lista=$(ls -1 *.txt)         # => lista de ficheros .txt separados por nueva línea

# Contar cuántos .txt hay usando sustitución anidada
echo "Hay $(wc -l <<< "$lista") ficheros .txt"
```

#### Ejemplos vistos en la terminal

```
var="hola mundo"
echo $var       # → hola mundo

var2='hola'
echo $var2      # → hola

echo "hola mundo $var"  # → hola mundo hola mundo
echo 'hola mundo $var'  # → hola mundo $var  (sin expansión)

variable=`pwd`   # o variable=$(pwd)
echo $variable   # → /root
```

**Claves del ejemplo**

1. **Expansión con comillas dobles**: dentro de `"..."` Bash reemplaza `$var` por su contenido.

2. **Comillas simples**: dentro de `'...'` no se expande nada; útil para strings literales.

3. **Sustitución de comandos (**`pwd`**)**: asigna la salida de un comando a una variable.

4. **Buenas prácticas**: usar `$(comando)` en lugar de backticks y siempre citar variables (`"$var"`).


> **Tip:** Cita siempre las variables con comillas dobles (`"$var"`) para evitar _word splitting_ y _globbing_ inesperado.
---

# Lección 4 – Variables: lectura por teclado y ámbito

#### 1. Ámbito (scope) de una variable

- **Global (por defecto)** · Toda variable declarada fuera de funciones vive en todo el script.

- **Local** · Si la declaras dentro de una función con `local nombre=valor`, sólo existe dentro de esa función.


```
#!/usr/bin/env bash
var_global=10

mi_funcion() {
  local var_local=20
  echo "dentro ⇒ $var_local"   # 20
}

echo "fuera ⇒ $var_global"      # 10
mi_funcion
# echo $var_local  # ← vacío: fuera de alcance
```

> 🔑 **Sólo añade** `**$**` **cuando quieras acceder al** _**valor**_ **de la variable**. Al asignar, **no** uses `$`.

```
var="hola"   
# ✅ asignación correcta
var2=$var     
# ✅ asignando el valor de otra variable
```

#### 2. Acceso y visualización del valor

- Básico: `echo $var`

- Seguro: `echo "$var"` (protege espacios y caracteres especiales)

- Forma explícita: `echo "${var}"`

#### 3. Lectura de datos por teclado – `read`

- Sintaxis simple: `read nombre_variable`

- Con mensaje: `read -p "Introduce tu nombre: " nombre`

- Ocultar lo tecleado (p.e. contraseñas): `read -s pass`

##### Ejemplo rápido

```
#!/usr/bin/env bash
read -p "Introduce datos: " dato
echo "Has escrito: $dato"
```

#### 4. Script de ejemplo completo

`pideDatos.sh`:

```
#!/usr/bin/env bash

echo "Introduce un número del 0 al 10:"
read numero

echo "El número introducido es: $numero"
```

```
chmod u+x pideDatos.sh
./pideDatos.sh
```

Salida típica:

```
Introduce un número del 0 al 10:
5
El número introducido es: 5
```

- **Comilla sin cerrar** ⇒ `unexpected EOF while looking for matching '...'`  
    Asegúrate de cerrar todas las comillas en `echo` y cadenas.

- **Olvidar** `**$**` ⇒ imprimirá el nombre de la variable y no su contenido.

---

# Lección 5. Variables especiales en Bash

Las variables especiales en Bash nos permiten conocer el entorno de ejecución del script y manejar argumentos dinámicos. Son fundamentales para desarrollar scripts robustos y adaptables a distintas situaciones.

---

## `$?` – Código de salida del último comando

Permite conocer si la instrucción anterior se ejecutó correctamente.

- `0` indica éxito (true)
- Cualquier otro valor indica error (false)

### Ejemplo:

```bash
echo $?
0

echoz hola mundo
# bash: echoz: command not found

echo $?
127
```

> ✅ Muy útil para verificar si comandos críticos han funcionado y tomar decisiones condicionales.

---

## `$$` – PID del proceso actual (del script)

Devuelve el identificador de proceso del script que se está ejecutando.

### Ejemplo:

```bash
echo $$
# 1234 (número variable según el sistema)
```

> 🧠 Útil para crear archivos temporales únicos o identificar procesos hijos.

---

## `$0` – Nombre del script  
## `$1` a `$9` – Argumentos posicionales

Permiten acceder a los argumentos individuales que se le pasan a un script desde la línea de comandos.  
`$0` contiene el nombre del script.  
`$1`, `$2`... hasta `$9` contienen los primeros 9 argumentos.

### Ejemplo práctico:

Archivo `argumentos.sh`:

```bash
#!/bin/bash

echo "Nombre script: $0"
echo "Valor del argumento 1: $1"
echo "Valor del argumento 2: $2"
echo "Valor del argumento 4: $4"
```

Dar permisos de ejecución:

```bash
chmod +x argumentos.sh
```

Ejecutar:

```bash
./argumentos.sh soy_uno soy_otro_arg soy_tres soy_cuatro
```

### Salida esperada:

```
Nombre script: ./argumentos.sh
Valor del argumento 1: soy_uno
Valor del argumento 2: soy_otro_arg
Valor del argumento 4: soy_cuatro
```

> 💡 Las variables existen aunque no tengan valor asignado si no se pasó argumento.

---

## `$@` – Todos los argumentos como lista

Devuelve todos los argumentos como una lista separada por espacios. Muy útil cuando se quiere iterar por todos los argumentos.

```bash
echo "Todos los argumentos: $@"
```

> ⚠️ En scripts con bucles, usar `"${@}"` para preservar argumentos con espacios.

---

## `$*` – Todos los argumentos como cadena única

Similar a `$@`, pero los trata como una sola cadena.

```bash
echo "Todos los argumentos como uno solo: $*"
```

> 📌 Diferencia importante: `"${@}"` conserva los argumentos separados, `"${*}"` los concatena.

---

## `$#` – Número de argumentos

Devuelve cuántos argumentos se pasaron al script.

```bash
echo "He recibido un total de $# argumentos"
```

> 🛡️ Sirve para validar si se han introducido los argumentos necesarios antes de continuar la ejecución del script.

---

## `$USER` – Usuario que ejecuta el script

Devuelve el nombre del usuario actual.

```bash
echo $USER
```

> 🧍 Ideal para verificar si quien ejecuta el script tiene permisos adecuados.

---

## `$HOSTNAME` – Nombre del host

Devuelve el nombre de la máquina en la que se ejecuta el script.

```bash
echo $HOSTNAME
```

> 🌐 Útil en scripts distribuidos o para control de acceso.

---

## `$RANDOM` – Número aleatorio

Devuelve un número aleatorio diferente cada vez que se consulta.

```bash
echo $RANDOM
# 28384
```

> 🎲 Ideal para generar datos de prueba o nombres temporales únicos.

---

## `$UID` – ID numérico del usuario actual

```bash
echo $UID
```

> 🔐 Útil para comprobar si se está ejecutando como root (`UID=0`).

---

## `$PWD` – Directorio actual

Devuelve la ruta absoluta del directorio de trabajo.

```bash
echo $PWD
```

> 📁 Útil para scripts que dependan de rutas relativas.

---

## `$HOME` – Ruta del directorio personal del usuario

```bash
echo $HOME
```

> 🏠 Comodidad para guardar archivos de usuario.

---

## Conclusión

Estas variables especiales permiten escribir scripts:

- Más interactivos
- Más seguros
- Más reutilizables

Conociéndolas, puedes crear scripts parametrizables y adaptados al entorno donde se ejecutan.

# Lección 6. Variables de entorno en Bash

Las **variables de entorno** contienen información del sistema y del usuario que es utilizada por el shell y por los procesos que se ejecutan. En esta lección veremos cómo consultarlas, cómo están estructuradas y cómo trabajar con ellas desde scripts.

---

## 🔍 Comando `env`

El comando `env` sin argumentos muestra **todas las variables de entorno** del sistema actual.

```bash
env
```

**Explicación**:
- `env`: Comando que imprime el entorno del usuario actual, útil para ver qué variables están disponibles en el sistema.

---

## 📌 Variables de entorno más comunes

| Variable       | Descripción                                                   |
|----------------|---------------------------------------------------------------|
| `$SHELL`       | Ruta absoluta al intérprete de comandos actual (`/bin/bash`)  |
| `$PATH`        | Lista de directorios donde se buscan los comandos ejecutables |
| `$USERNAME`    | Nombre del usuario (no siempre está definida)                 |
| `$USER`        | Nombre del usuario actual (más universal que `$USERNAME`)     |
| `$HOME`        | Directorio personal del usuario                               |
| `$PWD`         | Directorio actual donde te encuentras                         |
| `$LANG`        | Configuración de idioma y codificación del sistema            |

Para ver el valor de cualquier variable de entorno:

```bash
echo $VAR
```

Ejemplo:

```bash
echo $PATH
```

---

## 🛠️ ¿Qué es `$PATH`?

`$PATH` es una variable del sistema que contiene una **lista de rutas** separadas por `:`. Cada ruta es un directorio donde el sistema buscará los ejecutables de comandos que introducimos.

```bash
echo $PATH
```

Ejemplo de salida:

```
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

**Significado**:
- Si escribimos `ls`, el sistema buscará un ejecutable llamado `ls` en cada una de esas rutas, en orden, hasta encontrarlo.

---

## 🧪 Ejemplo práctico: script que obtiene una ruta del `$PATH`

Queremos pasarle al script un número (por ejemplo `3`) y que nos devuelva la tercera ruta del `$PATH`.

### ✅ Versión usando `cut`

Archivo `entorno.sh`:

```bash
#!/bin/bash

numero=$1
echo $PATH | cut -f$numero -d ":"
```

**Explicación línea a línea**:

- `#!/bin/bash`: Define que el script se ejecutará con Bash.
- `numero=$1`: Guarda el primer argumento que pasamos al script en la variable `numero`.
- `echo $PATH`: Muestra el contenido de la variable `$PATH`.
- `| cut -f$numero -d ":"`: El comando `cut` divide la salida de `$PATH` usando `:` como delimitador (`-d ":"`) y selecciona el campo número `$numero` (`-f$numero`).

**Ejecución**:

```bash
chmod +x entorno.sh
./entorno.sh 3
```

Resultado esperado (dependiendo del sistema):

```
/usr/sbin
```

---

### ✅ Versión usando `awk`

Archivo `entorno_awk.sh`:

```bash
#!/bin/bash

numero=$1
echo $PATH | awk -F: -v n="$numero" '{print $n}'
```

**Explicación línea a línea**:

- `numero=$1`: Guarda el primer argumento en la variable `numero`.
- `awk -F:`: Define `:` como delimitador de campos.
- `-v n="$numero"`: Crea una variable de awk llamada `n` con el valor de la variable de bash `numero`.
- `'{print $n}'`: Imprime el campo número `n` del texto recibido.

**Por qué usar esta sintaxis**:
Usar `` `echo $numero` `` o `$(...)` dentro de `awk` puede ser confuso para bash. Usar `-v` es la forma correcta y limpia de pasar variables de Bash a `awk`.

**Ejecución**:

```bash
chmod +x entorno_awk.sh
./entorno_awk.sh 3
```

---

## 🧠 Consideraciones sobre el orden semántico de evaluación

Cuando usamos comandos o expresiones con `$` y `$(...)`:

- `$(...)` o `` `...` `` → se evalúan **antes** que el resto del comando (es ejecución interna).
- `$$` → representa el PID del proceso actual (diferente de `$1`).
- `$variable` → se sustituye con el valor de la variable en tiempo de ejecución.

---

## ✅ Resumen

- Las **variables de entorno** nos permiten acceder a información clave del sistema.
- `$PATH` nos indica dónde se buscan los comandos ejecutables.
- Podemos usar herramientas como `cut` o `awk` para manipular su contenido.
- Comprender el **orden de evaluación** y cómo pasar argumentos es esencial para escribir scripts funcionales y seguros.

# Lección 7. Operaciones aritméticas en Bash

Bash, por defecto, **no tiene soporte completo** para realizar operaciones aritméticas complejas como otros lenguajes de programación. Sin embargo, existen varias formas de realizar cálculos básicos y avanzados.

---

## ❗ Problema

Si intentamos hacer una operación directamente:

```bash
echo 10 * 5
```

La salida será:

```
10 * 5
```

> ⚠️ **Bash no interpreta operadores matemáticos directamente** como hace Python o JavaScript. Necesitamos usar mecanismos especiales para realizar cálculos.

---

## ✅ Solución 1: Aritmética con `((...))`

Bash permite realizar operaciones básicas usando la sintaxis de **doble paréntesis**: `((...))`.  
Esto es una característica interna de Bash que permite evaluaciones aritméticas con enteros.

### Sintaxis:

```bash
variable=$(( operando1 operador operando2 ))
```

### Operadores disponibles:

| Operador | Significado     |
|----------|-----------------|
| `+`      | Suma            |
| `-`      | Resta           |
| `*`      | Multiplicación  |
| `/`      | División entera |
| `%`      | Módulo          |

### Ejemplos:

```bash
resultado=$((10 * 70))
echo $resultado
# 700

valor=$((20 + 5))
echo $valor
# 25

division=$((100 / 4))
echo $division
# 25
```

**Explicación**:

- `((...))`: Evaluación aritmética.
- El resultado se asigna a la variable con `=`.
- Se puede usar directamente en expresiones condicionales.

### Ventajas:

- Rápido y sin dependencias externas.
- Ideal para operaciones enteras simples.
- Muy útil en scripts básicos.

---

## ✅ Solución 2: Usar `bc` (Basic Calculator)

`bc` es una **calculadora de precisión arbitraria** para el terminal. Soporta:
- Operaciones decimales
- Potencias
- Paréntesis anidados
- Control de escala (número de decimales)

### Instalación:

```bash
sudo apt install bc
```

### Uso básico:

```bash
echo "200 * 10" | bc
# 2000
```

```bash
echo "8600 / 3" | bc
# 2866
```

### Con decimales:

```bash
echo "scale=2; 8600 / 3" | bc
# 2866.66
```

**Explicación**:

- `"200 * 10"`: Es la expresión matemática.
- `| bc`: Pasa la cadena como entrada a la calculadora `bc`.
- `scale=2`: Indica cuántos decimales queremos mostrar.

### Ventajas:

- Permite decimales.
- Más potente y versátil.
- Recomendado para scripts más avanzados de administración.

---

## 💡 ¿Por qué es útil esto?

Como administrador de sistemas o creador de scripts, puedes necesitar:

- Calcular porcentajes de uso
- Comparar tamaños de archivos
- Generar informes automáticos
- Hacer scripts dinámicos con condiciones numéricas

---

## ✅ Resumen

| Método      | Precisión | Soporta decimales | Complejidad | Dependencia |
|-------------|-----------|-------------------|-------------|-------------|
| `$((...))`  | Entera    | ❌ No              | Baja        | ❌ No        |
| `bc`        | Alta      | ✅ Sí              | Media       | ✅ Sí (`bc`) |

Tener dominio de ambas formas te permite elegir la herramienta adecuada según el contexto del script que estés creando.

# Lección 8. Operadores de comparación en Bash

En Bash, los operadores de comparación son fundamentales para realizar decisiones lógicas dentro de los scripts. Se usan para comparar números, cadenas y la existencia de archivos o variables.

---

## 📊 Tipos de operadores

### 🔢 Comparación numérica

| Operador | Significado        |
|----------|--------------------|
| `-eq`    | Igual a            |
| `-ne`    | No igual a         |
| `-gt`    | Mayor que          |
| `-ge`    | Mayor o igual que  |
| `-lt`    | Menor que          |
| `-le`    | Menor o igual que  |

---

### 🔤 Comparación de cadenas

| Operador | Significado       |
|----------|-------------------|
| `=`      | Igual a           |
| `!=`     | No igual a        |
| `>`      | Mayor (alfabético)|
| `<`      | Menor (alfabético)|

> ⚠️ En comparaciones de cadenas, es recomendable usar `[[ ... ]]` para mayor compatibilidad.

---

### ⚙️ Operadores lógicos

| Operador | Significado       |
|----------|-------------------|
| `-a`     | AND lógico         |
| `-o`     | OR lógico          |
| `!`      | Negación (NOT)     |

---

### 📁 Existencia de archivos

| Operador | Significado                        |
|----------|------------------------------------|
| `-e`     | Existe el archivo                  |
| `-f`     | Es un archivo normal               |
| `-d`     | Es un directorio                   |
| `-s`     | No está vacío                      |
| `-r`     | Tiene permisos de lectura          |
| `-w`     | Tiene permisos de escritura        |
| `-x`     | Tiene permisos de ejecución        |

---

## 🛠️ Comandos para comparar

### `test`

Es un comando integrado que evalúa condiciones. Devuelve `0` si es verdadero, `1` si es falso.

### `[ ... ]`

Forma alternativa de `test`. **Debe haber espacios** entre los corchetes y los elementos.

### `[[ ... ]]`

Mejora la sintaxis de `[ ... ]` y es más segura para comparar cadenas con operadores como `>` y `<`.

---

## 🔎 Ejemplo práctico – Comparaciones numéricas

```bash
var1=30
var2=3000
```

```bash
test $var1 -gt $var2
echo $?
# Resultado: 1 → Falso, 30 no es mayor que 3000
```

```bash
test $var1 -eq $var2
echo $?
# Resultado: 1 → Falso
```

```bash
test $var1 -ne $var2
echo $?
# Resultado: 0 → Verdadero, 30 no es igual a 3000
```

```bash
test $var1 -ge $var2
echo $?
# Resultado: 1 → Falso
```

```bash
test $var1 -le $var2
echo $?
# Resultado: 0 → Verdadero
```

```bash
test $var1 -lt $var2
echo $?
# Resultado: 0 → Verdadero
```

---

## 🧪 Comparación con `[ ... ]` (corchetes)

```bash
[ $var1 -lt $var2 ]
echo $?
# Resultado: 0 → Verdadero
```

> ⚠️ `[ $var1 -lgt $var2 ]` → Esto es incorrecto: `-lgt` no es un operador válido.

---

## 🧵 Comparaciones de cadenas de texto

```bash
var1="hola mundo"
var2="adios mundo"

test "$var1" != "$var2"
echo $?
# Resultado: 0 → Verdadero, son diferentes
```

### O usando `[[ ... ]]`:

```bash
[[ "$var1" > "$var2" ]]
echo $?
```

> 🧠 Esta comparación es alfabética. `"hola mundo"` es mayor alfabéticamente que `"adios mundo"`.

---

## 🧰 Script de ejemplo completo con comentarios

Archivo `comparar.sh`:

```bash
#!/bin/bash

# Variables de ejemplo
a=100
b=200

# Comparamos si son iguales
if [ $a -eq $b ]; then
  echo "a y b son iguales"
else
  echo "a y b son diferentes"
fi

# Comprobamos si a es menor que b
if [ $a -lt $b ]; then
  echo "a es menor que b"
fi

# Comparamos cadenas
cadena1="David"
cadena2="Rodríguez"

if [[ "$cadena1" != "$cadena2" ]]; then
  echo "Las cadenas son diferentes"
fi
```

### Explicación jerárquica:

- `#!/bin/bash` → Indica el intérprete.
- `a=100`, `b=200` → Definición de variables.
- `[ $a -eq $b ]` → Comparación numérica con `test`.
- `[[ "$cadena1" != "$cadena2" ]]` → Comparación segura de cadenas.
- `if ... fi` → Estructura de control condicional.

---

## ✅ Resumen

| Tipo de comparación | Usar operadores         | Recomendación           |
|---------------------|-------------------------|--------------------------|
| Números             | `-eq`, `-ne`, `-lt`...  | `test`, `[ ... ]`        |
| Cadenas             | `=`, `!=`, `>`, `<`     | `[[ ... ]]`              |
| Archivos            | `-e`, `-f`, `-d`, etc.  | `test`, `[ ... ]`        |
| Lógica              | `-a`, `-o`, `!`         | Agrupar con `[[ ... ]]`  |

Dominar estos operadores te permite tomar decisiones complejas dentro de tus scripts Bash.

# Lección 9. Operadores para buscar subcadenas en Bash

En Bash podemos usar expresiones de comparación para comprobar si una **cadena contiene una subcadena**. Esto es muy útil para búsquedas rápidas sin necesidad de usar herramientas externas como `grep`.

---

## 🔍 Sintaxis básica

Para comprobar si una variable contiene una subcadena:

```bash
var1="SoyUnsubstringABuscar, me encuentras?"
[[ "$var1" == *"substringABuscar"* ]]
echo $?
```

### Explicación:

- `[[ ... ]]`: Usamos corchetes dobles porque son más robustos para operaciones con strings.
- `== *subcadena*`: El asterisco actúa como comodín antes y después de la subcadena.
- `echo $?`: Muestra el resultado de la comparación:
  - `0`: Verdadero (la subcadena está presente)
  - `1`: Falso (la subcadena no está)

---

## 🛠️ Ejemplo práctico: buscar una subcadena en un fichero

Queremos hacer un script que reciba dos argumentos:
1. Un fichero de texto
2. La cadena a buscar

### Paso 1: Crear el fichero de texto

```bash
nano ficheroTexto
```

Contenido del fichero:

```
hola soy pablo
que tal estas
espero que todo bien
```

### Paso 2: Crear el script `buscarTexto.sh`

```bash
#!/bin/bash

fichero=$1               # Guardamos el nombre del fichero (primer argumento)
palabraBuscada=$2        # Guardamos la cadena a buscar (segundo argumento)

texto=$(cat $fichero)    # Leemos el contenido completo del fichero

[[ "$texto" == *$palabraBuscada* ]]
echo $?                  # Mostramos el resultado de la comparación
```

### Paso 3: Dar permisos de ejecución

```bash
chmod u+x buscarTexto.sh
```

### Ejecución del script con ejemplos:

```bash
./buscarTexto.sh ficheroTexto soy
# Resultado: 0 → "soy" está presente

./buscarTexto.sh ficheroTexto sop
# Resultado: 1 → "sop" no está en el texto

./buscarTexto.sh ficheroTexto "soy p"
# Resultado: 0 → "soy p" sí está como subcadena literal

./buscarTexto.sh ficheroTexto soy e
# Resultado: 0 → Está porque "soy" y "e" aparecen en el texto, aunque no consecutivamente

./buscarTexto.sh ficheroTexto "soy e"
# Resultado: 1 → No está como subcadena literal completa
```

---

## 🧠 Consideraciones importantes

- **Espacios**: si la subcadena contiene espacios, se debe encerrar entre comillas `"..."`.
- **Sensibilidad a mayúsculas/minúsculas**: Bash distingue entre `Hola` y `hola`.
- **Evaluación completa del contenido**: Al usar `cat`, todo el contenido del fichero se almacena como una única cadena.

---

## ✅ Resumen

| Elemento                         | Descripción                                                  |
|----------------------------------|--------------------------------------------------------------|
| `[[ "$texto" == *$cadena* ]]`    | Evalúa si `texto` contiene la subcadena `cadena`             |
| `echo $?`                        | Muestra el resultado: `0` si es true, `1` si es false        |
| `cat fichero` → `texto=$(...)`   | Permite tratar el fichero como una cadena única              |

Este método es útil cuando queremos validar rápidamente si una palabra o frase existe dentro de un contenido sin depender de `grep` o `awk`.

> 🎯 Ideal para scripts simples de validación, automatización o pruebas en línea.

---
# Lección 10. Operadores lógicos en Bash

Los **operadores lógicos** permiten realizar varias comprobaciones combinando condiciones en una sola instrucción.

---

## ⚙️ Operadores disponibles

| Operador | Significado    | Ejemplo                                 |
| -------- | -------------- | --------------------------------------- |
| `&&`     | AND lógico (y) | `cond1 && cond2` → ambas deben ser true |
| \|\|     | OR             |                                         |
| `!`      | Negación (NOT) | `!cond` → invierte el resultado         |

---

## 🧪 Ejemplo con variables

```bash
v1=20
v2=30
v3=40
v4=50
```

---

### ✅ Ejemplo 1 – AND lógico (`&&`)

```bash
test $v1 -ne $v2 && test $v3 -gt $v4
echo $?
```

- `test $v1 -ne $v2` → `20 != 30` → **verdadero**
    
- `test $v3 -gt $v4` → `40 > 50` → **falso**
    

El resultado final con `&&` es **falso**.  
Salida:

```
1
```

---

### ✅ Ejemplo 2 – AND con condiciones verdaderas

```bash
test $v1 -ne $v2 && test $v3 -lt $v4
echo $?
```

- `20 != 30` → verdadero
    
- `40 < 50` → verdadero
    

Ambas son verdaderas → resultado:

```
0
```

---

### ✅ Ejemplo 3 – OR lógico (`||`)

```bash
test $v1 -ne $v2 || test $v3 -gt $v4
echo $?
```

- Primera condición: `20 != 30` → verdadero
    
- Con OR, no importa la segunda porque al menos una ya es verdadera.
    

Salida:

```
0
```

---

### ✅ Ejemplo 4 – Negación (`!`)

```bash
test ! $v1 -eq $v2
echo $?
```

- `$v1 -eq $v2` → `20 == 30` → falso
    
- `! falso` → verdadero
    

Salida:

```
0
```

---

## 🧠 Claves prácticas

1. `&&` exige que **todas** las condiciones sean verdaderas.

2. `||` se cumple si **al menos una** condición es verdadera.

3. `!` invierte el resultado de la expresión.

4. El valor devuelto se consulta con `$?`:
    
    - `0` → verdadero
        
    - `1` → falso

---

## ✅ Resumen

Los operadores lógicos permiten:

- Encadenar comparaciones (`&&`, `||`)

- Negar resultados (`!`)

- Realizar tests más expresivos en scripts sin necesidad de estructuras largas de `if`.

---

# Lección 11. Operadores de existencia en Bash

Los **operadores de existencia** permiten comprobar si un archivo o directorio existe y qué tipo de permisos tiene.  
Se usan con `test`, `[ ... ]` o `[[ ... ]]`.

---

## 📌 Principales operadores

|Operador|Significado|
|---|---|
|`-e`|Comprueba si un fichero existe|
|`-f`|Comprueba si existe y es un fichero **regular** (texto, binario, script…)|
|`-d`|Comprueba si existe y es un **directorio**|
|`-r`|Comprueba si tiene permisos de **lectura**|
|`-w`|Comprueba si tiene permisos de **escritura**|
|`-x`|Comprueba si tiene permisos de **ejecución**|

> El resultado se evalúa en `$?`:
> 
> - `0` → verdadero
>     
> - `1` → falso
>     

---

## 🧪 Ejemplos prácticos en terminal

```bash
ls
# argumentos.sh  buscarTexto.sh  entorno.sh  entorno_awk.sh  ficheroTexto  holamundo.sh pideDatos.sh
```

---

### 1. Comprobar existencia de un fichero

```bash
test -e ficheroTexto
echo $?
# 0 → existe

test -e ficheroTexts
echo $?
# 1 → no existe
```

---

### 2. Comprobar directorio

```bash
mkdir midirectorio

test -d midirectorio/
echo $?
# 0 → sí es un directorio

test -f midirectorio/
echo $?
# 1 → no es un fichero regular
```

---

### 3. Comprobar fichero regular

```bash
test -f holamundo.sh
echo $?
# 0 → sí es un fichero regular
```

```bash
test -f ficheroTexto
echo $?
# 0 → existe como fichero regular
```

---

### 4. Comprobar permisos

Creamos un archivo `secret` y cambiamos sus permisos:

```bash
touch secret
chmod 300 secret   # permisos: escritura y ejecución, sin lectura
```

- Lectura:
    

```bash
test -r secret
echo $?
# 1 → no tiene lectura
```

- Escritura:
    

```bash
test -w secret
echo $?
# 0 → sí tiene escritura
```

- Ejecución:
    

```bash
test -x secret
echo $?
# 0 → sí tiene ejecución
```

---

## 📝 Script de ejemplo: `existeFichero.sh`

```bash
#!/bin/bash
fichero=$1

# Comprobamos si existe
echo "Existe fichero $fichero ?"
test -e $fichero
echo $?

# Comprobamos si es directorio
echo "Es un directorio $fichero ?"
test -d $fichero
echo $?

# Comprobamos si es regular
echo "Es un fichero regular $fichero ?"
test -f $fichero
echo $?
```

Dar permisos y ejecutar:

```bash
chmod u+x existeFichero.sh
./existeFichero.sh ficheroTexto
```

Salida:

```
Existe fichero ficheroTexto ?
0
Es un directorio ficheroTexto ?
1
Es un fichero regular ficheroTexto ?
0
```

---

## ✅ Resumen

- `-e` verifica existencia.
    
- `-f` y `-d` diferencian fichero regular de directorio.
    
- `-r`, `-w`, `-x` validan permisos.
    
- El valor de retorno (`$?`) permite encadenar comprobaciones en scripts.
    

---

# Lección 12. If, elif, else en Bash

Las estructuras condicionales permiten **bifurcar un script** según se cumplan o no ciertas condiciones.  
Se usan junto con comparaciones (`test`, `[ ... ]`, `[[ ... ]]`).

---

## 🔑 Sintaxis básica

```bash
if [ condicion ]
then
    # Instrucciones si se cumple
elif [ otra_condicion ]
then
    # Instrucciones si no se cumple la primera pero sí esta
else
    # Instrucciones si no se cumple ninguna
fi
```

> La palabra clave para cerrar el bloque siempre es `fi`.

---

## 🧪 Ejemplo 1 – Comparación simple

```bash
numero=200
echo "Introduce número a buscar:"
read jugador

if test $numero -eq $jugador
then
    echo "¡Acertaste!"
elif test $numero -gt $jugador
then
    echo "Tu número es menor"
else
    echo "Tu número es mayor"
fi
```

### Explicación:

- `test $numero -eq $jugador` → ¿son iguales?

- `elif` → segunda condición: ¿es mayor?

- `else` → caso por defecto si ninguna se cumple.


---

## 🧪 Ejemplo 2 – Juego de adivinar

Archivo `jugador.sh`:

```bash
#!/bin/bash

adivina=$1

echo -n "Jugador introduce un número (hasta 5 dígitos): "
read numero

if test $adivina -eq $numero
then
echo "¡Milagro, has acertado!"
elif test $adivina -lt $numero
then
echo "El número buscado es menor que el tuyo"
else
echo "El número buscado es mayor que el tuyo"
fi

echo "El número del jugador es: $numero"
echo "El número buscado es: $adivina"
```

### Ejecución:

```bash
chmod +x jugador.sh
./jugador.sh 329
```

Salida posible:

```
Jugador introduce un número (hasta 5 dígitos): 200
El número buscado es mayor que el tuyo
El número del jugador es: 200
El número buscado es: 329
```

---

## 🧠 Claves prácticas

1. **Comparadores numéricos** → `-eq`, `-lt`, `-gt`, etc.

2. **Comparadores de cadenas** → `=`, `!=`, etc.

3. `elif` evita anidar demasiados `if`.

4. Siempre terminar con `fi`.

5. Usar `[[ ... ]]` en lugar de `test` cuando compares cadenas con operadores `<` o `>`.

---

## ✅ Resumen

- `if` evalúa una condición.

- `elif` permite encadenar múltiples comprobaciones.

- `else` se ejecuta si ninguna condición se cumple.

- Ideal para **scripts interactivos** como validadores, menús o pequeños juegos.

---

# Lección 13. If – Control de argumentos en Bash

En muchos scripts es necesario **validar los argumentos** que se pasan al ejecutarlo. Esto se hace con estructuras condicionales (`if`) y variables especiales como:

- `$#` → número de argumentos recibidos.
    
- `$0` → nombre del script.
    
- `$1`, `$2`, … → argumentos posicionales.
    

---

## 📌 Ejemplo básico: comprobar número de argumentos

Archivo `control_argumentos.sh`:

```bash
#!/bin/bash

# Comprobación de argumentos
if test $# -ne 2
then
echo "Uso: $0 <numero1> <numero2>"
exit
fi

resultado=$(($1 * $2))
echo "El resultado de la operación $1 * $2 es: $resultado"
```

---

## 🔎 Explicación línea a línea

- `if test $# -ne 2`  
    Verifica si el número de argumentos (`$#`) es distinto de 2.

- `echo "Uso: $0 <numero1> <numero2>"`  
    Muestra al usuario cómo debe ejecutar el script.

- `exit`  
    Finaliza el script si la condición no se cumple.

- `resultado=$(($1 * $2))`  
    Multiplica los dos argumentos recibidos.

- `echo`  
    Imprime el resultado de la operación.

---

## 🧪 Ejecución y resultados

Dar permisos de ejecución:

```bash
chmod +x control_argumentos.sh
```

Ejecutar sin argumentos:

```bash
./control_argumentos.sh
# Uso: ./control_argumentos.sh <numero1> <numero2>
```

Ejecutar con un argumento:

```bash
./control_argumentos.sh 3
# Uso: ./control_argumentos.sh <numero1> <numero2>
```

Ejecutar con los dos argumentos correctos:

```bash
./control_argumentos.sh 3 2
# El resultado de la operación 3 * 2 es: 6
```

Ejecutar con más de dos argumentos:

```bash
./control_argumentos.sh 3 2 4
# Uso: ./control_argumentos.sh <numero1> <numero2>
```

---

## ✅ Resumen

- Validar argumentos evita errores en la ejecución.

- `$#` permite comprobar cuántos parámetros se pasaron.

- `$0` muestra el nombre del script, útil para dar instrucciones de uso.

- Condicionales (`if`) permiten detener el script si los argumentos no son válidos.

---

# Lección 14. Case y menús en Bash

El comando `case` en Bash es equivalente al `switch` en otros lenguajes de programación.  
Es muy útil cuando necesitamos implementar **menús interactivos** en los scripts para que el usuario pueda seleccionar entre varias opciones.

---

## 📌 Sintaxis básica

```bash
case $variable in
    patron1)
        # Instrucciones si coincide con patron1
        ;;
    patron2)
        # Instrucciones si coincide con patron2
        ;;
    *)
        # Instrucciones si no coincide con ningún patrón (opción por defecto)
        ;;
esac
```

- `;;` marca el fin de cada bloque de instrucciones.
    
- `*` funciona como **caso por defecto**, cuando no hay coincidencia.
    

---

## 📌 Ejemplo simple

```bash
#!/bin/bash
echo "Introduce opción:"
read opcion

case $opcion in
    1)
        echo "Has elegido la opción 1"
        ;;
    2)
        echo "Has elegido la opción 2"
        ;;
    *)
        echo "Opción no válida"
        ;;
esac
```

---

## 📌 Ejemplo avanzado: menú interactivo

Archivo `menu.sh`:

```bash
#!/bin/bash
log="/var/log"

echo "===== Menú [Título Script] ====="
echo "1) Listar el fichero /etc/passwd"
echo "2) Listar el directorio /etc"
echo "3) Comprobar existencia del directorio $log"
echo "4) Comprobar existencia de usuario"
echo "5) Finalizar ejecución"
echo -n "Introduce una opción: "
read opcion

case $opcion in
    1)
        cat /etc/passwd
        ;;
    2)
        ls /etc
        ;;
    3)
        if [ -d $log ]; then
            echo "El directorio $log existe"
        else
            echo "El directorio $log no existe"
        fi
        ;;
    4)
        echo -n "Introduce el usuario a buscar: "
        read usuario
        cat /etc/passwd | grep $usuario
        if [ $? -eq 0 ]; then
            echo "El usuario $usuario existe"
        else
            echo "El usuario $usuario no existe"
        fi
        ;;
    5)
        echo "Has decidido cerrar el script... saliendo..."
        exit
        ;;
    *)
        echo "Opción no válida"
        echo "Introduce un valor entre 1 y 5"
        ;;
esac
```

---

## 🧪 Ejecución

1. Dar permisos de ejecución:

```bash
chmod +x menu.sh
```

2. Ejecutar el script:

```bash
./menu.sh
```

📌 Ejemplo de interacción:

```
===== Menú [Título Script] =====
1) Listar el fichero /etc/passwd
2) Listar el directorio /etc
3) Comprobar existencia del directorio /var/log
4) Comprobar existencia de usuario
5) Finalizar ejecución
Introduce una opción: 2
```

Resultado:

```
adduser.conf  group  hosts  ...
```

---

## ✅ Resumen

- `case` permite simplificar múltiples condiciones.

- Es ideal para construir **menús interactivos** en scripts.

- Puede combinarse con `if` y comandos como `grep` para validaciones.

- Próximamente se combinará con **bucles** y **funciones** para crear menús persistentes y reutilizables.

---

# Lección 15. Bucle `for` en Bash

Los **bucles** son estructuras de iteración que permiten ejecutar un bloque de instrucciones repetidamente.  
En Bash, los más comunes son **`for`** y **`while`**.

El bucle `for` se usa cuando conocemos de antemano una lista de elementos sobre los que queremos iterar.

---

## 📌 Sintaxis general de `for`

```bash
for variable in lista
do
    # Instrucciones
done
```

- La **lista** puede definirse explícitamente o generarse dinámicamente con comandos.

- Cada elemento de la lista se asigna a la **variable** en cada iteración.

---

## 📌 Ejemplo básico

```bash
#!/bin/bash

lista=$(ls /)   # Guardamos en la variable "lista" el contenido del directorio raíz

for i in $lista
do
    echo "Elemento: $i"
done
```

Este script recorrerá todos los elementos del directorio `/` y los imprimirá uno a uno.

---

## 📌 Ejemplo práctico: contar directorios y ficheros

Archivo `for.sh`:

```bash
#!/bin/bash

if [ $# -eq 1 ]
then
    directorios=0
    regulares=0
    recurso=$1

    for i in $(ls $recurso)
    do
        if [ -d $recurso/$i ]
        then
            directorios=$(($directorios + 1))
        fi

        if [ -f $recurso/$i ]
        then
            regulares=$(($regulares + 1))
        fi
    done
else
    echo "Usage: bash for.sh <recurso a observar>"
    exit
fi

echo "En $recurso hay $directorios directorios"
echo "En $recurso hay $regulares ficheros regulares"
```

---

## 🧪 Ejecución

1. Dar permisos:

```bash
chmod +x for.sh
```

2. Ejecutar con un directorio como argumento:

```bash
./for.sh /etc
```

📌 Salida de ejemplo:

```
En /etc hay 43 directorios
En /etc hay 55 ficheros regulares
```

---

## ✅ Resumen

- `for` permite recorrer listas o resultados de comandos.

- Es útil para aplicar una operación repetida sobre múltiples elementos.

- Puede combinarse con condicionales (`if`) para procesar directorios, ficheros u otro tipo de datos.

---

# Lección 16. Bucle  `while` en Bash

## Concepto

- Los bucles `while` permiten ejecutar instrucciones **mientras se cumpla una condición**.

- Son muy útiles cuando no sabemos de antemano cuántas veces se repetirá la iteración.

---

### 📌 Ejemplo básico

```bash
tope=30
i=0

while [ $i -lt $tope ]
do
    echo $i
    i=$(($i+1))
done
```

👉 Esto imprime los números del **0 al 29**.

---

### 📌 Ejemplo ampliado (`bucle.sh`)

```bash
#!/bin/bash

tope=100
i=1

while [ $i -le $tope ]
do
    echo $i
    i=$(($i+1))
done
```

👉 Imprime los números del **1 al 100**.

---

### 📌 Ejemplo práctico: leer líneas de un fichero (`leerlineas.sh`)

```bash
#!/bin/bash

if [ $# -eq 1 ]
then
    filename=$1
    if [ -e $filename ]
    then
        while read linea
        do
            echo $linea
        done < $filename
    else
        echo "No has introducido un fichero válido"
        exit
    fi
else
    echo "Usage: $0 <filename>"
    exit
fi
```

👉 Este script **lee línea por línea** un archivo y muestra su contenido.

---

### 📌 Ejemplo práctico con `md5sum`

El script se mejora para calcular el **hash MD5** de cada línea (como si fuera una lista de contraseñas):

```bash
#!/bin/bash

if [ $# -eq 2 ]
then
    filename=$1
    output=$2
    if [ -e $filename ]
    then
        while read linea
        do
            echo -n $linea | md5sum | cut -f1 -d' ' >> $output
        done < $filename
    else
        echo "No has introducido un fichero válido"
        exit
    fi
else
    echo "Usage: $0 <filename> <output>"
    exit
fi
```

👉 Ahora el script recibe:

- `$1`: archivo de entrada con contraseñas (`pass`).

- `$2`: archivo de salida con los hashes (`fichero`).


Ejemplo de uso:

```bash
./leerlineas.sh pass fichero
```

Resultado:

- En `pass`: lista de contraseñas.

- En `fichero`: lista de hashes MD5 correspondientes.

---

📖 **Resumen de la lección**

- `while` ejecuta instrucciones **mientras la condición sea verdadera**.

- Puede usarse con contadores (`i`), lectura de ficheros (`while read`), o combinando con comandos (`md5sum`, `grep`, etc.).

- Es muy flexible para procesar entradas dinámicas o desconocidas.

---

# Lección 17. Funciones

## 📌 Definición

Las funciones permiten **reutilizar código** agrupando instrucciones bajo un nombre.

Sintaxis:

```bash
nombre_funcion() {
    [instrucciones]
}
```

Para ejecutar la función:

```bash
nombre_funcion
```

---

## 📌 Ejemplo básico

```bash
menuScript() {
    echo "Menu [Titulo script]"
    echo "===================="
    echo "1) listar el fichero /etc/passwd"
    echo "2) listar el directorio /etc"
    echo "3) comprobar existencia del directorio /var/log"
    echo "4) comprobar existencia de usuario"
    echo "5) finalizar ejecución"
}

menuScript   # llamada a la función
```

---

## 🔢 Pasar argumentos a funciones

Dentro de una función, los argumentos se manejan igual que en un script:

- `$1`, `$2`, … → parámetros individuales.
    
- `$#` → número de argumentos pasados.
    
- `$@` → todos los argumentos.
    

---

### 📌 Ejemplo: función para sumar

```bash
sumar() {
    echo "Argumentos que nos pasan: $#"
    resultado=$(($1 + $2))
    echo $resultado
}

sumar 30 29
```

👉 Resultado:

```
Argumentos que nos pasan: 2
59
```

---

### 📌 Validar número de argumentos

```bash
sumar() {
    if [ $# -eq 2 ]
    then
        resultado=$(($1 + $2))
        echo $resultado
    else
        echo "Valores introducidos incorrectamente"
    fi
}

sumar 30 40   # Devuelve 70
sumar 10      # Devuelve "Valores introducidos incorrectamente"
```

---

### 📌 Devolver valores de funciones

En Bash, no se devuelve con `return` (solo permite valores 0–255).  
Se recomienda **usar `echo`** y capturar el resultado:

```bash
resultado=$(sumar 20 30)
echo "El resultado es: $resultado"
```

👉 Salida:

```
El resultado es: 50
```

---

📖 **Resumen de la lección**

- Las funciones en Bash **organizan y reutilizan código**.

- Se invocan escribiendo su nombre.

- Admiten argumentos (`$1`, `$2`, …).

- Es buena práctica validar `$#` para asegurar que reciben los parámetros necesarios.

- Los valores se devuelven con `echo` y se capturan con sustitución de comandos `$( )`.

---

# Lección 18. Funciones (importar)

## 📌 Concepto principal

- En **Bash** se pueden **importar funciones definidas en otro archivo**, parecido a cómo funciona un `import` en otros lenguajes de programación.
    
- Esto permite **reutilizar código** y mantener los scripts más organizados.
    

---

### 📂 Sintaxis para importar funciones

```bash
#!/bin/bash

source ./nombre_fichero_script.sh
```

- `source` (o `.`) carga y ejecuta el contenido de otro archivo dentro del script actual.
    
- Las funciones definidas en el archivo importado se pueden invocar como si estuvieran en el mismo script.
    

---

### 📂 Ejemplo básico

**Archivo:** `funciones.sh`

```bash
#!/bin/bash

menuScript(){
    echo "Menu [Titulo script]"
    echo "====================="
    echo "1) listar el fichero /etc/passwd"
    echo "2) listar el directorio /etc"
    echo "3) comprobar existencia del directorio /var/log"
    echo "4) comprobar existencia de usuario"
    echo "5) finalizar ejecucion"
    echo
}
```

**Archivo:** `usarSource.sh`

```bash
#!/bin/bash

# Importamos las funciones del archivo funciones.sh
source ./funciones.sh

# Llamamos a la función definida en funciones.sh
menuScript
```

📌 **Ejecución:**

```bash
chmod u+x usarSource.sh
./usarSource.sh
```

**Salida:**

```
Menu [Titulo script]
=====================
1) listar el fichero /etc/passwd
2) listar el directorio /etc
3) comprobar existencia del directorio /var/log
4) comprobar existencia de usuario
5) finalizar ejecucion
```

---

### 🔄 Ejemplo con bucle y menú interactivo

En el script `usarSource.sh` se añade un **while** y un **case** para gestionar opciones:

```bash
#!/bin/bash

source ./funciones.sh

salida=0
while [ $salida -ne 5 ]
do
    menuScript
    echo "Introduce una opcion:"
    read opcion

    case $opcion in
        1) cat /etc/passwd ;;
        2) ls /etc ;;
        3) 
            log="/var/log"
            if [ -d $log ]; then
                echo "El directorio $log existe"
            else
                echo "El directorio $log no existe"
            fi
            ;;
        4) 
            echo "Introduce el usuario a buscar:"
            read usuario
            cat /etc/passwd | grep $usuario
            if [ $? -eq 0 ]; then
                echo "El usuario $usuario existe"
            else
                echo "El usuario $usuario no existe"
            fi
            ;;
        5) 
            echo "Has decidido cerrar el script... saliendo..."
            salida=5
            ;;
        *) 
            echo "Has introducido una opcion no valida"
            echo "Introduce una opcion entre 1 y 5"
            ;;
    esac
done
```

---

# Lección 19. Post Explotación Automatizada

### 🔹 Concepto

La post explotación consiste en **automatizar la ejecución de instrucciones** a partir de un fichero de entrada.  
El fichero contiene pares de valores con el formato:

```
InstruccionAEjecutar : NombreFicheroResultante
```

Cada línea indica una **instrucción a ejecutar** y el **fichero donde guardar el resultado**.

---

### 🔹 Script `postExplotacionAut.sh`

```bash
#!/bin/bash

if [ $# -eq 1 ]
then
    filename=$1
    if [ -e $filename ]
    then
        while read linea
        do
            instruccion=`echo $linea | cut -f1 -d':'`
            output=`echo $linea | cut -f2 -d':'`

            $instruccion > $output
        done < $filename
    else
        echo "Fichero no existe"
    fi
else
    echo "Usage: $0 <filename>"
fi
```

---

### 🔹 Funcionamiento

1. El script recibe **1 argumento obligatorio** → el fichero de instrucciones.

2. Comprueba que el fichero exista.

3. Recorre cada línea del fichero, separando:
    
    - **Comando** → antes de los `:`
        
    - **Fichero de salida** → después de los `:`

4. Ejecuta el comando y redirige la salida al fichero correspondiente.

---

### 🔹 Ejemplo de fichero `instrucciones`

```
ps aux:post/ps.txt
cat /etc/passwd:post/passwd.txt
netstat -tulpn:post/netstat.txt
```

📌 Esto generará dentro del directorio `post/` tres ficheros con la información recolectada:

- `ps.txt` → lista de procesos

- `passwd.txt` → usuarios del sistema

- `netstat.txt` → conexiones de red activas

---

### 🔹 Problemas comunes

- Si no se encuentra un comando, devolverá `command not found`.

- En el ejemplo fue necesario instalar `net-tools` para que funcionara `netstat`.

```bash
apt install net-tools
```

---

✅ Con este enfoque podemos crear **scripts automatizados de recolección de información post-explotación**, muy útiles para auditorías o análisis de intrusión.

---

# Lección 20. Escáner automático con Nmap

## 🎯 Objetivo

- Crear un **script automatizado en Bash** que permita al usuario seleccionar el tipo de escaneo que quiere realizar con Nmap.

- Reutilizar funciones para pedir **dirección IP** y/o **puertos** al usuario.

- Centralizar en un menú las opciones más usadas de Nmap.

---

## 📌 Tipos de escaneos incluidos

### 1. Ejecución básica

```bash
nmap <IP>
```

- Escaneo simple sobre la IP indicada.

- Detecta puertos abiertos de forma estándar.

---

### 2. Descubrimiento de hosts con ARP

```bash
nmap -sn <IP> --disable-arp-ping
```

- Se utiliza en redes locales (LAN).

- Detecta máquinas activas usando **ARP requests**.

- No hace escaneo de puertos, solo identifica hosts.

---

### 3. Descubrimiento con **Ping Sweep** (no ARP)

```bash
nmap -sn -PR <IP>
```

- Realiza un **ping** ICMP clásico para descubrir qué hosts responden.

- Útil fuera de la LAN (cuando ARP no es aplicable).

---

### 4. Escaneo de puertos con **SYN Scan**

```bash
nmap -p <PUERTO> -sS <IP>
```

- Técnica **half-open**: envía SYN y analiza la respuesta sin completar la conexión TCP.

- Muy rápido y común en auditorías de seguridad.

- Se puede especificar un **rango de puertos**:

```bash
-p 20-500,80,443
```

---

### 5. Escaneo completo con **-A**

```bash
nmap -A <IP>
```

- Incluye varias funciones avanzadas:
    
    - Detección del **sistema operativo**.
        
    - Detección de **versiones de servicios**.
        
    - Script scanning.
        
    - Traceroute.

- Más lento pero más **exhaustivo**.

---

### 6. Salida

- Opción para finalizar el script de manera controlada.

---

## 🖥️ Estructura del Script `nmap.sh`

1. **Funciones auxiliares**
    
    - `Mensajes()` → Muestra mensajes de ayuda (ej. pedir IP o puerto).
        
    - `LeerIP()` → Pide una IP al usuario.
        
    - `LeerPuerto()` → Pide un puerto o rango.
        
2. **Menú principal (while + case)**

```bash
#!/bin/bash

# Script: nmap.sh
# Escáner automático con Nmap (Lección 20)

# Función para mostrar mensajes
Mensajes(){
    if [ $# -eq 1 ]
    then
        mensaje=$1
        case $mensaje in
            0) echo -n "Introduce una dirección IP: " ;;
            1) echo -n "Introduce un puerto o rango de puertos (ej. 22, 80, 20-500, 20-30): " ;;
            2) echo "Saliendo..." ;;
            *) echo "Error en los argumentos" ;;
        esac
    else
        echo "Error en los argumentos"
    fi
}

# Función para leer una IP
LeerIP(){
    read ip
    echo $ip
}

# Función para leer un puerto
LeerPuerto(){
    read puerto
    echo $puerto
}

# ========================
# PROGRAMA PRINCIPAL
# ========================

if [ $# -eq 0 ]
then
    salida=0
    while [ $salida -ne 6 ]
    do
        echo "===== Nmap Script Beginners ====="
        echo
        echo "1) Nmap ejecución básica"
        echo "2) Nmap descubrimiento host (ARP)"
        echo "3) Nmap descubrimiento host (Ping sweep)"
        echo "4) Nmap portscan (SYN Scan)"
        echo "5) Nmap -A (todos los parámetros)"
        echo "6) Salir"
        echo
        echo -n "Introduce opción: "
        read opcion

        case $opcion in
            1)  Mensajes 0
                ip=$(LeerIP)
                nmap $ip
                ;;
            2)  Mensajes 0
                ip=$(LeerIP)
                nmap -sn -PR $ip
                ;;
            3)  Mensajes 0
                ip=$(LeerIP)
                nmap -sn -P $ip --disable-arp-ping
                ;;
            4)  Mensajes 0
                ip=$(LeerIP)
                Mensajes 1
                puerto=$(LeerPuerto)
                nmap -p $puerto -sS $ip
                ;;
            5)  Mensajes 0
                ip=$(LeerIP)
                nmap -A $ip
                ;;
            6)  Mensajes 6
                salida=6
                ;;
            *)  echo "Opción no válida. Introduce un número entre 1 y 6."
                ;;
        esac
    done
else
    echo "Uso: $0"
fi
```

---

### 🔎 Explicación rápida:

- **Menú** con 6 opciones → cada una lanza un tipo de escaneo distinto.
    
- Funciones:
    
    - `Mensajes()` → Muestra textos según la opción.
        
    - `LeerIP()` → Captura la IP introducida por el usuario.
        
    - `LeerPuerto()` → Captura el puerto o rango de puertos.

- **Opciones del menú**:
    
    1. Escaneo básico.
        
    2. Descubrimiento de hosts con ARP.
        
    3. Descubrimiento de hosts con Ping sweep (sin ARP).
        
    4. Escaneo de puertos con SYN Scan (`-sS`).
        
    5. Escaneo completo (`-A`, incluye OS detection, traceroute, servicios, scripts).
        
    6. Salir.

---

## ✅ Ventajas del Script

- **Automatiza tareas comunes** de Nmap.

- Reduce errores al recordar la sintaxis.

- Guía al usuario de forma didáctica.

- Se puede extender con más opciones (ej. guardar resultados en un fichero).

---


