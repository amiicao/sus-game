# Simple pygame program

# Import and initialize the pygame library
import pygame
import os
pygame.init()

FPS = 60
BIN_WIDTH, BIN_HEIGHT = 130, 200
WIDTH, HEIGHT = 800, 800

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

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

def draw_window():
    
    screen.blit(BACKGROUND, (0,0))

    # Add the Bins on NESW of screen
    screen.blit(BLUE_BIN, (0, 0 ))
    screen.blit(GREEN_BIN, (50, 250))
    screen.blit(BLACK_BIN, (250, 450))
    screen.blit(YELLOW_BIN, (250, 50))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (245, 245, 220), (400, 400), 75)

    # Flip the display
    #pygame.display.flip()

    # Update the screen
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    # Run until the user asks to quit
    running = True
    while running:
        clock.tick(FPS)
        draw_window()
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # Done! Time to quit.
    pygame.quit()
if __name__ == "__main__":
    main()
