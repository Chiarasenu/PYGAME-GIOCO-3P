import pygame
from pygame.math import Vector2

lato_celle = 40
numero_celle = 30

SCREEN_WIDTH = numero_celle * lato_celle
SCREEN_HEIGHT = numero_celle * lato_celle / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Snake_Rosso:
    def __init__(self) -> None:
        self.corpo_r = [Vector2(5,15), Vector2(4,15), Vector2(3,15)]
        self.direzione_r = Vector2(0,0)
        self.nuovo_corpo_r = False

    # IMMAGINI
        # Testa
        self.testaN_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_testaN.png').convert_alpha()
        self.testaE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_testaE.png').convert_alpha()
        self.testaS_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_testaS.png').convert_alpha()
        self.testaO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_testaO.png').convert_alpha()

        # Corpo
        self.corpoO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_corpo_orizzontale.png').convert_alpha()
        self.corpoV_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_corpo_verticale.png').convert_alpha()

        # Coda
        self.codaN_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_codaN.png').convert_alpha()
        self.codaE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_codaE.png').convert_alpha()
        self.codaS_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_codaS.png').convert_alpha()
        self.codaO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_codaO.png').convert_alpha()

        # Angoli
        self.angoloNE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_angoloNE.png').convert_alpha()
        self.angoloNO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_angoloNO.png').convert_alpha()
        self.angoloSE_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_angoloSE.png').convert_alpha()
        self.angoloSO_r = pygame.image.load('Gioco/Immagini/PartiSnake/Rosso/snake_rosso_angoloSO.png').convert_alpha()

    def update_testa(self):
        nuova_testa = self.corpo_r[1] - self.corpo_r[0]
        if nuova_testa == Vector2(1,0):
            self.testa = self.testaO_r
        elif nuova_testa == Vector2(-1,0):
            self.testa = self.testaE_r
        elif nuova_testa == Vector2(0,1):
            self.testa = self.testaN_r
        elif nuova_testa == Vector2(0,-1):
            self.testa = self.testaS_r

    def update_coda(self):
        nuova_coda = self.corpo_r[-2] - self.corpo_r[-1]
        if nuova_coda == Vector2(1,0):
            self.testa = self.codaO_r
        elif nuova_coda == Vector2(-1,0):
            self.coda = self.codaE_r
        elif nuova_coda == Vector2(0,1):
            self.coda = self.codaN_r
        elif nuova_coda == Vector2(0,-1):
            self.coda = self.codaS_r

    def aggiugi_blocco(self):
        self.nuovo_blocco = True

    def muovi_snake(self):
        if self.nuovo_blocco == True:
            copia_corpo = self.corpo_r[:]
            copia_corpo.insert(0, copia_corpo[0] + self.direzione_r)
            self.corpo_r = copia_corpo[:]
            self.nuovo_blocco_r = False
        
    def draw_snake(self, lato_cella, screen):
        self.update_testa()
        self.update_coda()

        for i, blocco in enumerate(self.corpo_r):
            pos_x = int(blocco.x * lato_cella)
            pos_y = int(blocco.y * lato_cella)
            rect_blocco = pygame.Rect(pos_x, pos_y, lato_cella, lato_cella)
            if i == 0:
                screen.blit(self.testa, rect_blocco)
            elif i == len(self.corpo_r) -1:
                screen.blit(self.coda, rect_blocco)
            else:
                # Calcola la differenza di posizione tra il blocco corrente e i blocchi precedente e successivo
                blocco_precedente = self.corpo_r[i + 1] - blocco
                blocco_successivo = self.corpo_r[i - 1] - blocco
                
                # Se il blocco precedente e successivo sono allineati verticalmente
                if blocco_precedente.x == blocco_successivo.x:
                    # Disegna l'immagine del corpo verticale del serpente
                    screen.blit(self.corpoV_r, rect_blocco)
                # Se il blocco precedente e successivo sono allineati orizzontalmente
                elif blocco_precedente.y == blocco_successivo.y:
                    # Disegna l'immagine del corpo orizzontale del serpente
                    screen.blit(self.corpoO_r, rect_blocco)
                else:
                    # Determina quale angolo disegnare in base alle direzioni dei blocchi precedente e successivo
                    if (blocco_precedente.x == -1 and blocco_successivo.y == -1) or (blocco_precedente.y == -1 and blocco_successivo.x == -1):
                        # Disegna l'angolo in alto a sinistra
                        screen.blit(self.angoloNO_r, rect_blocco)
                    elif (blocco_precedente.x == 1 and blocco_successivo.y == -1) or (blocco_precedente.y == -1 and blocco_successivo.x == 1):
                        # Disegna l'angolo in alto a destra
                        screen.blit(self.angoloNE_r, rect_blocco)
                    elif (blocco_precedente.x == -1 and blocco_successivo.y == 1) or (blocco_precedente.y == 1 and blocco_successivo.x == -1):
                        # Disegna l'angolo in basso a sinistra
                        screen.blit(self.angoloSO_r, rect_blocco)
                    elif (blocco_precedente.x == 1 and blocco_successivo.y == 1) or (blocco_precedente.y == 1 and blocco_successivo.x == 1):
                        # Disegna l'angolo in basso a destra
                        screen.blit(self.angoloSE_r, rect_blocco)


# Serve:
# - Coda, Corpo e Testa
# - Movimento
# - Mangiare (collisione con frutto)
# - Allungamento dopo Mangiare
# - Morte (collisione con se stesso o muro)