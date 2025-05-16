miDiccionario={
    "numero":"3,5,7",
    "palabra" : "anillo, casa",
    "formula" : "E=m*c2"
}
print(miDiccionario)
print(miDiccionario["formula"])
#Añadir elementos al diccionario con clave y valor
miDiccionario["pais"]= "mexico"
miDiccionario["animal"] = "pantera"
miDiccionario["actividad"] = "futbolista"

print(miDiccionario)
#modificar el valor de una clave

miDiccionario["animal"] = "perro"
print(miDiccionario)
#eliminar el valor de una clave
miDiccionario["actividad"]= ""
print(miDiccionario)
#borrar los elementos del diccionario
miDiccionario={}
print(miDiccionario)

