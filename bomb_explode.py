import pygame
from pygame.sprite import Sprite


class Bomb_explode(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bomb_phase = 0
        self.image = pygame.image.load('images/bomb2.bmp')
        self.rect  = self.image.get_rect()
        self.place = True