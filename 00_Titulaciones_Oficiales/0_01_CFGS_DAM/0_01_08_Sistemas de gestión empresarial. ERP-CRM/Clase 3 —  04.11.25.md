#ERP 

--- 

👨‍🏫 _Profesor: José Luis Sánchez Montejo 
📘 Sistemas de gestión empresarial. ERP-CRM 
🗓 Clase 3 — 04/11/2025 
🎯 Tema: ERP, CRM, SRM, CMS, BI, Odoo 

---

# Sistemas de Gestión Empresarial

---

## 📝 Próximo trabajo: Instalación y uso de Odoo

El próximo trabajo consiste en **instalar Odoo (versión open source)** utilizando una de estas opciones:

- Máquina virtual (recomendado: Ubuntu Server o Desktop)
- Contenedor Docker (más rápido y reproducible)

Tras la instalación, se revisarán:

### ✅ Módulos principales de Odoo
Odoo funciona de forma modular, por lo que se podrán instalar y probar aplicaciones como:

- Ventas  
- Compras  
- Inventario  
- Facturación  
- CRM  
- Proyectos  
- Fabricación  
- RR. HH.  
- Sitio Web / E-commerce  
- TPV (Punto de venta)  
- Marketing / Email Marketing  

![[Pasted image 20251111085104.png]]

Cada módulo se integra automáticamente con los demás y trabaja sobre la misma base de datos.

---

### ✅ Modalidades de pago de Odoo

**1. Odoo Online (Estándar)**  
- Hospedado en la nube de Odoo  
- Todas las aplicaciones disponibles  
- Coste mensual por usuario  

**2. Odoo Personalizado**  
- Odoo.sh o instalación on-premise  
- Multiempresa  
- API externa  
- Acceso a Odoo Studio  

**3. Una aplicación gratuita**  
- Una sola app activa  
- Usuarios ilimitados  
- Hosting limitado  
- Ideal para pruebas

---

### ✅ Próximo ejercicio

Realizar la instalación y posteriormente:

- Activar módulos desde la interfaz de Odoo  
- Crear datos de ejemplo (cliente, proveedor, producto, pedido)  
- Probar el flujo básico de Odoo  
- Ver cómo los módulos interactúan entre sí  

El objetivo es entender cómo un ERP modular integra procesos reales de empresa.


---

## 1️⃣1️⃣ Concepto de ERP

### 🔹 Definición y propósito

Un ERP (**Enterprise Resource Planning**) es un **sistema de gestión empresarial unificado** que conecta y centraliza la información de todos los procesos internos. Cada módulo representa un área funcional, pero todos comparten la **misma base de datos**:

- Ventas y CRM comercial
    
- Compras y proveedores
    
- Inventario y almacenes
    
- Contabilidad y finanzas
    
- Recursos humanos y nóminas
    
- Soporte y atención al cliente
    
- Producción y planificación
    
- Logística, transporte y distribución

El valor real: **todos los departamentos trabajan sobre los mismos datos**, en tiempo real, sin hojas duplicadas ni silos de información.

---

### 🔹 Características clave

- **Procesos orquestados end-to-end**  
    El ERP conecta el flujo operativo completo desde el primer contacto comercial hasta el cobro final.  
    Ejemplo estándar:
    
```
Lead → Presupuesto → Pedido → Fabricación → Albarán/Entrega → Factura → Cobro
```
>No hay saltos a herramientas externas.     Todo queda registrado y validado dentro del sistema.
	
- **Trazabilidad total**  
    Permite rastrear **quién hizo qué, cuándo y cómo**.  
    Desde el lote de una materia prima hasta el historial completo de un cliente.
    
- **Reglas de negocio unificadas**  
    Validaciones, autorizaciones y permisos se manejan de forma central:
    
    - aprobaciones de compras
        
    - límites de crédito
        
    - políticas de descuentos
        
    - auditoría y control interno
        
- **Seguridad y cumplimiento**  
    Gestiona roles, accesos y auditoría para cumplir regulaciones (como contabilidad, trazabilidad, protección de datos).
    
- **Modularidad**  
    La empresa puede activar solo lo que necesita:
    
    - ERP básico
        
    - ERP + CRM
        
    - ERP + producción
        
    - ERP + BI integrado
        
- **Automatización**  
    Notificaciones, alertas, workflows, recordatorios, tareas inteligentes.

---

### 🔹 Finalidad

- **Reducir tiempos operativos**  
    Menos tareas manuales, menos errores.
    
