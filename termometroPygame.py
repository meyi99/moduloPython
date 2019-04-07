'''
Created on 7 abr. 2019

@author: meyi
'''
import pygame, sys

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
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244, 236, 203))
        
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
            
            # Actualizar pantalla
            pygame.display.flip()
            
if __name__ == "__main__":
    pygame.init()
    app = MainApp()
    app.star()
            
            
            
            
            
            
            
            
            
            