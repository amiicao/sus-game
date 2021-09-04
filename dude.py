from globals import *

WIDTH, HEIGHT = 800, 800

class Dude:
    def __init__(self, lives) -> None:
        self.health = lives
        self.surface = pygame.image.load(os.path.join('assets','SPRITE_REST.png'))