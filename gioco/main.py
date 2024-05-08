import pygame
import math

pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000

#schermo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('gioco')

# immmagine
sfondo = pygame.image.load('gioco/immagini/sfondo.png')
sfondo = pygame.transform.scale(sfondo, (1600, 800))
sfondo_width = sfondo.get_width()
sfondo_rect = sfondo.get_rect()


# game loop
run = True
while run:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(sfondo, (0,0))
            
    pygame.display.update()
    
pygame.quit() 



