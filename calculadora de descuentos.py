""" 
**Problema: Calculadora de Descuento**

Crea un programa que funcione como una calculadora de descuento. El programa debe hacer lo siguiente:

1. Solicitar al usuario el precio original de un producto.
2. Solicitar al usuario el porcentaje de descuento que desea aplicar (por ejemplo, 10%).
3. Calcular el precio con descuento.
4. Mostrar el precio original, el porcentaje de descuento, el monto del descuento y el precio con descuento.

El programa debe garantizar que el precio original sea un número positivo y que el porcentaje de descuento esté entre 0% y 100%. Si el usuario ingresa datos incorrectos, debe mostrar un mensaje de error y volver a solicitar los valores.

A continuación, te muestro un ejemplo de cómo podría verse la ejecución del programa:

```
Calculadora de Descuento
------------------------

Ingrese el precio original del producto: $100
Ingrese el porcentaje de descuento (0-100%): 15

Resumen:
Precio Original: $100.00
Porcentaje de Descuento: 15%
Descuento: $15.00
Precio con Descuento: $85.00
```
"""

def calculadora_de_descuentos():
    precio = input("Ingrese el precio original del producto: ")
    porcentaje_descuento = input("Ingrese el porcentaje de descuento (0-100): ")
    descuento = int(precio) * int(porcentaje_descuento) / 100
    resultado = int(precio) - int(descuento)
    print(f"Resumen:\nPrecio Original: ${precio}\nPorcentaje de Descuento: {porcentaje_descuento}%\nDescuento: ${descuento}\nPrecio con Descuento: ${resultado}")



calculadora_de_descuentos()