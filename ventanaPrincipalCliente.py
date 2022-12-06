import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from ventanaReservar import VReservar

class VPrincipalCliente:
    def __init__(self, root):
        root.title("Cinemark")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        background=tk.Label(root)
        background["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        background["font"] = ft
        background["fg"] = "#333333"
        background["justify"] = "center"
        background["text"] = ""
        background.place(x=0,y=0,width=600,height=500)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=18)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Cinemark - Menú Principal"
        labelTitulo.place(x=0,y=0,width=600,height=50)

        botonPeliculas=tk.Button(root)
        botonPeliculas["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonPeliculas["font"] = ft
        botonPeliculas["fg"] = "#000000"
        botonPeliculas["justify"] = "center"
        botonPeliculas["text"] = "PELICULAS"
        botonPeliculas.place(x=60,y=260,width=200,height=60)
        botonPeliculas["command"] = self.botonPeliculas_command

        labelSubtitulo=tk.Label(root)
        labelSubtitulo["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=14)
        labelSubtitulo["font"] = ft
        labelSubtitulo["fg"] = "#01aaed"
        labelSubtitulo["justify"] = "center"
        labelSubtitulo["text"] = "Bienvenido"
        labelSubtitulo.place(x=0,y=60,width=600,height=40)

        botonReservar=tk.Button(root)
        botonReservar["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonReservar["font"] = ft
        botonReservar["fg"] = "#000000"
        botonReservar["justify"] = "center"
        botonReservar["text"] = "RESERVAR"
        botonReservar.place(x=60,y=370,width=200,height=60)
        botonReservar["command"] = self.botonReservar_command

        botonFunciones=tk.Button(root)
        botonFunciones["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonFunciones["font"] = ft
        botonFunciones["fg"] = "#000000"
        botonFunciones["justify"] = "center"
        botonFunciones["text"] = "FUNCIONES"
        botonFunciones.place(x=330,y=260,width=200,height=60)
        botonFunciones["command"] = self.botonFunciones_command

        botonReservas=tk.Button(root)
        botonReservas["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonReservas["font"] = ft
        botonReservas["fg"] = "#000000"
        botonReservas["justify"] = "center"
        botonReservas["text"] = "VER RESERVAS"
        botonReservas.place(x=330,y=370,width=200,height=60)
        botonReservas["command"] = self.botonReservas_command

    def botonPeliculas_command(self):
        print("command")


    def botonReservar_command(self):
        vReservar=VReservar(tk.Toplevel())


    def botonFunciones_command(self):
        print("command")


    def botonReservas_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = VPrincipalCliente(root)
    root.mainloop()
