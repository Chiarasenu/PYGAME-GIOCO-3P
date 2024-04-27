import pygame, sys
from pygame.locals import *


#schermo

window = (1000, 650)
screen = pygame.display.set_mode(window)
pygame.display.set_caption('gioco')
screen.fill((2, 247, 178))

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN: 
            run = True

        
    pygame.display.update()
    
pygame.quit()            
    