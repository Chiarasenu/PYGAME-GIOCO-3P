#Serve
- Menu che spieghi la diversa frutta
- Modalita Singleplayer e Multiplayer
- Due modalita, normale (solo mela) e Tuttifrutti (tutti i frutti)

import pygame
import math

pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

#schermo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Gioco')

# immmagine
sfondo = pygame.image.load('gioco/sfondo1.png')
sfondo = pygame.transform.scale(sfondo, (1600, 800))
sfondo_width = sfondo.get_width()
sfondo_rect = sfondo.get_rect()
ogg = pygame.image.load("gioco/mela.png").convert_alpha()
ogg = pygame.transform.scale(ogg, (32, 32))
ogg_rect = ogg.get_rect()

numero_celle = 20
lato_celle = 40


# game loop
run = True
while run:
    
    clock.tick(FPS)
    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        ogg_rect.x -= 5
    if key[pygame.K_d] == True:
        ogg_rect.x += 5
    if key[pygame.K_w] == True:
        ogg_rect.y -= 5
    if key[pygame.K_s] == True:
        ogg_rect.y += 5
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(sfondo, (0,0))
    pygame.draw.rect(screen, (255,0,255), ogg_rect)
    screen.blit(ogg, ogg_rect)

    
            
    pygame.display.update()
    
pygame.quit() 



