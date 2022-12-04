import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Función")
        #setting window size
        width=500
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        labelTitulo=tk.Label(root)
        labelTitulo["bg"] = "#1f93ff"
        ft = tkFont.Font(family='Times',size=16)
        labelTitulo["font"] = ft
        labelTitulo["fg"] = "#ffffff"
        labelTitulo["justify"] = "center"
        labelTitulo["text"] = "Cinemar"
        labelTitulo.place(x=0,y=0,width=500,height=40)

        labelSubtitulo=tk.Label(root)
        labelSubtitulo["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        labelSubtitulo["font"] = ft
        labelSubtitulo["fg"] = "#1f93ff"
        labelSubtitulo["justify"] = "center"
        labelSubtitulo["text"] = "Datos de la función"
        labelSubtitulo.place(x=0,y=35,width=500,height=25)

        background=tk.Label(root)
        background["bg"] = "#6f98aa"
        ft = tkFont.Font(family='Times',size=10)
        background["font"] = ft
        background["fg"] = "#ffffff"
        background["justify"] = "center"
        background["text"] = ""
        background.place(x=0,y=60,width=500,height=630)

        self.entryId=tk.Entry(root)
        self.entryId["borderwidth"] = "0px"
        self.entryId["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        self.entryId["font"] = ft
        self.entryId["fg"] = "#333333"
        self.entryId["justify"] = "left"
        self.entryId["text"] = ""
        self.entryId.place(x=100,y=100,width=100,height=25)

        self.entryFecha=tk.Entry(root)
        self.entryFecha["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        self.entryFecha["font"] = ft
        self.entryFecha["fg"] = "#333333"
        self.entryFecha["justify"] = "left"
        self.entryFecha["text"] = ""
        self.entryFecha.place(x=100,y=140,width=70,height=25)

        self.entryHora=tk.Entry(root)
        self.entryHora["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        self.entryHora["font"] = ft
        self.entryHora["fg"] = "#333333"
        self.entryHora["justify"] = "left"
        self.entryHora["text"] = ""
        self.entryHora.place(x=100,y=180,width=70,height=25)

        self.entryPelicula=tk.Entry(root)
        self.entryPelicula["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        self.entryPelicula["font"] = ft
        self.entryPelicula["fg"] = "#333333"
        self.entryPelicula["justify"] = "left"
        self.entryPelicula["text"] = ""
        self.entryPelicula.place(x=100,y=220,width=289,height=25)

        self.entryButacas=tk.Entry(root)
        self.entryButacas["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        self.entryButacas["font"] = ft
        self.entryButacas["fg"] = "#333333"
        self.entryButacas["justify"] = "left"
        self.entryButacas["text"] = ""
        self.entryButacas.place(x=100,y=260,width=40,height=25)

        self.entry3d=tk.Entry(root)
        self.entry3d["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        self.entry3d["font"] = ft
        self.entry3d["fg"] = "#333333"
        self.entry3d["justify"] = "left"
        self.entry3d["text"] = ""
        self.entry3d.place(x=100,y=300,width=40,height=25)

        self.entrySala=tk.Entry(root)
        self.entrySala["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        self.entrySala["font"] = ft
        self.entrySala["fg"] = "#333333"
        self.entrySala["justify"] = "left"
        self.entrySala["text"] = ""
        self.entrySala.place(x=100,y=340,width=42,height=25)

        self.entryPrecio=tk.Entry(root)
        self.entryPrecio["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        self.entryPrecio["font"] = ft
        self.entryPrecio["fg"] = "#333333"
        self.entryPrecio["justify"] = "left"
        self.entryPrecio["text"] = ""
        self.entryPrecio.place(x=100,y=380,width=50,height=25)

        labelId=tk.Label(root)
        labelId["bg"] = "#6f98aa"
        ft = tkFont.Font(family='Times',size=14)
        labelId["font"] = ft
        labelId["fg"] = "#ffffff"
        labelId["justify"] = "left"
        labelId["text"] = "Id"
        labelId.place(x=40,y=100,width=15,height=25)

        labelFecha=tk.Label(root)
        labelFecha["bg"] = "#6f98aa"
        ft = tkFont.Font(family='Times',size=14)
        labelFecha["font"] = ft
        labelFecha["fg"] = "#ffffff"
        labelFecha["justify"] = "left"
        labelFecha["text"] = "Fecha"
        labelFecha.place(x=40,y=140,width=38,height=25)

        labelHora=tk.Label(root)
        labelHora["bg"] = "#6f98aa"
        ft = tkFont.Font(family='Times',size=14)
        labelHora["font"] = ft
        labelHora["fg"] = "#ffffff"
        labelHora["justify"] = "left"
        labelHora["text"] = "Hora"
        labelHora.place(x=40,y=180,width=33,height=25)

        labelPelicula=tk.Label(root)
        labelPelicula["bg"] = "#6f98aa"
        ft = tkFont.Font(family='Times',size=14)
        labelPelicula["font"] = ft
        labelPelicula["fg"] = "#ffffff"
        labelPelicula["justify"] = "left"
        labelPelicula["text"] = "Película"
        labelPelicula.place(x=40,y=220,width=50,height=25)

        labelButacas=tk.Label(root)
        labelButacas["bg"] = "#6f98aa"
        ft = tkFont.Font(family='Times',size=14)
        labelButacas["font"] = ft
        labelButacas["fg"] = "#ffffff"
        labelButacas["justify"] = "left"
        labelButacas["text"] = "Butacas"
        labelButacas.place(x=40,y=260,width=50,height=25)

        label3d=tk.Label(root)
        label3d["bg"] = "#6f98aa"
        ft = tkFont.Font(family='Times',size=14)
        label3d["font"] = ft
        label3d["fg"] = "#ffffff"
        label3d["justify"] = "left"
        label3d["text"] = "3D"
        label3d.place(x=40,y=300,width=20,height=25)

        labelSala=tk.Label(root)
        labelSala["bg"] = "#6f98aa"
        ft = tkFont.Font(family='Times',size=14)
        labelSala["font"] = ft
        labelSala["fg"] = "#ffffff"
        labelSala["justify"] = "left"
        labelSala["text"] = "Sala"
        labelSala.place(x=40,y=340,width=28,height=25)

        labelPrecio=tk.Label(root)
        labelPrecio["bg"] = "#6f98aa"
        ft = tkFont.Font(family='Times',size=14)
        labelPrecio["font"] = ft
        labelPrecio["fg"] = "#ffffff"
        labelPrecio["justify"] = "left"
        labelPrecio["text"] = "Precio $"
        labelPrecio.place(x=40,y=380,width=50,height=25)

       

        botonGuardar=tk.Button(root)
        botonGuardar["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=14)
        botonGuardar["font"] = ft
        botonGuardar["fg"] = "#1f93ff"
        botonGuardar["justify"] = "center"
        botonGuardar["text"] = "Guardar"
        botonGuardar.place(x=110,y=440,width=120,height=30)
        botonGuardar["command"] = self.botonGuardar_command

    

        botonCancelar=tk.Button(root)
        botonCancelar["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=14)
        botonCancelar["font"] = ft
        botonCancelar["fg"] = "#1f93ff"
        botonCancelar["justify"] = "center"
        botonCancelar["text"] = "Cancelar"
        botonCancelar.place(x=280,y=440,width=120,height=30)
        botonCancelar["command"] = self.botonCancelar_command

    def botonGuardar_command(self):
        print("command")

    def botonCancelar_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
