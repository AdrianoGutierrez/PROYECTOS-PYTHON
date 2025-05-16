#-->Importaciones
from tkinter import *
import tkinter

#--> Creacion de la ventana principal
root=Tk()
root.title("**** USO DE LOS FRAMES EN VENTANAS GRAFICAS DE PYTHON****")


#-->creacion del marco
marco1 = LabelFrame(root, text="marco 1: Entrada de datos",
                   padx=20,
                   pady=20, 
                   background="pink",
                   )
marco1.grid(row=0, column=0, padx=15, pady=15)

#--> creacion marco2
marco2 = LabelFrame(root, 
                   text="marco2: Enviar",
                   padx=20,
                   pady=20, 
                   background="pink",
                   )
marco2.grid(row=1, column=0, padx=5, pady=15)

#--> creacion marco3 
marco3 = LabelFrame(root, 
                   text="resultado",
                   padx=20,
                   pady=20, 
                   background="pink",
                   )
marco3.grid(row=0, column=1, padx=5, pady=15)



#-->Entrada de datos en el marco 1
entrada = Entry(marco1, 
                background= "springgreen",
                border= 5,
                foreground= "black", 
                width = 30, 
                #font=("Arial, 15")
                )
entrada.pack()
entrada.insert(0, "escribe tu nombre")
entrada.bind("<Button-1>", lambda e: entrada.delete(0, tkinter.END))

def enviar():
    nombre = entrada.get()
    Label(marco3,
          text=f"hola {nombre}",
          background="Skyblue",
          width=27,
          ).pack()
    entrada.delete(0, tkinter.END)
    entrada.insert(0, "Escriba su nombre...")

#-->crear el boton enviar 
boton2 =Button(marco2, 
              text="Enviar",
              command=enviar,
              background="deepSkyblue",
              border=3,
              width= 26,
              ).pack()


#--> BUCLE DE EJECUCION
root.mainloop()



