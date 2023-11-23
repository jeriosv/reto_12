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