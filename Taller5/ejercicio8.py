datos= []
for dia in range(1,31):
    Temperatura = float(input(f"Ingrese la temperatura para el dia{dia}: "))
    datos.append(Temperatura)

#Promedio
prom = sum(datos) / len(datos)
    