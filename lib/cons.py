import pygame, os 
from lib.widgets import loc_params

# Tamaños de la ventana del juego
WINDOW_WIDTH    =   900
WINDOW_HEIGHT   =   600

# Titulo del juego
CAPTION         =   "Space Invaders"

# Path carpeta icons ../include/icons/**
ICONS           =   os.path.dirname(os.path.abspath(__file__)) + "/../include/icons"

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

#TODO: Aumentar a 920x620 el tamaño de las imagenes de fondo
# Iconos background
BG_PATH         =   ICONS + "/spaceBackground"
BG1             =   BG_PATH + "/s1.png"
BG2             =   BG_PATH + "/s2.png"
BG3             =   BG_PATH + "/s3.png"

# Icono del juego
ICON            =   ICONS + "/icon.png"

# Font del juego
pygame.font.init()
RETRO_FONT_PATH =   FONTS + "/retro_gaming/RetroGaming.ttf"
retro_font      =   pygame.font.Font(RETRO_FONT_PATH,16)
retro_font_btn  =   pygame.font.Font(RETRO_FONT_PATH,36)
retro_font_title=   pygame.font.Font(RETRO_FONT_PATH,48)

# Colores
INIT_ALPHA      =   [75,75,75,150]
BLACK           =   [0,0,0]
SOFT_BLACK      =   [25,25,25]
WHITE           =   [255,255,255]
GREY            =   [175,175,175]
LIGHT_GREY      =   [195,195,195]


# Parámetros de los botones 
BTN_START_LOC   =   loc_params(325,170,250,50)
BTN_TUTORIAL_LOC=   loc_params(325,240,250,50)
BTN_SETTINGS_LOC=   loc_params(325,310,250,50)
BTN_CREDITS_LOC =   loc_params(325,370,250,50)
BTN_GO_BACK     =   loc_params(830,50, 30, 30)