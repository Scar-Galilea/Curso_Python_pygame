"""
Nombre: Galilea Peralta Contreras.
Fecha: 08 de abril del 2025.

Descripción:
Se agregó la clase Configurations en el m
"""

import pygame
from Configurations import Configurations
from  Game_functionalities import game_event, screen_refresh

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
        game_over = game_event()

        #Elementos de la pantalla
        screen_refresh(screen)
    # Se cierran los recursos de pygame
    pygame.quit()


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    run_game()