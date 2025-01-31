import pygame
import sys, os
from collections import deque

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

map_dir = resource_path("img/map")


class Map:
    def __init__(self, game):
        self.game = game
        self.map_list = self.get_map()
        self.map_pos_x, self.map_pos_y = 0, 0
        self.speed_x = 0
        self.x_travelled = abs(0 - self.map_pos_x)

    def get_map(self):
        self.map_tiles = deque()
        for tile in range(4):
            self.tile = pygame.image.load(os.path.join(map_dir, "Path0{}.png".format(tile)))
            self.tile = pygame.transform.scale(self.tile, self.game.get_res())
            self.map_tiles.append(self.tile)

        #print(self.map_tiles)  #debug
        return self.map_tiles

    def get_map_tiles(self):
        pass

    def move_map(self, speed_x): # , speed_x
        self.speed_x = speed_x
        self.map_pos_x -= int(self.speed_x * 500)
        
        pass


    def update(self):
        #self.map_list.rotate(-1)
        #is this updating on tobie?
        #lmk
        pass


    def draw(self):
        self.game.screen.blit(self.map_list[0], (self.map_pos_x, self.map_pos_y))
