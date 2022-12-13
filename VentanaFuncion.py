import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from baseDeDatos import Conexion_BD

class VFuncion:
    def __init__(self, root):
        root.title("Función")
        width=300
        height=340
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        mainFrame = ttk.Frame(root)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=16)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Cinemar"
        labelTitulo.place(x=0,y=0,width=300,height=40)

        labelSubtitulo=tk.Label(root)
        labelSubtitulo["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        labelSubtitulo["font"] = ft
        labelSubtitulo["fg"] = "#1f93ff"
        labelSubtitulo["justify"] = "center"
        labelSubtitulo["text"] = "Datos de la función"
        labelSubtitulo.place(x=0,y=35,width=300,height=25)

        self.entryFecha=ttk.Entry(root)
        self.entryFecha["text"] = ""
        self.entryFecha.place(x=120,y=100,width=70)

        self.entryHora=ttk.Entry(root)
        self.entryHora["text"] = ""
        self.entryHora.place(x=120,y=140,width=70)

        self.entrySala=ttk.Entry(root)
        self.entrySala["text"] = ""
        self.entrySala.place(x=120,y=180,width=40)

        self.entryPelicula=ttk.Entry(root)
        self.entryPelicula["text"] = ""
        self.entryPelicula.place(x=120,y=220,width=40)

        labelFecha=ttk.Label(root)
        labelFecha["text"] = "Fecha"
        labelFecha.place(x=40,y=100)

        labelHora=ttk.Label(root)
        labelHora["text"] = "Hora"
        labelHora.place(x=40,y=140)

        labelSala=ttk.Label(root)
        labelSala["text"] = "id Sala"
        labelSala.place(x=40,y=180)

        labelPelicula=ttk.Label(root)
        labelPelicula["text"] = "id Película"
        labelPelicula.place(x=40,y=220)

        self.botonGuardar=ttk.Button(root)
        self.botonGuardar["text"] = "Guardar"
        self.botonGuardar.place(x=100,y=290)
        self.botonGuardar["command"] = self.botonGuardar_command

    def botonGuardar_command(self):
        conexion=Conexion_BD("BaseDeDatos.db")
        conexion.insertar("INSERT INTO Funciones (Fecha, Hora, id_Sala, id_Pelicula) VALUES (?,?,?,?)", (self.entryFecha.get(), self.entryHora.get(), self.entrySala.get(), self.entryPelicula.get()))
        messagebox.showinfo("", "Función creada con éxito")

if __name__ == "__main__":
    root = tk.Tk()
    app = VFuncion(root)
    root.mainloop()
