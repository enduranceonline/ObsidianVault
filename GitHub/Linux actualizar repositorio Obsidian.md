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

28.10.2025
# Cambios realizados 

- Unificación de ramas: `backup/2025-09-16` → `main` (rename y push forzado).
    
- Eliminación de rama antigua en remoto.
    
- Repositorio cambiado a **público**.
    
- Protección de rama `main`:
    
    - Block force pushes.
        
    - Restrict deletions.
        
    - (Sin PR obligatorio para mantener push directo).
        
- Commits **firmados por SSH**:
    
    - `gpg.format=ssh`
        
    - `user.signingkey=~/.ssh/id_ed25519.pub`
        
    - `commit.gpgsign=true`
        
    - `gpg.ssh.allowedSignersFile=~/.config/git/allowed_signers`
        
- Upstream corregido: `main` → `origin/main`.
    
- Limpieza de archivo de prueba `.gitkeep`.

# Configuración global aplicada (una sola vez)

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git config --global pull.rebase true
git config --global rebase.autoStash true
git config --global push.autoSetupRemote true
mkdir -p ~/.config/git
echo "$(git config user.email) $(cat ~/.ssh/id_ed25519.pub)" > ~/.config/git/allowed_signers
git config --global gpg.ssh.allowedSignersFile ~/.config/git/allowed_signers
```

# Flujo de trabajo desde ahora

```bash
# 1) Iniciar sesión SSH (cada nueva terminal)
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519

# 2) Trabajo diario en main
git status
git add -A
git commit -m "mensaje"      # firmado automáticamente (SSH)
git pull --rebase
git push
```

DUDAS:

1️⃣ **`git add -A` vs `git add .`**

- `git add .` añade archivos nuevos y modificados, **pero no detecta eliminaciones** (archivos borrados no se reflejan).
    
- `git add -A` añade **todo**: nuevos, modificados y eliminados.  
    Por eso se usa `-A` en flujos completos o de sincronización. Es más seguro y coherente.

2️⃣ **La línea `# firmado automáticamente (SSH)`**  
No es un comando. Es solo un comentario informativo.  

El commit se firma **en el momento de ejecutar `git commit -m "mensaje"`**, gracias a la configuración:

```bash
git config --global commit.gpgsign true
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
```

Así, cada commit se firma automáticamente al crearlo, sin pasos extra.  
Luego simplemente haces `git pull --rebase` y `git push` como siempre.
# Verificación rápida

- Local:
    
```bash
git log --show-signature -1    # Debe mostrar: Good "git" signature ...
```
    
- GitHub: el commit debe salir **Verified**.

# Si ves rechazo por “signed commits”

- Asegura agente y clave:
    
```bash
ssh-add -l                     # Debe listar id_ed25519
```
    
- Re-firma el último commit:
    
```bash
git commit --amend -S --no-edit
git push --force-with-lease
```

# Notas operativas

- Las reglas de rama evitan borrado y force push en `main`. El push normal sigue permitido.
    
- Si cambias de equipo o clave, repite la sección de **configuración global**.


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