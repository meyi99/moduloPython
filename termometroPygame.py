'''
Created on 7 abr. 2019

@author: meyi
'''
import pygame, sys
from pygame.constants import KEYDOWN, K_BACKSPACE, MOUSEBUTTONDOWN

class Termometro():
    '''
    Atributos
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.shape = pygame.image.load("/home/meyi/Imágenes/Wallpapers/termometro1.png")
        
    def convertir(self, grados, unidad):
        resultado = 0
        if unidad == "F":
            resultado = grados * 9/5 + 32
        elif unidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        return resultado

class Selector():
    '''
    Atributos
    '''
    __tipoUnidad = None
    
    def __init__(self, unidad="C"):
        '''
        Constructor
        '''
        self.__shape = []
        self.__shape.append(pygame.image.load("/home/meyi/Imágenes/Wallpapers/farenheit.png"))
        self.__shape.append(pygame.image.load("/home/meyi/Imágenes/Wallpapers/celsius.png"))
        self.__tipoUnidad = unidad
        
    def shape(self):
        '''
        Método getter para shape
        '''
        if self.__tipoUnidad == "F":
            return self.__shape[0]
        else:
            return self.__shape[1]
        
    def change(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.__tipoUnidad == "F":
                self.__tipoUnidad = "C"
            else:
                self.__tipoUnidad = "F"
                
    def unidad(self):
        '''
        Método getter para __tipoUnidad
        '''
        return self.__tipoUnidad 
        
class NumberInput():
    '''
    Atributos
    '''
    __value = 0
    __strValue = "0"
    __position = [0, 0]
    __size = [0, 0]
    
    def __init__(self, value=0):
        '''
        Constructor
        '''
        self.__font = pygame.font.SysFont("Arial", 24)
        self.value(value)
    
    def onEvent(self, event):
            if event.type == KEYDOWN:
                if event.unicode.isdigit() and len(self.__strValue) < 10:
                    self.__strValue += event.unicode
                    self.value(self.__strValue)
                elif event.key == K_BACKSPACE:
                    self.__strValue = self.__strValue[:-1]
                    self.value(self.__strValue)
    
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (236, 233, 233))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock)

    def value(self, val=None):
        '''
        Método getter y setter para __value
        '''
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
                self.__strValue = val
            except:
                pass
            
    def width(self, val=None):
        '''
        Método getter y setter para __size "ancho" 
        '''
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
            
    def height(self, val=None):
        '''
        Método getter y setter para __size "Alto"
        '''
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
    
    def size(self, val=None):
        '''
        Método getter y setter para __size
        '''
        if val == None:
            return self.__size
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass

    def coordX(self, val=None):
        '''
        Método getter y setter para __position "coordenada X" 
        '''
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
            
    def coordY(self, val=None):
        '''
        Método getter y setter para __position "coordenada Y"
        '''
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
    
    def position(self, val=None):
        '''
        Método getter y setter para __position
        '''
        if val == None:
            return self.__position
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass

class MainApp():
    '''
    Atributos
    '''
    termometro = None
    entrada = None
    selector = None

    def __init__(self):
        '''
        Constructor
        '''
        self.__screen = pygame.display.set_mode((315, 315))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((255, 255, 255))
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.position((140, 58))
        self.entrada.size((133, 28))
        self.selector = Selector()
        
    def __close(self):
        '''
        Método que cierra la app
        '''
        pygame.quit()
        sys.exit()
        
    def star(self):
        '''
        Método que inicia la app
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__close()
                
                self.entrada.onEvent(event)
                if event.type == MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
                    
                    
            self.__screen.blit(self.termometro.shape, (0, 50))
            text = self.entrada.render()
            pygame.draw.rect(self.__screen, (1, 0, 0), text[0])
            self.__screen.blit(text[1], self.entrada.position())
            self.__screen.blit(self.selector.shape(), (115, 105))
            # Actualizar pantalla
            pygame.display.flip()
            
if __name__ == "__main__":
    pygame.init()
    app = MainApp()
    app.star()
            
            
            
            
            
            
            
            
            
            