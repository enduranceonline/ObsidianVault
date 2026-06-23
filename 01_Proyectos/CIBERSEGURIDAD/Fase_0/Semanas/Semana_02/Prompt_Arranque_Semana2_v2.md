# Prompt de arranque — Chat Semana 2

Pega esto al inicio del nuevo chat:

---

Estoy en **Fase 0 de un roadmap de ciberseguridad** (3 meses pre-grado VIU, 8-10h/semana). Acabamos de cerrar la Semana 1 y empezamos la Semana 2, que tiene solo 2 mañanas de estudio disponibles.

## Estado actual del vault (Obsidian)

### Estructura
```
01_Proyectos/CIBERSEGURIDAD/
└── Fase_0/
    ├── Fase_0 - Dashboard.md
    └── Semanas/
        ├── Semana_01.md   (cerrada)
        └── Semana_02.md   (activa)

02_Ciberseguridad/
├── _MOCs/
│   ├── MOC - Redes.md
│   └── MOC - Sistemas Operativos.md
├── Bases_Ciberseguridad/
│   ├── Redes/
│   │   ├── Cisco - Modelo OSI.md          (vacía — pendiente)
│   │   ├── Cisco - Subnetting básico.md   (vacía — pendiente)
│   │   └── Cisco - Bandwidth and Data Transmission.md
│   └── Sistemas Operativos/Linux/
│       ├── Linux - Architecture.md
│       ├── Linux - Command Line Reference.md
│       ├── Linux - Distributions.md
│       ├── Linux - Filesystem Hierarchy.md
│       ├── Linux - Logical Operators and Test Conditions.md
│       ├── Linux - Permissions & Process Management.md
│       ├── Linux - Argument Parsing and Special Filenames.md
│       ├── Linux - File Type Detection.md
│       ├── Linux - find Command.md
│       └── Linux - Mini-reto Practica Basica.md
├── Kasiu_Dominios/
│   └── Dominio_1_Fundamentos_Ciberseguridad.md  (vacía — pendiente Semana 2)
├── Certificaciones/  (Network+, eJPT — material anterior al roadmap)
├── Pentesting/       (HTB, PortSwigger — material anterior al roadmap)
└── WarGames/BanditOverTheWire/
    └── Levels/
        ├── Bandit - Level 00.md
        ├── Bandit - Level 01.md
        ├── Bandit - Level 02.md
        ├── Bandit - Level 03.md
        ├── Bandit - Level 04.md
        └── Bandit - Level 05.md
```

### Convenciones del vault
- Notas técnicas en **inglés**. Notas de proceso (semanales, dashboard) en **español**.
- Notas atómicas por concepto, no por recurso. `Cisco - Modelo OSI` y `Cisco - Subnetting básico` están vacías — son placeholders para cuando se genere contenido real.
- Las notas de Bandit siguen el formato: Objetivo → Conexión → Conceptos → Solución → Fricciones → Next, con navegación `◀ Level N · Level N+2 ▶`.
- Cuando un nivel de Bandit genera un concepto nuevo con suficiente peso, se crea una nota técnica separada en `Linux/` y la nota del nivel enlaza a ella. Ejemplos: `Linux - Argument Parsing and Special Filenames.md` (generada por Nivel 1+2), `Linux - File Type Detection.md` (Nivel 4), `Linux - find Command.md` (Nivel 5).

## Decisiones importantes ya tomadas
- **Cisco Networking Essentials** descartado (solo instructor-led). Sustituido por **Networking Basics** (NetAcad, 22h, self-paced gratuito) + **Subnetting Mastery** (NetAcad, beta, 4h).
- **Mes 2**: Endpoint Security (NetAcad, 27h, 31 labs) sustituye a TryHackMe Pre Security como prioridad de profundización (cubre Dominio 2 y 3 de Kasiu con práctica real).
- **TickTick simplificado**: una tarea = un bloque de trabajo con etiquetas de tiempo/contexto (`[50min] [teoria] [diaLibre]`). Sin subtareas. El detalle vive en Obsidian.
- **Tags TickTick activos**: `50min`, `25min`, `pomodoro`, `teoria`, `practica`, `diaLibre`, `diaTrabajo`, `microtarea`.
- Regla anti-sobredocumentación: sin recurso teórico nuevo si el hito práctico de la semana anterior no se cerró. El hito de Semana 1 (Bandit 0-5) **sí se cerró** → Semana 2 desbloqueada.

## Resumen Semana 1 (cerrada)
**Completado:**
- Linux Journey — módulo Command Line ✅
- Networking Basics — Knowledge Check + Módulo 1 ✅
- Cisco Packet Tracer instalado (extra no planificado) ✅
- Mini-reto de práctica de comandos bash ✅
- Bandit OverTheWire niveles 0-5 ✅ — con 5 notas técnicas nuevas generadas

**No completado (arrastrado):**
- Kasiu — lectura panorámica (aplazado por 3ª vez: Semana 3 si no se hace en Semana 2)
- Subnetting Mastery (aplazado)
- Bandit 6-15 (en progreso)

**Lección retro**: semana con 12h de turnos de trabajo no equivale a 8-10h de estudio disponibles. Calibrar objetivos según días libres reales antes de comprometerse en TickTick.

## Semana 2 (activa) — solo 2 mañanas disponibles
**Prioridad 1** → Kasiu: índice completo + Dominio 1 panorámico `[50min] [teoria]`
**Prioridad 2** → Networking Basics: Módulo 2 `[50min] [teoria]`
**Aplazado explícitamente** → Bandit (continuar nivel 6) y Subnetting Mastery

La nota `Semana_02.md` ya está creada en el vault.

## Hitos de Mes 1 para referencia
- [ ] Networking Basics completado — ~15% hecho
- [ ] Subnetting Mastery completado — 0%
- [x] Linux Journey completado — 100%
- [ ] Bandit hasta nivel 15 — nivel 5 alcanzado (33%)
- [ ] Kasiu — lectura panorámica completa (11 dominios) — 0%

## Porcentaje Mes 1 estimado
~28-30% completado con ~16% del tiempo de mes transcurrido — ritmo global correcto, pero Kasiu y Subnetting están a cero y necesitan atención específica.

## Lo que necesito ahora
Continuar el trabajo de Semana 2: cuando traiga contenido (quizzes de Networking Basics, terminal de Bandit, fragmentos de Kasiu), generar notas atómicas en inglés siguiendo el mismo sistema que en Semana 1.

## Gestión de notas del vault en este chat
Las notas del vault (Obsidian) no están subidas al proyecto — viven en local. Si en algún momento necesitas leer o modificar una nota existente para continuar el trabajo, pídeme que la pegue en el chat. Las notas más probables que vayas a necesitar en Semana 2:
- `Semana_02.md` — para actualizarla con el progreso real
- `Fase_0 - Dashboard.md` — para marcar hitos completados
- `Bandit - Level 05.md` — punto de partida para el siguiente nivel
- Cualquier nota técnica de Linux si hay que ampliarla con contenido nuevo
- `MOC - Sistemas Operativos.md` y `MOC - Redes.md` — si se crean notas nuevas que enlazar

No intentes reconstruir el contenido de estas notas desde cero — pídeme el archivo y lo pego directamente.
