"""Module for GameStats"""

class Gamestats:
    """track statistics for the game"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that change during game"""
        self.livesleft = self.ai_settings.total_lives

