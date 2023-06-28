from config import *
import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, file_paths: list, lives,speed_x, sound_bullet, jumping_path, dead_path, character_type) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.frame_index = 0
        
        #loading running animation propperly
        self.file_paths = []
        for i in file_paths:
            image = pygame.image.load(i).convert_alpha()
            image = pygame.transform.scale(image, PLAYER_SIZE)
            self.file_paths.append(image)
        
        self.image = self.file_paths[self.frame_index]
        self.x = x
        self.y = y
        self.lives = lives
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.speed_x = speed_x
        self.speed_y = 0
        
        self.sound_bullet = pygame.mixer.Sound(sound_bullet)
        self.run = True
        self.cooldown_animation = 80
        self.current_time_animations = pygame.time.get_ticks()
        
        self.jumping = False
        self.jumping_img = pygame.image.load(jumping_path).convert_alpha()
        self.jumping_img = pygame.transform.scale(self.jumping_img, PLAYER_SIZE)
        self.character_type = character_type
        
        self.death_img = pygame.image.load(dead_path).convert_alpha()
        self.death_img = pygame.transform.scale(self.death_img, PLAYER_SIZE)
        
        self.action = 0
        self.dead = False
        
    
    def update(self):
        self.update_animations()
        if self.character_type == "enemy":
            if self.lives == 0:
                self.kill()
            self.rect.x -= self.speed_x * ENEMY_SPEED
        self.rect.y += self.speed_y

        if self.rect.bottom >= SCREEN_HEIGHT - FLOOR:   #compruba si la nave no sobrepase el limite izquierdo. Si sobrepasa se ejecuta la siguiente linea de codigo.
            self.rect.bottom = SCREEN_HEIGHT - FLOOR  #Establece la posición izquierda de la nave en 0, evitando que se desplace más hacia la izquierda y se salga de la pantalla.
        elif self.rect.top <= ROOF:  #compruba si la nave no sobrepase el limite derecho. Si sobrepasa se ejecuta la siguiente linea de codigo.
            self.rect.top = ROOF
        
        
        if self.character_type == "player":
            
            self.rect.x += self.speed_x
            if self.rect.x  == 180:
                self.speed_x = 0
            
    
    def shoot(self, sprites, bullets):
        bullet = Bullet(BULLET_PATH, BULLET_SIZE, (self.rect.midright[0], self.rect.midright[1] +5),BULLET_COLLITION, BULLET_SPEED)   #genero la instancia laser
        pygame.mixer.Sound.play(self.sound_bullet)
        sprites.add(bullet)
        bullets.add(bullet)
    
    def update_animations(self):
        if self.jumping == True:
            self.image = self.jumping_img
        else:
            self.jumping = False
            self.image = self.file_paths[self.frame_index]
        if pygame.time.get_ticks() - self.current_time_animations > self.cooldown_animation:
            self.current_time_animations = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index == len(self.file_paths):
            self.frame_index = 0
            
        if self.dead == True:
            self.image = self.death_img

                
            
             
        