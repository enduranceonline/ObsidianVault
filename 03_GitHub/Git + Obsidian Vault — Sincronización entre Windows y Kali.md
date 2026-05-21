## 📌 Objetivo

Mantener el mismo vault de Obsidian sincronizado entre:

- PC Windows
- Laptop Kali/Linux
- Repositorio remoto en GitHub

La regla principal es:

> Antes de editar: `git pull`  
> Después de editar: `git add -A` + `git commit` + `git push`

---

# 1️⃣ Rutas del vault

## Windows

```bash
cd ~/Documents/Documents_03_ESTUDIOS/Obsidian/ObsidianVault
````

Ruta equivalente en explorador:

```text
C:\Users\David\Documents\Documents_03_ESTUDIOS\Obsidian\ObsidianVault
```

## Kali / Linux

```bash
cd /home/endurance/Documentos/ObsidianVault
```

---

# 2️⃣ Flujo seguro antes de trabajar

Antes de abrir Obsidian o modificar notas desde cualquier equipo:

```bash
git pull origin main
git status
```

Si todo está correcto, debería aparecer:

```text
nothing to commit, working tree clean
```

Esto significa que el vault está limpio y actualizado.

---

# 3️⃣ Flujo seguro después de trabajar

Después de modificar notas en Obsidian:

```bash
git status
git add -A
git commit -m "Actualiza vault desde Windows"
git push origin main
```

O si estás en Kali:

```bash
git status
git add -A
git commit -m "Actualiza vault desde Kali"
git push origin main
```

---

# 4️⃣ Flujo completo en Windows

```bash
cd ~/Documents/Documents_03_ESTUDIOS/Obsidian/ObsidianVault
git pull origin main
git status
```

Trabajar en Obsidian.

```bash
git status
git add -A
git commit -m "Actualiza vault desde Windows"
git push origin main
```

---

# 5️⃣ Flujo completo en Kali

```bash
cd /home/endurance/Documentos/ObsidianVault
git pull origin main
git status
```

Trabajar en Obsidian.

```bash
git status
git add -A
git commit -m "Actualiza vault desde Kali"
git push origin main
```

---

# 6️⃣ Regla de oro

## Correcto

```text
Windows:
pull → editar → add → commit → push

