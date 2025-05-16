#importaciones
from tkinter import *

root=Tk()
root.title("ventana con radiobutton")

opcion=IntVar()
opcion.set(1)

def actualiza_radio(valor):
    Label(root, text=valor).pack()

radiobutton1=Radiobutton(root, text="red...", variable=opcion, value=1)
radiobutton1.pack()

radiobutton2=Radiobutton(root, text="blue...", variable=opcion, value=2)
radiobutton2.pack()

imprimerVariable= Button(root, text="enviar", command=lambda:actualiza_radio(opcion.get()))
imprimerVariable.pack()

#Bucle de ejecucion
mainloop()
