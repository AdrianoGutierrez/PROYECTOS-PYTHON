#Ejercicio 1
frase = ["esty", "aprendiendo", "Python", "con", "el", "curso", "de", "100", "dias", "de", "programacion", "fácil"]
concatenar_frase = "    ".join(frase)
#print(concatenar_frase)


#Ejercicio 2
colores = ["rojo", "azul", "verde","amarillo"]
viñeta= "-"
punto = "."
print("primera opcion")
for color in colores:
    salida = color.capitalize()
    print("{}{}{}".format(viñeta, salida, punto))
print("segunda opcion")
for color in colores:
    print("{}{}{}".format(viñeta,color.capitalize(),punto))

#Ejercicio 3
numero_1= 10
numero_2 = 34.50
resultado = (numero_1 * numero_2)
#formateo con signo porcentaje %
print( "la multiplicacion de %i * %.2f  da como resultado: %.2f " %(numero_1, numero_2,resultado))





