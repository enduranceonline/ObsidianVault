
---

👨‍🏫 **Profesor:** José Antonio Martín  
📘 **Unidad:** Programación Multiproceso  
🗓 Autoevaluación Diciembre— 10/12/2025 
🎯 Resultado:  **20/20**

---

# 📌 Programación Multiprocesos y Multihilos

---

## **1️⃣ ¿Qué no es un estado de un proceso?**

### 🔹 Posibilidades:

a) En ejecución  
b) Compilado  
c) Interrumpido  
d) Pausado / detenido / en espera

✅ **Respuesta correcta:** **b)**

📘 **Justificación:**  
Los estados de un proceso hacen referencia a su ciclo de vida en el sistema operativo (ejecución, listo, bloqueado, etc.).  
**“Compilado”** es una fase previa a la ejecución, no un estado del proceso.

---

## **2️⃣ ¿Cómo se identifican los archivos ejecutables en sistemas operativos basados en GNU/Linux?**

### 🔹 Posibilidades:

a) Por tener activado su permiso de ejecución  
b) Por su extensión `.exe`  
c) Por estar ubicados en la carpeta `/bin`  
d) Por estar compilados en código binario

✅ **Respuesta correcta:** **a)**

📘 **Justificación:**  
En GNU/Linux un archivo es ejecutable si tiene **permiso de ejecución (`x`)**, independientemente de su extensión o ubicación.

---

## **3️⃣ ¿Qué es un cambio de contexto en el sistema operativo?**

### 🔹 Posibilidades:

a) Asignar más memoria a un proceso  
b) Reiniciar el sistema operativo  
c) Guardar el estado de un proceso para asignar la CPU a otro  
d) Bloquear un hilo dentro de un proceso

✅ **Respuesta correcta:** **c)**

📘 **Justificación:**  
El cambio de contexto permite al sistema **interrumpir un proceso**, guardar su estado y **dar la CPU a otro**, garantizando multitarea.

---

## **4️⃣ ¿Qué caracteriza al algoritmo de planificación Round-Robin?**

### 🔹 Posibilidades:

a) Da prioridad a los procesos más importantes  
b) Divide los procesos en colas por prioridad  
c) Todos los procesos tienen un quantum de CPU igual  
d) Un proceso usa la CPU hasta finalizar

✅ **Respuesta correcta:** **c)**

📘 **Justificación:**  
Round-Robin reparte el tiempo de CPU de forma equitativa mediante un **quantum fijo**, asegurando justicia entre procesos.

---

## **5️⃣ ¿Qué diferencia hay entre el algoritmo FIFO y el Shortest Job First (SJF)?**

### 🔹 Posibilidades:

a) Son el mismo algoritmo  
b) FIFO prioriza procesos largos y SJF los cortos  
c) FIFO atiende por orden de llegada y SJF prioriza los procesos más cortos  
d) No hay diferencia

✅ **Respuesta correcta:** **c)**

📘 **Justificación:**

- **FIFO:** orden de llegada
    
- **SJF:** menor tiempo de ejecución primero  
    Esto impacta directamente en el tiempo de espera promedio.
    

---

## **6️⃣ ¿Cuál es la diferencia principal entre una aplicación y un ejecutable?**

### 🔹 Posibilidades:

a) Un ejecutable no necesita sistema operativo  
b) Son lo mismo  
c) La aplicación es el concepto funcional; el ejecutable es el archivo que se ejecuta  
d) Una aplicación siempre es `.exe`

✅ **Respuesta correcta:** **c)**

📘 **Justificación:**  
Una **aplicación** es el software como solución.  
Un **ejecutable** es el archivo concreto que el sistema puede lanzar.

---

## **7️⃣ ¿Cuál de los siguientes es un tipo de ejecutable?**

### 🔹 Posibilidades:

a) Interfaz gráfica  
b) Servicios  
c) Compiladores  
d) Binarios

✅ **Respuesta correcta:** **d)**

📘 **Justificación:**  
Los ejecutables son **archivos binarios** que el sistema operativo puede cargar y ejecutar.

---

## **8️⃣ ¿Qué significa que un proceso está en estado "bloqueado"?**

### 🔹 Posibilidades:

a) Espera por falta de memoria  
b) Está ejecutándose  
c) Espera a que termine una operación de E/S  
d) Ha finalizado

✅ **Respuesta correcta:** **c)**

📘 **Justificación:**  
Un proceso bloqueado **no puede continuar** hasta que finalice una operación de entrada/salida.

---

## **9️⃣ Los niveles de planificación de procesos son…**

### 🔹 Posibilidades:

a) Nuevo, medio y largo plazo  
b) No existen niveles  
c) Corto, medio y largo plazo  
d) Corto y largo plazo

✅ **Respuesta correcta:** **c)**

📘 **Justificación:**

- **Corto plazo:** CPU
    
- **Medio plazo:** suspensión
    
- **Largo plazo:** admisión de procesos
    

---

## **🔟 ¿Qué es un proceso en un sistema operativo?**

