print("  --> PIZZERÍA AGP <--  \n")

dinero = float(input("ingresa tu dinero disponible para la compra\n"))
dinero_inicial = dinero
total = 0.0
pedido = []

#tipos de pizza 
margarita = 3000.0
jamon = 4000.0
cuatro_quesos = 5000.0

#ingredientes
extra_queso = 1500.0
champiñones = 2000.0
piña = 3000.0

error = True
while True:

    print(f"1. margarita --> $ {margarita}\n")
    print(f"2. Jamon --> $ {jamon}\n")
    print(f"3. cuatro quesos --> $ {cuatro_quesos}\n")

    eleccion = int(input("hola, selecciona la pizza que desea\n"))

    match eleccion:
        case 1:
            print(f"ha seleccionado la pizza margarita , su valor es {margarita} pesos")
            dinero -=margarita
            print(f"le quedan {round(dinero, 2)} pesos")
            total += margarita
            pedido.append(f"margarita - {margarita} $")
            print(pedido)

            break

        case 2:
            print(f"ha seleccionado la pizza de Jamon , su valor es {jamon} pesos")
            dinero -=jamon
            print(f"le quedan {round(dinero, 2)} pesos")
            total += jamon
            pedido.append(f"jamon - {jamon} $")
            print(pedido)

            break

        case 3: 
            print(f"ha seleccionado la pizza cuatro quesos , su valor es {cuatro_quesos} pesos")
            dinero -=cuatro_quesos
            print(f"le quedan {round(dinero, 2)} pesos")
            total += cuatro_quesos
            pedido.append(f"cuatro quesos - {cuatro_quesos} $")
            print(pedido)

            break
        case __:
            print("seleccion incorrecta intentalo de nuevo")


#bucle para seleccionar ingredientes
while True:
    print("--> INGREDIENTES EXTRA <-- \n")
    print(f"1. extra de queso --> {extra_queso} pesos") 
    print(f"2. Champiñones --> {champiñones} pesos")   
    print(f"3. Piña --> {piña} pesos")   
    print(f"4. No elegir ningun ingrediente y pagar")

    eleccion = int(input("selecciona un numero para agregar los ingredientes extra")) 

    match eleccion:
        case 1:
            print(f"ha elegigo agregar extra de queso y debe pagar un adicional de  {extra_queso} pesos")
            dinero -= extra_queso
            total += extra_queso
            print(f"Total a pagar {total}")
            print(f"Le quedan {round(dinero,2)} pesos")
            pedido.append(f"extra de queso - {extra_queso}")

        case 2:
            print(f"ha elegigo agregar champiñones y debe pagar un adicional de  {champiñones} pesos")
            dinero -= champiñones
            total += champiñones
            print(f"Total a pagar {total}")
            print(f"Le quedan {round(dinero,2)} pesos")
            pedido.append(f"Champiñones - {champiñones}")

        case 3: 
            print(f"ha elegigo agregar piña y debe pagar un adicional de  {piña} pesos")
            dinero -= piña
            total += piña
            print(f"Total a pagar {total}")
            print(f"Le quedan {round(dinero,2)} pesos")
            pedido.append(f"piña - {piña}")

        case 4: 
            print(f"de acuerdo ningun ingrediente adicional ")
            break
        case __:
            print("selecciona una opcion correcta ")

if total <= dinero_inicial:
    print(" ---> SU PEDIDO <--- \n")
    print(f"su pedido fue:\n{pedido}")
    print(f"el total de su pedido es {total} pesos")
    print(f"pagó con {dinero_inicial} pesos ")
    print(f"Su cambio es {dinero} pesos\n")

    for i in pedido:
        print(f"-{i}")

    print("\n buen provecho")

else:
    print("no le alcanza el dinero, intentelo de nuevo")




            
