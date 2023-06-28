import pygame
from config import *
import random
#defino la clase asteroide para obtener la imagen y rectangulo del asteroide y generar los movimientos
class RotatingTrap(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, zappers_path1, zappers_path2, zappers_path3, zappers_path4):
        super().__init__()
        self.zapper_instance = random.randrange(1, 5)
        match self.zapper_instance:
            case 1:
                self.zappers = zappers_path1
                self.zapper_speed = 2
            case 2:
                self.zappers = zappers_path2
                self.zapper_speed = 25
            case 3:
                self.zappers = zappers_path3
                self.zapper_speed = 25
            case 4:
                self.zappers = zappers_path4
                self.zapper_speed = 25
        self.x = x
        self.y = y
        self.frame_index = 0
        self.angle = 0
        self.speed = speed
        self.image = self.zappers[self.frame_index]
        self.rect = self.image.get_rect()
        self.counter = 0
        self.rect.center = (x, y)
        self.collided = False
        
        
    def update(self):
        self.counter += 1
        self.rect.x += self.speed
        if self.counter >= self.zapper_speed:
            self.counter = 0
            self.frame_index += 1
            if self.frame_index == len(self.zappers):
                self.frame_index = 0
            else:
                self.image = self.zappers[self.frame_index]
                