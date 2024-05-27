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