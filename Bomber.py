import sys
import pygame

from settings import Settings
from player import Player
from bomb import Bomb

class Bomber:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # surface
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Bomber")
        
        self.player = Player(self)
        # set background color:
        self.bg_color = self.settings.bg_color

        self.screen_height = self.settings.screen_height

        self.screen_width = self.settings.screen_width
        self.bombs = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.player.update()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get(): # go through events since last call
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.moving_right = True
                if event.key == pygame.K_a:
                    self.player.moving_left = True
                if event.key == pygame.K_w:
                    self.player.moving_up = True
                if event.key == pygame.K_s:
                    self.player.moving_down = True
                if event.key == pygame.K_SPACE:
                    self._place_bomb()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.moving_right = False
                if event.key == pygame.K_a:
                    self.player.moving_left = False
                if event.key == pygame.K_w:
                    self.player.moving_up = False
                if event.key == pygame.K_s:
                    self.player.moving_down = False

    def _place_bomb(self):
        new_bomb = Bomb(self)
        if len(self.bombs.sprites()) < self.settings.max_bombs:
            self.bombs.add(new_bomb)

    def calc_map(self):
        if self.screen_height > self.screen_width:
            self.screen_width /= 11

        elif self.screen_width > self.screen_height:
            self.screen_height /= 11

        elif self.screen_height ==self.screen_width:
            self.screen_height /= 11

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.player.blitme()
        for bomb in self.bombs:
            bomb.place_bomb()
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    ai = Bomber()
    ai.run_game()
