"""
Nombre: Galilea Peralta Contreras.
Fecha: 09 de abril del 2025.

Descripción:
"""
import  pygame
from Configurations import Configurations
from Snake import SnakeBlock

def game_event() -> bool:
    #Se declara la bandera del fin del juego.
    game_over = False

    #Se verifican los eventos (teclado y ratón)
    for event in pygame.event.get():
        #Un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True
    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface, snake_head: SnakeBlock) -> None:
    # Se dibujan los elementos gráficos en la pantalla.
    # background = (227,0,82) # Fondo de la pantalla en formato RGB.
    screen.fill(Configurations.get_background())

    #Cabeza de serpiente
    snake_head.blit(screen)

    # Se actualiza la pantalla.
    pygame.display.flip()





