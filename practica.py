from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(datasets.load_iris().data, columns= {"Long sepalo", "ancho sepalo", "Long petalo", "Ancho Petalo"})

print(data)
print(data.info()) # informacion

print(data.head()) # Imprime los primeros 5 registros

print(data.tail()) # ultimos 5

print(data.describe()) # datos estadisticos basicos

data = pd.read_csv("el archivo")    # De esta manera se lee un archivo con la clase pandas

print(data.isna()) # Imprime

data2 = data.dropna() # borrar objetos que tienen campos nulos
print(data2)    # Imprime

data2 = data.fillna("1") # llenar con el valor en parametro

diccionario_valores {"ancho sepalo": 999, "Long petalo": 999, "Ancho Petalo": 999 "Long sepalo": 999 }
data2 = data.fillna(value = diccionario_valores)  # esto es para llenar los campos vacios clasificados por tipo de columnas

