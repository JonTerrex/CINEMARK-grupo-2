import tkinter as tk
import tkinter.font as tkFont

class VDescuentos:
    def __init__(self, root):
        #setting title
        root.title("Cinemar")
        #setting window size
        width=400
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=16)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Cinemar - Descuentos"
        labelTitulo.place(x=0,y=0,width=400,height=40)

        background=tk.Label(root)
        background["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        background["font"] = ft
        background["fg"] = "#333333"
        background["justify"] = "center"
        background["text"] = ""
        background.place(x=0,y=40,width=400,height=455)

        self.entryLunes=tk.Entry(root)
        self.entryLunes["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=13)
        self.entryLunes["font"] = ft
        self.entryLunes["fg"] = "#333333"
        self.entryLunes["justify"] = "center"
        self.entryLunes["text"] = "20%"
        self.entryLunes.place(x=220,y=90,width=35,height=25)

        self.entryMartes=tk.Entry(root)
        self.entryMartes["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        self.entryMartes["font"] = ft
        self.entryMartes["fg"] = "#333333"
        self.entryMartes["justify"] = "center"
        self.entryMartes["text"] = "15%"
        self.entryMartes.place(x=220,y=140,width=35,height=25)

        self.entryMiercoles=tk.Entry(root)
        self.entryMiercoles["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        self.entryMiercoles["font"] = ft
        self.entryMiercoles["fg"] = "#333333"
        self.entryMiercoles["justify"] = "center"
        self.entryMiercoles["text"] = "20%"
        self.entryMiercoles.place(x=220,y=190,width=35,height=25)

        self.entryJueves=tk.Entry(root)
        self.entryJueves["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        self.entryJueves["font"] = ft
        self.entryJueves["fg"] = "#333333"
        self.entryJueves["justify"] = "center"
        self.entryJueves["text"] = "15%"
        self.entryJueves.place(x=220,y=240,width=35,height=25)

        self.entryViernes=tk.Entry(root)
        self.entryViernes["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        self.entryViernes["font"] = ft
        self.entryViernes["fg"] = "#333333"
        self.entryViernes["justify"] = "center"
        self.entryViernes["text"] = "10%"
        self.entryViernes.place(x=220,y=290,width=35,height=25)

        self.entrySabado=tk.Entry(root)
        self.entrySabado["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        self.entrySabado["font"] = ft
        self.entrySabado["fg"] = "#333333"
        self.entrySabado["justify"] = "center"
        self.entrySabado["text"] = "10%"
        self.entrySabado.place(x=220,y=340,width=35,height=25)

        self.entryDomingo=tk.Entry(root)
        self.entryDomingo["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        self.entryDomingo["font"] = ft
        self.entryDomingo["fg"] = "#333333"
        self.entryDomingo["justify"] = "center"
        self.entryDomingo["text"] = "10%"
        self.entryDomingo.place(x=220,y=390,width=35,height=25)

        labelLunes=tk.Label(root)
        labelLunes["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        labelLunes["font"] = ft
        labelLunes["fg"] = "#333333"
        labelLunes["justify"] = "right"
        labelLunes["text"] = "LUNES"
        labelLunes.place(x=130,y=90,width=70,height=25)

        labelMartes=tk.Label(root)
        labelMartes["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        labelMartes["font"] = ft
        labelMartes["fg"] = "#333333"
        labelMartes["justify"] = "right"
        labelMartes["text"] = "MARTES"
        labelMartes.place(x=130,y=140,width=70,height=25)

        labelMiercoles=tk.Label(root)
        labelMiercoles["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        labelMiercoles["font"] = ft
        labelMiercoles["fg"] = "#333333"
        labelMiercoles["justify"] = "right"
        labelMiercoles["text"] = "MIÉRCOLES"
        labelMiercoles.place(x=130,y=190,width=70,height=25)

        labelJueves=tk.Label(root)
        labelJueves["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        labelJueves["font"] = ft
        labelJueves["fg"] = "#333333"
        labelJueves["justify"] = "right"
        labelJueves["text"] = "JUEVES"
        labelJueves.place(x=130,y=240,width=70,height=25)

        labelViernes=tk.Label(root)
        labelViernes["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        labelViernes["font"] = ft
        labelViernes["fg"] = "#333333"
        labelViernes["justify"] = "right"
        labelViernes["text"] = "VIERNES"
        labelViernes.place(x=130,y=290,width=70,height=25)

        labelSabado=tk.Label(root)
        labelSabado["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        labelSabado["font"] = ft
        labelSabado["fg"] = "#333333"
        labelSabado["justify"] = "right"
        labelSabado["text"] = "SÁBADO"
        labelSabado.place(x=130,y=340,width=70,height=25)

        labelDomingo=tk.Label(root)
        labelDomingo["bg"] = '#ffffff'
        ft = tkFont.Font(family='Times',size=12)
        labelDomingo["font"] = ft
        labelDomingo["fg"] = "#333333"
        labelDomingo["justify"] = "right"
        labelDomingo["text"] = "DOMINGO"
        labelDomingo.place(x=130,y=390,width=70,height=25)

        botonEditar=tk.Button(root)
        botonEditar["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonEditar["font"] = ft
        botonEditar["fg"] = "#000000"
        botonEditar["justify"] = "center"
        botonEditar["text"] = "Editar"
        botonEditar.place(x=90,y=450,width=90,height=30)
        botonEditar["command"] = self.botonEditar_command

        botonGuardar=tk.Button(root)
        botonGuardar["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonGuardar["font"] = ft
        botonGuardar["fg"] = "#000000"
        botonGuardar["justify"] = "center"
        botonGuardar["text"] = "Guardar"
        botonGuardar.place(x=220,y=450,width=90,height=30)
        botonGuardar["command"] = self.botonGuardar_command


    def botonEditar_command(self):
        print("command")


    def botonGuardar_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = VDescuentos(root)
    root.mainloop()
