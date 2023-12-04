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

df = pd.read_csv("./ventas.csv")

"""mostrar datos"""
print(df)

"""largo de la data"""
print(df.info())