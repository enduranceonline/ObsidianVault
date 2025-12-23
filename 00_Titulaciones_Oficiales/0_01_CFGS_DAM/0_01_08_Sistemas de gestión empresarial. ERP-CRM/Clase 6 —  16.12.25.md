# 📘 Sistemas de Gestión Empresarial — ERP / CRM

---

👨‍🏫 **Profesor:** José Luis Sánchez Montejo  
📘 **Asignatura:** Sistemas de gestión empresarial (ERP-CRM)  
🗓 **Clase:** 6 — 16/12/2025  
🎯 **Tema:** Instalación de Odoo 18 y Odoo 19 en Windows (entorno nativo)

---

## 1️⃣ Introducción a la instalación

En esta práctica se aborda la instalación de **Odoo 18 en un sistema Windows nativo**, con el propósito de comprender de forma completa cómo se realiza el despliegue inicial de un sistema ERP y cuáles son los elementos que intervienen en su puesta en marcha. El objetivo no es únicamente conseguir que la aplicación funcione, sino entender el proceso, las decisiones que se toman durante la instalación y el papel de cada uno de los componentes implicados.

Aunque en entornos empresariales reales suelen emplearse soluciones más robustas y orientadas a producción, como contenedores Docker o sistemas basados en Linux, en este caso se opta por una instalación directa sobre Windows. Este enfoque permite visualizar de manera clara y ordenada todos los pasos necesarios, desde la descarga del instalador hasta la creación del servicio y el arranque inicial del sistema, lo que resulta especialmente útil desde un punto de vista formativo.

---

## 2️⃣ Consideraciones previas sobre Windows nativo

La instalación de Odoo directamente sobre un sistema Windows presenta una serie de limitaciones cuando se compara con otras alternativas más habituales en entornos profesionales, como Docker o distribuciones Linux. Estas limitaciones están relacionadas principalmente con el rendimiento, la gestión de procesos y la facilidad de mantenimiento a largo plazo.

En sistemas Windows, Odoo puede experimentar un rendimiento inferior cuando se somete a cargas elevadas, especialmente en escenarios con múltiples usuarios concurrentes. Además, la escalabilidad y el mantenimiento del sistema resultan más complejos, ya que la gestión de servicios y dependencias no es tan flexible como en otros entornos. A esto se suma la dependencia de configuraciones internas del propio sistema operativo, que pueden influir en el comportamiento del ERP.

A pesar de estas desventajas, la instalación sobre Windows resulta adecuada para entornos de aprendizaje. Permite simplificar el proceso inicial, evita configuraciones avanzadas innecesarias y facilita la comprensión del flujo completo de despliegue del ERP. Por este motivo, es una opción válida para pruebas, demostraciones y prácticas formativas, donde el objetivo principal es adquirir conocimientos y no garantizar un funcionamiento productivo a largo plazo.

---

## 3️⃣ Requisitos mínimos y aconsejables

Antes de iniciar la instalación de Odoo 18, es necesario comprobar que el sistema cumple con unos requisitos mínimos que garanticen su correcto funcionamiento. En el caso de Windows, se requiere disponer de **Windows 10 o una versión superior**, ya que versiones anteriores no ofrecen la compatibilidad necesaria.

A nivel de hardware, se recomienda contar con un procesador de al menos **dos núcleos**, una **memoria RAM mínima de 4 GB** y **20 GB de espacio libre en disco**, lo que permite alojar tanto la aplicación como la base de datos y los archivos generados durante su uso. Asimismo, es imprescindible disponer de conexión a Internet para la descarga del software y de **permisos de administrador**, necesarios para la creación de servicios y la instalación de dependencias.

Un aspecto importante es que el instalador oficial de Odoo incluye internamente las dependencias necesarias, como **Python** y **PostgreSQL**, lo que evita tener que realizar instalaciones manuales adicionales y reduce la posibilidad de errores de configuración.

---

## 4️⃣ Descarga de Odoo 18

Para comenzar el proceso de instalación, se accede a la **página oficial de Odoo** y se navega hasta la parte final del sitio web, donde se encuentra la opción de descarga del software. Desde este apartado se inicia el proceso de obtención del instalador adecuado.

Durante la descarga, se solicitan algunos datos básicos y se selecciona la versión deseada del ERP. En este caso se elige **Odoo 18**, ya que se trata de una versión estable y adecuada para el desarrollo de la práctica. A continuación, se selecciona la versión correspondiente al sistema operativo **Windows**, lo que permite obtener un archivo ejecutable preparado específicamente para este entorno.

Una vez completado el formulario, se descarga el archivo necesario para continuar con la instalación.

---

## 5️⃣ Ejecución del instalador de Odoo 18

### 5.1 Pantalla de bienvenida

Al ejecutar el archivo descargado, se muestra la pantalla de bienvenida del instalador de **Odoo 18.0**. Esta primera ventana informa al usuario de que el asistente se encargará de guiar todo el proceso de instalación de manera secuencial.

![[Pasted image 20251222120243.png]]

El carácter guiado del instalador facilita la instalación incluso a usuarios sin experiencia previa en este tipo de software, ya que cada paso se presenta de forma clara y ordenada. Para continuar con el proceso, se pulsa el botón **Next**.

