---
tags: [linux, practice, semana1]
source: Mini-reto sandbox previo a Bandit — Semana 1
---

# Linux - Mini-reto: Práctica de Comandos Básicos

Ejercicio de sandbox local completado antes de empezar OverTheWire Bandit. Objetivo: demostrar que se pueden ejecutar los comandos de [[Linux - Command Line Reference]] sin consultar notas.

## Enunciado (resumen)

1. Crea una carpeta `practica` con tres subcarpetas: `docs`, `scripts`, `logs`.
2. Crea un archivo vacío en `docs` y otro en `scripts`. En `logs`, crea un archivo con texto.
3. Copia el archivo de `docs` con otro nombre. Renombra el de `scripts` añadiendo `_v1`.
4. Quítale permisos de ejecución al script. Verifica que falla. Luego dáselos y verifica que se ejecuta.
5. Busca, dentro de `practica/`, cualquier archivo `.log`.
6. Comprime toda la carpeta. Verifica el contenido sin extraer.
7. Lanza un proceso en segundo plano, confirma que corre, mátalo.
8. Limpieza: borra todo lo creado.

## Resolución (comandos clave)

```bash
mkdir -p practica/{docs,scripts,logs}
touch practica/docs/nota1.txt practica/scripts/deploy.sh
echo "arranque ok" > practica/logs/test.log

cp practica/docs/nota1.txt practica/docs/nota1_backup.txt
mv practica/scripts/deploy.sh practica/scripts/deploy_v1.sh

chmod 600 practica/scripts/deploy_v1.sh
./practica/scripts/deploy_v1.sh    # → Permission denied
chmod 755 practica/scripts/deploy_v1.sh
./practica/scripts/deploy_v1.sh    # → ejecuta sin error

find practica/ -type f -name "*.log"

tar -czvf practica.tar.gz practica/
tar -tvf practica.tar.gz           # lista sin extraer

sleep 100 &
jobs
ps aux | grep sleep
kill %1
jobs                               # ya no aparece

rm -r practica/ practica.tar.gz
```

## ⚡ Puntos de fricción

**Rutas relativas — error más recurrente**
El fallo más repetido: escribir el nombre de la carpeta donde ya se está parado. Si el prompt dice `~/Documentos/practica` y escribes `practica/docs/...`, el shell busca una subcarpeta `practica` *dentro* de `practica` — que no existe.

Regla para fijar: antes de escribir cualquier ruta, `pwd` primero. La ruta empieza *desde donde estás*, no desde donde quieres llegar.

**`..` ya ES la carpeta padre — no se nombra otra vez**
`../scripts/` desde dentro de `docs/` lleva a `practica/scripts/`. Escribir `../practica/scripts/` busca una carpeta `practica` *dentro de* `practica` — otra vez el mismo error en otra forma.

**`/ruta` vs `./ruta` vs `ruta`**
- `/algo` — ruta absoluta desde la raíz del disco. `/practica` busca en la raíz del sistema.
- `./algo` — relativa desde aquí: la carpeta `algo` que hay justo donde estás.
- `.algo` (sin barra) — archivo o carpeta *oculto* llamado literalmente ".algo". No es lo mismo que `./algo`.

**`find` necesita un punto de partida que exista desde donde estás**
`find practica/` desde dentro de `practica/` falla porque no hay una subcarpeta llamada `practica` ahí dentro. La forma correcta es `find ./` o `find .` para buscar en el directorio actual.

**`./script` vs `. script`**
`./script` lo ejecuta como proceso hijo independiente — lo que normalmente quieres.
`. script` (o `source script`) lo ejecuta dentro de tu sesión actual — solo para config files como `~/.bashrc`.

**`ps aux | grep nombre`**
El propio `grep` aparece en los resultados porque está corriendo mientras `ps` captura. No es un error, es comportamiento esperado.

**`killall nombre`**
Cuando un proceso tiene múltiples hijos (Spotify, Brave...), `kill PID` solo mata uno. `killall spotify` mata todos los procesos con ese nombre de una vez.

**`tree -L 1`** — el argumento de `-L` es un número (nivel de profundidad), no el nombre de una carpeta.
