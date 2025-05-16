

class Motocicleta():
    #definir atributos de clase
    estado = "nueva"
    motor = False
    
    

    #Definicion de metodo init
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, 
        modelo, fecha_fabricacion, velocidad_pico, peso, propietario, capacidad_max_combustible):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.Velocidad_pico = velocidad_pico
        self.peso = peso
        self.propietario = propietario
        self.capacidad_max_combustible = capacidad_max_combustible


    #definicion de metodos
    def arrancar(self):
        if self.motor:
            print("la motocicleta está encendida")
        else:
            print("La motocicleta ya estaba encendida")

    def detener(self):
        if self.motor:
            print("la motocicleta está apagada")
        else:
            print("la motocicleta ya estaba apagada")

    def consultar_precio(self):
        print(f"el valor de la moto {self.marca} es de {self.precio} pesos")
#**********************metodos para verificar el nivel de combustible*************   
    #metodo para verificar la cantidad de combustible que tiene actualmente
    def comprobar_combustible(self ):
        print(f"---> REPORTE DE COMBUSTIBLE PARA LA MOTO {self.marca} DE PLACA {self.matricula} <--- ")
        print(f"la moto  tiene {self.combustible_litros} litros de gasolina\nY su capacidad es {self.capacidad_max_combustible} litros")
        disp_para_tanquear= self.capacidad_max_combustible - self.combustible_litros
        print(f"puede tanquear {disp_para_tanquear} litros")
        print("---> FIN DEL REPORTE DE COMBUSTIBLE  <--- \n")

    
    #metodo para repostar combustible
    def tanquear(self):
        
        while True:
            self.repostar_combustible = float(input("introduzca la cantidad de litros a repostar"))
            if self.combustible_litros + self.repostar_combustible <= self.capacidad_max_combustible:
                print( "REPOSTAJE EXITOSO")
                print(f" se han repstado {self.repostar_combustible} litros")
                self.combustible_litros += self.repostar_combustible
                print(f"la cantidad de gasolina que hay en el tanque es { self.combustible_litros} litros ")
                break
            
            else:
                print("no se puede tanquear... el pedido sobrepasa la capacidad del tanque ")

            


    
        


#********************************************* fin del metodo para verificar combustible
#instanciar un objeto
honda_storm = Motocicleta("negro", "HKK123", 10, 2, "Honda", 2015, 
    "enero de 2015", "150 km/h", "125 Kg, ", "Adriano Gutierrez", 15)

yamaha = Motocicleta(
    matricula="HKL 213",
    combustible_litros= 1,
    modelo=2020,
    numero_ruedas = 3,
    marca= "yamaha",
    velocidad_pico= "200km/h",
    propietario= "Agp",
    peso= "250 kg",
    color= "rojo", 
    fecha_fabricacion= "enero 2020",
    capacidad_max_combustible = 12.5
)


#honda_storm.arrancar()
#yamaha.detener()
honda_storm.precio = 5000000#atributo declarado por fuera de la clase
#honda_storm.consultar_precio()
#yamaha.consultar_precio()

#Llamadas a los metodos
#honda_storm.tanquear()
yamaha.comprobar_combustible()
yamaha.tanquear()






