import pygame
from time import sleep
class Ship:
    """A class to manage the ship"""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Load the ship image and get its rect
        self.image = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\ship.bmp')
        self.rect = self.image.get_rect()
                    #get_rect() positions the image in a x y

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #Important to save the senter by doing this vvv
        self.x = float(self.rect.x)

        #Movment flag
        self.moving_right = False
        self.moving_left = False

        self.full_heart()

    def full_heart(self):
        """Fun that will desplay itself when all 3 hearts are up"""
        self.image_heart = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\full_hearts.bmp')
        self.heart_rect = self.image_heart.get_rect()
        self.heart_rect.left = self.screen_rect.left + 20
        self.heart_rect.top = 10

    def two_heart(self):
        """Fun that will desplay itself when all 2 hearts are up"""
        self.image_heart = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\two_hearts.bmp')
        self.heart_rect = self.image_heart.get_rect()
        self.heart_rect.left = self.screen_rect.left + 20
        self.heart_rect.top = 10

    def one_heart(self):
        """Fun that will desplay itself when all 1 hearts are up"""
        self.image_heart = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\one_hearts.bmp')
        self.heart_rect = self.image_heart.get_rect()
        self.heart_rect.left = self.screen_rect.left + 20
        self.heart_rect.top = 10

    def zero_heart(self):
        """Fun that will desplay itself when all 1 hearts are up"""
        self.image_heart = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\zero_hearts.bmp')
        self.heart_rect = self.image_heart.get_rect()
        self.heart_rect.left = self.screen_rect.left + 20
        self.heart_rect.top = 10

    def update(self):
        """Update the ship position based on the movment flag"""
                      #the x of right side ship   /the x of the edge of the screen right side
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -=self.settings.ship_speed
        self.rect.x =self.x

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location"""
                    #The source /  the location which keeps changing by the rest of the fun above
        self.screen.blit(self.image, self.rect)

    def show_heart(self):
        """Drawing heart"""
        self.screen.blit(self.image_heart , self.heart_rect)