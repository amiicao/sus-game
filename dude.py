from globals import *

WIDTH, HEIGHT = 800, 800

class Dude:
    def __init__(self, lives) -> None:
        self.health = lives
        self.atk_img = pygame.image.load(os.path.join('assets','SPRITE_ATK.png'))
        self.hurt_img = pygame.image.load(os.path.join('assets','SPRITE_HURT.png'))
        self.rest_img = pygame.image.load(os.path.join('assets','SPRITE_REST.png'))
        