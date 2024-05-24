import pygame
from pygame.math import Vector2
from random import randint

mela = pygame.image.load('Gioco\Immagini\Frutta\mela.png').convert_alpha()

class Mela:
    def __init__(self, numero_celle) -> None:
        self.x = randint(0, numero_celle -1)
        self.y = randint(0, numero_celle -1)
        self.pos = Vector2(self.x, self.y)

    def draw_mela(self, lato_celle, screen):
        mela_rect = pygame.Rect(int(self.pos.x * lato_celle), int(self.pos.y * lato_celle))
        screen.blit(mela, mela_rect)



# Serve 
# 1. la randomizzazione della posizione
# 2. il rect
# 3. la frutta diversa (non so se dobbiamo modificare 
#    la classe direttamnete anche se dubito, perche diversi poteri), 
#    (mela, mirtilli, banana, pera...)
# 4. Disegnare il frutto