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