_(Insertar imagen: Welcome to Odoo 18.0 Setup)_

---

### 5.2 Licencia de uso

En el siguiente paso se muestran los términos de la licencia **GNU LGPL v3**, bajo la cual se distribuye Odoo. Esta licencia regula el uso, la modificación y la redistribución del software.

![[Pasted image 20251222120257.png]]

Para poder continuar con la instalación es obligatorio aceptar los términos de la licencia. Esto se realiza pulsando el botón **I Agree**, lo que indica la conformidad con las condiciones establecidas.

_(Insertar imagen: License Agreement)_

---

### 5.3 Selección de componentes

A continuación, el instalador presenta la lista de componentes que se instalarán en el sistema. En esta pantalla se muestran, marcadas por defecto, las opciones necesarias para una instalación estándar:

![[Pasted image 20251222120306.png]]

- **Odoo Server**, que corresponde al núcleo de la aplicación
    
- **PostgreSQL Database**, que actúa como sistema gestor de bases de datos
    

No se realizan modificaciones en esta sección, ya que la configuración por defecto es suficiente para un entorno local de pruebas y aprendizaje. De este modo, se garantiza que todos los elementos esenciales queden correctamente instalados.

_(Insertar imagen: Select components)_

---

### 5.4 Configuración de PostgreSQL

En este paso se configura la conexión a la base de datos PostgreSQL que utilizará Odoo. El instalador muestra una serie de valores predefinidos, entre los que se incluyen el nombre del host, el puerto de conexión y las credenciales del usuario de base de datos.

![[Pasted image 20251222120316.png]]

Los valores que aparecen por defecto (`localhost`, puerto `5432`, usuario `openpg` y contraseña `openpgpwd`) están pensados para una instalación local y permiten que Odoo se conecte automáticamente a la base de datos sin necesidad de ajustes adicionales. Por este motivo, no se modifican estos parámetros.

_(Insertar imagen: PostgreSQL configuration)_

---

### 5.5 Selección de carpeta de instalación

El instalador propone una ruta por defecto donde se instalará Odoo, generalmente dentro del directorio **Program Files** del sistema. Esta ubicación es adecuada para aplicaciones instaladas a nivel de sistema y no requiere cambios para esta práctica.

![[Pasted image 20251222120337.png]]

Se mantiene la ruta propuesta y se pulsa el botón **Install** para iniciar el proceso de instalación propiamente dicho.

_(Insertar imagen: Destination folder)_

---

### 5.6 Proceso de instalación

En esta fase se lleva a cabo la instalación efectiva del software. El asistente comienza a copiar los archivos necesarios y a configurar los distintos componentes del sistema.

![[Pasted image 20251222120349.png]]

Durante este proceso se instalan el servidor de Odoo, la base de datos PostgreSQL, las dependencias internas y el servicio de Windows que permitirá ejecutar Odoo de forma automática. Este paso puede tardar algunos minutos, dependiendo del rendimiento del equipo.

_(Insertar imagen: Installing files)_

---

### 5.7 Finalización de la instalación

Una vez completada la instalación, el asistente muestra un mensaje indicando que **Odoo 18.0 ha sido instalado correctamente** en el sistema. En este punto se deja marcada la opción **Start Odoo**, lo que permite iniciar automáticamente el servicio al cerrar el instalador.

![[Pasted image 20251222120400.png]]

Para finalizar, se pulsa el botón **Finish**, concluyendo así el proceso de instalación del ejecutable.

_(Insertar imagen: Completing Odoo 18.0 Setup)_

---

## 6️⃣ Estado actual de la práctica

Al finalizar esta fase de la práctica, se puede confirmar que Odoo 18 ha quedado correctamente instalado en el sistema Windows. El servicio correspondiente ha sido creado y el servidor está preparado para su primer arranque y configuración inicial.

En la siguiente parte de la práctica se abordará la configuración de la base de datos y el acceso inicial al sistema, pasos necesarios para comenzar a trabajar con Odoo de forma funcional.

---

## 7️⃣ Acceso inicial a Odoo y configuración de la Base de Datos

Una vez finalizada la instalación del ejecutable, el siguiente paso consiste en comprobar que el servidor de Odoo está en funcionamiento y acceder a su interfaz web. Para ello, se abre un navegador y se introduce la siguiente dirección:

`http://localhost:8069/web/database/selector`

![[Pasted image 20251222120536.png]]

Esta URL corresponde al **gestor de bases de datos de Odoo**, una herramienta integrada que permite crear, administrar y restaurar bases de datos. Desde este panel se realiza la creación de la primera base de datos, que será el núcleo sobre el que trabajará el sistema ERP.

---

## 8️⃣ Creación de la base de datos inicial

Al acceder al gestor de bases de datos, Odoo muestra un formulario en el que se solicita la información necesaria para crear la base de datos inicial del sistema. Este paso es fundamental, ya que sin una base de datos creada Odoo no puede operar.

![[Pasted image 20251222120548.png]]

Entre los campos que se deben completar se encuentran los siguientes:

