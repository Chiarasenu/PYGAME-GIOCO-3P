import pygame
from pygame.math import Vector2

class Snake_Blu:
    def __init__(self) -> None:
        self.corpo = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direzione = Vector2(0,0)
        self.nuovo_corpo = False

    # IMMAGINI
        # Testa
        self.testaN = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_testaN.png').convert_alpha()
        self.testaE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_testaE.png').convert_alpha()
        self.testaS = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_testaS.png').convert_alpha()
        self.testaO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_testaO.png').convert_alpha()

        # Corpo
        self.corpoO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_corpo_orizzontale.png').convert_alpha()
        self.corpoV = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_corpo_verticale.png').convert_alpha()

        # Coda
        self.codaN = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaN.png').convert_alpha()
        self.codaE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaE.png').convert_alpha()
        self.codaS = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaS.png').convert_alpha()
        self.codaO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaO.png').convert_alpha()

        # Angoli
        self.angoloNE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloNE.png').convert_alpha()
        self.angoloNO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloNO.png').convert_alpha()
        self.angoloSE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloSE.png').convert_alpha()
        self.angoloSO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloSO.png').convert_alpha()

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
# - Movimento
# - Mangiare (collisione con frutto)
# - Allungamento dopo Mangiare
# - Morte (collisione con se stesso o muro)
