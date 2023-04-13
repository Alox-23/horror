import pygame
from Rend.settings import *
import math

class camera:
    def __init__(self):
        self.speed = 0.07
        self.x, self.y = 2.5, 1.5
        self.angle = 90
        self.floor = 0
    def movement(self): 
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        elif keys[pygame.K_RIGHT]:
            self.angle += 0.02
        
        if keys[pygame.K_w]:
            dx = math.cos(self.angle) * self.speed
            dy = math.sin(self.angle) * self.speed
        self.x += dx
        self.y += dy
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