Kali:
pull → editar → add → commit → push
```

## Incorrecto

```text
Windows edita sin hacer push
Kali edita sin hacer pull
Windows hace push
Kali intenta hacer push
```

Esto suele generar conflictos.

Git no es Dropbox. Git es más bien un notario con mala leche: si no le avisas bien, te monta expediente.

---

# 7️⃣ Comandos útiles

## Ver estado general

```bash
git status
```

## Ver estado resumido

```bash
git status --short
```

## Ver archivos modificados

```bash
git diff --name-only
```

## Ver cambios concretos en texto

```bash
git diff
```

## Traer cambios desde GitHub

```bash
git pull origin main
```

## Añadir todos los cambios

```bash
git add -A
```

`git add -A` registra:

- archivos nuevos
    
- archivos modificados
    
- archivos eliminados
    
- archivos movidos
    

Es el más adecuado para Obsidian.

## Crear commit

```bash
git commit -m "Actualiza apuntes de Obsidian"
```

## Subir cambios a GitHub

```bash
git push origin main
```

---

# 8️⃣ Mensajes de commit recomendados

## Genéricos

```bash
git commit -m "Actualiza vault de Obsidian"
```

```bash
git commit -m "Actualiza apuntes de Obsidian"
```

## Por equipo

```bash
git commit -m "Actualiza vault desde Windows"
```

```bash
git commit -m "Actualiza vault desde Kali"
```

## Por contenido

```bash
git commit -m "Actualiza apuntes del proyecto SIEM"
```

```bash
git commit -m "Reorganiza estructura del vault"
```

```bash
git commit -m "Añade notas de Git y Obsidian"
```

---

# 9️⃣ Qué hacer si aparece “nothing to commit”

Si al hacer commit aparece:

```text
nothing to commit, working tree clean
```

No pasa nada. Significa que no hay cambios pendientes.

No hace falta hacer push si no has creado ningún commit nuevo.

---

# 🔟 Qué hacer si Git dice que hay cambios

Si ejecutas:

```bash
git status
```

Y aparecen archivos modificados:

```text
modified:
```

o archivos nuevos:

```text
untracked files:
```

Entonces, si esos cambios son correctos:

```bash
git add -A
git commit -m "Actualiza vault de Obsidian"
git push origin main
```

---

# 1️⃣1️⃣ Qué hacer si Git dice que hay archivos eliminados

Si aparecen líneas como:

```text
deleted:
```

Puede significar dos cosas:

1. Has borrado notas.
    
2. Has reorganizado carpetas en Obsidian.
    

Si la reorganización es intencionada:

```bash
git add -A
git commit -m "Reorganiza vault de Obsidian"
git push origin main
```

Si no querías borrar esos archivos:

```bash
git restore .
```

Cuidado: `git restore .` deshace cambios locales no guardados.

---

# 1️⃣2️⃣ Qué hacer si hay conflicto

Si al hacer `git pull` aparece un conflicto, no hacer commit a ciegas.

Primero ver:

```bash
git status
```

Git marcará archivos en conflicto.

Abrir los archivos afectados en VS Code u Obsidian y buscar marcas como:

```text
<<<<<<< HEAD
contenido local
=======
contenido remoto
>>>>>>> origin/main
```

Hay que elegir qué contenido conservar, borrar las marcas y después:

```bash
git add -A
git commit -m "Resuelve conflicto de sincronización"
git push origin main
```

---

# 1️⃣3️⃣ Comando para comprobar configuración importante en Windows

En Windows se activaron rutas largas para evitar errores tipo `Filename too long`.

Comprobar:

```bash
git config --global core.longpaths
```

Debe devolver:

```text
true
```

Si no aparece `true`:

```bash
git config --global core.longpaths true
```

---

# 1️⃣4️⃣ Errores comunes

## Error: Filename too long

Solución:

```bash
git config --global core.longpaths true
```

Después, si el clonado quedó mal, borrar la carpeta y clonar de nuevo.

## Error: command not found

Ejemplo:

```text
bash: gittt: command not found
```

Normalmente es porque se ha escrito mal el comando.

Correcto:

```bash
git status
```

## Error: repo sucio antes de cambiar de equipo

Antes de cambiar de Windows a Kali, o de Kali a Windows, dejar siempre el repo limpio:

```bash
git status
```

Idealmente:

```text
nothing to commit, working tree clean
```

---

# 1️⃣5️⃣ Checklist rápida antes de cerrar sesión

Antes de apagar el PC o cambiar de equipo:

```bash
git status
```

Si hay cambios:

```bash
git add -A
git commit -m "Actualiza vault de Obsidian"
git push origin main
```

Después comprobar:

```bash
git status
```

Resultado ideal:

```text
nothing to commit, working tree clean
```

---

# 1️⃣6️⃣ Checklist rápida al empezar

Al empezar en cualquier equipo:

```bash
cd RUTA_DEL_VAULT
git pull origin main
git status
```

Donde `RUTA_DEL_VAULT` es:

## Windows

```bash
cd ~/Documents/Documents_03_ESTUDIOS/Obsidian/ObsidianVault
```

## Kali

```bash
cd /home/endurance/Documentos/ObsidianVault
```

---

# 1️⃣7️⃣ Resumen ultra corto

```bash
git pull origin main
```

Editar en Obsidian.

```bash
git add -A
git commit -m "Actualiza vault de Obsidian"
git push origin main
```

---

# 1️⃣8️⃣ Regla final

No abrir y editar el vault en dos equipos a la vez.

Antes de editar en un equipo, siempre traer lo último de GitHub.

Después de editar en un equipo, siempre subirlo a GitHub.

```text
Pull antes.
Push después.
Paz mental.
```