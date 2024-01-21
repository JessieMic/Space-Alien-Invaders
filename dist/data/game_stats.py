

class GameStats:
    """Track statistic of the game"""

    def __init__(self, ai_game):
        """Initialize statistic"""
        self.settings = ai_game.settings
        self.reset_stats()

        with open(r'C:\Users\Jessi\Desktop\AI\data\high_score.txt') as high_score:
            h_s =  high_score.read()
        self.high_score = int(h_s)

        # Start Ai in an active state.
        #self.game_active = True
        #Start the game in an invactive state.
        self.game_active = False
        self.game_exit = False


    def reset_stats(self):
        """Initiallize statistics that can be changed during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level =1