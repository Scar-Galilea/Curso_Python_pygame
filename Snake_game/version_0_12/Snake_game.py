"""
Nombre: Galilea Peralta Contreras.
Fecha: 08 de abril del 2025.

Descripción:
Versión 0.8
- Se agrega bloques al cuerpo de la serpiente
"""

import pygame
from Configurations import Configurations
from Game_functionalities import game_event, screen_refresh,snake_movement,check_collision,game_over_screen
from Snake import  SnakeBlock
from pygame.sprite import Group
from Manzana import Apple
from Media import Background,Audio,Scoreboard,GameOverImage

def run_game() -> None:
    """
    Función principal del videojuego
    """
    #Se inicializa el módulo pygame
    pygame.init()
    #Se configura el reloj de la serpiente
    clock = pygame.time.Clock()

    #Se inicializa la pantalla
    #screen_size = (1280, 720) #Resolución de la pantalla (ancho, alto)
    screen = pygame.display.set_mode(Configurations.get_screen_size() )

    #Se configura el título del juego
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())
    #Se crea el bloque inicial de la serpiente (cabeza)
    snake_head = SnakeBlock(is_head= True)
    snake_head.snake_head_init()

    #Se crea un grupo para almacenar el cuerpo de la serpiente
    snake_body = Group()
    snake_body.add(snake_head)

    # Se crea el grupo manzana.
    apple = Apple()
    apple.random_position(snake_body)

    apples = Group()
    apples.add(apple)

    background = Background()

    #Ciclo principal de videojuego
    game_over = False

    #Se reproduce la música y el sonido inicial.

    audio = Audio()
    audio.play_music(0.25)
    audio.play_star_sound()

    scoreboard = Scoreboard()

    gameOverImage = GameOverImage()

    while not game_over:
        game_over = game_event()
        screen_refresh(screen, clock, snake_body, apples,background,scoreboard)
        snake_movement(snake_body)
        if game_over:
            break

        game_over = check_collision(screen,snake_body,apples,audio,scoreboard)
        if game_over:
            gameOverImage.blit(screen)
            pygame.display.flip()
            game_over_screen(audio)
    #Se cierran los eventos
    pygame.quit()

if __name__ == '__main__':
    run_game()