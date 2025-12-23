#labs #linux #ejercicio
# 🛠️ Bandit OverTheWire – Resolución detallada (Niveles 0 → 34)

> **Actualizado:** 2025-06-02

Este documento es una guía **paso a paso** para las personas que se inician en ciberseguridad.  
Cada nivel introduce _conceptos fundamentales de Linux_, desde permisos de archivos y redirecciones hasta sockets, `cron` y Git.

Para **cada nivel** encontrarás:

- ✅ **Objetivo** – qué debes obtener o demostrar.  
- 🧠 **Concepto clave** – por qué el reto es importante y qué se aprende.  
- 💻 **Comando(s)** – la línea mínima (o script) que resuelve el nivel.  
- 🔍 **Detalles técnicos** – flags, sintaxis, GOTCHAs y contexto teórico.  
- 🗃️ **Ejemplo de salida** (‐si aporta claridad–).

---

## 🌐 Conexión SSH básica

```bash
# Sustituye X por el nivel al que quieras entrar
ssh banditX@bandit.labs.overthewire.org -p 2220
```

> 💡 **Por qué 2220?** Los juegos OTW escuchan en un puerto alto para evitar bloqueos de firewalls comunes.

La **contraseña de cada nivel** se guarda invariablemente en:

```
/etc/bandit_pass/banditX
```

Transfiérela a tu gestor de contraseñas o un archivo cifrado a medida que avances.

---

## 🔑 Niveles 0 → 10 – Manipulación de archivos

### Nivel 0 → 1
| | |
|---|---|
| ✅ **Objetivo** | Leer el archivo `readme` en `$HOME`. |
| 🧠 **Concepto** | Uso de **SSH** y visualización de un archivo con `cat`. |
| 💻 **Comando** | `cat readme` |
| 🔍 **Detalles** | Al conectarte via SSH ya estás en tu directorio personal (`~`). `cat` envía el contenido a **stdout** (descriptor 1). |

---

### Nivel 1 → 2  
|     |                                                                                                        |
| --- | ------------------------------------------------------------------------------------------------------ |
| ✅   | Leer un archivo llamado **`-`**.                                                                       |
| 🧠  | Un guion simple suele representar *stdin* para muchos comandos.                                        |
| 💻  | ```bash\ncat ./-\n```                                                                                  |
| 🔍  | `./` fuerza a Bash a interpretar el guion como **ruta relativa** en disco, no como argumento especial. |

---

### Nivel 2 → 3  
| | |
|---|---|
| ✅ | Leer un archivo con **espacios** en su nombre. |
| 🧠 | Cómo *escapar* nombres inusuales. |
| 💻 | `cat "spaces in this filename"` |
| 🔍 | Los espacios separan argumentos; entrecomillarlos (o escaparlos con `\ `) hace que el shell los trate como un único token. |

---

### Nivel 3 → 4  
|     |                                                          |
| --- | -------------------------------------------------------- |
| ✅   | Encontrar un **archivo oculto** en `inhere/`.            |
| 🧠  | Archivos que comienzan con `.` no se listan por defecto. |
| 💻  | ```bash\ncd inhere && ls -a && cat .hidden\n```          |
| 🔍  | `ls -a` muestra **all** (‐a) entradas, incl. `.` y `..`  |

---

### Nivel 4 → 5  

1. 📂 Entra en el directorio `inhere`:

    `cd inhere`

1. 📜 Verás varios archivos con nombres un poco raros. El problema es que no todos son "legibles" para humanos.

2. 🕵️ Usa el comando `file` para analizar de qué tipo es cada archivo:
    
    `file ./*`
    
    Te dirá qué archivos son **data**, cuáles son **ASCII text** (esos son los legibles), etc.
    
3. ✅ El archivo que salga como **ASCII text** (o similar) es el que contiene la contraseña.  
    Solo tienes que abrirlo con:
    
    `cat nombre_del_archivo`

---

### Nivel 5 → 6  

#### 1) Sobre `-size 1033c`

Esto ya lo tienes claro: `c` = **bytes exactos**.  
Ej.: `-size 1033c` ⇒ tamaño **exacto** 1033 bytes.

####  2) ¿Qué hace exactamente `find ! -perm /111`?

- `-perm /111` significa: “archivos donde **al menos uno** de los bits de ejecución está activado” (user `u=x`=1, group `g=x`=1, others `o=x`=1).  
    El `/` en `-perm /MODE` significa “**cualquiera de** esos bits”.

