import pygame.font

class Scoreboard:
    """A class to report coring information"""

    def __init__(self,ai_game):
        """Initialize scorekeeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font setting for scoring info
        self.text_color = (230,206,71)
        self.font = pygame.font.Font(r'C:\Users\Jessi\Desktop\AI\data\numbers.ttf', 30)
        #self.font = pygame.font.SysFont(None,48)

        #Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Turn score into rendered image"""
        rounded_score = round(self.stats.score , -1 )
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Display score at top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 5

    def prep_high_score(self):
        """Turn highscore into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx= self.screen_rect.centerx - 20
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the image into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Display score at top right
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top =  self.score_rect.top + 50

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image , self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)