import pygame
from pygame.locals import *
from sys import exit
from pygame import Vector2
from snake_blu import Snake_Blu
from snake_rosso import Snake_Rosso
from bottone import Bottone
from frutta2 import Frutta
from random import randint
from classe_main import c_MAIN

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
schermo_gioco = pygame.image.load("gioco/Immagini/sfondo1.png")
schermo_gioco = pygame.transform.scale(schermo_gioco, (1200, 600))

AZZURRO = (54, 204, 227)

<<<<<<< HEAD
=======


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# ogg_frutta = frutta(screen, [randint(0, numero_celle -1), 
#  randint(0, numero_celle -1)], lato_celle, enum_frutta.MELA.name,
#  enum_frutta.MELA.value)

>>>>>>> 71184b6 (.)
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

<<<<<<< HEAD
=======
#snake rosso
snake_r = Snake_Rosso()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------


>>>>>>> 71184b6 (.)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

snake = Snake_Blu()
frutta = Frutta()

def draw_erba():
    grass_color = (167,209,61)
    for riga in range(numero_celle):
        if riga % 2 == 0: 
            for col in range(numero_celle):
                if col % 2 == 0:
                    grass_rect = pygame.Rect(col * lato_celle,riga * lato_celle, lato_celle, lato_celle)
                    pygame.draw.rect(screen,grass_color,grass_rect)
        else:
            for col in range(numero_celle):
                if col % 2 != 0:
                    grass_rect = pygame.Rect(col * lato_celle,riga * lato_celle, lato_celle, lato_celle)
                    pygame.draw.rect(screen,grass_color,grass_rect)			

def draw():
    draw_erba()
    frutta.draw_frutta()
    snake.draw_snake(lato_celle, screen)

def controllo_collisioni():
    if frutta.pos == snake.corpo[0]:
        frutta.randomizza()
        snake.aggiugi_blocco()

    for blocco in snake.corpo[1:]:
        if blocco == frutta.pos:
            frutta.randomizza()

def update():
    snake.muovi_snake()
    controllo_collisioni()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def singleplayer():  
    while True:
        pygame.display.set_caption("Singleplayer")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == SCREEN_UPDATE:
                update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snake.direzione.y != 1:
                    snake.direzione = Vector2(0, -1)
                if event.key == pygame.K_d and snake.direzione.x != -1:
                    snake.direzione = Vector2(1, 0)
                if event.key == pygame.K_s and snake.direzione.y != -1:
                    snake.direzione = Vector2(0, 1)
                if event.key == pygame.K_a and snake.direzione.x != 1:
                    snake.direzione = Vector2(-1, 0)

        screen.fill((175,215,70))
        draw()
        pygame.display.update()
        clock.tick(60)

<<<<<<< HEAD

        screen.fill((175,215,70))
        draw()
        pygame.display.update()
        clock.tick(60)
=======
singleplayer()
>>>>>>> 71184b6 (.)
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def multiplayer():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
                
        pygame.display.update()
        clock.tick(FPS)
        
        
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------


    
def menu():
    pygame.display.set_caption("MENÙ")
    while True:
        screen.fill(AZZURRO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bottone_single.rect.collidepoint(pos):
                    bottone_single.toggle()
                    screen.blit(schermo_gioco, (0,0))
                    singleplayer()
                    
                elif bottone_multi.rect.collidepoint(pos):
                    bottone_multi.toggle()
                    screen.blit(schermo_gioco, (0,0))
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
        
        
        
        

<<<<<<< HEAD
menu()
singleplayer()
=======
menu()
>>>>>>> 71184b6 (.)
