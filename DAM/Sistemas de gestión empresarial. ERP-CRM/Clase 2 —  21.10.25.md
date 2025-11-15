#ERP 

---

👨‍🏫 _Profesor: José Luis Sánchez Montejo 
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

Un ERP es la columna vertebral del sistema de información empresarial. Gestiona todas las **transacciones críticas** de la organización y garantiza que cada dato tenga un único origen y una única versión válida. Esto elimina duplicidades, inconsistencias y falta de trazabilidad entre departamentos.

Un ERP **no es solo software**: es un marco metodológico que transforma cómo se gestiona el negocio.

---

### 🔹 Funciones (ampliación profunda)

#### **1. Control unificado de la información**

- Un único repositorio de datos compartido por toda la empresa.
    
- Elimina versiones múltiples del mismo documento (pedidos, inventarios, facturas).
    
- Facilita auditoría, control interno y cumplimiento normativo.

**Impacto real:**  
Ventas ya no pregunta a almacén si hay stock; el sistema lo sabe.

---

#### **2. Automatización de procesos repetitivos**

- Acciones automáticas que antes se hacían manualmente:
    
    - Actualización de stock en tiempo real.
        
    - Creación de asientos contables al facturar.
        
    - Generación de órdenes de producción según demanda.
        
    - Envío de avisos de cobro o de entrega.
        
    - Cálculo de necesidades de compra según MRP.

**Impacto real:**  
Menos errores humanos, menor tiempo administrativo, más productividad operativa.

---

#### **3. Trazabilidad completa**

- Seguimiento de:
    
    - lotes de productos
        
    - movimientos internos
        
    - cambios de precio
        
    - historiales de pedido y entrega
        
    - incidencias y devoluciones

**Impacto real:**  
Puedes reconstruir cada paso que siguió un pedido o una incidencia con precisión.

---

#### **4. Acceso dinámico en tiempo real**

- Todos los módulos se actualizan al instante.
    
- Indicadores financieros, de stock y producción se sincronizan automáticamente.

**Impacto real:**  
Los directores pueden tomar decisiones basadas en datos actualizados, no en archivos obsoletos.

---

### 🔹 Áreas integradas (explicación extendida)

- **Ventas:** presupuestos, pedidos, devoluciones.
    
- **Compras:** solicitudes, órdenes, recibos, control de proveedores.
    
- **Inventario:** control de ubicaciones, lotes, fechas de caducidad.
    
- **Producción:** listas de materiales (BOM), MRP, planificación, tiempos.
    
- **Contabilidad:** facturación, impuestos, asientos, conciliación bancaria.
    
- **RRHH:** nóminas, registros horarios, ausencias.
    
- **Logística:** picking, rutas, expediciones, transporte.
    
- **Soporte:** tickets, incidencias, garantías.

**Todos los procesos están encadenados.**  
No existen departamentos “ciegos”.

---

### 🔹 Arquitectura del ERP (ampliado)

La base técnica de un ERP se sustenta en un modelo OLTP:

- Tablas normalizadas
    
- Transacciones ACID
    
- Alta disponibilidad
    
- Baja latencia
    
- Integridad referencial estricta

Esto garantiza coherencia al operar en tiempo real.

---

### 🔹 Ejemplos con enfoque y matices

- **SAP S/4HANA:** entorno corporate, arquitectura in-memory, procesos avanzados y complejos.
    
- **Odoo:** modular, open source, ideal para PYMEs y negocios que necesitan flexibilidad.
    
- **Oracle NetSuite:** cloud nativo, muy fuerte en contabilidad multinivel.
    
- **Microsoft Dynamics 365:** potente integración con Office/Teams/Power BI.

---

## 4️⃣ CRM – Customer Relationship Management

El CRM se centra en **gestionar la relación comercial** con clientes potenciales y actuales.  

Opera antes de la transacción, durante la venta y en la fase de fidelización.

---

### 🔹 Objetivos principales (ampliación técnica y práctica)