- **Master Password**  
    Odoo genera automáticamente una contraseña maestra que protege el acceso al gestor de bases de datos. Esta contraseña actúa como una medida de seguridad adicional y será requerida en el futuro para realizar operaciones críticas, como eliminar, duplicar o restaurar bases de datos. Es importante conservarla correctamente, ya que sin ella no se podrán realizar estas acciones administrativas.
    
- **Database Name**  
    Se asigna un nombre identificativo a la base de  datos, que permitirá reconocerla dentro del sistema, especialmente en escenarios donde se gestionen varias bases de datos desde el mismo servidor.
    
- **Email y Password**  
    Estos datos corresponden al usuario  administrador inicial del sistema. Este usuario tendrá control total sobre el ERP, incluyendo la configuración general, la gestión de usuarios y la instalación de módulos.
    
- **Language y Country**  
    Se selecciona el idioma español y el país   España para adaptar la interfaz de usuario, los formatos de fecha, moneda y otros parámetros regionales al entorno de trabajo.
    

---

## 9️⃣ Opción _Demo Data_ (Datos de demostración)

Durante la creación de la base de datos se **marca la opción _Demo Data_**, lo que indica a Odoo que debe cargar datos de ejemplo en el sistema.

### ¿Por qué es importante marcar _Demo Data_?

La opción _Demo Data_ permite que Odoo genere automáticamente datos ficticios dentro de la base de datos, como clientes, productos, pedidos, facturas y distintas estructuras ya configuradas en los módulos. Estos datos no tienen un uso real, pero cumplen una función clave en entornos formativos.

En un **entorno de aprendizaje**, los datos de demostración permiten explorar el funcionamiento del ERP sin necesidad de crear información manualmente desde cero. Gracias a ello, es posible analizar cómo interactúan los distintos módulos, comprender los flujos de trabajo internos y simular el funcionamiento real de una empresa de forma inmediata.

Además, el uso de _Demo Data_ reduce considerablemente el tiempo necesario para realizar pruebas y facilita la comprensión global del sistema, ya que se dispone de ejemplos completos desde el primer acceso. En entornos productivos reales esta opción no se utiliza, pero en el contexto de esta práctica resulta la más adecuada.

---

## 🔟 Creación de la base de datos

Una vez completados todos los campos del formulario y marcada la opción _Demo Data_, se pulsa el botón **Create database** para iniciar el proceso de creación.

En este momento, Odoo comienza a generar la base de datos y a cargar los datos de demostración seleccionados. Este proceso puede tardar unos minutos, dependiendo del rendimiento del sistema, ya que implica la creación de tablas, relaciones y registros iniciales.

---

## 1️⃣1️⃣ Primer inicio de sesión en Odoo

Cuando finaliza la creación de la base de datos, el sistema redirige automáticamente a la pantalla de inicio de sesión de Odoo. En esta pantalla se introducen el correo electrónico y la contraseña definidos previamente para el usuario administrador.

![[Pasted image 20251222120633.png]]

Si las credenciales son correctas, se accede al sistema ERP sin problemas. En caso contrario, Odoo muestra un mensaje indicando que el usuario o la contraseña no son válidos, lo que permite identificar posibles errores en la introducción de datos.

---

## 1️⃣2️⃣ Acceso al panel principal de Odoo

Tras iniciar sesión correctamente, se accede al **panel principal de Odoo**, que actúa como punto central de navegación dentro del sistema. En este panel se muestran los distintos módulos disponibles, organizados por categorías.

Desde esta pantalla es posible acceder a las aplicaciones instaladas, activar nuevos módulos, configurar distintos aspectos del sistema y gestionar usuarios y datos. Este panel será el punto de partida para continuar con la práctica y analizar el uso funcional del ERP.

---

## 1️⃣3️⃣ Comprobación de la base de datos (PostgreSQL)

![[Pasted image 20251222120743.png]]
Durante el proceso de instalación, Odoo instala y configura automáticamente **PostgreSQL** como sistema gestor de bases de datos. Para verificar que todo se ha configurado correctamente, se puede utilizar una herramienta de administración como **pgAdmin**.

![[Pasted image 20251222120659.png]]
![[Pasted image 20251222120711.png]]

Mediante esta herramienta es posible comprobar la existencia de la base de datos creada, observar las tablas generadas automáticamente por Odoo y analizar la estructura interna del sistema. Esta comprobación confirma que Odoo utiliza PostgreSQL como motor de base de datos y que la instalación se ha realizado de forma correcta.

Llegados a este punto, se puede confirmar que el entorno está correctamente preparado. Odoo 18 se encuentra instalado en Windows, la base de datos ha sido creada sin errores y se han cargado los datos de demostración. Además, el sistema es accesible a través del navegador web y está listo para comenzar a trabajar con módulos y usuarios.

---

## 1️⃣4️⃣ Instalación de Odoo 19 sin desinstalar Odoo 18

Hasta este punto, Odoo 18 ha quedado instalado y funcionando correctamente en un sistema Windows nativo, con su servicio operativo, su puerto HTTP configurado y una base de datos plenamente funcional. El siguiente objetivo consiste en dar un paso más y **instalar Odoo 19 sin eliminar la versión anterior**, permitiendo así la convivencia de ambas versiones dentro del mismo sistema operativo.

