def registro_fumigacion():
    precios = {
        "1": 10,
        "2": 15,
        "3": 20,
        "4": 30
    }

    nombre= input("Ingrese el nombre del granjero: ")
    tipo= input(f"Ingrese el tipo de fumigacion que necesita {nombre} (1, 2, 3 o 4), coloque el numero: ")
    hectareas= float(input(f"Ingrese el numero de hectareas que necesita fumigar {nombre}: "))

    if tipo in precios:
        precio_base = precios[tipo]
        costo = precio_base * hectareas
        if hectareas > 1000:
              descuento = 0.05
        else: descuento = 0.0

        costo_final = costo * (1 - descuento)
        
        tope = 3000
        descuento_extra = 0.1
        
        if costo_final > tope:
              excedente = costo_final - tope
              costo_final = tope + (excedente * (1-descuento_extra))
        
        return {
            "nombre": nombre,
            "costo_final": costo_final
        }
    else:
        print("Tipo de fumigacion no valido")
        return None

registro = registro_fumigacion()
if registro:
     print(f"\nCLiente: {registro['nombre']} -> Costo final: {registro['costo_final']}")
