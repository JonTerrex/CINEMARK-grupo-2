from tkinter import ttk
import tkinter 
from tkinter.messagebox import askyesno
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD
from ventanaEditarFunciones import VEditarFunciones


class VFuncionesAdmin:
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
        
        cabecera = ["Fecha","Hora","Sala", "id Película", "Película"]
        
        conexion = Conexion_BD("BaseDeDatos.db")
        listaPelis = conexion.consulta("SELECT Fecha,Hora,id_Sala, p.id, Titulo FROM Funciones f INNER JOIN Peliculas p ON f.id_Pelicula = p.id")
        conexion.cerrar()

        ft = tkFont.Font(family='Times',size="10")
        self.frameTabla=tkinter.LabelFrame(root,text="Funciones")
        self.tb=ttk.Treeview(self.frameTabla,columns=tuple(cabecera),selectmode="extended")
        
        for t in cabecera:
            self.tb.column(t,width=120,anchor="center")
        for t in cabecera:
            self.tb.heading(t,text=t,anchor="w")
            
        for tupla in listaPelis:
            self.tb.insert("","end",text="",values=tupla)


        self.frameBotones=tkinter.LabelFrame(root,text="Operaciones")
        self.editar=tkinter.Button(self.frameBotones,text="Editar",command=self.editarFuncion)
        self.eliminar=tkinter.Button(self.frameBotones,text="Eliminar",command=self.eliminarFuncion)
        self.agregar=tkinter.Button(self.frameBotones,text="Agregar",command=self.agregarFuncion)
        self.agregar.grid(row=0,column=0)
        self.editar.grid(row=0,column=1)
        self.eliminar.grid(row=0,column=2)
        
        
        self.tb.pack(expand=1,fill="both")
        self.frameTabla.pack(side="top",anchor="s",expand=1,fill="both")
        self.frameBotones.pack(side="bottom",anchor="s",fill="x",expand=1)
        
    def eliminarFuncion(self):
        items=self.tb.selection()
        mensaje = askyesno(message='Seguro que desea borrar esta función?', icon='question', title= 'Atención')
        
        selection=self.tb.focus()
        print(self.tb.item(selection)["values"])
        funcionElegida=self.tb.item(selection)["values"]
        print(funcionElegida)
        conexion = Conexion_BD("BaseDeDatos.db")
        idFunc = conexion.consulta(f"SELECT id FROM Funciones WHERE Fecha = '{funcionElegida[0]}' AND Hora = '{funcionElegida[1]}' AND id_Sala = '{funcionElegida[2]}' AND id_Pelicula = '{funcionElegida[3]}'") ## nos permite recuperar el id de la Peli, cuyo titutlo vino desde el llamdo de esta ventana.
        idFunc = int(idFunc[0][0])
        print(idFunc)

        if mensaje:
            conexion.consulta(f"DELETE FROM Funciones WHERE id={idFunc}")
            for item in items:
                self.tb.delete(item)
            conexion.commit()
            conexion.cerrar            
        
    def agregarFuncion(self):
        v=VEditarFunciones(tkinter.Tk(),"Nueva Función","Agregar Función")
        datos=v.getCampos()
        
    
    def editarFuncion(self):
        item=self.tb.focus()
        print(self.tb.item(item)["values"])
        v=VEditarFunciones(tkinter.Tk(),"Funciones","Editar",self.tb.item(item)["values"])
        
        

if __name__ == "__main__":
    root = tkinter.Tk()
    app = VFuncionesAdmin(root)
    root.mainloop()
