from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from baseDeDatos import Conexion_BD
from ventanaEditReserva import VEditReserva

class VReservasCliente:
    def __init__(self,root, clienteActivo):
        self.cliente = clienteActivo
        self.root=root
        self.root.title("Cinemar")
        width=700
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        
        cabecera = ["Fecha", "Hora", "Película", "Cantidad"]

        conexion = Conexion_BD("BaseDeDatos.db")
        listaReservas = conexion.consulta(f"SELECT Fecha, Hora, Titulo, butacasReservadas FROM Reservas r INNER JOIN Funciones f ON r.id_Funcion = f.id AND r.id_Cliente = '{self.cliente.usuario}' INNER JOIN Peliculas p ON f.id_Pelicula = p.id INNER JOIN Detalle_Reservas d ON r.id = d.id_Reserva ORDER BY Fecha")
        conexion.cerrar()

        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side="right", fill="y")
        ft = tkFont.Font(family='Times',size="10")
        self.frameTabla=tk.LabelFrame(root,text=f"Reservas de {self.cliente.usuario}")
        self.tabReservas=ttk.Treeview(self.frameTabla,columns=tuple(cabecera),selectmode="extended",yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tabReservas.yview)

        self.botonModificar=ttk.Button(root)
        self.botonModificar["text"] = "Modificar Reserva"
        self.botonModificar.pack(side="bottom", pady=10)
        self.botonModificar["command"] = self.botonModificar_command

        for t in cabecera:
            self.tabReservas.column(t,width=100,anchor="center")
        for t in cabecera:
            self.tabReservas.heading(t,text=t,anchor="w")
            
        for tupla in listaReservas:
            self.tabReservas.insert("","end",text="",values=tupla)

        
        self.tabReservas.pack(expand=1,fill="both")
        self.frameTabla.pack(side="top",anchor="s",expand=1,fill="both")
    
    def botonModificar_command(self):
        winEditReserva = VEditReserva(tk.Toplevel(), self.cliente)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = VReservasCliente(root)
    
    root.mainloop()
