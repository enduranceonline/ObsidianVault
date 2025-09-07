#bases #linux #apuntes
# 🐱‍💻 Kali Linux - Introducción

Esta nota reúne atajos, comandos útiles y herramientas esenciales para comenzar con Kali Linux, organizado de forma clara y práctica para entornos de pentesting y administración avanzada.

---

## 🧭 1. Atajos útiles en Kali Linux

### 🖥️ Terminal (Bash)
- `Ctrl + C`: Detener comando en ejecución.
- `Ctrl + Z`: Suspender proceso (recuperar con `fg`).
- `Ctrl + L`: Limpiar pantalla.
- `Ctrl + D`: Cerrar terminal.
- `!!`: Repetir último comando.
- `!n`: Ejecutar comando nº `n` del historial.
- `Ctrl + R`: Buscar comando anterior.
- `Alt + .`: Insertar último argumento anterior.

### ✍️ Edición de texto
- `Ctrl + A / E`: Ir al inicio / final de la línea.
- `Ctrl + U / K`: Borrar al inicio / final de línea.
- `Ctrl + W`: Borrar palabra anterior.
- `Alt + F / B`: Mover una palabra adelante / atrás.

### 🗂️ Archivos y directorios
- `Tab`: Autocompletar.
- `cd -`: Volver al directorio anterior.

### 🧭 Sesión y navegación
- `Ctrl + Alt + T`: Nueva terminal.
- `Ctrl + Shift + T / W`: Nueva pestaña / cerrar pestaña.
- `Alt + Tab`: Cambiar ventana.
- `Ctrl + Alt + Fx`: Cambiar entre TTYs.

---

## 🔧 2. Comandos esenciales

### 📦 Gestión de paquetes
```bash
sudo apt update -y && sudo apt upgrade -y   # Actualiza el sistema
sudo apt full-upgrade -y                   # Actualización con cambios de dependencias
sudo apt dist-upgrade                      # Similar, más agresiva
sudo apt autoremove                        # Elimina dependencias no necesarias
sudo apt autoclean                         # Limpia caché obsoleta
```

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
