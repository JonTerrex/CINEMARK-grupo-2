import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from ventanaDescuentos import VDescuentos
from VentanaFuncion import VFuncion
from VentanaPeliculasAdmin import VPeliculasAdmin
from VentanaReservasAdmin import VReservasAdmin
from VentanaFuncionesAdmin import VFuncionesAdmin

class VPrincipalAdmin:
    def __init__(self, root):
        root.title("Cinemar")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        
        mainFrame = ttk.Frame(root)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=18)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Cinemar - Menú Principal"
        labelTitulo.place(x=0,y=0,width=600,height=50)

        labelSubtitulo=tk.Label(root)
        labelSubtitulo["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=16)
        labelSubtitulo["font"] = ft
        labelSubtitulo["fg"] = "#1f93ff"
        labelSubtitulo["justify"] = "center"
        labelSubtitulo["text"] = "Bienvenido"
        labelSubtitulo.place(x=0,y=60,width=600,height=40)

        botonPeliculas=tk.Button(root)
        botonPeliculas["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonPeliculas["font"] = ft
        botonPeliculas["fg"] = "#000000"
        botonPeliculas["justify"] = "center"
        botonPeliculas["text"] = "PELICULAS"
        botonPeliculas.place(x=60,y=150,width=470,height=60)
        botonPeliculas["command"] = self.botonPeliculas_command

        botonEditarFuncion=tk.Button(root)
        botonEditarFuncion["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonEditarFuncion["font"] = ft
        botonEditarFuncion["fg"] = "#000000"
        botonEditarFuncion["justify"] = "center"
        botonEditarFuncion["text"] = "EDITAR FUNCIONES"
        botonEditarFuncion.place(x=330,y=260,width=200,height=60)
        botonEditarFuncion["command"] = self.botonEditarFuncion_command        

        botonDescuentos=tk.Button(root)
        botonDescuentos["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonDescuentos["font"] = ft
        botonDescuentos["fg"] = "#000000"
        botonDescuentos["justify"] = "center"
        botonDescuentos["text"] = "DESCUENTOS"
        botonDescuentos.place(x=60,y=370,width=200,height=60)
        botonDescuentos["command"] = self.botonDescuentos_command

        botonCrearFuncion=tk.Button(root)
        botonCrearFuncion["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonCrearFuncion["font"] = ft
        botonCrearFuncion["fg"] = "#000000"
        botonCrearFuncion["justify"] = "center"
        botonCrearFuncion["text"] = "CREAR FUNCIÓN"
        botonCrearFuncion.place(x=60,y=260,width=200,height=60)
        botonCrearFuncion["command"] = self.botonCrearFuncion_command

        botonReservas=tk.Button(root)
        botonReservas["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonReservas["font"] = ft
        botonReservas["fg"] = "#000000"
        botonReservas["justify"] = "center"
        botonReservas["text"] = "RESERVAS"
        botonReservas.place(x=330,y=370,width=200,height=60)
        botonReservas["command"] = self.botonReservas_command

    def botonPeliculas_command(self):
        winPelis = VPeliculasAdmin(tk.Toplevel())

    def botonEditarFuncion_command(self):
        winFunciones = VFuncionesAdmin(tk.Toplevel())


    def botonDescuentos_command(self):
        winDescuentos = VDescuentos(tk.Toplevel())


    def botonCrearFuncion_command(self):
        winCrearFuncion = VFuncion(tk.Toplevel())


    def botonReservas_command(self):
        winReservas = VReservasAdmin(tk.Toplevel())

if __name__ == "__main__":
    root = tk.Tk()
    app = VPrincipalAdmin(root)
    root.mainloop()
