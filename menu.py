
import pygame
import pygame_menu
from snake.snakemain import *
from Packman.main import *
from Tetris.main import *
from ursina import Ursina
import threading

def update():
    pass
def runSnake():
    SnakeGame().run()

def runPacman():
    global update
    pygame.quit()
    game=Ursina()
    win=Window()
    update=lambda:win.update()
    game.run()

def runTettris():
    tetris()

def showMenu():
    pygame.init()
    surface = pygame.display.set_mode((720, 480))

    menu = pygame_menu.Menu('VRBProduction', 720, 480,
                            theme=pygame_menu.themes.THEME_SOLARIZED)
    menu.add.button("Snake", runSnake)
    menu.add.button("Tettris", runTettris)
    menu.add.button("Pacman", runPacman)

    menu.mainloop(surface)


threading.Thread(target=showMenu()).start()

