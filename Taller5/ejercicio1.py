N = int(input("Escoge un numero impar entero: "))
Impar = ((N + 1)//2)**2
if N % 2 == 0:
     raise ValueError("Ese no es un numero impar")
print("La suma de todos los numeros impares entre 1 y", N, "es: ",Impar)
