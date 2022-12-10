import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
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

        mainFrame = ttk.Frame(root)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=18)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Bienvenido a Cinemar"
        labelTitulo.place(x=0,y=0,width=600,height=48)

        labelSubTitulo=ttk.Label(root)
        labelSubTitulo["anchor"] = "c"
        labelSubTitulo["text"] = "Crear Usuario"
        labelSubTitulo["relief"] = ""
        labelSubTitulo.place(x=0,y=50,width=600,height=30)

        self.entryNombre=ttk.Entry(root)
        self.entryNombre["text"] = ""
        self.entryNombre.place(x=100,y=150,width=200,height=30)

        self.entryApellido=ttk.Entry(root)
        self.entryApellido["text"] = ""
        self.entryApellido.place(x=390,y=150,width=181,height=30)

        labelNombre=ttk.Label(root)
        labelNombre["text"] = "Nombre"
        labelNombre.place(x=20,y=150,width=72,height=30)

        labelApellido=ttk.Label(root)
        labelApellido["text"] = "Apellido"
        labelApellido.place(x=320,y=150,width=71,height=30)

        labelEmail=ttk.Label(root)
        labelEmail["text"] = "E-mail"
        labelEmail.place(x=20,y=200,width=70,height=30)

        self.entryEmail=ttk.Entry(root)
        self.entryEmail["text"] = ""
        self.entryEmail.place(x=100,y=200,width=310,height=30)

        labelUsuario=ttk.Label(root)
        labelUsuario["text"] = "Usuario *"
        labelUsuario.place(x=20,y=250,width=103,height=30)

        self.entryUsuario=ttk.Entry(root)
        self.entryUsuario["text"] = ""
        self.entryUsuario.place(x=130,y=250,width=205,height=30)

        labelPassword=ttk.Label(root)
        labelPassword["text"] = "Contraseña *"
        labelPassword.place(x=20,y=300,width=103,height=30)

        self.entryPassword=ttk.Entry(root)
        self.entryPassword["text"] = ""
        self.entryPassword.place(x=130,y=300,width=205,height=30)

        labelNacimiento=ttk.Label(root)
        labelNacimiento["text"] = "Fecha de Nacimiento"
        labelNacimiento.place(x=20,y=350,width=170,height=30)

        self.entryNacimiento=ttk.Entry(root)
        self.entryNacimiento["text"] = "**/**/**"
        self.entryNacimiento.place(x=160,y=350,width=80,height=30)

        labelCampos=ttk.Label(root)
        labelCampos["text"] = "(*) Campos obligatorios"
        labelCampos.place(x=20,y=410)

        botonRegistro=ttk.Button(root)
        botonRegistro["text"] = "REGISTRARSE"
        botonRegistro.place(x=225,y=430,width=150,height=40)
        botonRegistro["command"] = self.botonRegistro_command

    def botonRegistro_command(self):
        if len(self.entryUsuario.get()) != 0 and len(self.entryPassword.get()) != 0:
            cl=Cliente(self.entryUsuario.get(),self.entryPassword.get(),self.entryEmail.get(),self.entryNombre.get(),self.entryApellido.get(),self.entryNacimiento.get(),10,'No')
            cl.registrarse()
            messagebox.showinfo("Registro exitoso","Cierra la ventana de registro e inicia sesión")
            self.root.destroy()
        else: messagebox.showinfo("Error de registro","Complete los campos de usuario y contraseña")

if __name__ == "__main__":
    root = tk.Tk()
    app = VRegistro(root)
    root.mainloop()
