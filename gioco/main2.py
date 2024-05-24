# #Serve
# - Menu che spieghi la diversa frutta
# - Modalita Singleplayer e Multiplayer
# - Due modalita, normale (solo mela) e Tuttifrutti (tutti i frutti)

import pygame
import math
from Oggetti import snake_blu
from Oggetti import snake_rosso
from bottone import Bottone
from Oggetti import frutta
from random import randint

from enum import Enum
 
class enum_frutta(Enum):
    MELA = 'Gioco/Immagini/Frutta/mela.png'
    CILIEGIA = 'Gioco/Immagini/Frutta/mela.png'
    LIMONE = 'Gioco/Immagini/Frutta/mela.png'
    ANGURIA = 'Gioco/Immagini/Frutta/mela.png'

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

ogg_frutta = frutta(screen, [randint(0, numero_celle -1), randint(0, numero_celle -1)], lato_celle, enum_frutta.MELA.name, enum_frutta.MELA.value)

# menù
# due surface o una 



def menu():
    pygame.display.set_caption("MENÙ")
    while True:
        screen.blit(117, 212, 93)
        KEYDOWN_POS = pygame.KEYDOWN()
        

# game loop
run = True
while run:
    
    clock.tick(FPS)
    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        ogg_frutta.x -= 5
    if key[pygame.K_d] == True:
        ogg_frutta.x += 5
    if key[pygame.K_w] == True:
        ogg_frutta.y -= 5
    if key[pygame.K_s] == True:
        ogg_frutta.y += 5
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(sfondo, (0,0))
    screen.blit(ogg_frutta.get_image(), ogg_frutta)

    
            
    pygame.display.update()
    
pygame.quit() 



