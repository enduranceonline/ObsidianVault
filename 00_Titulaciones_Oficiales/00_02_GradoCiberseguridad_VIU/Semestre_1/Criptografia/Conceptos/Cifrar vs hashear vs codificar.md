---
asignatura: Criptografía (11GCIB)
tipo: concepto
origen: "[[S01 - Tutoría inicial]]"
tags: [criptografia, conceptos, cifrado, hash, codificacion]
---

# Cifrar vs hashear vs codificar

Las tres transforman datos, pero con **objetivos distintos**. La pregunta clave es: *¿se puede volver atrás, y quién puede hacerlo?*

| | **Codificar** | **Cifrar** | **Hashear** |
|---|---|---|---|
| Objetivo | Representar datos en otro formato | **Confidencialidad**: que solo lo lea quien tenga la clave | **Integridad**: obtener una "huella" de los datos |
| ¿Usa clave? | No | Sí | No (salvo HMAC) |
| ¿Reversible? | Sí, por cualquiera | Sí, solo con la clave | **No** (función de un solo sentido) |
| Longitud de salida | Depende de la entrada | Depende de la entrada | **Fija** (p. ej. 256 bits en SHA-256) |
| ¿Da seguridad? | Ninguna | Sí | Sí, para comprobar, no para ocultar y recuperar |
| Ejemplos | Base64, hexadecimal, ASCII, UTF-8, URL encoding, Morse | César, Atbash, Vigenère, AES, RSA | MD5 (roto), SHA-1 (roto), SHA-256, SHA-3; para contraseñas: bcrypt, Argon2 |

## Codificar

Cambiar la **representación** de los datos para que un sistema los pueda transmitir o almacenar. El algoritmo es público y no hay secreto: cualquiera puede decodificar.

```text
"hola" → Base64 → aG9sYQ==
"hola" → hex    → 686f6c61
```

> [!warning] Base64 no es cifrado
> Un error clásico es "proteger" contraseñas o tokens en Base64. Se revierte en un segundo. En los CTF, un texto que acaba en `=` o `==` suele ser Base64: es una de las primeras cosas a probar.

## Cifrar

Transformar el texto claro en texto cifrado usando un **algoritmo + una clave**. El algoritmo puede ser público; la seguridad está en la clave (**principio de Kerckhoffs**).

```text
cifrar(texto claro, clave)    → texto cifrado
descifrar(texto cifrado, clave) → texto claro
```

- **Simétrico**: la misma clave cifra y descifra (César, AES).
- **Asimétrico**: clave pública para cifrar, privada para descifrar (RSA). Lo veremos en los temas de clave privada y pública.

Los cifrados modernos añaden aleatoriedad, así que el mismo texto con la misma clave da salidas distintas:

```text
"hola" + AES-256 + clave123 → U2FsdGVkX1/nSks6C1xgu5RDyR8qprj5ryp/uVcP9Mc=
"hola" + AES-256 + clave123 → U2FsdGVkX19J4gSm7m3ljII7nAFsYeyfmAkHzLZOGys=
```

(La salida de AES aquí además va **codificada** en Base64 para poder mostrarla como texto: cifrado y codificación suelen ir juntos.)

> [!note] ¿Y ROT13?
> Técnicamente es un cifrado César con clave 13. Pero como la clave es fija y conocida, en la práctica funciona como una **codificación u ofuscación**: no protege nada. Lo mismo pasa con Atbash, que no tiene clave. Los cifrados de la [[S01 - Tutoría inicial|sesión 1]] son cifrados clásicos: históricos y didácticos, pero rotos.

## Hashear

Una función hash convierte una entrada **de cualquier tamaño** en una salida **de tamaño fijo**. Propiedades:

1. **Determinista**: la misma entrada siempre da el mismo hash.
2. **Un solo sentido**: no se puede obtener la entrada a partir del hash.
3. **Efecto avalancha**: un cambio mínimo cambia el hash por completo.
4. **Resistente a colisiones**: debe ser inviable encontrar dos entradas con el mismo hash.

```text
SHA-256("hola")             → b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79
SHA-256("Hola")             → e633f4fc79badea1dc5db970cf397c8248bac47cc3acf9915ba60b5d76b0e88f
SHA-256(texto de 180.000 c.) → e2457c12d64e611534a36a46d6216f195b1160930533e5e0f3cb4c867f00ccd8
```

Una sola mayúscula cambia todo, y un texto enorme da un hash de la misma longitud.

Usos:
- **Contraseñas**: el servidor no guarda tu contraseña, guarda su hash. Al hacer login, hashea lo que escribes y compara.
- **Integridad de archivos**: comparar el hash publicado de una descarga con el del archivo descargado.
- **Firmas digitales** y **blockchain**.

> [!important] "Romper" un hash no es descifrarlo
> No se revierte: se **adivina**. Se hashean millones de candidatos (diccionario, fuerza bruta) hasta que uno coincide, o se buscan en tablas precalculadas (*rainbow tables*). Por eso:
> - Las contraseñas se guardan con **sal** (un valor aleatorio por usuario) y con funciones **lentas a propósito** (bcrypt, scrypt, Argon2), no con un SHA-256 a secas.
> - Las contraseñas largas, como las "tres palabras aleatorias" del NCSC, multiplican el número de candidatos a probar.
>
> MD5 y SHA-1 se consideran rotos: se han encontrado colisiones.

## Cómo distinguirlos en un reto

- ¿Solo caracteres `A-Z a-z 0-9 + /` y quizá `=` al final? → probablemente **Base64**.
- ¿Solo `0-9 a-f` con longitud fija? 32 caracteres → MD5 · 40 → SHA-1 · 64 → SHA-256. Probablemente un **hash**: no se descifra, se busca o se adivina.
- ¿Palabras de la misma longitud que el original, letras "movidas"? → **cifrado clásico** (César, Atbash, sustitución): análisis de frecuencias.
- ¿Bytes aleatorios sin patrón y sin longitud fija? → probablemente **cifrado moderno**: hace falta la clave.

## Regla mnemotécnica

- **Codificar** → *formato* (cualquiera lo revierte)
- **Cifrar** → *secreto* (solo quien tiene la clave lo revierte)
- **Hashear** → *huella* (nadie lo revierte, solo se compara)
