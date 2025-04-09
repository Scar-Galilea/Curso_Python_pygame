from symtable import Class

import  pygame
from pygame.sprite import Sprite

class SnakeBlock(Sprite):

    def __init__  (self):
        """
        Constructor de clase
        """
        super().__init__()
        color = (87, 35, 100)

        self.image = pygame.Surface((40,40))
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def blit(self,screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar e bloque de la serpiente.
        :param screen: Pantalla en donde se dibuja.
        """
        screen.blit(self.image, self.rect)