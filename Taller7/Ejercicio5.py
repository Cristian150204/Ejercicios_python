def actualizar_tabla(equipos, partidos):
    
    for partido in partidos:
        local_cod = partido['local_cod']
        local_goles = partido['local_goles']
        visit_cod = partido['visit_cod']
        visit_goles = partido['visit_goles']
        
        if local_cod not in equipos or visit_cod not in equipos:
            print(f"Error: Equipo no encontrado en el partido {local_cod} vs {visit_cod}")
            continue
            
        eq_local = equipos[local_cod]
        eq_visit = equipos[visit_cod]
        
        # Actualizar Partidos Jugados
        eq_local['PJ'] += 1
        eq_visit['PJ'] += 1
        
        # Actualizar Goles
        eq_local['GF'] += local_goles
        eq_local['GC'] += visit_goles
        eq_visit['GF'] += visit_goles
        eq_visit['GC'] += local_goles
        
        # Calcular de resultados
        if local_goles > visit_goles:
            # Local
            eq_local['PG'] += 1
            eq_local['Puntos'] += 3
            eq_visit['PP'] += 1
        elif local_goles < visit_goles:
            # Visitante
            eq_visit['PG'] += 1
            eq_visit['Puntos'] += 3
            eq_local['PP'] += 1
        else:
            # Empate
            eq_local['PE'] += 1
            eq_visit['PE'] += 1
            eq_local['Puntos'] += 1
            eq_visit['Puntos'] += 1

    lista_equipos = list(equipos.values())
    lista_equipos.sort(key=lambda x: (x['Puntos'], x['GF'] - x['GC']), reverse=True)
    
    print(f"{'POS':<4} | {'EQUIPO':<15} | {'PJ':<3} | {'PG':<3} | {'PE':<3} | {'PP':<3} | {'GF':<3} | {'GC':<3} | {'DIF':<4} | {'PTS':<3}")
    print("-" * 75)
    for i, eq in enumerate(lista_equipos):
        dif = eq['GF'] - eq['GC']
        print(f"{i+1:<4} | {eq['nombre']:<15} | {eq['PJ']:<3} | {eq['PG']:<3} | {eq['PE']:<3} | {eq['PP']:<3} | {eq['GF']:<3} | {eq['GC']:<3} | {dif:<4} | {eq['Puntos']:<3}")

if __name__ == "__main__":
    tabla_actual = {
        'EQ1': {'código': 'EQ1', 'nombre': 'Nacional', 'PJ': 10, 'PG': 6, 'PE': 2, 'PP': 2, 'GF': 15, 'GC': 8, 'Puntos': 20},
        'EQ2': {'código': 'EQ2', 'nombre': 'Millonarios', 'PJ': 10, 'PG': 6, 'PE': 2, 'PP': 2, 'GF': 14, 'GC': 9, 'Puntos': 20},
        'EQ3': {'código': 'EQ3', 'nombre': 'America', 'PJ': 10, 'PG': 5, 'PE': 3, 'PP': 2, 'GF': 12, 'GC': 10, 'Puntos': 18},
        'EQ4': {'código': 'EQ4', 'nombre': 'Santa Fe', 'PJ': 10, 'PG': 4, 'PE': 4, 'PP': 2, 'GF': 10, 'GC': 10, 'Puntos': 16},
    }
    
    resultados_fecha = [
        {'local_cod': 'EQ1', 'local_goles': 1, 'visit_cod': 'EQ2', 'visit_goles': 1},
        {'local_cod': 'EQ3', 'local_goles': 2, 'visit_cod': 'EQ4', 'visit_goles': 0}
    ]
    
    print("ACTUALIZANDO TABLA...\n")
    actualizar_tabla(tabla_actual, resultados_fecha)