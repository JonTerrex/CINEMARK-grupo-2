import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from baseDeDatos import Conexion_BD
from Funcion import Reserva
from Funcion import Catalogo
from Funcion import Pelicula

class VReservar:
    def __init__(self, root, clienteActivo):
        self.cliente = clienteActivo
        root.title("Cinemar - Entradas")
        width=500
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        mainFrame=ttk.Frame(root)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=16)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Cinemar"
        labelTitulo.place(x=0,y=0,width=500,height=50)

        labelSubtitulo=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        labelSubtitulo["font"] = ft
        labelSubtitulo["fg"] = "#1f93ff"
        labelSubtitulo["justify"] = "center"
        labelSubtitulo["text"] = "Reservar entradas"
        labelSubtitulo.place(x=0,y=50,width=500,height=40)

        labelPelicula=ttk.Label(root)
        labelPelicula["text"] = "Película"
        labelPelicula.place(x=50,y=150)


        conexion=Conexion_BD("BaseDeDatos.db")
        pelis=conexion.consulta("SELECT Titulo FROM Peliculas ORDER BY Titulo")
        conexion.cerrar()
        listaPelis=[]
        for p in pelis:
            listaPelis.append(p[0])
        print(listaPelis)
        self.menuPeliculas=ttk.Combobox(root, values = listaPelis)
        self.menuPeliculas.bind('<<ComboboxSelected>>', self.cargarFuncion)
        self.menuPeliculas.place(x=130,y=150, width=300)
        conexion=Conexion_BD("BaseDeDatos.db")
        self.peliActiva=self.menuPeliculas.get()
        conexion.cerrar()

        labelFuncion=ttk.Label(root)
        labelFuncion["text"] = "Función"
        labelFuncion.place(x=50,y=230)

        self.menuFunciones=ttk.Combobox(root)
        self.menuFunciones.place(x=130,y=230, width=300)
        

        self.botonReservar=ttk.Button(root)
        self.botonReservar["text"] = "Reservar"
        self.botonReservar.place(x=190,y=420)
        #funcion = self.menuFunciones.get()
        #self.botonReservar["command"] = print(funcion)
        self.botonReservar["command"] = self.botonReservar_command

        labelCantidad=ttk.Label(root)
        labelCantidad["text"] = "Cantidad"
        labelCantidad.place(x=50,y=310)

        self.c = ttk.Spinbox(root, from_=1, to=10, width=3)
        self.c.place(x=130,y=307)
    def cargarFuncion(self, event):
        conexion=Conexion_BD("BaseDeDatos.db")
        self.funciones=conexion.consulta(f"SELECT f.id, f.id_Pelicula, Fecha, Hora FROM Funciones f INNER JOIN Peliculas p ON f.id_Pelicula = p.id WHERE p.Titulo = '{self.menuPeliculas.get()}'")
        funcionesCombobox = []
        for funcion in self.funciones:
            funcionesCombobox.append(funcion[2:])
        if funcionesCombobox:
            self.menuFunciones["state"] = 'normal'
            self.botonReservar["state"] = 'normal'
            self.menuFunciones["values"] = funcionesCombobox
        else:
            self.menuFunciones["state"] = 'disabled'
            self.botonReservar["state"] = 'disabled'
        print(funcionesCombobox)
        print(self.funciones)
        conexion.cerrar()

    def botonReservar_command(self):
        print(self.cliente)
        print(self.menuPeliculas.get())
        #funcion = self.menuFunciones.get()
        #conexion=Conexion_BD("BaseDeDatos.db")
        #conexion.consulta(f"INSERT INTO Reservas (id_Funcion, id_Cliente) VALUES ({reservaPrueba.id_Funcion}, {reservaPrueba.id_Cliente})")
        #conexion.commit()
        #
        #print(f"Reservaste {self.c.get()} entradas")



if __name__ == "__main__":
    root = tk.Tk()
    app = VReservar(root)
    root.mainloop()
