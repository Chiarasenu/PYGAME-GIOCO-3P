# #Serve
# - Menu che spieghi la diversa frutta
# - Modalita Singleplayer e Multiplayer
# - Due modalita, normale (solo mela) e Tuttifrutti (tutti i frutti)

import pygame
from sys import exit
import math
from Oggetti import snake_blu
from Oggetti import snake_rosso
from bottone2 import Bottone
from Oggetti import frutta
from random import randint

# from enum import Enum
 
# class enum_frutta(Enum):
#     MELA = 'Gioco/Immagini/Frutta/mela.png'
#     CILIEGIA = 'Gioco/Immagini/Frutta/mela.png'
#     LIMONE = 'Gioco/Immagini/Frutta/mela.png'
#     ANGURIA = 'Gioco/Immagini/Frutta/mela.png'

pygame.init()
clock = pygame.time.Clock()
FPS = 60

#schermo 
numero_celle = 30
lato_celle = 40

SCREEN_WIDTH = numero_celle * lato_celle
SCREEN_HEIGHT = numero_celle * lato_celle / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

# immmagine
sfondo = pygame.image.load('Gioco/Immagini/sfondo1.png')
sfondo = pygame.transform.scale(sfondo, (1600, 800))
sfondo_width = sfondo.get_width()
sfondo_rect = sfondo.get_rect()

# ogg_frutta = frutta(screen, [randint(0, numero_celle -1), randint(0, numero_celle -1)], lato_celle, enum_frutta.MELA.name, enum_frutta.MELA.value)

# menù
# due surface o una 

# bottone singleplayer
bottone_single = Bottone(screen,
                        [100, 300], # pos
                        [450, 100], # size
                        "Singleplayer")

# bottone multiplayer
bottone_multi = Bottone(screen,
                        [650, 300], # pos
                        [450, 100], # size
                        "Multiplayer")

# def menu():
#     pygame.display.set_caption("MENÙ")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    bottone_single.blit(screen)        
    pygame.display.update()
    clock.tick(FPS)
    
        

# game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
            
#     pygame.display.update()
#     clock.tick(FPS)
 