- **Evitar duplicidad**  
    Datos únicos, coherentes y sincronizados.
    
- **Mejorar la coordinación**  
    Ventas sabe lo que hay en stock, compras ve necesidades reales, contabilidad tiene información actualizada.
    
- **Optimizar recursos**  
    Menor inventario inmovilizado, fabricación más eficiente, menor carga administrativa.
    
- **Mejorar el control**  
    KPIs visibles en dashboards, reporting inmediato.

---

### 🔹 Resultado esperado

Un ERP convierte la empresa en un **sistema integrado**, no un conjunto de departamentos aislados.

Resultados típicos:

- Visión global y en tiempo real del negocio.
    
- Reducción del coste operativo por automatización.
    
- Decisiones más rápidas y con datos fiables.
    
- Mejora de la productividad y del servicio al cliente.
    
- Menor riesgo de errores, retrasos o falta de control.

---

## 1️⃣2️⃣ Beneficios de un ERP

- Unificación de procesos.
- Organización eficiente de la información.
- Eliminación de datos duplicados.
- Información fiable y actualizada.
- Acceso oportuno a datos críticos.
- Mejora del análisis y la toma de decisiones.
- Reducción de errores y operaciones innecesarias.
- Reducción de costes y tiempos.

---

## 1️⃣3️⃣ Cómo encajan ERP, CRM, SRM, CMS y BI

Piensa en la empresa como un sistema de **flujos de información**. Cada plataforma cubre un bloque distinto y se conecta a las otras.

### ERP — Núcleo transaccional

Gestiona toda la información **estructural y operativa**.  
Cada clic genera un registro contable, de inventario o de producción.

Operaciones típicas:

- Crear un pedido de venta → reserva de stock
    
- Confirmar orden de compra → actualización de previsiones MRP
    
- Registrar entrada de almacén → movimiento y coste
    
- Emitir factura → asiento contable
    

Propiedades técnicas:

- Arquitectura **OLTP** (ver más abajo)
    
- Transacciones ACID
    
- Permisos y workflows controlados
    
- Auditoría y logs internos
    

---

### CRM — Relación comercial

Procesa todo lo que pasa **antes**, **durante** y **después** de la venta, pero sin tocar contabilidad ni inventario.

Ejemplos:

- Lead capturado desde formulario web
    
- Llamada registrada con resultado
    
- Seguimiento de oportunidad con etapas
    
- Envío de presupuesto
    
- Gestión de incidencias y tickets
    

El CRM decide “**qué** vender, a **quién** y **cuándo**”.  
El ERP ejecuta “**cómo** se vende” y “**cuánto** se factura”.

---

### SRM — Relación con proveedores

Procesa todo lo que ocurre desde el punto de vista del proveedor, no del cliente.

Funciones:

- Evaluación de proveedores
    
- Gestión de contratos
    
- Indicadores de cumplimiento (entregas, calidad, retrasos)
    
- Peticiones de oferta (RFQ)
    
- Negociación de precios
    

Vinculación con ERP:

- En el SRM se decide con quién trabajar
    
- En el ERP se ejecutan las órdenes de compra reales
    

---

### BI — Capa analítica

No opera. Analiza.

Herramientas típicas:

- Power BI
    
- Tableau
    
- Qlik Sense
    
- Looker
    

Consume datos desde:

- ERP
    
- CRM
    
- SRM
    
- CMS
    
- Archivos externos (Excel, CSV, APIs)
    

Produce:

- Dashboards
    
- KPIs
    
- Informes automáticos
    
- Alertas
    

---

### CMS — Gestión de contenido

Exposición al cliente final vía web.

Publicado desde CMS:

- Fichas de producto
    
- Blog corporativo
    
- Páginas de marca
    
- Landing pages
    
- Catálogos digitales
    

No controla inventario ni facturación.  
Cuando hay e-commerce, actúa como **front-end** y delega en el ERP el back-end transaccional.

---

## 1️⃣4️⃣ Características de un ERP

### 🔹 Integrales

Un único flujo desde el origen hasta el impacto contable.  

Elimina islas de información.

Cadena típica de trazabilidad:

```markdown
1. Lead generado en CRM
2. Oportunidad cerrada → Pedido de venta (ERP)
3. Validación de stock
4. Planificación producción (MRP)
5. Orden de fabricación
6. Recepción y control de calidad
7. Salida de almacén
8. Entrega
9. Factura
10. Contabilización automática
11. Cierre de periodo
```

Antes del ERP esto era un caos de hojas Excel, emails, llamadas y archivos sueltos.

