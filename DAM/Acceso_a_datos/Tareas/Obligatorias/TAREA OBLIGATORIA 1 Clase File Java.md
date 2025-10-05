#JAVA 

---
## 🧩 **Ejercicio base**

> En un proyecto de Java, crear un directorio (`miDirectorio`) y dentro de ese directorio un archivo (`miFichero.txt`) utilizando la clase `File`.

### ✅ Solución:

```java
package vt01;                          // No es necesario, solo sirve para declarar que esta clase pertenece al paquete vt01, para que quede mas ordenado.

import java.io.File;                  // Importa la clase File.
import java.io.IOException;           // Importa la excepciÃ³n de E/S que puede lanzar createNewFile().

public class Ejercicio01 {           

    public static void main(String args[]) {

        File miDirectorio = new File("src/vt01/miDirectorio"); // Crea un objeto File que APUNTA a la ruta "src/vt01/miDirectorio". Importante: aquÃ­ todavÃ­a NO se crea fÃ­sicamente el directorio.
        File miFichero = new File("src/vt01/miDirectorio/miFichero.txt"); // Otro objeto File que apunta al fichero dentro del directorio anterior. Tampoco se crea aÃºn el fichero; solo se referencia la ruta.

        try {                                   // Inicio de un bloque que puede lanzar IOException.

            miDirectorio.mkdir();               // Intenta crear el directorio (un Ãºnico nivel). Devuelve true si lo crea y false si ya existÃ­a o si falla (por permisos, ruta inexistente, etc.).

            if (miFichero.createNewFile())      // Intenta crear fÃ­sicamente el fichero. Devuelve true si lo crea; false si YA EXISTE.
                System.out.println("Fichero creado correctamente"); // Mensaje cuando createNewFile() devuelve true.

            else
                System.out.println("ERROR: No se ha podido crear el fichero"); // Mensaje cuando createNewFile() devuelve false (p.ej. ya existÃ­a o no pudo crearse).

            // El if/else no es necesario para crear el fichero en sÃ­, solo lo ponemos para que quede mas profesional y muestre mas informaciÃ³n por consola.

        } catch (IOException e) {               // Captura la IOException que puede lanzar createNewFile().
            System.out.println("Error al crear el fichero: " + e.getMessage()); // Imprime por pantalla mensaje de error corto
            // Una alternativa a la lÃ­nea anterior es escribir directamente el siguiente mÃ©todo: e.printStackTrace();
            // El mÃ©todo e.printStackTrace() imprime la traza completa del error en la salida de errores. Ãštil para depuraciÃ³n: muestra clase, mÃ©todo y lÃ­nea exacta del fallo.
        }

        System.out.println("FIN DEL PROGRAMA"); // Mensaje optativo de cierre, solo informativo.
    }
}

```

🧠 **Explicación:**

- Importamos el paquete `java.io`, que contiene la clase `File`.
    
- Usamos `mkdir()` para crear el directorio (si no existe).
    
- `createNewFile()` puede lanzar una `IOException`, por eso va dentro de un **try–catch**.
    
- Comprobamos con `.exists()` si el recurso ya está creado.

---

## ⚙️ **Variante 1**

> Crear un fichero de texto llamado `fichero_de_texto.txt` en la ruta `C:\AD\Ejercicios`

```java
package vt01;

import java.io.File;
import java.io.IOException;

public class Variante1 {
    public static void main(String[] args) {
        try {
            File directorio = new File("C:\\AD\\Ejercicios");

            // Crear el directorio si no existe
            if (!directorio.exists()) {
                directorio.mkdirs(); // crea toda la ruta intermedia si es necesario
                System.out.println("Directorio creado correctamente.");
            }

            // Crear el fichero dentro del directorio
            File fichero = new File(directorio, "fichero_de_texto.txt");
            fichero.createNewFile();
            System.out.println("Fichero creado correctamente.");

        } catch (IOException e) {
            System.out.println("Error de entrada/salida: " + e.getMessage());
        }
    }
}
```

🔹 Aquí usamos `mkdirs()` en lugar de `mkdir()` para asegurar que se crean **todas las carpetas intermedias** de la ruta (`C:\AD\Ejercicios`).

---

## ⚙️ **Variante 2**

> Programa interactivo con menú para crear/eliminar directorios y ficheros.

```java
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Variante2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n=== MENÚ ===");
            System.out.println("1. Crear directorio nuevoDirectorio");
            System.out.println("2. Crear fichero fichero_de_texto2.txt");
            System.out.println("3. Eliminar fichero fichero_de_texto.txt");
            System.out.println("4. Eliminar directorio nuevoDirectorio");
            System.out.println("5. Salir");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); // limpiar buffer

            try {
                File dir = new File("C:\\AD\\Ejercicios\\nuevoDirectorio");
                File f1 = new File("C:\\AD\\Ejercicios\\fichero_de_texto.txt");
                File f2 = new File(dir, "fichero_de_texto2.txt");

                switch (opcion) {
                    case 1:
                        if (!dir.exists()) {
                            dir.mkdirs();
                            System.out.println("Directorio creado.");
                        } else {
                            System.out.println("El directorio ya existe.");
                        }
                        break;

                    case 2:
                        if (!dir.exists()) dir.mkdirs();
                        if (f2.createNewFile()) {
                            System.out.println("Fichero creado en nuevoDirectorio.");
                        } else {
                            System.out.println("El fichero ya existe.");
                        }
                        break;

                    case 3:
                        if (f1.exists()) {
                            f1.delete();
                            System.out.println("Fichero eliminado.");
                        } else {
                            System.out.println("El fichero no existe.");
                        }
                        break;

                    case 4:
                        if (dir.exists()) {
                            if (dir.delete()) {
                                System.out.println("Directorio eliminado.");
                            } else {
                                System.out.println("No se puede eliminar: no está vacío.");
                            }
                        } else {
                            System.out.println("El directorio no existe.");
                        }
                        break;

                    case 5:
                        System.out.println("Saliendo del programa...");
                        break;

                    default:
                        System.out.println("Opción no válida.");
                }

            } catch (IOException e) {
                System.out.println("Error de E/S: " + e.getMessage());
            }
        } while (opcion != 5);

        sc.close();
    }
}
```

---

### 🧩 Conceptos aplicados

|Elemento|Descripción|
|---|---|
|`java.io.File`|Clase usada para representar ficheros y directorios.|
|`mkdir()` / `mkdirs()`|Crea uno o varios directorios.|
|`createNewFile()`|Crea un nuevo fichero vacío (requiere `try–catch`).|
|`delete()`|Elimina un fichero o carpeta vacía.|
|`exists()`|Comprueba si el recurso ya existe.|
|`try–catch`|Controla excepciones como `IOException` o `FileNotFoundException`.|

---

📌 **Conclusión:**

- La **Variante 1** consolida la creación básica de ficheros y directorios.
    
- La **Variante 2** añade control mediante menú y práctica con `switch–case` y excepciones.
    
- Todo el código debe importarse desde `java.io` y ejecutarse dentro de un bloque `try–catch`.

---

