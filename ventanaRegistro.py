import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from Usuario import Cliente

class VRegistro:
    def __init__(self, root):
        root.title("Cinemar")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=18)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Bienvenido a Cinemar"
        labelTitulo.place(x=0,y=0,width=600,height=48)

        labelSubTitulo=tk.Label(root)
        labelSubTitulo["anchor"] = "center"
        labelSubTitulo["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=12)
        labelSubTitulo["font"] = ft
        labelSubTitulo["fg"] = "#d5d5d5"
        labelSubTitulo["justify"] = "center"
        labelSubTitulo["text"] = "CREAR USUARIO"
        labelSubTitulo["relief"] = "flat"
        labelSubTitulo.place(x=0,y=50,width=600,height=30)

        self.entryNombre=tk.Entry(root)
        self.entryNombre["bg"] = "#eaeaea"
        self.entryNombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.entryNombre["font"] = ft
        self.entryNombre["fg"] = "#333333"
        self.entryNombre["justify"] = "left"
        self.entryNombre["text"] = ""
        self.entryNombre.place(x=100,y=150,width=200,height=30)

        self.entryApellido=tk.Entry(root)
        self.entryApellido["bg"] = "#eaeaea"
        self.entryApellido["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.entryApellido["font"] = ft
        self.entryApellido["fg"] = "#333333"
        self.entryApellido["justify"] = "left"
        self.entryApellido["text"] = ""
        self.entryApellido.place(x=410,y=150,width=181,height=30)

        labelNombre=tk.Label(root)
        labelNombre["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        labelNombre["font"] = ft
        labelNombre["fg"] = "#d5d5d5"
        labelNombre["justify"] = "center"
        labelNombre["text"] = "Nombre"
        labelNombre.place(x=10,y=150,width=72,height=30)

        labelApellido=tk.Label(root)
        labelApellido["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        labelApellido["font"] = ft
        labelApellido["fg"] = "#d5d5d5"
        labelApellido["justify"] = "center"
        labelApellido["text"] = "Apellido"
        labelApellido.place(x=320,y=150,width=71,height=30)

        labelEmail=tk.Label(root)
        labelEmail["anchor"] = "center"
        labelEmail["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        labelEmail["font"] = ft
        labelEmail["fg"] = "#d5d5d5"
        labelEmail["justify"] = "center"
        labelEmail["text"] = "E-mail"
        labelEmail.place(x=10,y=200,width=70,height=30)

        self.entryEmail=tk.Entry(root)
        self.entryEmail["bg"] = "#eaeaea"
        self.entryEmail["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.entryEmail["font"] = ft
        self.entryEmail["fg"] = "#333333"
        self.entryEmail["justify"] = "left"
        self.entryEmail["text"] = ""
        self.entryEmail.place(x=100,y=200,width=310,height=30)

        labelUsuario=tk.Label(root)
        labelUsuario["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        labelUsuario["font"] = ft
        labelUsuario["fg"] = "#d5d5d5"
        labelUsuario["justify"] = "center"
        labelUsuario["text"] = "Usuario"
        labelUsuario.place(x=10,y=250,width=103,height=30)

        self.entryUsuario=tk.Entry(root)
        self.entryUsuario["bg"] = "#eaeaea"
        self.entryUsuario["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.entryUsuario["font"] = ft
        self.entryUsuario["fg"] = "#333333"
        self.entryUsuario["justify"] = "left"
        self.entryUsuario["text"] = ""
        self.entryUsuario.place(x=130,y=250,width=205,height=30)

        labelPassword=tk.Label(root)
        labelPassword["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        labelPassword["font"] = ft
        labelPassword["fg"] = "#d5d5d5"
        labelPassword["justify"] = "center"
        labelPassword["text"] = "Contraseña"
        labelPassword.place(x=10,y=300,width=103,height=30)

        self.entryPassword=tk.Entry(root)
        self.entryPassword["bg"] = "#eaeaea"
        self.entryPassword["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.entryPassword["font"] = ft
        self.entryPassword["fg"] = "#333333"
        self.entryPassword["justify"] = "left"
        self.entryPassword["text"] = ""
        self.entryPassword.place(x=130,y=300,width=205,height=30)

        labelNacimiento=tk.Label(root)
        labelNacimiento["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        labelNacimiento["font"] = ft
        labelNacimiento["fg"] = "#d5d5d5"
        labelNacimiento["justify"] = "center"
        labelNacimiento["text"] = "Fecha de Nacimiento"
        labelNacimiento.place(x=10,y=350,width=170,height=30)

        self.entryNacimiento=tk.Entry(root)
        self.entryNacimiento["bg"] = "#eaeaea"
        self.entryNacimiento["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.entryNacimiento["font"] = ft
        self.entryNacimiento["fg"] = "#787878"
        self.entryNacimiento["justify"] = "center"
        self.entryNacimiento["text"] = "**/**/**"
        self.entryNacimiento.place(x=200,y=350,width=80,height=30)

        botonRegistro=tk.Button(root)
        botonRegistro["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        botonRegistro["font"] = ft
        botonRegistro["fg"] = "#1f93ff"
        botonRegistro["justify"] = "center"
        botonRegistro["text"] = "REGISTRARSE"
        botonRegistro.place(x=225,y=430,width=150,height=40)
        botonRegistro["command"] = self.botonRegistro_command

        #botonCancelar=tk.Button(root)
        #botonCancelar["bg"] = "#ffffff"
        #ft = tkFont.Font(family='Times',size=14)
        #botonCancelar["font"] = ft
        #botonCancelar["fg"] = "#1f93ff"
        #botonCancelar["justify"] = "center"
        #botonCancelar["text"] = "CANCELAR"
        #botonCancelar.place(x=320,y=430,width=120,height=30)
        #botonCancelar["command"] = self.botonCancelar_command

    def botonRegistro_command(self):
        if len(self.entryUsuario.get()) != 0 and len(self.entryPassword.get()) != 0:
            cl=Cliente(self.entryUsuario.get(),self.entryPassword.get(),self.entryEmail.get(),self.entryNombre.get(),self.entryApellido.get(),self.entryNacimiento.get(),10,'No')
            cl.registrarse()
            messagebox.showinfo("Registro exitoso","Cierra la ventana de registro e inicia sesión")
            #root.destroy()
        else: messagebox.showinfo("Error","Complete los campos de usuario y contraseña")
    #def botonCancelar_command(self):
        #win=VRegistro(root)
        #win.destroy

if __name__ == "__main__":
    root = tk.Tk()
    app = VRegistro(root)
    root.mainloop()
