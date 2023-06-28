import pygame, sys
import random
from config import *
from PlayerClass import Player
from rocket import Rocket
from AlertClass import Alert
from Explossion import Explossion
from ZapperClass import RotatingTrap
from Laser import Laser
from Button import Button

class Game:
    def __init__(self, screen_width: int, screen_height: int, title: str,background_entry_img: str, background_img: str, player_imgs: list, background_music: str, jetpack_start: str, jetpack_stop: str, jetpack_fire: str, land_metal_sound: str, start_image: str, exit_image: str, menu_button:str, pause_image: str, unpause_button: str, options_button: str, hard_button: str, back_button: str):
        pygame.init()
        
        

        self.barry_images = player_imgs
        
        #score
        self.score = 0
        self.score_speed = 50
        self.best_score = 0
        #play game
        self.playing = False

        
        #setting up screen
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
        #game title
        pygame.display.set_caption(title)
        
        #fonts
        self.fuente = pygame.font.SysFont("Arial", 38)
        self.score_font = pygame.font.SysFont("comicsans", 40)
        
        #loading background images
        self.background_entry = pygame.image.load(background_entry_img).convert_alpha()
        self.background_entry = pygame.transform.smoothscale(self.background_entry, (screen_width , screen_height))
        self.background_entry_rect = self.background_entry.get_rect()
        self.background = pygame.image.load(background_img).convert_alpha()
        self.background = pygame.transform.smoothscale(self.background, (screen_width , screen_height))
        self.background_rect = self.background.get_rect()
        
        self.game_over_img = pygame.image.load(GAME_OVER_IMG).convert_alpha()
        self.game_over_img = pygame.transform.smoothscale(self.game_over_img, (400, 200))
        
        #loading groups
        self.sprites = pygame.sprite.Group()
        self.rockets = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.alerts = pygame.sprite.Group()
        self.explossions = pygame.sprite.Group()
        self.zappers = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.barrys = pygame.sprite.Group()
        
        #loading buttons
        self.button_img = pygame.image.load(start_image).convert_alpha()
        self.start_button = Button(screen_width // 2 - self.button_img.get_width() // 2, 0, self.button_img, 1)
        
        self.exit_img = pygame.image.load(exit_image).convert_alpha()
        self.exit_button = Button(screen_width // 2 - self.exit_img.get_width() // 2, screen_height - self.exit_img.get_height(), self.exit_img, 1)
        
        
        self.menu_img = pygame.image.load(menu_button).convert_alpha()
        self.menu_button = Button(screen_width -200, screen_height - self.menu_img.get_height() // 2 - 50, self.menu_img, 2)
        
        self.pause_img = pygame.image.load(pause_image).convert_alpha()
        self.pause_button = Button(screen_width - self.pause_img.get_width() * 0.8, 0, self.pause_img, 0.8)
        
        self.unpause_img = pygame.image.load(unpause_button).convert_alpha()
        self.unpause_button = Button(screen_width - 200, 0, self.unpause_img, 0.7)
        
        self.options_img = pygame.image.load(options_button).convert_alpha()
        self.options_button = Button(screen_width // 2 - self.options_img.get_width() // 2, screen_height // 2 - self.options_img.get_height() // 2, self.options_img, 1)
        
        
        self.hard_img = pygame.image.load(hard_button).convert_alpha()
        self.hard_button = Button(screen_width // 2 - self.hard_img.get_width() // 2 - 170, SCREEN_HEIGHT // 2 - self.hard_img.get_height() // 2, self.hard_img, 0.5)
        
        self.back_img = pygame.image.load(back_button).convert_alpha()
        self.back_button = Button(screen_width // 2 - self.back_img.get_width() // 2 - 290, SCREEN_HEIGHT // 2 - self.back_img.get_height() + 100, self.back_img, 1)
        
        #player
        self.barry = Player(0, screen_height // 2, self.barry_images, BARRY_LIVES, BARRY_SPEED, BULLET_SOUND, JUMPING_PATH_BARRY, DEATH_PATH_BARRY, "player")
        self.sprites.add(self.barry)
        
        
        
        self.last_laser_time = 0
        self.last_zapper_time = 0
        self.last_rocket_time = 0
        self.last_track_position = 0
        self.last_enemie = 0
        self.last_time_fire = 0
        self.last_run_sound = 0
        
        #variable to save the scrolling if the player pauses the game
        self.background_scroll2 = 0
        
        #controll how much time is spent on pause and menu
        self.last_time = 0
        self.pause_time = 0
        
        #handle gravity
        self.gravity = 1.7
        self.fall_count = 0
        self.jump_count = 0
        
        #handle scrolling
        self.bgX = 0
        self.bgX2 = self.background.get_width()
        self.background_scroll = SCROLL_SPEED
        
        #handle delays
        self.laser_delay = 2000
        self.zapper_time_wait = ZAPPER_TIME_WAIT
        self.rocket_time_wait = ROCKET_TIME_WAIT
        
        self.enemy_lives = ENEMY_LIVES
        
        #loading sounds
        self.jet_start_sound = pygame.mixer.Sound(jetpack_start)
        self.jet_fire_sound = pygame.mixer.Sound(jetpack_fire)
        self.jet_stop_sound = pygame.mixer.Sound(jetpack_stop)
        self.fall_sound = pygame.mixer.Sound(land_metal_sound)
        self.run_metal_sound1 = pygame.mixer.Sound(RUN_METAL_SOUND1)
        self.run_metal_sound2 = pygame.mixer.Sound(RUN_METAL_SOUND2)
        self.run_metal_sound3 = pygame.mixer.Sound(RUN_METAL_SOUND3)
        self.run_metal_sound4 = pygame.mixer.Sound(RUN_METAL_SOUND4)
        self.sound = pygame.mixer.Sound(MISSILE_WARNING_SOUND)
        self.sound2 = pygame.mixer.Sound(MISSILE_TAKES_OFF)
        pygame.mixer.music.load(background_music)
        pygame.mixer.set_num_channels(30)
        pygame.mixer.music.play(-1) 
        self.channel1 = pygame.mixer.Channel(0)
        
        
        
        
        #setting up flags
        self.laser_flag = False
        self.space_pressed = False
        self.jetpack_playing = False
        self.background_entry_flag = True
        self.score_adjusted = False
        self.scroll_adjusted = False
        self.start_game = False
        self.pause_game = False
        self.flag_rocket_warning = True
        self.flag_rocket = True
        self.difficulty_adjusted = False
        self.flag_options = False
        self.flag_highest_score = True

    def reset_game(self):
        self.sprites.empty()
        self.rockets.empty()
        self.bullets.empty()
        self.enemies.empty()
        self.alerts.empty()
        self.explossions.empty()
        self.zappers.empty()
        self.lasers.empty()
        self.barrys.empty()
        
        self.score = 0
        self.laser_flag = False
        self.space_pressed = False
        self.jetpack_playing = False
        self.background_entry_flag = True
        self.score_adjusted = False
        self.scroll_adjusted = False
        self.start_game = False
        self.pause_game = False
        self.flag_rocket_warning = True
        self.flag_rocket = True
        self.difficulty_adjusted = False
        self.flag_options = False
        
        self.enemy_lives = ENEMY_LIVES
        
        self.last_laser_time = 0
        self.last_zapper_time = 0
        self.last_rocket_time = 0
        self.last_track_position = 0
        self.last_enemie = 0
        self.last_time_fire = 0
        self.last_run_sound = 0
        
        self.fall_count = 0
        self.jump_count = 0
        
        self.background_scroll2 = 0
        
        self.bgX = 0
        self.bgX2 = self.background.get_width()
        self.background_scroll = SCROLL_SPEED
        
        self.barry = Player(0, SCREEN_HEIGHT // 2, self.barry_images, BARRY_LIVES, BARRY_SPEED, BULLET_SOUND, JUMPING_PATH_BARRY, DEATH_PATH_BARRY, "player")
        self.sprites.add(self.barry)
        
        self.zapper_time_wait = ZAPPER_TIME_WAIT
        self.rocket_time_wait = ROCKET_TIME_WAIT
        
        self.last_time = 0
        self.pause_time = 0

        self.score_speed = 10
    
    def load_csv_score(self):
        """
    Loads the score data from a CSV file, compares it with the current score, updates the best score if necessary,
    and saves the best score back to the CSV file. Prints error messages if any issues occur during file operations.
    """
        try:
            with open("Score.csv", "r") as file:
                    
                    for i in file:
                        if self.score > int(i):
                            self.best_score = self.score
                        
                            
        except Exception:
            print("No se pudo abrir el archivo")
        
        try:
            with open("Score.csv", "w") as file:
                    file.write(str(self.best_score))
        except Exception:
            print("No se pudo guardar el archivo")
        
    def menu(self):
        pygame.mixer.music.set_volume(0.1)
        self.handle_events()
        self.screen.blit(self.background_entry, ORIGIN)
        if not self.flag_options:
            if self.start_button.draw(self.screen):
                self.start_game = True
            if self.exit_button.draw(self.screen):
                self.exit()
            if self.options_button.draw(self.screen):
                self.flag_options = True
        if self.flag_options == True:
            if self.hard_button.draw(self.screen):
                self.background_scroll = -5
                self.rocket_time_wait = 5000
                self.flag_options = False
            if self.back_button.draw(self.screen):
                self.flag_options = False
        
        self.last_time = pygame.time.get_ticks() 
        
        pygame.display.flip()
    
    def game_over(self):
        pygame.mixer.music.set_volume(0.1)
        self.load_csv_score()
        self.handle_events()
        self.screen.blit(self.background, ORIGIN)
        self.screen.blit(self.game_over_img, (SCREEN_WIDTH // 2 - self.game_over_img.get_width() // 2, SCREEN_HEIGHT // 2 - self.game_over_img.get_height()))
        new_font2 = self.score_font.render(f"Enter to continue ", 1, (255, 255, 255))
        self.screen.blit(new_font2, (SCREEN_WIDTH // 2 - new_font2.get_width() // 2, SCREEN_HEIGHT - new_font2.get_height() - 100))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            
            self.reset_game()
            
        pygame.display.flip()
    
    def pause_screen(self):
        pygame.mixer.music.set_volume(0.2)
        self.handle_events()
        for enemy in self.enemies:
            enemy.speed_x = 0
        self.background_scroll = 0
        self.pause_time = pygame.time.get_ticks() - self.current_time
        
            
        self.screen.blit(self.background, (self.bgX, 0))
        self.screen.blit(self.background, (self.bgX2, 0))
        new_font = self.score_font.render(f"Score: {self.score}", 1, (255, 255, 255))
        
        self.screen.blit(new_font, ORIGIN)
        
        if self.unpause_button.draw(self.screen):
            self.pause_game = False
            self.background_scroll = self.background_scroll2
            for enemie in self.enemies:
                enemie.speed_x = self.background_scroll2
        if self.menu_button.draw(self.screen):
            self.load_csv_score()
            self.reset_game()
            
        self.sprites.draw(self.screen)
        pygame.display.flip()


    def start(self):
        try:
            with open("Score.csv", "w") as file:
                file.write(str(self.best_score))
        except Exception as e :
            print("No se pudo guardar el archivo")
            print(e)
            
        self.playing = True
        while self.playing:
            
            if self.start_game == False:
                self.menu()
            
            elif self.barry.dead == False and self.pause_game == False and self.start_game == True:
                pygame.mixer.music.set_volume(0.5)
                
                self.clock = pygame.time.Clock()
                self.clock.tick(FPS)
                
                self.current_time = pygame.time.get_ticks()  - self.last_time - self.pause_time
                
                self.background_scroll2 = self.background_scroll
                
                self.handle_events()
                self.handle_running()
                
                self.handle_score()
                
                self.handle_scrolling()
                

                self.actualizar_elementos()

                self.render_screen()
            
            elif self.barry.dead == True:
                self.game_over()
            
            elif self.pause_game:
                self.pause_screen()
    
    def jump(self):
        """
    Initiates a jump for the character. Sets the jumping flag to True, updates the vertical speed to move the character
    upward, and increments the jump count.
    """
        self.barry.jumping = True
        self.barry.speed_y = -self.gravity * 2.5
        self.jump_count += 1
        
    
    def handle_running(self):
        """
    Handles the running sound effect for the character. Plays the running sound effect at specific intervals
    when the character is not jumping.
    """
        if self.current_time - self.last_run_sound >= DELAY_RUN and self.barry.jumping == False:
            self.run_metal_sound1.play()
            self.last_run_sound = self.current_time
        
        if self.current_time - self.last_run_sound >= DELAY_RUN and self.barry.jumping == False:
            self.run_metal_sound2.play()
            self.last_run_sound = self.current_time
        if self.current_time - self.last_run_sound >= DELAY_RUN and self.barry.jumping == False:
            self.run_metal_sound3.play()
            self.last_run_sound = self.current_time
        if self.current_time - self.last_run_sound >= DELAY_RUN and self.barry.jumping == False:
            self.run_metal_sound4.play()
            self.last_run_sound = self.current_time
    
    def handle_score(self):
        """
    Handles the scoring mechanism in the game. Increases the score at a specific score speed interval,
    and adjusts the score speed based on specific conditions.
    """
        if self.score_speed> 0:
            if self.current_time % self.score_speed == 0:
                if not self.score_adjusted:
                    self.score +=1

            else:
                self.score_adjusted = False
    
    def pause(self):
        """
    Pauses the game when the pause button is clicked. Sets the `pause_game` flag to True.
    """
        if self.pause_button.draw(self.screen):
            self.pause_game = True
                
    def handle_difficulty_over_time(self):
        """
    Adjusts the game difficulty over time based on the player's score.
    """
        if self.current_time > 10:
            if self.score % 100 == 0:
                if not self.difficulty_adjusted:
                    if self.rocket_time_wait >=3000:
                        self.rocket_time_wait -= 500
                    if self.zapper_time_wait >= 1000:
                        self.zapper_time_wait -= 200
                    self.difficulty_adjusted = True
                    self.enemy_lives += 1
            else:
                self.difficulty_adjusted = False
    
    def handle_scrolling(self):
        """
    Handles the scrolling of the background in the game.
    """
        if self.current_time > 10:
            if self.current_time % 150 == 0:
                if not self.scroll_adjusted:
                    self.background_scroll -= 0.1
                    self.scroll_adjusted = True
            else:
                self.scroll_adjusted = False
            
        self.bgX += self.background_scroll
        self.bgX2 += self.background_scroll
        if self.bgX < self.background.get_width() * -1:
            self.bgX = self.background.get_width()
        if self.bgX2 < self.background.get_width() * -1:
            self.bgX2 = self.background.get_width()
     
    def handle_gravity(self):
        """
    Handles the gravity effect on the character in the game.
    """
        
        self.barry.speed_y += min(0.4, (self.fall_count / FPS) * self.gravity)
        self.fall_count += 1 

        if self.current_time - self.last_time_fire < 30 and self.barry.rect.y < SCREEN_HEIGHT -FLOOR and self.barry.rect.y > SCREEN_HEIGHT -FLOOR - 40:
            self.fall_sound.play()
    
    def handle_events(self):
        """
    Handles the events in the game, such as keyboard inputs and game window events.
    """
        
        keys = pygame.key.get_pressed()
        self.pause()
        if keys[pygame.K_SPACE]:
            self.jump()
            self.last_run_sound = self.current_time
            if not self.space_pressed:
                self.jet_start_sound.play()
                self.space_pressed = True
                self.jetpack_playing = True
        elif self.space_pressed:
            self.jet_stop_sound.play()
            self.space_pressed = False
            self.jetpack_playing = False 
            
            
        if self.jetpack_playing and self.current_time - self.last_time_fire >= DELAY_JETPACK_SOUND:
            self.last_time_fire = self.current_time
            self.channel1.play(self.jet_fire_sound)
            self.jet_fire_sound.set_volume(0.3)

        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.barry.shoot(self.sprites, self.bullets)
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.barry.jumping = False
                    self.jet_fire_sound.stop()
                    # self.jet_stop_sound.play()
               

    def actualizar_elementos(self):
        self.generate_laser()
        if self.laser_flag == False:
            self.generate_rockets()
            self.generate_enemies(MAX_ENEMIES)
            self.generate_zapper()
        self.handle_difficulty_over_time()
        self.handle_gravity()
        self.handle_collisions()
        self.sprites.update()
       
    def handle_collision_rockets(self):
        """
    Handles the collision between the player character and rockets.
    """
        for rocket in self.rockets:
            if rocket.rect.right <= 0: 
                rocket.kill() 
            else:
                if pygame.Rect.colliderect(self.barry.rect, rocket.rect):
                    explossion = Explossion(EXPLOSSIONS_LIST, (self.barry.rect.x +20, rocket.rect.y))
                    self.sprites.add(explossion)
                    # self.explossions.draw(self.screen)
                    rocket.kill()
                    self.barry.lives -= 1
    
    def handle_collision_enemies(self):
        """
    Handles the collision between the player character and enemies.
    """
        for enemy in self.enemies:
            if enemy.rect.right <= 0:
                enemy.kill()
            else:
                if pygame.Rect.colliderect(self.barry.rect, enemy.rect):
                    enemy.kill()
                    self.barry.lives -= 1
    
    def handle_collision_bullets(self):
        """
    Handles the collision between the enemie character and bullets.
    """
        for bullet in self.bullets: 
            if bullet.rect.left >= SCREEN_WIDTH: 
                bullet.kill()  
            else:
                list = pygame.sprite.spritecollide(bullet, self.enemies, False) 
                self.screen.blit(bullet.bullet_collision, bullet.rect.center)
                
                if len(list) != 0:
                    for i in list:
                        i.lives -=1
                    bullet.kill()
    
    def handle_collision_zappers(self):
        """
    Handles the collision between the player character and zappers.
    """
        for zapper in self.zappers:
            zapper.speed = self.background_scroll
            if zapper.rect.right <= 0:
                zapper.kill()
            else:
                if pygame.Rect.colliderect(self.barry.rect, zapper.rect):
                    if not zapper.collided:
                        self.barry.lives -= 1
                        zapper.kill()
                        zapper.collided = True
    
    
    def handle_collision_lasers(self):
        """
    Handles the collision between the player character and lasers.
    """
        for laser in self.lasers:
            if pygame.Rect.colliderect(self.barry.rect, laser.rect) and laser.fire == True and laser.frame_index >= 0:
                self.barry.lives = 0
    
    def handle_game_over(self):
        if self.barry.dead:
            self.background_scroll = 0


    def handle_collisions(self):
        if self.barry.lives == 0:
            self.barry.dead = True
            self.background_scroll = 0
        
        self.handle_collision_rockets()

        
        self.handle_collision_enemies()
        
        self.handle_collision_bullets()
        
        self.handle_collision_zappers()
        
        self.handle_collision_lasers()
    
    def render_screen(self):
        """
    Renders the game screen.
    """
        self.screen.blit(self.background, (self.bgX, 0))
        self.screen.blit(self.background, (self.bgX2, 0))
        new_font = self.score_font.render(f"Score: {self.score}", 1, (255, 255, 255))
        best_score_text = self.score_font.render(f"Best Score: {self.best_score}", 1, (0, 100, 0))
        self.screen.blit(new_font, ORIGIN)
        self.screen.blit(best_score_text, (300, 0))
        # self.screen.blit(self.pause_img, (SCREEN_WIDTH-  self.pause_img.get_width(), 0))
        self.pause()
        self.sprites.draw(self.screen)
        # self.alerts.draw(self.screen)
        pygame.display.flip()

    def exit(self):
        pygame.quit()               
        sys.exit()
 
    def generate_rockets(self): 
        """
        generates rockets in the game
        """
        
        position_for_rocket_x = SCREEN_WIDTH - 34
        position_for_rocket_y = SCREEN_HEIGHT/2
        # Generate rocket warning alert
        if self.flag_rocket and self.current_time - self.last_rocket_time >= self.rocket_time_wait - 2000:
            
            self.alert = Alert(ALERT_PATH, position_for_rocket_x, position_for_rocket_y)
            self.flag_rocket = False
            self.alerts.add(self.alert)
            self.sprites.add(self.alert)         
        
        # Generate rockets
        if self.current_time - self.last_rocket_time >= self.rocket_time_wait -10 and self.flag_rocket == False and self.alerts in self.sprites:
            self.last_rocket_time = self.current_time
            rocket = Rocket(ROCKET_PATH, ROCKET_SIZE, (position_for_rocket_x, self.alert.rect.y + 30), self.background_scroll)  
            self.sound2.play()
            self.alert.kill()
            self.rockets.add(rocket)
            self.sprites.add(rocket)
            self.flag_rocket = True
            self.flag_rocket_warning = True
        # Adjust rocket warning alert position
        if len(self.alerts) > 0:
            if not self.current_time - self.last_rocket_time >= self.rocket_time_wait - 800:         
                self.alert.rect.y = self.barry.rect.y 
            elif self.flag_rocket_warning == True:
                pygame.mixer.find_channel(True).play(self.sound)
                self.flag_rocket_warning = False
    

    def generate_enemies(self, max_quantity):     
        """
        generates enemies in the game
        """
        quantity = random.randrange(1, max_quantity)
        
        if len(self.enemies) == 0:
              if self.current_time - self.last_enemie >= ENEMY_TIME_WAIT:  # Check if 10 seconds have passed
                self.last_enemie = self.current_time
                for i in range(quantity):
                    x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH + 150)
                    y = SCREEN_HEIGHT - FLOOR
                    enemy = Player(x, y, SOLDIERS, self.enemy_lives, self.background_scroll, BULLET_SOUND, JUMPING_PATH_BARRY, DEATH_PATH_BARRY, "enemy")
                    self.enemies.add(enemy)                
                    self.sprites.add(enemy)     
                    
    
    def generate_zapper(self):
        """
        generates zappers in the game
        """
        if self.current_time - self.last_zapper_time >= ZAPPER_TIME_WAIT:
            x = SCREEN_WIDTH + 50
            y = random.randrange(0 + ROOF + 80, SCREEN_HEIGHT - FLOOR - 80)
            self.last_zapper_time = self.current_time
            zapper = RotatingTrap(x, y, self.background_scroll, ZAPPERS_LIST, ZAPPERS1_LIST, ZAPPERS2_LIST, ZAPPERS3_LIST)
            self.sprites.add(zapper)
            self.zappers.add(zapper)
            
    def generate_laser(self):
        """
    Generates lasers in the game.

    Steps:
    1. Determine the random time interval and quantity for laser generation.
    2. Check if lasers need to be generated.
    3. Generate lasers based on the determined quantity and positions.
    4. Handle the end of the laser.
    """
        quantity = random.randrange(2, 5)
        
        if self.current_time - self.last_laser_time >= LASER_TIME_WAIT - 4000:
            self.laser_flag = True
            for alert in self.alerts:
                alert.kill()
            if self.zappers not in self.sprites and self.rockets not in self.sprites and self.alerts not in self.sprites:
                # self.alerts.clear()
                if self.current_time - self.last_laser_time >= LASER_TIME_WAIT:
                    for i in range(quantity):
                        x = SCREEN_WIDTH // 2
                        match quantity:
                            case 1:
                                
                                x = SCREEN_WIDTH // 2
                                
                                y = random.randrange(0 + ROOF, SCREEN_HEIGHT - FLOOR - 100)
                            case 2:
                                x = SCREEN_WIDTH // 2
                                if i == 0:
                                    y = ROOF + 30 + LASER_HEIGHT
                                else:
                                    y = ROOF + LASER_HEIGHT * 5 + FLOOR
                            case 3:
                                x = SCREEN_WIDTH // 2
                                if i == 0:
                                    y = ROOF + 30
                                elif i == 1:
                                    y = ROOF + 30 + LASER_HEIGHT
                                else:
                                    y = ROOF + LASER_HEIGHT * 5 + FLOOR
                            case 4:
                                x = SCREEN_WIDTH // 2
                                if i == 0:
                                    y = ROOF + 30
                                elif i == 1:
                                    y = ROOF + 30 + LASER_HEIGHT
                                elif i == 2:
                                    y = ROOF + 30 + LASER_HEIGHT*4
                                else:
                                    y = ROOF + LASER_HEIGHT*5 + FLOOR

    
                        self.last_laser_time = self.current_time
                        laser = Laser(x, y, LASER_FIRE, LASERS_CHARGE, LASER_INACTIVE, LASER_INACTIVE_SOUND, LASER_FIRE_SOUND)
                        self.sprites.add(laser)
                        self.lasers.add(laser)  
                        laser.charge = True
        
        if len(self.lasers.sprites()) == 0 and self.current_time - self.last_laser_time <= LASER_TIME_WAIT - 4000:
            self.laser_flag = False
            
        for laser in self.lasers:
            if laser.laser_ended == True:
                laser.laser_ended = False
                self.last_rocket_time = self.current_time
                self.last_zapper_time = self.current_time
                self.flag_rocket = True
                laser.kill()
    
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE,BACKDROP_ENTRY, BACKGROUND_IMG, BARRYS, BACKGROUND_MUSIC, JETPACK_PLAIN_START_SOUND, JETPACK_PLAIN_STOP_SOUND, JETPACK_PLAIN_FIRE_SOUND, LAND_METAL_SOUND, START_IMG, EXIT_IMG, MENU_BUTTON, PAUSE_IMG, UNPAUSE_BUTTON, OPTIONS_BUTTON, HARD_BUTTON, BACK_BUTTON)
game.start()
