import pygame
from config import *


class Rocket(pygame.sprite.Sprite):
    def __init__(self, path_image: str, size: tuple, center: tuple, speed: int = 10):
        super().__init__() 

        self.image = pygame.transform.scale(pygame.image.load(path_image).convert_alpha(), size)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = speed

    def update(self):
        self.rect.x += self.speed * ROCKET_SPEED

