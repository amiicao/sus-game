from globals import * #Copy over the namespace
import dude

pygame.init()

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
