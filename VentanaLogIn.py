import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD
from Usuario import Cliente
from ventanaPrincipalAdmin import VPrincipalAdmin
from ventanaPrincipalCliente import VPrincipalCliente
from ventanaRegistro import VRegistro

class App:
    def __init__(self, root):
        root.title("Cinemar Login")
        width=300
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        mainFrame=ttk.Frame(root)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=18)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Bienvenido a Cinemar"
        labelTitulo.place(x=0,y=0,width=300,height=66)

        labelUsuario=ttk.Label(root)
        labelUsuario["text"] = "Usuario"
        labelUsuario.place(x=120,y=130)

        self.entryUsuario=ttk.Entry(root)
        self.entryUsuario["text"] = ""
        self.entryUsuario.place(x=80,y=160,width=140,height=25)

        labelPassword=tk.Label(root)
        labelPassword["text"] = "Contraseña"
        labelPassword.place(x=110,y=210)

        self.entryPassword=ttk.Entry(root, show="*")
        self.entryPassword["text"] = ""
        self.entryPassword.place(x=80,y=240,width=140,height=25)

        

        labelLogin=tk.Label(root)
        labelLogin["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        labelLogin["font"] = ft
        labelLogin["fg"] = "#1f93ff"
        labelLogin["justify"] = "center"
        labelLogin["text"] = "Ingresá a tu cuenta"
        labelLogin.place(x=0,y=65,width=300,height=30)

        botonLogin=ttk.Button(root)
        botonLogin["text"] = "Iniciar Sesión"
        botonLogin.place(x=90,y=280,width=120,height=30)
        botonLogin["command"] = self.botonLogin_command
        root.bind('<Return>', lambda e: botonLogin.invoke())

        labelSinCuenta=ttk.Label(root)
        labelSinCuenta["text"] = "¿No tenés cuenta?"
        labelSinCuenta.place(x=90,y=380)

        botonRegistro=ttk.Button(root)
        botonRegistro["text"] = "Registrate"
        botonRegistro.place(x=95,y=410)
        botonRegistro["command"] = self.botonRegistro_command
        
        
    def botonLogin_command(self):
        usuario = self.entryUsuario.get()
        password = self.entryPassword.get()
        conexion=Conexion_BD("BaseDeDatos.db")
        if conexion.consulta(f"SELECT * FROM Clientes WHERE usuario = '{usuario}' AND '{password}' == password"):
            cliente1=conexion.consulta(f"SELECT * FROM Clientes WHERE usuario = '{usuario}' AND '{password}' == password")
            clienteActivo=Cliente(*cliente1[0])
            
            if cliente1[0][8] == 'Admin':
                ventanaAdmin=VPrincipalAdmin(tk.Toplevel())
            else:
                ventanaCliente=VPrincipalCliente(tk.Toplevel(),clienteActivo)
        else:
            messagebox.showinfo("Error","Usuario o contraseña incorrecta")
        conexion.cerrar()


    def botonRegistro_command(self):
        winRegistro=VRegistro(tk.Toplevel())


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.entryUsuario.focus()
    root.mainloop()
