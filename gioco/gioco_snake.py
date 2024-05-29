import pygame
from pygame.locals import *
from sys import exit
from pygame import Vector2
from snake_blu import Snake_Blu
from snake_rosso import Snake_Rosso
from bottone import Bottone
from frutta import Frutta
from random import randint

pygame.init()
clock = pygame.time.Clock()
FPS = 60

# schermo
numero_celle = 30
lato_celle = 40

SCREEN_WIDTH = numero_celle * lato_celle
SCREEN_HEIGHT = numero_celle * lato_celle / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')
schermo_gioco = pygame.image.load("gioco/Immagini/sfondo1.png")
schermo_gioco = pygame.transform.scale(schermo_gioco, (1200, 600))

sfondo_menu = pygame.image.load("gioco/immagini/snake_principale.png")
sfondo_menu = pygame.transform.scale(sfondo_menu, (1200, 600))
AZZURRO = (54, 204, 227)

# bottone singleplayer
bottone_play = Bottone(screen,
                         [350, 400],  # pos
                         [500, 100],  # size
                         "Gioca")

# bottone singleplayer
bottone_reset = Bottone(screen,
                         [350, 400],  # pos
                         [500, 100],  # size
                         "Reset")

# bottone multiplayer
# bottone_multi = Bottone(screen,
#                         [650, 300],  # pos
#                         [450, 100],  # size
#                         "Multiplayer")

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

snake_blu = Snake_Blu()
snake_rosso = Snake_Rosso()
frutta = Frutta()

def draw_erba():
    grass_color = (167, 209, 61)
    for riga in range(numero_celle):
        if riga % 2 == 0:
            for col in range(numero_celle):
                if col % 2 == 0:
                    grass_rect = pygame.Rect(col * lato_celle, riga * lato_celle, lato_celle, lato_celle)
                    pygame.draw.rect(screen, grass_color, grass_rect)
        else:
            for col in range(numero_celle):
                if col % 2 != 0:
                    grass_rect = pygame.Rect(col * lato_celle, riga * lato_celle, lato_celle, lato_celle)
                    pygame.draw.rect(screen, grass_color, grass_rect)

def draw():
    draw_erba()
    frutta.draw_frutta()
    snake_blu.draw_snake(lato_celle, screen)

def controllo_collisioni():
    if frutta.pos == snake_blu.corpo[0]:
        frutta.randomizza()
        snake_blu.aggiugi_blocco()

    for blocco in snake_blu.corpo[1:]:
        if blocco == frutta.pos:
            frutta.randomizza()

def update():
    snake_blu.muovi_snake()
    controllo_collisioni()

def singleplayer():
    while True:
        pygame.display.set_caption("Singleplayer")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == SCREEN_UPDATE:
                update()

        key = pygame.key.get_pressed()
        if key[K_w] and snake_blu.direzione != Vector2(0, 1):
            snake_blu.direzione = Vector2(0, -1)
        if key[K_d] and snake_blu.direzione != Vector2(-1, 0):
            snake_blu.direzione = Vector2(1, 0)
        if key[K_s] and snake_blu.direzione != Vector2(0, -1):
            snake_blu.direzione = Vector2(0, 1)
        if key[K_a] and snake_blu.direzione != Vector2(1, 0):
            snake_blu.direzione = Vector2(-1, 0)

        if not 0 <= snake_blu.corpo[0].x < numero_celle or not 0 <= snake_blu.corpo[0].y < numero_celle:
            game_over()
        for blocco in snake_blu.corpo[1:]:
            if blocco == snake_blu.corpo[0]:
                game_over()

        screen.fill((175, 215, 70))
        draw()
        pygame.display.update()
        clock.tick(FPS)

def game_over():
    pygame.display.set_caption("GAME OVER")
    while True:
        screen.blit(sfondo_menu, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bottone_reset.rect.collidepoint(pos):
                    bottone_reset.toggle()
                    screen.blit(schermo_gioco, (0, 0))

                    singleplayer()

        # cambio colore se passo sopra i tasti singleplayer e multiplayer
        pos = pygame.mouse.get_pos()
        if bottone_reset.rect.collidepoint(pos):
            bottone_reset.chiaro()
        else:
            bottone_reset.base()
        bottone_reset.draw()

        pygame.display.update()
        clock.tick(FPS)

def menu():
    pygame.display.set_caption("MENÙ")
    while True:
        screen.blit(sfondo_menu, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bottone_play.rect.collidepoint(pos):
                    bottone_play.toggle()
                    screen.blit(schermo_gioco, (0, 0))
                    singleplayer()


        # cambio colore se passo sopra i tasti singleplayer e multiplayer
        pos = pygame.mouse.get_pos()
        if bottone_play.rect.collidepoint(pos):
            bottone_play.chiaro()
        else:
            bottone_play.base()
        bottone_play.draw()

        # pos = pygame.mouse.get_pos()
        # if bottone_multi.rect.collidepoint(pos):
        #     bottone_multi.chiaro()
        # else:
        #     bottone_multi.base()
        # bottone_multi.draw()

        bottone_play.draw()
        # bottone_multi.draw()
        pygame.display.update()
        clock.tick(FPS)

menu()
