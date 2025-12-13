#ERP #ODOO

--- 

👨‍🏫 _Profesor: José Luis Sánchez Montejo 
📘 Sistemas de gestión empresarial. ERP-CRM 
🗓 Clase 5 — 02/12/2025 
🎯 Tema: ODOO (Licencias, SaaS, Odoo.sh y On-Premise)

---
# **1️⃣ Introducción y contextualización**

En esta clase se profundiza en Odoo desde una perspectiva funcional, tecnológica y estratégica. El objetivo principal es entender **qué es Odoo dentro del ecosistema ERP/CRM**, cómo se organiza en módulos, qué tipos de instalación existen y cómo estas elecciones afectan a empresas reales según sus necesidades.

Odoo destaca entre los ERP modernos no solo por su modularidad y diseño, sino porque combina tres elementos poco comunes juntos:

1. **Código abierto (LGPL)** → accesible, auditable y modificable.
    
2. **Arquitectura modular** → permite crecer por partes, según necesidades.
    
3. **Flexibilidad de despliegue** → SaaS, PaaS, On-Premise o infraestructura propia.
    

Estas tres características permiten que Odoo se adapte tanto a una micropymes como a grandes empresas con procesos complejos.

---

# **1.1 ¿Qué es Odoo?**

Odoo es un **ERP modular y extensible** orientado a cubrir todas las áreas de la empresa bajo una sola plataforma integrada: ventas, compras, contabilidad, inventario, proyectos, marketing, RRHH, web, fabricación, comercio electrónico y más.

Cada área se gestiona mediante un **módulo especializado**, pero todos comparten la misma base de datos. Esto significa que:

- un pedido de la web actualiza automáticamente el inventario,
    
- ese movimiento genera asientos contables,
    
- el equipo comercial ve la venta en el CRM,
    
- el proyecto asociado puede iniciarse automáticamente.
    

Odoo ofrece algo muy valioso: **información unificada** y procesos conectados sin integraciones externas complejas.

### ¿Por qué es tan popular?

- Permite una implantación progresiva.
    
- La interfaz es moderna y usable.
    
- Su ecosistema de módulos crece cada año.
    
- La comunidad global aporta mejoras constantes.
    
- Su coste total de propiedad es menor que el de SAP o Dynamics.
    

---

# **1.2 Evolución de Odoo**

La historia de Odoo ayuda a entender por qué es tan flexible:

- **2005: TinyERP** → ERP básico, modular.
    
- **2009: OpenERP** → salto al modelo de “framework empresarial”.
    
- **2014: Odoo** → integración de apps modernas: web, e-commerce, marketing, POS.
    
- **Actualidad** → más de 7 millones de usuarios en 120+ países.
    

Odoo se ha convertido en el **ERP de código abierto más influyente del mundo**, hasta el punto de competir directamente con soluciones privativas corporativas.

Además, conviven dos versiones:

- **Odoo Community (LGPL)** → libre, modificable y gratuita.
    
- **Odoo Enterprise (privativa)** → con funcionalidades premium, soporte y servicios adicionales.
    

---

# **1.3 Planes y precios**

La clase compara los planes oficiales de Odoo Online (SaaS):

### **Plan Gratuito**

- Una única aplicación.
    
- Base de datos alojada en la nube de Odoo.
    
- Usuarios ilimitados.
    
- Ideal para pequeñas empresas o pruebas iniciales.
    
- Limitaciones: **solo una app**, no se permiten instalaciones adicionales.
    

### **Plan Estándar**

- Todas las aplicaciones disponibles.
    
- Base de datos en la nube (SaaS).
    
- Precio por usuario/mes.
    
- Es el plan más extendido: económico y sin necesidad de infraestructura propia.
    

### **Plan Personalizado**

- Todas las apps + Odoo Studio + multicompañía + API externa.
    
- Permite Odoo Online, Odoo.sh o instalación On-Premise.
    
- Enfocado a empresas grandes o con múltiples sociedades.
    
- Permite arquitecturas híbridas y automatizaciones avanzadas.
    

---

