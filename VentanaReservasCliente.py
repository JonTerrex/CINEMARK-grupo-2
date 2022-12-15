from tkinter import ttk
import tkinter 
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD

class VReservasCliente:
    def __init__(self,root, clienteActivo):
        self.cliente = clienteActivo
        self.root=root
        self.root.title("Cinemar")
        width=1400
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        
        cabecera = ["Fecha", "Hora", "Película", "Cantidad"]

        conexion = Conexion_BD("BaseDeDatos.db")
        listaReservas = conexion.consulta(f"SELECT Fecha, Hora, Titulo, butacasReservadas FROM Reservas r INNER JOIN Funciones f ON r.id_Funcion = f.id AND r.id_Cliente = '{self.cliente.usuario}' INNER JOIN Peliculas p ON f.id_Pelicula = p.id INNER JOIN Detalle_Reservas d ON r.id = d.id_Reserva ORDER BY Fecha")
        print(type(listaReservas))
        conexion.cerrar()

        ft = tkFont.Font(family='Times',size="10")
        self.frameTabla=tkinter.LabelFrame(root,text=f"Reservas de {self.cliente.usuario}")
        self.tb=ttk.Treeview(self.frameTabla,columns=tuple(cabecera),selectmode="extended")
        
        for t in cabecera:
            self.tb.column(t,width=120,anchor="center")
        for t in cabecera:
            self.tb.heading(t,text=t,anchor="w")
            
        for tupla in listaReservas:
            self.tb.insert("","end",text="",values=tupla)

        
        self.tb.pack(expand=1,fill="both")
        self.frameTabla.pack(side="top",anchor="s",expand=1,fill="both")
        
        
if __name__ == "__main__":
    root = tkinter.Tk()
    app = VReservasCliente(root)
    
    root.mainloop()
