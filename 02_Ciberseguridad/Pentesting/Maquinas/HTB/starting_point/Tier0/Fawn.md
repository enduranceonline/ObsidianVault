#apuntes #HTB

---

```markdown
# HTB Starting Point - Fawn 🐮

## 1. Reconocimiento de la máquina
- El servicio detectado es **FTP (File Transfer Protocol)**.  
- Escaneo con `nmap`:
  ```bash
  nmap -sV -Pn <IP>
```

- Resultado:
    
    - Puerto **21/tcp** abierto.
        
    - Servicio: **FTP vsftpd 3.0.3**.
        
    - Sistema operativo: **Unix/Linux**.
        

---

## 2. ¿Qué es FTP?

- **FTP (File Transfer Protocol)** → Protocolo usado para transferir archivos entre cliente y servidor.
    
- Funciona en **puerto 21** por defecto.
    
- El tráfico viaja en **texto plano**, sin cifrado → credenciales y archivos pueden ser interceptados.
    
- Alternativa segura: **SFTP (SSH File Transfer Protocol)**.
    

---

## 3. Herramientas útiles

- Cliente FTP incluido en la mayoría de sistemas:
    
    ```bash
    ftp <IP_objetivo>
    ```
    
- Para ver el menú de ayuda del cliente FTP:
    
    ```bash
    ftp -?
    ```
    

---

## 4. Acceso FTP

- FTP permite un login especial con el usuario:
    
    ```
    anonymous
    ```
    
- Esto permite acceder sin credenciales reales.
    
- Ejemplo:
    
    ```bash
    ftp <IP_objetivo>
    Name: anonymous
    Password: <cualquiera o vacío>
    ```
    
- Mensaje de login exitoso → código `230` (Login successful).
    

---

## 5. Comandos básicos de FTP

- Listar archivos:
    
    ```bash
    dir
    ls
    ```
    
- Descargar un archivo:
    
    ```bash
    get <archivo>
    ```
    

---

## 6. Resolviendo las tareas

1. **What does the 3-letter acronym FTP stand for?**  
    → `File Transfer Protocol`
    
2. **Which port does the FTP service listen on usually?**  
    → `21`
    
3. **FTP sends data in the clear... protocolo seguro basado en SSH**  
    → `SFTP`
    
4. **ICMP echo request para probar conexión**  
    → `ping`
    
5. **Versión de FTP en el target**  
    → `vsftpd 3.0.3`
    
6. **Tipo de sistema operativo**  
    → `Unix`
    
7. **Comando para mostrar ayuda del cliente FTP**  
    → `ftp -?`
    
8. **Usuario usado para login sin cuenta**  
    → `anonymous`
    
9. **Código de respuesta en 'Login successful'**  
    → `230`
    
10. **Comando alternativo a `dir` para listar archivos**  
    → `ls`
    
11. **Comando usado para descargar archivo**  
    → `get`
    

---

## 7. Flag

- Una vez dentro del FTP, con `ls` se encuentra el archivo `flag.txt`.
    
- Se descarga con:
    
    ```bash
    get flag.txt
    ```
    
- Flag:
    
    ```
    ********************************
    ```
    

---

## 📌 Conclusiones

- FTP en puerto 21 sin cifrado → vulnerable a sniffing.
    
- La configuración de **anonymous login** es un riesgo de seguridad si permite acceso a archivos sensibles.
    
- Este laboratorio enseña:
    
    - Reconocimiento básico con Nmap.
        
    - Uso de cliente FTP y sus comandos principales.
        
    - Identificación de configuraciones inseguras en servicios comunes.
        

```

---

👉 ¿Quieres que prepare también los apuntes en este formato para **todas las máquinas Tier 0** (Meow, Redeemer, Fawn, Dancing, etc.) para que tengas un pack completo en Obsidian?
```