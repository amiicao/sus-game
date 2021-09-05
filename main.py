from pygame.constants import WINDOWHITTEST
from globals import * #Copy over the namespace
import dude
from garbageController import GarbageController

pygame.init()

#GAME OVER message
def draw_endgame():
    print("endgame")
    endgame_text = ENDGAME_FONT.render("GAME OVER", 15, (0,0,0))
    screen.blit(endgame_text,(WIDTH/2 - endgame_text.get_width()/2, HEIGHT/2 ))
    pygame.display.update()
    pygame.time.delay(4000)

def draw_window(lives):
    
    screen.blit(BACKGROUND, (0,0))
    # showing the remaining lives
    Lives_text = HEALTH_FONT.render("Lives: ", 15, (127,255,212))
    screen.blit(Lives_text, (WIDTH - Lives_text.get_width()- LIFE.get_width()*5 - 15, 5)) #Lives: ***** |
    for i in range(lives):
        #LIVES_REM= HEALTH_FONT.render("Lives: "+ str(LIVES), 25, (0,0,0))
        screen.blit(LIFE, (WIDTH - LIFE.get_width()*5 - 15 + LIFE.get_width()*i, LIFE.get_height()/2)) # let i = 2, |    Lives: 
    
    # Add the Bins on NESW of screen
    screen.blit(BLUE_BIN, BLUE_BIN_COORD)
    screen.blit(GREEN_BIN, GREEN_BIN_COORD)
    screen.blit(BLACK_BIN, BLACK_BIN_COORD)
    screen.blit(YELLOW_BIN, YELLOW_BIN_COORD)

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (245, 245, 220), CIRCLE_COORDS, CIRCLE_RADIUS)

    #pygame.display.flip() # Flip the display


def main():
    clock = pygame.time.Clock()
    # Run until the user asks to quit
    running = True
    guy = dude.Dude(LIVES) #There should only ever be one Dude instance
    garbage_controller = GarbageController()

    while running:
        clock.tick(FPS)
        remHealth = guy.getHealth()
        draw_window(remHealth) #Init screen

        ##Game logic goes here!##
        guy.draw() #Only draw inside of a game loop!
        garbage_controller.update()



        # If guy dies, end game message shows
        if(remHealth == 0):
            print ("DEAD")
            draw_endgame()
            pygame.display.update()
            pygame.quit()

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            ##Grab more events here!##
            guy.events_processor(event)
            garbage_controller.events_processor(event)

            


        # Update the screen
        pygame.display.update()
    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()
