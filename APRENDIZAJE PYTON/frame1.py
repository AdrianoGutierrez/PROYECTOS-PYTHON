#importaciones
from tkinter import * 
import os
from PIL import ImageTk, ImageColor, Image


#--> vincular archivos del sistema operativo para vinvular imagenes
DirectorioRaiz = os.path.dirname(__file__)
directorioImagenes = os.path.join(DirectorioRaiz, "imagenes")
dirlogin = os.path.join(directorioImagenes, "login")
directorioFrame = os.path.join(directorioImagenes, "imgFrame")



#-->espacio para crear funciones
#1-funcion para crear un separador de elementos dentro del root
def separadorroot():
    separador=LabelFrame(root, text="",)
    separador.config(width=10, height=10, background="pink", )
    separador.pack()
#2-funcion para crear un separador de elementos dentro del Frame
def separadorframe():
    separador=LabelFrame(frame1, text="",)
    separador.config(width=10, height=10, background="green", )
    separador.pack()
#3-funcion para crear un boton en root
def crearBoton():
    Button(root, text="Clic aqui...boton 1 en el root", bd=3,command=mifuncion).pack()

#3-funcion para crear un boton en frame
def crearBoton1():
    Button(frame1, text="Clic aqui... boton de frame", bd=3, command=calcular).pack()
#4-funcion para el comando del boton
def mifuncion():    
    saludo=Label(text="bienvenido al sistema...  prueba del funcionamiento de un boton ")
    saludo.pack()

#5--> funcion para el comando del boton del frame
def calcular():
    calcula=Label(frame2, text="estoy procesando el calculo...")
    calcula.pack()



#-->creando los elementos de la ventana
#--->1-crear la ventana principal 
root = Tk()
root.title("uso de los frame")
root.geometry("400x600+400+10")
root.iconbitmap(os.path.join(dirlogin, "logoLogin.ico"))
root.configure(background="SkyBlue3", bd=5,)





#--->2 titulo de la ventana
tituloventana= Label(text="mi empresa Online",
                     padx=5,
                     pady=5,
                     width=100, height= 1,
                     anchor="center",
                     font=("Georgia", 25), 
                     justify="center",
                     bg="seashell3",
                     bd=5,                     
                     )



#---> 3crear el frame o contenedor1 
frame1=LabelFrame(root, text="titulo del marco 1", )
frame1.config(padx=5, pady=5, width=400, height=250,
              background="light cyan",
              border=1,
              foreground="black",
              font=("comic Sans Ms", 15, "bold"),
              relief="groove",
              )



#---> 3.1crear el frame o contenedor2
frame2=LabelFrame(root, text="titulo del marco 2")
frame2.config(padx=5, pady=5, width=400, height=250,
              background="light cyan",
              border=1,
              foreground="black",
              font=("comic Sans Ms", 15, "bold"),
              relief="groove",
              )


#--->4-Creando un label en el frame
textoframe1=Label(frame1, text="marco 1... ")
textoframe1.config(padx=5, pady= 5, width=100, height=1,
                   background="gray",
                   font=("Arial", 15, "bold"),                   
                   anchor="n",
                   relief="groove",#raised, flat,sunken,groove,ridge
                   )


#--->5-Creando label2 dentro del contenedor 1
textoframe2=Label(frame1, text="marco 1... ")
textoframe2.config(padx=5, pady= 5, width=100, height=1,
                   background="gray",
                   font=("Arial", 15, "bold"),                   
                   anchor="n",
                   relief="groove",#raised, flat,sunken,groove,ridge
                   )

#--->6-Creando un label1 en el frame o contenedor 2
textoframe3=Label(frame2, text="texto conetenedor 2... ")
textoframe3.config(padx=5, pady= 5, width=100, height=1,
                   background="gray",
                   font=("Arial", 15, "bold"),                   
                   anchor="n",
                   relief="groove",#raised, flat,sunken,groove,ridge
                   )

#-->importar una imagen en el frame2

imagenFrame2 = ImageTk.PhotoImage(Image.open(os.path.join(dirlogin, "logomoto1-removebg-preview.png")).resize((100, 100)))
mostrarimagenFrame2=Label(root, image=imagenFrame2)





#-->mostrar contenido de la ventana
mostrarimagenFrame2.pack()
tituloventana.pack()
separadorroot()
frame1.pack()
separadorframe()
textoframe1.pack()
separadorframe()
textoframe2.pack()
crearBoton1()
separadorroot()
frame2.pack()
textoframe3.pack()
#Button(frame2, text="clic aqui... boton del frame 2", command=mifuncion).pack()
separadorroot()
crearBoton()
separadorroot()








#-->bucle de ejecucion
root.mainloop()

