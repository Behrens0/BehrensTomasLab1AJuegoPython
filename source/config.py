import pygame


#screen sizes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ORIGIN = (0, 0)
FPS = 90
ROOF = 70
FLOOR = 50

# Game Title
TITLE = 'Jetpack Joyride cheap copy'


ROCKET_SPEED = 3

#BARRY
PLAYER_SIZE = (45, 40)
BARRY_SPEED = 2
BARRY_LIVES = 1
#bullet
BULLET_PATH = "assets\Jetpack Joyride\Bullet.png"
BULLET_SIZE = (7, 5)
BULLET_SPEED = 10
#enemy
MAX_ENEMIES = 2
ENEMY_SPEED = -1.7
ENEMY_LIVES = 1

ROCKET_TIME_WAIT = 7000
ENEMY_TIME_WAIT = 5000
ZAPPER_TIME_WAIT = 2000
LASER_TIME_WAIT = 35000
DELAY_JETPACK_SOUND = 30
DELAY_RUN = 330

ALERT_SIZE = (45, 45)
ROCKET_SIZE = (50, 32)
EXPLOSION_SIZE = (50, 50)
ZAPPER_SIZE = (70, 105)
LASER_SIZE = (SCREEN_WIDTH, 20)


SCROLL_SPEED = -1.7

#sound
BACKGROUND_MUSIC = "assets\Jetpack Joyride\Jetpack Joyride Theme Extended.mp3"
BULLET_SOUND = "assets/Jetpack Joyride/ricochet-2-101553.mp3"
MISSILE_WARNING_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\missile_warning.wav"
MISSILE_TAKES_OFF = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\missile_launch.wav"
PLAYER_HURT = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\player_hurt_2.wav"
LASER_INACTIVE_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\laser_warning.wav"
LASER_FIRE_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\laser_fire_lp.wav"
LASER_START_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\laser_start.wav"
LASER_STOP_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\laser_stop.wav"
LAND_METAL_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\land_metal.wav"
RUN_METAL_SOUND1 = "assets/Jetpack Joyride/Mobile - Jetpack Joyride - Sound Effects/run_metal_left_1.wav"
RUN_METAL_SOUND2 = "assets/Jetpack Joyride/Mobile - Jetpack Joyride - Sound Effects/run_metal_left_2.wav"
RUN_METAL_SOUND3 = "assets/Jetpack Joyride/Mobile - Jetpack Joyride - Sound Effects/run_metal_left_3.wav"
RUN_METAL_SOUND4 = "assets/Jetpack Joyride/Mobile - Jetpack Joyride - Sound Effects/run_metal_left_4.wav"
JETPACK_PLAIN_FIRE_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\jetpack_plain_lp.wav"
JETPACK_PLAIN_START_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\jetpack_plain_start.wav"
JETPACK_PLAIN_STOP_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\jetpack_plain_stop.wav"
LASER_START_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\laser_start.wav"
LASER_STOP_SOUND = "assets\Jetpack Joyride\Mobile - Jetpack Joyride - Sound Effects\laser_stop.wav"


BACKDROP_ENTRY = "assets\Jetpack Joyride\BackdropEntry2.png"
BACKGROUND_IMG = "assets\Jetpack Joyride\BackdropMain2.png"
BARRYS = ["assets\Jetpack Joyride\BarryRun1Gun.png", "assets\Jetpack Joyride\BarryRun2Gun.png", "assets\Jetpack Joyride\BarryRun3Gun.png"]
ROCKET_PATH = "assets\Jetpack Joyride\Rocket1.png"
JUMPING_PATH_BARRY = "assets\Jetpack Joyride\BarryFlyGun.png"
SOLDIERS = ["assets/enemy/Run/0.png", "assets/enemy/Run/1.png", "assets/enemy/Run/2.png", "assets/enemy/Run/3.png", "assets/enemy/Run/4.png", "assets/enemy/Run/5.png"]
DEATH_PATH_BARRY = "assets\Jetpack Joyride\BarryDead.png"
ALERT_PATH = "assets\Jetpack Joyride\RocketWarning.png"
BULLET_COLLITION = "assets\Jetpack Joyride\BulletCollision1.png"
EXPLOSIONS = ["assets\explosion\exp1.png", "assets\explosion\exp2.png", "assets\explosion\exp3.png", "assets\explosion\exp4.png", "assets\explosion\exp5.png"]




