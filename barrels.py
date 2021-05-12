import pygame
from pygame.sprite import Sprite
map = ("map_2.csv")
grid_list = []

class Barrel(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.wall_num = 0
        self.image = pygame.image.load('images/wall1.bmp')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height


        Barrel.calc_walls(self, grid_list)


    def draw_walls(self, map):
        for i in range(len(map)):
            for I in range(len(map[i])):
                if map[i][I] == "1":
                    Barrel._group_walls(self)
                    Barrel.draw_block(self, i,I,"wall")

    def calc_walls(self, map):
        for col in range(len(map)):
            for row in range(len(map[col])):
                if map[col][row] == "1":
                    self.wall_num += 1

    def draw_block(self, row, col, type):
        if type == "wall":
            rect = ((col)*90,(row)*90, 90, 90)
            pygame.draw.rect(self.screen, self.settings.color_1, rect)

    def _group_walls(self):
        if self.barrel.wall_num > len(self.map.walls):
            new_wall = Barrel(self)
            self.map.walls.add(new_wall)