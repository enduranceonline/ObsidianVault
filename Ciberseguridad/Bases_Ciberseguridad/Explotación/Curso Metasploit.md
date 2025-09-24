#metasploit

---
# 📑 Agenda - Curso Metasploit Framework Multiplataforma

## 1. Introducción
- Metasploit  
- Arquitectura  
- Estructura de Metasploit  
- Módulos y sus tipos  
- Comandos  
- Configuración y automatización  

## 2. Reconocimiento, enumeración y pentesting
- ¿Qué es un módulo **Auxiliary**?  
- Escáneres  
- Técnicas aplicadas de reconocimiento  
- Servidores  

## 3. Explotación
- Tipos de explotación  
- Configuración de módulos  
- Explotación en diferentes sistemas  

## 4. Post-Explotación
- Meterpreter  
- Comandos  
- Módulos  
- Pivoting  
- Movimiento lateral  

---
# 🧪 Make Lab - Laboratorios en VirtualBox

## Máquinas a utilizar
- **Kali Linux 2020.3**  
- **Windows 10**  
- **Windows 7**  
- **Mini Linux hca.iso** → [Descarga](http://hackersclub.academy/hca.iso)  
- **Ubuntu** (versión indiferente)  
- **Metasploitable2**  
- **Docker** (para algunos contenedores)  

## Notas
- Todas estas máquinas se pueden instalar y gestionar en **VirtualBox**.  
- Es recomendable configurar una **red interna** o **host-only** para aislar el laboratorio del resto de la red.  
- Algunas prácticas requerirán **Docker**, por lo que puede ejecutarse dentro de una VM de Ubuntu/Kali o directamente en el host si se prefiere.  

---
# 📘 Introducción

### ❓ Conceptos clave
- **¿Qué es un bug?**  
  Error o fallo en el software que provoca un comportamiento inesperado.

- **¿Qué es una vulnerabilidad?**  
  Debilidad en el sistema que puede ser explotada para comprometer la seguridad.

- **¿Qué es el software fiable?**  
  Software que funciona de manera consistente y predecible.

- **¿Qué es un software seguro?**  
  Software diseñado para resistir ataques y proteger datos/sistemas.

- **¿Qué es un exploit?**  
  Programa o técnica que aprovecha una vulnerabilidad para ejecutar acciones no autorizadas.  

- **¿Qué es una shellcode?**  
  Código ejecutable usado como parte de un exploit, normalmente para abrir una shell.  

- **¿Qué es un payload?**  
  Carga útil del exploit, es decir, lo que se ejecuta después de aprovechar la vulnerabilidad.  

- **¿Qué es un (exploit) 0day?**  
  Vulnerabilidad desconocida para el fabricante y sin parche disponible.  


# 🛠️ Metasploit

### ❓ ¿Qué es?
- **Framework de explotación**.  
- **No es un escáner de vulnerabilidades**.  

### 📂 Componentes principales
- **msfconsole** → Interfaz principal en consola para interactuar con Metasploit.  
- **msfd** → Permite ejecutar Metasploit en modo servicio y aceptar conexiones externas.  
- **msfvenom** → Generador de payloads personalizados y shellcodes.  
- **msfrpc / msfrpcd** → Comunicación con Metasploit a través de RPC (Remote Procedure Call), útil para automatización.  
- **msfupdate** → Actualiza la base de datos de exploits y módulos de Metasploit.  
- **msfelfscan** → Analiza binarios ELF (Linux) para detectar posibles vulnerabilidades.  
- **msfpayload** → (Obsoleto, reemplazado por msfvenom) permitía generar payloads.  
- **msfencode** → Herramienta de codificación/obfuscación para evitar detección (también absorbida por msfvenom).  
- **msfrop** → Ayuda a crear cadenas ROP (Return-Oriented Programming) para explotación avanzada.  
- **msfbinscan** → Escaneo de binarios en busca de patrones de explotación.  
- **lib / modules** → Librerías y repositorios de módulos (exploits, payloads, auxiliares, etc.).  

### 🎯 ¿Para qué usarlo?
- Investigación en explotación.  
- Pentesting.  

### 🔧 Otros kits de explotación
- **CORE Impact** → Framework comercial de explotación, con soporte avanzado para pruebas en entornos corporativos. Se enfoca en integración con entornos empresariales, reportes automáticos y simulaciones de ataques reales.  
- **CANVAS** → Toolkit comercial de explotación, muy usado en entornos de investigación. Incluye exploits actualizados y herramientas para ingeniería inversa.  

### 📦 Versiones de Metasploit
- **Community (gratuita):**  
  - Uso básico.  
  - Interfaz limitada.  
  - Menor automatización.  
  - Ideal para aprendizaje y laboratorios.  

- **Pro (comercial):**  
  - Escaneo de vulnerabilidades integrado.  
  - Automatización avanzada de exploits.  
  - Generación de reportes profesionales.  
  - Integración con herramientas de gestión de seguridad (Nexpose, etc.).  
  - Soporte técnico y actualizaciones premium.  

---
# 🏗️ Arquitectura de Metasploit

La arquitectura de Metasploit se organiza en **capas**, donde cada elemento cumple un rol específico y se interconecta para ofrecer un framework flexible y modular.

---

## 📦 Módulos de Metasploit
Metasploit cuenta con **7 tipos de módulos** principales:

1. **Exploit**  
   - Código que aprovecha una vulnerabilidad en el sistema objetivo.  
   - Lanza el ataque inicial.  

2. **Payloads**  
   - Carga útil que se ejecuta tras el exploit (ejemplo: una shell reversa, meterpreter, etc.).  
   - Define qué hará el atacante después de comprometer el sistema.  

3. **Auxiliary**  
   - Módulos que no generan acceso directo, pero permiten reconocimiento, escaneo, fuzzing, sniffing, etc.  
   - Ejemplo: escaneo de puertos o fuerza bruta.  

4. **Post**  
   - Acciones después de la explotación.  
   - Ejemplo: escalada de privilegios, exfiltración de credenciales, movimiento lateral.  

5. **Encoders**  
   - Codifican payloads para evadir antivirus o IDS/IPS.  
   - Ayudan a evitar detección mediante ofuscación. 

6. **Nops (No Operation)**  
   - Rellenos que aseguran estabilidad en la ejecución del exploit.  
   - Preparan la memoria para que el payload funcione correctamente.  

7. **Evasion (evasión)**  
   - Módulos diseñados específicamente para **evadir mecanismos de seguridad modernos** como antivirus, EDR o firewalls.  
   - Más avanzados que los encoders clásicos.  

---

## 📚 Librerías
Las librerías son el **corazón funcional** de Metasploit:  
- **REX (Ruby Exploitation Library):** provee funciones de red, sockets, protocolos, cifrado, etc.  
- **MSF CORE:** capa de abstracción que coordina librerías y módulos.  
- **MSF BASE:** lo más bajo del framework, maneja estructuras de datos, interacciones con módulos y plugins.  

👉 **MSF CORE y BASE interactúan constantemente:**  
- **BASE** es la parte más cruda (estructura básica del framework).  
- **CORE** abstrae y organiza, permitiendo que los módulos funcionen sin preocuparse por detalles bajos.  

---

## 🛠️ Herramientas
- Scripts y utilidades adicionales que extienden Metasploit.  
- Usan librerías y módulos para facilitar la automatización.  

---

## 🔌 Plugins
- Complementos que extienden las capacidades del framework.  
- Se integran con **MSF BASE** para añadir funcionalidades externas (ejemplo: integraciones con bases de datos, reporting, etc.).  

---

## 💻 Interfaces
Metasploit ofrece varias formas de interacción:  

>**Consola (`msfconsole`)**  
  >- La más usada y potente.  
  >- Es la interfaz principal del curso.  

>**CLI**  
  >- Permite automatizar mediante scripts.  
  >- Útil para ejecutar tareas rápidas con comandos directos.  

>**Web**  
  >- Interfaz accesible vía navegador.  
  >- Menos usada actualmente, más experimental.  

>**GUI**  
  >- Interfaz gráfica amigable (ejemplo: **Armitage**).  
  >- Orientada a quienes prefieren entorno visual.  

---

## 🔄 Cómo interactúan todos los componentes

1. **El usuario** accede mediante una **interfaz** (consola, CLI, web o GUI).  
2. Esta interfaz se comunica con el **MSF CORE** (capa de abstracción).  
3. **MSF CORE** gestiona las peticiones usando **REX** y **MSF BASE**.  
4. **MSF BASE** conecta con los **módulos** (exploit, payload, auxiliary, etc.).  
5. Opcionalmente, se pueden añadir **plugins** y **herramientas** que amplían la funcionalidad.  
6. El flujo final permite ejecutar exploits, cargar payloads y realizar post-explotación.  

---