#### **1. Mejorar la comunicación interna**

- Todos los miembros del equipo comercial ven el mismo historial del cliente.
    
- La información no se pierde entre correos o conversaciones.
    
- Facilita colaboración entre marketing, ventas y soporte.

**Escenario:**  
Un comercial sabe en segundos qué prometió otro compañero en una negociación anterior.

---

#### **2. Incrementar la productividad**

- Automatiza recordatorios, correos, seguimientos.
    
- Mide conversiones y rendimiento del equipo.
    
- Prioriza leads de mayor valor.

**Escenario:**  
El CRM asigna automáticamente un lead nuevo al comercial con menos carga.

---

#### **3. Aumentar ventas**

- Pipeline visual para ver el estado de cada oportunidad.
    
- Segmentación avanzada por criterios: país, sector, histórico.
    
- Estrategias de marketing automatizadas.

**Escenario:**  
El sistema detecta clientes con baja actividad y dispara campañas personalizadas.

---

### 🔹 Qué gestiona un CRM (visión detallada)

- **Leads:** datos de potenciales clientes captados por formularios o campañas.
    
- **Oportunidades:** negociaciones activas en diferentes etapas.
    
- **Actividades:** tareas, llamadas, reuniones agendadas.
    
- **Documentos:** presupuestos, contratos, propuestas.
    
- **Interacciones:** emails, notas internas, mensajes telefónicos.

El CRM es un registro exhaustivo de todas las comunicaciones con el cliente.

---

### 🔹 Integración CRM → ERP (flujo ampliado)

1. Un lead se convierte en oportunidad.
    
2. La oportunidad se trabaja en el CRM (reuniones, llamadas, negociaciones).
    
3. La oportunidad se gana.
    
4. El CRM crea el pedido de venta en el ERP.
    
5. El ERP:
    
    - reserva stock
        
    - actualiza inventario
        
    - genera orden de fabricación si hace falta
        
    - emite factura
        
    - registra el asiento contable

**Beneficio clave:**  
La venta se transforma automáticamente en impacto real en la operación y en la contabilidad.

---

### 🔹 Ejemplos con diferencias estratégicas

- **Salesforce:** máximo nivel de personalización, ecosistema amplio.
    
- **HubSpot:** excelente marketing automation.
    
- **Zoho CRM:** fuerte coste/beneficio.
    
- **Odoo CRM:** integrado nativamente con módulos ERP.

---

Si quieres, amplío ahora:

- Comparativa detallada ERP vs CRM en tabla
    
- Ejemplo práctico realend-to-end
    
- Arquitectura de integración real entre sistemas  
    Dime qué prefieres.

---

## 5️⃣ SRM – Supplier Relationship Management

El SRM es el sistema destinado a **centralizar, controlar y optimizar todo el ciclo de vida de los proveedores**. A diferencia del ERP, que gestiona las transacciones internas, el SRM está orientado a la **relación externa con proveedores**, su desempeño y su contribución a la cadena de suministro.

Un SRM no solo “registra pedidos”, sino que introduce criterios de calidad, evaluación y políticas de negociación que permiten mejorar la eficiencia de compras.

---

### 🔹 Funciones

#### **1. Homologación de proveedores**

- Registro y validación inicial del proveedor.
    
- Documentación obligatoria (certificaciones, seguros, normativas).
    
- Clasificación por categorías, riesgo y especialización.
    
- Evaluación previa antes de aceptar trabajar con ellos.

**Impacto real:**  
La empresa evita trabajar con proveedores que no cumplen requisitos legales o de calidad.

---

#### **2. Gestión de pedidos y contratos**

- Creación de solicitudes de ofertas (RFQ: Request For Quotation).
    
- Comparación de precios, plazos y condiciones.
    
- Firma digital y registro centralizado de contratos.
    
- Renovaciones, revisiones y alertas automáticas.
    
- Control de entregas y cumplimiento de plazos.

**Impacto real:**  
Compras puede gestionar múltiples proveedores simultáneamente sin perder control documental.

