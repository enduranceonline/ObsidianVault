#apuntes #HTB

---

```markdown
# HTB Starting Point - Dancing 💃

## 1. Reconocimiento de la máquina
- El protocolo identificado es **SMB (Server Message Block)**.
- Escaneo con `nmap`:
  ```bash
  nmap -sV -Pn <IP>
```

- Resultado:
    
    - Puerto **445/tcp** abierto.
        
    - Servicio: **microsoft-ds** (SMB).
        

---

## 2. ¿Qué es SMB?

- **SMB (Server Message Block)** es un protocolo de red que permite compartir **archivos, impresoras y otros recursos** entre equipos.
    
- Se usa principalmente en **sistemas Windows**.
    
- Los recursos compartidos se llaman **shares**.
    
- Acceso normalmente requiere **usuario y contraseña**, aunque a veces está mal configurado y permite acceso **anónimo o invitado**.
    

---

## 3. Herramientas útiles

- Cliente SMB:
    
    ```bash
    smbclient
    ```
    
- Para listar shares de un host:
    
    ```bash
    smbclient -L <IP_objetivo>
    ```
    
    - Flag **-L** → listar recursos compartidos disponibles en el servidor.
        

---

## 4. Shares en Dancing

- Enumeración de shares reveló **4 recursos**:
    
    - `ADMIN$`
        
    - `C$`
        
    - `IPC$`
        
    - `WorkShares`
        
- Los primeros tres son administrativos, pero el share **WorkShares** estaba mal configurado y accesible con **contraseña en blanco**.
    

---

## 5. Acceso a WorkShares

- Conexión:
    
    ```bash
    smbclient //<IP_objetivo>/WorkShares -U ""
    ```
    
    > Cuando pida contraseña, dejar en blanco.
    
- Dentro del SMB shell, comandos básicos:
    
    - `ls` → listar archivos
        
    - `cd <directorio>` → cambiar directorio
        
    - `get <archivo>` → descargar archivo
        
    - `exit` → salir
        

---

## 6. Resolviendo las tareas

1. **What does the 3-letter acronym SMB stand for?**  
    → `Server Message Block`
    
2. **What port does SMB use to operate at?**  
    → `445`
    
3. **What is the service name for port 445 that came up in our Nmap scan?**  
    → `microsoft-ds`
    
4. **Flag de smbclient para listar shares**  
    → `-L`
    
5. **How many shares are there on Dancing?**  
    → `4`
    
6. **Share accesible con contraseña en blanco**  
    → `WorkShares`
    
7. **Comando dentro de la shell SMB para descargar archivos**  
    → `get`
    

---

## 7. Flag

- Navegando en `WorkShares` → directorio `James.P` → archivo `flag.txt`.
    
- Descarga:
    
    ```bash
    get flag.txt
    ```
    
- Flag:
    
    ```
    ********************************
    ```
    

---

## 📌 Conclusiones

- SMB en el puerto 445 expuso un recurso compartido mal configurado.
    
- El uso de **smbclient** permitió acceder y extraer la flag sin credenciales válidas.
    
- Este laboratorio enseña:
    
    - Reconocimiento de servicios SMB.
        
    - Enumeración de shares.
        
    - Riesgos de configuraciones inseguras (anonymous/guest access).
        

```

---

👉 ¿Quieres que continúe con el mismo formato para **Archetype (Tier 2)** y siguientes máquinas de Starting Point, así lo dejas todo organizado para Obsidian?
```