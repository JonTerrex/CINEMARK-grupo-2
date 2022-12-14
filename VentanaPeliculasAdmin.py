from tkinter import ttk
import tkinter 
from tkinter.messagebox import askyesno
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD
from VentanaEditarPelis import VentanaEditar

class VPeliculasAdmin:
    def __init__(self,root):
        self.root=root
        self.root.title("Cinemar")
        width=1400
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        cabecera = ["Título","Estreno","Género","Duración", "Director", "Descripción","Clasificación"]
        
        conexion = Conexion_BD("BaseDeDatos.db")
        #listaPelis = conexion.consulta("SELECT * FROM Peliculas")
        listaPelis = conexion.consulta("SELECT Titulo,Estreno,Genero,Duracion,Director,Descripcion,Clasificacion FROM Peliculas")
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


        self.frameBotones=tkinter.LabelFrame(root,text="Operaciones")
        self.editar=tkinter.Button(self.frameBotones,text="Editar",command=self.editarPelicula)
        self.eliminar=tkinter.Button(self.frameBotones,text="Eliminar",command=self.eliminarPelicula)
        self.agregar=tkinter.Button(self.frameBotones,text="Agregar",command=self.agregarPelicula)
        self.agregar.grid(row=0,column=0)
        self.editar.grid(row=0,column=1)
        self.eliminar.grid(row=0,column=2)
        
        
        self.tb.pack(expand=1,fill="both")
        self.frameTabla.pack(side="top",anchor="s",expand=1,fill="both")
        self.frameBotones.pack(side="bottom",anchor="s",fill="x",expand=1)
        
    def eliminarPelicula(self):
        items=self.tb.selection()
        mensaje = askyesno(message='Seguro que desea borrar esta película?', icon='question', title= 'Atención')
        if mensaje:
            for item in items:
                self.tb.delete(item)
            
        
    def agregarPelicula(self):
        v=VentanaEditar(tkinter.Tk(),"Nueva Película","Agregar Película")
        datos=v.getCampos()
        
    
    def editarPelicula(self):
        item=self.tb.focus()
        print(self.tb.item(item)["values"])
        v=VentanaEditar(tkinter.Tk(),"Película","Editar",self.tb.item(item)["values"])
        
        

if __name__ == "__main__":
    root = tkinter.Tk()
    app = VPeliculasAdmin(root)
    root.mainloop()
