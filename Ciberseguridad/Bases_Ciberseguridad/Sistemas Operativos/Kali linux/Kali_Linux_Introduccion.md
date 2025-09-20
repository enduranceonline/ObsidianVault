#bases #linux #apuntes
# 🐱‍💻 Kali Linux - Introducción

Esta nota reúne atajos, comandos útiles y herramientas esenciales para comenzar con Kali Linux, organizado de forma clara y práctica para entornos de pentesting y administración avanzada.

---

# Linux Distributions 🐧

## Debian 🐟

### Características
- Distro muy usada y respetada por su **estabilidad y fiabilidad**.  
- Usos: **escritorio, servidores, sistemas embebidos**.  
- Sistema de gestión de paquetes: **APT (Advanced Package Tool)**.  
  - Permite actualizaciones y parches de seguridad de forma automática o manual.  

---

### Ventajas
- **Soporte a largo plazo (LTS):** actualizaciones hasta 5 años.  
- **Compromiso con seguridad y privacidad.**  
- **Gran comunidad de desarrollo** → parches rápidos ante vulnerabilidades.  
- **Alta flexibilidad y personalización.**  

---

### Consideraciones
- Curva de aprendizaje más pronunciada que Ubuntu o Fedora.  
- La configuración puede resultar más compleja, pero ofrece **gran control al usuario avanzado**.  
- Una vez dominado, permite gestionar tareas de forma más eficiente.  

---

### Conclusión
Debian es una distribución:
- Estable y confiable.  
- Con fuerte **historial de seguridad**.  
- Versátil: apta para **ciberseguridad, servidores y entornos críticos 24/7**.  
- Opción excelente para quienes buscan un sistema sólido y personalizable.

### 🧾 Información del sistema
```bash
cat /etc/os-release    # Ver info de la distribución
```

---

## 📚 3. Ayuda y documentación

### `help`
Muestra ayuda sobre comandos internos de Bash.

### `man`
Accede a los manuales de comandos.
```bash
man ls      # Ver manual de 'ls'
```

### `info`
Manual más detallado, especialmente para comandos GNU.

### `whatis`
Resumen corto de un comando.
```bash
whatis grep
```

### `apropos`
Busca comandos relacionados con una palabra clave.
```bash
apropos user
```

---

## ⚙️ 4. Comandos, argumentos y flags

### Tipos de comandos
- **Internos**: Integrados en la Shell (`cd`, `echo`, etc.)
- **Externos**: Binarios del sistema (`cp`, `ls`, etc.)
- **Funciones y alias**: Personalizados por el usuario.

#### 📁 Comando `cp` en Linux

El comando `cp` (copy) se usa para **copiar archivos y directorios** en sistemas Unix/Linux. Puede copiar de una ubicación a otra o duplicar archivos bajo un nuevo nombre.
###### 🧠 Sintaxis básica

```bash
cp [opciones] origen destino
```

 ###### 📄 Copiar archivos

  ✅ Ejemplo 1: Copiar un archivo a otro con nuevo nombre
```bash
cp documento.txt copia_documento.txt
```
> 🔹 Crea una copia del archivo `documento.txt` con el nombre `copia_documento.txt` en el mismo directorio.

 ✅ Ejemplo 2: Copiar un archivo a otro directorio
```bash
cp documento.txt /home/david/Documentos/
```
> 🔹 Copia el archivo `documento.txt` al directorio `Documentos`.

###### 📂 Copiar directorios

⚠️ IMPORTANTE: Para copiar directorios necesitas la opción `-r` (recursiva)

 ✅ Ejemplo 3: Copiar un directorio completo
```bash
cp -r carpeta_original/ carpeta_copia/
```
> 🔹 Copia todos los archivos y subdirectorios de `carpeta_original` a `carpeta_copia`.

###### 🧾 Otras opciones útiles

 `-i` (interactivo)
Pregunta antes de sobrescribir un archivo existente.
```bash
cp -i archivo.txt destino/
```

 `-u` (actualiza)
Solo copia si el archivo de origen es más reciente que el de destino o si no existe en destino.
```bash
cp -u archivo.txt destino/
```

 `-v` (verbose)
Muestra qué archivos se están copiando (útil para seguimiento).
```bash
cp -v archivo.txt destino/
```

###### 🧪 Casos combinados

 ✅ Ejemplo 4: Copiar múltiples archivos a un directorio
```bash
cp archivo1.txt archivo2.txt /home/david/copias/
```
> 🔹 Copia ambos archivos al directorio `copias`.

 ✅ Ejemplo 5: Copiar con confirmación e información
```bash
cp -iv archivo.txt /home/david/backup/
```
> 🔹 Pide confirmación antes de sobrescribir y muestra el proceso.

###### 🚫 Errores comunes

- ❌ No usar `-r` al copiar directorios:
```bash
cp carpeta/ destino/
# Resultado: error "omitting directory"
```

