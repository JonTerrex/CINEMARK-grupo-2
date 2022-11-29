import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Cinemar Login")
        #setting window size
        width=300
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        labelUsuario=tk.Label(root)
        labelUsuario["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=12)
        labelUsuario["font"] = ft
        labelUsuario["fg"] = "#333333"
        labelUsuario["justify"] = "center"
        labelUsuario["text"] = "Usuario"
        labelUsuario.place(x=110,y=130,width=70,height=25)

        self.entryUsuario=tk.Entry(root)
        self.entryUsuario["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.entryUsuario["font"] = ft
        self.entryUsuario["fg"] = "#939393"
        self.entryUsuario["justify"] = "center"
        self.entryUsuario["text"] = ""
        self.entryUsuario.place(x=80,y=160,width=140,height=25)

        labelPassword=tk.Label(root)
        labelPassword["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=12)
        labelPassword["font"] = ft
        labelPassword["fg"] = "#333333"
        labelPassword["justify"] = "center"
        labelPassword["text"] = "Contraseña"
        labelPassword.place(x=110,y=210,width=70,height=25)

        self.entryPassword=tk.Entry(root)
        self.entryPassword["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.entryPassword["font"] = ft
        self.entryPassword["fg"] = "#939393"
        self.entryPassword["justify"] = "center"
        self.entryPassword["text"] = ""
        self.entryPassword.place(x=80,y=240,width=140,height=25)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=18)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Bienvenido a Cinemar"
        labelTitulo.place(x=0,y=0,width=300,height=66)

        labelLogin=tk.Label(root)
        labelLogin["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        labelLogin["font"] = ft
        labelLogin["fg"] = "#1f93ff"
        labelLogin["justify"] = "center"
        labelLogin["text"] = "Ingresá a tu cuenta"
        labelLogin.place(x=0,y=65,width=300,height=30)

        botonLogin=tk.Button(root)
        botonLogin["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=14)
        botonLogin["font"] = ft
        botonLogin["fg"] = "#1f93ff"
        botonLogin["justify"] = "center"
        botonLogin["text"] = "Iniciar Sesión"
        botonLogin.place(x=90,y=280,width=120,height=30)
        botonLogin["command"] = self.botonLogin_command

        labelSinCuenta=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        labelSinCuenta["font"] = ft
        labelSinCuenta["fg"] = "#939393"
        labelSinCuenta["justify"] = "center"
        labelSinCuenta["text"] = "¿No tenés cuenta?"
        labelSinCuenta.place(x=90,y=380,width=130,height=25)

        botonRegistro=tk.Button(root)
        botonRegistro["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=14)
        botonRegistro["font"] = ft
        botonRegistro["fg"] = "#1f93ff"
        botonRegistro["justify"] = "center"
        botonRegistro["text"] = "Registrate"
        botonRegistro.place(x=90,y=410,width=120,height=30)
        botonRegistro["command"] = self.botonRegistro_command

    def botonLogin_command(self):
        print("command")


    def botonRegistro_command(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