# **2️⃣ Módulos disponibles en Odoo**

Odoo organiza todas sus funcionalidades en módulos. Cada módulo es una pieza independiente del sistema que:

- se instala o desinstala según necesidades,
    
- se integra con otros módulos,
    
- puede extenderse mediante otros addons.
    

Los módulos principales suelen categorizarse así:

### **Área comercial**

- CRM
    
- Ventas
    
- Suscripciones
    
- Punto de venta (POS)
    

### **Área financiera**

- Contabilidad
    
- Facturación
    
- Gestión de gastos
    

### **Área logística**

- Inventario
    
- Compras
    
- Fabricación (MRP)
    

### **Área de RRHH**

- Empleados
    
- Asistencias
    
- Horarios
    
- Reclutamiento
    

### **Área digital**

- Sitio web
    
- E-commerce
    
- Blogs
    
- Email marketing
    
- Redes sociales
    

### **Área de proyectos**

- Gestión de proyectos
    
- Tareas
    
- Tickets
    
- Servicios (Field Service)
    

Cada módulo añade vistas, modelos, lógica business y automatizaciones que enriquecen la base de datos común.

---

# **3️⃣ Posibilidades de instalación y uso**

Aquí entra la parte más importante de la clase: **cómo se puede instalar Odoo y qué implica cada opción**.

Existen cuatro modalidades:

---

# **3.1 Odoo Online (SaaS)**

Es la forma más sencilla de usar Odoo. Todo está gestionado en la nube de la propia empresa Odoo.

### Ventajas

- Sin servidores ni mantenimiento.
    
- Actualizaciones automáticas.
    
- Alta disponibilidad.
    
- Seguridad gestionada por Odoo.
    
- Ideal para empresas sin equipo técnico.
    

### Limitaciones

- No permite instalar módulos personalizados*.
    
- No se puede modificar el código.
    
- Integraciones externas limitadas.
    

* Excepto mediante el plan Personalizado con API y Odoo Studio (pero sigue siendo muy limitado comparado con On-Premise).

### Para quién es

Startups, micropymes, negocios sin recursos técnicos.

---

# **3.2 Odoo.sh (PaaS)**

Es la plataforma de hosting oficial de Odoo, basada en GitHub.  
Es un punto intermedio entre SaaS y On-Premise.

### Ventajas

- Permite módulos personalizados.
    
- Entornos de staging y producción automáticos.
    
- Integración continua con GitHub.
    
- Backups automatizados.
    
- Alto rendimiento.
    

### Limitaciones

- Coste adicional a las licencias.
    
- Dependencia del ecosistema de Odoo.
    
- Menos libertad que instalarlo tú mismo.
    

### Para quién es

Empresas con desarrollos propios que quieren facilidad de despliegue.

---

# **3.3 Odoo On-Premise**

Consiste en instalar Odoo en tus propios servidores (locales o cloud).  
Es la modalidad con **mayor control y flexibilidad**.

### Ventajas

- Acceso total al código.
    
- Puedes instalar cualquier módulo de terceros.
    
- Integraciones ilimitadas.
    
- Control de seguridad, backup y actualizaciones.
    
- Coste bajo si usas Odoo Community.
    

### Limitaciones

- Necesitas equipo técnico.
    
- Mantener servidores, actualizaciones y seguridad.
    
- Requiere más planificación.
    

### Para quién es

Empresas medianas y grandes con procesos complejos o personalización profunda.

---

# **3.4 Instalar Odoo en un servidor en la nube (IaaS/VM)**

Es la variante moderna de On-Premise: en lugar de tener un servidor físico, usas una máquina virtual en:

- AWS
    
- Azure
    
- Google Cloud
    
- OVH
    
- Hetzner
    
- Contabo
    
- etc.
    

### Ventajas

- Escalable (añadir CPU, RAM, almacenamiento).
    
- Más barato que servidores físicos.
    
- Backups y snapshots automáticos.
    
- Compatible con Docker, Kubernetes y arquitecturas avanzadas.
    

### Desventajas

- Necesitas administrador de sistemas o partner.
    

