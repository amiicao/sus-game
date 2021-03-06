from globals import *
from unit import *

bin_coord_map = {
    Direction.NORTH : BLUE_BIN_COORD,
    Direction.EAST : YELLOW_BIN_COORD,
    Direction.SOUTH : BLACK_BIN_COORD,
    Direction.WEST : GREEN_BIN_COORD,
}

class Garbage(Unit): #Pieces of trash
    def __init__(self, x, y, garbage_type, surface):
        super().__init__()
        self.x = x
        self.y = y
        self.surface = surface
        self.type = garbage_type
        self.head_inwards = True #Heading towards guy vs been hit & heading towards a bin
        self.direction = Direction.NEUTRAL #If heading towards guy, has not been hit in a direction yet
    
    #Move by 1 unit (a single screen update) towards Dude
    #OR move 1 unit towards garbage can that it was hit towards
    def move(self): 
        center_coords = (WIDTH/2, HEIGHT/2) #Roughly where the guy should be
        if(self.head_inwards):
            self.move_towards(center_coords)
        else:
            #assert self.direction != Direction.NEUTRAL, "Pieces should always have a direction after being hit!"
            if(self.direction == Direction.NEUTRAL):
                self.direction = Direction.NORTH #HACK
            self.move_towards(bin_coord_map[self.direction], 5)
    
    #Moves piece 1 unit towards dest
    def move_towards(self, dest, speed=1): 
        delta_x = dest[0] - self.x
        delta_y = dest[1] - self.y
        step_x = (delta_x / float(FPS)) * speed
        step_y = (delta_y / float(FPS)) * speed
        self.x += step_x
        self.y += step_y

    def draw(self):
        self.rect = screen.blit(self.surface, (self.x, self.y)) #Draw
        self.collide_rect = self.rect.inflate(2,2)

    def batted(self, direction): #Batted away by the guy
        self.head_inwards = False
        self.direction = direction

    def hit_guy(self): #Successfully hit the guy; Only deal with the piece, not the guy!
        self.collide_rect.size = (0,0); #Effectively remove the collision box around the "used" piece
        self.head_inwards = True #Get this piece to stop moving

    def reached_bin(self, bin_type: GarbageType): #Reached the garbage bin; Diff action depending on if correct bin
        global curr_score
        if (self.type == bin_type): #if reached correct bin; piece dies peacefully
            ding = pygame.mixer.Sound(os.path.join('assets', 'smw_coin.wav'))
            pygame.mixer.Sound.play(ding)
            curr_score[0] += 1
        else:
            curr_score[0] -= 1
            self.explode()
        #print(curr_score)
    
    def explode(self): #Upon reaching incorrect bin
        print("explosion")
        screen.blit(EXPLOSION,(self.x-10,(self.y-30))) #bluebin
        pygame.display.update()

        boom = pygame.mixer.Sound(os.path.join('assets', 'exploding_audio.ogg'))
        pygame.mixer.Sound.play(boom)
        pass 
