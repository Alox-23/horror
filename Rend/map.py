import pygame
from Rend.settings import *

class map:

    def __init__(self):
        self.world_map = {}
        self.mini_map = []

    def set_size(self, x, y, z):
        self.mini_map = []
        for i in range(z):
            floor = []
            for y in range(y+1):
                row = []
                for x in range(x+1):
                    row.append(0)
                floor.append(row)
            self.mini_map.append(floor)
            
    def add(self, x, y, z, item):
        self.mini_map[z][y][x] = item

    def update(self):
        for floor_num, floor in enumerate(self.mini_map):
            self.world_map[floor_num] = {}
            for j, row in enumerate(floor):
                for i, value, in enumerate(row):
                    if value != 0:
                        self.world_map[floor_num][(i, j)] = value

    def import_map(self, mini_map):
        self.mini_map = mini_map