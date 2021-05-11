import sys
import pygame

from settings import Settings
from player import Player
from bomb import Bomb
from map import Map, grid_list

map = ("map.csv")
grid_list = []

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

        self.load_grid_from_file(map)

        self.walls = pygame.sprite.Group()
        self._generate_walls(grid_list)


        self.grid = grid_list


    def run_game(self):
        while True:
            self._check_events()
            self.player.update()
            self._update_screen()
            self._check()

    def _generate_walls(self, map):
        wall = Map(self)
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "1":
                    wall = Map(self)
                    wall.x = 90 * i
                    wall.y = 90 * j
                    wall.rect.x = wall.x
                    wall.rect.y = wall.y
                    self.walls.add(wall)


    def _check_events(self):
        for event in pygame.event.get(): # go through events since last call
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.player.moving_right = self._check_moving_right()
                if event.key == pygame.K_a:
                    self.player.moving_left = self._check_moving_left()
                if event.key == pygame.K_w:
                    self.player.moving_up = self._check_moving_up()
                if event.key == pygame.K_s:
                    self.player.moving_down = self._check_moving_down()
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

    def _check(self):
        self._check_moving_down()
        self._check_moving_up()
        self._check_moving_left()
        self._check_moving_right()

    def _check_moving_right(self):
        rect_2 = self.player

        rect_2.rect.right += self.settings.player_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        else:
            return True

    def _check_moving_left(self):
        rect_2 = self.player

        rect_2.rect.left -= self.settings.player_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        else:
            return True

    def _check_moving_up(self):
        rect_2 = self.player

        rect_2.rect.top -= self.settings.player_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        else:
            return True

    def _check_moving_down(self):
        rect_2 = self.player

        rect_2.rect.bottom += self.settings.player_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        elif rect_2.rect.bottom > 990:
            return False
        else:
            return True


    def _place_bomb(self):
        new_bomb = Bomb(self)
        if len(self.bombs.sprites()) < self.settings.max_bombs:
            self.bombs.add(new_bomb)

    def check_for_colisions(self):
        if pygame.sprite.rect.colliderect(self.player, self.walls, False):
            print("a")
            print ("b")

    def load_grid_from_file(self, name):
        file = open(name)
        for line in file:
            x = line.replace('\n', '')
            grid_list.append(self.split(x))

    def split(self, word):
        return [char for char in word]


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.player.blitme()
        self.walls.draw(self.screen)
        for bomb in self.bombs:
            bomb.place_bomb()
        Map.drawGrid(self)
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    ai = Bomber()
    ai.run_game()
