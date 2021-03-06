import tkinter as tk
from tkinter import ttk, CENTER

import Interpolation


class InterfazInterpolacion(tk.frame):
    #coordenadas
    x = list()
    y = list()
    #indice
    z = 0

    def __init__(self, master, parent):
        tk.Frame.__init__(self, parent)
        self.master = master
        self.message = tk.StringVar(value="Resultado    :")
        self.text = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.master = master
        master.title("Interpolacion")
        master.geometry("600x400")
        # Datos de x
        self.label = tk.Label(master, text="El punto en X")
        self.label.place(x=50, y=20)
        self.entry = ttk.Entry(master, textvariable=self.text)
        self.entry.place(x=50, y=50)
        # Datos de y
        self.label2 = tk.Label(master, text="El punto en y")
        self.label2.place(x=200, y=20)
        self.entry2 = ttk.Entry(master, textvariable=self.text2)
        self.entry2.place(x=200, y=50)
        # Datos del valor a evaluar
        self.label3 = tk.Label(master, text="Dato a ser evaluado")
        self.label3.place(x=350, y=20)
        self.entry3 = ttk.Entry(master, textvariable=self.text3)
        self.entry3.place(x=350, y=50)
        # Botones
        self.button = tk.Button(master, text="Agregar", command=self.agregar)
        self.button.place(x=50, y=80)
        self.button2 = tk.Button(master, text="Calcular", command=self.calcular)
        self.button2.place(x=200, y=80)
        self.button2 = tk.Button(master, text="Regresar", command=self.regresar)
        self.button2.place(x=350, y=80)
        # Create an object of Style widget
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # Add a Treeview widget
        self.tree = ttk.Treeview(master, column=("x", "y"),
                                 show='headings', height=5)
        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="x")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="y")
        self.tree.place(x=50, y=200)
        #Resultado
        self.label4 = tk.Label(master, text=self.message)
        self.label4.place(x=50, y=350)
        # self.place(width=1100, height=400)

    def calcular(self):
        # print("Calculate")
        data3 = self.text3.get()
        obj = Interpolation.Interpolation(self.x, self.y)
        obj.compute2(data3)
        return None

    def agregar(self):
        # print("ADD")
        data = self.text.get()
        data2 = self.text2.get()
        self.x.append(data)
        self.y.append(data2)
        self.z = self.z + 1
        self.tree.insert(parent='', index=self.z, iid=self.z, text='', values=(data, data2))
        # print(data, data2, data3)
        # print(self.text.get(), self.text2.get(), self.text3.get())
        return None

    def regresar(self):
        # print("RETURN")
        return None


#root = tk.Tk()
#root.eval('tk::PlaceWindow . center')
#app = InterfazInterpolacion(root)
#root.mainloop()
