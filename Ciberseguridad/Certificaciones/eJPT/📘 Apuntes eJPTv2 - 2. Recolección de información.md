#apuntes #certificacion #eJPT #nmap #linux 

# nmap

**Network Mapper**
Esta herramienta nos permite conocer mejor la red con la que estamos trabajando. Viene instalada por defecto en kali y Parrot. Podemos ver los puertos abiertos y cerrados.

URL web oficial: [[https://nmap.org/man/es/|nmap]]

---
## 1. Características

### 1.1 Network Mapper

Herramienta que permite conocer mejor la red con la que estamos trabajando. Viene instalada por defecto en Kali y Parrot. Sirve para identificar **puertos abiertos/cerrados**, servicios y sistemas operativos.  
### 1.2 Network scanning

Realiza diferentes tipos de escaneo (ping, TCP, UDP, SYN, etc.) para mapear el estado de los puertos.  
### 1.3 Objetivo

#### - **Network exploration:** explorar y mapear la red.

#### - **Security auditing:** auditar sistemas, detectar vulnerabilidades y comprobar configuraciones de seguridad.  

### 1.4 Descubrir

#### - **Dispositivos disponibles en la red** (hosts activos).  

#### - **Servicios y versiones** que se están ejecutando en cada puerto.  

#### - **Sistema operativo** y características de la máquina objetivo.  

### 1.5 Usada por profesionales de seguridad y por sysadmin

- Profesionales de **seguridad** para pentesting y auditorías.  
- **Administradores de sistemas** para inventario, monitorización y resolución de incidencias.  

---
## 2. Escaneos

	Antes de nada, es importante conocer el funcionamiento del comando ifconfig para descubrir las    
	interfaces de red que el sistema tiene disponibles y su configuración actual.
### 2.1 Salida de `ifconfig`
![[Pasted image 20250907150853.png]]

- **`eth0` → Interfaz Ethernet (red real o virtual)**
    - Es la tarjeta de red principal que conecta tu máquina al resto de la red.
    - Tiene asignada una **dirección IPv4** (`10.0.2.15`), una **máscara de subred** y una **dirección MAC**.
    - También puede tener direcciones **IPv6**.
    - A través de esta interfaz tu máquina se comunica con otras máquinas en la red local o hacia internet.
- **`lo` → Interfaz loopback (localhost)**
    - Es una interfaz **virtual** que no sale de la máquina.
    - Siempre usa la dirección IP `127.0.0.1`.
    - Sirve para que un sistema pueda comunicarse **consigo mismo**, muy útil para pruebas de red y aplicaciones locales.
    - Ejemplo: cuando accedes a `http://127.0.0.1:8080`, estás entrando a un servicio que corre en tu propio equipo.
#### Interfaz `eth0` (Ethernet)
| Campo | Descripción |
|-------|-------------|
| flags=4163<UP,BROADCAST,RUNNING,MULTICAST> | Estado de la interfaz: UP (activa), BROADCAST (permite broadcast), RUNNING (funcionando), MULTICAST (acepta multicast). |
| mtu 1500 | Tamaño máximo de los paquetes (1500 bytes). |
| inet 10.0.2.15 | Dirección IPv4 asignada. |
| netmask 255.255.255.0 | Máscara de subred (/24). |
| broadcast 10.0.2.255 | Dirección de broadcast de la red. |
| inet6 ... | Direcciones IPv6 asignadas (global y link-local). |
| ether 08:00:27:59:3c:17 | Dirección MAC de la tarjeta de red. |
| txqueuelen 1000 | Tamaño de la cola de transmisión. |
| RX packets / bytes | Paquetes y bytes **recibidos** (≈2.3 GiB). |
| TX packets / bytes | Paquetes y bytes **enviados** (≈610 MiB). |
| RX/TX errors, dropped, overruns, collisions | Estadísticas de errores → todo en 0 (sin problemas de red). |
#### Interfaz `lo` (Loopback)
| Campo | Descripción |
|-------|-------------|
| flags=73<UP,LOOPBACK,RUNNING> | Estado: activa, loopback (interfaz interna). |
| mtu 65536 | Tamaño máximo de los paquetes. |
| inet 127.0.0.1 | Dirección IPv4 (localhost). |
| netmask 255.0.0.0 | Máscara de subred estándar para loopback. |
| RX/TX packets / bytes | Paquetes transmitidos y recibidos localmente. |
| RX/TX errors... | Estadísticas de errores (normalmente 0). |
## 2.2 1️⃣ **Tipos de escaneo (método de descubrimiento de puertos)**

Estos definen **cómo Nmap interactúa con el puerto** para determinar si está abierto, cerrado o filtrado.

📌 **Ejemplo práctico:**

`nmap -sS -p- [IP]   # Escaneo SYN de todos los puertos`
### 👉 **-sS: TCP SYN Scan (por defecto)**  
  Escaneo rápido y sigiloso que envía un paquete SYN. Si recibe SYN/ACK → puerto abierto, si recibe RST → puerto cerrado. No completa la conexión (half-open scan). 

### **-sT: TCP Connect() Scan**  
  Completa la conexión TCP con el sistema objetivo. Menos sigiloso porque queda registrado en logs, pero no requiere privilegios de root.  

### **-sA: ACK Scan**  
  Envía paquetes ACK para mapear reglas de firewall y distinguir si un puerto está filtrado o no. No determina si un puerto está abierto o cerrado.  

### **-sW: Window Scan**  
  Variante del ACK Scan que analiza el tamaño de la ventana TCP en la respuesta para inferir el estado del puerto.  

### **-sM: Maimon Scan**  
  Escaneo menos común que explota un comportamiento descrito por Uriel Maimon en ciertos sistemas TCP.  

### **-sU: UDP Scan**  
  Escanea puertos UDP. Más lento que TCP porque muchos servicios no responden fácilmente, requiriendo retransmisiones.  

### **-sN: Null Scan**  
  Envía paquetes TCP sin flags. Un puerto abierto no debería responder; uno cerrado suele devolver un RST.  

### **-sF: FIN Scan**  
  Envía un paquete con el flag FIN. Los puertos cerrados responden con RST, los abiertos no responden.  

### **-sX: Xmas Scan**  
  Envía un paquete con los flags FIN, PSH y URG encendidos (como un "árbol de navidad"). Similar al Null y FIN Scan para detectar puertos abiertos/cerrados.  

## 2.3  2️⃣ **Opciones/comandos adicionales (parámetros que complementan el escaneo)**

Estos no cambian la forma en que Nmap envía los paquetes, sino que **añaden funciones**

📌 **Ejemplo práctico:**

`nmap -sS -sV -O -p- --min-rate 5000 [IP]`

	`-sS` define **cómo se hace el escaneo**
    `-sV -O -p- --min-rate` son **opciones que complementan el escaneo**

`nmap [IP]`

	por defecto hace un escaneo del Top1000 de puertos mas usados y solo devolvera los que encuentre    
	abiertos sin mas informacion.

`nmap -p- [IP]
`nmap 1-65535 [IP]

	Si queremos escanear todos los puertos (65535)

![[Pasted image 20250907155921.png]]
![[Pasted image 20250907175808.png]]
### 🔹 Opción `-v / -vv`

- **Descripción:** Muestra información detallada (verbose) del escaneo. A medida que encuentre puertos abiertos los va volcando la info del escaneo a tiempo real. Lo podemos usar si tarda mucho como un reconocimiento inicial. Aunque de cara a las certificaciones y coger capturas no va bien.
    
- **Ejemplo:**
    

```bash
nmap [IP] -v
nmap [IP] -vv
```

### 🔹 👉Opción `-sV`

- **Descripción:** Detecta el servicio y la **versión** que se ejecuta en los puertos que están abiertos.
    
- **Ejemplo:**
    

```bash
nmap -sV [IP]
```

### 🔹 Opción `-O`

- **Descripción:** Identifica el **sistema operativo** del host.
    
- **Ejemplo:**
    

```bash
nmap -O [IP]
```

### 🔹 Opción `-oA`

- **Descripción:** Exporta los resultados del escaneo en **tres formatos**:
    
    - Normal (`.nmap`)
        
    - Grepable (`.gnmap`)
        
    - XML (`.xml`)
        
- **Ejemplo:**
    

```bash
nmap -oA resultado [IP]
```

_(Genera: `resultado.nmap`, `resultado.gnmap`, `resultado.xml`)_

### 🔹 Opción `-sC`

- **Descripción:** Ejecuta los **scripts por defecto** de Nmap (NSE).
    
- **Ejemplo:**
    

```bash
nmap -sC [IP]
```

### 🔹 Opción `--min-rate

- **Descripción:** Envía los paquetes a una velocidad mínima especificada (en paquetes por segundo).  
	Útil para acelerar el escaneo.  
    
- **Ejemplo:**
    un min rate de 5000 va hacer que tarde mucho menos nmap en ejecutar. Como contra, puede hacer que nos dejemos información por el camino, aunque para el eJPT nos agiliza los tiempos.

```bash
nmap --min-rate 5000 [IP]
```

### 🔹 Opción `-Pn`

- **Descripción:** Trata al host como **online**, sin hacer ping previo.  Algunas veces nos lo pedirá el propio nmap cuando la maquina no responda a los pings que estamos lanzando
    Se usa cuando ICMP está bloqueado por firewall.
    
- **Ejemplo:**
    

```bash
nmap -Pn [IP]
```

---

### 🔹 Opción `--traceroute`

- **Descripción:** Muestra los **saltos de red** (routers intermedios) hasta el objetivo. No se usa tanto para descubrir servicios, sino para **entender la topología de red entre tu máquina y el objetivo**. Esto es importante en un pentest (y en el eJPT) por varias razones:
#### 🔎 ¿Por qué interesa conocer los saltos de red?

1. **Identificación de Firewalls y Filtrado**
    - Si un traceroute se detiene en cierto salto o empieza a mostrar _timeouts_, puede indicar la presencia de un firewall, IDS/IPS o reglas de filtrado.
        
    - Ejemplo: Si no llegas al host pero ves que muere en un salto intermedio, probablemente hay filtrado en el camino.
        
2. **Reconocimiento de la infraestructura**
    - Permite ver **qué routers intermedios existen** entre tú y el objetivo.
        
    - Puede revelar información de **proveedores de red, IPs internas o externas** que normalmente no se verían.
        
3. **Detección de NAT o segmentación de red**
    - Si el último salto visible es una IP pública y después el host responde con una IP interna (privada), podemos inferir que está detrás de un **NAT o segmentado en una red privada**.
        
4. **Ayuda en Pivoting y Movimiento Lateral**
    - Saber cómo llegas a la máquina te da pistas de qué otras redes existen detrás.
        
    - En pruebas avanzadas, estos datos ayudan a planear un **pivoting** o un ataque en entornos con múltiples subredes.
        
5. **Optimización de ataques**
    - Si ves que la conexión pasa por varios saltos con latencia alta, puedes ajustar herramientas (como Nmap con `--min-rate` o `--max-retries`) para que sean más eficientes.
- **Ejemplo:**
    

```bash
nmap --traceroute [IP]
```

---

### 🔹 Opción `-p`

- **Descripción:** Permite definir **puertos específicos** a escanear.
    
- **Ejemplos:**
    

```bash
nmap -p22 [IP]          # Escanear solo el puerto 22
nmap -p21,22,80 [IP]    # Escanear múltiples puertos
nmap -p- [IP]           # Escanear todos los puertos (1-65535)
```

---

### 🔹👉 Opción `-A`

- **Descripción:** Escaneo agresivo. Incluye:
    
    - Detección de sistema operativo
        
    - Versión de servicios
        
    - Scripts NSE por defecto
        
    - Traceroute
        
- **Ejemplo:**
    

```bash
nmap -A [IP]
```

---
## 2.4 Escaneos

### 🔹 Escaneo completo de puertos con detección de servicios

```bash
nmap -p- -sV --min-rate 5000 [IP]
```

- `-p-` → Escanea **todos los puertos (1-65535)**
    
- `-sV` → Detecta el **servicio y la versión** que corre en el puerto
    
- `--min-rate 5000` → Asegura que se envíen al menos **5000 paquetes por segundo** (más rápido)
    

### 🔹 Escaneo agresivo

```bash
nmap -A [IP]
```

- Incluye:
    
    - Detección de **SO**
        
    - Detección de **versión de servicios**
        
    - Ejecución de **scripts NSE por defecto**
        
    - **Traceroute**
        

### 🔹 Escaneo enfocado en SMB

```bash
nmap -p139,445 --script=*smb* [IP]
```

- `-p139,445` → Escanea los puertos de **SMB**
    
- `--script=*smb*` → Ejecuta los scripts NSE relacionados con **SMB**  
    (ejemplo: enumeración de usuarios, vulnerabilidades conocidas como EternalBlue, etc.)
    

✅ Este escaneo es útil para **detección de vulnerabilidades SMB** en entornos Windows.


---
## 2.5 Scripts

### 📌 Nmap Scripting Engine (NSE)

#### 🔹 ¿Qué es?
El **Nmap Scripting Engine (NSE)** permite ampliar las funcionalidades de Nmap mediante **scripts en Lua**.  
Estos scripts están diseñados para:  
- Detectar versiones e información detallada del objetivo  
- Detectar **vulnerabilidades**  
- Explotar vulnerabilidades conocidas  
#### 🔹 Ubicación de scripts
Los scripts por defecto de Nmap se encuentran en:

`/usr/share/nmap/scripts`

#### 🔹 Ejecución de scripts

Se ejecutan con la opción `--script`:
````
nmap [IP] --script=[nombre_script]
````
 
 Ejemplo:
````
nmap [IP] --script=[nombre_script]
````
 (Muestra el título de las páginas web que corren en el host)

#### 🔹 Uso de comodines

Se pueden ejecutar varios scripts de una categoría usando comodines:

```
nmap [IP] --script="http-*"
```
(Ejecuta todos los scripts relacionados con HTTP)

#### 🔹 Categorías de scripts NSE

Algunos grupos comunes de scripts:

- `auth` → autenticación
- `brute` → fuerza bruta
- `discovery` → descubrimiento de servicios
- `vuln` → búsqueda de vulnerabilidades
- `exploit` → explotación directa

✅ NSE es muy útil para automatizar pruebas específicas (como SMB, HTTP, FTP, etc.) sin tener que usar herramientas externas

![[Pasted image 20250907184035.png]]

#### 📌 Categorías de Scripts NSE (Nmap Scripting Engine)

> ⚠️ En el eJPT no es necesario aprender cada uno en detalle, pero sí entender para qué sirven en general.

### 🔹 Auth
- Scripts relacionados con **autenticación**.  
- Ej: probar credenciales, enumerar métodos de login.  

### 🔹 Broadcast
- Escanean múltiples hosts a través de la red local.  
- Útiles para descubrimiento rápido de servicios.  

### 🔹 Default
- Scripts que se ejecutan con `-sC`.  
- Diseñados para ser **seguros y rápidos**.  

### 🔹 Discovery
- Descubren información adicional sobre el objetivo.  
- Ej: nombres de host, rutas, recursos compartidos.  

### 🔹 Dos
- Scripts de **Denial of Service** (DoS).  
- ⚠️ No se usan en entornos legales de pentest básico.  

### 🔹 Exploit
- Intentan **explotar vulnerabilidades** conocidas.  
- Ej: SMB exploits, HTTP exploits.  

### 🔹 External
- Dependen de **servicios externos** (p. ej., consultar reputación de IPs en bases de datos online).  

### 🔹 Fuzzer
- Scripts que realizan **fuzzing** enviando entradas inesperadas.  
- Útiles para detectar comportamientos anómalos.  

### 🔹 Intrusive
- Pueden ser **invasivos** y generar efectos secundarios.  
- Ej: intentos de login por fuerza bruta.  

### 🔹 Malware
- Detectan posibles **infecciones o backdoors** conocidas.  

### 🔹 Safe
- Scripts considerados **seguros** para usarse sin impacto negativo.  
- ⚖️ Son los recomendados en entornos productivos.  

### 🔹 Version
- Recopilan información sobre **versiones de servicios** (complemento de `-sV`).  

### 🔹 Vuln
- Buscan **vulnerabilidades conocidas** en los servicios detectados.  
- Ej: detección de Heartbleed, MS17-010 (EternalBlue), etc.  

---

✅ En la práctica para el eJPT, las más útiles suelen ser:  
- **Default**, **Discovery**, **Version** y **Vuln**.  
- Ejemplo:
```
nmap -p80,443 --script=vuln [IP]
```