- `! -perm /111` niega lo anterior ⇒ “archivos donde **ninguno** de los bits de ejecución (u,g,o) está activado”.

En otras palabras: **no ejecutables para nadie**.

Comprobación rápida:

```bash
# Muestra todo lo que tenga algún bit x
find . -perm /111

# Muestra todo lo que NO tenga ningún bit x (lo que nos interesa)
find . ! -perm /111
```

####  3) “Human-readable” con `file` (cómo encadenarlo bien)

Tu objetivo: 
pasar candidatos a `file` y quedarte con los que contengan “text”.

Forma robusta manteniendo el nombre del archivo:

```bash
find . -type f -size 1033c ! -perm /111 -exec file -- {} \; | grep -i "text"
```

Detalles:

- `file -- {}`: el `--` evita que nombres que empiezan por `-` se interpreten como opciones.

- Sin `-b`, `file` imprime `RUTA: TIPO`. Así puedes **grepear** por “text” y **ver la ruta**.


Si quieres **quedarte solo con la ruta**, recorta la parte antes de `:`:

```bash
find . -type f -size 1033c ! -perm /111 -exec file -- {} \; \
| grep -i "text" \
| cut -d: -f1
```

####  4) ¿Qué hacen `-print0` y `xargs -0`?

Es la combinación “a prueba de balas” para nombres raros:

- `-print0` → imprime cada ruta terminada en **byte nulo** (`\0`) en vez de salto de línea.  
    Así, si el nombre tiene espacios, saltos de línea o comillas, **no se rompe**.
    
- `xargs -0` → lee entradas separadas por `\0` y las pasa como argumentos **seguros** al comando siguiente.
    

Ejemplo:

```bash
find . -type f -print0 | xargs -0 ls -l
```

Sin esto, un archivo llamado `spaces file1` se partiría en dos argumentos. Con `-print0/-0` **no**.

####  5) Ensamblado “triple filtro” en un solo recorrido

##### Variante A (con `-exec file … \;` — simple y clara)

```bash
find . -type f -size 1033c ! -perm /111 -exec file -- {} \; \
| grep -i "text" \
| cut -d: -f1 \
| xargs -r cat
```

- `grep -i "text"` filtra “ASCII text”, “UTF-8 text”, etc.
    
- `cut -d: -f1` deja solo la ruta.
    
- `xargs -r cat` imprime el contenido (la contraseña). `-r` evita ejecutar `cat` si no hay resultados.
    

> Si quieres **ver primero qué archivo es** antes de abrirlo:
> 
> ```bash
> find . -type f -size 1033c ! -perm /111 -exec file -- {} \; | grep -i "text"
> ```
> 
> Cuando confirmes que solo hay uno, haces `cat RUTA`.

##### Variante B (blindaje total con `-print0` + `xargs -0`)

```bash
find . -type f -size 1033c ! -perm /111 -print0 \
| xargs -0 file -- \
| grep -i "text" \
| cut -d: -f1 \
| xargs -r cat
```

- Aquí `file --` recibe **todas** las rutas desde `xargs`, sin sufrir por espacios o guiones iniciales.
    

#####  Variante C (sin `grep`, usando `file -b` + shell)

Si prefieres lógica “dentro” del `find`:

```bash
find . -type f -size 1033c ! -perm /111 -exec sh -c '
  for f; do
    if file -b -- "$f" | grep -qi "text"; then
      echo "$f"
    fi
  done
' sh {} + | xargs -r cat
```

- `-exec … {} +` agrupa varios archivos por ejecución (más eficiente).
    
- `file -b` imprime solo el tipo; `grep -qi "text"` decide.
    

#### Errores típicos que evitas con esto

- **Nombres con guion**: usa `--` o `./` antes del nombre (`file -- -file1` o `file ./-file1`).
    
- **Espacios/nuevas líneas**: `-print0 | xargs -0`.
    
- **Tamaño exacto**: usa `1033c`, no KB/MB.
    
- **Legible**: filtra por “text” con `file`, no confundir con `-readable`.

#### ¿Quieres el “one-liner” final?

Si ya te sientes cómodo, ejecuta esta (te saca **directo** la password):

```bash
find . -type f -size 1033c ! -perm /111 -exec file -- {} \; \
| grep -i "text" \
| cut -d: -f1 \
| xargs -r cat
```

