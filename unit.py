#For easier collision detection

from globals import *

class Unit:
    def __init__(self):
        self.rect = None #lateinit
        self.collide_rect = None

    @abstractmethod
    def collision(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def death(self):
        pass
