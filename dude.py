from pygame.constants import DOUBLEBUF, KEYUP, K_SPACE, K_a, K_w
from globals import *
from enum import Enum

class Direction(Enum):
    NEUTRAL = 0 #Batter is not swinging in any direction
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Stance(Enum):
    REST = DUDE_REST
    ATK = DUDE_ATK
    HURT = DUDE_HURT

class Dude:
    def __init__(self, lives) -> None:
        self.health = lives
        self.stance = Stance.REST
        self.swingtimer = 1500 #1.5s
        self.injurytimer = 3500 #3.5s
        self.direction = Direction.NEUTRAL
        self.last_swing_time = 0 #Used to track DUDE_ATK stance
        self.last_injury_time = 0 #Used to track DUDE_HURT stance
    
    def events_processor(self, event): #Call method as part of events loop
        #If dude is injured, he is not able to aim in a direction or do anything
        injury_time_delta = pygame.time.get_ticks() - self.last_injury_time
        if(self.stance == Stance.HURT and injury_time_delta >= self.injurytimer):
            self.change_stance(Stance.REST)
        elif(self.stance == Stance.HURT):
            self.direction = Direction.NEUTRAL #Cannot aim into a direction while injured
            return

        #If swing timer eclipsed, return back to rest stance (regardless of spacebar events)
        swing_time_delta = pygame.time.get_ticks() - self.last_swing_time
        if(self.stance == Stance.ATK and swing_time_delta >= self.swingtimer): 
            self.change_stance(Stance.REST)

        if (event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE and self.stance == Stance.REST): #If able to and attempting to hit
                self.last_swing_time = pygame.time.get_ticks()
                self.change_stance(Stance.ATK)
                self.swing_bat() #TODO
            
            if(event.key == pygame.K_w):
                self.direction = Direction.NORTH
            elif(event.key == pygame.K_d):
                self.direction = Direction.EAST
            elif(event.key == pygame.K_s):
                self.direction = Direction.SOUTH
            elif(event.key == pygame.K_a):
                self.direction = Direction.WEST
            
        elif (event.type == pygame.KEYUP):
            if(event.key == pygame.K_SPACE and self.stance == Stance.ATK):
                self.change_stance(Stance.REST)
            if (event.key in (pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)):
                self.direction = Direction.NEUTRAL


    def change_stance(self, stance): #Must blit the new stance after changing
        self.stance = stance

    def draw(self):
        screen.blit(self.stance.value, (CIRCLE_COORDS[0] - DUDE_HEIGHT_OFFSET + 10, CIRCLE_COORDS[1] - DUDE_HEIGHT_OFFSET - 10)) #Draw

    #Template: Implement collision logic with trash objects; Only check for collision at moment of KEYDOWN!
    def swing_bat(self):
        pass

    #Call in events loop, when guy is hit
    def injured(self): #Hurt dudes cannot be hurt again while injured; Only able to lose one life at a time
        self.last_injury_time = pygame.time.get_ticks()
        self.change_stance(Stance.HURT) #Timer set, injured dude cannot attack/revert to rest instantly
        self.health -= 1
        if(self.health <= 0):
            self.death() #TODO


    #Template: what happens when ded?
    def death(self):
        pass