Si prefieres comprobar antes, quita el último `| xargs -r cat`, mira la ruta, y luego:

```bash
cat RUTA_ENCONTRADA
```

¿Te doy ahora una versión con `-print0` para que quede 100% a prueba de nombres raros, o así ya lo rematas?

---

### Nivel 6 → 7  

#### 🎯 Objetivo

Encontrar la contraseña que:

- Está en un archivo **propiedad del usuario `bandit7`**
    
- Pertenece al grupo **`bandit6`**
    
- Tiene un tamaño exacto de **33 bytes**

#### 🔎 Proceso de resolución

##### 1. Identificar lo que necesitamos

El enunciado nos da **3 filtros** para usar con `find`:

- `-user bandit7` → buscar archivos propiedad de este usuario.
    
- `-group bandit6` → buscar archivos propiedad de este grupo.
    
- `-size 33c` → buscar archivos de exactamente 33 **bytes** (`c = bytes`).

##### 2. Primeros intentos (fallidos)

Probé con:

```bash
find . -type f -size 33c | grep -i bandit7
```

❌ Esto no funciona porque `grep` busca texto dentro de la **salida del comando**, no filtra por propietario.  
Además, aparecen muchos errores de _Permission denied_.

##### 3. Ajuste correcto del comando

La forma correcta es usar directamente los filtros de `find`:

```bash
find . -type f -size 33c -user bandit7 -group bandit6
```

✅ Ahora se buscan **solo** archivos que cumplen los tres requisitos.  
Aún así, siguen apareciendo muchos _Permission denied_.

##### 4. Manejo de errores de permisos

Redirigí los errores al vacío con `2>/dev/null`:

```bash
find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null
```

- `/` → buscar desde la raíz del sistema.
- `2>/dev/null` → oculta los mensajes de error.
##### 5. Resultado encontrado

El comando devolvió:

```bash
/var/lib/dpkg/info/bandit7.password
```

##### 6. Lectura de la contraseña

Finalmente:

```bash
cat /var/lib/dpkg/info/bandit7.password
```

Contraseña obtenida:

```
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```

---

### Nivel 7 → 8  

#### 🎯 Objetivo

Encontrar la contraseña que está almacenada en el archivo `data.txt`, **junto a la palabra `millionth`**.

#### 🔎 Proceso de resolución

##### 1. Identificar la pista

El enunciado nos dice que el archivo `data.txt` contiene muchas líneas, pero solo **una** tiene la palabra clave `millionth`.  
La contraseña está justo al lado de esa palabra.

##### 2. Primer intento

Abrir el archivo con `cat` muestra demasiado contenido y es difícil encontrar la palabra manualmente.  
Ejemplo:

```bash
cat data.txt
```

❌ Demasiado texto, poco práctico.

##### 3. Uso de `grep` para buscar la palabra clave

La forma directa es filtrar la línea que contiene “millionth”:

```bash
cat data.txt | grep -i "millionth"
```

ó, más eficiente:

```bash
grep -i "millionth" data.txt
```

##### 4. Resultado obtenido

El comando devuelve:

```bash
millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

Por tanto, la **contraseña** es:

```
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

#### 📝 Forma alternativa

##### Usando `awk` para mostrar solo la segunda columna

El archivo tiene un formato de “palabra + contraseña”.  
Podemos extraer directamente la contraseña con:

```bash
awk '/millionth/ {print $2}' data.txt
```

Esto busca la línea con “millionth” y muestra únicamente la segunda columna → la contraseña.

##### Usando `grep -w` para buscar palabra exacta

```bash
grep -w "millionth" data.txt
```

La opción `-w` asegura que busca la palabra completa y no parte de otra.

##### Usando `strings` (si sospecháramos datos binarios)

En este nivel no hacía falta, pero otra idea sería:

```bash
strings data.txt | grep "millionth"
```

#### 📌 Resumen de comandos clave

|Comando|Función|
|---|---|
|`grep -i "millionth" data.txt`|Busca línea con la palabra “millionth” (ignora mayúsculas)|
|`awk '/millionth/ {print $2}' data.txt`|Devuelve solo la contraseña|
|`grep -w "millionth" data.txt`|Busca la palabra exacta|
|`strings file`|Extrae texto legible de archivos binarios|

---

### Nivel 8 → 9  

#### `uniq` + `sort` + `grep`

##### 🔹 `uniq`

Filtra líneas repetidas consecutivas.

