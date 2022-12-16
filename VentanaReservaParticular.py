from tkinter import ttk
import tkinter 
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD

class VReservaParticular:
    def __init__(self,root, reservasParticulares):
        self.reservas = reservasParticulares
        self.root=root
        self.root.title("Cinemar")
        width=700
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        
        cabecera = ["Id Reserva", "Id Función","Id Cliente" ]

        #conexion = Conexion_BD("BaseDeDatos.db")
        #listaReservas = conexion.consulta(f"SELECT * FROM Reservas ORDER BY Fecha")
        #conexion.cerrar()

        scrollbar = tkinter.Scrollbar(root)
        scrollbar.pack(side="right", fill="y")
        ft = tkFont.Font(family='Times',size="10")
        self.frameTabla=tkinter.LabelFrame(root,text=f"Reservas particulares")
        self.tabReservas=ttk.Treeview(self.frameTabla,columns=tuple(cabecera),selectmode="extended",yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tabReservas.yview)

        for t in cabecera:
            self.tabReservas.column(t,width=100,anchor="center")
        for t in cabecera:
            self.tabReservas.heading(t,text=t,anchor="w")
            
        for tupla in reservasParticulares:
            self.tabReservas.insert("","end",text="",values=tupla)

        
        self.tabReservas.pack(expand=1,fill="both")
        self.frameTabla.pack(side="top",anchor="s",expand=1,fill="both")
        
        
if __name__ == "__main__":
    root = tkinter.Tk()
    app = VReservaParticular(root)
    
    root.mainloop()
