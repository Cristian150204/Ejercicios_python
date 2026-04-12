def primos_hasta(N):

    primos=[]

    for numero in range(2, N+1):
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0: 
                es_primo = False
                break
        if es_primo:
            primos.append(numero)
    return primos

#Numeros primos hasta N
N = int(input("Ingrese un numero entero N:"))
lista_primos = primos_hasta(N)
print(f"\nLos numeros primos hasta {N} son: {lista_primos}")

#Suma de la lista primos
print(f"\nLa suma de los numeros primos hasta {N} es: {sum(lista_primos)}" )

#Cantidad de primos en la lista
cantidad = sum(1 for valor in lista_primos)
print(f"\nHay {cantidad} numeros primos hasta {N}")
