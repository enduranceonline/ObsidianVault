ssh -vT git@github.com
eval "$(ssh-agent -s)" ssh-add ~/.ssh/id_ed25519
git pull --rebase     # por si hay cambios en remoto
git add -A
git commit -m "Actualiza notas"
git push

 🚀. **cheatsheet** clara y separada en dos bloques: **Windows (Git Bash/PowerShell)** y **Linux (bash/zsh)**.
1. Arrancas el agente SSH.
2. Cargas tu clave privada (la que ya existe en `~/.ssh/id_ed25519`).
3. Compruebas conexión con GitHub.
4. Luego usas Obsidian con Git.

---

# 🔑 Cheatsheet Git + SSH para Obsidian

## 🟦 Windows (Git Bash o PowerShell)

```bash
# 1. Iniciar el agente SSH (solo si no está en marcha)
eval $(ssh-agent -s)

# 2. Añadir tu clave privada al agente si usas ed25519:
ssh-add ~/.ssh/id_ed25519

# 3. Ver claves cargadas
ssh-add -l

# 4. Comprobar conexión con GitHub
ssh -T git@github.com

# 5. Flujos Git habituales
git status
git fetch --all --prune
git pull origin main
git push origin main
```

📌 Nota: en Windows puede que necesites arrancar `ssh-agent` como servicio:

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
```

---

## 🟩 Linux (bash/zsh)

```bash
# 1. Iniciar el agente SSH (si no está activo)
eval $(ssh-agent -s)

# 2. Añadir tu clave privada si usas ed25519:
ssh-add ~/.ssh/id_ed25519

# 3. Ver claves cargadas
ssh-add -l

# 4. Probar conexión con GitHub
ssh -T git@github.com

# 5. Flujos Git habituales
git status
git fetch --all --prune
git pull origin main
git push origin main
```

---

✅ Con esto en ambos equipos:

1. Abres terminal.
2. Cargas la clave en el agente.
3. Pruebas conexión.
4. Ya puedes trabajar desde Obsidian con `git pull/push`.