Este escenario resulta especialmente interesante desde un punto de vista técnico, ya que obliga a comprender cómo gestiona Odoo sus recursos internos y qué ocurre cuando varias versiones intentan ejecutarse en paralelo. No se trata únicamente de “tener dos programas instalados”, sino de entender cómo interactúan con el sistema, con la red y con la base de datos.

En Windows, el instalador oficial de Odoo despliega la aplicación dentro de una estructura relativamente cerrada en el directorio _Program Files_. Cuando se instalan dos versiones distintas —por ejemplo Odoo 18 y Odoo 19— cada una se aloja en su propia carpeta, lo que a primera vista podría dar la impresión de que no existe ningún conflicto. Sin embargo, **si no se realiza ninguna modificación adicional**, ambas versiones pueden intentar utilizar los mismos parámetros de ejecución por defecto.

Los conflictos más habituales aparecen cuando ambas instalaciones intentan:

- Escuchar en el mismo puerto HTTP.
    
- Conectarse a la misma base de datos.
    
- Utilizar configuraciones idénticas de conexión y arranque.
    

En estas situaciones, el sistema no puede distinguir correctamente qué versión debe responder a las peticiones, lo que provoca que una de ellas no llegue a iniciarse, quede inaccesible desde el navegador o funcione de manera incorrecta. En la práctica, una versión “se impone” sobre la otra.

Por tanto, la clave de este proceso no es evitar la coexistencia, sino **configurar correctamente cada instalación para que sea independiente a nivel lógico**, aunque compartan el mismo sistema operativo.

Es fundamental entender que:

- Dos instalaciones de Odoo pueden convivir sin problemas siempre que cada una tenga **una configuración coherente y diferenciada**.
    
- El conflicto más común se produce cuando ambas comparten **el mismo puerto HTTP**, ya que un puerto solo puede ser utilizado por un servicio a la vez.
    
- También se generan errores si ambas intentan utilizar **la misma base de datos**, especialmente cuando pertenecen a versiones distintas.
    
- Aunque **una sola instancia de Odoo puede gestionar múltiples bases de datos** (por ejemplo, varios clientes o empresas), **cada versión mayor de Odoo requiere bases de datos compatibles con su estructura interna**, por lo que no es viable reutilizar la misma base de datos entre versiones distintas.
    

Este ejercicio permite visualizar de forma práctica por qué, en entornos profesionales, se planifica cuidadosamente la arquitectura antes de desplegar nuevas versiones.

---

## 1️⃣5️⃣ Revisión de directorios de instalación en _Program Files_

Para confirmar que ambas versiones están correctamente instaladas, se accede al explorador de archivos de Windows y se navega hasta el directorio:

`C:\Program Files\`

En este directorio se puede observar que existen carpetas independientes para cada versión de Odoo instalada. Por ejemplo, una carpeta correspondiente a Odoo 18 y otra correspondiente a Odoo 19, cada una con su propia estructura interna de archivos y dependencias.

![[Pasted image 20251223074940.png]]

Este hecho confirma que Windows permite la coexistencia de múltiples versiones del mismo software a nivel de sistema de archivos, ya que cada instalación queda aislada físicamente en su propio directorio. Sin embargo, esta separación a nivel de carpetas **no implica automáticamente que las aplicaciones puedan ejecutarse sin conflicto**.

Aunque los binarios y archivos estén separados, ambos servicios siguen compartiendo recursos del sistema como:

- Puertos de red.
    
- Servicios del sistema operativo.
    
- Acceso al servidor de bases de datos PostgreSQL.
    

Por este motivo, la revisión de los directorios es solo el primer paso. A partir de aquí resulta imprescindible analizar la configuración interna de cada instalación para garantizar que ambas versiones puedan funcionar de forma independiente.

---

## 1️⃣6️⃣ Identificación del archivo de configuración `odoo.conf`

Cada instalación de Odoo dispone de un archivo de configuración principal que define el comportamiento del servidor. Este archivo se encuentra dentro de la carpeta `server` de cada instalación y se denomina:

`odoo.conf`

Este archivo es uno de los elementos más importantes de todo el sistema, ya que actúa como punto central de configuración del servidor Odoo. En él se definen parámetros críticos que determinan cómo se inicia la aplicación, cómo se comunica con la base de datos y cómo se expone el servicio al exterior.

![[Pasted image 20251223075011.png]]

Entre los parámetros más relevantes que se encuentran en este archivo destacan:

- El **puerto HTTP** (`http_port`) en el que Odoo escuchará las peticiones del navegador.
    
- Los datos de conexión a PostgreSQL, como `db_host`, `db_port`, `db_user` y `db_password`.
    
- Rutas internas, comportamiento de módulos y opciones avanzadas del servidor.
    

Para analizar correctamente este archivo, se abre utilizando un editor de texto avanzado como Visual Studio Code, lo que permite una lectura clara y ordenada de todos los parámetros. Al revisar el `odoo.conf` de Odoo 18, se observa que utiliza el puerto **8069**, que es el puerto estándar por defecto, y que se conecta a PostgreSQL en `localhost` a través del puerto `5432`, usando el usuario `openpg`.

Este análisis es fundamental porque permite identificar **qué valores deben modificarse en Odoo 19** para evitar conflictos. A partir de aquí se entiende que el archivo `odoo.conf` no es simplemente un archivo más, sino el elemento que permite controlar de forma precisa el comportamiento de cada instancia de Odoo y garantizar su correcta convivencia con otras versiones instaladas en el mismo sistema.

---

## 1️⃣7️⃣ Por qué una sola instancia puede servir a múltiples bases de datos

Un aspecto clave para comprender la arquitectura de Odoo es que **una sola instancia del servidor puede trabajar simultáneamente con múltiples bases de datos**. Esto significa que un único proceso de Odoo, ejecutándose en un puerto concreto, puede dar servicio a varias empresas o clientes distintos, siempre que cada uno disponga de su propia base de datos independiente.

Desde el punto de vista técnico, Odoo actúa como una capa de aplicación que, en función de la base de datos seleccionada en el gestor de bases de datos o en la URL de acceso, carga una u otra información. Cada base de datos contiene su propia configuración, usuarios, módulos instalados y datos empresariales, pero todas comparten el mismo código del servidor Odoo.

Este enfoque resulta especialmente útil en escenarios como:

- Entornos multiempresa, donde una misma instalación aloja varias compañías.
    
- Proveedores de servicios que gestionan múltiples clientes desde un único servidor.
    
- Desarrollo de módulos personalizados que se reutilizan en distintos proyectos, manteniendo una sola base de código.
    

Sin embargo, este diseño también tiene implicaciones importantes. Aunque una instancia puede servir múltiples bases de datos, **no es viable que distintas versiones mayores de Odoo (como Odoo 18 y Odoo 19) compartan los mismos recursos lógicos**. Cada versión introduce cambios internos en la estructura del sistema, en los módulos base y en las tablas de la base de datos, lo que hace que una base de datos creada para una versión no sea compatible con otra.

Por este motivo, cuando se trabaja con varias versiones de Odoo en un mismo sistema, es imprescindible separar claramente:

- La **versión del servidor** que se está ejecutando.
    
- El **puerto HTTP** en el que escucha cada versión.
    
- La **base de datos** asociada a cada una.
    

Entender esta distinción es fundamental para evitar conflictos y errores de arranque, y permite comprender por qué la coexistencia de versiones requiere una configuración cuidadosa.

---

## 1️⃣8️⃣ Configuración de Odoo 19 para evitar conflicto de puertos

Al analizar el archivo `odoo.conf` correspondiente a la instalación de Odoo 19, se observa que el parámetro `http_port` puede estar configurado inicialmente con el mismo valor que utiliza Odoo 18. Esto ocurre porque el instalador aplica una configuración por defecto que no tiene en cuenta la existencia de otras versiones previamente instaladas.

El problema surge porque **un puerto de red solo puede ser utilizado por un servicio a la vez**. Si Odoo 18 y Odoo 19 intentan escuchar en el mismo puerto, el sistema operativo solo permitirá que uno de ellos se inicie correctamente, mientras que el otro fallará o quedará inaccesible desde el navegador.

Para evitar este conflicto, se decide asignar un puerto distinto a cada versión. Por ejemplo:

- Odoo 18 continúa utilizando el puerto estándar `8069`.
    
- Odoo 19 se configura para utilizar un nuevo puerto, como `8070`.
    

Este cambio se realiza modificando el valor de `http_port` en el archivo `odoo.conf` de Odoo 19. De este modo, cada versión escucha en un puerto distinto y ambas pueden ejecutarse de forma simultánea sin interferirse.

Este ajuste ilustra un concepto fundamental en la administración de servicios: **la correcta asignación de puertos es esencial cuando se ejecutan múltiples aplicaciones o versiones en un mismo servidor**, y forma parte de las configuraciones básicas en cualquier despliegue real.

---

## 1️⃣9️⃣ Permisos en Windows para editar `odoo.conf`

Un aspecto práctico que aparece al modificar el archivo `odoo.conf` es la gestión de permisos en Windows. Las carpetas ubicadas dentro de `C:\Program Files\` están protegidas por el sistema operativo para evitar modificaciones accidentales o malintencionadas en aplicaciones instaladas a nivel de sistema.

Debido a esta protección, al intentar guardar cambios en el archivo `odoo.conf` puede aparecer un error indicando que no se dispone de permisos suficientes para escribir en el archivo. Para poder continuar con la práctica, es necesario revisar y modificar temporalmente los permisos del archivo.

Este proceso se realiza accediendo a las **Propiedades** del archivo, entrando en la pestaña **Seguridad** y permitiendo permisos de escritura al usuario correspondiente. De este modo, se habilita la posibilidad de editar y guardar los cambios necesarios en la configuración.

![[Pasted image 20251223075106.png]]

Es importante remarcar que esta acción se considera aceptable en un **entorno didáctico o de pruebas**, donde el objetivo es experimentar y comprender el funcionamiento del sistema. Sin embargo, en un entorno de producción real, este tipo de permisos amplios no sería recomendable, ya que reduce la seguridad y aumenta el riesgo de modificaciones no controladas.

Este punto permite entender una diferencia importante entre entornos formativos y entornos productivos, y refuerza la idea de que las prácticas realizadas en Windows nativo están orientadas al aprendizaje y no a un despliegue final.

---

## 2️⃣0️⃣ Creación de una nueva base de datos para Odoo 19

Aunque ya existe una base de datos creada y en uso por Odoo 18, **no es posible reutilizarla para Odoo 19**. Cada versión mayor de Odoo introduce modificaciones internas que afectan directamente a la estructura de la base de datos: nuevas tablas, cambios en campos existentes, alteraciones en relaciones y ajustes en los módulos base que forman el núcleo del sistema.

Por este motivo, una base de datos creada para Odoo 18 **no es compatible** con Odoo 19. Intentar arrancar una versión nueva sobre una base de datos antigua puede provocar errores graves, impedir el arranque del servidor o generar comportamientos impredecibles.

Para evitar estos problemas, se crea una **nueva base de datos independiente**, por ejemplo `db-odoo19`, que será inicializada específicamente para esta versión. Esta base de datos partirá completamente desde cero y contendrá únicamente las estructuras compatibles con Odoo 19, garantizando así un entorno limpio y estable.

Este enfoque refleja una buena práctica habitual en despliegues reales: **cada versión mayor de Odoo debe disponer de su propia base de datos**, incluso aunque el resto de la infraestructura sea compartida.

---

## 2️⃣1️⃣ Acceso a pgAdmin y verificación del estado de bases de datos

Para gestionar PostgreSQL y trabajar con las bases de datos existentes, se utiliza la herramienta **pgAdmin**, que permite administrar visualmente el servidor de bases de datos.

![[Pasted image 20251223075147.png]]

Al acceder a pgAdmin se puede comprobar:

- La existencia de la base de datos utilizada por Odoo 18.
    
- El usuario de conexión configurado (`openpg`).
    
- El estado general del servidor PostgreSQL.
    

Desde este punto se procede a crear la nueva base de datos destinada a Odoo 19. Durante la creación se mantiene como propietario el usuario `openpg`, que es el usuario configurado por defecto en la instalación oficial de Odoo y el que aparece definido en el archivo `odoo.conf`.

![[Pasted image 20251223075232.png]]

La elección del propietario no es un detalle menor: Odoo solo podrá conectarse y operar sobre aquellas bases de datos para las que el usuario configurado en `odoo.conf` tenga permisos. Mantener coherencia entre **usuario de base de datos** y **configuración del servidor** evita errores de acceso posteriores.

![[Pasted image 20251223075244.png]]

Una vez creada, la nueva base de datos aparece listada junto a la de Odoo 18, lo que confirma que ambas pueden coexistir en el mismo servidor PostgreSQL sin interferirse.

---

## 2️⃣2️⃣ Por qué la base de datos recién creada está “vacía”

En este punto es importante entender qué significa “crear” una base de datos en PostgreSQL. Al crear una base de datos nueva, esta existe a nivel técnico, pero **no contiene ninguna de las tablas ni estructuras que Odoo necesita para funcionar**.

![[Pasted image 20251223075316.png]]

La base de datos recién creada está vacía en el sentido funcional:

- No hay tablas de usuarios.
    
- No existen módulos instalados.
    
- No hay menús, vistas ni configuraciones internas.
    

![[Pasted image 20251223075259.png]]

En otras palabras, el **núcleo del ERP aún no existe** dentro de esa base de datos. Por este motivo, si se intenta arrancar Odoo 19 apuntando directamente a esta base de datos, el sistema no puede funcionar correctamente, ya que le faltan las tablas mínimas necesarias para operar.

Odoo requiere un conjunto inicial de tablas internas —en torno a más de un centenar, dependiendo de la versión— que forman la base de su funcionamiento. Estas tablas incluyen desde la definición de usuarios y permisos hasta los modelos internos que permiten cargar módulos, vistas y configuraciones.

Por ello, es imprescindible **inicializar la base de datos** antes de poder utilizarla.

---

## 2️⃣3️⃣ Inicialización de la base de datos mediante Terminal y `-i base`

Para crear la estructura mínima necesaria en la base de datos de Odoo 19 se utiliza el método recomendado en instalaciones **on-premise**, que consiste en ejecutar el servidor de Odoo manualmente desde terminal y forzar la instalación del módulo base.

Este método permite un control total sobre el proceso y hace visible lo que normalmente ocurre de forma automática durante una instalación estándar. Al ejecutar Odoo desde terminal se puede observar cómo se cargan los módulos, se crean tablas y se inicializa el sistema paso a paso.

![[Pasted image 20251223075504.png]]

La inicialización mediante terminal es especialmente útil en este contexto porque:

- Permite trabajar con una base de datos ya creada manualmente.
    
- Garantiza que la estructura se adapte exactamente a la versión de Odoo utilizada.
    
- Evita conflictos con configuraciones automáticas del instalador.
    

Este proceso marca el punto en el que la base de datos pasa de ser un contenedor vacío a convertirse en una base de datos funcional para Odoo.

---

## 2️⃣4️⃣ Comando de arranque para crear tablas base

Para llevar a cabo la inicialización se ejecuta el siguiente comando desde el directorio de instalación de Odoo 19:

![[Pasted image 20251223075526.png]]

```powershell
.\python\python.exe .\server\odoo-bin -c .\server\odoo.conf -d db-odoo19 -i base
```

Este comando tiene una función muy concreta: **crear el núcleo mínimo de Odoo dentro de la base de datos**. Cada uno de sus parámetros cumple un papel esencial:

- Se utiliza el intérprete de Python incluido con Odoo para evitar conflictos con otras versiones de Python instaladas en el sistema.
    
- Se ejecuta el archivo `odoo-bin`, que es el punto de entrada del servidor Odoo.
    
- Se indica explícitamente el archivo de configuración `odoo.conf`, asegurando que se respeten los parámetros definidos (puerto, usuario de base de datos, etc.).
    
- Se especifica la base de datos destino (`db-odoo19`).
    
- Se fuerza la instalación del módulo **`base`**, que contiene el conjunto mínimo imprescindible de tablas y configuraciones.
    

El parámetro más importante en este proceso es **`-i base`**. Sin él, Odoo se limitaría a intentar conectarse a la base de datos sin crear la estructura necesaria, y la base de datos permanecería vacía e inutilizable.

Durante la ejecución del comando se puede observar en la terminal cómo se cargan numerosos recursos internos, como archivos XML y definiciones de modelos. Este proceso hace visible, de forma mucho más clara que durante una instalación automática, cómo Odoo construye internamente su núcleo de funcionamiento.

Cuando el comando finaliza sin errores, la base de datos ya contiene todas las tablas necesarias y está lista para ser utilizada por Odoo 19.

---

## 2️⃣5️⃣ Acceso a Odoo 19 desde el navegador (puerto 8070)

Una vez finalizado correctamente el proceso de inicialización de la base de datos, el siguiente paso consiste en comprobar que el servidor Odoo 19 es accesible y funcional desde el navegador web. Para ello, se introduce la siguiente dirección:

`http://localhost:8070`

