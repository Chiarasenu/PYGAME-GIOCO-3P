# #Serve
# - Menu che spieghi la diversa frutta
# - Modalita Singleplayer e Multiplayer
# - Due modalita, normale (solo mela) e Tuttifrutti (tutti i frutti)

import pygame
from pygame.locals import *
from sys import exit
import math
from snake_blu import Snake_Blu
from snake_rosso import Snake_Rosso
from bottone2 import Bottone
from frutta import Frutta
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

AZZURRO = (54, 204, 227)

# ogg_frutta = frutta(screen, [randint(0, numero_celle -1), 
#  randint(0, numero_celle -1)], lato_celle, enum_frutta.MELA.name,
#  enum_frutta.MELA.value)

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

# snake blu
snake_b = Snake_Blu()

#snake rosso
snake_r = Snake_Rosso()


def singleplayer():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
                
        pygame.display.update()
        clock.tick(FPS)
    

def multiplayer():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
                
        pygame.display.update()
        clock.tick(FPS)
    
def menu():
    pygame.display.set_caption("MENÙ")
    while True:
        screen.fill(AZZURRO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bottone_single.rect.collidepoint(event.pos):
                    bottone_single.toggle()
                    singleplayer()
                elif bottone_multi.rect.collidepoint(event.pos):
                    bottone_multi.toggle()
                    multiplayer()
        
        # cambio colore se passo sopra i tasti singleplayer e multiplayer
        pos = pygame.mouse.get_pos()
        if bottone_single.rect.collidepoint(pos):
            bottone_single.chiaro()
        else:
            bottone_single.base()
        bottone_single.draw()
        
        pos = pygame.mouse.get_pos()
        if bottone_multi.rect.collidepoint(pos):
            bottone_multi.chiaro()
        else:
            bottone_multi.base()
        bottone_multi.draw()
            

        bottone_single.draw()
        bottone_multi.draw()        
        pygame.display.update()
        clock.tick(FPS)
        
        

menu()