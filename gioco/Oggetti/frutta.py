import pygame
from pygame.math import Vector2
from random import randint


class Frutta:
    def __init__(self, screen, pos, lato_celle, tipo, image) -> None:
        # self.x = randint(0, numero_celle -1)
        # self.y = randint(0, numero_celle -1)
        self.pos = pos
        self.lato_celle = lato_celle
        self.tipo = tipo

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.lato_celle)
        self.rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())

    def get_image(self):
        return self.image
    
    def draw(self, lato_celle, screen):
        self.display.blit(self.image, (self.rect.x, self.rect.y))



# Serve 
# 1. la randomizzazione della posizione
# 2. il rect
# 3. la frutta diversa (non so se dobbiamo modificare 
#    la classe direttamnete anche se dubito, perche diversi poteri), 
#    (mela, mirtilli, banana, pera...)
# 4. Disegnare il frutto