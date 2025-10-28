#ERP 

---

📘 _Profesor: José Luis Sánchez Montejo 

📘 Sistemas de gestión empresarial. ERP-CRM

 🗓 Clase 2 — 21/10/2025 

🎯 Tema:  ERP, CRM, SRM, CMS, BI, Odoo

---

# Sistemas de Gestión Empresarial

---

## 1️⃣ Concepto de sistema de gestión empresarial

Un **sistema de gestión empresarial (SGE)** es un conjunto de aplicaciones informáticas que permiten **automatizar y centralizar las operaciones internas más importantes de una empresa**, como finanzas, compras, ventas, producción, inventario y atención al cliente.

Su objetivo es **unificar la información y optimizar procesos** mediante un flujo de datos compartido entre departamentos.  

Los módulos típicos incluyen:

|Departamento|Funciones principales|
|---|---|
|**Dirección**|Control de costes, márgenes y objetivos (OKR) desde cuadros de mando.|
|**Comercial / CRM**|Gestión de oportunidades, presupuestos y pedidos enlazados con ventas.|
|**Ventas**|Pedidos, albaranes y facturas conectados con stock y cobros.|
|**Compras**|Solicitud y aprobación de pedidos a proveedores, reposición de stock.|
|**Almacén / Inventario**|Entradas y salidas, ubicaciones, lotes o series, sincronizado con ventas y compras.|
|**Finanzas / Contabilidad**|Asientos automáticos, IVA, conciliación bancaria.|
|**RR. HH. / Nóminas**|Gestión de empleados, permisos, turnos, costes por centro o proyecto.|
|**Atención al cliente**|Tickets, SLA y seguimiento de incidencias vinculadas a pedidos.|
|**E-commerce / TPV**|Catálogo, ventas online o físicas integradas con stock y facturación.|

---

## 2️⃣ Familias de soluciones de gestión

Los sistemas empresariales se agrupan en familias según su función:

- **ERP – Enterprise Resource Planning:** planificación de recursos y control interno.
    
- **CRM – Customer Relationship Management:** gestión del ciclo de vida del cliente.
    
- **SRM – Supplier Relationship Management:** gestión de la relación con proveedores.
    
- **CMS – Content Management System:** creación y publicación de contenidos digitales.
    
- **BI – Business Intelligence:** análisis y visualización de datos empresariales.

---

## 3️⃣ ERP – Enterprise Resource Planning

Sistema que **integra y coordina todas las áreas de una empresa** en una base de datos común. Es el **núcleo transaccional** donde confluyen compras, ventas, inventarios, producción y contabilidad.

### 🔹 Funciones

- Control unificado de la información.
    
- Automatización de procesos repetitivos.
    
- Trazabilidad completa de pedidos, gastos y recursos.
    
- Acceso dinámico a datos en tiempo real.

### 🔹 Ejemplos

SAP S/4HANA, Odoo, Oracle NetSuite, Microsoft Dynamics 365.

---

## 4️⃣ CRM – Customer Relationship Management

Sistema que **centraliza todas las interacciones entre empresa y clientes**. Sirve de apoyo al área comercial para administrar contactos, oportunidades, tareas y campañas.

### 🔹 Objetivos

- **Mejorar la comunicación interna:** las tareas ligadas a clientes se asignan y monitorizan.
    
- **Incrementar la productividad:** evita correos y reuniones innecesarias.
    
- **Aumentar las ventas:** permite seguimiento de oportunidades y personalización.

### 🔹 Ejemplos

Salesforce, HubSpot, Zoho CRM, Odoo CRM.

---

## 5️⃣ SRM – Supplier Relationship Management

Software destinado a **estandarizar y optimizar la relación con proveedores**.

### 🔹 Funciones

- Homologación de proveedores.
    
- Gestión de pedidos y contratos.
    
- Evaluación de desempeño y cumplimiento.

**Ejemplo:** en un modelo _drop & shipping_, el SRM controla proveedores externos que envían directamente al cliente final.

---

## 6️⃣ CMS – Content Management System

Sistema de gestión de contenidos que **permite crear, editar y publicar contenido digital sin necesidad de programar código**.

### 🔹 Tipos

- **Tradicional o monolítico:** back + front integrados (WordPress, Drupal, Joomla).
    
- **Headless:** el CMS solo guarda el contenido y lo expone vía **API**; el front se desarrolla aparte.
    
- **Híbrido:** combina páginas clásicas con APIs headless (WordPress REST, Drupal JSON:API).

> 🧩 Aclaración del profesor:  
> 
> WordPress crea contenido, pero no es la herramienta del cliente para introducirlo dinámicamente.  
>
> Se puede desarrollar un CMS propio que, mediante una API, **alimente una web externa**.  
> En este modelo, **el backend se comunica con el frontend a través de la API**, y el _headless_ es esa API.

---

## 7️⃣ BI – Business Intelligence

Conjunto de herramientas que **recopilan, integran y analizan los datos de la empresa** para transformarlos en información útil y cuadros de mando (_dashboards_).

### 🔹 Objetivo

Ayudar a la dirección a **tomar decisiones estratégicas** basadas en indicadores de rendimiento (**KPI**).

### 🔹 Ejemplos

Microsoft Power BI, Tableau, Qlik Sense, Looker Studio.

> Imagen del profesor: dashboard de Power BI mostrando estadísticas por municipio y género.

---

## 8️⃣ Toma de requisitos

Proceso previo a la implantación de un sistema empresarial.  

Consiste en **identificar necesidades, objetivos y limitaciones** de la organización para seleccionar la solución más adecuada.

### 🔹 Etapas

1. **Análisis de procesos existentes.**
    
2. **Identificación de carencias y objetivos.**
    
3. **Definición funcional y técnica (requisitos del software).**
    
4. **Priorización por coste y valor añadido.**

---

## 9️⃣ Interrelación entre los sistemas

Los diferentes sistemas no funcionan aislados: **se complementan para cubrir todo el ciclo operativo.**

|Sistema|Rol principal|Integración típica|
|---|---|---|
|**ERP**|Gestión global de recursos|Se conecta con CRM, SRM y BI.|
|**CRM**|Gestión de clientes|Exporta datos de ventas al ERP.|
|**SRM**|Gestión de proveedores|Sincroniza compras e inventario con ERP.|
|**CMS**|Gestión de contenidos web|Consume datos mediante API (_headless_).|
|**BI**|Análisis de datos globales|Consolida la información de todos los anteriores.|

> En conjunto, el ERP actúa como **el “control del barco”**, mientras BI muestra en el _dashboard_ los indicadores para mantener el rumbo.

---

## 🔟 Ejemplo práctico – Odoo

**Odoo** nació como software _open source_ que integra módulos ERP, CRM, SRM, CMS y BI en una única plataforma.  

Se utiliza a menudo como alternativa económica a sistemas más exigentes, ya que puede instalarse en hardware modesto sin necesidad de comprar un equipo nuevo.

### 🔹 Ventajas

- Código abierto y personalizable.
    
- Módulos independientes y escalables.
    
- Ideal para aprendizaje o pequeñas empresas.

---
