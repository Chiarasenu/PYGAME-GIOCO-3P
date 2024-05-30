import pygame
from pygame.math import Vector2

lato_celle = 40
numero_celle = 30

SCREEN_WIDTH = numero_celle * lato_celle
SCREEN_HEIGHT = numero_celle * lato_celle / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Snake_Blu:
    def __init__(self) -> None:
        self.corpo = [Vector2(5,7), Vector2(4,7), Vector2(3,7)]
        self.direzione = Vector2(1,0)
        self.punteggio = 0
        self.nuovo_blocco = False

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
        self.codaN = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaS.png').convert_alpha()
        self.codaE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaE.png').convert_alpha()
        self.codaS = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaN.png').convert_alpha()
        self.codaO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_codaO.png').convert_alpha()

        # Angoli
        self.angoloNE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloNE.png').convert_alpha()
        self.angoloNO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloNO.png').convert_alpha()
        self.angoloSE = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloSE.png').convert_alpha()
        self.angoloSO = pygame.image.load('Gioco/Immagini/PartiSnake/Blu/snake_blu_angoloSO.png').convert_alpha()

    

    def aggiungi_blocco(self):
        self.nuovo_blocco = True
        self.punteggio +=1

    def muovi_snake(self):
        if self.nuovo_blocco == True:
            copia_corpo = self.corpo[:]
            copia_corpo.insert(0, copia_corpo[0] + self.direzione)
            self.corpo = copia_corpo[:]
            self.nuovo_blocco = False
        else:
            copia_corpo = self.corpo[:-1]
            copia_corpo.insert(0, self.corpo[0] + self.direzione)
            self.corpo = copia_corpo[:]
            
    def update_testa(self):
        nuova_testa = self.corpo[0] - self.corpo[1]
        if nuova_testa == Vector2(1,0):
            self.testa = self.testaE
        elif nuova_testa == Vector2(-1,0):
            self.testa = self.testaO
        elif nuova_testa == Vector2(0,1):
            self.testa = self.testaS
        elif nuova_testa == Vector2(0,-1):
            self.testa = self.testaN

    def update_coda(self):
        nuova_coda = self.corpo[-1] - self.corpo[-2]
        if nuova_coda == Vector2(1,0):
            self.coda = self.codaE
        elif nuova_coda == Vector2(-1,0):
            self.coda = self.codaO
        elif nuova_coda == Vector2(0,1):
            self.coda = self.codaN
        elif nuova_coda == Vector2(0,-1):
            self.coda = self.codaS

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

    def draw_snake(self, lato_cella, screen):
        self.update_testa()
        self.update_coda()

        for i, blocco in enumerate(self.corpo):
            pos_x = int(blocco.x * lato_cella)
            pos_y = int(blocco.y * lato_cella)
            rect_blocco = pygame.Rect(pos_x, pos_y, lato_cella, lato_cella)
            if i == 0:
                screen.blit(self.testa, rect_blocco)
            elif i == len(self.corpo) -1:
                screen.blit(self.coda, rect_blocco)
            else:
                # Calcola la differenza di posizione tra il blocco corrente e i blocchi precedente e successivo
                blocco_precedente = self.corpo[i + 1] - blocco
                blocco_successivo = self.corpo[i - 1] - blocco
                
                # Se il blocco precedente e successivo sono allineati verticalmente
                if blocco_precedente.x == blocco_successivo.x:
                    # Disegna l'immagine del corpo verticale del serpente
                    screen.blit(self.corpoV, rect_blocco)
                # Se il blocco precedente e successivo sono allineati orizzontalmente
                elif blocco_precedente.y == blocco_successivo.y:
                    # Disegna l'immagine del corpo orizzontale del serpente
                    screen.blit(self.corpoO, rect_blocco)
                else:
                    # Determina quale angolo disegnare in base alle direzioni dei blocchi precedente e successivo
                    if (blocco_precedente.x == -1 and blocco_successivo.y == -1) or (blocco_precedente.y == -1 and blocco_successivo.x == -1):
                        # Disegna l'angolo in alto a sinistra
                        screen.blit(self.angoloNO, rect_blocco)
                    elif (blocco_precedente.x == 1 and blocco_successivo.y == -1) or (blocco_precedente.y == -1 and blocco_successivo.x == 1):
                        # Disegna l'angolo in alto a destra
                        screen.blit(self.angoloNE, rect_blocco)
                    elif (blocco_precedente.x == -1 and blocco_successivo.y == 1) or (blocco_precedente.y == 1 and blocco_successivo.x == -1):
                        # Disegna l'angolo in basso a sinistra
                        screen.blit(self.angoloSO, rect_blocco)
                    elif (blocco_precedente.x == 1 and blocco_successivo.y == 1) or (blocco_precedente.y == 1 and blocco_successivo.x == 1):
                        # Disegna l'angolo in basso a destra
                        screen.blit(self.angoloSE, rect_blocco)
