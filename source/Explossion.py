import pygame
from config import *

class Explossion(pygame.sprite.Sprite):
    def __init__(self, file_paths: list, center: tuple):
        super().__init__()

        self.file_paths = file_paths
        
        
        self.frame_index = 0
        self.image = self.file_paths[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.impact = False
        self.counter = 0

    
    def update(self):
        explosion_speed = 10
        self.counter += 1

        if self.counter >= explosion_speed:
            self.counter += 1
            self.frame_index += 1
            if self.frame_index == len(self.file_paths):
                self.kill()
            else:
                self.image = self.file_paths[self.frame_index]
