# Space Invaders con PYGAME

Esto es una versión del juego _Space Invaders_, popularizado en 1978 por Toshihiro Nishikado, al que se le ha dado un estilo más actual gracias a la librería 
<a href="https://www.pygame.org/docs/" target="_blank">**pygame (versión 2.1.1)**</a>

![Space Inavaders demo](include/icons/Space%20Invaders.gif)

## Índice
1. [Un poco de historia](#un-poco-de-historia)
2. [Descargar](#descargar)
3. [Compilar](#compilar)
4. [Reglas del Juego](#reglas-del-juego)
5. [Controles](#controles)

## Un poco de historia

_Space Invaders_ es un videojuego de arcade diseñado por Toshihiro Nishikado y lanzado al mercado en 1978. En un principio fue fabricado y vendido por Taito Co. en Japón, para posteriormente ser licenciado para producción y distribución en Estados Unidos por Midway Games, división de Bally Technologies. Space Invaders es uno de los primeros juegos matamarcianos. Es uno de los videojuegos más importantes de la historia. Su objetivo es eliminar oleadas de alienígenas con un cañón láser y obtener la mayor cantidad de puntos posible. Para el diseño del juego, Nishikado se inspiró en Breakout, La guerra de los mundos y Star Wars.

Puede ver más de la historia de este juego pinchando <a href="https://es.wikipedia.org/wiki/Space_Invaders" target="_blank"> **aquí** </a>


## Descargar

1. Clone el repositorio desde su bash en la ubicación en la que desea tenerlo:
```
git clone https://github.com/nachoperezzv/SpaceInvaders.git
```

2. Cree el entorno virtual de python para no modificar sus bibliotecas personales y asegurarse de que se descarga la versión correcta de **pygame**. Puede hacerlo de la siguiente forma , estando en la misma ubicación que en el paso anterior:

```
python -m venv SpaceInvaders
```

3. Acceda a la carpeta:
```
cd SpaceInvaders
```

4. Deberá activar su entorno virtual. Por convención, con `venv` debería de disponer de un directorio de nombre `Scripts`. Acceda a el y luego ejecute el siguiente comando. 

    - Desde `cmd`:
    ```
    cd Scripts
    .\activate.bat
    ```

    - Desde `terminal` (linux):
    ```
    source \Scripts\.activate.bat
    ```

5. Una vez ha generado y activado su entorno virtual, instale los paquetes:

```
python install -r requirements.txt
```

6. EXTRA. Es posible que deba de cambiar los nombres de alguna carpeta. Asegurese que el nombre de sus carpetas es `/include` y `/src` (ambos en minúsculas)


## Compilar

Este dato es importante puesto que se debe compilar exclusivamente desde la carpeta `/src`. Si se hace desde la carpeta general de `/SpaceInvaders` provocará un fallo. 

```
C:\Users\user\SpaceInvaders\src\python main.py 
```

## Reglas del Juego

### Marcador
1. El marcador va sumando con el tiempo. Es decir **mientras permanezca vivo** el marcador irá aumentando. 

2. Además de permanecer vivo, si **destruye un ASTEROIDE** se le sumarán **5 puntos** a su marcador.

3. Si **destruye un ENEMIGO** se le sumarán **10 puntos** a su marcador. 

### Movimiento
1. Se le permite moverse horizontalmente, pero no verticalmente

2. Puede controlar el ratón para girar sobre si mismo y orientar su disparo

### Fin del juego
El juego finaliza si un asteroide o enemigo choca contra usted. Los enemigos no pueden disparar. 

## Controles
Al iniciar el juego dispone de una sección de `TUTORIAL` para probar y aprender los controles y una sección `SETTINGS` para poder ajustar el volumen del juego. 

```
Q: Para moverse a la izquierda
W: Para moverse a la derecha
E: Actua como booster y aumenta la velocidad
```

```
SPACE: Para disparar
```

```
MOUSE: Para orientar el disparo
```