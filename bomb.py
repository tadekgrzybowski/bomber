import pygame
from pygame.sprite import Sprite

sprites = [ pygame.image.load('images/bomb1.bmp'), pygame.image.load('images/bomb2.bmp') ]

class Bomb(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bomb_phase = 0
        self.image = sprites[self.bomb_phase]
        self.rect = self.rect = self.image.get_rect()
        self.place = True

        
    def bomb_image(self):
        if self.bomb_phase > 5:
            self.image = sprites[1]
            
            
    def tick(self):
       
        self.bomb_phase += 1
        
        if self.bomb_phase > 10:
            self.bomb_phase = 0
        
        self.bomb_image()
        
