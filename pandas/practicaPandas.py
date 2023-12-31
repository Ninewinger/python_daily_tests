""" 1. Cargar los Datos:

- Lee el archivo ventas.csv en un DataFrame de Pandas.

2. Explorar los Datos:

- Muestra las primeras filas del DataFrame para entender la estructura de los datos.
- Obtén información básica sobre el conjunto de datos (número de filas, columnas, tipos de datos, etc.).

3. Análisis de Ventas:

- Calcula y muestra la cantidad total de productos vendidos.
- Encuentra el producto más vendido.
- Encuentra el día con las ventas más altas.

4. Visualización de Datos:

- Crea un gráfico de línea para visualizar la tendencia de las ventas a lo largo del tiempo.
- Crea un gráfico de barras para mostrar los productos más vendidos.

5. Agregaciones y Resúmenes:

- Calcula la suma total de ventas.
- Encuentra el promedio de ventas diarias.
- Agrupa los datos por mes y calcula las ventas mensuales. """

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./ventas.csv")

"""mostrar datos"""
print(df.head())

"""info de la data"""
print(df.info())

"""cantidad total de productos vendidos"""
cantidad = df["Cantidad"]
print("cantidad de productos vendidos: ", cantidad.sum())

"""producto mas vendido"""
producto_mas_vendido = df[["Producto", "Cantidad"]]
print("producto mas vendido: \n", producto_mas_vendido.max())

"""fecha con mayor venta"""
fecha_mayor_venta = df[["Fecha", "Cantidad"]]

"""grafico de linea de las ventas"""
""" plot1 = df.plot(kind='line', title='tendencia ventas', x='Fecha', y='Cantidad') """

""" plt.show() """

"""grafico de barra de productos mas vendidos"""
plot2 = df.plot(kind='hist', title="total de ventas", y='Total', index=["Producto_A", "Producto_B", "Producto_C"])

plt.show()