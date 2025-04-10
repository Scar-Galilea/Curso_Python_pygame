from symtable import Class

import  pygame
from pygame.sprite import Sprite
from Configurations import Configurations

class SnakeBlock(Sprite):

    def __init__  (self):
        """
        Constructor de clase
        """
        super().__init__()
        if is_head:
            color = Configurations
        else:
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

    def snake_head_init(self)-> None:
        screen_width = Configurations.get_creen_size()[0]
        screen_height = Configurations.get_creen_size()[1]
        snake_block_size = Configurations.get_snake_block_size()
