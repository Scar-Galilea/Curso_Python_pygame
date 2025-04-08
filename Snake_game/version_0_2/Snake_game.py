"""
Nombre: Galilea Peralta Contreras.
Fecha: 08 de abril del 2025.

Descripción:
"""

import pygame
from Configurations import Configurations

def run_game() -> None:
    """
    Función principal.
    """
    #Se inicializa el módulo de pygame.
    pygame.init()

    # Se inicializa la pantalla.
    #screen_size =(1288,720) # Resolución de la pantalla (ancho,alto).
    screen = pygame.display.set_mode(Configurations.get_creen_size())

    #Se configura el título del juego.
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())

    # Ciclo principal del videojuego.
    game_over = False

    while not game_over:
        # Se verifican los eventos (teclado y ratón) del juego.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        # Se dibujan los elementos gráficos en la pantalla.
        #background = (227,0,82) # Fondo de la pantalla en formato RGB.
        screen.fill(Configurations.get_background())

        #Se actualiza la pantalla.
        pygame.display.flip()
    pygame.quit()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    run_game()