'''
Created on 1 abr. 2019

@author: meyi
'''

class Termometro():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__unidadM = "C"
        self.__temperatura = 0
        
    def __conversor(self, temperatura, unidad):
        if unidad == "C":
            return "{} °F".format(temperatura * 9/5 + 32)
        elif unidad == "F":
            return "{} °C".format((temperatura - 32) * 5/9)
        else:
            return "Dato incorrecto"
        
    def __str__(self):
        return "{} °{}".format(self.__temperatura, self.__unidadM)
        
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == "F" or uniM == "C":
                self.__unidadMedida = uniM
            
    def temp(self, temperatura=None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self, uniM=None):
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            if uniM == "F" or uniM == "C":
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()

t = Termometro()
t.temp(32)
t.unidadMedida("F")
print(t.mide("C"))




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            