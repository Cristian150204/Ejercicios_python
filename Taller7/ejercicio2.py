import numpy as np

#Pedimos el tamaño para la matriz NxN
print("Recuerde que esta matriz sera NxN, por lo que tendra la misma cantidad de filas y columnas")
filas = int(input("\nIngrese el numero de filas y columnas que tendra la matriz: "))

matriz = np.random.randint(1,21, size=(filas, filas))
det = np.linalg.det(matriz)

print("\nMatriz generada:")
print(matriz)
print("\nEl determinante es: ", det)
