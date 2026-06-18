#bases #network #ejercicio
# 🔧 Nmap - Ejercicios Prácticos con One-Liners

Este apunte contiene una colección de **one-liners con Nmap**, ideales para situaciones reales de reconocimiento, escaneo y enumeración en pruebas de penetración.

---

## 🧠 ¿Qué es un One-Liner?

Una línea de comando compacta que realiza una tarea completa, combinando múltiples opciones de Nmap para lograr resultados potentes en una sola ejecución.

---

## 🧪 1. Escaneo completo de puertos con detección de servicios

```bash
nmap -p- -sV 192.168.1.1
```
> Escanea todos los puertos TCP (1-65535) e identifica servicios y versiones.

---

## 🔍 2. Escaneo SYN + detección de OS + servicios + scripts NSE básicos

```bash
nmap -sS -sV -O -sC -T4 192.168.1.1
```
> Escaneo rápido con información detallada sobre servicios y sistema operativo.

---

## 🎯 3. Escaneo de múltiples hosts desde un archivo

```bash
nmap -iL targets.txt -sS -sV -oN resultado.txt
```
> Escanea todos los hosts listados en `targets.txt` y guarda la salida.

---

## 🛡️ 4. Escaneo con técnicas de evasión

```bash
nmap -sS -T2 -f --data-length 20 --source-port 53 192.168.1.1
```
> Fragmenta paquetes, camufla el tráfico como DNS y reduce velocidad para evadir detección.

---

## 🌐 5. Enumeración de servicios HTTP

```bash
nmap -p 80,443 --script=http-title,http-headers,http-enum 192.168.1.1
```
> Ejecuta scripts HTTP comunes para extraer información del servidor web.

---

## 🔐 6. Buscar servicios FTP anónimos

```bash
nmap -p 21 --script=ftp-anon 192.168.1.1
```
> Comprueba si se permite acceso FTP anónimo.

---

## 🧰 7. Buscar vulnerabilidades con NSE

```bash
nmap --script=vuln -p 80,443,21,22,23 192.168.1.1
```
> Usa scripts de tipo "vuln" para identificar servicios con vulnerabilidades conocidas.

---

## 🗂️ 8. Guardar resultados en diferentes formatos

```bash
nmap -sV -oA escaneo_completo 192.168.1.1
```
> Genera tres archivos: `.nmap` (normal), `.gnmap` (greppable), `.xml` (automatización).

---

## 📦 9. Escanear solo puertos comunes abiertos

```bash
nmap --top-ports 100 -sV 192.168.1.1
```
> Escanea los 100 puertos más comunes.

---

## 📑 10. Buscar palabras clave en banners

```bash
nmap -sV --script=banner -p- 192.168.1.1 | grep -i 'apache\|ssh\|nginx'
```
> Filtra los banners detectados para buscar software conocido.

---

## 💡 Consejos adicionales

- Usa `--script-help <script>` para saber qué hace un script NSE antes de usarlo.
- Agrega `--reason` para entender por qué se considera un puerto abierto.
- Añade `--open` para mostrar solo puertos abiertos.
- Combina `grep`, `awk` o `cut` para análisis post-escaneo.

---

> 🧠 Ideal para scripts de automatización o para uso rápido en entornos con tiempo limitado.
