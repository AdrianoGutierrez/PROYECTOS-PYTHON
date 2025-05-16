#REANDO LISTAS 
print("LISTAS EN PYTHON\n")

lista_numeros = [10,45,55,76]
print(lista_numeros)
print(lista_numeros[3])

print(f" utiliza la lista del ejercicio 1 para mmostrar el numero {lista_numeros[0]} y el numero {lista_numeros[3]}.")

lista_colores = ["rojo", "azul", "verde", "amarillo"]
print(lista_colores[1][2])

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
print(len(paises))
print(paises[193])
print(paises[192])
print(f"los ultimos paises son {paises[-1]} y {paises[-2]}")


#modificar la lista lista_colores agregando elementos en diferentes posiciones usando extend()
lista_colores.insert(0, "Gris")
lista_colores.append("rosa")
lista_colores.insert(3, "Naranja")
print(lista_colores)
#eliminar colores de la lista usando el metodo pop
lista_colores.pop(1)
print(lista_colores)
lista_colores.pop(3)
print(lista_colores)
lista_colores.pop(3)
print(lista_colores)
print(f"la nueva lista despues de eliminar elementos es {lista_colores}")

#duplicar una lista 
lista_duplicada=lista_colores.copy()
print(f"la lista duplicada es {lista_duplicada}")

#Contar elementos repetidos de una lista
numeros=[10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
print(f"existen {numeros.count(10)} numeros diez repetidos")

#mostrar un valor especifico de la lista
print(paises.index("Brasil"))
print(paises[25])

#ordenar una lista 
lista_numeros.sort()
print(f"lista ordenada en orden ascendente\n{lista_numeros}")
#ordenar lista en forma descendente
lista_numeros.reverse()
print(f"lista ordenada en orden descendente\n{lista_numeros}")
#mostrar la cantidad de elementos de una lista
print(len(lista_numeros))