---

### 🔹 Adaptables

Concepto técnico: **parametrización**.  
No se programa, se configura.

Capas de configuración:

1. Parámetros contables
    
2. Flujo de documentos
    
3. Impuestos y retenciones
    
4. Plantillas de coste
    
5. Rutas logísticas
    
6. Perfiles de usuario

Esto permite usar el mismo ERP en:

- tiendas pequeñas
    
- pymes industriales
    
- multinacionales

---

## 1️⃣5️⃣ Qué integra un ERP

### Procesos Internos (visión operativa)

- **Ventas:** pedidos, devoluciones, contratos, descuentos
    
- **Compras:** solicitudes, órdenes, recepción, incidencias
    
- **Producción:** MRP, BOM, planificación, escandallos
    
- **Inventario:** lotes, ubicaciones, picking, FIFO/FEFO
    
- **Calidad:** inspecciones, no conformidades
    
- **Logística:** expediciones, transportistas, tracking

### Capas y relaciones (visión estratégica)

- BI: análisis
    
- KM: base documental interna
    
- PRM: red de socios/distribuidores
    
- PLM: ingeniería del producto

---

## 1️⃣6️⃣ Data Warehouse

Un **DW** es un entorno optimizado para análisis, no para procesos diarios.

### 🔹 Arquitectura básica: ETL/ELT

1. **E**xtract: se extraen datos del ERP/CRM/SRM/CMS
    
2. **T**ransform: limpieza, normalización, agregación
    
3. **L**oad: carga en el DW

O, en arquitecturas modernas, ELT:

- Se cargan datos brutos
    
- Se transforman dentro del DW (con SQL, dbt, engine interno)

---

### 🔹 OLTP vs OLAP

OLTP y OLAP son dos modelos diseñados para **objetivos radicalmente distintos**. Explico cada punto con precisión y lógica técnica.

![[Pasted image 20251111093947.png]]

---

####  OLTP (On-Line Transaction Processing) — típico del ERP

**Qué es:**  
Sistema pensado para **registrar operaciones del día a día**. Todo lo que hace un usuario genera una transacción pequeña, inmediata, crítica.

##### Características explicadas

- **Transaccional**  
    El foco está en asegurar que operaciones como “crear pedido”, “actualizar stock”, “registrar factura” se ejecuten correctamente y sin errores.
    
- **Tablas normalizadas**  
    Bases de datos con diseño riguroso (3FN o superior).  
    Se evita duplicación de datos.  
    Ejemplo: productos, clientes, almacenes, stock en tablas separadas.
    
- **Operaciones rápidas y cortas**  
    Consultas muy específicas:
    
```
Dame el stock actual del producto X.
```
    
    Deben responder en milisegundos.
    
- **ACID**  
    Garantías de consistencia:
    
    - **A**tomicidad: la operación se hace o no se hace
        
    - **C**onsistencia: la BD queda en un estado válido
        
    - **I**solación: transacciones no se pisan
        
    - **D**urabilidad: si se escribe, se persiste
        
- **Actualizaciones minuto a minuto**  
    Alguien modifica un pedido, otro actualiza un pago…  
    Todo entra en tiempo real.

---

####  OLAP (On-Line Analytical Processing) — típico del Data Warehouse

**Qué es:**  
Sistema optimizado para **análisis, informes y decisiones**, no para registrar operaciones del día a día.

##### Características explicadas

- **Analítico**  
    No ejecuta ventas ni compras.  
    Se usa para entender tendencias, patrones, rendimiento.
    
- **Estructuras desnormalizadas**  
    Tablas grandes, “anchas”, diseñadas para agrupar datos fácilmente.  
    Modelos estrella (_star schema_) o copo de nieve (_snowflake schema_).
    
- **Consultas pesadas**  
    Búsquedas que analizan millones de filas:
    
```
Ventas totales por región entre 2015 y 2024
segmentado por categoría de producto
y comparado con el forecast.
```
    
- **Análisis multidimensional**  
    Dimensiones clásicas:
    
    - tiempo
        
    - cliente
        
    - producto
        
    - región
        
    - canal
    
    Permite ver datos desde múltiples ángulos sin  reescribir consultas complejas.
    
- **Datos históricos**  
    Guarda _años_ de información consolidada.  
    El ERP no debe almacenar ni consultar tanto  volumen porque se degrada su rendimiento.

---

####  Resumen lógico

