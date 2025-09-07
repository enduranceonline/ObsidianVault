#bases #linux #guia
# 📁 Comando `cp` en Linux

El comando `cp` (copy) se usa para **copiar archivos y directorios** en sistemas Unix/Linux. Puede copiar de una ubicación a otra o duplicar archivos bajo un nuevo nombre.

---

## 🧠 Sintaxis básica

```bash
cp [opciones] origen destino
```

---

## 📄 Copiar archivos

### ✅ Ejemplo 1: Copiar un archivo a otro con nuevo nombre
```bash
cp documento.txt copia_documento.txt
```
> 🔹 Crea una copia del archivo `documento.txt` con el nombre `copia_documento.txt` en el mismo directorio.

### ✅ Ejemplo 2: Copiar un archivo a otro directorio
```bash
cp documento.txt /home/david/Documentos/
```
> 🔹 Copia el archivo `documento.txt` al directorio `Documentos`.

---

## 📂 Copiar directorios

### ⚠️ IMPORTANTE: Para copiar directorios necesitas la opción `-r` (recursiva)

### ✅ Ejemplo 3: Copiar un directorio completo
```bash
cp -r carpeta_original/ carpeta_copia/
```
> 🔹 Copia todos los archivos y subdirectorios de `carpeta_original` a `carpeta_copia`.

---

## 🧾 Otras opciones útiles

### `-i` (interactivo)
Pregunta antes de sobrescribir un archivo existente.
```bash
cp -i archivo.txt destino/
```

### `-u` (actualiza)
Solo copia si el archivo de origen es más reciente que el de destino o si no existe en destino.
```bash
cp -u archivo.txt destino/
```

### `-v` (verbose)
Muestra qué archivos se están copiando (útil para seguimiento).
```bash
cp -v archivo.txt destino/
```

---

## 🧪 Casos combinados

### ✅ Ejemplo 4: Copiar múltiples archivos a un directorio
```bash
cp archivo1.txt archivo2.txt /home/david/copias/
```
> 🔹 Copia ambos archivos al directorio `copias`.

### ✅ Ejemplo 5: Copiar con confirmación e información
```bash
cp -iv archivo.txt /home/david/backup/
```
> 🔹 Pide confirmación antes de sobrescribir y muestra el proceso.

---

## 🚫 Errores comunes

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

## 📌 Resumen rápido

| Opción | Función                             |
|--------|-------------------------------------|
| `-r`   | Copia directorios recursivamente    |
| `-i`   | Solicita confirmación al sobrescribir |
| `-u`   | Copia solo si es más reciente       |
| `-v`   | Muestra detalles de la operación    |

---

> ✅ Recomendación: Usa `-iv` si no estás seguro de sobrescribir archivos.
