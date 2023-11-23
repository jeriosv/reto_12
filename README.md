# Reto No. 12: "Ya casi vacaciones"
Métodos de Strings y ejercicios de procesamiento de archivo

## 1. Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

## Métodos de strings en Python:

- endswith: indica si la cadena termina con una subcadena determinada.

Sintaxis: cadena.endswith("subcadena", inicio, fin)

```python
cadena = "bienvenido a mi aplicación" 
print(cadena.endswith("mi", 13, 15)) #True
print(cadena.endswith("aplicación")) #True
print(cadena.endswith("mi")) #False
```

- startswith: retorna True si la cadena inicia con la subcadena especificada. 

Sintaxis: cadena.startswith("subcadena", posicion_inicio, posicion_fin)
```python
cadena = "bienvenido a mi aplicación"
print(cadena.startswith("bienvenido")) #True
print(cadena.startswith("aplicación", 16, 26)) #True
```
**- isalpha:** indica si la cadena es alfabética.

Sintaxis: cadena.isalpha()
```python
cadena = "Amazonas" 
print(cadena.isalpha()) #True

cadena = "Amazonas en 2025" 
print(cadena.isalpha()) #False

cadena = "Amazonas y el Caribe" 
print(cadena.isalpha()) #False
```
**- isalnum:** indica si la cadena es alfanumérica.

Sintaxis: cadena.isalnum()
```python
cadena = "Amazonas2025" 
print(cadena.isalnum()) #True

cadena = "20385"
print(cadena.isalnum()) #True
```
**- isdigit:** indica si la cadena es numérica.

Sintaxis: cadena.isdigit()
```python
numero = "1234"
print(numero.isdigit()) #True

numero = "23 50"
print(numero.isdigit()) #False

numero = "2.6"
print(numero.isdigit()) #False
```
**- isspace:** indica si la cadena está comformada por espacios.

Sintaxis: cadena.isspace()
```python
string = " "
print(string.isspace()) #True

string = ""
print(string.isspace()) #False

string = "Hola "
print(string.isspace()) #False
```
**- istitle:** indica si la cadena es un título, es decir que laprimera letra de la palabra es mayúscula y el resto son minúsculas.

Sintaxis: cadena.istitle()
```python
string = "Día Internacional"
print(string.istitle()) #True

string = "Día internacional"
print(string.istitle()) #False

string = "Hola"
print(string.istitle()) #True
```
**- islower:** indica si la cadena está compuesta solo por letras minúsculas.

Sintaxis: cadena.islower()
```python
string = "muerte y vida"
print(string.islower()) #True

string = "Muerte y Vida"
print(string.islower()) #False

string = "vida54"
print(string.islower()) #True
```

**- isupper:** indica si la cadena está compuesta solo por letras mayúsculas.

Sintaxis: cadena.isupper()
```python
string = "CIEN AÑOS DE SOLEDAD"
print(string.isupper()) #True

string = "CIENAÑOS"
print(string.isupper()) #True

string = "HOLA8"
print(string.isupper()) #True
```
Consultado en https://uniwebsidad.com/libros/python/capitulo-6/metodos-de-validacion

**2.** Procesar el [archivo] y extraer:

- Cantidad de vocales

  ```python
  def numVocales(x: str)->int: #se define la función
    letra = 0
    for i in x: #se utiliza un ciclo for para recorrer el texto
        if i.isalpha() and i in "aeiou" or i in "AEIOU": #como condicion se verifica que se tomen en cuenta solo las letras y que sean vocales
            letra += 1 
    return letra


  if __name__ == "__main__":
    s = "mbox-short.txt" #se define una variable con el archivo a utilizar
    with open(s, "r") as file: #se abre el archivo
        vocales = numVocales(file.read())
        print(f"Hay {vocales} vocales en el archivo.") #imprime el número de vocales
  ```
- Cantidad de consonantes

  ```python
  def numConsonantes(x: str)->int: #se define la función
    letras = 0
    for i in x: #se utiliza un ciclo for para recorrer el texto
        if i.isalpha() and i not in "aeiou" and i not in "AEIOU": #como condicion se verifica que se tomen en cuenta solo las letras excluyendo las vocales
            letras += 1
    return letras


  if __name__ == "__main__":
    s ='brain.txt' #se define una variable con el archivo a utilizar
    with open(s,"r") as file: #se abre el archivo
        Consonantes = numConsonantes(file.read())
        print(f"Hay {Consonantes} consonantes en el archivo.") #imprime el número de consonantes
  ```
- Listado de las 50 palabras que más se repiten
