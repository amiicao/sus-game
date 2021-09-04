import pygame # Import and initialize the pygame library
import os

FPS = 60
BIN_WIDTH, BIN_HEIGHT = 130, 200
WIDTH, HEIGHT = 800, 800

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT]) #This must run before anything is drawn

LIVES = 5

#images
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets','BACKGROUND.jpg')),(WIDTH,HEIGHT))

BLUE_BIN_IMAGE = pygame.image.load(os.path.join('assets','BLUE_BIN.png'))
BLUE_BIN = pygame.transform.scale(BLUE_BIN_IMAGE, (BIN_WIDTH, BIN_HEIGHT))
GREEN_BIN_IMAGE = pygame.image.load(os.path.join('assets','GREEN_BIN.png'))
GREEN_BIN = pygame.transform.scale(GREEN_BIN_IMAGE, (BIN_WIDTH, BIN_HEIGHT))
BLACK_BIN_IMAGE = pygame.image.load(os.path.join('assets','BLACK_BIN.png'))
BLACK_BIN = pygame.transform.scale(BLACK_BIN_IMAGE, (BIN_WIDTH, BIN_HEIGHT))
YELLOW_BIN_IMAGE = pygame.image.load(os.path.join('assets','YELLOW_BIN.png'))
YELLOW_BIN = pygame.transform.scale(YELLOW_BIN_IMAGE, (BIN_WIDTH, BIN_HEIGHT))

DUDE_ATK_IMG = pygame.image.load(os.path.join('assets','SPRITE_ATK.png'))
DUDE_HURT_IMG = pygame.image.load(os.path.join('assets','SPRITE_HURT.png'))
DUDE_REST_IMG = pygame.image.load(os.path.join('assets','SPRITE_REST.png'))