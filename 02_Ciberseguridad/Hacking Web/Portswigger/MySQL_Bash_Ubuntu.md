# 🐬 MySQL - Comandos y Ejemplos Avanzados desde Bash (Ubuntu - VMware)

#labs #mysql #linux

Este documento contiene una guía detallada sobre cómo operar con bases de datos MySQL desde la terminal de Linux (Ubuntu), ideal para practicar en entornos como máquinas virtuales (VMware) y prepararse para laboratorios como los de PortSwigger.

---

## 🔐 Conexión a MySQL

```bash
sudo mysql -u root -p
```

- `-u root`: Especifica el usuario, en este caso `root`.
- `-p`: Solicita que ingreses la contraseña.

---

## 📂 Comandos básicos en MySQL

```sql
SHOW DATABASES;
```
Muestra todas las bases de datos disponibles.

```sql
CREATE DATABASE nombre_base;
```
Crea una nueva base de datos.

```sql
USE nombre_base;
```
Selecciona la base de datos con la que vamos a trabajar.

```sql
SHOW TABLES;
```
Muestra las tablas existentes en la base de datos actual.

```sql
DESCRIBE nombre_tabla;
```
Muestra la estructura de la tabla: columnas, tipos de datos, claves, etc.

---

## 🏗️ Crear Tablas

```sql
CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    contraseña VARCHAR(100) NOT NULL,
    rol ENUM('Admin', 'Cliente') DEFAULT 'Cliente'
);
```
- `AUTO_INCREMENT`: Incrementa automáticamente el ID.
- `PRIMARY KEY`: Define la clave principal.
- `ENUM`: Limita los valores posibles para el campo `rol`.

---

## ➕ Insertar Datos

```sql
INSERT INTO Usuarios (usuario, contraseña, rol)
VALUES ('juan', '1234', 'Cliente');
```
Inserta un nuevo registro en la tabla.

```sql
INSERT INTO Usuarios (usuario, contraseña)
VALUES ('test', 'test');
```
Si no especificas el campo `rol`, tomará el valor por defecto (`Cliente`).

---

## 🔍 Consultas SELECT

```sql
SELECT * FROM Usuarios;
```
Muestra todos los registros y columnas.

```sql
SELECT usuario, rol FROM Usuarios WHERE rol = 'Admin';
```
Filtra solo los usuarios con rol `Admin`.

```sql
SELECT * FROM Usuarios ORDER BY usuario ASC;
```
Ordena alfabéticamente por el campo `usuario`.

```sql
SELECT * FROM Usuarios LIMIT 3;
```
Devuelve solo los primeros 3 registros.

```sql
SELECT COUNT(*) FROM Usuarios WHERE rol = 'Cliente';
```
Cuenta cuántos usuarios son `Cliente`.

---

## 📝 Modificar Datos (UPDATE)

```sql
UPDATE Usuarios SET contraseña = 'nueva123' WHERE usuario = 'juan';
```
Actualiza la contraseña de un usuario específico.

```sql
UPDATE Usuarios SET rol = 'Admin' WHERE id = 5;
```
Cambia el rol del usuario con ID 5 a `Admin`.

---

## ❌ Eliminar Datos (DELETE)

```sql
DELETE FROM Usuarios WHERE usuario = 'test';
```
Elimina el usuario llamado `test`.

```sql
DELETE FROM Usuarios WHERE rol = 'Cliente';
```
Elimina todos los usuarios con rol `Cliente`.

---

## 🔁 JOIN entre Tablas

```sql
CREATE TABLE Pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    producto VARCHAR(100),
    cantidad INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id)
);

SELECT u.usuario, p.producto, p.cantidad
FROM Pedidos p
JOIN Usuarios u ON p.id_usuario = u.id;
```
Muestra los pedidos con el nombre del usuario que los realizó.

---

## ⚙️ Alterar Tablas Existentes

```sql
ALTER TABLE Usuarios ADD email VARCHAR(100);
```
Agrega una nueva columna.

```sql
ALTER TABLE Usuarios DROP COLUMN email;
```
Elimina la columna `email`.

```sql
ALTER TABLE Usuarios MODIFY usuario VARCHAR(100);
```
Modifica el tipo de dato o longitud de una columna.

---

## 🧼 Eliminar y Vaciar Tablas

```sql
DROP TABLE Pedidos;
```
Elimina completamente la tabla `Pedidos`.

```sql
TRUNCATE TABLE Usuarios;
```
Vacía la tabla eliminando todos sus registros, pero mantiene su estructura.

---

## 📌 Índices y Restricciones

```sql
CREATE UNIQUE INDEX idx_usuario ON Usuarios(usuario);
```
Crea un índice único para evitar que se repita el campo `usuario`.

```sql
ALTER TABLE Usuarios ADD UNIQUE (usuario);
```
Otra forma de aplicar una restricción única directamente desde la tabla.

---

## 🧪 Ejercicios para practicar

1. Crea una base de datos llamada `SeguridadDB`.
2. Dentro de ella, crea las tablas `Usuarios`, `Productos` y `Pedidos`.
3. Inserta al menos 5 usuarios con roles diferentes.
4. Inserta productos con nombre, precio y stock.
5. Registra pedidos hechos por distintos usuarios.
6. Muestra todos los pedidos con JOIN para saber quién los hizo.
7. Cuenta cuántos pedidos hizo cada usuario (`GROUP BY`).
8. Busca productos que contengan la palabra 'USB' (`LIKE '%USB%'`).
9. Actualiza el stock de un producto tras una compra.
10. Elimina usuarios que no han hecho ningún pedido (consulta avanzada).

---

## 🧠 Consejos finales

- Termina cada sentencia SQL con `;`.
- Puedes repetir comandos previos con las flechas ↑ ↓.
- Usa `\c` para cancelar una sentencia a medio escribir.
- Reinicia el servicio MySQL si es necesario:
```bash
sudo service mysql start
```

---

