from globals import *


class Atk_range(): # this is for the ZONE, the attack range of the dude
    def __init__(self, x):
        self.x = x
    
    def draw(self):
        self.rect = screen.blit(ZONE_IMG,(CIRCLE_COORDS[0] - self.x/2, CIRCLE_COORDS[1] - DUDE_HEIGHT_OFFSET - 30 )) 
        self.collide_rect = self.rect.inflate(1,1)