import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import randint, choice


class SnakeBlock(Sprite):
    # Atributos de clase banderas e movimiento de la serpiente
    _is_moving_right = False
    _is_moving_left = False
    _is_moving_up = False
    _is_moving_down = False

    def __init__(self, is_head: bool = False):
        """
        Constructor de la clase
        """
        super().__init__()

        if is_head:
            #color = Configurations.get_snake_head_color()
            self.image = pygame.image.load(Configurations.get_background_image_head())
        else:
            #color  = Configurations.get_snake_body_color()
            path = choice(Configurations.get_body_images_path())
            self.image = pygame.image.load(path)

        snake_block_size = Configurations.get_snake_block_size()
        #self.image = pygame.Surface((snake_block_size, snake_block_size))
        #self.image.fill(color)
        self.image = pygame.transform.scale(self.image,(snake_block_size,snake_block_size))

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        param screen: Pantalla en dnde se dibuja
        """
        angle = 0
        if SnakeBlock.get_is_moving_up():
            angle = 90

        elif SnakeBlock.get_is_moving_left():
            angle = 180

        elif SnakeBlock.get_is_moving_down():
            angle = 270
        image_flip = pygame.transform.rotate(self.image,angle)
        screen.blit(image_flip, self.rect)

    def snake_head_init(self) -> None:
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        snake_block_size = Configurations.get_snake_block_size()

        self.rect.x = snake_block_size * randint(0,(screen_width // snake_block_size -1))
        self.rect.y = snake_block_size * randint(0,(screen_height // snake_block_size -1))


    @classmethod
    def get_is_moving_right(cls) -> bool:
        """
        Getter para la bandera get_is_moving_right(cls) -> bool:
        :param cls:
        :return:
        """
        return cls._is_moving_right

    @classmethod
    def set_is_moving_right(cls, value: bool) -> None:
        """
        Setter para la bandera de is_moving_right(cls) -> bool:
        :return:
        """
        cls._is_moving_right = value

        # ---------------------------------

    @classmethod
    def get_is_moving_left(cls) -> bool:
        """
        Getter para la bandera get_is_moving_right(cls) -> bool:
        :param cls:
        :return:
        """
        return cls._is_moving_left

    @classmethod
    def set_is_moving_left(cls, value: bool) -> None:
        """
        Setter para la bandera de is_moving_right(cls) -> bool:
        :return:
        """
        cls._is_moving_left = value

    # -------------------

    @classmethod
    def get_is_moving_up(cls) -> bool:
        """
        Getter para la bandera get_is_moving_right(cls) -> bool:
        :param cls:
        :return:
        """
        return cls._is_moving_up

    @classmethod
    def set_is_moving_up(cls, value: bool) -> None:
        """
        Setter para la bandera de is_moving_right(cls) -> bool:
        :return:
        """
        cls._is_moving_up = value

    @classmethod
    def get_is_moving_down(cls) -> bool:
        """
        Getter para la bandera get_is_moving_right(cls) -> bool:
        :param cls:
        :return:
        """
        return cls._is_moving_down

    @classmethod
    def set_is_moving_down(cls, value: bool) -> None:
        """
        Setter para la bandera de is_moving_right(cls) -> bool:
        """
        cls._is_moving_down = value