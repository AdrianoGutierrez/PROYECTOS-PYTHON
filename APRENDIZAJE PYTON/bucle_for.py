#bucle for
print("BUCLE FOR")
"""
for i in range(5):
    print(f"este es el valor del contador {i}")

print("good bye fin del programa")

#bucle for con inicio y parada en difente indice usando start y stop
for i in range(3, 7):
    print(f"este es el valor del contador {i}")
print("fin del codigo 2")

#iterar una lista con el bucle for
colores=["rojo","azul", "verde", "amarillo"]
print("*******LISTA DE COLORES***********")
for color in colores:
    #print(f"este es el color {color}")
    if color== "azul" or color == "verde":
        continue
    print(f"este es el color:  {colores}")

    """

colores=["rojo", "verde", "azul","amarillo"]

for color in colores:
    if color=="azul":
        print(color)
        print("El codigo se ha detenido")
        break
    print(f"este es el color {color}")



