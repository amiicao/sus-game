#For easier collision detection

from globals import *

class Unit:
    def __init__(self):
        self.rect = None #lateinit
        self.collide_rect = None

    @abstractmethod
    def draw(self):
        pass