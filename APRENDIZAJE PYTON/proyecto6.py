#para que funcione el programa se debe llamar las funciones contenidas en el archivo funciones_auxiliares.py
from os import system
from funciones_auxiliares import *
print("---> CALCULADORA <--- ")

"""
#FUNCION PARA CREAR UN MENU DE OPCIONES
def menu_opciones():
    print('INGRESA UN NÚMERO VÁLIDO.')

    print("Seleccione una de las siguientes operaciones\n")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. división")
    print("5. potencia")
    print("6. Salir del programa")
    while True:
        try:
            eleccion = int(input("\nDigita un numeros para seleccionar una operación: "))
            if eleccion >= 1 and eleccion <= 6:
                if eleccion == 1:
                    system("cls")
                    print("ha elegido sumar")  
                    agregar_y_sumar(lista_numeros)
                    continue
                                                    
                elif eleccion == 2:
                    system("cls")
                    print("ha elegido restar")
                    restar()
                    continue
                elif eleccion == 3:
                    system("cls")
                    print("ha elegido multiplicar")
                    multiplicar()
                    continue
                elif eleccion == 4:
                    system("cls")
                    print("ha elegido dividir")
                    dividir_numero()
                    continue
                elif eleccion == 5:
                    system("cls")
                    print("ha elegido hallar potencias")
                    hallar_potencia()
                    continue
                elif eleccion == 6:
                    system("cls")
                    print("ha salido del programa")
                    exit()
                break
            else:
                system("cls")
                menu_opciones()
        except ValueError:
            system("cls")
            menu_opciones()
menu_opciones()

"""

#programa usando match
def calculadora():
    while True:
        try:
            print("Seleccione una de las siguientes operaciones\n")
            print("1. suma")
            print("2. resta")
            print("3. multiplicacion")
            print("4. división")
            print("5. potencia")
            print("6. Salir del programa")

            opcion = int(input("\nDigita un numeros para seleccionar una operación: "))

            match opcion:
                case 1:
                    system("cls")
                    print("ha elegido sumar")
                
                    agregar_y_sumar(lista_numeros)
                    
                case 2:
                    system("cls")
                    print("ha elegido restar")
                
                    restar()
                    

                    
                case 3:
                    system("cls")
                    print("ha elegido multiplicar")
                
                    multiplicar()

                    
                case 4:
                    system("cls")
                    print("ha elegido dividir")
                    dividir_numero()

                    
                case 5:
                    system("cls")
                    print("ha elegido hallar potencias")
                
                    hallar_potencia()

                    
                case 6:
                    print("salir del programa")
                    break
                case __:
                    print("Ingrese un valor correcto")
                
        except ValueError:
            print("Ingresa valores numericos solamente")  
            calculadora()
calculadora()

