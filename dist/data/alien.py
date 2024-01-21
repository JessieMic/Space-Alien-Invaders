import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class that manages all the info for the alien"""

    def __init__(self,ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Loading the alien image and setting it as an attribute
        self.image = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\Alien.bmp')
        self.image = pygame.transform.scale(self.image,(70,57))
        self.rect = self.image.get_rect()

        #start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aline's exact horizontalk position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            #We will later on keep ask if one of the answers is true we will change der
            return True

    def update(self):
        """Move alien to the right or left"""
        self.x+= (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x