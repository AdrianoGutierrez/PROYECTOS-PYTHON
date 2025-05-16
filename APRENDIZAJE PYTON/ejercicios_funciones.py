"""
ejercicio 1: agregar un color a una lista empleando una funcion
"""
#1 se crea la lista colores

colores = ["rojo", "verde", "amarillo"]

#se implementa la funcion para agregar colores a la lista

def agregarColores(color): 
    colores.append(color)
    
agregarColores(input("agrega un color\n"))
print(colores)