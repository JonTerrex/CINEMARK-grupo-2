import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from baseDeDatos import Conexion_BD

class VDescuentos:
    def __init__(self, root):
        root.title("Cinemar")
        width=300
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        mainFrame = ttk.Frame(root)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=16)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Cinemar - Descuentos"
        labelTitulo.place(x=0,y=0,width=300,height=40)


        conexion = Conexion_BD("BaseDeDatos.db")
        descActuales = conexion.consulta("SELECT * FROM Descuentos")
        conexion.cerrar()
        
        actualesLabel = ttk.Label(root)
        actualesLabel["text"] = "Descuentos \n  Actuales"
        actualesLabel.place(x=165, y=50)

        LunesActual = ttk.Label(root)
        LunesActual.place(x=190, y=90)
        LunesActual["text"] = descActuales[0][0]

        MartesActual = ttk.Label(root)
        MartesActual.place(x=190, y=140)
        MartesActual["text"] = descActuales[0][1]

        MiercolesActual = ttk.Label(root)
        MiercolesActual.place(x=190, y=190)
        MiercolesActual["text"] = descActuales[0][2]

        JuevesActual = ttk.Label(root)
        JuevesActual.place(x=190, y=240)
        JuevesActual["text"] = descActuales[0][3]

        ViernesActual = ttk.Label(root)
        ViernesActual.place(x=190, y=290)
        ViernesActual["text"] = descActuales[0][4]

        SabadoActual = ttk.Label(root)
        SabadoActual.place(x=190, y=340)
        SabadoActual["text"] = descActuales[0][5]

        DomingoActual = ttk.Label(root)
        DomingoActual.place(x=190, y=390)
        DomingoActual["text"] = descActuales[0][6]

        self.entryLunes=ttk.Entry(root)
        self.entryLunes["text"] = ""
        self.entryLunes.place(x=120,y=90,width=35)

        self.entryMartes=ttk.Entry(root)
        self.entryMartes["text"] = ""
        self.entryMartes.place(x=120,y=140,width=35)

        self.entryMiercoles=ttk.Entry(root)
        self.entryMiercoles["text"] = ""
        self.entryMiercoles.place(x=120,y=190,width=35)

        self.entryJueves=ttk.Entry(root)
        self.entryJueves["text"] = ""
        self.entryJueves.place(x=120,y=240,width=35)

        self.entryViernes=ttk.Entry(root)
        self.entryViernes["text"] = ""
        self.entryViernes.place(x=120,y=290,width=35)

        self.entrySabado=ttk.Entry(root)
        self.entrySabado["text"] = ""
        self.entrySabado.place(x=120,y=340,width=35)

        self.entryDomingo=ttk.Entry(root)
        self.entryDomingo["text"] = ""
        self.entryDomingo.place(x=120,y=390,width=35)

        labelLunes=ttk.Label(root)
        labelLunes["text"] = "LUNES"
        labelLunes.place(x=30,y=90)

        labelMartes=ttk.Label(root)
        labelMartes["text"] = "MARTES"
        labelMartes.place(x=30,y=140)

        labelMiercoles=ttk.Label(root)
        labelMiercoles["text"] = "MIÉRCOLES"
        labelMiercoles.place(x=30,y=190)

        labelJueves=ttk.Label(root)
        labelJueves["text"] = "JUEVES"
        labelJueves.place(x=30,y=240)

        labelViernes=ttk.Label(root)
        labelViernes["text"] = "VIERNES"
        labelViernes.place(x=30,y=290)

        labelSabado=ttk.Label(root)
        labelSabado["text"] = "SÁBADO"
        labelSabado.place(x=30,y=340)

        labelDomingo=ttk.Label(root)
        labelDomingo["text"] = "DOMINGO"
        labelDomingo.place(x=30,y=390)

        botonGuardar=ttk.Button(root)
        botonGuardar["text"] = "Guardar"
        botonGuardar.place(x=100,y=450)
        botonGuardar["command"] = self.botonGuardar_command


    def botonGuardar_command(self):
        if self.entryLunes.get() == "" or self.entryMartes.get() == "" or self.entryMiercoles.get() == "" or self.entryJueves.get() == "" or self.entryViernes.get() == "" or self.entrySabado.get() == "" or self.entryDomingo.get() == "":
            messagebox.showerror("Error","Por favor complete todos los campos")
        else:
            conexion = Conexion_BD("BaseDeDatos.db")
            conexion.consulta(f"UPDATE Descuentos SET Lunes='{self.entryLunes.get()}', Martes='{self.entryMartes.get()}', Miércoles='{self.entryMiercoles.get()}', Jueves='{self.entryJueves.get()}', Viernes='{self.entryViernes.get()}', Sábado='{self.entrySabado.get()}', Domingo='{self.entryDomingo.get()}'")
            conexion.commit()
            conexion.cerrar()
            messagebox.showinfo("","Los descuentos se han actualizado exitosamente")

if __name__ == "__main__":
    root = tk.Tk()
    app = VDescuentos(root)
    root.mainloop()
