from tkinter import *

root = Tk()
root.title("introducir y leer datos por pantalla")
root.geometry("700x500+10+10")

#entrada de datos 
#Entrada nombre
Label(root, text = "Nombre").grid(row= 0, column= 0)
entrada_nombre = Entry(root)
entrada_nombre.grid(row=0, column=1)

#Entrada edad
Label(root, text = "edad").grid(row= 1, column= 0)
entrada_edad = Entry(root)
entrada_edad.grid(row=1, column=1)

#creamos el evento para el boton enviar, para mostrar informacion guardada
def mostrar_datos():
    nombre = entrada_nombre.get() 
    edad = entrada_edad.get() 
    #se muestra la informacion en un label
    Label(root, text=f"My name is {nombre}, and {edad} years old").grid(row= 3, column= 1)

#creamos el boton enviar
Button(root, text = "Enviar", command=  mostrar_datos).grid(column= 1, row= 2)

#bucle de ejecicion
root.mainloop()
