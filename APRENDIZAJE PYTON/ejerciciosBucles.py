"""
print("Ejercicio 1")

#imprimir la serie del 7 al 14 mediante un bucle for
print("usando for con condicional if")
for i in range(15):
    if i>6:
        print(f"El valor del bucle es: {i}")

print("usando for indicando el rango start y stop")
for i in range(7, 15):
    print(f"El valor del bucle es: {i}")
print("Usando el bucle while")
i=7
while i <=14:
    print(f"El valor del bucle es {i}")
    i+=1
"""
    

#ejercicio 3

for i in range(0, -5001, -500):
    print(f"el valor del bucle es: {i}") 

print("usando while")
i=0
while i>=-5000:
    print(f"el valor del bucle while es: {i}")  
    i-=500
print("iterar una lista en python")
paises=["Afganistán",
"Albania",
"Alemania",
"Andorra",
"Angola",
"Antigua y Barbuda",
"Arabia Saudita",
"Argelia",
"Argentina",
"Armenia",
"Australia",
"Austria",
"Azerbaiyán",
"Bahamas",
"Bangladés",
"Barbados",
"Baréin",
"Bélgica",
"Belice",
"Benín",
"Bielorrusia",
"Birmania",
"Bolivia",
"Bosnia y Herzegovina",
"Botsuana",
"Brasil",
"Brunéi",
"Bulgaria",
"Burkina Faso",
"Burundi",
"Bután",
"Cabo Verde",
"Camboya",
"Camerún",
"Canadá",
"Catar",
"Chad",
"Chile",
"China",
"Chipre",
"Ciudad del Vaticano",
"Colombia",
"Comoras",
"Corea del Norte",
"Corea del Sur",
"Costa de Marfil",
"Costa Rica",
"Croacia",
"Cuba",
"Dinamarca",
"Dominica",
"Ecuador",
"Egipto",
"El Salvador",
"Emiratos Árabes Unidos",
"Eritrea",
"Eslovaquia",
"Eslovenia",
"España",
"Estados Unidos",
"Estonia",
"Etiopía",
"Filipinas",
"Finlandia",
"Fiyi",
"Francia",
"Gabón",
"Gambia",
"Georgia",
"Ghana",
"Granada",
"Grecia",
"Guatemala",
"Guyana",
"Guinea",
"Guinea ecuatorial",
"Guinea-Bisáu",
"Haití",
"Honduras",
"Hungría",
"India",
"Indonesia",
"Irak",
"Irán",
"Irlanda",
"Islandia",
"Islas Marshall",
"Islas Salomón",
"Israel",
"Italia",
"Jamaica",
"Japón",
"Jordania",
"Kazajistán",
"Kenia",
"Kirguistán",
"Kiribati",
"Kuwait",
"Laos",
"Lesoto",
"Letonia",
"Líbano",
"Liberia",
"Libia",
"Liechtenstein",
"Lituania",
"Luxemburgo",
"Macedonia del Norte",
"Madagascar",
"Malasia",
"Malaui",
"Maldivas",
"Malí",
"Malta",
"Marruecos",
"Mauricio",
"Mauritania",
"México",
"Micronesia",
"Moldavia",
"Mónaco",
"Mongolia",
"Montenegro",
"Mozambique",
"Namibia",
"Nauru",
"Nepal",
"Nicaragua",
"Níger",
"Nigeria",
"Noruega",
"Nueva Zelanda",
"Omán",
"Países Bajos",
"Pakistán",
"Palaos",
"Panamá",
"Papúa Nueva Guinea",
"Paraguay",
"Perú",
"Polonia",
"Portugal",
"Reino Unido",
"República Centroafricana",
"República Checa",
"República del Congo",
"República Democrática del Congo",
"República Dominicana",
"Ruanda",
"Rumanía",
"Rusia",
"Samoa",
"San Cristóbal y Nieves",
"San Marino",
"San Vicente y las Granadinas",
"Santa Lucía",
"Santo Tomé y Príncipe",
"Senegal",
"Serbia",
"Seychelles",
"Sierra Leona",
"Singapur",
"Siria",
"Somalia",
"Sri Lanka",
"Suazilandia",
"Sudáfrica",
"Sudán",
"Sudán del Sur",
"Suecia",
"Suiza",
"Surinam",
"Tailandia",
"Tanzania",
"Tayikistán",
"Timor Oriental",
"Togo",
"Tonga",
"Trinidad y Tobago",
"Túnez",
"Turkmenistán",
"Turquía",
"Tuvalu",
"Ucrania",
"Uganda",
"Uruguay",
"Uzbekistán",
"Vanuatu",
"Venezuela",
"Vietnam",
"Yemen",
"Yibuti",
"Zambia",
"Zimbabue",]
print("usando for")
for pais in paises:
    print(f"--> {pais}<--")

print("usando wile")
pais=0
while pais<len(paises):
    print(f"-->{paises[pais]} <--")
    pais+=1
    

#Ejercicio 4
print("itererar la lista numeros excluyendo el 10 y rompiendo el ciclo en 356\n")
numeros=[10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10,400]
numeros.sort()
print(numeros)
for i in numeros:
    if i== 10:
        continue
    elif i==356:
        break
    else:
        print(f"el valor del elemento es: {i} ")
