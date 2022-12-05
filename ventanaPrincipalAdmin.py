import tkinter as tk
import tkinter.font as tkFont
from ventanaDescuentos import VDescuentos

class VPrincipalAdmin:
    def __init__(self, root):
        root.title("Cinemark")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        background=tk.Label(root)
        background["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        background["font"] = ft
        background["fg"] = "#333333"
        background["justify"] = "center"
        background["text"] = ""
        background.place(x=0,y=0,width=600,height=500)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=18)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Cinemark - Menú Principal"
        labelTitulo.place(x=0,y=0,width=600,height=50)

        botonSalas=tk.Button(root)
        botonSalas["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonSalas["font"] = ft
        botonSalas["fg"] = "#000000"
        botonSalas["justify"] = "center"
        botonSalas["text"] = "SALAS"
        botonSalas.place(x=60,y=260,width=200,height=60)
        botonSalas["command"] = self.botonSalas_command

        labelSubtitulo=tk.Label(root)
        labelSubtitulo["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=14)
        labelSubtitulo["font"] = ft
        labelSubtitulo["fg"] = "#01aaed"
        labelSubtitulo["justify"] = "center"
        labelSubtitulo["text"] = "Bienvenido"
        labelSubtitulo.place(x=0,y=60,width=600,height=40)

        botonDescuentos=tk.Button(root)
        botonDescuentos["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonDescuentos["font"] = ft
        botonDescuentos["fg"] = "#000000"
        botonDescuentos["justify"] = "center"
        botonDescuentos["text"] = "DESCUENTOS"
        botonDescuentos.place(x=60,y=370,width=200,height=60)

        botonDescuentos["command"] = self.botonDescuentos_command

        botonFunciones=tk.Button(root)
        botonFunciones["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonFunciones["font"] = ft
        botonFunciones["fg"] = "#000000"
        botonFunciones["justify"] = "center"
        botonFunciones["text"] = "FUNCIONES"
        botonFunciones.place(x=330,y=260,width=200,height=60)
        botonFunciones["command"] = self.botonFunciones_command

        botonReservas=tk.Button(root)
        botonReservas["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        botonReservas["font"] = ft
        botonReservas["fg"] = "#000000"
        botonReservas["justify"] = "center"
        botonReservas["text"] = "RESERVAS"
        botonReservas.place(x=330,y=370,width=200,height=60)
        botonReservas["command"] = self.botonReservas_command

    def botonSalas_command(self):
        print("command")


    def botonDescuentos_command(self):
        winDescuentos = VDescuentos(tk.Toplevel())


    def botonFunciones_command(self):
        print("command")


    def botonReservas_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = VPrincipalAdmin(root)
    root.mainloop()