|Característica|OLTP (ERP)|OLAP (DW)|
|---|---|---|
|Objetivo|Operaciones diarias|Análisis estratégico|
|Diseño|Normalizado|Desnormalizado|
|Rendimiento|Millones de transacciones pequeñas|Calcular grandes agregaciones|
|Tipo de consultas|Cortas, exactas|Largas, complejas|
|Datos|Actualizados|Históricos agregados|
|Usuario típico|Administrativo, ventas, almacén|Direcciones, analistas, BI|

---
#### Ejemplo:

**OLTP (ERP):**

```sql
SELECT stock_actual FROM inventario WHERE id_producto=123;
```

**OLAP (DW):**

```sql
SELECT SUM(ventas) 
FROM cubo_ventas 
WHERE producto=123 AND año BETWEEN 2020 AND 2024
GROUP BY mes;
```
---

### 🔹 Modelado dimensional (star schema)

DW usa:

- **Tabla de hechos**: ventas, stock, producción
    
- **Tablas de dimensiones**: cliente, producto, tiempo, zona

Esto permite análisis multidimensional:

```nginx
ventas por → producto → mes → región → canal
```

---

### 🔹 Beneficios reales del DW

- Evita “romper” el ERP con consultas pesadas
    
- Analiza datos de múltiples sistemas
    
- Mantiene el histórico (años)
    
- Facilita BI y planificación estratégica
    
- Prepara terreno para algoritmos de predicción

---

## 🧪 Test – Preguntas, respuestas y justificación

---

### ✅ Pregunta 1  
**¿Qué función principal cumple un sistema ERP dentro de una empresa?**

- A. Controlar únicamente las ventas y clientes.  
- **B. Integrar y automatizar los procesos internos en una base de datos única.**  
- C. Crear contenido web y catálogos.  
- D. Analizar tendencias de mercado externas.

**Respuesta correcta: B**  
**Justificación:** Un ERP integra todos los módulos operativos y centraliza la información en una sola base de datos para automatizar procesos.

---

### ✅ Pregunta 2  
**¿Qué módulo del ERP registra pedidos, albaranes y facturas conectados al stock?**

- A. Compras  
- B. Finanzas  
- **C. Ventas**  
- D. Proyectos  

**Respuesta correcta: C**  
**Justificación:** El módulo de ventas cubre el flujo completo: pedido → albarán → factura, siempre conectado con inventario y cobros.

---

### ✅ Pregunta 3  
**¿Cuál de los siguientes sistemas está más orientado al análisis y toma de decisiones?**

- A. ERP  
- B. CRM  
- **C. BI**  
- D. SRM  

**Respuesta correcta: C**  
**Justificación:** BI transforma datos operativos en inteligencia estratégica mediante dashboards y KPIs.

---

### ✅ Pregunta 4  
**¿Qué ventaja ofrece un ERP respecto a trabajar con múltiples sistemas aislados?**

- A. Mayor personalización en cada departamento  
- **B. Eliminación de duplicidades y mayor trazabilidad**  
- C. Procesos independientes  
- D. Menor necesidad de formación  

**Respuesta correcta: B**  
**Justificación:** El ERP unifica datos y procesos, eliminando duplicados y asegurando seguimiento completo.

---

### ✅ Pregunta 5  
**¿Qué rol cumple el Data Warehouse dentro de una arquitectura empresarial?**

- A. Procesar pedidos en tiempo real  
- B. Gestionar relaciones con clientes  
- **C. Centralizar datos históricos para análisis y toma de decisiones**  
- D. Controlar stock e inventario  

**Respuesta correcta: C**  
**Justificación:** El Data Warehouse está diseñado para análisis avanzado, no para operativa diaria.

---

### ✅ Pregunta 6  
**¿A qué corresponde la siguiente definición?  
“Un software que permite guardar todas las interacciones entre los clientes y la empresa en una única base de datos”**

- A. ERP  
- **B. CRM**  
- C. BI  
- D. SRM

**Respuesta correcta: B**  
**Justificación:** CRM centraliza toda interacción con clientes: llamadas, emails, oportunidades, incidencias, ventas y posventa.

---

### ✅ Pregunta 7  
**El CMS de tipo “Headless” se caracteriza por…**

- A. Integrar directamente la base de datos con el TPV  
- **B. Separar el backend del frontend y ofrecer contenido mediante API**  
- C. Gestionar clientes en tiempo real  
- D. Requerir conocimientos de contabilidad  

**Respuesta correcta: B**  
**Justificación:** Un CMS headless almacena contenido y lo expone mediante API para que distintos frontends lo consuman (web/app).

---

