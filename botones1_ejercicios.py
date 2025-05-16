from tkinter import *

root = Tk()
root.title("ejercicio 1 Botones")

root.geometry("900x700+10+10")

#funcion para crear el evento del boton despues de pulsarlo.
def boton_pulsado(numero_boton):
    mensaje = Label(root, text=f"Boton {numero_boton} pulsado")
    mensaje.pack()



#creamos los botones
"""
Button(root, text = "humanosr").pack()
Button(root, text = "animales").pack()
Button(root, text = "tecnologia").pack()
Button(root, text = "ciencia").pack()
"""

#presentando los botones usando el grid o lo que se puede llamar usando una tabla
boton1 =Button(root, text = "Boton1 ", command= lambda : boton_pulsado(1)).pack() #grid(column= 0, row= 1)
boton2 =Button(root, text = "Boton2 ", command= lambda : boton_pulsado(2)).pack() #grid(column= 0, row= 2)
boton3 =Button(root, text = "Boton3 ", command= lambda : boton_pulsado(3)).pack() #grid(column= 2, row= 1)
boton4 =Button(root, text = "Boton4" , command= lambda : boton_pulsado(4)).pack() #grid(column= 2, row= 2)


root.mainloop()