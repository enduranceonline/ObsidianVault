

---
# **Proyecto SIEM-HomeLab**

El proyecto **SIEM-HomeLab** es una infraestructura real y documentada diseñada para aprender, practicar y demostrar habilidades de **Blue Team**, **SOC Analyst** y **Arquitectura de Seguridad**, utilizando como base una vivienda inteligente de 2026/2027 con numerosos dispositivos de última generación.

El objetivo principal es construir un entorno que permita:

- monitorizar una red doméstica compleja
    
- detectar ataques reales y simulados
    
- responder a incidentes
    
- realizar ejercicios controlados de ataque/defensa
    
- documentar las metodologías y decisiones técnicas
    
- obtener experiencia directamente aplicable a un puesto SOC
    

Este homelab se plantea como un **proyecto a largo plazo**, escalable, realista y dividido en fases claras, desde la teoría hasta la operación continua, pasando por el diseño arquitectónico y la implementación completa.

---

## **1. Objetivos Generales del Proyecto**

### **Aprendizaje técnico profundo**

Dominar de forma práctica los conceptos clave de un SOC moderno:

- segmentación de red
    
- firewalling avanzado
    
- SIEM (Wazuh)
    
- IDS/IPS (Suricata)
    
- honeypots
    
- análisis de logs
    
- correlación de eventos
    
- detección basada en MITRE ATT&CK
    
- OSQuery, Sysmon y telemetría de endpoints
    
- automatización SOAR
    

### **Creación de un entorno realista**

Integrar:

- un firewall dedicado
    
- switch gestionable L3
    
- puntos de acceso WiFi profesionales
    
- VLANs
    
- contenedores Docker
    
- VMs conforme a un SOC real
    
- dispositivos IoT reales
    
- PCs personales como endpoints monitorizados
    

### **Desarrollo de proyecto demostrable**

Documentación completa:

- diagramas
    
- decisiones técnicas
    
- comparativas
    
- escenarios A/B/C
    
- justificación de elecciones
    
- costes energéticos y económicos
    
- fichas de componentes
    
- ejercicios de ataque y defensa
    
- reporte final estilo SOC
    

El resultado final servirá como **pieza sólida de portfolio profesional**.

---

## **2. Motivación del Proyecto**

La vivienda de obra nueva permitirá:

- cableado estructurado
    
- ubicaciones óptimas para firewall, switch y APs
    
- una red diseñada desde cero
    
- gran número de dispositivos IoT y electrodomésticos inteligentes
    
- un NAS dedicado
    
- dos PCs potentes y un portátil Kali Linux de gama alta
    

Este contexto da pie a una **arquitectura similar a la de una pequeña empresa**, ideal para practicar procesos SOC con realismo, sin limitaciones de laboratorio “artificial”.

---

## **3. Alcance Técnico del Proyecto**

El SIEM-HomeLab cubrirá:

### **Diseño**

- Arquitectura lógica y física
    
- Segmentación por VLANs
    
- Escenarios tecnológicos y decisiones (A/B/C)
    
- Planificación espacial del piso
    
- Diagramas completos
    

### **Implementación**

- Firewall (OPNsense/pfSense)
    
- Docker y contenedores del SOC
    
- Wazuh como SIEM
    
- Suricata como IDS
    
- Honeypots aislados
    
- Agentes Windows, Linux, IoT
    

### **Operaciones SOC**

- monitorización
    
- correlación avanzada
    
- generación de alertas
    
- respuesta a incidentes
    
- automatización SOAR
    
- mantenimiento y actualización
    

### **Laboratorio**

- ataques (scans, explotación, movimiento lateral)
    
- defensa (detecciones en SIEM, IDS, endpoints)
    
- ejercicios MITRE ATT&CK
    
- pentesting interno controlado
    
- evaluación continua
    

---

## **4. Estructura del Proyecto en Obsidian**

El proyecto está organizado en carpetas principales:

```
00_Base/
10_Teoria_Base/
20_Diseño_Arquitectura/
30_Implementacion/
40_Operaciones_SOC/
50_Laboratorio/
60_Proyecto_Final/
```

Cada área contiene decenas de notas, diagramas y procesos detallados para permitir una experiencia real de trabajo SOC.

---

## **5. Estilo y documentación**

Todo el proyecto se documenta siguiendo:

- formato Markdown
    
- diagramas en Excalidraw
    
- enlaces internos entre notas
    
- redacción clara orientada a comprensión técnica
    
- enfoque pedagógico y profesional
    
- revisiones incrementales
    

Cada decisión técnica será siempre:

- explicada
    
- justificada
    
- comparada
    
- y asociada a un impacto real dentro de la arquitectura
    

---

## **6. Resultado esperado**

Al finalizar el proyecto, se obtendrá:

- un SOC doméstico **funcional**, **estable** y **monitorizando en tiempo real**
    
- experiencia equivalente a un entorno corporativo pequeño
    
- dominio técnico demostrable en entrevistas SOC
    
- un caso real que mejora tu perfil profesional
    
- documentación completa que podrás mostrar en tu portafolio
    
- un entorno permanente para seguir aprendiendo
    

---
