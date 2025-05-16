#Importamos el modulo de interfaces graficas llamado tkinter
import tkinter

#Definimos una variable para iniciar la interfaz grafica de la ventana principal
root= tkinter.Tk()

#creacion de la etiqueta label 
mensaje = tkinter.Label(root, text="Mi primera ventana en python")
l_nombre = tkinter.Label(root, text="Nombre")
l_apellido = tkinter.Label(root, text="Apellido")

#mostrar la etiqueta en pantalla
mensaje.pack()
l_nombre.pack( padx=[10, 0] ,pady=[100, 0])
l_apellido.pack(padx=10,pady=100)

#llamada para mostrar la interfaz grafica
root.mainloop()



