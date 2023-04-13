import pygame
from Rend.settings import *


class object_renderer:

    def __init__(self, screan):
        self.screan = screan
        self.textures = self.load_wall_textures()

    def get_objects_to_render(self, obj, map):
        self.objects_to_render = []
        floor = len(map) - 1
        for i in range(len(map)):
            for ray, values in enumerate(obj[floor]):
                depth, proj_height, texture, offset = values

                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE)
                wall_column = pygame.transform.scale(wall_column,
                                                     (SCALE, proj_height))
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 1.4 -
                            (HALF_HEIGHT // 4) - (floor * proj_height))

                self.objects_to_render.append((depth, wall_column, wall_pos))
            floor -= 1

    def draw(self):
        self.render_game_objects()

    def render_game_objects(self):
        for depth, img, pos in self.objects_to_render:
            self.screan.blit(img, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('wall.png'),
        }
