#creando funciones 
# se usa la palabra reservada def

#funcion para saludar de forma personalizada


def saludar():
    persona = input("hola, escribe tu nombre...\n")
    print(f"\nbienvenido, {persona} reciba un cordial saludo")

#llamar a la funcion saludar
saludar()


"""funciones con argumentos
"""
def saludo(nombre):
    print(f"Bienvenido {nombre} reciba un cordial saludo")

saludo("Adriano")

#funciones con varios argumentos

def sumar(a,b,c):
    suma = a+b+c
    print(f"El total de la suma es {suma}")

sumar(2,3,4,)

