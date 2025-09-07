#apuntes #certificacion #eJPT

![[Pasted image 20250907104756.png]]

METODOLOGIA DE MAQUINAS EN eJPT
Cuando nos enfrentamos a una maquina lo que tenemos es una IP objetivo. Sobre esa IP objetivo lo que vamos a necesitar conseguir son 2 flags.

1. Cuando conseguimos acceso a la maquina es la primera flag.
**Reverse shell**: Cuando conseguimos tener una consola de comandos ejecutándose en nuestra maquina, pero en realidad estamos dentro de la maquina objetivo. Aun estando en nuestro equipo, si le preguntamos que IP somos nos dirá la del objetivo atacado.

2. Elevar Privilegios para obtener la segunda flag.

---
# 🗂 Índice

1. Recolección de información
   - Escaneo nmap
   - Servicios HTTP
   - Servicios SMB
   - FTP
2. Explotación - Acceso a la máquina
   - Vulnerabilidades
   - Reverse Shell
3. Enumeración interna
   - Usuarios
   - Flags
   - Passwords
   - Hotfixes
   - Redes
4. Pivoting
   - Rangos de red
   - Metasploit

---
## Recolección de información

---
### Escaneo con nmap

````markdown
- Puertos abiertos  
- Servicios y versiones  
- Preguntas examen 5-7  

**Comandos útiles:**

nmap -sS -sV -p- <IP>
nmap -A <IP>
````



---

### Servicios HTTP

- Identificar:
    
    - Versiones
        
    - Plugins
        
    - Usuarios
        
    - Temas
        
- CMS (WordPress, Drupal)
    
- Herramientas:
    
    - `wpscan`
        
    - `droopescan`
        
    - `drupageddon`
        
    - `hydra`
        
- Fuerza bruta directorios → `dirb`, diccionario: `/usr/share/dirb/wordlists/common.txt`
    
- Revisar código fuente
    

**Preguntas examen:** 7-10

---

### Servicios SMB

- Versiones y usuarios
    
- Tools:
    
    - `enum4linux`
        
    - `smbclient`
        
    - `smbmap`
        

**Preguntas examen:** 1-2

---

### FTP

- Comprobar login **anonymous**
    

---

## 💥 Explotación - Acceso a la máquina

### Vulnerabilidades

- Recursos:
    
    - `searchsploit`
        
    - [exploit-db](https://www.exploit-db.com/)
        
- Lenguajes:
    
    - PHP
        
    - PowerShell
        

---

### Reverse Shell

- Opciones:
    
    - Bash
        
    - PHP
        
    - PowerShell
        
- Web útil: [revshells.com](https://www.revshells.com/)
    

---

## 🕵️ Enumeración interna

### Usuarios

- **Preguntas examen:** 1-2
    

### Flags

- Archivo: `flag.txt`
    
- Dinámicas
    
- **Preguntas examen:** 2-3
    

### Passwords

- Técnicas: Fuerza bruta
    
- Herramientas:
    
    - `hydra`
        
    - `metasploit`
        
- Diccionario: `rockyou.txt`
    
- **Preguntas examen:** 2-4
    

### Hotfixes

- Comandos:
    
    ```bash
    Get-Hotfix
    wmic qfe list full /format:list > hotfixes.txt
    systeminfo
    ```
    
- **Preguntas examen:** 0-1
    

### Redes

- Comandos:
    
    ```bash
    ifconfig
    ipconfig
    ```
    
- Obtener **rangos de red**
    

---

## 🔄 Pivoting

### Relación con redes internas

- Identificar rangos de red con `ifconfig` / `ipconfig`
    

### Metasploit

- Módulos útiles:
    
    - `post/multi/manage/autoroute`
        
    - `post/windows/gather/arp_scanner`
        
    - `post/windows/manage/portproxy`
        
    - `use auxiliary/scanner/portscan/tcp`
        
- Ejemplo:
    
    ```bash
    db_nmap -sS -sV -p 1234 localhost
    ```
    
- **Preguntas examen:** 1-4
    

---
