traductor = {
    "español" : "ingles",
    "numero": "number",
    "arbol" : "tree"}
print(traductor)

for i in traductor:
    print(f"este es el valor en cada vuelta del iterador {i}")
    

#iterar la clave y el valor
for español in traductor:
    print(f"{español.capitalize()} : {traductor[español]}")

