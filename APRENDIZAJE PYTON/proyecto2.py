#Crear una calculadora que pueda sumar,restar, multiplicar dividir, hallar potencias usuando el condicional if

print("******CALCULADORA EN PYTHON*******\n")

print("Selecciona la operacion que deasea realiar, marque una de las opciones\n")
print("1. sumar\n")
print("2. Restar\n")
print("3. multiplicar\n")
print("4. Dividir\n")
print("5. cociente\n")
print("6. resto\n")
print("7. potencia")
print("8. raices")

opcion = input("¿Qué operacion desea resolver?")
n1 = 0
n2 = 0
respuesta = 0
n1 = int(input(print("ingrese el primer numero")))
n2 = int(input(print("ingrese el segundo numero")))

if opcion == "1":
    respuesta = n1+n2
    print(f"la suma es {respuesta}")
elif opcion == "2":
    respuesta = n1-n2
    print(f"la diferencia es {respuesta}")
elif opcion == "3":
    respuesta=n1*n2
    print(f"El producuto es {respuesta}")
elif opcion=="4":
    if n2 <= 0:
        print("error... No se puede dividir entre cero")
    else:
        respuesta=float(n1)//float(n2)
        print(f"el cociente es {respuesta}")
elif opcion == "5":
    if n2 <= 0: 
        print("error... No se puede dividir entre cero")
    else:
        respuesta=n1%n2
        print(f"el resto es {respuesta}")
elif opcion == "6":
    if n2 <= 0: 
        print("error... No se puede dividir entre cero")
    else:
        respuesta=n1%n2
        print(f"el resto es {respuesta}")
elif opcion == "7":
    respuesta=n1**n2
    print(f"la potencia es {respuesta}")
elif opcion == "8":
    #respuesta= n1**n2
    #print(f"la raiz es {respuesta}")
    print("estamos rectificando el procedimiento de la raiz")
