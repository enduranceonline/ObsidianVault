#apuntes #HTB

---

```markdown
# HTB Starting Point - Redeemer 🗄️

## 1. Reconocimiento de la máquina
- Escaneo con `nmap`:
  ```bash
  nmap -sV -Pn <IP>
```

- Resultado:
    
    - Puerto **6379/tcp** abierto.
        
    - Servicio: **Redis** (REmote DIctionary Server).
        

---

## 2. ¿Qué es Redis?

- Redis es una **base de datos en memoria** (_In-memory Database_).
    
- Almacena datos en **RAM** → altísima velocidad de acceso.
    
- Soporta persistencia en disco para backup.
    
- Uso habitual: cacheo de datos, colas, almacenamiento de sesiones, pub/sub, ranking en tiempo real.
    

---

## 3. Herramientas necesarias

- Cliente oficial:
    
    ```
    redis-cli
    ```
    
- Instalación en Debian/Ubuntu:
    
    ```bash
    sudo apt install redis-tools
    ```
    

---

## 4. Conexión al servidor Redis

- Sintaxis general:
    
    ```bash
    redis-cli -h <IP_objetivo>
    ```
    
- Flag **-h**: se usa para indicar el hostname o la dirección del servidor.
    

---

## 5. Comandos básicos en Redis

- Obtener información y estadísticas del servidor:
    
    ```bash
    info
    ```
    
- Seleccionar la base de datos deseada (por índice):
    
    ```bash
    select <n>
    ```
    
    > Por defecto Redis tiene 16 bases numeradas de 0 a 15.
    
- Ver cuántas claves hay en cada base de datos (Keyspace):
    
    ```
    db0:keys=4,expires=0,avg_ttl=0
    ```
    
    → Aquí **db0** (índice 0) contiene **4 claves**.
    
- Listar todas las claves:
    
    ```bash
    keys *
    ```
    
- Obtener el valor de una clave:
    
    ```bash
    get <clave>
    ```
    

---

## 6. Resolviendo las tareas

1. **Which TCP port is open on the machine?**  
    → `6379`
    
2. **Which service is running on the port that is open on the machine?**  
    → `Redis`
    
3. **What type of database is Redis?**  
    → `In-memory Database`
    
4. **Which command-line utility is used to interact with the Redis server?**  
    → `redis-cli`
    
5. **Which flag is used with the Redis command-line utility to specify the hostname?**  
    → `-h`
    
6. **Once connected to a Redis server, which command is used to obtain the information and statistics about the Redis server?**  
    → `info`
    
7. **What is the version of the Redis server being used on the target machine?**  
    → `5.0.7`
    
8. **Which command is used to select the desired database in Redis?**  
    → `select`
    
9. **How many keys are present inside the database with index 0?**  
    → `4`
    
10. **Which command is used to obtain all the keys in a database?**  
    → `keys *`
    

---

## 7. Flag

- Una vez listadas las claves y accediendo con `get <clave>`, se obtiene la flag.
    
- Flag:
    
    ```
    ********************************
    ```
    

---

## 📌 Conclusiones

- Redis expone datos sensibles si no está protegido con autenticación.
    
- El uso de `redis-cli` y comandos básicos (`info`, `keys *`, `get`) permite enumerar y extraer información sin necesidad de exploits.
    
- La máquina enseña conceptos fundamentales sobre **enumeración de servicios y bases de datos en memoria**.
