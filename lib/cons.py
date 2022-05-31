import os 

# Tamaños de la ventana del juego
WINDOW_WIDTH    =   900
WINDOW_HEIGHT   =   600

# Titulo del juego
CAPTION         =   "Space Invaders"

# Path carpeta icons ../include/icons/**
ICONS           =   os.path.dirname(os.path.abspath(__file__)) + "\..\include\icons"

# Path de las naves 
SPACESHIPS_PATH =   ICONS + "\spaceships"
SHIP1           =   SPACESHIPS_PATH + "\spaceship1.png"
SHIP2           =   SPACESHIPS_PATH + "\spaceship2.png"
SHIP3           =   SPACESHIPS_PATH + "\spaceship3.png"
SHIP4           =   SPACESHIPS_PATH + "\spaceship4.png"
SHIP5           =   SPACESHIPS_PATH + "\spaceship5.png"
SHIP6           =   SPACESHIPS_PATH + "\spaceship6.png"
SHIP7           =   SPACESHIPS_PATH + "\spaceship7.png"
SHIP8           =   SPACESHIPS_PATH + "\spaceship8.png"
SHIP9           =   SPACESHIPS_PATH + "\spaceship9.png"

#TODO: Aumentar a 920x620 el tamaño de las imagenes de fondo
# Iconos background
BG_PATH         =   ICONS + "\spaceBackground"
BG1             =   BG_PATH + "\s1-2.png"
BG2             =   BG_PATH + "\s2.png"
BG3             =   BG_PATH + "\s3.png"

# Icono del juego
ICON            =   ICONS + "\icon.png"


# Colores
BLACK           =   [0,0,0]
WHITE           =   [255,255,255]
