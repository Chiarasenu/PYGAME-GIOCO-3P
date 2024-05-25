import pygame
from pygame.math import Vector2
from random import randint
import gioco_snake

mela = pygame.image.load("Gioco/Immagini/Frutta/mela.png")

class Frutta:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * gioco_snake.lato_celle),int(self.pos.y * gioco_snake.lato_celle),gioco_snake.lato_celle, gioco_snake.lato_celle)
        gioco_snake.screen.blit(mela,fruit_rect)
        pygame.draw.rect(gioco_snake.screen,(126,166,114),fruit_rect)

    def randomize(self):
        self.x = randint(0, gioco_snake.numero_celle - 1)
        self.y = randint(0, gioco_snake.numero_celle - 1)
        self.pos = Vector2(self.x,self.y)