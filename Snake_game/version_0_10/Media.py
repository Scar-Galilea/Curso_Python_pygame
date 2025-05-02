import pygame
from  Configurations import Configurations

class Background:
    """
    Clase que contien el fonfo d epanatalla.
    """

    def __init__(self):
        backgrounds_image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(backgrounds_image_path)

        #Tamaño de la pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)
        self.rect = self.image.get_rect()



    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)