#Importamos el modulo de interfaz grafica de usuario tkinter
from tkinter import *
#Creamos la ventana principal root
root = Tk()
root.title("Datos personales del usuario ")


#widget para ingresar datos por teclado usando entry
entrada = Entry(root )
entrada.insert(0, "Escriba su nombre")
entrada.bind("<Button-1> ", lambda e : entrada.delete(0, END)) #colocamos la funcion lambda para que no se borre el contenido  de insert automaticamente
entrada.pack()

def pulsar_boton():
    Nombre = entrada.get()
    Label(root, text=Nombre).pack()
    
#creacion del boton
Button(root, text = "Enviar", command=pulsar_boton).pack()

#print(Button)

#Ejecucion del bucle
root.mainloop()


