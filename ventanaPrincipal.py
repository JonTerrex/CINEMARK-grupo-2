import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Cinemark")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_972=tk.Label(root)
        GLabel_972["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_972["font"] = ft
        GLabel_972["fg"] = "#333333"
        GLabel_972["justify"] = "center"
        GLabel_972["text"] = ""
        GLabel_972.place(x=0,y=0,width=600,height=500)

        GLabel_96=tk.Label(root)
        GLabel_96["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_96["font"] = ft
        GLabel_96["fg"] = "#ffffff"
        GLabel_96["justify"] = "center"
        GLabel_96["text"] = "Cinemark - Menú Principal"
        GLabel_96.place(x=0,y=0,width=600,height=50)

        GButton_956=tk.Button(root)
        GButton_956["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_956["font"] = ft
        GButton_956["fg"] = "#000000"
        GButton_956["justify"] = "center"
        GButton_956["text"] = "SALAS"
        GButton_956.place(x=60,y=260,width=200,height=60)
        GButton_956["command"] = self.GButton_956_command

        GLabel_507=tk.Label(root)
        GLabel_507["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_507["font"] = ft
        GLabel_507["fg"] = "#333333"
        GLabel_507["justify"] = "center"
        GLabel_507["text"] = "Estás logueado como Administrador"
        GLabel_507.place(x=0,y=60,width=600,height=25)

        GButton_228=tk.Button(root)
        GButton_228["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_228["font"] = ft
        GButton_228["fg"] = "#000000"
        GButton_228["justify"] = "center"
        GButton_228["text"] = "DESCUENTOS"
        GButton_228.place(x=60,y=370,width=200,height=60)
        GButton_228["command"] = self.GButton_228_command

        GButton_560=tk.Button(root)
        GButton_560["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_560["font"] = ft
        GButton_560["fg"] = "#000000"
        GButton_560["justify"] = "center"
        GButton_560["text"] = "FUNCIONES"
        GButton_560.place(x=330,y=260,width=200,height=60)
        GButton_560["command"] = self.GButton_560_command

        GButton_908=tk.Button(root)
        GButton_908["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_908["font"] = ft
        GButton_908["fg"] = "#000000"
        GButton_908["justify"] = "center"
        GButton_908["text"] = "RESERVAS"
        GButton_908.place(x=330,y=370,width=200,height=60)
        GButton_908["command"] = self.GButton_908_command

    def GButton_956_command(self):
        print("command")


    def GButton_228_command(self):
        print("command")


    def GButton_560_command(self):
        print("command")


    def GButton_908_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