---

# **4️⃣ Demostraciones vistas en clase (pantallas del profesor)**

La clase incluyó ejemplos reales de:

### **✔ Paneles de Power BI conectados a Odoo**

- Tablas relacionales
    
- Modelos de relaciones
    
- Filtros por provincia, proyecto, género, zonas desfavorecidas
    
- Dashboards con indicadores visuales
    

Esto demuestra la potencia de Odoo como base de datos empresarial.

### **✔ Aplicaciones de Odoo en uso real**

- Registro de usuarios mediante terminal RFID
    
- Ventas: creación de presupuestos y envío al cliente
    
- Sitio web: plantilla, catálogo, blog, e-commerce
    

Estas demos sirven para visualizar cómo Odoo integra ERP + CRM + Web + BI en un solo ecosistema.

---

# **5️⃣ Comparativa detallada de despliegues: PC personal, servidor local y servidor en la nube**

Una vez vistas las modalidades, en clase se profundiza en **cómo cambia realmente Odoo** según dónde se instale. No es una decisión trivial: afecta a la seguridad, mantenimiento, rendimiento y coste total del sistema.

La comparación se centra en tres escenarios reales:

- instalar Odoo en un PC personal,
    
- instalarlo en un servidor local de la empresa,
    
- o instalarlo en un servidor en la nube (VM/IaaS).
    

---

## **5.1 Odoo instalado en un PC personal (NO recomendable para producción)**

Esta opción aparece en clase como ejemplo de _“lo que NO se debe hacer”_.  
Es útil en formación, pruebas o entornos educativos, pero NO en empresas reales.

**Limitaciones severas:**

- **Disponibilidad nula:** si el usuario apaga el PC, se apaga el ERP.
    
- **Riesgo crítico de datos:** si se rompe el disco, la empresa se queda sin contabilidad, facturas, inventario…
    
- **Seguridad mínima:** sin firewall dedicado, sin aislamiento, sin políticas de backup.
    
- **Rendimiento insuficiente:** no está pensado para multiusuario, procesos de inventario o informes pesados.
    
- **Imposible cumplir RGPD:** datos sensibles en un ordenador personal es un riesgo legal.
    

**Conclusión:**  
Solo válido para aprender. Nunca para una pyme real.

---

## **5.2 Odoo en un servidor local de la empresa (On-Premise clásico)**

Es la modalidad tradicional: un servidor físico dentro de la empresa (sala de servidores, SAI, red estable, backups internos…).

### **Qué es y para qué sirve**

Permite que los usuarios de oficina, taller o planta accedan al ERP con **latencia mínima**, integración directa con dispositivos físicos (lectores, etiquetadoras, maquinaria…) y control total sobre los datos.

### **Por qué muchas pymes lo eligen**

- **Datos bajo tu techo:** para empresas que no quieren subir datos a Internet.
    
- **Latencia muy baja en LAN:** imprescindible en entornos industriales o logísticos.
    
- **Integración con hardware local:** impresoras industriales, básculas, terminales RFID.
    
- **Control de cambios:** la empresa decide cuándo actualizar y cómo.
    

### **Costes y obligaciones que casi nadie cuenta al principio**

- **Coste inicial:** servidor, SAI, racks, switches, climatización, discos.
    
- **Mantenimiento constante:** parches, backups fuera del edificio, pruebas periódicas.
    
- **Disponibilidad:** si hay inundación o corte eléctrico largo → _todo cae_.
    
- **Acceso remoto:** requiere montar VPN o Zero-Trust.
    
- **Equipo de TI:** no basta con un informático “generalista”; se necesita alguien que entienda de Linux, bases de datos, seguridad y monitorización.
    

### **Cuándo tiene sentido**

- Pymes industriales.
    
- Talleres, almacenes o plantas con hardware local.
    
- Empresas con política estricta de datos internos.
    

---

## **5.3 Odoo en un servidor en la nube (IaaS/VM)**

Aunque sigue siendo un despliegue _On-Premise_ (porque sigues gestionando la máquina), se diferencia del servidor físico en que se ejecuta sobre una VM en un proveedor cloud.

