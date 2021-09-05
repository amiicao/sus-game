import pygame # Import and initialize the pygame library
import os
from abc import abstractmethod
from enum import Enum
import random
import math
pygame.font.init()


isALIVE = True
FPS = 60
BIN_WIDTH, BIN_HEIGHT = 130, 200
WIDTH, HEIGHT = 800, 800

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT]) #This must run before anything is drawn

HEALTH_FONT = pygame.font.SysFont('comicsans', 75)
ENDGAME_FONT = pygame.font.SysFont('comicsans', 75)
CIRCLE_COORDS = (400, 400)
CIRCLE_RADIUS = 75
LIVES = 5
GARBAGE_SIZE = 25

class Direction(Enum):
    NEUTRAL = 0 #Batter is not swinging in any direction
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class GarbageType(Enum):
    BLUE = 0
    GREEN = 1
    BLACK = 2
    YELLOW = 3

#Images
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets','BACKGROUND.jpg')),(WIDTH,HEIGHT))
BLUE_BIN_IMAGE = pygame.image.load(os.path.join('assets','BLUE_BIN.png'))
BLUE_BIN = pygame.transform.scale(BLUE_BIN_IMAGE, (BIN_WIDTH, BIN_HEIGHT))
GREEN_BIN_IMAGE = pygame.image.load(os.path.join('assets','GREEN_BIN.png'))
GREEN_BIN = pygame.transform.scale(GREEN_BIN_IMAGE, (BIN_WIDTH, BIN_HEIGHT))
BLACK_BIN_IMAGE = pygame.image.load(os.path.join('assets','BLACK_BIN.png'))
BLACK_BIN = pygame.transform.scale(BLACK_BIN_IMAGE, (BIN_WIDTH, BIN_HEIGHT))
YELLOW_BIN_IMAGE = pygame.image.load(os.path.join('assets','YELLOW_BIN.png'))
YELLOW_BIN = pygame.transform.scale(YELLOW_BIN_IMAGE, (BIN_WIDTH, BIN_HEIGHT))

BLUE_BIN_COORD = (WIDTH/2-BLUE_BIN.get_width()/2, 0)
GREEN_BIN_COORD = (0,(HEIGHT/2-GREEN_BIN.get_height()/2))
BLACK_BIN_COORD = (WIDTH/2-BLACK_BIN.get_width()/2, HEIGHT-BLACK_BIN.get_height())
YELLOW_BIN_COORD = (WIDTH-YELLOW_BIN.get_width(),HEIGHT/2-YELLOW_BIN.get_height()/2)

LIFE_IMAGE = pygame.image.load(os.path.join('assets','LIVES.png'))
LIFE = pygame.transform.scale(LIFE_IMAGE, (25, 30))

DUDE_HEIGHT_OFFSET = 50
DUDE_ATK_IMG = pygame.image.load(os.path.join('assets','SPRITE_ATK.png'))
DUDE_ATK = pygame.transform.scale(DUDE_ATK_IMG, (CIRCLE_RADIUS, CIRCLE_RADIUS + DUDE_HEIGHT_OFFSET))
DUDE_HURT_IMG = pygame.image.load(os.path.join('assets','SPRITE_HURT.png'))
DUDE_HURT = pygame.transform.scale(DUDE_HURT_IMG, (CIRCLE_RADIUS, CIRCLE_RADIUS + DUDE_HEIGHT_OFFSET))
DUDE_REST_IMG = pygame.image.load(os.path.join('assets','SPRITE_REST.png'))
DUDE_REST = pygame.transform.scale(DUDE_REST_IMG, (CIRCLE_RADIUS, CIRCLE_RADIUS + DUDE_HEIGHT_OFFSET))