El uso de este puerto confirma que se está accediendo específicamente a la instancia de **Odoo 19**, diferenciándola claramente de Odoo 18, que continúa ejecutándose en el puerto 8069. Este detalle es importante, ya que permite verificar que ambas versiones están activas de forma simultánea y completamente independientes entre sí.

En el primer acceso se utilizan las credenciales por defecto del sistema (`admin / admin`). Estas credenciales existen únicamente porque previamente se ha inicializado la base de datos con el módulo base, que crea el usuario administrador mínimo necesario para acceder al sistema.

Si el acceso se realiza correctamente, se muestra la pantalla principal de Odoo con el panel de aplicaciones. Además, observando la URL en el navegador se puede confirmar que el servidor responde efectivamente a través del puerto **8070**, lo que valida que la configuración del archivo `odoo.conf` ha sido aplicada correctamente y que no existe conflicto con la instancia de Odoo 18.

Este paso representa una verificación clave: el sistema ya no solo existe a nivel de archivos o base de datos, sino que **está operativo y accesible desde el exterior**, que es el objetivo final de todo el proceso de configuración.

---

## 2️⃣6️⃣ Verificación de tablas en pgAdmin tras inicializar la base de datos

Para completar la comprobación del correcto funcionamiento de Odoo 19, se vuelve a **pgAdmin** y se refresca el árbol de objetos de la base de datos `db-odoo19`.

