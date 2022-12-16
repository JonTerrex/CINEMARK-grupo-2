import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD

class VAgregar:
    def __init__(self, root,tituloFrame,titulo,editar=None):
        root.title(titulo)
        width=400
        height=360
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        

        if(editar is None):
            editar=["","","","","","",""]
        
        self.titulo=titulo
        self.frame1=ttk.LabelFrame(root,text=tituloFrame)
        

        self.titulo=ttk.Label(self.frame1)
        self.titulo["text"] = "Título:"
        self.titulo.grid(row=0,column=0)
        
        self.tituloEntry=ttk.Entry(self.frame1)
        self.tituloEntry.insert('0',editar[0])
        self.tituloEntry.grid(row=0,column=1)

        self.estreno=ttk.Label(self.frame1)
        self.estreno["text"] = "Estreno:"
        self.estreno.grid(row=1,column=0)
        
        self.estrenoEntry=ttk.Entry(self.frame1)
        self.estrenoEntry.insert('0',editar[1])
        self.estrenoEntry.grid(row=1,column=1)
        

        self.genero=ttk.Label(self.frame1)
        self.genero["text"] = "Género:"
        self.genero.grid(row=2,column=0)
        
        self.generoEntry=ttk.Entry(self.frame1)
        self.generoEntry.insert('0',editar[2])
        self.generoEntry.grid(row=2,column=1)

        self.duracion=ttk.Label(self.frame1)
        self.duracion["text"] = "Duración:"
        self.duracion.grid(row=3,column=0)
        
        self.duracionEntry=ttk.Entry(self.frame1)
        self.duracionEntry.insert('0',editar[3])
        self.duracionEntry.grid(row=3,column=1)

        self.director=ttk.Label(self.frame1)
        self.director["text"] = "Género:"
        self.director.grid(row=4,column=0)
        
        self.directorEntry=ttk.Entry(self.frame1)
        self.directorEntry.insert('0',editar[4])
        self.directorEntry.grid(row=4,column=1)

        self.descripcion=ttk.Label(self.frame1)
        self.descripcion.grid(row=5,column=0)

        self.descripcionText=tk.Text(self.frame1,height=10,width=20, wrap="word")
        self.descripcionText.grid(row=5,column=1)
        self.descripcionText.insert('0.0',editar[5])

        self.clasificacion=ttk.Label(self.frame1)
        self.clasificacion["text"] = "Clasificación:"
        self.clasificacion.grid(row=6,column=0)
        
        self.clasificacionEntry=ttk.Entry(self.frame1)
        self.clasificacionEntry.insert('0',editar[6])
        self.clasificacionEntry.grid(row=6,column=1)

        self.guardar=ttk.Button(self.frame1,text="Guardar",command=self.__guardar)
        self.guardar.grid(row=7,column=1)

        self.datos=[]

        self.frame1.pack(fill="both",expand=5)
    
    def __guardar(self):
        conexion = Conexion_BD("BaseDeDatos.db")
        conexion.insertar("INSERT INTO Peliculas (Titulo, Estreno, Genero, Duracion, Director, Descripcion, Clasificacion) VALUES (?,?,?,?,?,?,?)", (self.tituloEntry.get(),self.estrenoEntry.get(),self.generoEntry.get(),self.duracionEntry.get(),self.directorEntry.get(),self.descripcionText.get('0.0',"end"),self.clasificacionEntry.get()))
        self.datos=[self.tituloEntry.get(),self.estrenoEntry.get(),self.generoEntry.get(),self.duracionEntry.get(),self.directorEntry.get(),self.descripcionText.get('0.0',"end"),self.clasificacionEntry.get()]

    def getCampos(self):
        return self.datos