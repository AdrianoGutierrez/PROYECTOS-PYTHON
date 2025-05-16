
#emplear la funcion lamda
#crear una calculadora de area del circulo
radio = int(input("introduzaca el radio del circulo\n"))
PI = 3.1415
calcularArea = lambda radio : PI * radio**2
area=calcularArea(radio)
print(f"El área del circulo es {area}")


#Funcion lambda para un saludo personalizado
(lambda nombre : print(f"bienvenodo {nombre}" ))("adriano")

colores = ["rojo", "azul", "verde", "amarillo"]
(lambda color: print(f"el color { color} se encuentra en la posicion {colores.index(color)} de la lista"))("amarillo")