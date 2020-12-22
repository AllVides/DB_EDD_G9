import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Windows5
import WindowMain
import MainG as j

class Ventana(tk.Toplevel):
    def __init__(self, parent,namebase,nametable):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 7")
        self.namebase=namebase
        self.nametable=nametable
        label1 = Label(self,text=self.namebase + " --- "+self.nametable)
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)

        label2 = Label(self,text="¡ FUNCIONES EN TUPLAS ! ")
        label2.config(font=("Verdana", 20))
        label2.grid(row=3, column=3)
        boton1 = tk.Button(self, text="insertar", width=20, command=self.insertar)
        boton1.grid(row=5, column=2, padx=20, pady=30)
        boton2 = tk.Button(self, text="extractRow", width=20, command=self.extractRow)
        boton2.grid(row=5, column=3, padx=20, pady=30)
        boton3 = tk.Button(self, text="update", width=20, command=self.update)
        boton3.grid(row=5, column=4, padx=20, pady=30)
        boton4 = tk.Button(self, text="truncate", width=20, command=self.truncate)
        boton4.grid(row=5, column=5, padx=20, pady=30)
        label3 = Label(self,text="\nInsert Parameters")
        label3.config(font=("Verdana", 12))
        label3.grid(row=9, column=3)  
        
        self.b=tk.StringVar() 
        base=Entry(self, width=50,textvariable=self.b)
        base.grid(row=10,column=2)
        self.t=tk.StringVar() 
        tablita=Entry(self, width=50,textvariable=self.t)
        tablita.grid(row=10,column=3)
        self.l=tk.StringVar() 
        lista=Entry(self, width=50,textvariable=self.l)
        lista.grid(row=10,column=4)

        boton = tk.Button(self, text="Aplicar Cambios", width=20, command=self.atras)
        boton.grid(row=13, column=3, padx=20, pady=30)
        
        self.parent.withdraw()

    def atras(self):
        self.destroy()
        print(self.namebase)
        Windows5.Ventana(self.parent,self.namebase)
        
    def close(self):
        self.parent.destroy()
    
    def insertar(self): 
        base=str(self.b.get())
        tabla=str(self.t.get())
        lista=self.l.get()
        datos = lista.lstrip("[")
        datos=datos.rstrip("]")
        dat=datos.split(",")     
        arreglo=[]
        for i in dat:
            arreglo.append(i)

        print(arreglo)

        messagebox.showinfo("Funcion de base de datos",str(j.insert(base,tabla,arreglo)))
        print(j.extractTable(base,tabla)) 

    def extractRow(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.extractRow()))

    def update(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.update(para[0],para[1],para[2],para[3])))
   
    def truncate(self):
        parametros=str(self.parameters.get())
        para=parametros.split(",")
        messagebox.showinfo("Funcion de base de datos",str(j.truncate(para[0],para[1])))

    