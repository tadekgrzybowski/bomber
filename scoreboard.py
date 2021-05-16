import pygame
import pygame.font

class Scoreboard():
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
