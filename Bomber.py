import sys
import pygame

from settings import Settings
from player import Player
from bomb import Bomb
from map import Map, grid_list


class Bomber:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # surface
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Bomber")
        
        self.player = Player(self)
        self.map = Map(self)
        # set background color:
        self.bg_color = self.settings.bg_color

        self.screen_height = self.settings.screen_height

        self.screen_width = self.settings.screen_width
        self.bombs = pygame.sprite.Group()

        self.grid = grid_list


    def run_game(self):
        while True:
            self._check_events()
            self.player.update()
            self.check_for_colisions()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get(): # go through events since last call
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.moving_right = self._check_moving_right()
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

    def _check_moving_right(self):
        if self.player.rect.right + self.settings.player_speed

    def _place_bomb(self):
        new_bomb = Bomb(self)
        if len(self.bombs.sprites()) < self.settings.max_bombs:
            self.bombs.add(new_bomb)

    def check_for_colisions(self):
        if pygame.sprite.spritecollide(self.player, self.map.walls, False):
            print("a")
            print ("b")


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.player.blitme()
        for bomb in self.bombs:
            bomb.place_bomb()
        Map.drawGrid(self)
        Map.draw_walls(self, self.grid)
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    ai = Bomber()
    ai.run_game()
