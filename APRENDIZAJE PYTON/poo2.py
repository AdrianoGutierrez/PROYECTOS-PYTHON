#Definimos la clase vehiculo
class Vehiculo():
    pais_origen = "Alemania"

    def __init__(self, color, longitud, ruedas, pais_origen) -> None:
        self.color = color
        self.longitud = longitud
        self.ruedas = ruedas

    #Definimos los métodos o acciones 
    def arrancar(self ):
        print("El vehículo ha encendido")

    def parar(self ):
        print("El vehículo está detenido")

#Instanciamos objetos... es decir necesitamos llamar un objeto llamado vehiculo1 para ello se debe crear una variable para llamarlo
vehiculo1 = Vehiculo("Amarillo", 4, 4, "francia")
vehiculo2 = Vehiculo("rojo", 4.5, 8, "Alemania")
vehiculo2.material_aleron = "fibra de carbono"

print(vehiculo1.color)
print(vehiculo1.pais_origen)
print(vehiculo2.color)
print(vehiculo2.pais_origen)