LASERS_CHARGE_PATH = ["assets\Jetpack Joyride\LaserCharge1.png", "assets\Jetpack Joyride\LaserCharge2.png", "assets\Jetpack Joyride\LaserCharge3.png", ]
LASERS_FIRE_PATH = ["assets\Jetpack Joyride\LaserFire1.png", "assets\Jetpack Joyride\LaserFire2.png"]
LASER_INACTIVE = "assets\Jetpack Joyride\LaserInactive.png"


#zappers
ZAPPER_PATH = ["assets\Jetpack Joyride\Zapper1.png", "assets\Jetpack Joyride\Zapper2fifteen.png", "assets\Jetpack Joyride\Zapper3thirty.png", "assets\Jetpack Joyride\Zapper4fortyfive.png", "assets\Jetpack Joyride\Zapper1sixty.png", "assets\Jetpack Joyride\Zapper2seventyfive.png", "assets\Jetpack Joyride\Zapper3ninety.png", "assets\Jetpack Joyride\Zapper4oneofive.png", "assets\Jetpack Joyride\Zapper1onetwenty.png", "assets\Jetpack Joyride\Zapper2onethirtyfive.png", "assets\Jetpack Joyride\Zapper3onefifty.png", "assets\Jetpack Joyride\Zapper4onesixtyfive.png"]
ZAPPERS_1 = ["assets\Jetpack Joyride\Zapper1.png", "assets\Jetpack Joyride\Zapper2.png", "assets\Jetpack Joyride\Zapper3.png", "assets\Jetpack Joyride\Zapper4.png"]
ZAPPERS_2 = ["assets\Jetpack Joyride\Zapper1ninety.png", "assets\Jetpack Joyride\Zapper2ninety.png", "assets\Jetpack Joyride\Zapper3ninety.png", "assets\Jetpack Joyride\Zapper4ninety.png"]
ZAPPERS_3 = ["assets\Jetpack Joyride\Zapper1onetwenty.png", "assets\Jetpack Joyride\Zapper2onetwenty.png", "assets\Jetpack Joyride\Zapper3onetwenty.png", "assets\Jetpack Joyride\Zapper4onetwenty.png"]

#button images
START_IMG = "assets\start_btn.png"
RESTART_IMG = "assets/restart_btn.png"
EXIT_IMG = "assets/button_quit.png"
MENU_BUTTON = "assets\menubutton.png"
PAUSE_IMG = "assets\pausebutton.png"
GAME_OVER_IMG = "assets\Daco_5222304.png"
UNPAUSE_BUTTON = "assets/button_resume.png"
OPTIONS_BUTTON = "assets/button_options.png"
HARD_BUTTON = "assets\hardbutton.png"
BACK_BUTTON = "assets/button_back.png"

def load_images(file_paths: list, size: int)->list:
    """
    Loads and resizes images from the given file paths.

    Args:
        file_paths (list): A list of file paths specifying the locations of the images.
        size (tuple): A tuple specifying the desired width and height of the images.

    Returns:
        list: A list of pygame.Surface objects representing the loaded and resized images.

    """
    file_paths_real = []
    for i in file_paths:
        image = pygame.image.load(i).convert_alpha()
        image = pygame.transform.smoothscale(image, size)
        file_paths_real.append(image)
    
    return file_paths_real
 
#lists   
EXPLOSSIONS_LIST = load_images(EXPLOSIONS, EXPLOSION_SIZE)
ZAPPERS_LIST = load_images(ZAPPER_PATH, ZAPPER_SIZE)
ZAPPERS1_LIST = load_images(ZAPPERS_1, (40, 100))
ZAPPERS2_LIST = load_images(ZAPPERS_2, (100, 50))
ZAPPERS3_LIST = load_images(ZAPPERS_3, (90, 70))
LASER_FIRE = load_images(LASERS_FIRE_PATH, (SCREEN_WIDTH, 60))
LASERS_CHARGE = load_images(LASERS_CHARGE_PATH, (SCREEN_WIDTH, 60))
