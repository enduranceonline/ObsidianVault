
---

**Asignatura:** Desarrollo de interfaces. JAVASCRIPT, JQUERY, REALIDAD VIRTUAL 
**Profesor:** Sara Gonzalo   
**Alumno:** David Rodríguez Igual  
**Fecha de cierre:** lunes, 10 de noviembre de 2025, 23:59  

---

# 📊 Análisis de rendimiento y usabilidad web  
**Sitio analizado:** [https://mrguitarras.com](https://mrguitarras.com)  
**Herramienta empleada:** Pingdom Tools (test desde Frankfurt, Europa)

---

## 1️⃣ ¿Cómo es la carga de la página?

El tiempo total de carga registrado fue de **4,03 segundos**, con un evento `DOMContentLoaded` a los **2,49 s** y un tiempo hasta carga completa (`onLoad`) de **2,8 s**.  

En términos generales, el rendimiento se sitúa dentro de los valores aceptables para una web con contenido visual y multimedia, aunque podría optimizarse para mejorar la experiencia del usuario en conexiones medias o móviles.  

El servidor responde correctamente, pero se observa una **espera inicial de más de un segundo** (tiempo de “wait”) durante el establecimiento de conexión y transferencia de recursos, lo que indica que **existe margen de mejora en el tiempo de respuesta del servidor (TTFB)**.

---

## 2️⃣ ¿Cuánto ocupan las imágenes del tamaño total de la página?

Las imágenes representan una **porción importante del tamaño total**, con archivos grandes asociados al catálogo de productos y banners de cabecera.  

Según el registro HAR, la mayoría de las peticiones provienen de ficheros CSS y de recursos gráficos vinculados a WordPress y WooCommerce.

Se estima que las **imágenes suponen aproximadamente entre un 45 % y un 55 %** del peso total de la página, un valor alto que impacta negativamente en el tiempo de descarga y renderizado.

**Medidas recomendadas:**  
- Comprimir y optimizar las imágenes sin pérdida de calidad.  
- Implementar **lazy loading** para cargar únicamente las imágenes visibles.  
- Servir imágenes en formatos modernos (WebP o AVIF).  

---

## 3️⃣ ¿Cuánto ocupan las fuentes del tamaño total de la página?  

Las fuentes personalizadas procedentes de **Google Fonts (Montserrat y Bitter)** y las tipografías del tema “Jupiter” añaden un peso adicional estimado del **3 % al 5 %** del total de la página.  

Aunque su impacto no es tan alto como el de las imágenes, **su carga externa genera peticiones adicionales y aumenta la latencia**, especialmente en los dispositivos móviles.

**Medidas recomendadas:**  
- Combinar las fuentes en un único archivo CSS.  
- Usar solo los pesos necesarios (por ejemplo, eliminar variantes bold o light no utilizadas).  
- Habilitar almacenamiento local de fuentes mediante `font-display: swap`.  

---

## 4️⃣ ¿Cómo se puede reducir la velocidad de carga de la página?

Para reducir el tiempo de carga se pueden aplicar las siguientes estrategias técnicas:

1. **Activar la caché del navegador y del servidor** para almacenar recursos estáticos.  
2. **Habilitar compresión GZIP o Brotli**, optimizando la transferencia de ficheros CSS y JS.  
3. **Minificar y combinar** archivos CSS y JavaScript para reducir el número de peticiones HTTP.  
4. **Implementar un CDN (Content Delivery Network)** que distribuya el contenido desde servidores más cercanos al usuario.  
5. **Optimizar consultas a la base de datos** y revisar el uso de plugins en WordPress, ya que algunos duplican recursos innecesariamente.  
6. **Evaluar migración a PHP 8+**, dado que el sitio aún utiliza **PHP 7.4.33**, una versión desactualizada que limita el rendimiento.

---

## 5️⃣ Observaciones adicionales de rendimiento y usabilidad

El análisis del HAR muestra que el sitio **redirige de `http://mrguitarras.com` a `https://www.mrguitarras.com`**, lo que añade una llamada adicional (código 301) que puede evitarse configurando correctamente la URL principal.  

El peso total de la página supera los **1,7 MB**, repartido en **más de 80 peticiones HTTP**, lo que explica el tiempo de carga cercano a los 4 s.

En términos de **usabilidad**, el sitio utiliza una arquitectura basada en WooCommerce con múltiples hojas de estilo (`woocommerce.css`, `jupiter.min.css`, `animate.min.css`) que se cargan simultáneamente. Esta sobrecarga visual puede afectar la consistencia y accesibilidad.

---

## 6️⃣ Recomendaciones de mejora globales

### 🔹 Rendimiento
- Consolidar y minificar recursos CSS/JS.  
- Implementar un sistema de caché dinámico (por ejemplo, WP Super Cache o LiteSpeed).  
- Habilitar HTTP/2 si el servidor lo permite.  
- Analizar plugins activos y eliminar los que dupliquen funciones.  

### 🔹 Usabilidad
- Revisar la jerarquía visual del contenido y mantener la coherencia cromática.  
- Garantizar la legibilidad en dispositivos móviles, aplicando diseño **responsive** optimizado.  
- Asegurar que las acciones principales (carrito, búsqueda, contacto) sean visibles sin desplazamiento.  
- Mejorar el feedback visual en botones y formularios (colores, mensajes de error, confirmaciones).  

---

## 7️⃣ Conclusión

El sitio de *Mr. Guitarras* ofrece una experiencia visual rica y un diseño atractivo, pero **sacrifica parte de su rendimiento por exceso de recursos gráficos y hojas de estilo**.  

Con ajustes orientados a la optimización del contenido estático, la reducción del número de peticiones y la actualización tecnológica, se podría reducir el tiempo de carga por debajo de los **2,5 segundos**, alcanzando una calificación de rendimiento óptima según los estándares del W3C y los principios de **usabilidad de Nielsen**, especialmente en los aspectos de **visibilidad del estado del sistema, eficiencia y consistencia.**

---


