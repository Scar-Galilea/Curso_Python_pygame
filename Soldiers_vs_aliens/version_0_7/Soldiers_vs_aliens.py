"""
Nombre: Galilea Peralta Contreras.
Fecha: 08 de abril del 2025.

Descripción:
Se agregó la clase Configurations en el m
"""
from email.headerregistry import Group

import  pygame

from Configurations import Configurations
from Game_functionalities import game_event, screen_refresh
from Media import Background
from Soldiers import Soldiers
from pygame.sprite import Group

def run_game() -> None:
    """
    Función principal.
    """
    #Se inicializa el módulo de pygame.
    pygame.init()

    clock = pygame.time.Clock()

    # Se inicializa la pantalla.
    #screen_size =(1288,720) # Resolución de la pantalla (ancho,alto).
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    #Se configura el título del juego.
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())

    # Ciclo principal del videojuego.
    game_over = False

    background = Background()
    soldiers = Soldiers(screen)

    shot = Group()

    while not game_over:
        game_over = game_event(soldiers,shot)  # Verificamos si se debe cerrar el juego.
        screen_refresh(screen, clock, background,soldiers, shot)  # Actualizamos la pantalla en cada iteración.

    pygame.quit()


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    run_game()