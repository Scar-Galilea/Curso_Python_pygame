"""
Nombre: Galilea Peralta Contreras.
Fecha: 09 de abril del 2025.

Descripción:
"""
import  pygame
from Configurations import Configurations
from Media import Background
from Soldiers import Soldiers

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

def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background, soldiers) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    #Dibujamos la imagen de fondo en la pantalla.
    background.blit(screen)
    soldiers.blit(screen)
    pygame.display.flip()  #Actualizamos el contenido de la ventana.

    clock.tick(Configurations.get_fps())

    soldiers.blit(screen)


