
"""

#****************************************************************
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
                    print("ha elegido sumar")                                       
                elif eleccion == 2:
                    print("ha elegido restar")
                elif eleccion == 3:
                    print("ha elegido multiplicar")
                elif eleccion == 4:
                    print("ha elegido dividir")
                elif eleccion == 5:
                    print("ha elegido hallar potencias")
                elif eleccion == 6:
                    print("salir del programa")
                    exit()
                break
            else:
                menu_opciones()
        except ValueError:
            menu_opciones()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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
                from funciones_auxiliares import *
                agregar_y_sumar(lista_numeros)
                break
            case 2:
                system("cls")
                print("ha elegido restar")
                from funciones_auxiliares import *
                restar()

                break
            case 3:
                system("cls")
                print("ha elegido multiplicar")
                from funciones_auxiliares import *
                multiplicar()

                break
            case 4:
                system("cls")
                print("ha elegido dividir")
                from funciones_auxiliares import *
                dividir_numero()

                break
            case 5:
                system("cls")
                print("ha elegido hallar potencias")
                from funciones_auxiliares import *
                hallar_potencia()

                break
            case 6:
                print("salir del programa")
                exit()
            case __:
                print("Ingrese un valor correcto")
                
    except ValueError:
        print("Ingresa valores numericos solamente")  


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


"""

#*****************************************************************
#FUNCION PARA SUMAR NUMEROS INGRESADOS POR TECLADO

def agregar_y_sumar(lista):
    while True: 
        try:
            # Solicitar al usuario que ingrese la cantidad de números que desea agregar
            cantidad = int(input("Ingresa la cantidad de números que deseas agregar a la lista: "))

            # Agregar números a la lista
        
            for _ in range(cantidad):
                numero = int(input("Ingresa un número: "))
            
                lista.append(numero)
            

            # Sumar los números en la lista con un bucle for
            suma = 0
            for elemento in lista:
                suma += elemento

            # Mostrar la lista y el resultado de la suma
            print(f"Números sumados: {lista}")
            print(f"La suma de los números es: {suma}")
            break          
        except ValueError:
            print("Error: Ingresa números válidos.")
            continue
# Lista inicial
lista_numeros = []

# Llamar a la función
#agregar_y_sumar(lista_numeros)



#**************************************************************
#FUNCION PARA RESTAR DOS NUMEROS INGRESADOS POR TECLADO

def restar():
    while True: 
        try:
            minuendo = int(input("ingrese el minuendo:   "))
            sustraendo = int(input("ingresa el sustraendo:   "))

            diferencia = minuendo -sustraendo 
            print(f"la diferencia entre {minuendo} y el {sustraendo} es:  {diferencia}")
            break
            
        except ValueError:
            print("Error al ingresar los datos: Ingresa números válidos.")
            continue
    
#restar()           




#**************************************************************
#FUNCION PARA MULTIPLICAR 
def multiplicar():
    while True:
        try:        
            numero1 = int(input("ingrese el primer factor:   "))
            numero2 = int(input("ingresa el segundo factor:   "))

            producto = numero1 * numero2 
            print(f"El producto es:  {producto}")
            break           

        except ValueError:
            print("Error al ingresar los datos: Ingresa números válidos.")
            continue
        
#multiplicar()



#********************************************************
#FUNCION PARA DIVIDIR 
def dividir_numero():
    while True:
        try:
            dividendo = int(input("Ingresa el Dividendo:  "))
            divisor = int(input("Ingresa el divisor:  "))
            cociente = dividendo / divisor
            print(f"el cociente es: {cociente}")
            break
        except ValueError:
            print("Error al ingresar los datos: Ingresa números válidos.")
            continue

#dividir_numero()



#********************************
#FUNCION PARA HALLAR POTENCIAS

def hallar_potencia():
    while True:
        try:
            base = int(input("Ingresa la base:  "))
            exponente = int(input("Ingresa el exponente:  "))
            potencia = base ** exponente
            print(f"La potencia es: {potencia}")
            break
        except ValueError:
            print("Error al ingresar los datos: Ingresa números válidos.")
            continue

#hallar_potencia()
