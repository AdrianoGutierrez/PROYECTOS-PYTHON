
from tkinter import *
import os
from PIL import ImageTk, ImageColor, Image

#---carga de directorios---
#--- cargar el directorio principal
carpetaRaiz=os.path.dirname(__file__)

#--cargar carpeta imagenes
carpeta_imagenes=os.path.join(carpetaRaiz,"imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")
#print(carpetaRaiz)
#print(carpeta_imagenes)

root=Tk()
root.title("ventanas en PYTHON")
root.geometry("600x600+20+50")

#mostrar imagen guardada en carpeta
root.iconbitmap(os.path.join(carpeta_imagenes, "imagen1.ico"))

#---cargar imagenes en el root
bosque = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "bosque3.jpg")).resize((700,400)))
etiqueta = Label(image=bosque)

etiqueta.pack()


root.mainloop()


