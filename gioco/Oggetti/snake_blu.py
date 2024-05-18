import pygame
from math import Vector2

class Snake_Blu:
    def __init__(self) -> None:
        self.corpo = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direzione = Vector2(0,0)
        self.nuovo_corpo = False

        # IMMAGINI BLU
            # Testa
        self.testaN = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_testaN.png')

# Serve:
# - Coda, Corpo e Testa
# - Movimento
# - Mangiare (collisione con frutto)
# - Allungamento dopo Mangiare
# - Morte (collisione con se stesso o muro)
