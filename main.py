from typing import List
from pygame.constants import WINDOWHITTEST
from globals import * #Copy over the namespace
import dude
from garbageController import GarbageController
import atk_range

pygame.init()

#GAME OVER message
def draw_endgame():
    global curr_score
    print("End game")
    endgame_text = ENDGAME_FONT.render("GAME OVER", 15, (127,255,212))
    endgame_text_coords = (WIDTH/2 - endgame_text.get_width()/2, HEIGHT/2)
    score_text = ENDGAME_FONT.render(f"Score : {curr_score[0]}", 15, (127,255,212))
    screen.blit(endgame_text, endgame_text_coords)
    screen.blit(score_text, (endgame_text_coords[0] + 45, endgame_text_coords[1] - 55))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                return

def draw_window(lives):
    global curr_score
    screen.blit(BACKGROUND, (0,0))
    # showing the remaining lives
    lives_text = HEALTH_FONT.render("Lives: ", 15, (127,255,212))
    score_text = HEALTH_FONT.render(f"Score: {curr_score[0]}", 15, (127,255,212))
    x_coord_text = WIDTH - lives_text.get_width()- LIFE.get_width()*5 - 15
    screen.blit(lives_text, (x_coord_text, 5))
    screen.blit(score_text, (x_coord_text, 55)) 
    for i in range(lives):
        screen.blit(LIFE, (WIDTH - LIFE.get_width()*5 - 15 + LIFE.get_width()*i, LIFE.get_height()/2)) # let i = 2, |    Lives: 
    

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
    zone = atk_range.Atk_range(ZONE_IMG.get_width() )

    while running:
        clock.tick(FPS)
        remHealth = guy.getHealth()
        draw_window(remHealth) #Init screen
        bins = draw_bins()

        ##Game logic goes here!##
        zone.draw()
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
            guy.events_processor(event, garbage_controller.actives,zone)
            garbage_controller.events_processor(event)
            

        # Update the screen
        pygame.display.update()
    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    main()
