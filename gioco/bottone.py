class Bottone():
    def __init__(self, immagine, pos, font, colore_scuro, colore_chiaro, testo_input):
        
        self.immagine = immagine
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.colore_scuro = colore_scuro
        self.colore_chiaro = colore_chiaro
        self.testo_input = testo_input
        self.testo = self.font.render(self.testo_input, True, self.colore_scuro)
        if self.immagine == None:
            self.immagine = self.testo
        centro = (self.x, self.y)
        self.rect = self.immagine.get_rect(centro)
        self.testo_rect = self.testo.get_rect(centro)

    def update(self, screen):
        if self.immagine is not None:
            screen.blit(self.immagine, self.testo)
        screen.blit(self.testo, self.testo_rect)

    def controllo_mouse(self, posizione):
        