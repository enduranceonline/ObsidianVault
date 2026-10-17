---
asignatura: Estadística e investigación operativa
tipo: tema
tema: Introducción a la estadística y la investigación operativa
fuentes: "[[03GCIB-sesión_1.pdf]] (diap. 4-15)"
clases: "[[EIO-clase01]]"
estado: sesión 1 cubierta; los conceptos técnicos se formalizan en sesiones posteriores
---

# Introducción a la estadística y la investigación operativa

> [!note] Convención de esta nota
> Lo que viene de la presentación lleva la referencia (diap. N). Lo marcado como *(añadido)* es ampliación mía que no está en el material del curso.

## 1. Intuición

Un sistema de seguridad genera muchísimos datos (conexiones, logins, transferencias). Nadie puede mirarlos uno a uno. La estadística sirve para dos cosas:

1. **Definir qué es "normal"** (un promedio y cuánto se suele desviar de él).
2. **Detectar lo que se aleja de lo normal** y valorar cuán improbable es.

La investigación operativa (IO) da el paso siguiente: una vez detectado el problema, **decidir cómo actuar de la mejor manera posible** con recursos limitados.

> [!tip] Idea que repitió el profesor
> Las conclusiones se sacan comparando lo observado con el comportamiento normal (la media) y valorando la probabilidad de esa desviación. Prioridad de estudio: **entender bien el promedio**.

## 2. Estadística en ciberseguridad (diap. 4)

Los sistemas de ciberseguridad analizan tráfico, accesos o archivos sospechosos para identificar **anomalías** (desviaciones del comportamiento normal). La estadística convierte datos de seguridad en información útil para **detectar, analizar, predecir y responder** a amenazas.

Aplicaciones citadas en la presentación:
- Calcular **umbrales** (promedios, desviaciones estándar).
- Construir **modelos probabilísticos** que indiquen anomalías.
- Detectar tendencias en malware o intrusiones, y clasificar ataques por similitud o frecuencia.
- Detectar bots o comportamientos automatizados.
- Calcular la probabilidad de un ataque y estimar su impacto.
- En un IDS: medir **tasas de falsos positivos y negativos**, optimizar umbrales de alerta y evaluar el rendimiento.

## 3. Investigación operativa (diap. 5-6)

> [!definition] Investigación operativa (IO)
> Su objetivo principal es **optimizar algún aspecto de un proceso**: minimizar costes, maximizar ganancias, reducir tiempos, mejorar la eficiencia, asignar recursos (diap. 5).

| Ámbito | Para qué se usa la IO (diap. 5) |
|---|---|
| IDS | Priorizar alertas y asignar recursos de cómputo |
| Firewalls y redes | Elegir rutas más seguras y eficientes, minimizar retrasos, detectar cuellos de botella |
| Malware | Clasificar archivos sospechosos, elegir características óptimas, reducir falsos positivos |
| Respuesta a un ciberataque | Asignar personal según la urgencia y minimizar el tiempo de contención (detección → contención → recuperación) |

> [!tip] Eficacia y eficiencia *(añadido)*
> **Eficacia**: lograr el objetivo. **Eficiencia**: lograrlo con el mínimo de recursos (tiempo, coste, cómputo). La IO persigue la segunda.

La asignatura es una introducción a estas dos áreas, indispensables en ciberseguridad (diap. 6).

## 4. Qué es la estadística (diap. 8-9)

> [!definition] Estadística
> Ciencia que se encarga de **recolectar, organizar, analizar e interpretar** datos para ayudar a tomar decisiones o comprender mejor un fenómeno. (diap. 8)
>
> Cuatro pasos: reúne datos (encuestas, mediciones, observaciones) → los organiza (tablas, gráficos) → los analiza (medias, porcentajes, variabilidad, relaciones) → extrae conclusiones para describir lo que ocurre o predecir lo que podría ocurrir.

### 4.1 Descriptiva e inferencial (diap. 9)

| Rama | Definición (diap. 9) | Ejemplo en ciberseguridad *(añadido)* |
|---|---|---|
| **Descriptiva** | Resume y describe datos (gráficos, promedios, medianas, desviaciones) | Resumir el log del mes: tráfico medio diario 5 000 conexiones, con un histograma por horas |
| **Inferencial** | Usa una **muestra** para hacer inferencias o predicciones sobre una **población** más grande (intervalos de confianza, pruebas de hipótesis) | Auditar 200 equipos y estimar, con un intervalo de confianza, el porcentaje infectado de los 10 000 de la empresa |

> [!warning] Cómo distinguirlas *(añadido)*
> Si te limitas a describir los datos que tienes, es descriptiva. Si das el salto de esos datos a algo que no has medido (el resto de la población, el futuro), es inferencial.

## 5. Población, muestra y probabilidad (diap. 14-15)

