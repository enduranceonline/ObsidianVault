
git pull --rebase     # por si hay cambios en remoto
git add -A
git commit -m "Actualiza notas"
git push

## 1) Prueba la conexión (modo verbose para diagnosticar)

`ssh -vT git@github.com`

- Si ves `Permission denied (publickey)` y líneas de `Offering public key: ...` sin éxito, sigue abajo.
    

---

## 2) ¿Tienes clave SSH?

`ls -la ~/.ssh`

Mira si existen `id_ed25519` y `id_ed25519.pub` (o `id_rsa`/`.pub`).

### Si **NO** tienes clave, créala:

`ssh-keygen -t ed25519 -C "tu_email_de_github" # Enter para ruta por defecto (~/.ssh/id_ed25519) # Pon passphrase si quieres`

---

## 3) Carga la clave en el agente

`eval "$(ssh-agent -s)" ssh-add ~/.ssh/id_ed25519`

> Si tu clave privada tiene otro nombre, ajusta la ruta.

---

## 4) Añade la **clave pública** a tu cuenta de GitHub

Copia y pega en GitHub → _Settings_ → _SSH and GPG keys_ → **New SSH key**:

`cat ~/.ssh/id_ed25519.pub`

Prueba de nuevo:

`ssh -T git@github.com # Esperado: "Hi enduranceonline! You've successfully authenticated..."`

---

## 5) Asegura permisos y fuerza el uso de esa clave

A veces SSH ignora claves por permisos o por tener varias. Arregla permisos y crea config mínima:

`chmod 700 ~/.ssh chmod 600 ~/.ssh/id_ed25519 chmod 644 ~/.ssh/id_ed25519.pub  cat > ~/.ssh/config << 'EOF' Host github.com   HostName github.com   User git   IdentityFile ~/.ssh/id_ed25519   IdentitiesOnly yes EOF chmod 600 ~/.ssh/config`

Vuelve a probar:

`ssh -T git@github.com`

---

## 6) Empuja

`git push`

---

### Opcionales útiles

**SSH por puerto 443 (si red bloquea el 22):**

`cat >> ~/.ssh/config << 'EOF'  Host github-443   HostName ssh.github.com   Port 443   User git   IdentityFile ~/.ssh/id_ed25519   IdentitiesOnly yes EOF  ssh -T github-443 # Si funciona, puedes apuntar el remoto a este host: git remote set-url origin github-443:enduranceonline/ObsidianVault.git`

**Usar HTTPS en vez de SSH:**

`git remote set-url origin https://github.com/enduranceonline/ObsidianVault.git git push # Con 2FA te pedirá un Personal Access Token como contraseña.`

---

Si quieres, pega aquí el resultado de:

`ssh -vT git@github.com`

(y ocultas cualquier dato sensible). Con eso te digo exactamente en qué paso está fallando (clave no encontrada, no cargada, permisos, etc.).