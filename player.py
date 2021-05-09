import pygame
from pygame.sprite import Sprite

sprites = [ pygame.image.load('images/bomber1.bmp'), pygame.image.load('images/bomber2.bmp') ]

class Player(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.move_phase = 0
        self.image = sprites[self.move_phase]
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

              
    def advance_image(self):
        if self.move_phase > 5:
            self.image = sprites[1]
        else:
            self.image = sprites[0]
            
    def animate(self):
        self.move_phase += 1
        
        if self.move_phase > 10:
            self.move_phase = 0
        
        self.advance_image()

        
    def update(self):
            
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
            self.animate()
            
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
            self.animate()
            
        if self.moving_up and self.y > 0:
            self.y -= self.settings.player_speed
            self.animate()
            
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.player_speed
            self.animate()
            
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

        