### ✅ Pregunta 8  
**El SRM (Supplier Relationship Management) gestiona principalmente…**

- A. Relaciones con clientes  
- **B. Relaciones con proveedores**  
- C. Publicación de contenido web  
- D. Análisis de ventas  

**Respuesta correcta: B**  
**Justificación:** SRM evalúa, controla y gestiona todo lo relacionado con proveedores (contratos, pedidos, desempeño).

---

### ✅ Pregunta 9  
**¿Cuál de los siguientes sistemas se utiliza para publicar contenido sin programar?**

- A. ERP  
- B. CRM  
- **C. CMS**  
- D. BI  

**Respuesta correcta: C**  
**Justificación:** CMS (Content Management System) permite crear y editar páginas, blogs y catálogos sin necesidad de código.

---

### ✅ Pregunta 10  
**El término OLTP hace referencia a…**

- A. Procesamiento analítico orientado a históricos  
- **B. Procesamiento transaccional en tiempo real**  
- C. Integración de datos procedentes de múltiples fuentes  
- D. Modelado de datos multidimensional  

**Respuesta correcta: B**  
**Justificación:** OLTP gestiona operaciones rápidas y actualiza datos instantáneamente (pedidos, cobros, stock).

---

### ✅ Pregunta 11  
**¿Qué diferencia principal existe entre OLTP y OLAP?**

- A. OLTP es para análisis y OLAP para transacciones  
- B. Ambos se utilizan únicamente en BI  
- **C. OLTP procesa operaciones diarias; OLAP analiza información histórica**  
- D. OLAP requiere más velocidad que OLTP  

**Respuesta correcta: C**  
**Justificación:** OLTP → tiempo real; OLAP → análisis histórico multidimensional.

---

### ✅ Pregunta 12  
**Un Data Warehouse se caracteriza por…**

- A. Almacenar sólo los datos del día actual  
- **B. Integrar información de distintos sistemas para análisis estratégico**  
- C. Sustituir la base de datos del ERP  
- D. Generar automáticamente facturas  

**Respuesta correcta: B**  
**Justificación:** El DW centraliza datos de ERP/CRM/CMS para análisis avanzado y dashboards.

---

### ✅ Pregunta 13  
**¿Cuál de las siguientes afirmaciones es correcta respecto a un CRM?**

- **A. Se centra en el seguimiento y gestión de las relaciones con los clientes**  
- B. Su objetivo principal es analizar datos financieros  
- C. Sustituye al ERP en compras  
- D. Sólo se utiliza en grandes empresas  

**Respuesta correcta: A**  
**Justificación:** CRM gestiona contactos, oportunidades, tareas comerciales y posventa.

---

### ✅ Pregunta 14  
**De las siguientes afirmaciones, indica cuál supone una desventaja para un ERP:**

- A. Estandarización e integración de información  
- **B. Costes de licencias**  
- C. Mayor control organizacional  
- D. Minimiza el tiempo de análisis  

**Respuesta correcta: B**  
**Justificación:** Licencias, implantación, formación y mantenimiento suponen costes elevados.

---

### ✅ Pregunta 15  
**En general, un ERP contiene un CRM.**

- **A. Verdadero**  
- B. Falso

**Respuesta correcta: A**  
**Justificación:** La mayoría de ERP modernos son modulares e incluyen un módulo CRM para gestionar el ciclo comercial sobre la misma base de datos.  

*Matiz:* No todos lo incluyen. Algunos ERP integran un CRM externo mediante API.

---

### ✅ Pregunta 16  
**¿Cuál es la afirmación INCORRECTA? Un ERP…**

- A. Permite la optimización de los procesos empresariales  
- **B. Solo es útil para grandes empresas**  
- C. Está formado por diferentes módulos  
- D. Reduce el tiempo y los costes de los procesos  

**Respuesta correcta: B**  
**Justificación:** Hoy existen ERP accesibles a microempresas y PYMEs. Las demás opciones describen ventajas reales de un ERP.

---

### ✅ Pregunta 17  
**La diferencia entre los ERP y los CRM es:**

- A. Los CRM gestionan la información orientada exclusivamente a las compras  
- **B. Los CRM gestionan la información orientada exclusivamente a las ventas**  
- C. Los CRM gestionan la información orientada exclusivamente a los pedidos  
- D. Los CRM gestionan la información orientada exclusivamente a las nóminas  

**Respuesta correcta: B**  
**Justificación:** CRM se centra en la relación comercial con clientes: marketing → leads → oportunidades → ventas → posventa.

---


