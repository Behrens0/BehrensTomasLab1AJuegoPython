import pygame
from config import *

#defino la clase asteroide para obtener la imagen y rectangulo del asteroide y generar los movimientos
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, laser_fire, laser_charge, laser_inactive, laser_charge_sound, laser_fire_sound):
        super().__init__()
        self.x = x
        self.y = y
        self.frame_index = -1
        self.angle = 0
        self.lasers_fire = laser_fire
        self.laser_charge = laser_charge
        self.laser_inactive = laser_inactive
        self.flag = True
        self.image = pygame.image.load(self.laser_inactive).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, LASER_SIZE)
        self.rect = self.image.get_rect()
        self.counter = 0
        self.rect.center = (self.x, self.y)
        self.charge = False
        self.fire = False
        self.inactive = True
        self.counter_fire = 40
        self.laser_charge_sound = pygame.mixer.Sound(laser_charge_sound)
        self.laser_fire_sound = pygame.mixer.Sound(laser_fire_sound)
        self.laser_start_sound = pygame.mixer.Sound(LASER_START_SOUND)
        self.laser_stop_sound = pygame.mixer.Sound(LASER_STOP_SOUND)
        self.laser_ended = False
        self.flag_sound = True
        self.channel2 = pygame.mixer.Channel(1)
        self.channel3 = pygame.mixer.Channel(2)

    def update(self):
        turn_speed_fire = 70
        turn_speed_charge = 60
        
        if self.fire:
            self.counter_fire += 1
            if self.counter_fire >= turn_speed_fire:
                
                self.frame_index += 1
                if self.frame_index == 0:
                    self.laser_fire_sound.play()
                
                
                
                self.counter_fire = 0
                if self.frame_index == len(self.lasers_fire):
                    self.fire = False
                    self.charge = False
                    self.flag = False
                    self.laser_ended= True
                    if self.flag_sound:
                        self.channel2.play(self.laser_stop_sound)
                        self.flag_sound = False
                elif self.frame_index >= 0:
                    
                    self.image = self.lasers_fire[self.frame_index]
        
        elif self.charge:
            self.counter += 1
            if self.counter >= turn_speed_charge:
                self.frame_index += 1
                self.counter = 0
                if self.frame_index == 0:
                    self.y = self.y - 20
                    self.laser_charge_sound.play()
                
                if self.frame_index >= len(self.laser_charge):
                    self.frame_index = -1
                    self.charge = False
                    self.fire = True
                
                elif self.frame_index >= 0:
                    self.image = self.laser_charge[self.frame_index]
                self.rect.center = (self.x, self.y)
                
                
                
            