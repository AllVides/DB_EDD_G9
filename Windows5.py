import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import Windows3
import MainG as m

import WindowMain

class Ventana(tk.Toplevel):
    def __init__(self, parent,namebase):
        super().__init__(parent)
        self.parent = parent
        self.namebase=namebase
        self.basesdatos=[]
        self.b()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Ventana 4")

        label1 = Label(self,text=namebase)
        label1.config(font=("Verdana", 35))
        label1.grid(row=1, column=3)

        label2 = Label(self,text="¡ Tablas : ")
        label2.config(font=("Verdana", 20))
        label2.grid(row=3, column=3)
        label5=Label(self,text="representacion de las tablas")

        label5.config(font=("Verdana", 20))
        label5.grid(row=5, column=3)

        self.bases=tk.StringVar(self)
        self.bases.set('Seleccionar...')
        d=[0,0,0,0]
        menu = tk.OptionMenu(self, self.bases, *d)
        menu.config(width=20)
        menu.grid(row = 7, column = 10, padx = 30, pady = 30)


        button1 = Button(self, text= 'Atras', padx= 15, pady=6, bg= 'grey',fg='white',command=self.ventana3)
        button1.grid(row=8, column=0)
#        button5 = Button(self, text= 'Enter to Base', padx= 15, pady=6, bg= 'grey',fg='white',command=self.Ventana4)
 #       button5.grid(row=8, column=10)
  #      button2 = Button(self, text= 'Function Data', padx= 15, pady=6, bg= 'grey',fg='white',command=self.Ventana4)
   #     button2.grid(row=8, column=15)
        
        
        self.parent.withdraw()

    def ventana3(self):
        self.destroy()
        Windows3.Ventana(self.parent)
        
    def close(self):
        self.parent.destroy()
        
    def b(self):
        self.basesdatos.clear()
        if len(m.showDatabases())!=0:
            for k in m.showTables(self.namebase):
                self.basesdatos.append(k)
        elif len(self.basesdatos)==0:
            self.basesdatos.append("l")
            self.basesdatos.append("l")
