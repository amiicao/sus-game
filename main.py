from pygame.constants import WINDOWHITTEST
from globals import * #Copy over the namespace
import dude

pygame.init()

#GAME OVER message
def draw_endgame():
    draw_endgame = ENDGAME_FONT.render("GAME OVER", 25, (0,0,0))
    screen.blit(draw_endgame,WIDTH/2-draw_endgame.get_width() /2 , HEIGHT/2 - draw_endgame.get_height()/2)

def draw_window():
    
    screen.blit(BACKGROUND, (0,0))

    # showing the remaining lives
    LIVES_REM= HEALTH_FONT.render("Lives: "+ str(LIVES), 25, (0,0,0))
    screen.blit(LIVES_REM, (WIDTH - LIVES_REM.get_width() - 10, 10))
    
    # Add the Bins on NESW of screen
    screen.blit(BLUE_BIN, (WIDTH/2-BLUE_BIN.get_width()/2, 0 ))
    screen.blit(GREEN_BIN, (0,(HEIGHT/2-GREEN_BIN.get_height()/2)))
    screen.blit(BLACK_BIN, (WIDTH/2-BLACK_BIN.get_width()/2, HEIGHT-BLACK_BIN.get_height()))
    screen.blit(YELLOW_BIN, (WIDTH-YELLOW_BIN.get_width(),HEIGHT/2-YELLOW_BIN.get_height()/2))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (245, 245, 220), (400, 400), 75)

    #pygame.display.flip() # Flip the display


def main():
    clock = pygame.time.Clock()
    # Run until the user asks to quit
    running = True
    while running:
        clock.tick(FPS)
        draw_window() #Init screen

        ##Game logic goes here!##
        guy = dude.Dude(LIVES)

        # If guy dies, end game message shows
        #draw_endgame()

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            ##Grab more events here!##
            

        # Update the screen
        pygame.display.update()
    # Done! Time to quit.
    pygame.quit()
if __name__ == "__main__":
    main()