### 🔹 Posibilidades:

a) Un programa en ejecución gestionado por el SO  
b) Una app sin CPU  
c) Instrucciones en RAM  
d) Un archivo binario

✅ **Respuesta correcta:** **a)**

📘 **Justificación:**  
Un proceso es **un programa en ejecución**, con recursos y control del sistema operativo.

---

## **1️⃣1️⃣ ¿Qué es un servicio?**

### 🔹 Posibilidades:

a) Un proceso con ventana  
b) Un proceso sin interfaz gráfica gestionado por el sistema  
c) Un hilo especial de Java  
d) Un gestor de impresoras

✅ **Respuesta correcta:** **b)**

📘 **Justificación:**  
Los servicios funcionan en segundo plano y **no interactúan directamente con el usuario**.

---

## **1️⃣2️⃣ ¿Qué se conoce por Equidad en los elementos de un proceso?**

### 🔹 Posibilidades:

a) Igual número de procesos en cola  
b) No es un elemento del proceso  
c) Reparto equitativo del tiempo de CPU  
d) Mismo número de procesos por procesador

✅ **Respuesta correcta:** **c)**

📘 **Justificación:**  
La equidad garantiza que **todos los procesos reciban CPU de forma justa**, evitando el hambre.

---

## **1️⃣3️⃣ ¿Qué se conoce como Tiempo de respuesta de un proceso?**

### 🔹 Posibilidades:

a) Tiempo de respuesta del hilo  
b) Consumo total de CPU  
c) Tiempo total en CPU  
d) Tiempo desde que entra en cola hasta que empieza a ejecutarse

✅ **Respuesta correcta:** **d)**

📘 **Justificación:**  
Mide la **rapidez del sistema** desde que el proceso solicita CPU hasta que la obtiene.

---

## **1️⃣4️⃣ ¿Qué hace el comando `kill` en Linux?**

### 🔹 Posibilidades:

a) Cierra un proceso  
b) No existe  
c) Lista procesos  
d) Lanza un proceso

✅ **Respuesta correcta:** **a)**

📘 **Justificación:**  
`kill` envía señales a procesos, normalmente para **finalizarlos**.

---

## **1️⃣5️⃣ ¿Qué implica un sistema multiproceso?**

### 🔹 Posibilidades:

a) Varios procesadores ejecutando procesos simultáneamente  
b) Procesos solo sin E/S  
c) Seudoparalelismo  
d) Un proceso en varios núcleos

✅ **Respuesta correcta:** **a)**

📘 **Justificación:**  
Multiproceso implica **paralelismo real** con más de una CPU.

---

## **1️⃣6️⃣ ¿Qué relación hay entre proceso e hilo?**

### 🔹 Posibilidades:

a) Un proceso puede contener varios hilos  
b) Un hilo contiene procesos  
c) Son idénticos  
d) Un hilo es un servicio

✅ **Respuesta correcta:** **a)**

📘 **Justificación:**  
Los hilos comparten recursos del proceso y permiten ejecución concurrente.

---

## **1️⃣7️⃣ ¿Qué significa que un proceso está en estado "listo"?**

### 🔹 Posibilidades:

a) Espera su turno de CPU  
b) Está bloqueado  
c) Ha finalizado  
d) Se está ejecutando

✅ **Respuesta correcta:** **a)**

📘 **Justificación:**  
El proceso está preparado, pero **espera asignación de CPU**.

---

## **1️⃣8️⃣ El objetivo prioritario del planificador a largo plazo es:**

### 🔹 Posibilidades:

a) Proporcionar una mezcla equilibrada de trabajos  
b) Aceptar solo procesos CPU  
c) Ejecutar todos los procesos  
d) Aceptar solo procesos de E/S

✅ **Respuesta correcta:** **a)**

📘 **Justificación:**  
Busca equilibrio entre procesos CPU-bound y I/O-bound.

---

## **1️⃣9️⃣ ¿Qué sucede cuando un proceso consume su quantum de CPU?**

### 🔹 Posibilidades:

a) Se pausa y vuelve al final de la cola de listos  
b) Se bloquea  
c) Se elimina  
d) Se vuelve de tiempo real

✅ **Respuesta correcta:** **a)**

📘 **Justificación:**  
En planificación preventiva, el proceso **cede la CPU** al agotarse el quantum.

---

## **2️⃣0️⃣ ¿Cuál es la extensión típica de un ejecutable?**

### 🔹 Posibilidades:

a) `.OR`, `.PHP`, `.ES`, `.EXE`, `.APK`  
b) `.JAVA`, `.OR`, `.PHP`, `.ES`  
c) `.EXE`, `.DLL`, `.PIF`, `.CMD`, `.APK`  
d) `.OR`, `.PHP`, `.ES`, `.COM`

✅ **Respuesta correcta:** **c)**

📘 **Justificación:**  
Son extensiones comúnmente asociadas a **archivos ejecutables**, especialmente en entornos Windows.

---
