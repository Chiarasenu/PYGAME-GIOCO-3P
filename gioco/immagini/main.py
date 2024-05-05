import pygame, sys
from pygame.locals import *


#schermo

WINDOW_SIZE = (1000, 650)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('gioco')
screen.fill((2, 247, 178))
schermo = pygame.Surface((1000, 650))
schermo.fill((2, 0, 178))
sfondo = pygame.image.load('gioco/immagini/menu_background.png')
# sfondo = pygame.transform.scale(sfondo, (1000, 650))

running = True
clock = pygame.time.Clock()
fps = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN: 
            run = True   
    pygame.display.update()
    clock.tick(fps)
pygame.quit() 

#eventuali personaggi

  


