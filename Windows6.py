import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Windows3
import WindowMain
import MainG as j

class Ventana(tk.Toplevel):
    def __init__(self, parent,namebase):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 4")
        self.namebase=namebase
        label1 = Label(self,text=self.namebase)
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)

        label2 = Label(self,text="¡ Select your Funtion : ")
        label2.config(font=("Verdana", 20))
        label2.grid(row=3, column=3)
        boton1 = tk.Button(self, text="createTable", width=20, command=self.createTable)
        boton1.grid(row=5, column=2, padx=20, pady=30)
        boton2 = tk.Button(self, text="extractTable", width=20, command=self.extractTable)
        boton2.grid(row=5, column=3, padx=20, pady=30)
        boton3 = tk.Button(self, text="extractRangeTable", width=20, command=self.extractRangeTable)
        boton3.grid(row=5, column=4, padx=20, pady=30)
        boton4 = tk.Button(self, text="alterAddPK", width=20, command=self.alterAddPK)
        boton4.grid(row=5, column=2, padx=20, pady=30)
        boton5 = tk.Button(self, text="alterDropPK", width=20, command=self.alterDropPK)
        boton5.grid(row=5, column=3, padx=20, pady=30)
        boton6 = tk.Button(self, text="showTable", width=20, command=self.showTable)
        boton6.grid(row=5, column=4, padx=20, pady=30)
        boton7 = tk.Button(self, text="alterTable", width=20, command=self.alterTable)
        boton7.grid(row=5, column=2, padx=20, pady=30)
        boton10 = tk.Button(self, text="alterAddColumn", width=20, command=self.alteraddColumn)
        boton10.grid(row=5, column=4, padx=20, pady=30)
        boton9 = tk.Button(self, text="alterDropColumn", width=20, command=self.alterDropColumn)
        boton9.grid(row=5, column=4, padx=20, pady=30)
        boton8 = tk.Button(self, text="dropTable", width=20, command=self.dropTable)
        boton8.grid(row=5, column=4, padx=20, pady=30)
        label3 = Label(self,text="\nInsert Parameters")
        label3.config(font=("Verdana", 12))
        label3.grid(row=7, column=3)  
        
        self.parameters=tk.StringVar() 
        parametros=Entry(self, width=50,textvariable=self.parameters)
        parametros.grid(row=10,column=3)

        boton = tk.Button(self, text="Aplicar Cambios", width=20, command=self.ventana3)
        boton.grid(row=13, column=3, padx=20, pady=30)
        
        self.parent.withdraw()

    def ventana3(self):
        self.destroy()
        Windows3.Ventana(self.parent)
        
    def close(self):
        self.parent.destroy()
    
    def createTable(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.createDatabase(para[0])))

    def showTable(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.alterDatabase(para[0],para[1])))

    def extractTable(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.dropDatabase(para[0])))
   
    def extractRangeTable(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.createDatabase(para[0])))

    def alterAddPK(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.alterDatabase(para[0],para[1])))

    def alterDropPK(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.dropDatabase(para[0])))


    def alterTable(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.createDatabase(para[0])))

    def alteraddColumn(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.alterDatabase(para[0],para[1])))

    def alterDropColumn(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.dropDatabase(para[0])))

    def dropTable(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.dropDatabase(para[0])))