Tras la actualización, se observa que la base de datos ya no está vacía y contiene un número elevado de tablas (134 en esta versión). Estas tablas corresponden al núcleo interno de Odoo e incluyen:

- Modelos base del sistema.
    
- Definición de usuarios y permisos.
    
- Estructura de módulos.
    
- Configuración de menús y vistas.
    
- Elementos internos necesarios para el arranque del ERP.
    

La presencia de estas tablas confirma que el comando ejecutado previamente con la opción `-i base` ha funcionado correctamente y que la base de datos ha sido inicializada de forma completa. Esta verificación es importante porque permite comprobar, desde el punto de vista de la base de datos, que el sistema está preparado para operar y no depende únicamente de que el navegador muestre una interfaz.

En este punto se puede afirmar que Odoo 19 dispone de una base de datos funcional, correctamente enlazada con su servidor y lista para instalar módulos adicionales o continuar con configuraciones más avanzadas.

---

## 2️⃣7️⃣ Regla clave: cada versión de Odoo requiere su propia base de datos

Una de las conclusiones más importantes de todo el proceso es que **cada versión mayor de Odoo debe trabajar con su propia base de datos**. Esta regla no es opcional ni una recomendación teórica, sino una necesidad técnica derivada de la evolución interna del software.

Entre versiones mayores, Odoo introduce cambios en:

- La estructura de tablas.
    
- Los módulos base.
    
- Los modelos de datos.
    
- Las relaciones internas entre entidades.
    

Por este motivo, reutilizar una base de datos antigua con una versión nueva del servidor puede provocar errores críticos o impedir directamente el arranque del sistema. Separar las bases de datos por versión evita estos problemas y permite trabajar con entornos limpios, controlados y reproducibles.

Este principio es aplicable tanto en entornos de prueba como en despliegues reales y explica por qué, en migraciones de versión, se utilizan procesos específicos de actualización y conversión de bases de datos en lugar de reutilizarlas directamente.

