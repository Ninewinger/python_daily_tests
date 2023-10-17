""" Problema: Palíndromo

Escribe un programa que verifique si una palabra o frase ingresada por el usuario es un palíndromo o no. Un palíndromo es una palabra, frase u otra secuencia de caracteres que se lee igual hacia adelante y hacia atrás (ignorando espacios, signos de puntuación y mayúsculas/minúsculas).

Especificaciones:

El programa debe solicitar al usuario que ingrese una palabra o frase.
Debes eliminar todos los espacios en blanco y convertir todo el texto a minúsculas (o mayúsculas, como prefieras) antes de verificar si es un palíndromo.
Debes ignorar signos de puntuación como comas, puntos, comillas, etc.
Muestra un mensaje que indique si la palabra o frase es un palíndromo o no.
Ejemplo de entrada/salida:

Ingresa una palabra o frase: "Anilina"
"Anilina" es un palíndromo.

Puedes usar métodos de cadenas de texto en Python para eliminar los espacios y convertir el texto a minúsculas.
Puedes usar un bucle para comparar los caracteres desde el principio con los caracteres desde el final del texto para determinar si es un palíndromo. """

def palindrome():
    text = input("ingrese palabra o frase: ")
    low = text.lower()
    strip = low.strip()
    no_spaces = strip.replace(" ", "")
    no_dotes = no_spaces.replace(".", "")
    no_commas = no_dotes.replace(",", "")
    print(no_commas)
    if no_commas == no_commas[::-1]:
        print(f"{text} es un palíndromo")
    else:
        print(f"{text} no es un palíndromo")


palindrome()