- ❌ Confundir destino cuando es un archivo en lugar de un directorio:
```bash
cp archivo.txt otro_archivo.txt/
# Resultado: error si otro_archivo.txt no es un directorio
```

---

> ✅ Recomendación: Usa `-iv` si no estás seguro de sobrescribir archivos.

### Argumentos
- **Posicionales**: `cat archivo.txt`
- **Flags cortas**: `ls -l` / `-a`
- **Flags largas**: `ls --all`

### Combinar argumentos
```bash
cp archivo1 archivo2 /ruta/destino/
```

---

## 🔗 5. Operadores lógicos

### En shell:
- `&&`: Ejecuta el siguiente comando solo si el anterior fue exitoso.
- `||`: Ejecuta el segundo solo si el primero falló.
- `!`: Niega una condición.

### En scripts (comparaciones):
- Números: `-eq`, `-ne`, `-lt`, `-le`, `-gt`, `-ge`
- Cadenas: `=`, `!=`, `-z`, `-n`
- Archivos: `-e`, `-f`, `-d`, `-r`, `-w`, `-x`

### En herramientas:
- `grep 'error\|warning'`: OR lógico
- `find ... -and -size +1M`: AND lógico

---

## 🎛️ 6. Flags comunes

### Uso general
```bash
ls -l          # Flag corta
ls --help      # Flag larga
```

### Ejemplos por herramienta

#### `ls`
- `-l`, `-a`, `-h`

#### `cat`
- `-n`, `-E`

#### `grep`
- `-i`, `-r`, `-v`

#### `find`
- `-name`, `-type`, `-size`

#### `tar`
- `-czvf archivo.tar.gz carpeta`

#### `nmap`
- `-sS`, `-A`, `-p`, `-v`

#### `hydra`
- `-l`, `-P`, `-t`

#### `msfconsole`
- `-q`, `-x`

---

## 🧩 7. Alias en Bash

### ¿Qué es un alias?
Es una abreviatura personalizada para ejecutar comandos complejos.

### Crear alias temporal
```bash
alias ll='ls -la'
```

### Eliminar alias
```bash
unalias ll
```

### Hacer alias permanente
1. Edita `~/.bashrc`
2. Añade: `alias ll='ls -la'`
3. Ejecuta: `source ~/.bashrc`

---

> ✅ Usa esta nota como referencia rápida mientras trabajas con Kali Linux.


## 8. Linux Architecture

The Linux operating system can be broken down into layers:

|**Layer**|**Description**|
|---|---|
|`Hardware`|Peripheral devices such as the system's RAM, hard drive, CPU, and others.|
|`Kernel`|The core of the Linux operating system whose function is to virtualize and control common computer hardware resources like CPU, allocated memory, accessed data, and others. The kernel gives each process its own virtual resources and prevents/mitigates conflicts between different processes.|
|`Shell`|A command-line interface (**CLI**), also known as a shell that a user can enter commands into to execute the kernel's functions.|
|`System Utility`|Makes available to the user all of the operating system's functionality.|

---

## 9. File System Hierarchy

The Linux operating system is structured in a tree-like hierarchy and is documented in the [Filesystem Hierarchy](http://www.pathname.com/fhs/) Standard (FHS). Linux is structured with the following standard top-level directories:

![Diagram of Linux file system hierarchy with root directory branching to folders: /bin, /boot, /dev, /etc, /lib, /media, /mnt, /opt, /home, /run, /root, /proc, /sys, /tmp, /usr, /var.](https://academy.hackthebox.com/storage/modules/18/NEW_filesystem.png)

|**Path**|**Description**|
|---|---|
|`/`|The top-level directory is the root filesystem and contains all of the files required to boot the operating system before other filesystems are mounted, as well as the files required to boot the other filesystems. After boot, all of the other filesystems are mounted at standard mount points as subdirectories of the root.|
|`/bin`|Contains essential command binaries.|
|`/boot`|Consists of the static bootloader, kernel executable, and files required to boot the Linux OS.|
|`/dev`|Contains device files to facilitate access to every hardware device attached to the system.|
|`/etc`|Local system configuration files. Configuration files for installed applications may be saved here as well.|
|`/home`|Each user on the system has a subdirectory here for storage.|
|`/lib`|Shared library files that are required for system boot.|
|`/media`|External removable media devices such as USB drives are mounted here.|
|`/mnt`|Temporary mount point for regular filesystems.|
|`/opt`|Optional files such as third-party tools can be saved here.|
|`/root`|The home directory for the root user.|
|`/sbin`|This directory contains executables used for system administration (binary system files).|
|`/tmp`|The operating system and many programs use this directory to store temporary files. This directory is generally cleared upon system boot and may be deleted at other times without any warning.|
|`/usr`|Contains executables, libraries, man files, etc.|
|`/var`|This directory contains variable data files such as log files, email in-boxes, web application related files, cron files, and more.|

---
