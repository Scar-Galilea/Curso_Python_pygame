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

        self._is_moving_up = False
        self._is_moving_down = False


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        param screen: Pantalla en donde se dibuja
        """
        screen.blit(self.image, self.rect)

    def update_positions(self) -> None:
        if self.is_moving_up:
            self.rect.y -= 10
        if self.is_moving_down:
            self.rect.y += 10

    @property
    def is_moving_up(self) -> bool:
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self, value: bool) -> None:
        self._is_moving_up = value

    @property
    def is_moving_down(self) -> bool:
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self, value: bool) -> None:
        self._is_moving_down = value