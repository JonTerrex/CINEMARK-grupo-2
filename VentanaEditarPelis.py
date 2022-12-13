import tkinter as tk
import tkinter.font as tkFont

class VentanaEditar(tk.Toplevel):
    def __init__(self, root,tituloFrame,titulo,editar=None):
        #setting title
        root.title(titulo)
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        if(editar is None):
            editar=["","","",""]
        
        self.titulo=titulo
        self.frame1=tk.LabelFrame(root,text=tituloFrame)

        self.nombre=tk.Label(self.frame1)
        ft = tkFont.Font(family='Times',size=10)
        self.nombre["font"] = ft
        self.nombre["fg"] = "#333333"
        self.nombre["justify"] = "left"
        self.nombre["text"] = "Nombre:"
        self.nombre.place(x=80,y=70,width=70,height=25)
        self.nombre.grid(row=0,column=0)
        
        self.nombreEntry=tk.Entry(self.frame1)
        self.nombreEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.nombreEntry["font"] = ft
        self.nombreEntry["fg"] = "#333333"
        self.nombreEntry["justify"] = "center"
        self.nombreEntry.place(x=300,y=70,width=70,height=25)
        self.nombreEntry.insert('0',editar[0])
        self.nombreEntry.grid(row=0,column=1)

        self.cantidad=tk.Label(self.frame1)
        ft = tkFont.Font(family='Times',size=10)
        self.cantidad["font"] = ft
        self.cantidad["fg"] = "#333333"
        self.cantidad["justify"] = "left"
        self.cantidad["text"] = "Cantidad:"
        self.cantidad.place(x=80,y=110,width=70,height=25)
        self.cantidad.grid(row=1,column=0)
        
        self.cantidadEntry=tk.Entry(self.frame1)
        self.cantidadEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.cantidadEntry["font"] = ft
        self.cantidadEntry["fg"] = "#333333"
        self.cantidadEntry["justify"] = "center"
        self.cantidadEntry.place(x=300,y=110,width=70,height=25)
        self.cantidadEntry.insert(0,editar[1])
        self.cantidadEntry.grid(row=1,column=1)
        

        self.precio=tk.Label(self.frame1)
        ft = tkFont.Font(family='Times',size=10)
        self.precio["font"] = ft
        self.precio["fg"] = "#333333"
        self.precio["justify"] = "left"
        self.precio["text"] = "Precio:"
        self.precio.place(x=80,y=160,width=70,height=25)
        self.precio.grid(row=2,column=0)
        
        self.precioEntry=tk.Entry(self.frame1)
        self.precioEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.precioEntry["font"] = ft
        self.precioEntry["fg"] = "#333333"
        self.precioEntry["justify"] = "center"
        self.precioEntry.place(x=300,y=160,width=70,height=25)
        self.precioEntry.insert('0',editar[2])
        self.precioEntry.grid(row=2,column=1)

        self.descripcion=tk.Label(self.frame1)
        ft = tkFont.Font(family='Times',size=10)
        self.descripcion["font"] = ft
        self.descripcion["fg"] = "#333333"
        self.descripcion["justify"] = "center"

        self.descripcion.place(x=80,y=210,width=70,height=25)
        self.descripcion.grid(row=3,column=0)

        self.descripcionText=tk.Text(self.frame1,height=10,width=20)
        self.descripcionText.grid(row=4,column=1)
        self.descripcionText.insert('0.0',editar[3])
        self.guardar=tk.Button(self.frame1,text="Guardar",command=self.__guardar)
        self.guardar.grid(row=5,column=0)
        
        self.datos=[]
        
        self.frame1.pack()
    
    def __guardar(self):
        self.datos=[self.nombreEntry.get(),self.cantidadEntry.get(),self.precioEntry.get(),self.descripcionText.get('0.0',"end")]
        super().destroy()

    def getCampos(self):
        return self.datos