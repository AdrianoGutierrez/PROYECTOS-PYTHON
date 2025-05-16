#--> Importaciones
from tkinter import *
import os
from PIL import ImageTk, ImageColor, Image

#--> vincular los directorios
carpetaRaiz = os.path.dirname(__file__)
carpetaImagen=os.path.join(carpetaRaiz,"imagenes")
carpetaMotos = os.path.join(carpetaImagen,"motos")
listaMotos=["moto1.jpeg", "moto2.jpeg", "moto3.jpeg", "moto4.jpeg"]


#--> creacion de la ventana principal
root = Tk()
#-->titulo de la ventana
root.title("ejercicios con tkinter")
root.geometry("1250x800+10+10")
#--> Icono de la ventana
root.iconbitmap(os.path.join(carpetaImagen,"imagen1.ico"))



#-->cargar imagenes como contenido de la ventana
moto_1 = ImageTk.PhotoImage(Image.open(os.path.join(carpetaMotos,listaMotos[0])).resize((400, 250)))
moto_2 = ImageTk.PhotoImage(Image.open(os.path.join(carpetaMotos,listaMotos[1])).resize((400, 250)))
moto_3 = ImageTk.PhotoImage(Image.open(os.path.join(carpetaMotos,listaMotos[2])).resize((400, 250)))
moto_4 = ImageTk.PhotoImage(Image.open(os.path.join(carpetaMotos,listaMotos[3])).resize((400, 250)))

imagenMoto1 = Label(image= moto_1)
imagenMoto2 = Label(image=moto_2)
imagenMoto3 = Label(image=moto_3)
imagenMoto4 = Label(image=moto_4)



imagenMoto1.grid(row=1,column=1)
imagenMoto2.grid(row=1,column=2)
imagenMoto3.grid(row=2, column=1)
imagenMoto4.grid(row=2, column=2)


#--> Bucle de ejecucion
root.mainloop()
