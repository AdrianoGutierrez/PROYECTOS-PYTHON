from tkinter import *

root = Tk()
root.title("Ventana con python")
root.geometry("900x700+10+10")
#creacion de la etiqueta label 
mensaje = Label(root, text="Mi primera ventana en python")
l_nombre = Label(root, text="Nombre")
l_apellido = Label(root, text="Apellido")
l_identificacion= Label(root, text="identificacion")

#mostrar la etiqueta en pantalla
mensaje.anchor()
mensaje.grid(row=0)
l_nombre.grid(row = 2, column=0)
l_apellido.grid(row = 2, column=3)
l_identificacion.grid(row=3,column=4)

#llamada para mostrar la interfaz grafica
root.mainloop()