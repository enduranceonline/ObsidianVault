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
| | |
|---|---|
| ✅ | Leer un archivo llamado **`-`**. |
| 🧠 | Un guion simple suele representar *stdin* para muchos comandos. |
| 💻 | ```bash\ncat ./-\n``` |
| 🔍 | `./` fuerza a Bash a interpretar el guion como **ruta relativa** en disco, no como argumento especial. |

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
| | |
|---|---|
| ✅ | Hallar el **único** archivo ASCII legible en `inhere/`. |
| 🧠 | Comando `file` identifica tipo de datos leyendo *magic numbers*. |
| 💻 | ```bash\nfind inhere -type f -exec file {} \; | grep "ASCII text" | cut -d: -f1 | xargs cat\n``` |
| 🔍 | `find -type f` lista archivos. `file` añade tipo. `grep` filtra. `cut` extrae la ruta. `xargs` re‑inyecta esa ruta en `cat`. |

---

### Nivel 5 → 6  
| | |
|---|---|
| ✅ | Localizar archivo legible de **1033 bytes**, no ejecutable. |
| 🧠 | Filtros de tamaño con `find`. Un byte = `c` en la sintaxis GNU. |
| 💻 | ```bash\nfind inhere -type f -size 1033c -readable ! -executable -exec cat {} \;\n``` |
| 🔍 | `! -executable` niega la prueba. |

---

### Nivel 6 → 7  
| | |
|---|---|
| ✅ | Buscar un archivo de **33 bytes** cuyo **owner** sea *bandit7* y **group** *bandit6*. |
| 🧠 | Recurse root FS y silencia errores. |
| 💻 | ```bash\nfind / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null -exec cat {} \;\n``` |
| 🔍 | `2>/dev/null` redirige **stderr** (descriptor 2) a *null* para no contaminar la salida. |

---

### Nivel 7 → 8  
| | |
|---|---|
| ✅ | Obtener la palabra **tras** `millionth` en `data.txt`. |
| 💻 | ```bash\ngrep -Eo "millionth .*" data.txt | awk '{print $2}'\n``` |
| 🔍 | `-Eo` = **E**xtended regex + **o**nly‑matching. |

---

### Nivel 8 → 9  
| | |
|---|---|
| ✅ | Encontrar la línea que aparece **una sola vez**. |
| 💻 | ```bash\nsort data.txt | uniq -u\n``` |
| 🔍 | `uniq -u` emite las líneas cuyo conteo es 1 en la entrada ya ordenada. |

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
| | |
|---|---|
| ✅ | Lanzar un intérprete `sh` para sortear restricciones. |
| 💻 | ```bash\nsh\ncat /etc/bandit_pass/bandit33\n``` |

---

## Nivel 33 → 34  
| | |
|---|---|
| ✅ | No publicado. ¡Bandit completado! |

---
