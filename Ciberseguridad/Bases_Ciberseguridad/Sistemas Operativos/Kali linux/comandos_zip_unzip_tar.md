#bases #linux #guia
# 🗜️ Comandos `zip`, `unzip` y `tar` en Linux

En sistemas Linux, estos comandos se utilizan para **comprimir** y **descomprimir** archivos y directorios, pero cada uno tiene características, opciones y formatos distintos.

---

## 🔹 `zip` y `unzip`

### 📌 ¿Qué es `zip`?
`zip` comprime archivos en un único archivo `.zip`. Es compatible con otros sistemas operativos (Windows, macOS) y permite **compresión individual por archivo** dentro del contenedor.

### 📌 ¿Qué es `unzip`?
`unzip` se utiliza para descomprimir archivos `.zip`.

---

### ✅ Sintaxis

```bash
zip [opciones] archivo.zip archivos...
unzip archivo.zip
```

---

### ✅ Ejemplos

#### Crear un archivo zip con varios archivos:
```bash
zip archivos.zip documento.txt imagen.png script.sh
```

#### Crear un zip de una carpeta completa:
```bash
zip -r carpeta.zip mi_carpeta/
```

#### Ver el contenido de un archivo zip:
```bash
unzip -l archivos.zip
```

#### Extraer un archivo zip:
```bash
unzip archivos.zip
```

#### Extraer en una carpeta específica:
```bash
unzip archivos.zip -d /ruta/destino/
```

---

### ✅ Opciones útiles de `zip`

| Opción | Descripción |
|--------|-------------|
| `-r`   | Comprime de forma recursiva (directorios) |
| `-e`   | Solicita contraseña para proteger el zip |
| `-9`   | Compresión máxima |

---

## 🔸 `tar`

### 📌 ¿Qué es `tar`?
`tar` se usa para **agrupar** archivos en un único archivo `.tar`, con o sin compresión. Por sí solo **no comprime**, solo empaqueta. Pero combinado con otras herramientas (`gzip`, `bzip2`, `xz`), se vuelve muy potente.

- `.tar` → solo empaquetado
- `.tar.gz` o `.tgz` → empaquetado + compresión GZIP
- `.tar.bz2` → compresión con BZIP2
- `.tar.xz` → compresión con XZ

---

### ✅ Sintaxis

```bash
tar [opciones] archivo.tar archivos...
```

---

### ✅ Ejemplos comunes

#### Crear un archivo `.tar` sin comprimir:
```bash
tar -cvf archivos.tar archivo1.txt archivo2.txt
```

#### Crear un `.tar.gz` comprimido:
```bash
tar -czvf archivos.tar.gz carpeta/
```

#### Extraer `.tar.gz`:
```bash
tar -xzvf archivos.tar.gz
```

#### Listar contenido sin extraer:
```bash
tar -tvf archivos.tar.gz
```

#### Extraer en una carpeta específica:
```bash
tar -xzvf archivos.tar.gz -C /ruta/destino/
```

---

### ✅ Opciones comunes de `tar`

| Opción | Descripción |
|--------|-------------|
| `-c`   | Crear archivo |
| `-x`   | Extraer archivo |
| `-v`   | Mostrar progreso |
| `-f`   | Nombre del archivo |
| `-z`   | Usar compresión gzip |
| `-j`   | Usar compresión bzip2 |
| `-J`   | Usar compresión xz |

---

## 🔍 Diferencias principales

| Característica        | `zip`                      | `tar` + compresión |
|-----------------------|----------------------------|---------------------|
| Compatibilidad        | Alta (Windows, macOS)      | Alta (Linux/Unix)   |
| Compresión por archivo| Sí                         | No (archivo único)  |
| Seguridad             | Puede usar contraseña      | No por defecto      |
| Eficiencia            | Menos eficiente            | Más eficiente       |
| Uso más común         | Archivos individuales      | Backups completos   |

---

## 🎯 Cuándo usar uno u otro

- Usa **`zip`** si necesitas compartir archivos con usuarios de Windows o añadir contraseña fácilmente.
- Usa **`tar`** (especialmente `.tar.gz`) para copias de seguridad, despliegues y empaquetado eficiente en sistemas Linux.

---

> ✅ Recomendación: Para backups, usa `tar -czvf`; para compartir, usa `zip -r`.
