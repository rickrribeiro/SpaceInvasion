import sys
import pygame
from settings import Settings
from ship import ship

def run_game():
        # Initialize game and create a screen object.u     
        pygame.init()   
        ai_settings = Settings()  
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption("Alien Invasion") 
        bg_color = (230, 230, 230)   
        # Start the main loop for the game.w     
        while True:
                    # Watch for keyboard and mouse events.x         
            for event in pygame.event.get():   
                if event.type == pygame.QUIT:                
                    sys.exit()        # Make the most recently drawn screen visible.z
            # Redraw the screen during each pass through the loop.
            screen.fill(ai_settings.bg_color)
            pygame.display.flip()

run_game()