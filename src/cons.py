import pygame, os 

# Tamaños de la ventana del juego
WINDOW_WIDTH    =   900
WINDOW_HEIGHT   =   600

# Titulo del juego
CAPTION         =   "Space Invaders"

# Path carpeta icons ../include/icons/**
ICONS           =   os.path.dirname(os.path.abspath(__file__)) + "/../include/icons"
SOUNDS          =   os.path.dirname(os.path.abspath(__file__)) + "/../include/sounds"

# Path carpeta fonts ../include/fonts/**
FONTS           =   os.path.dirname(os.path.abspath(__file__)) + "/../include/fonts"

# Path de las naves 
SPACESHIPS_PATH =   ICONS + "/spaceships"
SHIP1           =   SPACESHIPS_PATH + "/spaceship1.png"
SHIP2           =   SPACESHIPS_PATH + "/spaceship2.png"
SHIP3           =   SPACESHIPS_PATH + "/spaceship3.png"
SHIP4           =   SPACESHIPS_PATH + "/spaceship4.png"
SHIP5           =   SPACESHIPS_PATH + "/spaceship5.png"
SHIP6           =   SPACESHIPS_PATH + "/spaceship6.png"
SHIP7           =   SPACESHIPS_PATH + "/spaceship7.png"
SHIP8           =   SPACESHIPS_PATH + "/spaceship8.png"
SHIP9           =   SPACESHIPS_PATH + "/spaceship9.png"

LASER           =   SPACESHIPS_PATH + "/laser.png"

# Path de las imagenes para las teclas que se emplean - Tutorial
QWE_KEY         =   ICONS + "/keys/QWE_KEY.png"
SPACE_KEY       =   ICONS + "/keys/SPACE_KEY.png"
MOUSE1          =   ICONS + "/keys/MOUSE2.png"
MOUSE2          =   ICONS + "/keys/MOUSE3.png"

# Iconos background
BG_PATH         =   ICONS + "/spaceBackground"
BG1             =   BG_PATH + "/s1.png"
BG2             =   BG_PATH + "/s2.png"
BG3             =   BG_PATH + "/s3.png"

# Iconos asteroiddes
ASTEROID1       =   ICONS + "/asteroids/asteroid1.png"
ASTEROID2       =   ICONS + "/asteroids/asteroid2.png"
ASTEROID3       =   ICONS + "/asteroids/asteroid3.png"
ASTEROID4       =   ICONS + "/asteroids/asteroid4.png"
ASTEROID5       =   ICONS + "/asteroids/asteroid5.png"

OBSTACLES       =   [
    'asteroid1','asteroid1',
    'asteroid2','asteroid2',
    'asteroid3','asteroid3',
    'asteroid4','asteroid4',
    'asteroid5'
    ]

# Iconos enemigos
ENEMY1          =   ICONS + "/enemies/enemy1.png"
ENEMY2          =   ICONS + "/enemies/enemy2.png"
ENEMY3          =   ICONS + "/enemies/enemy3.png"

ENEMIES         =   ['enemy1','enemy2','enemy2']

# Icono del juego
ICON            =   ICONS + "/icon.png"
ICON2           =   ICONS + "/icon2.png"

# Font del juego
pygame.font.init()
RETRO_FONT_PATH =   FONTS + "/retro_gaming/RetroGaming.ttf"
retro_font_mini =   pygame.font.Font(RETRO_FONT_PATH,10)
retro_font      =   pygame.font.Font(RETRO_FONT_PATH,16)
retro_font_btn  =   pygame.font.Font(RETRO_FONT_PATH,36)
retro_font_title=   pygame.font.Font(RETRO_FONT_PATH,48)

class Fonts():
    def __init__(self):
        self.retro_font_mini= retro_font_mini
        self.retro_font     = retro_font
        self.retro_font_btn = retro_font_btn
        self.retro_font_title=retro_font_title

# Modos
SELECT_MODE         =   0
LEVEL1              =   1
END_OF_GAME         =   -1

# Colores
INIT_ALPHA      =   [75,75,75,150]
BLACK           =   [0,0,0]
SOFT_BLACK      =   [25,25,25]
WHITE           =   [255,255,255]
GREY            =   [175,175,175]
LIGHT_GREY      =   [195,195,195]
SOFT_LIGHT      =   [225,225,225]
YELLOW          =   [229,190,1]
BLUE            =   [62,95,138]


class loc_params:
    def __init__(self,left,top,width,height):
        self.left   = left
        self.top    = top
        self.width  = width
        self.height = height

# Parámetros de los botones 
BTN_START_LOC   =   loc_params(325,170,250,50)
BTN_TUTORIAL_LOC=   loc_params(325,240,250,50)
BTN_SETTINGS_LOC=   loc_params(325,310,250,50)
BTN_CREDITS_LOC =   loc_params(325,370,250,50)
BTN_GO_BACK     =   loc_params(830,50, 30, 30)

BTN_SELECT_SPACESHIP = loc_params(375,300,150,150)

BTN_S1          =   loc_params(230,120,110,110)
BTN_S2          =   loc_params(405,120,110,110)
BTN_S3          =   loc_params(580,120,110,110)

BTN_S4          =   loc_params(230,270,110,110)
BTN_S5          =   loc_params(405,270,110,110)
BTN_S6          =   loc_params(580,270,110,110)

BTN_S7          =   loc_params(230,420,110,110)
BTN_S8          =   loc_params(405,420,110,110)
BTN_S9          =   loc_params(580,420,110,110)

# Parámetros de los sliders 
BAR_MUSIC       =   loc_params(325,280,250,10)
SLD_MUSIC       =   loc_params(555,270,20, 30)

BAR_EFFECTS     =   loc_params(325,480,250,10)
SLD_EFFECTS     =   loc_params(555,470,20,30)