---

#### **3. Evaluación de desempeño y cumplimiento**

- Métricas clave:
    
    - puntualidad en entregas
        
    - calidad del material
        
    - tasa de incidencias
        
    - cumplimiento contractual
        
    - precios históricos
        
- Informes periódicos y dashboards comparativos.

**Impacto real:**  
Permite identificar proveedores fiables, negociar mejor y reducir riesgos de la cadena de suministro.

---

### 🔹 SRM en modelos modernos como Drop & Shipping (explicación extendida)

En un modelo de **drop & shipping**:

- el vendedor no almacena stock
    
- el proveedor envía directamente al cliente final

El SRM se vuelve crítico porque:

- controla la disponibilidad real del proveedor
    
- gestiona incidencias y tiempos de entrega
    
- registra el cumplimiento del proveedor
    
- coordina la logística externa
    
- genera indicadores de rendimiento por proveedor

**Resultado:**  
La empresa puede vender sin almacén propio, pero mantiene control sobre calidad y plazos.

---

## 6️⃣ CMS – Content Management System

Un CMS es un sistema diseñado para **crear, estructurar, editar y publicar contenido digital** sin necesidad de conocimientos avanzados de programación. El CMS es usado por el equipo de marketing, comunicación o editores de contenido.

Su propósito no es gestionar transacciones, inventarios ni contabilidad, sino **gestionar contenido web**.

---

### 🔹 Tipos

#### **1. CMS tradicional o monolítico**

Back-end + front-end unidos en una única aplicación.

- El CMS genera contenido
    
- Controla la base de datos
    
- Renderiza el frontend

Ejemplos:

- WordPress
    
- Joomla
    
- Drupal

**Ventaja:** fácil de usar, instalación rápida.  
**Desventaja:** menos flexible para arquitecturas avanzadas o apps móviles.

---

#### **2. CMS headless**

Backend independiente que **solo gestiona contenido**.

- No tiene interfaz web para mostrar el contenido
    
- Expone el contenido vía **API REST/GraphQL**
    
- Front-end se desarrolla en cualquier tecnología:
    
    - React
        
    - Vue
        
    - Angular
        
    - Apps móviles
        
    - Portales personalizados

**Ventaja:** máxima flexibilidad y escalabilidad.  
**Desventaja:** requiere desarrollo del front.

---

#### **3. CMS híbrido**

Combina páginas generadas tradicionalmente con contenido accesible vía API.

- WordPress con REST API habilitada
    
- Drupal con JSON:API
    
- Backend monolítico con endpoints headless

**Ventaja:** se aprovecha facilidad del CMS tradicional + flexibilidad de headless.  

**Desventaja:** mayor complejidad técnica y de mantenimiento.

---

### 🧩 Aclaración del profesor

> WordPress crea contenido, pero no es la herramienta del cliente para introducirlo dinámicamente.

Esto significa:

- WordPress **permite crear contenido**, pero la forma en que un usuario final introduce datos “dinámicos” depende del diseño del sitio.
    
- En entornos profesionales, el cliente no siempre edita el sitio directamente; se diseña un CMS **a medida** que alimenta la web externa mediante una API.

En un modelo **headless**:

- El CMS actúa como **backend puro**
    
- La API es el medio de comunicación
    
- El frontend consume contenido dinámico desde esa API

En otras palabras:  
**El "headless" es la API. El CMS es el origen del contenido. El frontend es independiente.**

---

Si quieres, ahora amplío también:

- Comparativa SRM vs ERP en procesos de compras
    
- Flujo completo “solicitud de oferta → entrega → incidencia”
    
- Ejemplo real de arquitectura CMS headless con Odoo como backend.

---

## 7️⃣ BI – Business Intelligence

BI agrupa un conjunto de **tecnologías, metodologías y herramientas** orientadas a transformar datos operativos (provenientes del ERP, CRM, SRM, CMS, Data Warehouse, etc.) en información estructurada y comprensible para apoyar la toma de decisiones.  

