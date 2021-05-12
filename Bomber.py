import sys
import pygame

from settings import Settings
from player import Player
from bomb import Bomb
from map import Map, grid_list
from enemy import Enemy
from barrels import Barrel
from bomb_explode import Bomb_explode

clock = pygame.time.Clock()

map = ("map.csv")
map_2 = ("map_2.csv")
grid_list = []
grid_list_2 = []

class Bomber:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # surface
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Bomber")
        
        self.player = Player(self)
        self.map = Map(self)
        self.barrel = Barrel(self)
        self.bomb = Bomb(self)
        self.enemy = Enemy(self)
        self.bomb_explode = Bomb_explode(self)

        # set background color:
        self.bg_color = self.settings.bg_color

        self.screen_height = self.settings.screen_height

        self.screen_width = self.settings.screen_width
        self.bombs = pygame.sprite.Group()
        self.bombs_explode = pygame.sprite.Group()

        self.load_grid_from_file(map)
        self.load_grid_from_file_2(map_2)

        self.walls = pygame.sprite.Group()
        self._generate_walls(grid_list)

        self.barrels = pygame.sprite.Group()
        self._generate_barrels(grid_list_2)

        self.bomb_signal = False

        self.grid = grid_list
        

        self.blitme_explosion_signal = False

        self.new_bomb_rect = 0


    def run_game(self):
        while True:
            self._check_events()
            self.player.update()
            self.enemy.update()
            self._update_screen()
            self._bomb_calc()
            self._update_screen()
            self.check_for_destroyed_barrels()
            clock.tick(10)


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

    def _generate_barrels(self, map):
        barrel = Barrel(self)
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "1":
                    wall = Barrel(self)
                    wall.x = 90 * i
                    wall.y = 90 * j
                    wall.rect.x = wall.x
                    wall.rect.y = wall.y
                    self.barrels.add(wall)


    def _bomb_calc(self):
        if self.bomb_signal:
            self.bomb.tick()
        if self.bomb.bomb_phase == 10:
            self.bombs.empty()
        if self.bomb.bomb_phase > 10:
            self._place_bomb_explode()
        if self.bomb.bomb_phase == 15:
            self.bomb.bomb_phase = 0
            self.bomb_signal = False
            self.bombs.empty()
            self.bombs_explode.empty()


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
                if event.key == pygame.K_RIGHT:
                    self.enemy.moving_right = self._try_moving_right()
                if event.key == pygame.K_LEFT:
                    self.enemy.moving_left = self._try_moving_left()
                if event.key == pygame.K_UP:
                    self.enemy.moving_up = self._try_moving_up()
                if event.key == pygame.K_DOWN:
                    self.enemy.moving_down = self._try_moving_down()
                    self.bomb_signal =True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.player.moving_right = False
                if event.key == pygame.K_a:
                    self.player.moving_left = False
                if event.key == pygame.K_w:
                    self.player.moving_up = False
                if event.key == pygame.K_s:
                    self.player.moving_down = False
                if event.key == pygame.K_RIGHT:
                    self.enemy.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.enemy.moving_left = False
                if event.key == pygame.K_UP:
                    self.enemy.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.enemy.moving_down = False


    def _check_moving_right(self):
        rect_2 = self.player

        rect_2.rect.right += self.settings.player_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        elif pygame.sprite.sprtecolideany(rect_2, self.barrels):
            return False
        else:
            return True

    def _check_moving_left(self):
        rect_2 = self.player

        rect_2.rect.left -= self.settings.player_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        elif pygame.sprite.sprtecolideany(rect_2, self.barrels):
            return False
        else:
            return True

    def _check_moving_up(self):
        rect_2 = self.player

        rect_2.rect.top -= self.settings.player_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        elif pygame.sprite.sprtecolideany(rect_2, self.barrels):
            return False
        else:
            return True

    def _check_moving_down(self):
        rect_2 = self.player

        rect_2.rect.bottom += self.settings.player_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        elif pygame.sprite.sprtecolideany(rect_2, self.barrels):
            return False
        else:
            return True
        
    def _try_moving_right(self):
        rect_2 = self.enemy

        rect_2.rect.right += self.settings.enemy_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        elif pygame.sprite.sprtecolideany(rect_2, self.barrels):
            return False
        else:
            return True

    def _try_moving_left(self):
        rect_2 = self.enemy

        rect_2.rect.left -= self.settings.enemy_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        elif pygame.sprite.sprtecolideany(rect_2, self.barrels):
            return False
        else:
            return True

    def _try_moving_up(self):
        rect_2 = self.enemy

        rect_2.rect.top -= self.settings.enemy_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        elif pygame.sprite.sprtecolideany(rect_2, self.barrels):
            return False
        else:
            return True

    def _try_moving_down(self):
        rect_2 = self.enemy

        rect_2.rect.bottom += self.settings.enemy_speed

        if pygame.sprite.spritecollideany(rect_2, self.walls):
            return False
        elif pygame.sprite.sprtecolideany(rect_2, self.barrels):
            return False
        else:
            return True


    def _place_bomb(self):
        new_bomb = Bomb(self)
        if len(self.bombs.sprites()) < self.settings.max_bombs:
            new_bomb.rect.center = self.player.rect.center
            self.bomb_location = new_bomb.rect
            self.bomb_location_center = new_bomb.rect.center
            self.bombs.add(new_bomb)

    def _place_bomb_explode(self):
        new_bomb = Bomb_explode(self)
        if len(self.bombs_explode.sprites()) < self.settings.max_bombs:
            new_bomb.rect.center = self.bomb_location_center
            self.bomb_location = new_bomb.rect
            self.bombs_explode.add(new_bomb)

    def check_for_destroyed_barrels(self):
        pygame.sprite.groupcollide(self.bombs_explode, self.barrels, False, True)

        pygame.sprite.spritecollide(self.player, self.bombs_explode, False)


    def load_grid_from_file(self, name):
        file = open(name)
        for line in file:
            x = line.replace('\n', '')
            grid_list.append(self.split(x))

    def load_grid_from_file_2(self, name):
        file = open(name)
        for line in file:
            x = line.replace('\n', '')
            grid_list_2.append(self.split(x))

    def split(self, word):
        return [char for char in word]


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.player.blitme()
        self.enemy.blitme()
        self.walls.draw(self.screen)
        self.bombs.draw(self.screen)
        self.barrels.draw(self.screen)
        self.bombs_explode.draw(self.screen)


        Map.drawGrid(self)
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    ai = Bomber()
    ai.run_game()
