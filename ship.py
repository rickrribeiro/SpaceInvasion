import pygame

class Ship():
    def __init__(self,ai_settings,screen): #self reference and the screen where the shil will be drawed
        #initialize and set position
        self.screen =screen
        self.ai_settings = ai_settings
        #load image
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect() #Python let you to treat the elements as rectangles
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        
    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)