### **Ventajas que se notan en el día a día**

- **Alta disponibilidad:** la nube tiene redundancia nativa.
    
- **Snapshots y restauración rápida:** volver a un estado anterior en segundos.
    
- **Escalabilidad:** si necesitas más CPU o RAM, lo aumentas en minutos.
    
- **Acceso global:** sin necesidad de VPN compleja (aunque es recomendable para administración).
    
- **Backups y monitorización integradas:** muchos clouds añaden copias programadas.
    

### **Cuándo brilla especialmente**

- Pymes multisede.
    
- Empresas con teletrabajo habitual.
    
- Proyectos que crecerán en usuarios, informes o módulos.
    
- Empresas que no quieren invertir en un servidor físico.
    

### **Desventajas**

- Coste mensual recurrente.
    
- Dependencia del proveedor cloud.
    
- Requiere administrador de sistemas.
    

---

# **6️⃣ Dimensionamiento y requisitos: ¿qué máquina pedir?**

El profesor recalca aquí algo muy práctico:  
**no se elige un servidor por intuición**, sino por número de usuarios concurrentes, uso real de módulos, carga de informes y tamaño de inventario.

Guía mental de la clase:

### **Pruebas o uso individual (1–3 usuarios esporádicos)**

- 2 vCPU
    
- 4–8 GB RAM
    
- Disco 40–60 GB SSD  
    Sirve para “ver Odoo” o trabajar con pocos datos.
    

---

### **Pyme pequeña (10–20 usuarios mixtos, uso moderado)**

- 4 vCPU
    
- 8–16 GB RAM
    
- Disco 100–200 GB  
    Aquí ya conviene:
    
- separar datos de pruebas,
    
- backups diarios,
    
- dominio + HTTPS.
    

---

### **Pyme mediana (30–60 usuarios, varios módulos, informes pesados)**

- 8 vCPU
    
- 16–32 GB RAM
    
- Disco 200–500 GB (con retención de copias)
    

Aquí se vuelve crucial la **planificación de capacidad** y la **monitorización**.

---

### **Más de 60 usuarios o picos intensivos**

Entramos en el terreno de:

- alta disponibilidad,
    
- separación de servicios (app + base de datos),
    
- políticas estrictas de auditoría,
    
- redundancia.
    

Este tipo de despliegues se ven en cursos avanzados.

---

# **7️⃣ Licencias, libertad y control**

La clase introduce una idea clave: la relación entre **lo que la empresa puede hacer** y **el control que ejerce el proveedor**.

El espectro queda así:

**GPL → AGPL → LGPL → MIT/BSD → Freeware → Shareware**

- A la izquierda: más libertad técnica.
    
- A la derecha: más control del proveedor.
    

Esto sirve para entender:

- qué puedes modificar,
    
- qué puedes redistribuir,
    
- qué puedes integrar,
    
- qué puedes automatizar.
    

---

# **8️⃣ Software libre vs Open Source vs Software propietario**

### **8.1 Software libre**

Cumple las 4 libertades (usar, estudiar, modificar, redistribuir).

Ejemplos: Linux, LibreOffice, Odoo Community.

### **8.2 Open Source**

Código accesible, filosofía pragmática: más calidad, menos bugs.

Ejemplos: MySQL, VS Code, Android (parte libre).

### **8.3 Software propietario**

Código cerrado → solo licencia de uso.

Ejemplos: SAP, Microsoft Dynamics, Salesforce, Odoo Enterprise.

---

# **9️⃣ Odoo Community vs Odoo Enterprise**

### **Odoo Community**

- Licencia LGPLv3
    
- Gratuita
    
- Código abierto
    
- Permite módulos propios
    
- Ideal para desarrollos a medida
    

### **Odoo Enterprise**

- Licencia privativa
    
- Funciones premium
    
- Requiere contrato
    
- Soporte oficial
    
- NO permite copiar código (ni siquiera si lo ves en clase)
    

---

# **🔟 Por qué no se puede copiar código de Odoo Enterprise**

