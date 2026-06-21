---
tags: [fase0, roadmap, proyecto]
inicio: 2026-06-17
fin_estimado: 2026-09-16
---

# Fase 0 — Anticipación (3 meses pre-grado)

**Duración:** 3 meses · 8-10h/semana
**Objetivo:** llegar al primer cuatrimestre del Grado VIU con base de redes y Linux funcionando, visión panorámica de los dominios de ciberseguridad, profundización iniciada en los dominios Cloud-relevantes, primer proyecto público en GitHub (homelab), y el patrón de sobredocumentación roto desde el día 1.

## ⚠️ Regla innegociable
> Ningún recurso teórico nuevo si no se ha completado el hito práctico de la semana anterior.

Esta regla se respeta semana a semana — el check correspondiente vive en cada nota semanal, no aquí.

## Progreso por mes

### Mes 1 — Tronco de base + arranque del libro
- [ ] Networking Basics (NetAcad, 22h) completado — Knowledge Check + Módulo 1 hechos
- [ ] Subnetting Mastery (NetAcad, beta, 4h) completado
- [x] Linux Journey completado
- [ ] OverTheWire Bandit hasta nivel 15 — niveles 0 a 5 cerrados
- [ ] Libro de Kasiu — lectura panorámica completa (ver sección abajo) — sin empezar todavía

### Mes 2 — Profundización dominios Cloud-relevantes + práctica
- [ ] Endpoint Security (NetAcad, 27h, 31 labs) completado — vehículo principal de profundización (cubre Dominio 2 y 3 con práctica real, no solo relectura de Kasiu)
- [ ] OverTheWire Bandit hasta nivel 25
- [ ] Homelab básico iniciado
- [ ] Profundización en los dominios prioritarios (ver sección abajo)
- [ ] *(opcional, si queda tiempo)* TryHackMe Pre Security path

### Mes 3 — Consolidación + homelab + GitHub público
- [ ] TryHackMe Cyber Security 101 path completo
- [ ] Homelab funcionando: VM Ubuntu + VM Windows + conectividad básica
- [ ] Homelab documentado en repo público de GitHub
- [ ] Dominios prioritarios del libro cerrados

## 📖 Seguimiento del libro de Kasiu

> El libro es panorámico por diseño — para los dominios prioritarios, "profundización" significa un recurso real con práctica, no releer el capítulo. Dominio 2 y 3 ya tienen ese recurso (Endpoint Security). Dominio 4, 7 y 8 todavía no — buscar cuando llegue el mes 2, no antes.

- [ ] Dominio 1 — Fundamentos de Ciberseguridad
- [ ] Dominio 2 — Seguridad de Red *(prioritario)*
  - [ ] Profundización (mes 2) → vía Endpoint Security
- [ ] Dominio 3 — Seguridad de Endpoints *(prioritario)*
  - [ ] Profundización (mes 2) → vía Endpoint Security
- [ ] Dominio 4 — Gestión de Identidades y Accesos / IAM *(prioritario)*
  - [ ] Profundización (mes 2) → recurso pendiente de buscar
- [ ] Dominio 5 — Seguridad de Aplicaciones y Datos
- [ ] Dominio 6 — Seguridad en la Nube
- [ ] Dominio 7 — Criptografía *(prioritario)*
  - [ ] Profundización (mes 2) → recurso pendiente de buscar
- [ ] Dominio 8 — Monitorización y SOC *(prioritario)*
  - [ ] Profundización (mes 2) → recurso pendiente de buscar
- [ ] Dominio 9 — Respuesta a Incidentes y Forense (DFIR)
- [ ] Dominio 10 — Gestión de Vulnerabilidades
- [ ] Dominio 11 — Continuidad de Negocio y Recuperación ante Desastres

## Hitos medibles de Fase 0 (criterio de cierre de fase)
- [ ] Bandit hasta nivel 25 mínimo
- [ ] Pre Security path completo (TryHackMe)
- [ ] Cyber Security 101 path completo (TryHackMe)
- [ ] Kasiu — panorámico completo + dominios prioritarios profundizados *(ver sección de arriba)*
- [ ] Homelab funcionando con 2 VMs y conectividad
- [ ] Repo público en GitHub documentando el homelab
- [ ] LinkedIn optimizado (sin actividad todavía)

## 🗂️ Aplazado (no es Fase 0)
- **Cisco Networking Essentials** — bloqueado, solo instructor-led vía academia.
- **Network Technician Career Path** (NetAcad, 70h + examen CCST) — confirmado free self-paced, pero su presupuesto de horas se come prácticamente toda Fase 0 él solo. Retomar durante el Grado si interesa la certificación CCST; por ahora solo se usa el primer curso (Networking Basics, 22h).
  - *Network Addressing and Basic Troubleshooting* (14h) requiere como prerrequisito el curso 2 (Networking Devices and Initial Configuration) — cogerlo suelto deja un hueco en configuración de switches/routers; cogerlo con su prerrequisito reabre el problema de horas. Se hace junto con el resto de la ruta, no antes.

## Registro semanal

| Semana | Mes | Estado | Hito práctico cerrado |
|---|---|---|---|
| [[Semana_01]] | 1 | 🟢 Cerrada (parcial — Kasiu/Subnetting pendientes) | Sí |
| [[Semana_02]] | 1 | 🟡 En curso | |

*(Duplica la fila al crear cada nueva semana desde `_Plantilla_Semana.md`)*

## 🔗 Índices (MOC)
- [[MOC - Redes]]
- [[MOC - Sistemas Operativos]]

*(añade aquí cada MOC nueva que crees en `_MOCs/`)*
