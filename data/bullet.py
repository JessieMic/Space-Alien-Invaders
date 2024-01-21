import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """A class to manage bullets """

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #self.color = self.settings.bullet_color

        #Creat a bullet rect at (0,0) and then set it to current position
        self.image = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\bullet_1.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        #The bullet posi/the game to get the ship rect and to have the bullet start at mid top of ship
        self.rect.midtop = ai_game.ship.rect.midtop

        #Stores the butllet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        #Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        #This function draws/surface/color of bullet/ the rect of bullet
        pygame.draw.rect(self.screen, self.color ,self.rect)