El profesor remarca un punto legal importante:

- El código Enterprise es **propiedad intelectual de Odoo S.A.**
    
- Verlo en clase **no da derecho a copiarlo**.
    
- No puede usarse en proyectos propios.
    
- Es equivalente a copiar módulos de pago de SAP, Dynamics o Salesforce.
    

---

#  📝 Test — Preguntas, respuestas y justificación

---

## ✅ **Pregunta 1**

**¿Cuál de estos factores NO se menciona como clave del éxito de Odoo frente a otros ERP?**

A. Naturaleza modular  
B. Código abierto  
C. Flexibilidad de instalación  
D. Uso exclusivo en entornos Windows

**Respuesta correcta: D**

**Justificación:**  
Odoo destaca por su modularidad, su modelo abierto y su flexibilidad de despliegue.  
Sin embargo, **no es exclusivo de Windows**; de hecho, su base es Linux y funciona en múltiples entornos. Por tanto, la opción D no forma parte de los factores clave.

---

## ✅ **Pregunta 2**

**¿Qué característica distingue a Odoo respecto a ERP “clásicos”?**

A. Que solo gestiona contabilidad  
B. Que combina potencia corporativa con una interfaz moderna y usable  
C. Que no tiene versión de pago  
D. Que no dispone de módulos de comunidad

**Respuesta correcta: B**

**Justificación:**  
Odoo destaca por mezclar un backend potente propio de ERP profesionales con una interfaz moderna, intuitiva y fácil de usar. Esa combinación es precisamente lo que lo separa de los ERP tradicionales más rígidos y anticuados.

---

## ✅ **Pregunta 3**

**En Odoo, ¿qué implica que todos los módulos compartan una única base de datos?**

A. Que cada módulo debe instalar su propio PostgreSQL  
B. Que las operaciones en un módulo impactan automáticamente en otros procesos relacionados  
C. Que no se puede hacer copia de seguridad parcial  
D. Que no es posible desinstalar módulos

**Respuesta correcta: B**

**Justificación:**  
La integración total permite que cualquier acción (venta, inventario, contabilidad…) se propague automáticamente al resto del sistema gracias a la **base de datos unificada**. Es el corazón del funcionamiento de Odoo.

---

## ✅ **Pregunta 4**

**¿Cuál es la diferencia de licencia entre Odoo Community y Odoo Enterprise?**

A. Community es GPL y Enterprise es MIT  
B. Community es LGPL y Enterprise es comercial con soporte oficial  
C. Ambas son Apache 2.0  
D. Enterprise es totalmente gratuita

**Respuesta correcta: B**

**Justificación:**  
Odoo Community se publica con **licencia LGPLv3**, permitiendo uso libre y modificación.  
Odoo Enterprise es **software privativo**, requiere contrato y ofrece funcionalidades premium y soporte oficial.

---

## ✅ **Pregunta 5**

**¿Qué modalidad de Odoo se describe como SaaS puro, donde el cliente solo usa el navegador y Odoo se encarga de todo lo técnico?**

A. Odoo On-Premise  
B. Odoo.sh  
C. Odoo Online  
D. Odoo Local Server

**Respuesta correcta: C**

**Justificación:**  
Odoo Online es el servicio SaaS oficial: Odoo se encarga del hosting, seguridad, actualizaciones y disponibilidad. El cliente solo navega y utiliza el sistema.

---

## ✅ **Pregunta 6**

**¿Cuál es una limitación clave de Odoo Online según el texto?**

A. No permite multiempresa  
B. No soporta base de datos PostgreSQL  
C. No permite instalar módulos personalizados ni de terceros  
D. No se puede acceder desde móvil

**Respuesta correcta: C**

**Justificación:**  
Odoo Online bloquea la instalación de módulos externos o personalizados. Solo permite usar las aplicaciones oficiales del ecosistema SaaS.

---

## ✅ **Pregunta 7**

**¿Qué ventaja se destaca de Odoo Online respecto a un ERP propietario tradicional instalado on-premise?**

