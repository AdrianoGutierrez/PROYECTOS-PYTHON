soberana=[]
precio = 3000.0
queso = 4000.0
mani = 4000.0
piña = 5000.0

print(soberana)
print("ingesa los ingredientes digitando el numero \n")
print(f"queso --> $ {queso}")
print(f"mani --> $ {mani}")
print(f"piña --> $ {piña}")

soberana.append(input("ingresa los ingredientes\n"))

print(soberana)

for i in soberana:
    if i == "queso":
        precio = precio + queso
        print(f"la pizza cuesta en total {precio} pesos")
    elif i== "mani":
        precio = precio + mani
        print(f"la pizza cuesta {precio} pesos")

    elif i == "piña":
        precio += piña
        print(f"la pizza cuesta {precio} pesos")    

    else: 
        print("ingredientes incorrectos")
        



