Numero = int(input("Ingrese el numero entero que quiere en otra representacion: "))
Base = input("Escoja si quiere la representacion en binario, octal o hexagonal: ")

if Base.lower() == "binario":
    print(f"La representacion de {Numero} en base binario es: ", bin(Numero)[2:])
elif Base.lower() == "octal":
    print(f"La representacion de {Numero} en base octal es: ", oct(Numero)[2:])
elif Base.lower() == "hexagonal":
    print(f"La representacion de {Numero} en base hexagonal es: ", hex(Numero)[2:])
else: print("La base colocada no esta en las opciones")
