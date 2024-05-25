from snake_blu import Snake_Blu
from frutta2 import Frutta
import gioco_snake
import pygame

class Main:
    def __init__(self) -> None:
        self.snake = Snake_Blu()
        self.frutta = Frutta()
    
    def draw_erba(self):
        grass_color = (167,209,61)
        for riga in range(gioco_snake.numero_celle):
            if riga % 2 == 0: 
                for col in range(gioco_snake.numero_celle):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * gioco_snake.lato_celle,riga * gioco_snake.lato_celle, gioco_snake.lato_celle, gioco_snake.lato_celle)
                        pygame.draw.rect(gioco_snake.screen,grass_color,grass_rect)
            else:
                for col in range(gioco_snake.numero_celle):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * gioco_snake.lato_celle,riga * gioco_snake.lato_celle, gioco_snake.lato_celle, gioco_snake.lato_celle)
                        pygame.draw.rect(gioco_snake.screen,grass_color,grass_rect)			

    def draw(self):
        self.draw_erba()
        self.frutta.draw_frutta()
        self.snake.draw_snake()

    def controllo_collisioni(self):
        if self.frutta.pos == self.snake.corpo[0]:
            self.frutta.randomizza()
            self.snake.aggiugi_blocco()

        for blocco in self.snake.corpo[1:]:
            if blocco == self.frutta.pos:
                self.frutta.randomizza()

    def update(self):
        self.snake.muovi_snake()
        self.controllo_collisioni()
    
    
    
    





# # #Serve
# # - Menu che spieghi la diversa frutta
# # - Modalita Singleplayer e Multiplayer
# # - Due modalita, normale (solo mela) e Tuttifrutti (tutti i frutti)

# import pygame
# import math
# from gioco import snake_blu
# from gioco import snake_rosso


# pygame.init()
# clock = pygame.time.Clock()
# FPS = 60

# #schermo 
# numero_celle = 30
# lato_celle = 40

# SCREEN_WIDTH = numero_celle * lato_celle
# SCREEN_HEIGHT = numero_celle * lato_celle / 2

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Snake')

# # immmagine
# sfondo = pygame.image.load('Gioco/Immagini/sfondo1.png')
# sfondo = pygame.transform.scale(sfondo, (1600, 800))
# sfondo_width = sfondo.get_width()
# sfondo_rect = sfondo.get_rect()
# ogg = pygame.image.load("Gioco/Immagini/Frutta/mela.png").convert_alpha()
# ogg = pygame.transform.scale(ogg, (32, 32))
# ogg_rect = ogg.get_rect()

# # menù
# # due surface o una 



# def menu():
#     pygame.display.set_caption("MENÙ")
#     while True:
#         screen.blit(117, 212, 93)
#         KEYDOWN_POS = pygame.KEYDOWN()
        

# # game loop
# run = True
# while run:
    
#     clock.tick(FPS)
    
    
#     key = pygame.key.get_pressed()
#     if key[pygame.K_a] == True:
#         ogg_rect.x -= 5
#     if key[pygame.K_d] == True:
#         ogg_rect.x += 5
#     if key[pygame.K_w] == True:
#         ogg_rect.y -= 5
#     if key[pygame.K_s] == True:
#         ogg_rect.y += 5
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     screen.blit(sfondo, (0,0))
#     screen.blit(ogg, ogg_rect)

    
            
#     pygame.display.update()
    
# pygame.quit() 