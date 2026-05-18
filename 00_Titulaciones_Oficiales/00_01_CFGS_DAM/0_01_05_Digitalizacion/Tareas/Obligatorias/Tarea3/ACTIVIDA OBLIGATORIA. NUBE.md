# Ejercicio 1: Funciones de la nube

La computación en la nube se ha convertido en uno de los pilares fundamentales de la digitalización actual, tanto a nivel personal como empresarial. A continuación, se desarrollan sus principales características, ventajas y riesgos asociados.

## ¿Qué es la nube?

La computación en la nube es un modelo de prestación de servicios informáticos que permite el acceso remoto, a través de Internet, a recursos tecnológicos como servidores, almacenamiento, aplicaciones y sistemas de procesamiento. Estos recursos no residen en el equipo del usuario, sino en centros de datos gestionados por proveedores especializados, que garantizan su disponibilidad, mantenimiento y escalabilidad.

Gracias a este modelo, los usuarios pueden utilizar software y servicios sin necesidad de instalar programas localmente ni disponer de infraestructuras propias, pagando generalmente solo por los recursos que utilizan.

## Ventajas principales de la nube

Una de las principales ventajas de la nube es la accesibilidad. Los servicios en la nube pueden utilizarse desde cualquier lugar y dispositivo con conexión a Internet, lo que facilita el teletrabajo y la colaboración entre usuarios.

Otra ventaja destacable es la escalabilidad. La nube permite adaptar los recursos tecnológicos a las necesidades reales de cada momento, aumentando o reduciendo la capacidad de almacenamiento o procesamiento sin necesidad de realizar inversiones en hardware.

Asimismo, la nube supone un importante ahorro de costes, ya que elimina la necesidad de adquirir y mantener infraestructuras propias, trasladando esa responsabilidad al proveedor del servicio. Además, muchos servicios incluyen actualizaciones automáticas y copias de seguridad.

Por último, la nube favorece el trabajo colaborativo, permitiendo que varios usuarios accedan y trabajen de forma simultánea sobre los mismos documentos o aplicaciones.

## Desventajas o riesgos y medidas para reducirlos

Uno de los principales riesgos de la computación en la nube es la dependencia de la conexión a Internet. En caso de fallos de red, el acceso a los servicios puede verse interrumpido. Para reducir este riesgo, es recomendable disponer de conexiones alternativas o mantener copias locales de la información más crítica.

Otro aspecto relevante es la seguridad y la privacidad de los datos. Al almacenarse la información en servidores externos, existe el riesgo de accesos no autorizados o brechas de seguridad. Para minimizar este problema, es fundamental utilizar sistemas de cifrado, contraseñas seguras y mecanismos de autenticación multifactor, así como elegir proveedores que cumplan con normativas de protección de datos.

---

# Ejercicio 2: Fog, Mist y Edge Computing

El crecimiento del Internet de las Cosas (IoT) y de los sistemas en tiempo real ha impulsado nuevos modelos de procesamiento de datos complementarios a la nube tradicional, como el edge, fog y mist computing.

## Explicación de los conceptos

El edge computing se basa en procesar los datos lo más cerca posible de su origen, normalmente en el propio dispositivo o en un nodo cercano, como un router o una pasarela de red. De este modo, se evita enviar toda la información a la nube.

El fog computing actúa como una capa intermedia entre el edge y la nube. En este modelo, el procesamiento se realiza en servidores o nodos locales cercanos a los dispositivos, permitiendo una gestión más eficiente de grandes volúmenes de datos.

El mist computing representa el nivel más básico de procesamiento, ya que se lleva a cabo directamente en sensores o microcontroladores con recursos muy limitados. Estos dispositivos realizan operaciones simples, como la detección de umbrales o la activación de alertas.

## Ventajas que aportan estos modelos

La principal ventaja del edge, fog y mist computing es la reducción de la latencia, ya que los datos se procesan localmente sin necesidad de enviarlos a centros de datos lejanos. Esto resulta esencial en aplicaciones que requieren respuestas inmediatas.

Además, estos modelos reducen el tráfico de red y el consumo de ancho de banda, ya que solo se envía a la nube la información realmente relevante. También mejoran la fiabilidad del sistema, al permitir que ciertos procesos sigan funcionando incluso si la conexión con la nube se interrumpe.

## Ejemplos reales

Un ejemplo de edge computing sería una cámara de videovigilancia capaz de detectar movimiento y generar alertas sin necesidad de enviar continuamente vídeo a la nube.

En el caso del fog computing, se puede citar una planta industrial en la que un servidor local analiza los datos de múltiples sensores antes de enviarlos a un sistema central.

Como ejemplo de mist computing, se encuentran los sensores de temperatura que detectan valores anómalos y activan una señal de aviso de forma autónoma.

## Representación del modelo

```mermaid
graph TD
    A[ Sensores y dispositivos (Mist) ] --> B[ Nodos cercanos / Edge ]
    B --> C[ Servidores intermedios (Fog) ]
    C --> D[ Nube (Cloud) ]
```

---

# Ejercicio 3: Identificación de niveles de la nube

La computación en la nube se organiza habitualmente en tres niveles de servicio: SaaS, PaaS e IaaS, en función del grado de control que tiene el usuario.

## Clasificación de los ejemplos

El uso de Google Docs para redactar y compartir documentos en línea corresponde al modelo SaaS (Software as a Service), ya que el usuario utiliza directamente una aplicación sin preocuparse por la infraestructura o la plataforma.

El desarrollo de aplicaciones en Google App Engine se encuadra dentro del modelo PaaS (Platform as a Service), puesto que el proveedor ofrece un entorno de desarrollo completo donde el programador se centra únicamente en el código.

Por último, el uso de Amazon EC2 para alojar servidores virtuales pertenece al modelo IaaS (Infrastructure as a Service), ya que se proporciona infraestructura virtual sobre la que el usuario tiene un control avanzado.

## Tipos de usuarios que utilizan cada nivel

El modelo SaaS está orientado principalmente a consumidores finales y empresas que necesitan utilizar aplicaciones de forma sencilla y directa.

El modelo PaaS es utilizado mayoritariamente por programadores y desarrolladores, ya que les permite crear y desplegar aplicaciones sin gestionar servidores.

El modelo IaaS está dirigido a empresas, administradores de sistemas y perfiles técnicos que requieren un control total sobre la infraestructura y la configuración del sistema.