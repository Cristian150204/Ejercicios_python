datos= []
for dia in range(1,31):
    Temperatura = float(input(f"Ingrese la temperatura en °C para el dia {dia}: "))
    datos.append(Temperatura)

#Promedio
prom = sum(datos) / len(datos)
print("\nEl promedio de la temperatura en el mes es: ",prom)
#Cantidad de dias encima del promedio
MayorProm = sum(1 for valor in datos if valor > prom)
print("\nLa cantidad de dias encima del promedio es de: ", MayorProm)
#Cantidad de dias debajo del promedio
MenorProm = sum(1 for valor in datos if valor < prom)
print("\nLa cantidad de dias por debajo del promedio es de: ", MenorProm)
#Valor mayor y menor del mes 
mayor = max(datos)
DiaMayor = datos.index(mayor) + 1
menor = min(datos)
DiaMenor = datos.index(menor) + 1   
print(f"\nLa temperatura maxima es {mayor} en el dia {DiaMayor}")
print(f"\nLa temperatura minima es {menor} en el dia {DiaMenor}")
