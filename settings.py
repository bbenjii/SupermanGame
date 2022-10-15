"""Module for setting attributes"""

class Settings():
    """A class to store all game settings"""

    def __init__(self):
        # Initialize static game settings
        self.screen_width = 1300
        self.screen_height = 800
        self.screen_dimensions = (self.screen_width, self.screen_height)
        self.background_color = (135, 206, 235)

        # Number of lives
        self.total_lives = 5

        # Laser settings
        self.laser_speed = 3

        #speedup scale
        self.speedup_scale = 1.1

        self.setup_dynamic_settings()

    def setup_dynamic_settings(self):
        """initialize dynamic settings
        that change throughout the game"""
        self.superman_speed = 4
        self.kryptonite_speed = 1.5

    def increase_speed(self):
        """speedup the game after
        each level is cleared"""
        self.superman_speed *= self.speedup_scale
        self.kryptonite_speed *= self.speedup_scale
