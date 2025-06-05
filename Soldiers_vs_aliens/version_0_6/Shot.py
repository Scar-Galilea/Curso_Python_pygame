import pygame
from pygame.sprite import Sprite
from Configurations import Configurations


class Shot(Sprite):

    def __init__(self, soldiers):

        """
        Constructor de la clase
        """
        super().__init__()

        # Lista que almacena los frames de los disparos.
        self._frames = []

        # Se carga la hoja que contiene los frames del disparo.
        sheet_path = Configurations.get_shop_sheet_path()
        shop_sheet = pygame.image.load(sheet_path)

        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_shot_row()
        sheet_width = shop_sheet.get_width()
        sheet_height = shop_sheet.get_height()
        shot_frame_width = sheet_width // sheet_frames_per_row
        shot_frame_height = sheet_height

        # Se obtiene el tamaño para escalar cada frame.
        shot_frame_size = Configurations.get_shop_size()

        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * shot_frame_width
            y = 0
            subsurface_rect = (x, y, shot_frame_width, shot_frame_height)
            frame = shop_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, shot_frame_size)

            self._frames.append(frame)

        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()  # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0  # Índice de la lista.

        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()

        screen_rect = soldiers.rect
        self.rect.right = screen_rect.right - 150
        self.rect.centery = screen_rect.centery - 10


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        param screen: Pantalla en donde se dibuja
        """

        screen.blit(self.image, self.rect)


    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del disparo, dando la impresión de animación.
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


    def update_position(self):
        self.rect.right = self.rect.right - 150
