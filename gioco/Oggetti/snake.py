from math import Vector2

class Snake:
    def __init__(self) -> None:
        self.corpo = [Vector2]

# Serve:
# - Coda, Corpo e Testa
# - Movimento
# - Mangiare (collisione con frutto)
# - Allungamento dopo Mangiare
# - Morte (collisione con se stesso o muro)