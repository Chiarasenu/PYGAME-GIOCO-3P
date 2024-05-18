import pygame
from math import Vector2

class Snake_Blu:
    def __init__(self) -> None:
        self.corpo = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direzione = Vector2(0,0)
        self.nuovo_corpo = False

    # IMMAGINI
        # Testa
        self.testaN = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_testaN.png')
        self.testaE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_testaE.png')
        self.testaS = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_testaS.png')
        self.testaO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_testaO.png')

        # Corpo
        self.corpoO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_corpo_orizzontale.png')
        self.corpoV = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_corpo_verticale.png')

        # Coda
        self.codaN = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaN.png')
        self.codaE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaE.png')
        self.codaS = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaS.png')
        self.codaO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaO.png')

        # Angoli
        self.angoloNE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloNE.png')
        self.angoloNO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloNO.png')
        self.angoloSE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloSE.png')
        self.angoloSO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloSO.png')

    


# Serve:
# - Coda, Corpo e Testa
# - Movimento
# - Mangiare (collisione con frutto)
# - Allungamento dopo Mangiare
# - Morte (collisione con se stesso o muro)
