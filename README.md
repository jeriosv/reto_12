# Reto No. 12: "Ya casi vacaciones"
Métodos de Strings y ejercicios de procesamiento de archivo

## 1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

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


## 2. Procesar el [archivo] y extraer:

- Cantidad de vocales

  ```python
  def countVowels(text:str) -> int:
    vowels = 0
    for char in text:
        if char in "AEIOUaeiou":
            vowels += 1
    return vowels

    if __name__ == "__main__":
    with open("mbox-short.txt", "r") as file:
        print(f"There are {countVowels(file.read())} of vowels in the file.")
  ```

- Cantidad de consonantes

  ```python
  def countConsonants(text:str) -> int:
    consonants = 0
    for x in text:
        if x.isalpha() and x not in "AEIOUaeiou":
            consonants += 1
    return consonants

  if __name__ == "__main__":
    with open("mbox-short.txt", "r") as file:
        print(f"There are {countConsonants(file.read())} of consonants in the file.")
  ```
- Listado de las 50 palabras que más se repiten

  ```python
  def countFiftyFrequentWords(text:str) -> list:
    
    words = text.split() # A list is created from the text, separing the words by whitespace or newline.
    for i in range(len(words)): # A loop is made to delete characters that are not part of the actual word.
        if not words[i].isalpha(): # If the word is not completely an alphabetic character then:
            new = words[i].strip(",;.:-_") # Punctuation signs are deleted.
            words.pop(i) # The word is replaced with the striped version.
            words.insert(i, new)

    # Create a dictionary with word as key an occurance as value.
    ord_words = {}
    for word in words:
        if word in ord_words and word.isalpha():
            ord_words[word] += 1
        elif word not in ord_words and word.isalpha():
            ord_words[word] = 1
  
    ord_words2 = [list(ord_words.items())[i][::-1] for i in range(len(ord_words))] # Reverse the set created by .items() so then it can be sorted by value.
    freq_words = sorted(ord_words2, reverse=True)[:50] # Sort the fifty most frequent words.
    words_50 = [freq_words[i][1] for i in range(len(freq_words))] # Creates a list with only the words.

    return words_50

  if __name__ == "__main__":
    with open("mbox-short.txt", "r") as file:
        print(*countFiftyFrequentWords(file.read()), sep='\n')
  ```
