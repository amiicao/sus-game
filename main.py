# Simple pygame program

# Import and initialize the pygame library
import pygame
import os
pygame.init()

FPS = 60

#images
#BACKGROUND = pygame.image.load(os.path.join('assets','BACKGROUND.png'))
#BLUE_BIN = pygame.image.load(os.path.join('assets','BLUE_BIN.png'))
#GREEN_BIN = pygame.image.load(os.path.join('assets','GREEN_BIN.png'))
#BLACK_BIN = pygame.image.load(os.path.join('assets','BLACK_BIN.png'))

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

def draw_window():
    # Add the Bins on lower screen
    #screen.blit(BLUE_BIN, (400, 183 ))
    #screen.blit(GREEN_BIN, (400, 316))
    #screen.blit(BLACK_BIN, (400, 450))

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

    # Update the screen
    #pygame.display.update()


def main():
    clock = pygame.time.Clock()
    # Run until the user asks to quit
    running = True
    while running:
        clock.tick(FPS)

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_window()
    # Done! Time to quit.
    pygame.quit()
if __name__ == "__main__":
    main()
