import pygame
from pygame.sprite import Sprite
from player import Player

sprites = [ pygame.image.load('images/enemy.bmp')]

class Enemy(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.move_phase = 0
        self.image = sprites[self.move_phase]
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.player = Player(self)
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
          
          
    def advance_image(self):
        if self.move_phase > 5:
            self.image = sprites[0]
        else:
            self.image = sprites[0]
            
    def animate(self):
        self.move_phase += 1
        
        if self.move_phase > 10:
            self.move_phase = 0
        
        self.advance_image()

    
    def blitme(self):
        self.screen.blit(self.image, self.rect)