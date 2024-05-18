import pygame
from math import Vector2

class Snake:
    def __init__(self) -> None:
        self.corpo = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direzione = Vector2(0,0)
        self.nuovo_corpo = False

        # IMMAGINI
            # Testa
        self.testaN = pygame.image.load

# Serve:
# - Coda, Corpo e Testa
# - Movimento
# - Mangiare (collisione con frutto)
# - Allungamento dopo Mangiare
# - Morte (collisione con se stesso o muro)
