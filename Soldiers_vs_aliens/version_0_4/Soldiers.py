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

        self._speed = Configurations.get_soldier_speed()
        self._rect_y = float(self.rect.y)


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        param screen: Pantalla en donde se dibuja
        """
        screen.blit(self.image, self.rect)

    def update_position(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para actualizar la posición del soldado de acuerdo a las banderas de movimiento.
        :param screen: Pantalla en donde se verifican los límites.
        """
        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect = screen.get_rect()

        # Se verifican los estados de la bandera para modificar la posición.
        if self._is_moving_up:
            self._rect_y -= self._speed

        elif self._is_moving_down:
            self._rect_y += self._speed

        # Se verifica que el personaje no sobrepase los bordes de la pantalla.
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.y)

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.y = int(self._rect_y)

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