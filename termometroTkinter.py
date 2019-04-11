'''
Created on 10 abr. 2019

@author: meyi
'''

from tkinter import *
from tkinter import  ttk

class Ventana(Tk):
    '''
    Atributos
    '''
    __tamaño = "250x300"
    entrada = None
    unidad = None
    __temperaturaAnterior = ""
    
    def __init__(self):
        '''
        Constructor
        '''
        Tk.__init__(self)
        self.geometry(self.__tamaño)
        self.title("Termómetro")
        self.configure(bg = "#D8D8D8")
        
        self.temperatura = StringVar(value="")
        self.temperatura.trace("w", self.validacion)
        self.unidad = StringVar(value="")
        
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura, width=25).place(x=20, y=20)
        self.lbUnidad = ttk.Label(self, text="Grados:").place(x=20, y=55)
        self.rbtnF = ttk.Radiobutton(self, text="Faharenheit", variable=self.unidad, value="F", command=self.seleccion).place(x=20, y=80)
        self.rbtnC = ttk.Radiobutton(self, text="Centígrados", variable=self.unidad, value="C", command=self.seleccion).place(x=20, y=105)
     
    def validacion(self, *args):
        nuevoValor = self.temperatura.get()
        try:
            float(nuevoValor)
            self.__temperaturaAnterior = nuevoValor
        except:
            self.temperatura.set(self.__temperaturaAnterior)
    
    def seleccion(self):
        resultado = 0
        toUnidad = self.unidad.get()        
        grados = float(self.temperatura.get())
        
        if toUnidad == "F":
            resultado = grados * 9/5 + 32
        elif toUnidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        self.temperatura.set(resultado)
    
    def star(self):
        self.mainloop()


    
if __name__ == "__main__":
    app = Ventana()
    app.star()        
        
