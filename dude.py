from pygame.constants import DOUBLEBUF, KEYUP, K_DOWN, K_SPACE, K_a, K_w
from globals import *
from unit import *
from atk_range import *

class Stance(Enum):
    REST = DUDE_REST
    ATK = DUDE_ATK
    HURT = DUDE_HURT

class Dude(Unit):
    def __init__(self, lives) -> None:
        super().__init__()
        self.health = lives
        self.stance = Stance.REST
        self.swingtimer = 3000 #3.5s
        self.injurytimer = 50 #0.2s
        self.direction = Direction.NEUTRAL
        self.last_swing_time = 0 #Used to track DUDE_ATK stance
        self.last_injury_time = 0 #Used to track DUDE_HURT stance
        self.coordinates = (CIRCLE_COORDS[0] - DUDE_HEIGHT_OFFSET + 10, CIRCLE_COORDS[1] - DUDE_HEIGHT_OFFSET - 10)
    
    def events_processor(self, event, garbage_list, zone): #Call method as part of events loop
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
            #If able to and attempting to hit; No empty swings allowed
            if(event.key == pygame.K_SPACE and self.stance == Stance.REST): #Must click spacebar
                self.last_swing_time = pygame.time.get_ticks()
                self.change_stance(Stance.ATK)
                self.swing_bat(self.direction, garbage_list,zone) #Cannot swing in neutral
#!!!!!!!!!!!!!!!!!
            
            if(event.key in (pygame.K_w, pygame.K_UP)):
                self.direction = Direction.NORTH
            elif(event.key in (pygame.K_d, pygame.K_RIGHT)):
                self.direction = Direction.EAST
            elif(event.key in (pygame.K_s, pygame.K_DOWN)):
                self.direction = Direction.SOUTH
            elif(event.key in (pygame.K_a, pygame.K_LEFT)):
                self.direction = Direction.WEST
            
        elif (event.type == pygame.KEYUP):
            if(event.key == pygame.K_SPACE and self.stance == Stance.ATK):
                self.change_stance(Stance.REST)
            if (event.key in (pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)):
                self.direction = Direction.NEUTRAL


    def change_stance(self, stance): #Must blit the new stance after changing
        self.stance = stance

    def draw(self):
        self.rect = screen.blit(self.stance.value, self.coordinates) #Draw
        self.collide_rect = self.rect.inflate(1,1)

    #Template: Implement collision logic with trash objects; Only check for collision at moment of KEYDOWN!
    def swing_bat(self, hit_dir, garbage_list, zone):
        for piece in garbage_list: #Can hit multiple pieces out at once
###            #if (self.collide_rect.colliderect(piece.collide_rect)):
            if (zone.collide_rect.colliderect(piece.collide_rect)):
                piece.batted(hit_dir)

    #Call when guy is hit
    def injured(self): #Hurt dudes cannot be hurt again while injured; Only able to lose one life at a time
        self.last_injury_time = pygame.time.get_ticks()
        self.change_stance(Stance.HURT) #Timer set, injured dude cannot attack/revert to rest instantly
        self.health -= 1
    
        meow = pygame.mixer.Sound(os.path.join('assets', 'meow_audio.wav'))
        pygame.mixer.Sound.play(meow)


    #Call in main game loop; Checks if guy hit by garbage & injures him if so
    def hit_check(self, garbage_list) -> bool: #Takes in list of active Garbage objs from garbageController
        t_list = garbage_list.copy()
        for piece in t_list:
            #if(self.collide_rect.colliderect(piece.collide_rect) and self.stance == Stance.REST and temp == True):
            if(self.collide_rect.colliderect(piece.collide_rect) and self.stance == Stance.REST ):
                if(piece.head_inwards): #Don't let the guy whack pieces into himself
                    piece.hit_guy()
                    garbage_list.remove(piece); del piece
                    self.injured()
                    print ("been hit")

    #passing health to
    def getHealth(self):
        return self.health

    #Template: what happens when ded?
 #   def death(self):
 #       pass
