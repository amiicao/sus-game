from garbage import Garbage
from globals import *

garbage_dict = {
    'BLU1.png' : GarbageType.BLUE, 'BLU2.png' : GarbageType.BLUE, 'BLU3.png' : GarbageType.BLUE,
    'G1.png' : GarbageType.GREEN, 'G2.png' : GarbageType.GREEN, 'G3.png' : GarbageType.GREEN,
    'B1.png' : GarbageType.BLACK, 'B2.png' : GarbageType.BLACK, 'B3.png' : GarbageType.BLACK,   
    'Y1.png' : GarbageType.YELLOW, 'Y2.png' : GarbageType.YELLOW, 'Y3.png' : GarbageType.YELLOW,
    }

class GarbageController: #deliberately not inheriting off Garbage; This just stores and manages garbage objects
    def __init__(self) -> None:
        self.actives = [] #List of Garbage objects currently in flight
        self.last_spawn_time = 0 #get delta (in ms)
        self.spawn_timer = 1000 #spawn garbage every 1s
        self.generator = self.garbage_generator()

    def edge_coord_generator(self):
        bucket = [0,1] #x, y
        choice = random.choice(bucket)
        if(not choice): #x is edge
            x_coord = random.choice([0, WIDTH - GARBAGE_SIZE])
            y_coord = random.randrange(HEIGHT+1)
        else:
            x_coord = random.randrange(WIDTH+1)
            y_coord = random.choice([0, HEIGHT - GARBAGE_SIZE])
        return (x_coord, y_coord)

    
    def garbage_generator(self): #Assign this to a func var & call next(var) to generate more garbage
        while True:
            piece = random.choice([key for key in garbage_dict]) #Choose a random key
            garbage_img = pygame.image.load(os.path.join('assets',piece))
            garbage_surface = pygame.transform.scale(garbage_img, (GARBAGE_SIZE, GARBAGE_SIZE))
            coords = self.edge_coord_generator()
            garbage = Garbage(coords[0], coords[1], garbage_dict[piece], garbage_surface)
            self.actives.append(garbage)
            yield garbage

    def events_processor(self, event):
        pass
        #TODO collision


    def update(self, bins):
        spawn_delta = pygame.time.get_ticks() - self.last_spawn_time
        if(spawn_delta >= self.spawn_timer):
            next(self.generator)
            self.last_spawn_time = pygame.time.get_ticks() #reset

        t_list = self.actives.copy()
        for piece in t_list:
            piece.move() #move THEN draw new pos
            piece.draw()
            
            #Garbage going into a bin
            collided_bin = piece.collide_rect.collidelist(bins)
            if (collided_bin > -1 and piece.direction != Direction.NEUTRAL): #if collided
                bin_type = GarbageType(collided_bin) 
                piece.reached_bin(bin_type)
                self.actives.remove(piece)
                del piece