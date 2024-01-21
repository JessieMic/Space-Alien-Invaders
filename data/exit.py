import pygame

class Exit:
    """Class that handles the rect of the exit button"""

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\exit.bmp')
        self.image = pygame.transform.scale(self.image, (314,326))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def draw_exit(self):
        """Draws exit menu on screen"""
        self.screen.blit(self.image, self.rect)
