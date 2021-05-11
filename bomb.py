import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.rect = pygame.Rect(0, 0, self.settings.bomb_width, self.settings.bomb_height)
        self.rect.midtop = ai_game.player.rect.midtop
        self.place = True

    def place_bomb(self):
        if self.place:
            pygame.draw.circle(self.screen, 0, self.rect.center, self.settings.bomb_radius)

