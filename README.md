# Reto No. 12: "Ya casi vacaciones"
Métodos de Strings y ejercicios de procesamiento de archivo

### 1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

## Métodos de strings en Python:

- endswith: retorna True si la cadena termina con la subcadena especificada.

Sintaxis: cadena.endswith("subcadena", inicio, fin)

```python
texto = "Hola, ¿cómo estás?"
print(texto.endswith("?"))  # Devuelve True
print(texto.endswith("!"))  # Devuelve False
```

- startswith: Retorna True si la cadena inicia con la subcadena especificada. 

Sintaxis: cadena.startswith("subcadena", inicio, fin)
```python
texto = "Hola, ¿cómo estás?"
print(texto.startswith("Hola"))  # Devuelve True
print(texto.startswith("Adiós"))  # Devuelve False
```
- isalpha: Retorna True cuando los elementos de la cadena son letras (caracteres alfabéticos).

Sintaxis: cadena.isalpha()
```python
texto = "Hola"
print(texto.isalpha())  # Devuelve True

texto = "Hola123"
print(texto.isalpha())  # Devuelve False

```
- isalnum: Retorna True cuando la cadena es alfanumérica.

Sintaxis: cadena.isalnum()
```python
texto = "Hola123"
print(texto.isalnum())  # Devuelve True

texto = "Hola!"
print(texto.isalnum())  # Devuelve False
```
- isdigit: Retorna True cuando la cadena está compuesta por dígitos numéricos.

Sintaxis: cadena.isdigit()
```python
texto = "123"
print(texto.isdigit())  # Devuelve True

texto = "Hola123"
print(texto.isdigit())  # Devuelve False
```
- isspace: Retorna True cuando todos los caracteres de la cadena son espacios.

Sintaxis: cadena.isspace()
```python
texto = "   "
print(texto.isspace())  # Devuelve True

texto = "Hola"
print(texto.isspace())  # Devuelve False
```
- istitle: Retorna True cuando todas las palabras de la cadena tienen su primera letra en mayúscula y el resto de las letras en minúscula. Este método solo revisa los caracteres del abecedario, es decir, ignora los símbolos, números y espacios.

Sintaxis: cadena.istitle()
```python
texto = "Hola, ¿Cómo Estás?"
print(texto.istitle())  # Devuelve True

texto = "Hola, ¿Cómo estás?"
print(texto.istitle())  # Devuelve False
```
- islower: Retorna True cuando todos los caracteres de la cadena están en minúsculas. Este método solo revisa los caracteres del abecedario, es decir, ignora los símbolos, números y espacios.

Sintaxis: cadena.islower()
```python
texto = "hola"
print(texto.islower())  # Devuelve True

texto = "Hola"
print(texto.islower())  # Devuelve False
```

- isupper: Retorna True cuando todos los caracteres de la cadena están en mayúsculas. Este método solo revisa los caracteres del abecedario, es decir, ignora los símbolos, números y espacios.
  
Sintaxis: cadena.isupper()
```python
texto = "HOLA"
print(texto.isupper())  # Devuelve True

texto = "Hola"
print(texto.isupper())  # Devuelve False
```


### 2. Procesar el "mbox-short.txt" y extraer:

- Cantidad de vocales:

```python
def contar_vocales(texto: str):   # Función que cuenta las vocales
    vocales = 0                   # Inicializar el contador de vocales en 0
    for letra in texto:           # Iterar sobre cada letra en el texto
        if letra in "aeiouAEIOU": # Verificar si la letra está en el conjunto de vocales
            vocales += 1          # Incrementar el contador de vocales
    return vocales                # Retornar el total de vocales

with open("mbox-short.txt", 'r') as file:  # Abrir el archivo "mbox-short.txt" en modo lectura
    texto = file.read()   # Lee todo el contenido del archivo y lo guarda en la variable "texto"

# Llama a la función contar_vocales con el contenido del archivo como argumento
cantidad_vocales = contar_vocales(texto)

# Imprimir la cantidad de vocales en el texto
print("La cantidad de vocales en el texto es: " + str(cantidad_vocales))
```

- Cantidad de consonantes:

```python
def contar_consonantes(texto: str):  # Función que cuenta las consonantes
    consonantes = 0                  # Inicializamos el contador de consonantes en 0
    for letra in texto:              # Iterar sobre cada letra en el texto
        if letra.isalpha() and letra not in "aeiouAEIOU": # Verificar si la letra es un carácter alfabético y no es una vocal
            consonantes += 1         # Incrementar el contador de consonantes
    return consonantes               # Retornar el total de consonantes

with open("mbox-short.txt", 'r') as file:  # Abre el archivo "mbox-short.txt" en modo lectura
    texto = file.read()   # Lee todo el contenido del archivo y lo guarda en la variable "texto"

# Llama a la función contar_consonantes con el contenido del archivo como argumento
cantidad_consonantes = contar_consonantes(texto)

# Imprime la cantidad de consonantes en el texto
print("La cantidad de consonantes en el texto es: " + str(cantidad_consonantes))
```

- Listado de las 50 palabras que más se repiten:

  ```python
  def palabras_repetidas(texto: str):  # Función que busca las palabras más repetidas en un texto
    texto = texto.lower()            # Convertir todo el texto a minúsculas

    numero_de_palabras = {}          # Diccionario para almacenar el número de ocurrencias de cada palabra

    for s in texto:                  # Reemplazar los caracteres que no son letras ni espacios por espacios en blanco
        if not s.isalpha() and s != " ":
            texto = texto.replace(s, " ")

    archivo = texto.split()          # Dividir el texto en palabras individuales

    for l in archivo:                # Contar el número de ocurrencias de cada palabra
        if l not in numero_de_palabras:  # Si la palabra aún no está en el diccionario, la inicializamos en 0
            numero_de_palabras[l] = 0
        numero_de_palabras[l] += 1   # Incrementar el contador de ocurrencias de la palabra

    # Imprimimos las palabras más repetidas (hasta las 50 más repetidas)
    for s in sorted(numero_de_palabras, reverse=True, key=lambda s: numero_de_palabras[s])[:51]:
        print("La palabra: {} \tSe repite {} \tveces en el archivo".format(s, numero_de_palabras[s]))

  with open("mbox-short.txt", 'r') as file:   # Leer el contenido del archivo y lo guardamos en la variable "txt"
    txt = file.read()
    palabras_repetidas(txt)       # Llamar a la función palabras_repetidas pasando el contenido del archivo como argumento
  ```
