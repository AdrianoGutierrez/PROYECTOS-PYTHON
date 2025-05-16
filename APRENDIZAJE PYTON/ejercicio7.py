colores = {
    1:"rojo",
    2: "azul",
    3: "verde",
    4: "amarillo"
}
print(colores)
for color in colores:

    print(f"{color} : -{colores[color].capitalize()}")

colores[5] = "anaranjado"
print(colores)
for color in colores: 
    print(f"{color} : -{colores[color].capitalize()}")