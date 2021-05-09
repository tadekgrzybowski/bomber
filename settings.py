class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 990
        self.screen_height = 990
        self.bg_color = (115, 204, 0)
        self.player_speed = 1
        self.bomb_width = 90
        self.bomb_height = 90
        self.bomb_color = (96,96,96)
        self.max_bombs = 2
        self.bomb_radius = 45
        self.color_1 = (200, 200, 200)
        self.color_2 = (0, 0, 0)
        self.row_width = self.screen_width / 11
        self.col_width = self.screen_width / 11