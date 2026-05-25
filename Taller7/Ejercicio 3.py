import random

def procesar_examen(n_estudiantes, respuestas_correctas, datos_estudiantes):
    if n_estudiantes == 0:
        print("No hay estudiantes para procesar.")
        return

    clave_math = respuestas_correctas[:30]
    clave_verb = respuestas_correctas[30:]
    
    resultados = []
    suma_math = 0
    suma_verb = 0
    suma_total = 0
    
    for est in datos_estudiantes:
        credencial = est['credencial']
        res_math = est['respuestas_math']
        res_verb = est['respuestas_verb']
        
        puntos_math = sum(1 for i in range(30) if res_math[i] == clave_math[i])
        puntos_verb = sum(1 for i in range(30) if res_verb[i] == clave_verb[i])
        puntos_totales = puntos_math + puntos_verb
        
        resultados.append({
            'credencial': credencial,
            'puntos_math': puntos_math,
            'puntos_verb': puntos_verb,
            'puntos_totales': puntos_totales
        })
        
        suma_math += puntos_math
        suma_verb += puntos_verb
        suma_total += puntos_totales

    promedio_math = suma_math / n_estudiantes
    promedio_verb = suma_verb / n_estudiantes
    promedio_total = suma_total / n_estudiantes

    superan_promedio = [r for r in resultados if r['puntos_totales'] >= promedio_total]

    mayor_puntaje = max(resultados, key=lambda x: x['puntos_totales'])

    print("--- RESULTADOS DEL EXAMEN ---")
    print(f"Promedio Aptitud Matemática: {promedio_math:.2f}")
    print(f"Promedio Aptitud Verbal: {promedio_verb:.2f}")
    print(f"Promedio Total: {promedio_total:.2f}\n")
    
    print("Estudiantes con puntaje superior o igual al promedio total:")
    for est in superan_promedio:
        print(f"  - Credencial: {est['credencial']}, Puntaje: {est['puntos_totales']}")
        
    print(f"\nEL MAYOR PUNTAJE fue {mayor_puntaje['puntos_totales']} obtenido por la credencial {mayor_puntaje['credencial']}")

if __name__ == "__main__":
    claves = [random.randint(1, 5) for _ in range(60)]
    
    estudiantes_mock = [
        {
            'credencial': '1001',
            'respuestas_math': [random.randint(1, 5) for _ in range(30)],
            'respuestas_verb': [random.randint(1, 5) for _ in range(30)]
        },
        {
            'credencial': '1002',
            'respuestas_math': claves[:30],
            'respuestas_verb': [random.randint(1, 5) for _ in range(30)]
        },
        {
            'credencial': '1003',
            'respuestas_math': [random.randint(1, 5) for _ in range(30)],
            'respuestas_verb': claves[30:]
        }
    ]
    
    procesar_examen(len(estudiantes_mock), claves, estudiantes_mock)