"""
Nombre: Galilea Peralta Contreras.
Fecha: 09 de abril del 2025.

Descripción:
"""

import  pygame
from Configurations import Configurations
from Media import Background
from Soldiers import Soldiers

def game_event(soldiers: Soldiers) -> bool:
    #Se declara la bandera del fin del juego.
    game_over = False

    #Se verifican los eventos (teclado y ratón)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                soldiers.is_moving_up = True
            if event.key == pygame.K_DOWN:
                soldiers.is_moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                soldiers.is_moving_up = False
            if event.key == pygame.K_DOWN:
                soldiers.is_moving_down = False

        #Un clic en cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True
    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background, soldiers,shot) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    #Dibujamos la imagen de fondo en la pantalla.
    background.blit(screen)
    soldiers.update_position(screen)

    soldiers.update_animation()
    soldiers.blit(screen)

    shot.blit(screen)
    shot.update_animation()

    pygame.display.flip()  #Actualizamos el contenido de la ventana.



    clock.tick(Configurations.get_fps())

    soldiers.blit(screen)


