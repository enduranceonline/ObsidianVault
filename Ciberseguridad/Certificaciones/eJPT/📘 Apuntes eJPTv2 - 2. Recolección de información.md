#apuntes #certificacion #eJPT

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
## 2.2 Tipos de escaneo

- **-sS: TCP SYN Scan (por defecto)**  
  Escaneo rápido y sigiloso que envía un paquete SYN. Si recibe SYN/ACK → puerto abierto, si recibe RST → puerto cerrado. No completa la conexión (half-open scan). 

- **-sT: TCP Connect() Scan**  
  Completa la conexión TCP con el sistema objetivo. Menos sigiloso porque queda registrado en logs, pero no requiere privilegios de root.  

- **-sA: ACK Scan**  
  Envía paquetes ACK para mapear reglas de firewall y distinguir si un puerto está filtrado o no. No determina si un puerto está abierto o cerrado.  

- **-sW: Window Scan**  
  Variante del ACK Scan que analiza el tamaño de la ventana TCP en la respuesta para inferir el estado del puerto.  

- **-sM: Maimon Scan**  
  Escaneo menos común que explota un comportamiento descrito por Uriel Maimon en ciertos sistemas TCP.  

- **-sU: UDP Scan**  
  Escanea puertos UDP. Más lento que TCP porque muchos servicios no responden fácilmente, requiriendo retransmisiones.  

- **-sN: Null Scan**  
  Envía paquetes TCP sin flags. Un puerto abierto no debería responder; uno cerrado suele devolver un RST.  

- **-sF: FIN Scan**  
  Envía un paquete con el flag FIN. Los puertos cerrados responden con RST, los abiertos no responden.  

- **-sX: Xmas Scan**  
  Envía un paquete con los flags FIN, PSH y URG encendidos (como un "árbol de navidad"). Similar al Null y FIN Scan para detectar puertos abiertos/cerrados.  

## 2.3 🙌 Comandos básicos

![[Pasted image 20250907155921.png]]
````markdown
# 📌 Comandos básicos de Nmap

### 🔹 Opción `-v / -vv`
- **Descripción:** Muestra información detallada (verbose) del escaneo.  
- **Ejemplo:**
```bash
nmap [IP] -v
nmap [IP] -vv
````

### 🔹 Opción `-sV`

- **Descripción:** Detecta el servicio y la **versión** que se ejecuta en el puerto.
    
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

---




---
# aa


