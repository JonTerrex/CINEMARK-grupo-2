from tkinter import ttk
import tkinter 
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD

class VFuncionesCliente:
    def __init__(self,root):
        self.root=root
        self.root.title("Cinemar")
        width=900
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        
        cabecera = ["Fecha","Hora","Sala","Película","Butacas disponibles"]

        conexion = Conexion_BD("BaseDeDatos.db")
        listaFunciones = conexion.consulta("SELECT Fecha, Hora, id_Sala, Titulo, butacasLibres FROM Funciones f INNER JOIN Peliculas p ON f.id_Pelicula = p.id ORDER BY Fecha")
        conexion.cerrar()

        scrollbar = tkinter.Scrollbar(root)
        scrollbar.pack(side="right", fill="y")
        ft = tkFont.Font(family='Times',size="10")
        self.frameTabla=tkinter.LabelFrame(root,text="Funciones")
        self.tabFunciones=ttk.Treeview(self.frameTabla,columns=tuple(cabecera),selectmode="extended",yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tabFunciones.yview)
        
        for t in cabecera:
            self.tabFunciones.column(t,width=120,anchor="center")
        for t in cabecera:
            self.tabFunciones.heading(t,text=t,anchor="w")
            
        for tupla in listaFunciones:
            self.tabFunciones.insert("","end",text="",values=tupla)

        
        self.tabFunciones.pack(expand=1,fill="both")
        self.frameTabla.pack(side="top",anchor="s",expand=1,fill="both")
        
        
if __name__ == "__main__":
    root = tkinter.Tk()
    app = VFuncionesCliente(root)
    
    root.mainloop()
