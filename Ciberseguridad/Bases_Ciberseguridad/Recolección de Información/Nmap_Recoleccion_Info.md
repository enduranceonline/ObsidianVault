#bases #network #apuntes
# 🌐 Nmap - Recolección de Información

Este apunte recoge los usos más comunes y efectivos de `nmap` para la recolección de información, desde escaneos básicos hasta técnicas de evasión y detección de servicios. Ideal para fases iniciales de pentesting.

---

## 🧠 1. ¿Qué es Nmap?

`nmap` (Network Mapper) es una herramienta de código abierto para escanear redes y descubrir hosts, puertos, servicios, sistemas operativos y vulnerabilidades potenciales.

---

## 🚀 2. Escaneos básicos

### Ver si un host está activo
```bash
nmap -sn 192.168.1.0/24
```
> Escaneo de ping (descubrimiento de hosts activos en la red).

### Escaneo de puertos más comunes
```bash
nmap 192.168.1.1
```

### Escaneo completo (puertos 1-65535)
```bash
nmap -p- 192.168.1.1
```

---

## 🧰 3. Detección de servicios y versiones

```bash
nmap -sV 192.168.1.1
```
> Intenta identificar el software y la versión de los servicios que corren en los puertos abiertos.

### Banner grabbing + versión
```bash
nmap -sV --version-intensity 5 192.168.1.1
```

---

## 🛠️ 4. Detección de sistema operativo

```bash
nmap -O 192.168.1.1
```
> Requiere privilegios elevados. Intenta identificar el sistema operativo del host.

---

## 🧪 5. Escaneos avanzados

### Escaneo con scripts NSE (Nmap Scripting Engine)
```bash
nmap --script=vuln 192.168.1.1
```
> Ejecuta scripts que identifican vulnerabilidades conocidas.

### Script HTTP:
```bash
nmap -p 80 --script=http-enum 192.168.1.1
```

### Script FTP:
```bash
nmap -p 21 --script=ftp-anon 192.168.1.1
```

---

## 🕵️ 6. Técnicas de evasión y sigilo

### Escaneo "stealth" SYN
```bash
nmap -sS 192.168.1.1
```

### Cambiar puerto fuente
```bash
nmap --source-port 53 192.168.1.1
```

### Fragmentar paquetes
```bash
nmap -f 192.168.1.1
```

### Escaneo con intervalo de tiempo
```bash
nmap -T2 192.168.1.1
```
> Reduce la velocidad del escaneo para evitar detección.

---

## 🧾 7. Exportar resultados

```bash
nmap -oN salida.txt 192.168.1.1
nmap -oX salida.xml 192.168.1.1
```

---

## 📚 8. Escaneos combinados útiles

### Escaneo rápido con detección de versiones y OS
```bash
nmap -sS -sV -O -T4 192.168.1.1
```

### Todos los scripts NSE contra un host
```bash
nmap -sC -sV 192.168.1.1
```

---

## 🧩 9. Combinaciones prácticas

| Opción         | Función                                  |
|----------------|-------------------------------------------|
| `-sS`          | Escaneo SYN (stealth)                     |
| `-sV`          | Detectar versiones                        |
| `-O`           | Detección de sistema operativo            |
| `-p-`          | Escanear todos los puertos                |
| `--script=vuln`| Buscar vulnerabilidades conocidas         |
| `-T0` a `-T5`  | Control de velocidad/agresividad          |
| `-oN`, `-oX`   | Exportar en formato legible o XML         |

---

## 🛡️ 10. Cuándo usar qué tipo de escaneo

- **Reconocimiento inicial**: `nmap -sn` o `nmap -sP`
- **Detección de servicios**: `nmap -sV -p-`
- **Enumeración avanzada**: `--script=*`
- **Evasión de detección IDS/IPS**: `-sS -T2 -f`
- **Red interna**: `-sC -sV -O -T4`

---

> 🧠 Tip: Usa `nmap --script-help <script>` para entender qué hace un script NSE antes de usarlo.
