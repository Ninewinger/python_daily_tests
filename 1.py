""" ¡Claro! Aquí tienes un problema de programación en Python de mediana dificultad:

Problema: Encontrar el Número Mayor y Menor

Escribe un programa que tome una lista de números como entrada y encuentre el número más grande y el número más pequeño en la lista.

Especificaciones:

El programa debe solicitar al usuario que ingrese una serie de números, uno a la vez, separados por una coma.
Debes encontrar el número más grande y el número más pequeño en la lista de números ingresados.
Luego, muestra el número más grande y el número más pequeño.
Tu programa debe manejar adecuadamente números positivos y negativos.
Ejemplo de entrada/salida:

Ingresa una serie de números separados por comas: 5, 3, -2, 7, 1, 0
El número más grande es 7.
El número más pequeño es -2.
¡Espero que disfrutes resolviendo este problema! Te ayudará a practicar tus habilidades en Python. """

def mayor_menor():
    entrada = input("introduzca numeros +/- separados por comas:")
    array = entrada.split(",")
    numeros = [int(x) for x in array]
    print(max(numeros))
    print("el numero más grande: ", max(numeros))
    print("el numero más pequeño: ", min(numeros))

mayor_menor()