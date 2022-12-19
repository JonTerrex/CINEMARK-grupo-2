import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD

class VEditarFunciones:
    def __init__(self, root,tituloFrame,titulo,editar=None):
        root.title(titulo)
        width=300
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        self.funcionAntes=editar
        print(self.funcionAntes)
        conexion = Conexion_BD("BaseDeDatos.db")
        self.idFuncion = conexion.consulta(f"SELECT id FROM Funciones WHERE Fecha = '{self.funcionAntes[0]}' AND Hora = '{self.funcionAntes[1]}' AND id_sala = '{self.funcionAntes[2]}' AND id_pelicula= '{self.funcionAntes[3]}'") ## nos permite recuperar el id de la Funcion
        self.idFuncion = int(self.idFuncion[0][0])
        print(self.idFuncion)
        conexion.cerrar()
        
        if(editar is None):
            editar=["","","",""]
        
        self.titulo=titulo
        self.frame1=ttk.LabelFrame(root,text=tituloFrame)
        

        self.fecha=ttk.Label(self.frame1)
        self.fecha["text"] = "Fecha:"
        self.fecha.grid(row=0,column=0)
        
        self.fechaEntry=ttk.Entry(self.frame1)
        self.fechaEntry.insert('0',editar[0])
        self.fechaEntry.grid(row=0,column=1)

        self.hora=ttk.Label(self.frame1)
        self.hora["text"] = "Hora:"
        self.hora.grid(row=1,column=0)
        
        self.horaEntry=ttk.Entry(self.frame1)
        self.horaEntry.insert('0',editar[1])
        self.horaEntry.grid(row=1,column=1)
        

        self.sala=ttk.Label(self.frame1)
        self.sala["text"] = "Sala:"
        self.sala.grid(row=2,column=0)
        
        self.salaEntry=ttk.Entry(self.frame1)
        self.salaEntry.insert('0',editar[2])
        self.salaEntry.grid(row=2,column=1)

        self.idPelicula=ttk.Label(self.frame1)
        self.idPelicula["text"] = "id Película:"
        self.idPelicula.grid(row=3,column=0)
        
        self.idPeliculaEntry=ttk.Entry(self.frame1)
        self.idPeliculaEntry.insert('0',editar[3])
        self.idPeliculaEntry.grid(row=3,column=1)

        self.guardar=ttk.Button(self.frame1,text="Guardar",command=self.__guardar)
        self.guardar.grid(row=4,column=1)

        self.datos=[]

        self.frame1.pack(fill="both",expand=5)
    
    def __guardar(self):
        conexion = Conexion_BD("BaseDeDatos.db")
        conexion.actualizar("UPDATE Funciones SET Fecha = ?, Hora = ?, id_Sala = ?, id_Pelicula = ? WHERE id = ?", (self.fechaEntry.get(),self.horaEntry.get(),self.salaEntry.get(),self.idPeliculaEntry.get(), self.idFuncion))
        self.datos=[self.fechaEntry.get(),self.horaEntry.get(),self.salaEntry.get(),self.idPeliculaEntry.get()]

    def getCampos(self):
        return self.datos