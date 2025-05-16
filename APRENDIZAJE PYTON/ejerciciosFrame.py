#Importaciones
from tkinter import *

root = Tk()
root.title("practica con los Frames")

marco1= LabelFrame(root, text="", width=50, height=50,  background="white", border=0)
marco1.grid(row=0, column=0)


marco2= LabelFrame(root, text="", width=50, height=50,  background="black", border=0)
marco2.grid(row=0, column=1)

marco3= LabelFrame(root, text="", width=50, height=50,  background="black", border=0)
marco3.grid(row=1, column=0)


marco4= LabelFrame(root, text="", width=50, height=50,  background="white", border=0)
marco4.grid(row=1, column=1)

marco5= LabelFrame(root, text="", width=50, height=50,  background="white", border=0)
marco5.grid(row=2, column=0)


marco6= LabelFrame(root, text="", width=50, height=50,  background="black", border=0, padx=10, pady=10)
marco6.grid(row=2, column=1)


marco7= LabelFrame(root, text="", width=50, height=50,  background="white", border=0, padx=10, pady=10)
marco7.grid(row=0, column=3)

marco8= LabelFrame(root, text="", width=50, height=50,  background="black", border=0, padx=10, pady=10)
marco8.grid(row=1, column=3)

marco9= LabelFrame(root, text="", width=50, height=50,  background="white", border=0, padx=10, pady=10)
marco9.grid(row=2, column=3)



#bucle de ejecucion
mainloop()