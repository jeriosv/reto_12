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