> ⚠️ Importante: solo detecta repeticiones **si están juntas** → normalmente se combina con `sort`.

```bash
uniq archivo.txt        # elimina duplicados consecutivos
uniq -c archivo.txt     # muestra cuántas veces aparece cada línea
uniq -d archivo.txt     # muestra solo líneas duplicadas
uniq -u archivo.txt     # muestra solo líneas únicas (sin duplicados)
```
##### 🔹 `sort`

Ordena líneas de texto.

```bash
sort archivo.txt        # orden alfabético
sort -r archivo.txt     # orden inverso
sort -n archivo.txt     # orden numérico
sort -k 2 archivo.txt   # ordenar por la segunda columna
sort -u archivo.txt     # ordenar y eliminar duplicados
```

##### 🔹 `sort + uniq` (combinación típica)

1. **Eliminar duplicados globales** (no solo consecutivos):

  ```bash
  sort archivo.txt | uniq
   ```

1. **Contar cuántas veces aparece cada línea**:

```bash
  sort archivo.txt | uniq -c
```

1. **Encontrar la línea única** (aparece solo una vez):

 ```bash
 sort archivo.txt | uniq -u
 ```

2. **Encontrar las líneas repetidas**:

 ```bash
  sort archivo.txt | uniq -d
   ```

##### 🔹 `grep` (filtrado rápido)

```bash
grep "palabra" archivo.txt       # buscar coincidencias
grep -i "palabra" archivo.txt    # ignorar mayúsculas/minúsculas
grep -w "palabra" archivo.txt    # palabra exacta
```

---

### Nivel 9 → 10  

| ✅ | Extraer cadena tras varios `=` en `data.txt`. |
| 💻 | ```bash\nstrings data.txt | grep -oE "=+([A-Za-z0-9]{32})" | cut -d= -f2\n``` |
| 🧠 | `strings` revela texto ASCII escondido en binarios. |

---

### Nivel 10 → 11  
|                          |                                                                                                             |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| ✅ **Objetivo**           | El archivo `data.txt` está **codificado en Base64**. Decodifica y obtén la contraseña.                      |
| 🧠 **Concepto clave**    | *Base64* no es cifrado; simplemente representa binarios en ASCII. Muy usado en correos y APIs.              |
| 💻 **Comando**           | ```bash\nbase64 -d data.txt\n```                                                                            |
| 🔍 **Detalles técnicos** | `-d` (decode) lee desde `stdin` si no se especifica archivo. Base64 produce siempre longitud múltiplo de 4. |
| 🗃️ Ejemplo de salida    | `The password is <pass11>`                                                                                  |

---

### Nivel 11 → 12  
| | |
|---|---|
| ✅ | El contenido de `data.txt` está ofuscado con **ROT13**. |
| 🧠 | ROT13 es una sustitución simétrica (A↔N, B↔O, …). Aplicar dos veces devuelve texto original. |
| 💻 | ```bash\ntr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt\n``` |
| 🔍 | `tr` (translate) opera byte‑a‑byte. Dos rangos iguales en longitud producen sustitución. |
| 🗃️ Ejemplo | `The password is <pass12>` |

---

### Nivel 12 → 13 — “Muñeca rusa” de compresión  
|                                 |                                                                                                                                                                                                                                                                         |                                                                                                                  |                                                                       |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| ✅                               | Se parte de un hexdump reconstruido. Desencapsula **múltiples capas** (gzip, bzip2, tar, 7‑zip…) hasta hallar ASCII.                                                                                                                                                    |                                                                                                                  |                                                                       |
| 🧠                              | Practicar identificación de **formatos binarios** y automatizar descompresión.                                                                                                                                                                                          |                                                                                                                  |                                                                       |
| 💻 **Script Bash simplificado** | ```bash\nf=data.bin\nwhile true; do\n  t=$(file -b \"$f\")\n  case $t in\n    *gzip*)   mv \"$f\" f.gz  && gunzip  f.gz  && f=${f%.gz} ;;\n    *bzip2*)  mv \"$f\" f.bz2 && bunzip2 f.bz2 && f=${f%.bz2} ;;\n    *7-zip*)  7z x -y \"$f\" >/dev/null && f=$(7z l \"$f\" | awk '/Name/{{getline;getline;print $NF}}') ;;\n    *tar*)    mv \"$f\" f.tar && tar xf f.tar && f=$(tar tf f.tar | head -n1) ;;\n    *ASCII*)  cat \"$f\" && break ;;\n  esac\ndone\n``` |
| 🔍                              | `file -b` devuelve solo el dictamen. Cada bloque mueve/extrae y actualiza la variable `f`.                                                                                                                                                                              |                                                                                                                  |                                                                       |
| 🗃️ Salida final                | `The password is <pass13>`                                                                                                                                                                                                                                              |                                                                                                                  |                                                                       |