---

## 2️⃣8️⃣ Observación sobre `db_user` y credenciales de conexión

Durante toda la práctica se ha mantenido el usuario de base de datos `openpg`, que es el usuario creado por defecto por el instalador oficial de Odoo en Windows. Esta decisión simplifica la configuración inicial y permite centrarse en los aspectos clave del despliegue sin introducir complejidad adicional.

No obstante, en entornos reales o multicliente, sería habitual adoptar un enfoque más segmentado, creando usuarios distintos de PostgreSQL para cada instancia o proyecto. De este modo, se mejora la seguridad, se aíslan accesos y se controla de forma más precisa qué instancia puede acceder a cada base de datos.

En cualquier caso, este apartado pone de manifiesto la importancia del archivo `odoo.conf`, ya que es en él donde se definen las credenciales que el servidor utiliza en cada arranque. El hecho de que el comando ejecutado desde terminal haga referencia explícita a este archivo demuestra que `odoo.conf` no es solo un archivo de configuración pasivo, sino un elemento central en el funcionamiento del sistema.

Comprender la relación entre el servidor Odoo, el archivo de configuración y el usuario de base de datos es fundamental para entender cómo se controla el acceso a la información y cómo se evita que distintas instancias interfieran entre sí.

---

## 2️⃣9️⃣ Próximos pasos de configuración recomendados

Una vez completada la instalación y configuración básica de Odoo 18 y Odoo 19, el sistema se encuentra en un estado funcional, pero aún lejos de lo que sería una instalación completa o preparada para un uso continuado. En esta fase final se identifican una serie de configuraciones adicionales que, aunque no son estrictamente necesarias para el arranque inicial, resultan habituales y altamente recomendables en entornos más avanzados.

Estos pasos permiten mejorar la estabilidad del sistema, ampliar sus funcionalidades y acercar la instalación a un escenario más próximo al uso real de un ERP.

---

### Configuraciones aconsejables

Entre las configuraciones consideradas aconsejables se encuentran aquellas que amplían funcionalidades clave del sistema o facilitan su uso diario:

**`wkhtmltopdf`**  
Esta herramienta es fundamental para la generación de documentos PDF dentro de Odoo, como presupuestos, facturas o informes. Sin ella, muchas funciones de exportación no están disponibles o generan errores. Su instalación permite a Odoo convertir vistas HTML en documentos PDF de forma automática.

**SMTP**  
La configuración de un servidor SMTP permite a Odoo enviar correos electrónicos, lo que resulta esencial para notificaciones, confirmaciones de pedidos, envío de facturas o comunicación con clientes. Sin SMTP configurado, el sistema queda limitado a un uso muy básico y no puede interactuar correctamente con los usuarios externos.

**Filestore**  
El filestore es la carpeta donde Odoo almacena los archivos adjuntos, como documentos, imágenes o facturas. Configurarlo correctamente es importante para garantizar que los datos no se pierdan y que el sistema pueda gestionar correctamente los archivos asociados a cada registro.

**Ajustes avanzados de `odoo.conf`**  
En esta fase también resulta habitual profundizar en la configuración del archivo `odoo.conf`, ajustando parámetros relacionados con:

- Acceso a bases de datos.
    
- Rutas de módulos personalizados.
    
- Filtros de bases de datos visibles.
    
- Configuración del superadministrador.
    
- Optimización del comportamiento del servidor.
    

Estos ajustes permiten adaptar Odoo a las necesidades concretas del entorno en el que se ejecuta.

---

### Configuraciones muy recomendables

Además de las configuraciones anteriores, existen otras que, aunque requieren mayor conocimiento técnico, son consideradas buenas prácticas en cualquier instalación seria de Odoo:

**HTTPS detrás de un proxy**  
Publicar Odoo mediante HTTPS es fundamental para garantizar la seguridad de las comunicaciones. Habitualmente se utiliza un proxy inverso que gestiona el cifrado y redirige las peticiones al servidor Odoo, mejorando tanto la seguridad como el control del acceso.

**Copias de seguridad y restauración**  
Disponer de un sistema de copias de seguridad periódicas y pruebas de restauración es esencial para proteger los datos frente a fallos, errores humanos o problemas del sistema. No basta con crear copias: es imprescindible comprobar que pueden restaurarse correctamente.

**Gestión de logs y mantenimiento**  
La correcta gestión de registros (logs) permite detectar errores, analizar el comportamiento del sistema y realizar tareas de mantenimiento preventivo. Una política de higiene operativa evita la acumulación innecesaria de archivos y mejora la estabilidad del servidor a largo plazo.

---

### Resolución de errores comunes

Durante el uso y la ampliación de Odoo pueden aparecer errores relacionados con dependencias externas. Un ejemplo habitual es:

> `External dependency phonenumbers not installed`

Este error está relacionado con la validación de números de teléfono y suele aparecer al instalar determinados módulos o activar funciones concretas. En algunos casos puede resolverse desde el propio entorno de Odoo, mientras que en otros es necesario instalar librerías adicionales en el sistema.

Estos escenarios se abordarán en fases posteriores, ya que forman parte del uso avanzado y del mantenimiento habitual de una instalación de Odoo.

---
