import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from baseDeDatos import Conexion_BD
from Funcion import Catalogo

class VReservar:
    def __init__(self, root):
        #setting title
        root.title("Cinemar - Entradas")
        #setting window size
        width=400
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
        background.place(x=0,y=0,width=400,height=500)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=16)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Cinemar"
        labelTitulo.place(x=0,y=0,width=400,height=50)

        labelSubtitulo=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        labelSubtitulo["font"] = ft
        labelSubtitulo["fg"] = "#1f93ff"
        labelSubtitulo["justify"] = "center"
        labelSubtitulo["text"] = "Reservar entradas"
        labelSubtitulo.place(x=0,y=50,width=400,height=40)

        labelPelicula=tk.Label(root)
        labelPelicula["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        labelPelicula["font"] = ft
        labelPelicula["fg"] = "#333333"
        labelPelicula["justify"] = "left"
        labelPelicula["text"] = "Película"
        labelPelicula.place(x=50,y=150,width=60,height=25)


        conexion=Conexion_BD("BaseDeDatos.db")
        pelis=conexion.consulta("SELECT Titulo FROM Peliculas")
        conexion.commit()
        conexion.cerrar()
        self.menuPeliculas=ttk.Combobox(root,  values = pelis)
        self.menuPeliculas.place(x=130,y=150)

        labelFuncion=tk.Label(root)
        labelFuncion["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        labelFuncion["font"] = ft
        labelFuncion["fg"] = "#333333"
        labelFuncion["justify"] = "left"
        labelFuncion["text"] = "Función"
        labelFuncion.place(x=50,y=230,width=60,height=25)

        funciones=[('Jueves 7 18:00 Sala 2'),('Viernes 8 21:00 Sala 1'), ('Sábado 9 20:30 Sala 3'), ('Domingo 10 22:00 Sala 2')]
        self.menuFunciones=ttk.Combobox(root, state="readonly", values=funciones)
        self.menuFunciones.place(x=130,y=230)

        botonReservar=tk.Button(root)
        botonReservar["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        botonReservar["font"] = ft
        botonReservar["fg"] = "#000000"
        botonReservar["justify"] = "center"
        botonReservar["text"] = "Reservar"
        botonReservar.place(x=150,y=420,width=100,height=40)
        botonReservar["command"] = self.botonReservar_command

        labelCantidad=tk.Label(root)
        labelCantidad["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        labelCantidad["font"] = ft
        labelCantidad["fg"] = "#333333"
        labelCantidad["justify"] = "left"
        labelCantidad["text"] = "Cantidad"
        labelCantidad.place(x=50,y=310,width=70,height=25)

        cantidad=[]
        for i in range(1,11):
            cantidad.append(i)
            i+=1
        self.menuCantidad=ttk.Combobox(root, state="readonly", values=cantidad)
        self.menuCantidad.place(x=130,y=310)
    
    def botonReservar_command(self):
        peli = self.menuPeliculas.get()
        print(f"La peli seleccionada es {peli}")
    def listarPeliculas():
        conexion = Conexion_BD("BaseDeDatos.db")
        conexion.consulta("SELECT Titulo FROM Peliculas")
        conexion.commit()
        conexion.cerrar()


if __name__ == "__main__":
    root = tk.Tk()
    app = VReservar(root)
    root.mainloop()
