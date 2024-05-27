# from enum import Enum
 
# class enum_frutta(Enum):
#     MELA = 'Gioco/Immagini/Frutta/mela.png'
#     CILIEGIA = 'Gioco/Immagini/Frutta/mela.png'
#     LIMONE = 'Gioco/Immagini/Frutta/mela.png'
#     ANGURIA = 'Gioco/Immagini/Frutta/mela.png'

# ogg_frutta = frutta(screen, [randint(0, numero_celle -1), 
#  randint(0, numero_celle -1)], lato_celle, enum_frutta.MELA.name,
#  enum_frutta.MELA.value)

# Gestione degli eventi: 
# Il movimento del serpente deve essere aggiornato 
# in ogni ciclo del gioco. Attualmente, 
# la chiamata alla funzione update() viene 
# eseguita solo quando viene rilevata una 
# pressione di tasto, ma dovrebbe essere 
# eseguita indipendentemente dagli eventi 
# della tastiera.

# Inizializzazione della direzione del serpente: 
# Assicurati che il serpente inizi con una direzione
# predefinita, altrimenti non si muoverà.

# Uso corretto della variabile self.nuovo_blocco: 
# Hai alcune incoerenze con l'uso della variabile 
# self.nuovo_blocco e self.nuovo_corpo nel metodo 
# muovi_snake.

# update()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         if main_game.snake.direzione.y != 1:
            #             main_game.snake.direzione = Vector2(0,-1)
            #     if event.key == pygame.K_RIGHT:
            #         if main_game.snake.direzione.x != -1:
            #             main_game.snake.direzione = Vector2(1,0)
            #     if event.key == pygame.K_DOWN:
            #         if main_game.snake.direzione.y != -1:
            #             main_game.snake.direzione = Vector2(0,1)
            #     if event.key == pygame.K_LEFT:
            #         if main_game.snake.direzione.x != 1:
            #             main_game.snake.direzione = Vector2(-1,0)

                # if key[K_w]:
                #     if main_game.snake.direzione.y != 1:
                #         main_game.snake.direzione = Vector2(0, -1)
                # if key[K_d]:
                #     if main_game.snake.direzione.x != -1:
                #         main_game.snake.direzione = Vector2(1, 0)
                # if key[K_s]:
                #     if main_game.snake.direzione.y != -1:
                #         main_game.snake.direzione = Vector2(0, 1)
                # if key[K_a]:
                #     if main_game.snake.direzione.x != 1:
        #         #         main_game.snake.direzione = Vector2(-1, 0)
                    
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_UP:
        #             if main_game.snake.direzione.y != 1:
        #                 main_game.snake.direzione = Vector2(0,-1)
        #         if event.key == pygame.K_RIGHT:
        #             if main_game.snake.direzione.x != -1:
        #                 main_game.snake.direzione = Vector2(1,0)
        #         if event.key == pygame.K_DOWN:
        #             if main_game.snake.direzione.y != -1:
        #                 main_game.snake.direzione = Vector2(0,1)
        #         if event.key == pygame.K_LEFT:
        #             if main_game.snake.direzione.x != 1:
        #                 main_game.snake.direzione = Vector2(-1,0)