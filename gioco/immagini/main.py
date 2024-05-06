import pygame
import math

pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 375

#schermo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('gioco')

# immmagine
sfondo = pygame.image.load('gioco/immagini/sfondo.png').convert()
sfondo_width = sfondo.get_width()
sfondo_rect = sfondo.get_rect()

# variabili
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / sfondo_width) + 1

# game loop
run = True
while run:
    
    clock.tick(FPS)

    for  i in range(0, tiles):
        screen.blit(sfondo, (i * sfondo_width + scroll,0))
        sfondo_rect.x = i * sfondo_width + scroll
        # pygame.draw.rect(screen, (0, 255, 0), sfondo_rect, 1)
    
    scroll -= 5
    
    if abs(scroll) > sfondo_width:
        scroll = 0
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    
pygame.quit() 

  


