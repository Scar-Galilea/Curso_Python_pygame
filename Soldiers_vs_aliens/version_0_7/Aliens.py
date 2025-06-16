import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import choice

class Aliens(Sprite):

    def __init__(self,screen: pygame.surface.Surface):
        """
        Constructor de la clase
        """
        super().__init__()

        # Lista que almacena los frames del soldado.
        self._frames = []

        # Banderas de movimiento.

        movement = [True,False]
        self._is_moving_up = choice(movement)
        self._is_moving_down = not self._is_moving_up

        self.speed_aliens_x = Configurations.get_speed_aliens_x()
        self.speed_aliens_y = Configurations.get_speed_aliens_y()

        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = choice(Configurations.get_aliens_sheet_path())
        aliens_sheet = pygame.image.load(sheet_path)

        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = aliens_sheet.get_width()
        sheet_height = aliens_sheet.get_height()
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height


        # Se obtiene el tamaño para escalar cada frame.
        soldier_frame_size = Configurations.get_aliens_size()

        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * soldier_frame_width
            y = 0
            subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
            frame = aliens_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, soldier_frame_size)

            self._frames.append(frame)


        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()    # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0                               # Índice de la lista.

        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        screen_rect = screen.get_rect()
        self.rect.centery = screen_rect.centery

        self._rect_y = float(self.rect.y)
        self._speed_x = Configurations.get_speed_aliens_x()
        self._speed_y = Configurations.get_speed_aliens_y()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        param screen: Pantalla en donde se dibuja
        """
        screen.blit(self.image, self.rect)



    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._frames):
                self._frame_index = 0

    def update_position(self,screen):
        self.rect.right = self.rect.right + self.speed_aliens_x

        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect = screen.get_rect()

        # Se verifican los estados de la bandera para modificar la posición.
        if self._is_moving_up:
            self._rect_y -= self._speed_y

        elif self._is_moving_down:
            self._rect_y += self._speed_y

        # Se verifica que el personaje no sobrepase los bordes de la pantalla.
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.y)

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.y = int(self._rect_y)