Su función principal es convertir grandes volúmenes de datos dispersos en **conocimiento accionable**.

El BI no ejecuta operaciones, no factura, no mueve stock. BI **analiza**.

---

### 🔹 Objetivo

El objetivo central de BI es proporcionar a la dirección y a los mandos intermedios información de **valor estratégico**.  
Esto se consigue mediante:

- **Indicadores clave de rendimiento (KPIs)**  
    Miden con precisión el avance hacia objetivos   (ventas, margen, rotación de stock, eficiencia de producción).
    
- **Cuadros de mando interactivos (dashboards)**  
    Presentan los datos de forma visual y clara  para detectar patrones, tendencias y anomalías.
    
- **Informes personalizados**  
    Filtrados por departamento, región, producto,  cliente, periodo temporal.
    
- **Análisis comparativos**  
    Año contra año (YoY), mes contra mes (MoM), previsión vs real.

En resumen: BI permite pasar de **datos brutos** a **decisión fundamentada**.

---

### 🔹 Qué hace BI realmente (visión profunda)

- **Unifica fuentes de datos** en un único modelo analítico
    
- **Permite análisis multidimensional**: por cliente, zona, producto, tiempo
    
- **Genera alertas** cuando un KPI sale de rango
    
- **Detecta tendencias** que no son visibles en los sistemas operativos
    
- **Optimiza la toma de decisiones** mediante gráficos, tablas dinámicas y filtros

**Ejemplo práctico:**  
Un director quiere saber:

- qué productos tienen menor margen
    
- en qué regiones hay más devoluciones
    
- qué comerciales tienen mejor tasa de conversión
    
- qué proveedores generan más retrasos

El BI reúne datos del ERP, CRM y SRM y responde en segundos.

---

### 🔹 Ejemplos

**Microsoft Power BI**

- Ideal para empresas que ya usan Microsoft 365.
    
- Potente capacidad de modelado y conectores nativos a ERP/CRM.

**Tableau**

- Excelente en visualización avanzada.
    
- Ideal para análisis complejos y exploratorios.

**Qlik Sense**

- Modelo asociativo que permite encontrar relaciones ocultas.
    
- Ideal para análisis de grandes volúmenes.

**Looker Studio (antes Data Studio)**

- Integración con ecosistema Google.
    
- Orientado a dashboards rápidos y accesibles.

---

### 🔹 Relación BI ↔ Data Warehouse

BI consume datos del **Data Warehouse**, no del ERP en vivo.  
Esto evita:

- cargar demasiado el ERP
    
- ralentizar operaciones
    
- inconsistencias de datos en análisis

El DW prepara datos limpios y consolidados → BI los transforma en paneles visuales.

---

## 8️⃣ Toma de requisitos

La toma de requisitos es una fase crítica antes de seleccionar, diseñar o implantar un sistema empresarial (ERP, CRM, SRM, CMS o BI).  
Es el momento en que se define **qué necesita realmente la empresa**, más allá de la tecnología.

Sin una buena toma de requisitos:

- se eligen soluciones inadecuadas
    
- el proyecto se descontrola
    
- surgen sobrecostes
    
- los usuarios rechazan el sistema

---

### 🔹 Etapas

#### **1. Análisis de procesos existentes**

- Mapear procesos actuales
    
- Identificar roles y responsabilidades
    
- Detectar herramientas utilizadas
    
- Observar flujos de trabajo reales, no teóricos

**Objetivo:** entender cómo funciona realmente la empresa, no cómo debería funcionar.

---

#### **2. Identificación de carencias y objetivos**

- Problemas detectados (falta de trazabilidad, retrasos, duplicidades, errores)
    
- Necesidades del negocio (agilidad, control, escalabilidad)
    
- Objetivos estratégicos (crecer, exportar, automatizar, reducir costes)

**Impacto:** establece el norte del proyecto.

---

#### **3. Definición funcional y técnica**

