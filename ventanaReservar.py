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
        self.funciones = None
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
        listaPelis=[]
        for p in conexion.consulta("SELECT Titulo FROM Peliculas ORDER BY Titulo"):
            listaPelis.append(p[0])
        conexion.cerrar()
        self.menuPeliculas=ttk.Combobox(root, values = listaPelis)
        self.menuPeliculas.bind('<<ComboboxSelected>>', self.cargarFuncion)
        self.menuPeliculas.selection_clear()
        self.menuPeliculas.place(x=130,y=150, width=300)

        labelFuncion=ttk.Label(root)
        labelFuncion["text"] = "Función"
        labelFuncion.place(x=50,y=230)

        self.menuFunciones=ttk.Combobox(root)
        self.menuFunciones["state"]="disabled"
        self.menuFunciones.bind('<<ComboboxSelected>>', self.habilitarCantidad)
        self.menuFunciones.place(x=130,y=230, width=300)
        
        labelCantidad=ttk.Label(root)
        labelCantidad["text"] = "Cantidad"
        labelCantidad.place(x=50,y=310)

        self.c = ttk.Spinbox(root, from_=1, to=10, width=3,wrap=True)
        self.c["state"]="disabled"
        self.c.place(x=130,y=307)

        self.labelButacas=ttk.Label(root)
        self.labelButacas["text"] = "[No Hay Butacas disponibles]"
        self.labelButacas.place(x=200,y=307)

        self.botonReservar=ttk.Button(root)
        self.botonReservar["text"] = "Reservar"
        self.botonReservar.place(x=190,y=420)
        self.botonReservar["command"] = self.botonReservar_command

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
            self.menuFunciones["state"]="normal"
        else:
            self.menuFunciones.set('')
            self.menuFunciones["state"] = 'disabled'
            self.botonReservar["state"] = 'disabled'
            self.labelButacas["text"] = "[No Hay Butacas disponibles]"
        conexion.cerrar()

    def habilitarCantidad(self, event):
        conexion=Conexion_BD("BaseDeDatos.db")
        self.butacas=conexion.consulta(f"SELECT totalButacas FROM Funciones WHERE id = '{self.funciones[self.menuFunciones.current()][0]}'")
        self.butacas=self.butacas[0][0]
        if self.butacas:
            self.labelButacas["text"] = "[Hay {} Butacas disponibles]".format(self.butacas)
            self.c.config(from_=1,to=self.butacas)
            self.c.set('1')
            self.c["state"]="normal"
        else:
            self.c.set('')
            self.labelButacas["text"] = "[No Hay Butacas disponibles]"

    def botonReservar_command(self):
        reserva_actual = Reserva(self.funciones[self.menuFunciones.current()][0],self.cliente.usuario)
        #Llamada al método reservar del objeto tipo Reserva el cual devuelve en la propiedad id del mismo
        #el último id generado al agregar la reserva. (ver cursor.lastrowid)
        reserva_actual.reservar()
        #Si se devuelve el generado al reservar se agrega el detalle
        if reserva_actual.id:
            reserva_actual.detallar(int(self.c.get()))
            if reserva_actual.id_detalle_reservas:
                conexion=Conexion_BD("BaseDeDatos.db")
                #self.butacas -> Cantidad de butacas totales de la función actual
                #int(self.c.get()) -> Conversión de la cantidad seleccionada en el spinbox self.c
                #self.funciones[self.menuFunciones.current()][0] -> id de la función obtenido en el método cargarFuncion(self, event)
                #     self.menuFunciones.current() -> Valor del índice del opción seleccionada en el componente menuFunciones
                conexion.actualizar("UPDATE funciones SET totalButacas = ? WHERE id = ?", (self.butacas-int(self.c.get()),self.funciones[self.menuFunciones.current()][0]))





if __name__ == "__main__":
    root = tk.Tk()
    app = VReservar(root)
    root.mainloop()
