import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 
def run_game():
        # Initialize game and create a screen object.u     
        pygame.init()   
        ai_settings = Settings()  
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption("Alien Invasion") 
        ship = Ship(ai_settings,screen)
        bg_color = (230, 230, 230)   
        # Start the main loop for the game.w     
        while True:
                    # Watch for keyboard and mouse events.x         
            gf.check_events(ship)
            ship.update()
            # Redraw the screen during each pass through the loop.
            gf.update_screen(ai_settings,screen,ship)

run_game()




#Refactoring is a disciplined technique for restructuring an existing body of code, altering its internal structure without changing its external behavior. Its heart is a series of small behavior preserving transformations.