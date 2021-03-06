import pygame
from pygame.sprite import Sprite


class Bomb(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bomb_phase = 0
        self.image = pygame.image.load('images/bomb1.bmp')
        self.rect  = self.image.get_rect()
        self.place = True

        
    def tick(self):
        self.bomb_phase += 1
        if self.bomb_phase > 17:
            self.bomb_phase = 0
