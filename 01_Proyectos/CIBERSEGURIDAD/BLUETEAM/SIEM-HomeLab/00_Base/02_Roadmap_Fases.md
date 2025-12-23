# **Roadmap del Proyecto SIEM-HomeLab**

Este roadmap define el orden lógico, técnico y pedagógico del proyecto.  

Cada fase tiene objetivos claros, entregables concretos y dependencias explícitas, de forma que el progreso sea continuo y el resultado final sea un homelab funcional equivalente al de una pequeña empresa.

---

# **📌 Resumen global del Roadmap**

1. **Fase 0 — Fundamentos teóricos**
    
2. **Fase 1 — Diseño completo de arquitectura**
    
3. **Fase 2 — Implementación física y lógica de la red**
    
4. **Fase 3 — Despliegue de la plataforma SOC (SIEM + IDS + Honeypots)**
    
5. **Fase 4 — Operaciones SOC y casos de uso reales**
    
6. **Fase 5 — Laboratorio (ataque/defensa) y validación final**
    
7. **Fase 6 — Documentación final y portfolio profesional**
    

Este orden está optimizado para no perder tiempo, minimizar errores y asegurar una curva de aprendizaje sólida y acumulativa.

---
# **0️⃣ Fase 0 — Fundamentos Teóricos**

### **Objetivo**

Construir una base sólida para entender la red, el SOC y todos los componentes del proyecto sin improvisar.

### **Qué vas a hacer**

- Aprender cómo funciona una red segmentada (VLAN, routing, NAT).
    
- Entender qué hace un firewall.
    
- Comprender Docker, contenedores y servicios del SOC.
    
- Dominar conceptos SIEM, IDS, Sysmon, OSQuery y MITRE ATT&CK.
    

### **Qué tendrás al finalizar**

- Conocimiento suficiente para diseñar tu arquitectura sin dudas.
    
- Notas organizadas que usarás durante todo el proyecto.
    

### **Qué debe estar hecho antes**

Nada. Esta fase es el punto de partida.

---

# **1️⃣ Fase 1 — Diseño Completo de Arquitectura**

### **Objetivo**

Definir cómo será tu red y tu SOC, antes de comprar hardware o tocar configuraciones.

### **Qué vas a hacer**

- Diseñar la red lógica (VLANs, tráfico, zonas).
    
- Diseñar la red física adaptada a tu piso.
    
- Elegir hardware (firewall, switch, APs, NAS…).
    
- Comparar escenarios y elegir el definitivo.
    
- Crear los diagramas que guiarán toda la implementación.
    

### **Qué tendrás al finalizar**

- Una arquitectura profesional y pensada para SOC real.
    
- Diagrama final y lista de compras lista para ejecutar.
    

### **Qué debe estar hecho antes**

Comprender los conceptos teóricos básicos (Fase 0).

---

# **2️⃣ Fase 2 — Implementación Base de la Red**

### **Objetivo**

Construir la red real segmentada donde funcionará tu SOC.

### **Qué vas a hacer**

- Configurar el firewall con las zonas y reglas básicas.
    
- Configurar el switch con VLANs y routing interno.
    
- Distribuir los APs y segmentar el WiFi.
    
- Configurar el NAS para almacenamiento inicial.
    
- Verificar que cada segmento funciona como debe.
    

### **Qué tendrás al finalizar**

- Una red doméstica profesional, separada y segura.
    
- Todos los equipos conectados a sus VLANs correspondientes.
    
- Un “esqueleto” perfecto para desplegar el SOC.
    

### **Qué debe estar hecho antes**

El diseño final validado (diagramas y decisiones de la Fase 1).

---

# **3️⃣ Fase 3 — Despliegue de la Plataforma SOC**

### **Objetivo**

Instalar todo el ecosistema de seguridad: SIEM, IDS, Honeypots y contenedores.

### **Qué vas a hacer**

- Instalar Docker y preparar todos los servicios.
    
- Desplegar Wazuh (SIEM) completo.
    
- Instalar y conectar Suricata (IDS).
    
- Crear la red de honeypots aislada.
    
- Integrar IDS + SIEM + endpoints reales.
    

### **Qué tendrás al finalizar**

- Un SOC doméstico funcionando realmente.
    
- Logs en tiempo real, alertas, detección de tráfico y actividad.
    

### **Qué debe estar hecho antes**

La red segmentada funcionando (Fase 2).

---

# **4️⃣ Fase 4 — Operaciones SOC**

### **Objetivo**

Aprender a “ser” un analista SOC: monitorizar, crear reglas, cazar amenazas.

### **Qué vas a hacer**

- Revisar alertas y paneles.
    
- Crear reglas personalizadas “a medida”.
    
- Mapear eventos a MITRE ATT&CK.
    
- Simular procedimientos de respuesta a incidentes.
    
- Automatizar tareas con SOAR (opcional).
    

### **Qué tendrás al finalizar**

- Conocimientos equivalentes a un analista SOC Nivel 1–2.
    
- Un entorno donde puedes detectar actividad maliciosa real.
    

### **Qué debe estar hecho antes**

Wazuh, Suricata y honeypots funcionando (Fase 3).

---

# **5️⃣ Fase 5 — Laboratorio (Ataque y Defensa)**

### **Objetivo**

Generar actividad maliciosa real en tu red y practicar detección y respuesta.

### **Qué vas a hacer**

- Escanear tu red como un atacante real.
    
- Explotar servicios vulnerables.
    
- Hacer movimiento lateral.
    
- Intentar evadir el IDS.
    
- Introducir malware controlado en una VM aislada.
    
- Crear nuevas reglas y correlaciones basadas en tus ataques.
    

### **Qué tendrás al finalizar**

- Detecciones demostradas en tu SIEM/IDS.
    
- Evidencias documentadas para tu portfolio.
    
- Conocimiento profundo del ciclo ataque → defensa.
    

### **Qué debe estar hecho antes**

Tener un SOC completamente operativo (Fase 4).

---

# **6️⃣ Fase 6 — Documentación Final y Portfolio**

### **Objetivo**

Transformar todo el proyecto en documentación profesional para presentar en tu CV o entrevistas.

### **Qué vas a hacer**

- Redactar el informe técnico.
    
- Crear el dossier visual (diagramas, capturas, flujos).
    
- Preparar el resumen para tu CV.
    
- Seleccionar evidencias del laboratorio.
    
- Preparar material para entrevistas.
    

### **Qué tendrás al finalizar**

- Un proyecto completo, serio y demostrable.
    
- Un caso real que te diferencia en entrevistas SOC.
    
- Material sólido para tu portfolio profesional.
    

### **Qué debe estar hecho antes**

Todas las fases previas completadas.