## Apuntes sobre el script **Bandit12**

> Script Bash que extrae recursivamente un fichero comprimido en formato **7‑Zip** hasta encontrar un archivo de texto legible, registrando todos los niveles de compresión por los que pasa.

---

### 1. Objetivo

Descomprimir **Bandit12** (fichero 7‑Zip) capa a capa, añadiendo cada nombre de archivo a un array y deteniendo el proceso cuando el fichero que toca extraer ya no sea otro contenedor sino un _texto plano_. Finalmente se muestra por pantalla el contenido del archivo de texto hallado.

---

### 2. Dependencias

- **bash** (≥4: usa arrays y `[[ … ]]`)
    
- **p7zip** ‑ proporciona los comandos `7z x` (extraer) y `7z l` (listar).
    
- Utilidad estándar **file** para identificar el tipo MIME del archivo.
    

---

### 3. Código fuente original

```bash
#!/usr/bin/bash

File="Bandit12"
Verificator=""
Archivos=()
Contador=0

while [[  $Verificator = "" ]]
do
        7z x $File 1>/dev/null
        Archivos+=($File)
        File=$(7z l $File | grep "Name" -A 2 | awk '{print $NF}' | tail -n 1)
        Verificator=$(file $File | grep "text")
done

for i in "${Archivos[@]}"; do
    echo "Se ha descomprimido $i"
done

cat $File
```

---

### 4. Explicación paso a paso

|Línea|Descripción|
|---|---|
|**1**|_Shebang_ que fuerza el uso de la versión de **bash** instalada en `/usr/bin/bash`.|
|**3‑6**|Definición de variables: • `File`: nombre del contenedor inicial. • `Verificator`: marcador vacío para controlar el bucle. • `Archivos`: array donde se irán almacenando los contenedores extraídos. • `Contador`: no se utiliza realmente (quedó sin usar).|
|**8‑15**|**Bucle `while`**: continúa mientras `Verificator` permanezca vacío (es decir, mientras **no** se haya detectado un archivo de texto). 1. `7z x $File`: extrae el contenido del contenedor actual (**stdout** redirigido para suprimir mensajes). 2. `Archivos+=($File)`: añade el nombre del contenedor al array. 3. `7z l $File …`: lista el contenido del contenedor recién extraído, filtra y obtiene el nombre del primer archivo encontrado; la sustitución de comandos actualiza la variable `File` con ese nombre. 4. `file $File …`: comprueba si el nuevo `$File` es texto; si lo es, la línea `grep "text"` devuelve texto y se rompe el bucle.|
|**17‑20**|Recorre el array `Archivos` mostrando los contenedores descomprimidos en orden.|
|**22**|`cat $File`: muestra en pantalla el contenido del archivo de texto final.|

---

### 5. Aspectos a tener en cuenta

1. **Comillas y espacios**: Si un nombre de archivo contiene espacios, convendría entrecomillar las expansiones (`"$File"`).
    
2. **Condición del bucle**: `[[ -z $Verificator ]]` es más idiomático que `[[ $Verificator = "" ]]`.
    
3. **Variable `Contador`**: declarada pero sin uso; puede eliminarse o aprovecharse para numerar niveles.
    
4. **Limpieza**: los contenedores extraídos permanecen en disco; se podría añadir una rutina que los elimine (`rm -- "$i"`) tras haberlos procesado.
    
5. **Control de errores**: incorporar `set -euo pipefail` al inicio ayuda a abortar ante fallos y a detectar variables sin definir.
    
6. **Portabilidad**: exige Bash ≥ 4 (arrays) y p7zip; en sistemas minimalistas puede no estar disponible.
    

---

### 6. Posibles mejoras / refactorización

```bash
#!/usr/bin/env bash
set -euo pipefail

initial_file="Bandit12"
current_file="$initial_file"
decoded=()

while [[ $(file -b --mime-type "$current_file") != text/* ]]; do
    7z x "$current_file" >/dev/null
    decoded+=("$current_file")
    current_file=$(7z l "$current_file" | awk '/^----------/{getline; print $NF; exit}')
done

printf 'Se han descomprimido: %s\n' "${decoded[@]}"
cat "$current_file"
```

