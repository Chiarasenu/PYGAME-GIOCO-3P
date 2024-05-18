import pygame
from math import Vector2

class Snake_Rosso:
    def __init__(self) -> None:
        self.corpo_r = [Vector2(35,10), Vector2(36,10), Vector2(37,10)]
        self.direzione_r = Vector2(0,0)
        self.nuovo_corpo_r = False

    # IMMAGINI
        # Testa
        self.testaN_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_testaN.png')
        self.testaE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_testaE.png')
        self.testaS_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_testaS.png')
        self.testaO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_testaO.png')

        # Corpo
        self.corpoO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_corpo_orizzontale.png')
        self.corpoV_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_corpo_verticale.png')

        # Coda
        self.codaN_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_codaN.png')
        self.codaE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_codaE.png')
        self.codaS_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_codaS.png')
        self.codaO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_codaO.png')

        # Angoli
        self.angoloNE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_angoloNE.png')
        self.angoloNO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_angoloNO.png')
        self.angoloSE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_angoloSE.png')
        self.angoloSO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_angoloSO.png')

    


# Serve:
# - Coda, Corpo e Testa
# - Movimento
# - Mangiare (collisione con frutto)
# - Allungamento dopo Mangiare
# - Morte (collisione con se stesso o muro)