> [!definition] Población, censo y muestra (diap. 15)
> - **Población de interés**: colección bien definida de objetos sobre los que se enfoca una investigación.
> - **Censo**: la información está disponible para **todos** los objetos de la población. Casi siempre es impráctico por restricciones de tiempo, dinero y recursos.
> - **Muestra**: subconjunto de la población, seleccionado de manera prescrita.

La Figura 1.2 (diap. 14) relaciona las dos ideas con dos flechas:

```mermaid
flowchart LR
    P([Población]) -- "Probabilidad" --> M([Muestra])
    M -- "Estadística inferencial" --> P
```

> [!tip] Cómo leer la figura *(añadido)*
> - **Probabilidad** (población → muestra): conozco la población y pregunto qué muestras son esperables.
> - **Inferencia** (muestra → población): tengo una muestra y pregunto qué puedo decir de la población.
>
> Conexión con conjuntos: población = conjunto; muestra = subconjunto. Ver [[EIO-Tema-TeoriaConjuntos]].

## 6. Casos prácticos (diap. 10-13)

Todos siguen el mismo patrón: **comportamiento normal → observación → desviación → alerta**.

| Caso | Normal | Observado | Conclusión de la diap. |
|---|---|---|---|
| 1. Intrusión por tráfico (diap. 10) | Promedio diario 5 000 conexiones, desviación estándar 300 | 12 000 en una noche | Evento fuera de rango: posible DDoS o escaneo masivo |
| 2. Fuerza bruta (diap. 11) | 5-15 intentos de login por hora | 1 200 en una hora, desde IP secuenciales | Probable ataque automatizado de fuerza bruta |
| 3. Exfiltración (diap. 12) | 30-50 MB al día | 4 GB a un dominio desconocido | Posible robo de datos internos (*insider threat*) |
| 4. Fraude bancario (diap. 13) | Compras pequeñas en su país | Compras de miles de dólares en otro continente | Posible tarjeta clonada; mismo principio para cuentas comprometidas |

> [!example] Caso 1 con números *(añadido)*
> Aquí **promedio** $\mu=5000$ y **desviación estándar** $\sigma=300$ (conceptos que se formalizarán más adelante). ¿A cuántas desviaciones está el dato de 12 000?
> $$z=\frac{x-\mu}{\sigma}=\frac{12000-5000}{300}\approx 23{,}3$$
> Un valor así de alejado es casi imposible bajo el comportamiento normal, por eso salta la alerta.
> Orden de magnitud en el caso 2: $1200/15=80$ veces el máximo habitual.

### Los tres conceptos que aparecen sin definir

> [!definition] Qué significan (intuición, se formalizan más adelante) *(añadido)*
> - **Promedio** ($\mu$ o $\bar{x}$): el valor "típico" alrededor del cual se reparten los datos. **Prioridad de estudio.**
> - **Desviación estándar** ($\sigma$): cuánto se suelen separar los datos del promedio (la "anchura" de lo normal).
> - **Modelo estadístico**: una descripción probabilística del comportamiento normal, que permite decir cuán improbable es una observación.

```python
# Comprobación del caso 1 y de la idea de muestra frente a población
import numpy as np

mu, sigma, x = 5000, 300, 12000
print((x - mu) / sigma)                 # 23.33...

rng = np.random.default_rng(0)
poblacion = rng.normal(mu, sigma, 10_000)       # "todo el tráfico" (simulado)
muestra = rng.choice(poblacion, 200, replace=False)   # subconjunto
print(poblacion.mean(), muestra.mean())  # la media muestral estima la poblacional
```

## 7. Conexiones

- **Teoría de conjuntos:** población y muestra como conjunto y subconjunto → [[EIO-Tema-TeoriaConjuntos]].
- **Criptografía:** la probabilidad aparece en el análisis de seguridad (por ejemplo, de claves y ataques de fuerza bruta).
- **Lógica y matemática discreta:** los problemas en redes de la parte de IO usan grafos.
- **En esta asignatura (temario de la Guía):** probabilidad y variable aleatoria → inferencia → programación lineal → regresión → redes.

## 8. Pendiente de ampliar

- [ ] Promedio, desviación estándar y modelo estadístico, cuando el profesor los formalice.
- [ ] Falsos positivos y negativos en un IDS: cuándo se vean los contrastes de hipótesis.
- [ ] Intervalos de confianza y pruebas de hipótesis (inferencial).
- [ ] Programación lineal y redes (IO).
- [ ] Revisar qué tipos de muestreo se trabajan más adelante.

## Glosario

| Término | Significado |
|---|---|
| Anomalía | Desviación del comportamiento normal (diap. 4) |
| Umbral | Valor a partir del cual se dispara una alerta (calculado con promedios y desviaciones) |
| IDS | Sistema de detección de intrusiones |
| IO | Investigación operativa |
| Población | Colección bien definida de objetos de interés (diap. 15) |
| Censo | Información de todos los objetos de la población (diap. 15) |
| Muestra | Subconjunto de la población (diap. 15) |
