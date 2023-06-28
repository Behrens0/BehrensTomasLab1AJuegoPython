import pygame
from config import *
class Alert(pygame.sprite.Sprite):
    def __init__(self, image: str, x: int, y: int):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, ALERT_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.y = y
        self.x = x