- Comparación directa del tipo MIME (`file -b --mime-type`).
    
- Extracción de un solo nombre con **awk** sin tuberías adicionales.
    
- Uso de variables con nombres auto‑explicativos (`initial_file`, `current_file`).
    
- Eliminación de la variable inútil `Contador`.
    
- `set -euo pipefail` para robustez.
    

---

### 7. Ejecución

```bash
chmod +x Bandit12_extractor.sh
./Bandit12_extractor.sh
```

---

### 8. Referencias

- [Página de manual de 7‑Zip](https://man7.org/linux/man-pages/man1/7z.1.html)
    
- [Guía de buenas prácticas en Bash](https://github.com/koalaman/shellcheck/wiki/Directive)#


---

## Nivel 13 → 14  
| | |
|---|---|
| ✅ | Se suministra **clave SSH privada**. Autentícate como *bandit14*. |
| 💻 | ```bash\nchmod 600 sshkey.private\nssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220\ncat /etc/bandit_pass/bandit14\n``` |
| 🧠 | Permisos 600 evitan que OpenSSH rechace la key por ser muy accesible. |
| 🔍 | Usa `-i` para especificar la clave. Tras loguearte, la contraseña del nivel siguiente está en el path habitual. |

---

## Nivel 14 → 15  
| | |
|---|---|
| ✅ | Debes **enviar la contraseña** obtenida al **puerto 30000/TCP** en la misma máquina y leer la respuesta. |
| 💻 | ```bash\necho <pass14> | nc localhost 30000\n``` |
| 🧠 | `nc` (netcat) abre un socket TCP y envía stdin al servidor. |
| 🔍 | El servidor devuelve el pass 15 en texto plano y luego cierra conexión. |

---
## Nivel 15 → 16  
| | |
|---|---|
| ✅ **Objetivo** | Igual que el nivel anterior, pero el servicio está **cifrado en TLS** (puerto 30001). |
| 🧠 **Concepto clave** | Uso de `openssl s_client` como “netcat+TLS” para hablar con servicios SSL/TLS. |
| 💻 **Comando** | ```bash\necho <pass15> | openssl s_client -quiet -connect localhost:30001\n``` |
| 🔍 **Detalles técnicos** | `-quiet` suprime el handshake verboso. `openssl s_client` espera en **stdin** la cadena que debe enviar. |
| 🗃️ Salida | `Correct! The next password is <pass16>` |

---

## Nivel 16 → 17  
| | |
|---|---|
| ✅ | Uno de los puertos **31000 → 32000** acepta la contraseña (algunos hablan TLS, otros no). |
| 🧠 | Aprender a **detectar puertos abiertos** y probar protocolo plano vs TLS. |
| 💻 **Escaneo sin Nmap** |```bash\nfor p in {{31000..32000}}; do\n  timeout 1 bash -c \"echo >/dev/tcp/127.0.0.1/$p\" 2>/dev/null && echo \"OPEN $p\";\ndone\n``` |
| 💻 **Prueba cada puerto** |```bash\nfor p in $(grep OPEN scan.txt | awk '{{print $2}}'); do\n  echo <pass16> | nc -w1 localhost $p   || true\n  echo <pass16> | openssl s_client -quiet -connect localhost:$p 2>/dev/null || true\ndone | grep -i password\n``` |
| 🔍 | `timeout` mata cualquier socket que no responda; redirige errores. |
| 🗃️ | El puerto correcto devuelve usuario+password de *bandit17*. |

---

## Nivel 17 → 18  
| | |
|---|---|
| ✅ | Buscar la línea distinta entre `passwords.old` y `passwords.new`. |
| 🧠 | Uso de `diff` para análisis de files. |
| 💻 | ```bash\ndiff passwords.old passwords.new | awk '/^>/{print $2}'\n``` |
| 🔍 | En la salida de `diff`, las líneas que empiezan con `>` pertenecen al segundo archivo. |

---

## Nivel 18 → 19  
| | |
|---|---|
| ✅ | Entrar sin que `.bashrc` cierre la sesión inmediatamente. |
| 🧠 | SSH permite **ejecutar un único comando remoto** sin abrir shell interactivo. |
| 💻 | ```bash\nssh bandit18@bandit.labs.overthewire.org -p 2220 \"cat readme\"\n``` |
| 🔍 | La salida impresa es la contraseña de *bandit19*. |

---

## Nivel 19 → 20  
| | |
|---|---|
| ✅ | Usar binario **SUID** `bandit20-do` para leer la contraseña. |
| 🧠 | **SUID** ejecuta el binario con UID de su dueño (bandit20), permitiendo escalar privilegios controlados. |
| 💻 | ```bash\n./bandit20-do bash -c 'cat /etc/bandit_pass/bandit20'\n``` |
| 🔍 | El comando pasado tras `bash -c` se ejecuta con privilegios elevados. |

---

## Nivel 20 → 21  
| | |
|---|---|
| ✅ | Otro binario SUID (`suconnect`) se conecta al puerto indicado y envía la contraseña; devuelve la nueva. |
| 💻 **Procedimiento** |```bash\n# 1. Terminal A (listen):\nnc -l 4444 &\n# 2. Terminal B:\n./suconnect 4444\n# 3. Terminal A: pega <pass20>\n``` |
| 🔍 | El proceso en Terminal A recibirá la contraseña del nivel 21. |

---

## Nivel 21 → 22  
|     |                                                                                                         |                                                                           |
| --- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| ✅   | Analizar **cronjob** en `/etc/cron.d/` que ejecuta un script como *bandit22*.                           |                                                                           |
| 💻  | ```bash\ncat /etc/cron.d/*                                                                              | grep bandit22 -n\ncat /usr/bin/cronjob_bandit22  # (ruta del script)\n``` |
| 🧠  | Entender rutas y variables usadas, luego leer el archivo donde el script escribe la contraseña, p. ej.: |                                                                           |
| 💻  | ```bash\ncat /tmp/secret_bandit22\n```                                                                  |                                                                           |
| 🔍  | La ubicación exacta puede cambiar; sigue el script.                                                     |                                                                           |

---
## Nivel 22 → 23  
|                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅ **Objetivo**         | Encontrar la contraseña escrita por un **cron** que corre como *bandit23*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 🧠 **Concepto clave**  | Los cronjobs están definidos en `/etc/cron.d/`. Entender variables de entorno y rutas de salida.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 💻                     | ```bash\ncat /etc/cron.d/cronjob_bandit23\ncat /usr/bin/cronjob_bandit23.sh\n```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 🔍 **Detalles**        | El script copia la contraseña de `/etc/bandit_pass/bandit23` a un archivo en `/tmp/` cuyo nombre incluye una suma hash.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 💻 **Lectura directa** | ```bash\ncat $(grep -oE '/tmp/[^ ]+' /usr/bin/cronjob_bandit23.sh)\n```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Solución               | $ cd /etc/cron.d/<br>$ ls -l <br>$ cat cronjob_bandit23<br>$ cat /usr/bin/cronjob_bandit23.sh<br>-- #!/bin/bash<br>-- myname=$(whoami)<br>-- mytarget=$(echo I am user $myname \| md5sum \| cut -d ' ' -f 1)<br>-- echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"<br>-- cat /etc/bandit_pass/$myname > /tmp/$mytarget<br>$ /usr/bin/cronjob_bandit23.sh<br>## whoami = bandit22<br>$ myname=bandit23<br>$ mytarget=$(echo I am user $myname \| md5sum \| cut -d ' ' -f 1)<br>$ echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"<br>$ cat /etc/bandit_pass/$myname > /tmp/$mytarget<br>$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349<br>jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n<br> |
	- Cuando tenemos una variable así  con un $dolar$ y entre paréntesis:
		myname=$(whoami)
		mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
	
	 - Significa que todo lo que esté ahí dentro van a ser comandos y la salida de 
	 estos comandos se van a almacenar en la variable.
	 
	 - En este caso podemos usar ingeniería inversa para ver el valor que puede 
	 tomar la variable mytarget.
	 
	 - Entonces ejecutaríamos el comando:
	 echo I am user $myname | md5sum | cut -d ' ' -f 1
	 
	 - De esta forma obtenemos el valor de la variable mytarget que coincide con
	 del nombre del archivo almacenado en /tmp/$mytarget
	 
	 - Finalmente hacemos un cat a  esa ruta absoluta y obtenemos la password.
---

## Nivel 23 → 24  
|          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅        | Subir un script propio a la carpeta que el cron de *bandit24* ejecuta.                                                                                                                                                                                                                                                                                                                                                                                                              |
| 💻       | ```bash\necho -e '#!/bin/bash\\ncat /etc/bandit_pass/bandit24 > /tmp/pass24' > /var/spool/bandit24/evil.sh\nchmod +x /var/spool/bandit24/evil.sh\nsleep 90 && cat /tmp/pass24\n```                                                                                                                                                                                                                                                                                                  |
| 🧠       | El cron ejecuta scripts en esa ruta cada minuto.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Solución | $ cd /etc/cron.d/<br>$ ls -l <br>$ cat cronjob_bandit24<br>$ cat /usr/bin/cronjob_bandit24.sh<br>$ mkdir /tmp/fcchx<br>$ cd /tmp/fcchx<br>$ touch getx.sh<br>$ chmod 777 getx.sh<br>$ ls -la getx.sh<br>$ vim getx.sh<br>-- #!/bin/bash<br>-- cat /etc/bandit_pass/bandit24 > /tmp/fcchx/password<br>$ touch password<br>$ chmod 666 password<br>$ ls -la password<br>$ cp getx.sh /var/spool/bandit24/<br>## Wait 5 sec.<br>$ cat password<br>UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ<br> |

---

## Nivel 24 → 25  
|               |                                                                                                                                                                                                                                                                                                                              |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅             | Brute‑force un **PIN de 4 dígitos** asociado al servicio en `localhost:30002`.                                                                                                                                                                                                                                               |
| 💻 **Script** | ```bash\nfor pin in $(seq -w 0000 9999); do\n  echo \"<pass24> $pin\"                                                                                                                                                                                                                                                        |
| solución      | $ cd /tmp<br>$ mkdir fcch-pass25; cd fcch-pass25; touch genpass.sh<br>$ vim genpass.sh<br>-- #!/bin/bash<br>-- pass=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ<br>-- for i in {0000..9999} <br>-- do<br>--    echo $pass $i >> pass25.txt<br>-- done<br>$ cat pass25,txt \| nc localhost 30001<br>uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG<br> |

---

## Nivel 25 → 26  
| | |
|---|---|
| ✅ | Bypass de shell forzado (`bandit26`). |
| 💻 | ```bash\nssh bandit26@localhost -p 2220 cat /etc/bandit_pass/bandit26\n``` |
| 🧠 | SSH ejecuta comando remoto sin abrir el shell restringido. |

---

## Nivel 26 → 27  
| | |
|---|---|
| ✅ | Escapar de **`more`**. |
| 💻 | ```bash\n!/bin/bash\ncat /etc/bandit_pass/bandit27\n``` |

---

## Nivel 27 → 28  
| | |
|---|---|
| ✅ | Clonar el repo Git y leer el `README`. |
| 💻 | ```bash\ngit clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo repo27 && cat repo27/README\n``` |

---

## Nivel 28 → 29  
| | |
|---|---|
| ✅ | Revisar **tags**. |
| 💻 | ```bash\ncd repo27\ngit tag -l\ngit show secret\n``` |

---

## Nivel 29 → 30  
| | |
|---|---|
| ✅ | Buscar commit en rama remota. |
| 💻 | ```bash\ngit branch -a\ngit checkout dev\ngit show HEAD:password.txt\n``` |

---

## Nivel 30 → 31  
| | |
|---|---|
| ✅ | Explorar **stash**. |
| 💻 | ```bash\ngit stash list\ngit stash show -p | grep -A1 password\n``` |

---

## Nivel 31 → 32  
| | |
|---|---|
| ✅ | Conectarse con la **clave SSH** extraída. |
| 💻 | ```bash\nchmod 600 sshkey.private\nssh -i sshkey.private bandit31@bandit.labs.overthewire.org -p 2220\n``` |
| 🔍 | Una vez dentro, interactuar con servicio en `127.0.0.1:10007`: |
| 💻 | ```bash\necho $(cat /etc/bandit_pass/bandit31) | nc 127.0.0.1 10007\n``` |

---

## Nivel 32 → 33  
|     |                                                       |
| --- | ----------------------------------------------------- |
| ✅   | Lanzar un intérprete `sh` para sortear restricciones. |
| 💻  | ```bash\nsh\ncat /etc/bandit_pass/bandit33\n```       |

---

## Nivel 33 → 34  
| | |
|---|---|
| ✅ | No publicado. ¡Bandit completado! |

---