A. Permite más personalización que cualquier otra opción  
B. No requiere ningún tipo de configuración inicial  
C. Tiene un coste de entrada mucho más bajo y predecible para pymes  
D. No necesita conexión a Internet

**Respuesta correcta: C**

**Justificación:**  
Odoo Online reduce los costes iniciales al eliminar infraestructura, instalación y mantenimiento. Esto lo convierte en una opción accesible para pymes.

---

## ✅ **Pregunta 8**

**¿Por qué motivo una empresa que empieza en Odoo Online podría verse obligada a migrar a Odoo.sh?**

A. Porque Odoo Online no soporta multiusuario  
B. Porque necesita desarrollar módulos a medida o usar módulos Community  
C. Porque Odoo Online no permite facturar  
D. Porque Odoo.sh es más barato en todos los casos

**Respuesta correcta: B**

**Justificación:**  
Odoo Online **bloquea módulos personalizados**.  
Si una empresa necesita desarrollos a medida o módulos Community, debe migrar a Odoo.sh o a On-Premise.

---

## ✅ **Pregunta 9**

**¿Qué afirmación describe mejor a Odoo.sh según el documento?**

A. Es un hosting compartido sin integración con herramientas de desarrollo  
B. Es un PaaS gestionado por Odoo que integra GitHub, entornos dev/staging/prod y despliegues automáticos  
C. Es simplemente un servidor dedicado en la nube sin servicios añadidos  
D. Es la versión gratuita de Odoo Enterprise

**Respuesta correcta: B**

**Justificación:**  
Odoo.sh es una plataforma gestionada por Odoo con integración directa con GitHub, automatización de despliegues y entornos profesionales de desarrollo.

---

## ✅ **Pregunta 10**

**¿Por qué motivo instalar Odoo en el PC personal de un usuario NO se considera adecuado para producción?**

A. Porque no permite más de un módulo  
B. Porque no soporta PostgreSQL  
C. Por nula disponibilidad, riesgo de datos, problemas de seguridad y baja capacidad multiusuario  
D. Porque Odoo no funciona en Windows

**Respuesta correcta: C**

**Justificación:**  
Un PC personal no garantiza seguridad, disponibilidad, backups ni rendimiento multiusuario. Es totalmente inadecuado para entornos productivos.

---

## ✅ **Pregunta 11**

**¿Cuál es una ventaja clara de instalar Odoo en un servidor local de la empresa frente a un PC personal?**

A. No se necesita UPS ni SAI  
B. Mejores garantías de disponibilidad, seguridad física y rendimiento para múltiples usuarios  
C. Se eliminan las copias de seguridad  
D. Deja de ser necesaria la red local

**Respuesta correcta: B**

**Justificación:**  
Un servidor local permite redundancia, seguridad, SAI, hardware dedicado y rendimiento constante para varios usuarios. Un PC personal carece de todo eso.

---

## ✅ **Pregunta 12**

**¿En qué escenario brilla especialmente un Odoo instalado en una VM de cloud público?**

A. Empresas sin conexión a Internet  
B. Pymes multi-sede o con teletrabajo habitual que quieren escalar recursos con rapidez  
C. Microempresas con un solo usuario local  
D. Empresas que no quieren ningún coste recurrente

**Respuesta correcta: B**

**Justificación:**  
La nube ofrece escalabilidad, acceso global y disponibilidad, ideales para empresas con varias sedes o trabajo remoto.

---

# **1️⃣2️⃣ Conclusión general de la clase**

Elegir una modalidad de instalación no es una decisión técnica aislada: determina la autonomía, los costes, la seguridad, la escalabilidad y la capacidad futura de la empresa.

La clase enseña a analizar:

- el tamaño de la pyme,
    
- el número de usuarios,
    
- la necesidad real de personalización,
    
- el presupuesto en TI,
    
- la criticidad de los datos,
    
- el rendimiento esperado.
    

Odoo funciona en cualquier escala, pero **cada modalidad tiene ventajas y restricciones claras**. Conocerlas permite elegir la solución adecuada desde el principio.

---

