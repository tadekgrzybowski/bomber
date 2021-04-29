import pygame
from pygame.sprite import Sprite

class Bomb(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.rect = pygame.Rect(0, 0, self.settings.bomb_width, self.settings.bomb_height)
        self.rect.midtop = ai_game.player.rect.midtop

    def place_bomb(self):
        pygame.draw.circle(self.screen, 0, self.rect.midbottom, self.settings.bomb_radius)

