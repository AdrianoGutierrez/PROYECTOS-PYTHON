#construye un proyecto para la venta de pizzas
print("\n ### PIZAS LA SOBERANA ###\n")
dinero = 0.0
total = 0.0
#precio de cada pizza
psoberana = 5000.0
pextragrande = 10000.0
pvoladora = 20000.0

#tipos de pizza existentes
soberana = []
extragrande = []
voladora = []
#ingredientes extra
queso = 3000.0
mani = 2000.0
salsa = 3500.0
frutas = 4000.0

print("¿De cúanto dinero dispones para comprar tu pizza?... \n")

#El usuario ingresa la cantidad de dinero disponible
while True:
    try:
        dinero=float(input("digita la cantidad de dinero\n"))
        print(f"usted tiene {dinero} pesos para comprar tu pizza")
    except ValueError:
        print("digita una cantidad de dinero correcta")
        continue
    if dinero <= 0:
        print("Debes escribir solo valores positivos")
        continue
    else:
        break
#tipos de pizza a elegir
print("Tenemos los siguientes tipos de Pizza...")
print("\n1. soberana --> $5000 \n2. extragrande --> $10000\n3. la voladora --> $20000\n")

while True:
    try:
        tipoPizza=int(input("Selecciona la que desea digitando el numero"))
        
    except ValueError:
        print("digita un numero por favor")
        continue
    if tipoPizza<=0:
        print("Debes escribir solo numeros positivos")
        continue
    else:
        break

error=True

match tipoPizza:
    case 1:
        print("usted ha elegido la pizza soberana")
        print(f"esta pizza te cuesta {psoberana} pesos.")
        soberana.append(input("agrega los ingredientes favoritos"))
        total = psoberana + 3000
        print(f"esta es tu pizza {soberana} y cuesta {total} pesos")
    case 2:
        print("usted ha elegido la pizza extragrande")
        print(f"esta pizza te cuesta {pextragrande} pesos.")
    case 3:
        print("usted ha elegido la pizza voladora")
        print(f"esta pizza te cuesta {pvoladora} pesos.")
    case __:
        print("error... saliendo del programa")
        error=False

        



