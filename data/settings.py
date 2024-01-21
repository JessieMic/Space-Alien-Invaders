class Settings:
    """A class to store all settings for AI"""

    def __init__(self):
        """Initialize the game's  static settings"""
        #screen settings
        self.screen_width= 1200
        self.screen_hight = 800
        self.bg_color = (60,8,50)

        # Star settings
        self.star_speed = 1.2

        #Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 20
        self.score_scale = 1.2
        self.fleet_drop_speed = 25


        self.initialize_dynamic_settings_medium()


    def initialize_dynamic_settings_easy(self):
        """Initialize settings that change throughout the game"""
        self.alien_points = 5
        self.ship_speed = 2.4
        self.bullet_speed = 3.5
        self.alien_speed = 0.7
        self.bullets_allowed = 6
        self.speedup_scale = 1.2
        self.speedup_scale_ship = 1.1
        self.bullet_width = 5
        #Fleet_direction of 1 represents right; -1 is left
        self.fleet_direction = 1

    def initialize_dynamic_settings_medium(self):
        """Initialize settings that change throughout the game"""
        self.alien_points = 10
        self.ship_speed = 3
        self.bullet_speed = 3.5
        self.alien_speed = 1.1
        self.bullets_allowed = 4
        self.speedup_scale = 1.2
        self.speedup_scale_ship = 1.1
        self.bullet_width = 3
        #Fleet_direction of 1 represents right; -1 is left
        self.fleet_direction = 1

    def initialize_dynamic_settings_hard(self):
        """Initialize settings that change throughout the game"""
        self.alien_points = 30
        self.ship_speed = 3.6
        self.bullet_speed = 3.5
        self.alien_speed = 1.5
        self.bullets_allowed = 3
        self.speedup_scale = 1.2
        self.speedup_scale_ship = 1.2
        self.bullet_width = 2
        #Fleet_direction of 1 represents right; -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        if self.ship_speed < 8:
            self.ship_speed += self.speedup_scale_ship
        if self.bullet_speed < 15:
            self.bullet_speed *= self.speedup_scale
        if self.bullet_width < 10:
            self.bullet_width += 1
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

