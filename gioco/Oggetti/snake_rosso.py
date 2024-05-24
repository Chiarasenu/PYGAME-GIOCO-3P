import pygame
from pygame.math import Vector2

class Snake_Rosso:
    def __init__(self) -> None:
        self.corpo_r = [Vector2(35,10), Vector2(36,10), Vector2(37,10)]
        self.direzione_r = Vector2(0,0)
        self.nuovo_corpo_r = False

    # IMMAGINI
        # Testa
        self.testaN_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_testaN.png').convert_alpha()
        self.testaE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_testaE.png').convert_alpha()
        self.testaS_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_testaS.png').convert_alpha()
        self.testaO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_testaO.png').convert_alpha()

        # Corpo
        self.corpoO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_corpo_orizzontale.png').convert_alpha()
        self.corpoV_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_corpo_verticale.png').convert_alpha()

        # Coda
        self.codaN_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_codaN.png').convert_alpha()
        self.codaE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_codaE.png').convert_alpha()
        self.codaS_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_codaS.png').convert_alpha()
        self.codaO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_codaO.png').convert_alpha()

        # Angoli
        self.angoloNE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_angoloNE.png').convert_alpha()
        self.angoloNO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_angoloNO.png').convert_alpha()
        self.angoloSE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_angoloSE.png').convert_alpha()
        self.angoloSO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_rosso_angoloSO.png').convert_alpha()

    def update_testa(self):
        nuova_testa = self.corpo[1] - self.body[0]
        if nuova_testa == Vector2(1,0):
            self.testa = self.testaO
        elif nuova_testa == Vector2(-1,0):
            self.testa = self.testaE
        elif nuova_testa == Vector2(0,1):
            self.testa = self.testaN
        elif nuova_testa == Vector2(0,-1):
            self.testa = self.testaS

    def update_coda(self):
        nuova_coda = self.corpo[-2] - self.body[-1]
        if nuova_coda == Vector2(1,0):
            self.testa = self.codaO
        elif nuova_coda == Vector2(-1,0):
            self.coda = self.codaE
        elif nuova_coda == Vector2(0,1):
            self.coda = self.codaN
        elif nuova_coda == Vector2(0,-1):
            self.coda = self.codaS

    def aggiugi_blocco(self):
        self.nuovo_blocco = True

    def muovi_snake(self):
        if self.nuovo_blocco == True:
            copia_corpo = self.corpo[:]
            copia_corpo.insert(0, copia_corpo[0] + self.direzione)
            self.corpo = copia_corpo[:]
            self.nuovo_blocco = False


# Serve:
# - Coda, Corpo e Testa
# - Movimento
# - Mangiare (collisione con frutto)
# - Allungamento dopo Mangiare
# - Morte (collisione con se stesso o muro)