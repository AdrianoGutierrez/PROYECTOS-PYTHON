#ejemplo de condicionales en python
#condicional if

print("condicional IF")
edad = int(input(print("¿Cuál es tu edad?")))
print(f"Tu edad es, {edad}")
respuesta = None
if edad >= 18:
    print("eres mayor de edad,  ")
    print("¿Que desea comprar... selecciona una opcion")
    respuesta =input("puedes comprar:\n1. vino\n2. ron\n3. wiski\n")
    if respuesta == "1":
        print("Tu bebida comprada es vino ")
    elif respuesta == "2":
        print("has elegido comprar ron ")
    elif respuesta == "3":
        print("Has elegido comprar Wisky")
    else:
        print("opcion no válida")
else:
    print("eres menor de edad y no puedes comprar licor")

    