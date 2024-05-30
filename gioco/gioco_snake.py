# IMPORTAZIONI -------------------------------------------------------------------------------------- #

import pygame
from pygame.locals import *
from sys import exit
from pygame import Vector2
from snake_blu import Snake_Blu
from snake_rosso import Snake_Rosso
from bottone import Bottone
from frutta import Frutta
from random import randint

# INIZIALIZZAZIONE ---------------------------------------------------------------------------------- #

pygame.init()
clock = pygame.time.Clock()
FPS = 60

# SCHERMO ------------------------------------------------------------------------------------------- #
numero_celle = 30
lato_celle = 40

SCREEN_WIDTH = numero_celle * lato_celle
SCREEN_HEIGHT = numero_celle * lato_celle / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

sfondo_menu = pygame.image.load("gioco/immagini/snake_principale.png")
sfondo_menu = pygame.transform.scale(sfondo_menu, (1200, 600))
AZZURRO = (54, 204, 227)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# SUONI --------------------------------------------------------------------------------------------- #
suono_mangia = pygame.mixer.Sound("Gioco/MusicaSuoni/crunch.wav")
musica = pygame.mixer.Sound("Gioco/MusicaSuoni/pixelated-dreams-206019.mp3")

# BOTTONI ------------------------------------------------------------------------------------------- #
bottone_play = Bottone(screen,
                        [350, 400],  # pos
                        [500, 100],  # size
                        "gioca")

bottone_reset = Bottone(screen,
                        [100, 400],  # pos
                        [450, 100],  # size
                        "reset")

bottone_quit = Bottone(screen,
                        [650, 400],  # pos
                        [450, 100],  # size
                        "quit")

# ASSEGNAZIONI CLASSI ------------------------------------------------------------------------------- #
snake_blu = Snake_Blu()
snake_rosso = Snake_Rosso()
frutta = Frutta()

# FUNZIONI ------------------------------------------------------------------------------------------ #
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
        snake_blu.aggiungi_blocco()
        suono_mangia.play()

    for blocco in snake_blu.corpo[1:]:
        if blocco == frutta.pos:
            frutta.randomizza()

def update():
    snake_blu.muovi_snake()
    controllo_collisioni()

def reset_game():
    global snake_blu, frutta
    snake_blu = Snake_Blu()
    frutta = Frutta()

# FUNZIONI DEL GIOCO -------------------------------------------------------------------------------- #


def singleplayer():
    reset_game()
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

        if not 0 <= snake_blu.corpo[0].x < numero_celle or not 0 <= snake_blu.corpo[0].y < numero_celle / 2:
            game_over()
        for blocco in snake_blu.corpo[1:]:
            if blocco == snake_blu.corpo[0]:
                game_over()

        musica.play(-1)
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
                pos = pygame.mouse.get_pos()
                if bottone_reset.rect.collidepoint(pos):
                    bottone_reset.toggle()
                    singleplayer()
                elif bottone_quit.rect.collidepoint(pos):
                    bottone_quit.toggle()
                    pygame.quit()
                    exit()

        # cambio colore se passo sopra i tasti reset e quit
        pos = pygame.mouse.get_pos()
        if bottone_reset.rect.collidepoint(pos):
            bottone_reset.chiaro()
        else:
            bottone_reset.base()

        pos = pygame.mouse.get_pos() 
        if bottone_quit.rect.collidepoint(pos):
            bottone_quit.chiaro()
        else:
            bottone_quit.base()

        bottone_reset.draw()
        bottone_quit.draw()
        musica.play(-1)
        pygame.display.update()
        clock.tick(FPS)

def menu():
    pygame.display.set_caption("MENÙ")
    while True:
        screen.blit(sfondo_menu, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bottone_play.rect.collidepoint(pos):
                    bottone_play.toggle()
                    singleplayer()

        # Cambio colore se passo sopra il tasto singleplayer
        pos = pygame.mouse.get_pos()
        if bottone_play.rect.collidepoint(pos):
            bottone_play.chiaro()
        else:
            bottone_play.base()

        bottone_play.draw()
        pygame.display.update()
        clock.tick(FPS)

menu()
