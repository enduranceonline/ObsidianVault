#bases #bash #ejercicio
# 📁 Bash - Recolección de Información (sin Nmap)

Este apunte recopila métodos prácticos de **recolección de información** en Bash basados en desafíos como **Bandit (OverTheWire)** y otros entornos de entrenamiento. No se usa Nmap; el enfoque está en herramientas básicas como `nc`, `telnet`, `curl`, y utilidades propias de Bash.

---

## 🧭 1. ¿Qué buscamos en la fase de Recolección?

- Puertos abiertos (manual)
- Servicios disponibles
- Banners de servicios
- Ficheros accesibles
- Métodos de conexión válidos
- Información de usuarios y entorno

---

## 🧰 2. Herramientas clave sin Nmap

### 🔌 `nc` (Netcat)
Netcat es una herramienta para conexión directa por TCP o UDP. Permite enviar y recibir datos manualmente.

#### ✅ Escanear puertos manualmente
```bash
for port in {20..1024}; do nc -zv 192.168.1.1 $port 2>&1 | grep open; done
```
> Escanea puertos del 20 al 1024 en busca de servicios abiertos.

#### ✅ Obtener banners
```bash
nc 192.168.1.1 80
HEAD / HTTP/1.1
Host: 192.168.1.1
```
> Al conectarte a un puerto y enviar una petición HTTP, puedes recibir un banner con versión de software.

---

### 📞 `telnet`
Permite conexión a puertos remotos de forma similar a `nc`.

```bash
telnet 192.168.1.1 22
```
> Útil para comprobar manualmente si un puerto está abierto y qué banner devuelve.

---

### 🌐 `curl` y `wget`
Para obtener contenido de URLs o rutas accesibles por HTTP/HTTPS.

```bash
curl -I http://192.168.1.1
```
> Muestra cabeceras HTTP (versión del servidor, cookies, etc.)

```bash
wget --spider http://192.168.1.1
```
> Comprueba si un recurso está disponible sin descargarlo.

---

## 🔍 3. Comprobaciones del sistema

### 🧠 Variables de entorno
```bash
env
printenv
```
> Identificar rutas, usuarios, o configuraciones internas útiles para escalar privilegios o moverse lateralmente.

### 🏠 Archivos de interés
```bash
cat /etc/passwd | cut -d: -f1
```
> Lista de usuarios del sistema.

```bash
find / -perm -4000 2>/dev/null
```
> Binarios con SUID activado (posibles escaladas).

---

## 📂 4. Extracción y análisis de ficheros

### Buscar archivos ocultos
```bash
ls -la
```

### Leer archivos línea a línea
```bash
while read line; do echo $line; done < archivo.txt
```

### Decodificar cadenas
```bash
echo "c3VwZXIgc2VjcmV0" | base64 -d
```
> Decodifica una cadena base64 (útil en muchos niveles de Bandit).

---

## 🔐 5. Otras técnicas clave (Bandit & similares)

### Acceder como otro usuario con contraseña conocida
```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```

### Leer archivo con permisos restringidos vía comandos indirectos
```bash
cat ./-file
```
> Archivos con nombres no estándar pueden requerir sintaxis especial.

### Usar comandos `strings`, `grep`, `xxd`
```bash
strings archivo.bin | grep pass
xxd archivo | less
```
> Útiles para buscar contenido legible en binarios.

---

## 🔗 6. Combinaciones útiles en Bash

### Conectar y volcar información a archivo
```bash
nc 192.168.1.1 80 > salida.txt
```

### Buscar patrones en la salida
```bash
cat salida.txt | grep flag
```

### Automatizar tareas con bucles
```bash
for i in $(seq 1 65535); do echo "probando $i"; done
```

---

## 📌 Conclusión

Aunque `nmap` es potente, con herramientas básicas de Bash puedes:
- Detectar servicios y puertos abiertos
- Leer banners y cabeceras
- Obtener archivos expuestos
- Acceder como usuarios conocidos
- Automatizar búsquedas y extracción de datos

> 🧠 Estas técnicas son esenciales para entornos restringidos o CTFs donde el uso de `nmap` está bloqueado o limitado.
