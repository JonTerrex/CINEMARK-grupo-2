from tkinter import ttk
import tkinter 
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD

class VPeliculasCliente:
    def __init__(self,root):
        self.root=root
        self.root.title("Cinemar")
        width=1400
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        
        cabecera = ["Título","Estreno","Género","Duración", "Director", "Descripción","Clasificación"]

        conexion = Conexion_BD("BaseDeDatos.db")
        listaPelis = conexion.consulta("SELECT Titulo, Estreno, Genero, Duracion, Director, Descripcion, Clasificacion FROM Peliculas")
        conexion.cerrar()

        ft = tkFont.Font(family='Times',size="10")
        self.frameTabla=tkinter.LabelFrame(root,text="Películas")
        self.tb=ttk.Treeview(self.frameTabla,columns=tuple(cabecera),selectmode="extended")
        
        for t in cabecera:
            self.tb.column(t,width=120,anchor="center")
        for t in cabecera:
            self.tb.heading(t,text=t,anchor="w")
            
        for tupla in listaPelis:
            self.tb.insert("","end",text="",values=tupla)

        
        self.tb.pack(expand=1,fill="both")
        self.frameTabla.pack(side="top",anchor="s",expand=1,fill="both")
        
        
if __name__ == "__main__":
    root = tkinter.Tk()
    app = VPeliculasCliente(root)
    
    root.mainloop()