- Requisitos funcionales:
    
    - qué debe hacer el sistema
        
    - módulos necesarios
        
    - flujos de trabajo
        
    - pantallas clave
        
    - informes y permisos
        
- Requisitos técnicos:
    
    - integración con otros sistemas
        
    - servidores, bases de datos
        
    - rendimiento y seguridad
        
    - requerimientos legales

**Resultado:** documento de especificaciones.

---

#### **4. Priorización por coste y valor añadido**

- No todo se implementa de golpe
    
- Se priorizan:
    
    - procesos críticos
        
    - módulos esenciales
        
    - quick wins
        
- Se decide una hoja de ruta (roadmap)

**Resultado:** implantación escalonada, control de costes y adopción gradual.

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

Odoo es un ecosistema empresarial modular que combina en un único entorno funciones de ERP, CRM, SRM, CMS y BI. Nació como un proyecto **open source** con el objetivo de ofrecer una solución flexible, accesible y adaptable a distintos tamaños de negocio, especialmente PYMEs, startups y entornos educativos.

Su arquitectura permite activar únicamente los módulos necesarios y ampliar capacidades conforme crece la empresa. Esto lo convierte en un sistema eficiente tanto para escenarios reales como para formación técnica.

---

### 🔹 Ventajas

#### **1. Código abierto y personalizable**

- Acceso completo al código en la versión Community.
    
- Permite modificar vistas, modelos, workflows y lógica de negocio.
    
- Integrable con APIs, módulos externos, conectores de comercio electrónico o TPV.
    
- Amplia comunidad de desarrolladores y repositorios de módulos adicionales.

**Impacto práctico:**  
Puedes adaptar Odoo a procesos específicos sin depender del proveedor.

---

#### **2. Módulos independientes y escalables**

Odoo está compuesto por cientos de módulos categorizados:

- Ventas
    
- Inventario
    
- Compras
    
- Contabilidad
    
- Fabricación
    
- Proyecto
    
- Marketing
    
- Sitio web y e-commerce
    
- TPV
    
- CRM
    
- RRHH

Cada módulo agrega funcionalidad inmediatamente y se integra con los demás sin configuraciones complejas.

**Impacto práctico:**  
La empresa empieza con pocos módulos (por ejemplo, Ventas + Inventario) y amplía según necesidad.

---

#### **3. Ideal para aprendizaje**

- Interfaz intuitiva
    
- Arquitectura clara basada en modelos (ORM), vistas y controladores
    
- Permite entender cómo funcionan los sistemas empresariales de forma práctica
    
- Fácil instalación en máquinas virtuales, contenedores o en local

**Impacto práctico:**  
Excelente para realizar prácticas en ciclos formativos o másteres.

---

#### **4. Requisitos de hardware modestos**

- Puede funcionar en un servidor básico o incluso en una máquina virtual local
    
- Compatible con Docker para despliegues rápidos
    
- No necesita infraestructura costosa

**Impacto práctico:**  
Reduce barreras de entrada para PYMEs o estudiantes.

---

### 🔹 Flujo práctico usando Odoo

Odoo permite realizar un flujo empresarial completo sin salir de la plataforma:

```
1. CRM: captación de oportunidad
2. Ventas: creación de presupuesto y pedido
3. Inventario: reserva de stock y preparación de albarán
4. Compras: si falta stock, MRP genera necesidad de compra
5. Producción: orden de fabricación si aplica
6. Logística: envío
7. Facturación: factura automáticamente generada
8. Contabilidad: asiento contable generado
```

Cada paso se registra automáticamente y queda vinculado a los demás.

---

### 🔹 Modalidades Odoo

Odoo ofrece tres modalidades principales:

- **Community (open source)**  
    Gratuita, autoalojada, sin limitaciones de usuarios.
    
- **Odoo Online**  
    Hosting en la nube, mantenimiento automático.  
    Pago por usuario/mes.
    
- **Odoo Enterprise**  
    Despliegue en Odoo.sh o en servidores propios.  
    Funcionalidades avanzadas en contabilidad, fabricación y soporte.

---