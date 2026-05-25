def procesar_ventas(n_vendedores, m_anios, matriz_ventas):
    if n_vendedores == 0 or m_anios == 0:
        print("La matriz de ventas está vacía.")
        return

    totales_por_vendedor = [0] * n_vendedores
    totales_por_anio = [0] * m_anios
    gran_total = 0

    for i in range(n_vendedores):
        for j in range(m_anios):
            venta = matriz_ventas[i][j]
            totales_por_vendedor[i] += venta
            totales_por_anio[j] += venta
            gran_total += venta

    print("--- REPORTE DE VENTAS ---")
    print("1. Total de ventas por vendedor:")
    for i in range(n_vendedores):
        print(f"   Vendedor {i+1}: ${totales_por_vendedor[i]:,.2f}")
        
    print("\n2. Total de ventas por año:")
    for j in range(m_anios):
        print(f"   Año {j+1}: ${totales_por_anio[j]:,.2f}")
        
    print(f"\n3. GRAN TOTAL DE VENTAS: ${gran_total:,.2f}")

if __name__ == "__main__":
    N = 4 
    M = 3 
    
    ventas = [
        [1500, 2000, 2500],
        [1000, 1100, 1200],
        [3000, 3100, 2900],
        [500,  800,  1500] 
    ]
    
    procesar_ventas(N, M, ventas)