from globals import *

class Dude:
    def __init__(self, lives) -> None:
        self.health = lives
        self.atk_img = DUDE_ATK_IMG
        self.hurt_img = DUDE_HURT_IMG
        self.rest_img = DUDE_REST_IMG
        screen.blit(self.rest_img, (WIDTH/2, HEIGHT/2))
    
        