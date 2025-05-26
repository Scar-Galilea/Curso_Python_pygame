import pygame
from pygame.sprite import Sprite
from Configurations import Configurations


class Soldiers(Sprite):
    def __init__(self, screen: pygame.surface.Surface):
        """
        Constructor de la clase
        """
        super().__init__()

        self.image = pygame.image.load(Configurations.get_soldiers_image_path())
        snake_block_size = Configurations.get_snake_block_size()
        self.image = pygame.transform.scale(self.image, (snake_block_size, snake_block_size))
        self.rect = self.image.get_rect()

        screen_rect = screen.get_rect()
        self.rect.centery = screen_rect.centery
        self.rect.right = screen_rect.right


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        param screen: Pantalla en dnde se dibuja
        """
        screen.blit(self.image, self.rect)
