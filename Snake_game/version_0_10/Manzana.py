import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import randint

class Apple(Sprite):
    #Atributo de clase para la puntuación.
    _no_apples = 0
    def __init__(self):
        super().__init__()

        Apple._no_apples += 1

        #self.image = pygame.Surface((Configurations.get_apple_size(),Configurations.get_apple_size()))
        #self.image.fill(Configurations.get_apple_color())
        self._apple_frames = []
        apple_block_size = Configurations.get_apple_size()

        for i in range(len(Configurations.get_image_apple_path())):
            frame = pygame.image.load(Configurations.get_image_apple_path()[i])
            frame = pygame.transform.scale(frame,(apple_block_size,apple_block_size))
            self._apple_frames.append(frame)

        #self.image = pygame.image.load(Configurations.get_background_image_apple())
        #apple_block_size = Configurations.get_apple_size()
        #self.image = pygame.transform.scale(self.image,(apple_block_size,apple_block_size))
        self._last_update_time = pygame.time.get_ticks()

        self._frame_index = 0

        self.image = self._apple_frames[self._frame_index]
        self._frame_index = 1
        
        self.rect = self.image.get_rect()

    def blit(self,screen: pygame.surface.Surface)-> None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibuja.
        """
        screen.blit(self.image,self.rect)




    def random_position(self, snake_body: pygame.sprite.Group)-> None:
        """
        Se utiliza para
        """
        repeat = True
        while repeat:
            #Se genera la poosicion aleatoria
            screen_width = Configurations.get_screen_size()[0]
            screen_height = Configurations.get_screen_size()[1]
            apple_block_size = Configurations.get_apple_size()

            self.rect.x = apple_block_size * randint(0, (screen_width // apple_block_size - 1))
            self.rect.y = apple_block_size * randint(0, (screen_height // apple_block_size - 1))

            #Se verifica que no se encunetre en el cuerpo de serpiente.
            for snake_block in snake_body.sprites():
                if self.rect == snake_block.rect:
                    repeat = True
                    break
                else:
                    repeat = False

    def animate_time(self)->None:
        current_time = pygame.time.get_ticks()
        time_to_refresh = 200

        needs_refresh = (current_time - self._last_update_time) >= time_to_refresh

        if needs_refresh:
            self.image = self._apple_frames[self._frame_index]

            self._last_update_time = current_time
            self._frame_index += 1

            if self._frame_index >= len(self._apple_frames):
                self._frame_index = 0


    @classmethod
    def get_no_apples(cls) -> int:
        """
        """
        return cls._no_apples

