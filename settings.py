class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 990
        self.screen_height = 990
        self.bg_color = (115, 204, 0)
        self.player_speed = 1
        self.bomb_width = 9
        self.bomb_height = 9
        self.bomb_color = (60,60,60)
        self.max_bombs = 2
        self.bomb_radius = 45