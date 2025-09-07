#bases #linux #apuntes
# 🐧 Comandos básicos de Linux con ejemplos

## 📂 Navegación y gestión de archivos

### `uname`
Muestra información del sistema operativo.
```bash
uname -a    # Información completa del sistema
```

### `pwd`
Muestra la ruta absoluta del directorio actual.
```bash
pwd
```

### `ls`
Lista archivos y directorios.
```bash
ls -l       # Lista detallada
ls -a       # Incluye archivos ocultos
```

### `cd`
Cambia de directorio.
```bash
cd /home/usuario/    # ruta absoluta partiendo de la raiz "/"
cd ..                # Subir un nivel
```

### `tree`
Muestra la estructura de directorios en forma de árbol. Estructura del árbol de directorios y subdirectorios
```bash
tree        # Puede requerir instalación previa
tree -L 1   # Podemos limitar que nos muestre sólo hasta el nivel que queramos 
```

### `cp`
Copia archivos o directorios.
```bash
cp archivo.txt copia.txt    # copia de archivos
cp -r dir1/ dir2/           # Copia recursiva
```

### `mv`
Mueve o renombra archivos.
```bash
mv archivo.txt nueva_ubicacion/      # mv [origen] [destino]
mv archivo.txt nuevo_nombre.txt      # mv file_old.txt file_new.txt
```

### `rm`
Elimina archivos o directorios.
```bash
rm archivo.txt
rm -r carpeta/   # Elimina recursivamente
```

### `touch`
Crea archivos vacíos o actualiza su marca de tiempo.
```bash
touch nuevo_archivo.txt
```

### `mkdir`
Crea un nuevo directorio.
```bash
mkdir nueva_carpeta
mkdir -p ruta/completa/   # Crea estructura de carpetas
```

## 🔧 Redirecciones y permisos

### `>` `>>` `<`
Redireccionan entrada/salida.
```bash
echo "Hola" > saludo.txt     # Crea o sobreescribe
echo "Otra línea" >> saludo.txt  # Añade al final
cat < saludo.txt             # Entrada desde archivo
```

### `chmod`
Modifica permisos.
```bash
chmod 755 script.sh
chmod +x script.sh          # Da permiso de ejecución
```

### `chown`
Cambia el propietario.
```bash
sudo chown usuario:grupo archivo.txt
```

### Bits Especiales
- **SUID**: Ejecuta como propietario.
- **SGID**: Ejecuta con grupo del archivo.
- **Sticky Bit**: Solo propietario puede borrar.
```bash
chmod u+s archivo
chmod g+s carpeta/
chmod +t /tmp
```

## 🛠️ Comandos administrativos

### `su`
Cambia a otro usuario.
```bash
su         # Cambia a root
su - usuario
```

### `sudo`
Ejecuta como superusuario.
```bash
sudo apt update
```

## 📤 Transferencia de archivos

### `scp`
Copia entre máquinas por SSH.
```bash
scp archivo.txt usuario@host:/ruta/destino
```

## ✍️ Editores de texto

### `nano`
Editor simple.
```bash
nano archivo.txt
```

### `vim`
Editor avanzado.
```bash
vim archivo.txt
```

### `gedit`
Editor gráfico (entorno de escritorio).
```bash
gedit archivo.txt &
```

## 🧾 Lectura y búsqueda de texto

### `cat`
Muestra el contenido.
```bash
cat archivo.txt
```

### `grep`
Filtra líneas que contienen texto.
```bash
grep "error" log.txt
```

## 🗜️ Compresión

### `zip` / `unzip`
Comprimir y descomprimir archivos.
```bash
zip archivo.zip archivo.txt
unzip archivo.zip
```

### `tar`
Archivar y comprimir.
```bash
tar -cvf archivo.tar carpeta/
tar -xvf archivo.tar
```

## 🔍 Monitorización y gestión del sistema

### `ps`
Muestra procesos activos.
```bash
ps aux       # Todos los procesos
```

### `history`
Muestra el historial de comandos.
```bash
history
```

---

> ✅ Ideal para repaso y uso diario en terminal. Compatible con Obsidian.
