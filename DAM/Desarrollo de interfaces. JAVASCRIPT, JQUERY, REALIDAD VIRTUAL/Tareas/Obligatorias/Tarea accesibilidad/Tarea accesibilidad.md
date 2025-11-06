
---

**Asignatura:** Desarrollo de interfaces. JAVASCRIPT, JQUERY, REALIDAD VIRTUAL 
**Profesor:** Sara Gonzalo   
**Alumno:** David Rodríguez Igual  
**Fecha de cierre:** jueves, 20 de noviembre de 2025, 23:59

---
## Objetivo

El objetivo de esta actividad es **identificar y corregir los principales problemas de accesibilidad web** detectados en una evaluación hipotética de un sitio web. 

La tarea consiste en analizar una serie de incidencias comunes y **proponer soluciones técnicas** que garanticen el cumplimiento de las pautas **WCAG 2.1** y las recomendaciones del **W3C**, favoreciendo la inclusión y la experiencia de usuario.

---

## 1️⃣ Uso de atributos no válidos  

Cuando se emplean atributos obsoletos o incompatibles con la versión declarada de HTML, el código pierde coherencia y puede generar errores de visualización en diferentes navegadores.  

**Medida correctora:**

Validar el documento con la herramienta oficial del [W3C Validator](https://validator.w3.org/), eliminar propiedades no reconocidas y adaptar las etiquetas a la versión **HTML5**, asegurando una semántica clara y estandarizada.

---

## 2️⃣ Falta de texto alternativo en imágenes  

La ausencia del atributo `alt` en imágenes o iconos impide que los lectores de pantalla interpreten correctamente el contenido visual, dificultando el acceso a usuarios con discapacidad visual.  

**Medida correctora:** 

Añadir el atributo `alt` en todos los elementos gráficos, describiendo brevemente su función o propósito. En contenido decorativo, se recomienda usar `alt=""` para evitar redundancia.

---

## 3️⃣ Contraste insuficiente en el menú lateral  

Cuando el contraste entre el texto y el fondo es bajo, la legibilidad disminuye significativamente.  

**Medida correctora:**  

Comprobar la relación de contraste con herramientas como [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) y garantizar un mínimo de **4.5:1** según las pautas **WCAG**.  

De ser necesario, ajustar colores o tipografías sin alterar la identidad visual del sitio.

---

## 4️⃣ Formularios maquetados con tablas  

El uso de tablas para organizar formularios o elementos de diseño genera confusión en los lectores de pantalla y rompe la estructura lógica del contenido.  

**Medida correctora:**  

Sustituir la maquetación basada en tablas por contenedores `<div>` y CSS, reservando las tablas únicamente para **datos tabulares**.  

Aplicar etiquetas semánticas (`<label>`, `<fieldset>`, `<legend>`) para mantener la accesibilidad del formulario.

---

## 5️⃣ Uso de animaciones en Flash  

Flash es una tecnología desfasada y no compatible con navegadores modernos ni dispositivos móviles.  

**Medida correctora:**  

Reemplazar las animaciones en Flash por alternativas en **HTML5**, **CSS3** o **JavaScript**, asegurando compatibilidad y manteniendo la experiencia visual sin afectar la carga de la página.

---

## 6️⃣ Vídeos sin subtítulos  

La ausencia de subtítulos o transcripciones en vídeos limita el acceso a personas con discapacidad auditiva.  

**Medida correctora:**  

Incluir subtítulos sincronizados o una transcripción textual accesible.  

En plataformas como YouTube, se pueden generar automáticamente y editar para mejorar su precisión.

---

## 7️⃣ Navegación no compatible con teclado  

Cuando una web no permite recorrer sus elementos con la tecla `Tab`, los usuarios con limitaciones motrices no pueden interactuar con ella adecuadamente.  

**Medida correctora:** 

Revisar la estructura de enfoque (`tabindex`) y asegurarse de que todos los elementos interactivos (botones, enlaces, formularios) puedan recibir foco.  
Verificar que el orden de tabulación sea lógico y continuo.

---

## Observaciones de la tarea

La implementación de estas medidas mejora tanto la **accesibilidad universal** como la **usabilidad general**.  

Cumplir con las pautas del **W3C** y las **WCAG 2.1** no solo favorece la inclusión, sino que también:

- Mejora el posicionamiento SEO.  
- Reduce la tasa de rebote.  
- Incrementa la satisfacción del usuario.  
- Cumple con las obligaciones legales establecidas por el **Reglamento Europeo de Accesibilidad Digital (EN 301 549)**.

---

