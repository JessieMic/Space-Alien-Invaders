import pygame
from pygame.sprite import Sprite

class Stars(Sprite):
    """Class that helps desplay stars in the background"""

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Loading pics of stars
        self.image = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\star_6.bmp')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        #Methods that change something need to be named update
        self.y += self.settings.star_speed
        #it creates
        self.rect.y = self.y



