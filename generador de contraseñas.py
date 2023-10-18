import random
import string
""" Problema: Generador de Contraseñas Seguras

Crea un programa que genere contraseñas seguras para los usuarios. La contraseña debe cumplir con los siguientes requisitos:

Debe tener al menos 12 caracteres de longitud.
Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, @, #, $, etc.).
No puede contener espacios en blanco.
El programa debe solicitar al usuario la longitud de la contraseña que desea y luego generar una contraseña segura al azar que cumpla con los requisitos anteriores. Después, debe mostrar la contraseña generada.

Recuerda importar cualquier módulo necesario y considera utilizar caracteres especiales válidos, como: ! @ # $ %, etc. """

def generador_de_contraseñas():
    constraseña_en_array = []
    for caracter in range(12):        
        constraseña_en_array.append(random.choice(
            [random.choice([0,1,2,3,4,5,6,7,8,9]),random.choice(["#", "@", "$", "ñ", "%", "&", "!", "?", "="]), random.choice(string.ascii_letters)]
            ))
    contraseña = "".join(str(x) for x in constraseña_en_array)
    print(contraseña)

generador_de_contraseñas()
