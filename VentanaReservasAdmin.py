from tkinter import ttk
import tkinter 
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD
from VentanaReservaParticular import VReservaParticular

class VReservasAdmin:
    def __init__(self,root):
        self.root=root
        self.root.title("Cinemar")
        width=700
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        
        cabecera = ["Id Reserva", "Id Función", "Id Cliente"]

        conexion = Conexion_BD("BaseDeDatos.db")
        listaReservas = conexion.consulta(f"SELECT * FROM Reservas")
        conexion.cerrar()

        scrollbar = tkinter.Scrollbar(root)
        scrollbar.pack(side="right", fill="y")

        self.frameTabla=tkinter.LabelFrame(root,text=f"Reservas")
        self.frameFiltro=tkinter.Frame(root)
        self.tabReservas=ttk.Treeview(self.frameTabla,columns=tuple(cabecera),selectmode="extended",yscrollcommand=scrollbar.set)
        
        scrollbar.config(command=self.tabReservas.yview)
        labelUsuario = ttk.Label(self.frameFiltro, text="Mostrar reservas del usuario: ")
        

        self.botonFiltrar = ttk.Button(self.frameFiltro, text="Buscar reservas", command=self.botonFiltrar_command)

        for t in cabecera:
            self.tabReservas.column(t,width=100,anchor="center")
        for t in cabecera:
            self.tabReservas.heading(t,text=t,anchor="w")
            
        for tupla in listaReservas:
            self.tabReservas.insert("","end",text="",values=tupla)

    
        self.entryUsuario = ttk.Entry(self.frameFiltro)

        self.tabReservas.pack(expand=1,fill="both")
        self.frameTabla.pack(side="top",anchor="s",expand=1,fill="both")
        self.frameFiltro.pack(side="bottom")
        labelUsuario.pack(side="left", padx=5, pady=10)
        self.entryUsuario.pack(side="left", padx=5, pady=10)
        self.botonFiltrar.pack(side="right", padx=5, pady=10)
        self.tabReservas.bind('<ButtonRelease-1>', self.selectItem)
        root.bind('<Return>', lambda e: self.botonFiltrar.invoke())

    def selectItem(self, event):
        curItem = self.tabReservas.focus()
        #print(self.tabReservas.item(curItem))
        curItem = self.tabReservas.item(curItem)
        curItem = curItem["values"][2]
        print(curItem)
        
    def botonFiltrar_command(self):
        conexion = Conexion_BD("BaseDeDatos.db")
        reservasParticulares = conexion.consulta(f"SELECT * FROM Reservas WHERE id_Cliente = '{self.entryUsuario.get()}'")
        conexion.cerrar()
        vParticular = VReservaParticular(tkinter.Toplevel(), reservasParticulares)

        
if __name__ == "__main__":
    root = tkinter.Tk()
    app = VReservasAdmin(root)
    app.entryUsuario.focus()
    root.mainloop()
