"""
**Problema: Calculadora de Factorial**

Escribe un programa que calcule el factorial de un número ingresado por el usuario.

**Especificaciones:**

- El programa debe solicitar al usuario que ingrese un número entero no negativo.
- Debes calcular el factorial de ese número.
- El factorial de un número entero `n` se define como el producto de todos los enteros positivos desde 1 hasta `n`.
- Muestra el resultado del cálculo del factorial.

**Ejemplo de entrada/salida:**

```
Ingresa un número entero no negativo: 5
El factorial de 5 es 120.
```

**Consejos:**

- Puedes implementar esta calculadora de factorial usando un bucle `for`.
- Asegúrate de manejar casos especiales, como el factorial de 0 (que es 1) y números negativos (para los cuales puedes mostrar un mensaje de error).

¡Espero que disfrutes resolviendo este problema y que te ayude a fortalecer tus habilidades en Python!
"""
def factorial():
    numero = input("ingrese un numero entero no negativo: ")
    if int(numero) < 0:
        print("error:el numero debe ser positivo")
    elif int(numero) == 0:
        print(1)
    else:
        total = 1
        for i in range(1,int(numero)+1):
            total = i * total
            print(total)

        print(f"El factorial de {numero} es {total}")

factorial()