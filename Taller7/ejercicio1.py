def burbuja(lista): 
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

#Pedimos al usuario la lista de N numeros
n = int(input("Cuantos numeros desea ingresar?: "))
numeros = []

#Generemos un espacio antes de los numeros que de el usuario
print("")
#Construimos la lista con los numeros ingresado
for i in range(n):
    num = float(input(f"Ingrese el numero {i+1}: "))
    numeros.append(num)

print("\nLista creada:", numeros)
print("Lista ordenada:", burbuja(numeros))
