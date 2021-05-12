import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/bomb1.bmp')
        self.rect = self.rect = self.image.get_rect()
        self.place = True

    def place_bomb(self):
        if self.place:
            #pygame.draw.circle(self.screen, 0, self.rect.center, self.settings.bomb_radius)
            self.image = pygame.image.load("images/bomb1.bmp")
