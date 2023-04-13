import math
import pygame
from Rend.settings import *


class raycasting:

    def __init__(self):
        self.ray_casting_result = {}
        self.objects_to_render = []

    def ray_cast(self, map, cam):
        ray_casting_result = []
        ox, oy = cam.pos
        x_map, y_map = cam.map_pos
        ray_angle = cam.angle - HALF_FOV + 0.0001

        texture_vert, texture_hor = 1, 1
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            #horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in map:
                    texture_hor = map[tile_hor]
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            #verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in map:
                    texture_vert = map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            #depth
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor
                
            #remove fishbowl effect
            depth *= math.cos(cam.angle - ray_angle)
            
            proj_height = SCREEN_DIST / (depth + 0.0001)

            ray_casting_result.append(
                (depth, proj_height, texture, offset))

            ray_angle += DELTA_ANGLE
        return ray_casting_result