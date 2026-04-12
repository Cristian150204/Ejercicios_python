def registro_estudiante(): 
    estudiantes = []
    cantidad = int(input("Ingrese la cantidad de estudiantes que quiere revisar: "))

    for N in range(cantidad):
        nombre = input(f"\nIngrese el nombre del estudiante {N+1}: ")
        calificacion = list(map(float, input(f"Ingrese las calificacion de {nombre} separadas por un espacio: ").split()))
        estudiantes.append((nombre, calificacion))
    return estudiantes

lista_estudiantes = registro_estudiante()
aprobado = 0
reprobado = 0
for nombre, calificacion in lista_estudiantes:
    prom = sum(calificacion) / len(calificacion)
    estado = "APROBO" if prom >= 6.0 else "REPROBO" 
    print(f"\n{nombre} tiene un promedio de: {prom:.1f} donde {estado}")
    if prom >= 6.0:
        aprobado += 1
    else: reprobado += 1

#Aprobacion o reprobacion de los estudiantes
print(f"\nLa cantidad de estudiantes que aprobaron son: {aprobado}")
print(f"\nLa cantidad de estudiantes que reprobaron son: {reprobado}")

#Calificacion alta y baja
nota_maxima = -1
nota_minima = 11
estudiante_max = ""
estudiante_min = ""
for nombre, calificacion in lista_estudiantes:
    mayor_nota = max(calificacion)
    menor_nota = min(calificacion)
    if mayor_nota > nota_maxima:
        nota_maxima = mayor_nota
        estudiante_max = nombre
    if menor_nota < nota_minima:
        nota_minima = menor_nota
        estudiante_min = nombre 
 
print(f"\nLa nota mas alta es {nota_maxima} del estudiante {estudiante_max}")
print(f"\nLa nota mas baja es {nota_minima} del estudiante {estudiante_min}")
