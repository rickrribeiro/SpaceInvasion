import pygame

class ship():
    def __init__(self,screen): #self reference and the screen where the shil will be drawed
        #initialize and set position
        self.screen()=screen
        #load image
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect() #Python 
        self.screen_rect = screen.get_rect()

        #start each new ship at the botton center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.botton = self.screen_rect.botton

    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)
