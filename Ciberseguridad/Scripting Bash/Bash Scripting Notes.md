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
var="hola"   # ✅ asignación correcta
var2=$var     # ✅ asignando el valor de otra variable
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