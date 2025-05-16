#-->importaciones
from tkinter import *
import os
from PIL import ImageTk, ImageColor, Image


#-->vincular directorios
DirectorioRaiz = os.path.dirname(__file__)
dirImagenes = os.path.join(DirectorioRaiz, "imagenes")
dirLogin = os.path.join(dirImagenes, "login")

#tupla vacia para almacenar usuario y contraseña
usuarioCreado = ()



while True:
    nuevoUsuario = input("introduzca el nombre de usuario, \n")
    nuevaContraseña = input("introduzca la  contraseña \n")

    repitaUsuario = input("introduzca nuevamente el nombre de usuario \n")
    repitaContraseña = input("introduzca nuevamente la contraseña \n")

    if nuevoUsuario != repitaUsuario or nuevaContraseña != repitaContraseña:
        print("los valores ingresados no coinciden Vuelva a intentarlo...")
    else:
        usuarioCreado= (nuevoUsuario, nuevaContraseña)
        break



#-->creando la ventana principal
root=Tk()
root.title("moto touring")
root.geometry("350x550+100+00")
root.iconbitmap(os.path.join(dirLogin, "logoLogin.ico"))
root.configure(background="#CED8F6")

#-->cargar contenido de la ventana
bienvenida = Label(root, text="ingrese su usuario y contraseña") #-->titulo 
bienvenida.configure(background="#CED8F6") #-->color del fondo de la ventana
logoMoto = ImageTk.PhotoImage(Image.open(os.path.join(dirLogin, "logomoto1-removebg-preview.png")).resize((400, 400)))
imgUsuario = ImageTk.PhotoImage(Image.open(os.path.join(dirLogin,"user.jpeg")).resize((100, 100)))
mostrarlogoMoto = Label(image=logoMoto)
mostrarUser = Label(image=imgUsuario)
imgPassw = ImageTk.PhotoImage(Image.open(os.path.join(dirLogin, "pass.jpeg")).resize((100, 100)))
mostrarpassw = Label(image=imgPassw)


#-->mostrar imagenes  de la ventana
bienvenida.grid(row=1, column=2)
mostrarlogoMoto.grid(row=2, column=2)
mostrarUser.grid(row=5, column=2)
mostrarpassw.grid(row=8, column=2)

#mostrar contenido de la ventana campos de usuario y contraseña
User = Label(text="Nombre de usuario")
User.grid(row=5, column=3)
password=Label( text= "password")
password.grid(row=8, column=3)
ingresarUser=Entry( )
ingresarUser.insert(0, "nombre de usuario")
ingresarUser.bind("<Button-1>", lambda e: ingresarUser.delete(0, END))
ingresarUser.grid(row=5, column=4)
ingresarPassword= Entry()
ingresarPassword.insert(0, "*"*12)
ingresarPassword.bind("<Button-1>", lambda e: ingresarPassword.delete(0, END))
ingresarPassword.grid(row=8, column=4)




#funcion para validar el usuario  y la contraseña 
def validar():
    obteneruser = ingresarUser.get()
    obtenerPassword = ingresarPassword.get()
    if obteneruser != usuarioCreado[0] or obtenerPassword != usuarioCreado[1]:
        Label(text="usuario o contraseña incorrectos").grid(row=1, column=4)
        
    else:
        Label(text=f"hola {usuarioCreado[0]}, Bienvenido al sistema").grid(row=1, column=4)

#crear y mostrar el boton entrar
entrar= Button(text="Entrar", command=validar)
entrar.grid(row=10, column=4)



#-->bucle de ejecucion
root.mainloop()