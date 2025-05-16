"""Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

print("*****VALIDAR CONTRASEÑA******")

usuario = "Agp"
psw = "A76*"

print("Ingrese su usuario y contraseña para ingresar al sistema")
usr = input("login: \n")
pssw = input("contraseña\n")

if usuario == usr and psw == pssw:
    print(f"bienvenido {usuario} al sistema")
else:
    print("usuario o contraseña no validos")

