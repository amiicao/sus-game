from typing import List
from pygame.constants import WINDOWHITTEST
from globals import * #Copy over the namespace
import dude
from garbageController import GarbageController

pygame.init()

#GAME OVER message
def draw_endgame():
    print("End game")
    endgame_text = ENDGAME_FONT.render("GAME OVER", 15, (127,255,212))
    screen.blit(endgame_text,(WIDTH/2 - endgame_text.get_width()/2, HEIGHT/2 ))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                return

def draw_window(lives):
    screen.blit(BACKGROUND, (0,0))
    # showing the remaining lives
    Lives_text = HEALTH_FONT.render("Lives: ", 15, (127,255,212))
    screen.blit(Lives_text, (WIDTH - Lives_text.get_width()- LIFE.get_width()*5 - 15, 5)) #Lives: ***** |
    for i in range(lives):
        #LIVES_REM= HEALTH_FONT.render("Lives: "+ str(LIVES), 25, (0,0,0))
        screen.blit(LIFE, (WIDTH - LIFE.get_width()*5 - 15 + LIFE.get_width()*i, LIFE.get_height()/2)) # let i = 2, |    Lives: 

    # Draw a solid circle in the center
    pygame.draw.circle(screen, (245, 245, 220), CIRCLE_COORDS, CIRCLE_RADIUS)

def draw_bins() -> List: #Get bin rects
    bins_rect = [] # Add the Bins on NESW of screen
    bins_rect.append(screen.blit(BLUE_BIN, BLUE_BIN_COORD))
    bins_rect.append(screen.blit(GREEN_BIN, GREEN_BIN_COORD))
    bins_rect.append(screen.blit(BLACK_BIN, BLACK_BIN_COORD))
    bins_rect.append(screen.blit(YELLOW_BIN, YELLOW_BIN_COORD))
    return bins_rect #[Blue, Green, Black, Yellow]

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
        bins = draw_bins()

        ##Game logic goes here!##
        guy.draw() #Only draw inside of a game loop!
        garbage_controller.update(bins)
        guy.hit_check(garbage_controller.actives)


        # If guy dies, end game message shows
        if(remHealth == 0):
            draw_endgame()
            running = False

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            ##Grab more events here!##
            guy.events_processor(event, garbage_controller.actives)
            garbage_controller.events_processor(event)

            


        # Update the screen
        pygame.display.update()
    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()
