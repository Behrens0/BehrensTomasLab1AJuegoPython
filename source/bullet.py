import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, path_image: str, size: tuple, center: tuple, bullet_collision, speed: int = 10):   #contructor
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(path_image).convert_alpha(), size)

        self.rect = self.image.get_rect()

        self.rect.center = center

        self.speed = speed

        self.impact = False

        self.bullet_collision =  pygame.transform.smoothscale(pygame.image.load(bullet_collision).convert_alpha(), size)
    def update(self):
        self.speed = self.speed - self.speed *0.008
        self.rect.x += self.speed
