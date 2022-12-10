import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
from baseDeDatos import Conexion_BD
from Funcion import Reserva
from Funcion import Catalogo
from Funcion import Pelicula
#from Funcion import Reservas

class VReservar:
    def __init__(self, root):
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
        i=0
        for p in pelis:
            listaPelis.append(pelis[i][0])
            i+=1
        self.menuPeliculas=ttk.Combobox(root, values = listaPelis)
        self.menuPeliculas.place(x=130,y=150, width=300)
        conexion=Conexion_BD("BaseDeDatos.db")
        peliActiva=conexion.consulta(f"SELECT * FROM Peliculas WHERE Titulo = '{self.menuPeliculas.get()}'")
        #peliObjeto=Pelicula(peliActiva[0][1],peliActiva[0][2],peliActiva[0][3],peliActiva[0][4],peliActiva[0][5],peliActiva[0][6],peliActiva[0][7])
        conexion.cerrar()

        labelFuncion=ttk.Label(root)
        labelFuncion["text"] = "Función"
        labelFuncion.place(x=50,y=230)

        conexion=Conexion_BD("BaseDeDatos.db")
        funciones=conexion.consulta(f"SELECT Fecha, Hora FROM Funciones INNER JOIN Peliculas ON Titulo = '{peliActiva}'")
        conexion.cerrar()
        self.menuFunciones=ttk.Combobox(root, values=funciones)
        self.menuFunciones.place(x=130,y=230, width=300)

        botonReservar=ttk.Button(root)
        botonReservar["text"] = "Reservar"
        botonReservar.place(x=190,y=420)
        #funcion = self.menuFunciones.get()
        #botonReservar["command"] = print(funcion)
        botonReservar["command"] = self.botonReservar_command

        labelCantidad=ttk.Label(root)
        labelCantidad["text"] = "Cantidad"
        labelCantidad.place(x=50,y=310)

        self.c = ttk.Spinbox(root, from_=1, to=10, width=3)
        self.c.place(x=130,y=307)
    
    def botonReservar_command(self):
        conexion=Conexion_BD("BaseDeDatos.db")
        peliActiva=conexion.consulta(f"SELECT * FROM Peliculas WHERE Titulo = '{self.menuPeliculas.get()}'")
        #peliObjeto=Pelicula(peliActiva[0],peliActiva[1],peliActiva[2],peliActiva[3],peliActiva[4],peliActiva[5],peliActiva[6])
        conexion.cerrar()
        print(peliActiva)
        #funcion = self.menuFunciones.get()
        #conexion=Conexion_BD("BaseDeDatos.db")
        #conexion.consulta(f"INSERT INTO Reservas (id_Funcion, id_Cliente) VALUES ({reservaPrueba.id_Funcion}, {reservaPrueba.id_Cliente})")
        #conexion.commit()
        #conexion.cerrar()
        #print(f"Reservaste {self.c.get()} entradas")



if __name__ == "__main__":
    root = tk.Tk()
    app = VReservar(root)
    root.mainloop()
