import pygame
from pygame.math import Vector2
from random import randint

lato_celle = 40
numero_celle = 30

SCREEN_WIDTH = numero_celle * lato_celle
SCREEN_HEIGHT = numero_celle * lato_celle / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Frutta:
    def __init__(self):
        self.randomizza()
        immagine_mela = pygame.image.load("Gioco/Immagini/Frutta/mela.png").convert_alpha()
        size_mela = (40, 40)
        self.mela = pygame.transform.scale(immagine_mela, size_mela)


    def draw_frutta(self):
        fruit_rect = pygame.Rect(int(self.pos.x * lato_celle),int(self.pos.y * lato_celle), lato_celle, lato_celle)
        screen.blit(self.mela,fruit_rect)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomizza(self):
        self.x = randint(0, numero_celle - 1)
        self.y = randint(0, int(numero_celle /2) - 1)
        self.pos = Vector2(self.x,self.y)