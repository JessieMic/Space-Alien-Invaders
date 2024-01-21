import pygame.font

class Button:

    def __init__(self, ai_game):
        """Initalize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()


    def main_mode(self):
        self.image = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\start_blank.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def easy_mode(self):
        self.image = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\start_easy.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def medium_mode(self):
        self.image = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\start_mid.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def hard_mode(self):
        self.image = pygame.image.load(r'C:\Users\Jessi\Desktop\AI\data\start_hard.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    #def _prep_msg(self,msg):
        #"""Turn msg into a rendered im age and center text on the button"""
        #                                     This makes it smooth
        #self.msg_image = self.font.render(msg, True , self.text_color, self.button_color)
        #self.msg_image_rect = self.msg_image.get_rect()
        #self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draw blank button then msg
        #Fill surface with solid colors
        #     main surface Draw one image onto another
        self.screen.blit(self.image, self.rect)