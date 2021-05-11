import pygame
from pygame.sprite import Sprite
map = ("map.csv")
grid_list = []

class Map(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.wall_num = 0
        self.image = pygame.image.load('images/wall2.bmp')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height


        Map.calc_walls(self, grid_list)


    def drawGrid(self):
        for x in range(0, self.settings.screen_width, self.settings.bomb_width):
            for y in range(0, self.settings.screen_height, self.settings.bomb_height):
                rect = pygame.Rect(x, y, self.settings.bomb_height, self.settings.bomb_width)
                pygame.draw.rect(self.screen, self.settings.color_1, rect, 1)

    def draw_walls(self, map):
        for i in range(len(map)):
            for I in range(len(map[i])):
                if map[i][I] == "1":
                    Map._group_walls(self)
                    Map.draw_block(self, i,I,"wall")

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
        if self.map.wall_num > len(self.map.walls):
            new_wall = Map(self)
            self.map.walls.add(new_wall)

